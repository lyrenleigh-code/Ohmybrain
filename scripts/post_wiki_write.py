#!/usr/bin/env python3
"""
PostToolUse hook: wiki/ 下的文件被 Write/Edit 后自动 lint。

协议:
- stdin 读 Claude Code 传入的 JSON, 形如:
    {"tool_name": "Write", "tool_input": {"file_path": "..."}, ...}
- 仅对路径含 `wiki/` 的文件生效
- 非阻断: lint 失败也只 stderr 提示, exit 0
"""
import io
import json
import subprocess
import sys

sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

if "wiki/" not in path:
    sys.exit(0)

# 仅对 .md 文件跑 lint
if not path.endswith(".md"):
    sys.exit(0)

result = subprocess.run(
    [sys.executable, "scripts/lint_wiki.py"],
    capture_output=True, text=True, encoding="utf-8",
)

if result.returncode != 0:
    print(
        f"[lint_wiki 未通过] 请修复以下问题:\n{result.stdout}{result.stderr}",
        file=sys.stderr,
    )

sys.exit(0)
