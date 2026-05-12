#!/usr/bin/env python3
"""
check_memory_log_gap.py — Stop hook（提醒型，exit 0）

会话结束时检查 auto-memory ``MEMORY.md`` 中带日期条目是否都已沉淀到 Hub ``wiki/log.md``。
缺口存在则 stdout 提示（不阻断，PostToolUse 不连发），无缺口则静默通过。

设计：
- exit 0 + stdout 写提醒（Windows Terminal 友好，不堆 tab）
- 只看"缺口最近日期"是否够近（7 天内）+ 缺口总数
- 决策由用户做，hook 只指路：``python scripts/diff_memory_log.py``
"""
from __future__ import annotations

import io
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MEMORY_INDEX = Path.home() / ".claude/projects/D--Claude/memory/MEMORY.md"
HUB_LOG = Path(__file__).resolve().parent.parent / "wiki/log.md"

INDEX_LINE_RE = re.compile(r"^- \[(.+?)\]\((.+?)\) — (.+)$")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
# 兼容单日 `## [YYYY-MM-DD]` 与日期范围 `## [YYYY-MM-DD ~ YYYY-MM-DD]`
LOG_HEADER_RE = re.compile(r"## \[(\d{4}-\d{2}-\d{2})(?:\s*~\s*(\d{4}-\d{2}-\d{2}))?\]")

RECENT_DAYS = 7  # 缺口在 N 天内才视为"急需提醒"


def memory_dated_entries() -> set[str]:
    if not MEMORY_INDEX.exists():
        return set()
    dates: set[str] = set()
    for line in MEMORY_INDEX.read_text(encoding="utf-8").splitlines():
        m = INDEX_LINE_RE.match(line)
        if not m:
            continue
        _, filename, desc = m.groups()
        date_match = DATE_RE.search(desc) or DATE_RE.search(filename)
        if date_match:
            dates.add(date_match.group(1))
    return dates


def log_dates() -> set[str]:
    if not HUB_LOG.exists():
        return set()
    text = HUB_LOG.read_text(encoding="utf-8")
    dates: set[str] = set()
    for start, end in LOG_HEADER_RE.findall(text):
        if not end:
            dates.add(start)
            continue
        d0 = datetime.strptime(start, "%Y-%m-%d").date()
        d1 = datetime.strptime(end, "%Y-%m-%d").date()
        cur = d0
        while cur <= d1:
            dates.add(cur.strftime("%Y-%m-%d"))
            cur += timedelta(days=1)
    return dates


def main() -> int:
    mem = memory_dated_entries()
    log = log_dates()
    missing = sorted(mem - log)

    if not missing:
        sys.exit(0)

    today = date.today()
    cutoff = today - timedelta(days=RECENT_DAYS)
    recent = [d for d in missing if datetime.strptime(d, "%Y-%m-%d").date() >= cutoff]

    if not recent:
        sys.exit(0)

    print(
        f"[memory→Hub] {len(missing)} 个日期 memory 有但 wiki/log.md 缺，"
        f"其中 {len(recent)} 个在最近 {RECENT_DAYS} 天内（最近：{recent[-1]}）"
    )
    print(
        f"  详情：python scripts/diff_memory_log.py --out draft/log-draft-{today}.md"
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
