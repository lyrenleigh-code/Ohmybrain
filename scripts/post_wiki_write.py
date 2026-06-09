#!/usr/bin/env python3
"""
PostToolUse hook: Ohmybrain wiki/ 下的文件被 Write/Edit 后自动 lint。

协议:
- stdin 读 Claude Code 传入的 JSON, 形如:
    {"tool_name": "Write", "tool_input": {"file_path": "..."}, ...}
- 仅对 **Ohmybrain wiki/** 下的 .md 文件生效（按 __file__ 定位 Hub 根，cwd 无关；
  避免在会话根 = D:/Claude 时把其他项目的 wiki/ 误判或用错 cwd 跑 lint）
- 非阻断: lint 失败也只 stderr 提示, exit 0
"""
import io
import json
import subprocess
import sys
from pathlib import Path

sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent  # Ohmybrain 根
ROOT_STR = str(ROOT).replace("\\", "/")

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

# 仅对 Ohmybrain wiki/ 下的 .md 生效（绝对路径或含 /Ohmybrain/wiki/ 的路径）
in_hub_wiki = path.startswith(ROOT_STR + "/wiki/") or "/Ohmybrain/wiki/" in path
if not in_hub_wiki or not path.endswith(".md"):
    sys.exit(0)

result = subprocess.run(
    [sys.executable, str(ROOT / "scripts" / "lint_wiki.py")],
    cwd=str(ROOT),
    capture_output=True, text=True, encoding="utf-8",
)

if result.returncode != 0:
    print(
        f"[lint_wiki 未通过] 请修复以下问题:\n{result.stdout}{result.stderr}",
        file=sys.stderr,
    )

sys.exit(0)
