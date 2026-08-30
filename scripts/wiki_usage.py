#!/usr/bin/env python3
"""
wiki_usage.py — 聚合 `.usage/wiki_reads.jsonl`（log_wiki_read.py 产出）成审计可消费的读取报表。

用法：
  python scripts/wiki_usage.py                     # 近 90 天，Hub 页面
  python scripts/wiki_usage.py --days 30 --top 20
  python scripts/wiki_usage.py --project UWAcomm   # 看下游项目 wiki（不列「从未被读」）
  python scripts/wiki_usage.py --file <jsonl>      # 测试用

口径（AI 记忆系统设计框架 I4「读取即投票」笨版本）：
- 同一 session 内同一页多次读只算 1 票（去重键 session+page）
- 「查询入口」= index.md 被读的 session 数（llm-wiki 三层协议 Step 1）
- 「写作触碰」= verb 为 write 的事件，单列不计票
- 「从未被读」= wiki 内容页集合 − 记录期内被读集合（自记录起算，起始日随报表打印；mcp-entities 投影页不计）
审计裁 🕸️ / 去索引候选时，用本报表替代「只看 mtime」。
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HUB_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILE = HUB_ROOT / ".usage" / "wiki_reads.jsonl"
SKIP_SUBS = {"mcp-entities"}
ROOT_PAGES = ("wiki/index.md", "wiki/log.md")


def load(path: Path, days: int) -> list[dict]:
    if not path.exists():
        return []
    since = datetime.now() - timedelta(days=days)
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
            if datetime.fromisoformat(r["ts"]) >= since:
                rows.append(r)
        except (ValueError, KeyError):
            continue
    return rows


def content_pages(wiki: Path) -> set[str]:
    pages: set[str] = set()
    for d in wiki.iterdir():
        if d.is_dir() and d.name not in SKIP_SUBS:
            pages.update(f"wiki/{d.name}/{f.name}" for f in d.glob("*.md"))
    return pages


def report(rows: list[dict], project: str, top: int, days: int, wiki: Path | None) -> str:
    rows = [r for r in rows if r.get("project") == project]
    reads = [r for r in rows if r.get("verb") != "write"]
    writes = [r for r in rows if r.get("verb") == "write"]
    votes: dict[str, set[str]] = defaultdict(set)
    last: dict[str, str] = {}
    for r in reads:
        votes[r["page"]].add(r.get("session", ""))
        last[r["page"]] = max(last.get(r["page"], ""), r["ts"][:10])
    sessions = {r.get("session", "") for r in rows}
    first_ts = min((r["ts"][:10] for r in rows), default="—")
    n_index = len(votes.get(ROOT_PAGES[0], set()))
    n_log = len(votes.get(ROOT_PAGES[1], set()))

    out = [f"## Wiki 读取报表 · {project} · 近 {days} 天（记录起始 {first_ts}）", ""]
    out.append(f"- 事件：读 {len(reads)} / 写作触碰 {len(writes)}；session {len(sessions)} 个")
    out.append(f"- **查询入口**（index.md 被读 session 数）：{n_index}")
    out.append(f"- log.md 被读 session 数：{n_log}")
    out.append("")
    ranked = sorted(((len(s), p) for p, s in votes.items() if p not in ROOT_PAGES), reverse=True)
    out.append("| # | 页面 | 读取 session 数 | 最近读取 |")
    out.append("|---|---|---|---|")
    for i, (n, p) in enumerate(ranked[:top], 1):
        out.append(f"| {i} | `{p}` | {n} | {last[p]} |")
    if not ranked:
        out.append("| — | （无内容页读取记录） | | |")
    if wiki and wiki.is_dir():
        allp = content_pages(wiki)
        never = sorted(allp - set(votes))
        out.append("")
        out.append(f"**记录期内从未被读的内容页：{len(never)} / {len(allp)}**（去索引候选，需结合创建日期判断）")
        out.extend(f"- `{p}`" for p in never[:top])
        if len(never) > top:
            out.append(f"- … 另 {len(never) - top} 页")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", type=Path, default=DEFAULT_FILE)
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--project", default=HUB_ROOT.name)
    args = ap.parse_args()
    rows = load(args.file, args.days)
    if not rows:
        print(f"（无记录：{args.file} 不存在或近 {args.days} 天为空）")
        return 0
    wiki = HUB_ROOT / "wiki" if args.project == HUB_ROOT.name else None
    print(report(rows, args.project, args.top, args.days, wiki))
    return 0


if __name__ == "__main__":
    sys.exit(main())
