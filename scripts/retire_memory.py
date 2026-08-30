#!/usr/bin/env python3
"""
retire_memory.py — auto-memory 退役 = 去索引，不销毁（AI 记忆系统设计框架 I1）。

把 `~/.claude/projects/D--Claude/memory/<name>.md` 移入 Hub `raw/memory-retired/`
（append-only 冷层，git 跟踪、backup_push 一并备份），从 `MEMORY.md` 删除索引行，
并在 `raw/memory-retired/INDEX.md` 登记（日期 / 文件 / 原描述 / 退役原因）。
移出 memory 目录是为了同时脱离 Claude Code 的 recall 检索面（留在原目录仍可能被召回）。

用法：
  python scripts/retire_memory.py project_xxx [feedback_yyy ...] --reason "已蒸馏进 concept 页"
  python scripts/retire_memory.py --list
  python scripts/retire_memory.py project_xxx --dry-run
  --mem-dir / --dest 可改路径（其他项目的 memory 目录，或测试）

退役后 CANON 计数变化（memory 总数 / 子类），记得跑 `python scripts/dashboard_snapshot.py --check`
并级联。恢复 = 手动移回 + 在 MEMORY.md 补一行（INDEX.md 保留原描述可直接复用）。
"""
from __future__ import annotations

import argparse
import io
import re
import shutil
import sys
from datetime import date
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

HUB_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MEM = Path.home() / ".claude/projects/D--Claude/memory"
DEFAULT_DEST = HUB_ROOT / "raw" / "memory-retired"
QUOTE = chr(34)
PIPE = chr(124)
INDEX_HEADER = """# 退役 auto-memory 冷层

> 由 `scripts/retire_memory.py` 维护。**去索引不销毁**：文件原样留存、脱离 `MEMORY.md` 与 recall 检索面。
> 本目录**不走 /ingest**（内容已蒸馏或已失效）；需要时按下表回看原文或恢复。

| 退役日期 | 文件 | 原描述 | 退役原因 |
|---|---|---|---|
"""
DESC_RE = re.compile(r"^description:\s*(.+)$", re.M)


def description_of(p: Path) -> str:
    m = DESC_RE.search(p.read_text(encoding="utf-8"))
    return m.group(1).strip().strip(QUOTE) if m else ""


def cell(s: str) -> str:
    return s.replace(PIPE, "/")


def retire_one(name: str, mem_dir: Path, dest: Path, reason: str, dry: bool) -> bool:
    name = name[:-3] if name.endswith(".md") else name
    src = mem_dir / f"{name}.md"
    if not src.is_file():
        print(f"  ✗ 不存在：{src}")
        return False
    target = dest / f"{name}.md"
    if target.exists():
        target = dest / f"{name}-{date.today():%Y%m%d}.md"
    index = mem_dir / "MEMORY.md"
    lines = index.read_text(encoding="utf-8").split("\n") if index.exists() else []
    kept = [l for l in lines if f"({name}.md)" not in l]
    removed = len(lines) - len(kept)
    desc = description_of(src)
    tag = "[dry] " if dry else ""
    print(f"  {tag}{src.name} → {target}（MEMORY.md 去 {removed} 行）")
    if dry:
        return True
    dest.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(target))
    if removed:
        index.write_text("\n".join(kept), encoding="utf-8", newline="\n")
    idx = dest / "INDEX.md"
    if not idx.exists():
        idx.write_text(INDEX_HEADER, encoding="utf-8", newline="\n")
    with idx.open("a", encoding="utf-8", newline="\n") as f:
        f.write(f"| {date.today()} | `{target.name}` | {cell(desc)} | {cell(reason)} |\n")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*", help="memory 文件名（可不带 .md）")
    ap.add_argument("--reason", default="", help="退役原因（写入 INDEX.md）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true", help="列出已退役条目")
    ap.add_argument("--mem-dir", type=Path, default=DEFAULT_MEM)
    ap.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    args = ap.parse_args()

    if args.list:
        idx = args.dest / "INDEX.md"
        print(idx.read_text(encoding="utf-8") if idx.exists() else "（尚无退役条目）")
        return 0
    if not args.names:
        ap.error("请给出至少一个 memory 名，或用 --list")
    if not args.reason and not args.dry_run:
        ap.error("--reason 必填（退役原因是 provenance 的一部分）")
    print(f"memory 目录：{args.mem_dir}\n冷层目录：{args.dest}")
    ok = sum(retire_one(n, args.mem_dir, args.dest, args.reason, args.dry_run) for n in args.names)
    tail = "" if args.dry_run else "；记得 `python scripts/dashboard_snapshot.py --check` 级联 memory 计数"
    print(f"完成 {ok}/{len(args.names)}{tail}")
    return 0 if ok == len(args.names) else 1


if __name__ == "__main__":
    sys.exit(main())
