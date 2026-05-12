#!/usr/bin/env python3
"""
sync_agent.py — 防 wiki-ingester.md 项目本地副本与全局副本漂移

源头：``D:/Claude/Ohmybrain/.claude/agents/wiki-ingester.md``（git 跟踪 / 契约权威）
镜像：``~/.claude/agents/wiki-ingester.md``（invocable handle，subagent_type 列表用）

工序：
- 主用户 Edit 项目本地版后，全局副本会漂移
- 漂移后 ``/ingest`` 路径 B 首选调用的是过期契约
- 本脚本检查 SHA-256 并按需镜像

用法::

    python scripts/sync_agent.py            # 检查 + 漂移则 diff 报告
    python scripts/sync_agent.py --check    # 只检查，漂移 exit 1（适合 hook）
    python scripts/sync_agent.py --sync     # 源 → 镜像（项目本地是 source of truth）
"""
from __future__ import annotations

import argparse
import hashlib
import io
import shutil
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

SOURCE = Path(__file__).resolve().parent.parent / ".claude/agents/wiki-ingester.md"
MIRROR = Path.home() / ".claude/agents/wiki-ingester.md"


def sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def short_diff(src: Path, mir: Path) -> str:
    """简短摘要 diff（行数 / 字节数差），不展开完整 unified diff。"""
    s = src.read_text(encoding="utf-8")
    m = mir.read_text(encoding="utf-8") if mir.exists() else ""
    return (
        f"  源 {src}: {len(s.splitlines())} 行 / {len(s.encode('utf-8'))} 字节\n"
        f"  镜像 {mir}: {len(m.splitlines())} 行 / {len(m.encode('utf-8'))} 字节"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="同步 wiki-ingester.md 项目本地 ↔ 全局")
    parser.add_argument("--check", action="store_true", help="只检查，漂移 exit 1（hook 用）")
    parser.add_argument("--sync", action="store_true", help="源 → 镜像（项目本地是 source of truth）")
    args = parser.parse_args()

    if not SOURCE.exists():
        print(f"[错误] 源文件不存在：{SOURCE}", file=sys.stderr)
        return 2

    src_hash = sha256(SOURCE)
    mir_hash = sha256(MIRROR)

    if src_hash == mir_hash:
        print(f"✓ wiki-ingester.md 已同步（{src_hash[:12]}）")
        return 0

    if mir_hash is None:
        print(f"[漂移] 镜像不存在：{MIRROR}", file=sys.stderr)
    else:
        print(f"[漂移] 源 vs 镜像 SHA-256 不一致", file=sys.stderr)
        print(f"  源 hash:   {src_hash[:12]}", file=sys.stderr)
        print(f"  镜像 hash: {mir_hash[:12]}", file=sys.stderr)
    print(short_diff(SOURCE, MIRROR), file=sys.stderr)

    if args.sync:
        MIRROR.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE, MIRROR)
        print(f"✓ 已镜像 → {MIRROR}")
        return 0

    if args.check:
        print(
            f"  修复：python scripts/sync_agent.py --sync",
            file=sys.stderr,
        )
        return 1

    # 默认：报告 + 修复指引（exit 0，不阻断）
    print("\n手动修复：python scripts/sync_agent.py --sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
