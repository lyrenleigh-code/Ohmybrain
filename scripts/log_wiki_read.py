#!/usr/bin/env python3
"""
log_wiki_read.py — PostToolUse hook（静默型，恒 exit 0）

把「wiki 页被读取」事件 append 到 `.usage/wiki_reads.jsonl`（Hub 根，gitignored）。
动机：AI 记忆系统设计框架 I4「读取即投票」——Hub 一直只有写入侧记录（log.md），
没有读取侧记录，审计只能用 query/promote 条目数当粗替身。本 hook 是该缺口的笨版本：
原始事件 append-only（I1 冷层），聚合由 `wiki_usage.py` 事后做（留存看效用）。

记录范围：
- Read 工具：file_path 命中 `wiki/<sub>/<slug>.md` 或 `wiki/{index,log}.md`
- Bash 工具：命令字符串中出现的同类路径；verb 字段 = write（python/tee/sed -i/重定向）
  或命令首词，报表侧据此把写作触碰与纯读分列
每条：ts / tool / verb / session / project（wiki 所属目录名）/ page / sub / slug

覆盖 D:/Claude 下所有项目的 wiki/（project 字段区分），报表默认只看 Hub。
测试可用环境变量 WIKI_USAGE_FILE 覆盖落盘路径。
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BS = chr(92)  # 反斜杠常量：源码里不写双反斜杠（Bash heredoc 会折叠）
HUB_ROOT = Path(__file__).resolve().parent.parent
USAGE_FILE = Path(os.environ.get("WIKI_USAGE_FILE") or HUB_ROOT / ".usage" / "wiki_reads.jsonl")

# 前缀（可含盘符）+ wiki/ + 可选子目录 + slug（允许中文）+ .md
PAGE_RE = re.compile(r"((?:[A-Za-z]:)?[\w./\u4e00-\u9fff-]*?)wiki/(?:([\w-]+)/)?([\w\u4e00-\u9fff-]+)\.md")
WRITE_RE = re.compile(r"(^|[;&|]\s*)(python3?|tee|cp|mv|rm)\b|sed\s+-i|>\s*[\w./-]*wiki/")


def norm(p: str) -> str:
    return p.replace(BS, "/")


def classify(command: str) -> str:
    if WRITE_RE.search(command):
        return "write"
    return (command.strip().split() or [""])[0][:20]


def find_pages(text: str, cwd: str) -> list[dict]:
    out: list[dict] = []
    seen: set[str] = set()
    for m in PAGE_RE.finditer(norm(text)):
        prefix, sub, slug = m.groups()
        if not sub and slug not in ("index", "log"):
            continue
        page = f"wiki/{sub}/{slug}.md" if sub else f"wiki/{slug}.md"
        prefix = prefix.rstrip("/")
        if prefix and prefix not in (".", ".."):
            project = prefix.split("/")[-1]
        else:
            project = Path(norm(cwd)).name if cwd else ""
        key = f"{project}:{page}"
        if key in seen:
            continue
        seen.add(key)
        out.append({"project": project, "page": page, "sub": sub or "", "slug": slug})
    return out


def main() -> int:
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        return 0
    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}
    cwd = data.get("cwd", "") or os.getcwd()
    if tool == "Read":
        text, verb = inp.get("file_path", ""), "read"
    elif tool == "Bash":
        text = inp.get("command", "")
        verb = classify(norm(text))
    else:
        return 0
    pages = find_pages(text, cwd)
    if not pages:
        return 0
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    session = (data.get("session_id") or "")[:8]
    try:
        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with USAGE_FILE.open("a", encoding="utf-8") as f:
            for p in pages:
                row = {"ts": ts, "tool": tool, "verb": verb, "session": session, **p}
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    except OSError:
        pass  # 记录失败不影响主流程
    return 0


if __name__ == "__main__":
    sys.exit(main())
