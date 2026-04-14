#!/usr/bin/env python3
"""
SessionStart hook: 向新会话注入 wiki 最近活动 + 项目列表。

stdout 内容会进入 Claude 上下文。保持简短。
"""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "wiki" / "log.md"
PROJECTS = ROOT / "projects"


def recent_log_entries(n: int = 3) -> list[str]:
    """返回 log.md 最近 n 条 `## [日期]` 开头的条目标题行."""
    if not LOG.exists():
        return []
    entries: list[str] = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("## [") and len(entries) < n:
            entries.append(line[3:])  # strip "## "
    return entries


def list_projects() -> list[str]:
    if not PROJECTS.exists():
        return []
    return sorted(p.name for p in PROJECTS.iterdir() if p.is_dir())


def main() -> None:
    print("## Ohmybrain Hub 当前状态")
    print()

    entries = recent_log_entries()
    if entries:
        print("### wiki 最近变更")
        for e in entries:
            print(f"- {e}")
        print()

    projects = list_projects()
    if projects:
        print(f"### 已注册项目 ({len(projects)})")
        print(f"- {', '.join(projects)}")


if __name__ == "__main__":
    main()
