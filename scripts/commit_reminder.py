#!/usr/bin/env python3
"""
Stop hook: 会话结束时若 wiki/ 有未提交变更, 提示用户 commit/push.

非阻断 (exit 0). 仅 stdout 提醒.
"""
import io
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def changed_wiki_files() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain", "wiki/"],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    changes = changed_wiki_files()
    if not changes:
        sys.exit(0)

    count = len(changes)
    print(f"[reminder] wiki/ 有 {count} 处未提交变更, 考虑:")
    print("  git add wiki/ && git commit -m '...' && git push")


if __name__ == "__main__":
    main()
