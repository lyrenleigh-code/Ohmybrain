#!/usr/bin/env python3
"""
calendar_reminder.py — Stop hook：每日 calendar 日志提醒（节流）

**工作区级 hook**（非 Hub 专属）：会话回合结束时检查 ``D:/Claude/calendar/`` 下
今天的日志（命名惯例 ``YYYY-MM-DD 标题.md``）是否存在；不存在则 stdout 提醒。

非阻断（exit 0）。**节流**：Stop 每轮回复结束都触发，故经 stamp 文件限制为
≥ REMIND_INTERVAL_H 小时最多提醒一次，避免刷屏。

测试钩子：env ``CALENDAR_DIR`` 覆盖日历目录；``CALENDAR_STAMP`` 覆盖 stamp 路径。

注册位置：仅 ``D:/Claude/.claude/settings.json``（会话根）。脚本托管 Hub scripts/。
"""
from __future__ import annotations

import io
import os
import sys
import time
from datetime import date
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

WORKSPACE = Path(__file__).resolve().parent.parent.parent  # D:/Claude（cwd 无关）
CALENDAR_DIR = Path(os.environ.get("CALENDAR_DIR", WORKSPACE / "calendar"))
STAMP = Path(os.environ.get("CALENDAR_STAMP", WORKSPACE / ".claude" / ".calendar_reminder.stamp"))
REMIND_INTERVAL_H = 4  # 同一缺口最多每 4 小时提醒一次


def throttled() -> bool:
    try:
        if STAMP.exists():
            return (time.time() - STAMP.stat().st_mtime) < REMIND_INTERVAL_H * 3600
    except OSError:
        pass
    return False


def main() -> None:
    if not CALENDAR_DIR.is_dir():
        sys.exit(0)  # 无 calendar 目录的环境直接放行

    today = date.today().isoformat()
    if any(CALENDAR_DIR.glob(f"{today}*.md")):
        sys.exit(0)  # 今日日志已建

    if throttled():
        sys.exit(0)

    try:
        STAMP.parent.mkdir(parents=True, exist_ok=True)
        STAMP.write_text(today, encoding="utf-8")
    except OSError:
        pass  # stamp 写不进也照常提醒一次

    print(
        f"[reminder] 今日 calendar 日志未建：calendar/{today} <标题>.md "
        f"（命名惯例 YYYY-MM-DD 标题.md；本提醒每 {REMIND_INTERVAL_H}h 至多一次）"
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
