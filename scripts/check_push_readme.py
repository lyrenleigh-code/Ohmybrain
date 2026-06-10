#!/usr/bin/env python3
"""
check_push_readme.py — PreToolUse(Bash) hook：git push 前检查 README 是否同步更新

**工作区级 hook**（非 Hub 专属）：拦截 D:/Claude 下任意 git 仓的 push——若本次待
push 的 commit（含同一命令里链式 commit 的暂存/工作区改动）没有动过任何 README*
文件，exit 2 阻断并提示先同步 README；确认无需更新时在命令前加 ``SKIP_README=1 ``
重试即放行。

宽松优先：JSON 解析失败 / 非 push 命令 / 无 upstream / dry-run / 仓不在
D:/Claude 下 / git 调用出错 → 一律 exit 0 放行。

注册位置：仅 ``D:/Claude/.claude/settings.json``（会话根；嵌套项目 settings 不被
加载，见 Hub CLAUDE.md 2026-06-09 注）。脚本本体托管 Hub scripts/ 走 git。
"""
from __future__ import annotations

import io
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

WORKSPACE = Path(__file__).resolve().parent.parent.parent  # D:/Claude（cwd 无关）
ESCAPE_TOKEN = "SKIP_README=1"


def parse_push_segment(command: str) -> list[str] | None:
    """命令按 && ; | 切段，返回首个『git ... push』段的 token 列表；无则 None。"""
    for segment in re.split(r"&&|;|\|", command):
        try:
            tokens = shlex.split(segment.strip())
        except ValueError:
            continue
        if not tokens:
            continue
        head = Path(tokens[0]).name.lower()
        if head in ("git", "git.exe") and "push" in tokens[1:]:
            return tokens
    return None


def repo_dir_from(tokens: list[str], cwd: str) -> Path:
    """处理 `git -C <path> push`；否则用 hook 注入的 cwd。"""
    for i, tok in enumerate(tokens[:-1]):
        if tok == "-C":
            p = Path(tokens[i + 1])
            return p if p.is_absolute() else Path(cwd) / p
    return Path(cwd)


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, encoding="utf-8",
    )


def touches_readme(paths: list[str]) -> bool:
    return any(Path(p).name.lower().startswith("readme") for p in paths if p.strip())


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    if payload.get("tool_name") != "Bash":
        sys.exit(0)
    command = (payload.get("tool_input") or {}).get("command", "")
    if not command or ESCAPE_TOKEN in command:
        sys.exit(0)

    tokens = parse_push_segment(command)
    if tokens is None or "--dry-run" in tokens or "-n" in tokens:
        sys.exit(0)

    repo = repo_dir_from(tokens, payload.get("cwd") or ".")
    try:
        repo = repo.resolve()
        if WORKSPACE.resolve() not in (repo, *repo.parents):
            sys.exit(0)  # 工作区外的仓不管
    except OSError:
        sys.exit(0)

    upstream = git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    if upstream.returncode != 0:
        sys.exit(0)  # 新分支 / 无 upstream，无法判定 outgoing，放行

    ahead = git(repo, "rev-list", "--count", "@{u}..HEAD")
    outgoing = git(repo, "diff", "--name-only", "@{u}..HEAD")
    status = git(repo, "status", "--porcelain")  # 链式 commit+push 时未提交改动也算
    if ahead.returncode != 0 or outgoing.returncode != 0:
        sys.exit(0)

    n_ahead = int(ahead.stdout.strip() or "0")
    pending = [line[3:] for line in status.stdout.splitlines()] if status.returncode == 0 else []
    has_chained_commit = bool(re.search(r"\bgit\b[^|;&]*\bcommit\b", command))
    if n_ahead == 0 and not (has_chained_commit and pending):
        sys.exit(0)  # 没有 outgoing commit，也没有链式 commit 要推

    changed = outgoing.stdout.splitlines() + (pending if has_chained_commit else [])
    if touches_readme(changed):
        sys.exit(0)

    scope = f"{n_ahead} 个 outgoing commit" if n_ahead else "链式 commit 待提交改动"
    print(
        f"[Hook] BLOCKED: 待 push 的 {scope}（仓 {repo.name}）未更新任何 README* 文件。\n"
        f"  请先同步 README 状态再 push；确认本次确实无需更新 README，"
        f"在命令前加 `{ESCAPE_TOKEN} ` 重试即放行。",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
