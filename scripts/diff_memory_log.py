#!/usr/bin/env python3
"""
diff_memory_log.py — 对照 auto-memory MEMORY.md 与 Hub wiki/log.md，找出未沉淀的项目记录

读 ``~/.claude/projects/D--Claude/memory/MEMORY.md`` 的索引行，对照 ``wiki/log.md`` 的日期 header，
按 ``[promote-candidate / log-only / review / skip]`` 分类输出 markdown 报告。

不直接修改 log.md，只产 draft 供用户审核后手工 merge。

用法::

    python scripts/diff_memory_log.py                # stdout
    python scripts/diff_memory_log.py --out draft.md # 写到文件
"""
from __future__ import annotations

import argparse
import io
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MEMORY_INDEX = Path.home() / ".claude/projects/D--Claude/memory/MEMORY.md"
HUB_LOG = Path(__file__).resolve().parent.parent / "wiki/log.md"

INDEX_LINE_RE = re.compile(r"^- \[(.+?)\]\((.+?)\) — (.+)$")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
# 兼容单日 `## [YYYY-MM-DD]` 与日期范围 `## [YYYY-MM-DD ~ YYYY-MM-DD]`
LOG_HEADER_RE = re.compile(r"## \[(\d{4}-\d{2}-\d{2})(?:\s*~\s*(\d{4}-\d{2}-\d{2}))?\]")


@dataclass(frozen=True)
class MemoryEntry:
    filename: str
    title: str
    description: str
    date: str | None  # 首个日期（展示用）
    dates: tuple[str, ...]  # 全部日期（缺口检测用，单行可多日）
    action: str


def classify(filename: str, title: str) -> str:
    """根据文件名前缀与标题关键词推断建议动作。"""
    fn = filename.lower()
    t = title.lower()

    if fn.startswith("user_"):
        return "skip"
    if fn.startswith("reference_"):
        return "promote-candidate"
    if fn.startswith("feedback_"):
        keywords = ("workflow", "path", "bug", "tradeoff", "convention", "boundary", "ownership")
        if any(k in t for k in keywords):
            return "promote-candidate"
        return "review"
    if "session" in fn:
        return "skip-or-log-only"
    if fn.startswith("project_") and ("init" in fn or "scope" in fn):
        return "log-only"
    if fn.startswith("project_"):
        return "review"
    return "review"


def parse_memory_index(path: Path) -> list[MemoryEntry]:
    if not path.exists():
        return []
    entries: list[MemoryEntry] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = INDEX_LINE_RE.match(line)
        if not m:
            continue
        title, filename, desc = m.groups()
        # 收集 desc + filename 全部日期（单行可登记多日进展）；首个作展示日期，
        # 全集用于缺口检测——用 findall 而非 search 避免只取首日漏报
        all_dates = tuple(dict.fromkeys(DATE_RE.findall(desc) + DATE_RE.findall(filename)))
        date = all_dates[0] if all_dates else None
        action = classify(filename, title)
        entries.append(MemoryEntry(filename, title, desc, date, all_dates, action))
    return entries


def extract_log_dates(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    dates: set[str] = set()
    for start, end in LOG_HEADER_RE.findall(text):
        if not end:
            dates.add(start)
            continue
        # 范围 header：展开为闭区间内所有日期
        d0 = datetime.strptime(start, "%Y-%m-%d").date()
        d1 = datetime.strptime(end, "%Y-%m-%d").date()
        cur = d0
        while cur <= d1:
            dates.add(cur.strftime("%Y-%m-%d"))
            cur += timedelta(days=1)
    return dates


def render_report(entries: list[MemoryEntry], log_dates: set[str]) -> str:
    out: list[str] = []
    out.append("# Memory → Hub log.md 缺口报告")
    out.append("")
    out.append(f"生成时间：{datetime.now().isoformat(timespec='seconds')}")
    out.append("")

    by_date: dict[str, list[MemoryEntry]] = defaultdict(list)
    no_date: list[MemoryEntry] = []
    for e in entries:
        if e.dates:
            for d in e.dates:  # 多日条目归入每个日期，缺口检测才不漏
                by_date[d].append(e)
        else:
            no_date.append(e)

    dated_count = sum(1 for e in entries if e.dates)
    missing = sorted(d for d in by_date if d not in log_dates)
    aligned = sorted(d for d in by_date if d in log_dates)

    out.append("## 概览")
    out.append("")
    out.append(f"- memory 索引条目总数：**{len(entries)}**")
    out.append(f"- 带日期条目：{dated_count}（无日期：{len(no_date)}）")
    out.append(f"- Hub log.md 已记录日期数：{len(log_dates)}")
    out.append(f"- **缺口日期数**：**{len(missing)}** ← memory 有但 log.md 缺")
    out.append(f"- 已对齐日期数：{len(aligned)}")
    out.append("")

    out.append("## 缺口（按日期倒序，最近的优先处理）")
    out.append("")
    if not missing:
        out.append("（无缺口）")
        out.append("")
    else:
        for date in reversed(missing):
            out.append(f"### {date}")
            out.append("")
            for r in by_date[date]:
                out.append(f"- **[{r.action}]** [{r.title}]({r.filename}) — {r.description}")
            out.append("")

    out.append("## 已对齐日期（参考）")
    out.append("")
    for date in reversed(aligned):
        out.append(f"### {date}")
        for r in by_date[date]:
            out.append(f"- [{r.action}] [{r.title}]({r.filename})")
        out.append("")

    out.append("## 无日期条目（按建议动作分组）")
    out.append("")
    by_action: dict[str, list[MemoryEntry]] = defaultdict(list)
    for r in no_date:
        by_action[r.action].append(r)
    for action in sorted(by_action):
        out.append(f"### [{action}]")
        out.append("")
        for r in by_action[action]:
            out.append(f"- [{r.title}]({r.filename}) — {r.description}")
        out.append("")

    out.append("## 行动指引")
    out.append("")
    out.append("- **promote-candidate** — 含跨项目可复用结论，走 `/promote-answer` 落到 Hub concept/reference")
    out.append("- **log-only** — 项目派生/初始化等事件，加 wiki/log.md entry 即可，不必新建 concept")
    out.append("- **review** — 项目侧 session 记录，主要看是否有结论可抽出")
    out.append("- **skip / skip-or-log-only** — 一般不沉淀（user profile / session snapshot）")
    out.append("")
    out.append("处理后逐条移除本报告对应行，或勾选 `- [x]` 留档。")
    out.append("")

    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="对照 MEMORY.md 与 wiki/log.md 找未沉淀记录")
    parser.add_argument("--out", type=Path, help="写到文件而非 stdout")
    parser.add_argument("--memory", type=Path, default=MEMORY_INDEX, help="MEMORY.md 路径")
    parser.add_argument("--log", type=Path, default=HUB_LOG, help="wiki/log.md 路径")
    args = parser.parse_args()

    if not args.memory.exists():
        print(f"[错误] memory index 不存在：{args.memory}", file=sys.stderr)
        return 1

    entries = parse_memory_index(args.memory)
    log_dates = extract_log_dates(args.log)
    report = render_report(entries, log_dates)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
        print(f"已写入：{args.out}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
