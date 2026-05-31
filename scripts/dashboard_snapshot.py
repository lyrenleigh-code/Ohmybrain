#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dashboard_snapshot.py — Ohmybrain 生态规模快照生成器

用途
----
统计 Ohmybrain Hub 与全局 ~/.claude 资源的规模，输出一段 markdown 表到 stdout，
用于手动对齐 wiki/topics/ecosystem-dashboard.md 的「Hub 内部规模快照」章节。

覆盖统计
--------
  - wiki 各子目录 *.md 页数 + 根文件 (index/log) + 总计
  - scripts/*.py 数量
  - ~/.claude/skills/ 含 SKILL.md 的目录数（本地两层之「本地」层；注入后 90+ 需人工标注）
  - ~/.claude/agents/*.md 数量
  - ~/.claude/rules/ 目录数
  - ~/.claude/projects/D--Claude/memory/ 各前缀类型文件数（user/feedback/project/reference）

用法
----
  python scripts/dashboard_snapshot.py

  在 Ohmybrain 仓根目录或其任意子目录下运行均可（脚本自动向上定位 wiki/ 锚点）。
  将 stdout 输出替换 ecosystem-dashboard.md 的「Hub 内部规模快照」表后，再手动核对
  「当前焦点」session 锚点（脚本不解析 memory 内容，仅统计文件数）。

约束：纯标准库，pathlib 跨平台（Windows 路径友好）。
"""

from __future__ import annotations

import sys
from pathlib import Path

# wiki 子目录展示顺序（与 dashboard 页一致）
WIKI_SUBDIRS = [
    "concepts",
    "entities",
    "architecture",
    "topics",
    "explorations",
    "source-summaries",
    "mcp-entities",
    "comparisons",
]

# memory 文件名前缀 → 类型标签
MEMORY_PREFIXES = ["user", "feedback", "project", "reference"]


def find_hub_root(start: Path) -> Path | None:
    """从 start 向上查找含 wiki/ 与 scripts/ 的 Ohmybrain 仓根。"""
    for cur in [start, *start.parents]:
        if (cur / "wiki").is_dir() and (cur / "scripts").is_dir():
            return cur
    return None


def count_md(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    return sum(1 for _ in directory.glob("*.md"))


def count_glob(directory: Path, pattern: str) -> int:
    if not directory.is_dir():
        return 0
    return sum(1 for _ in directory.glob(pattern))


def count_wiki(hub_root: Path) -> tuple[dict[str, int], int, int, int]:
    """返回 (各子目录页数, 内容页合计, 根文件数, 总文件数)。"""
    wiki = hub_root / "wiki"
    per_dir = {sub: count_md(wiki / sub) for sub in WIKI_SUBDIRS}
    content_total = sum(per_dir.values())
    root_files = count_md(wiki)  # 根级 index.md / log.md
    grand_total = content_total + root_files
    return per_dir, content_total, root_files, grand_total


def count_skills(claude_root: Path) -> tuple[int, int]:
    """返回 (skill 目录数, 含 SKILL.md 的目录数)。"""
    skills_dir = claude_root / "skills"
    if not skills_dir.is_dir():
        return 0, 0
    dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
    with_skill = sum(1 for d in dirs if (d / "SKILL.md").is_file())
    return len(dirs), with_skill


def count_agents(claude_root: Path) -> int:
    return count_glob(claude_root / "agents", "*.md")


def count_rules(claude_root: Path) -> int:
    rules_dir = claude_root / "rules"
    if not rules_dir.is_dir():
        return 0
    return sum(1 for d in rules_dir.iterdir() if d.is_dir())


def count_memory(claude_root: Path) -> tuple[dict[str, int], int]:
    """返回 (各前缀类型文件数, 总数)；不含 MEMORY.md 索引本身。"""
    mem_dir = claude_root / "projects" / "D--Claude" / "memory"
    counts = {p: 0 for p in MEMORY_PREFIXES}
    other = 0
    total = 0
    if not mem_dir.is_dir():
        return counts, 0
    for f in mem_dir.glob("*.md"):
        if f.name == "MEMORY.md":
            continue
        total += 1
        matched = False
        for prefix in MEMORY_PREFIXES:
            if f.name.startswith(prefix + "_") or f.name == prefix + ".md":
                counts[prefix] += 1
                matched = True
                break
        if not matched:
            other += 1
    if other:
        counts["other"] = other
    return counts, total


def render(hub_root: Path, claude_root: Path) -> str:
    per_dir, content_total, root_files, wiki_total = count_wiki(hub_root)
    scripts_n = count_glob(hub_root / "scripts", "*.py")
    skill_dirs, skill_with_md = count_skills(claude_root)
    agents_n = count_agents(claude_root)
    rules_n = count_rules(claude_root)
    mem_counts, mem_total = count_memory(claude_root)

    wiki_breakdown = " + ".join(
        f"{per_dir[s]} {s}" for s in WIKI_SUBDIRS
    )
    mem_breakdown = " / ".join(
        f"{k} {v}" for k, v in mem_counts.items() if v
    )

    lines = [
        "| 指标 | 数值 | 说明 |",
        "|------|------|------|",
        f"| wiki 内容页 | **{content_total}** | {wiki_breakdown} |",
        f"| wiki 总文件 | **{wiki_total}** | {content_total} 内容页 + {root_files} 根文件 (index/log) |",
        f"| 自动化脚本 | **{scripts_n}** | `scripts/*.py` 全量 |",
        f"| 全局 skill（本地） | **{skill_with_md}** | `~/.claude/skills/` 含 SKILL.md 的目录（共 {skill_dirs} 目录） |",
        "| 全局 skill（注入后可见） | **90+** | 本地叠加 `ecc:*` plugin / marketplace 注入（人工标注，脚本不统计） |",
        f"| 全局 agent | **{agents_n}** | `~/.claude/agents/*.md` |",
        f"| rules 目录 | **{rules_n}** | `~/.claude/rules/` 下子目录 |",
        f"| Memory 条目 | **{mem_total}** | {mem_breakdown} |",
        "| MCP servers | **6** | context7 / exa / github / memory / playwright / sequential-thinking（人工标注） |",
    ]
    return "\n".join(lines)


def main() -> int:
    hub_root = find_hub_root(Path(__file__).resolve().parent)
    if hub_root is None:
        hub_root = find_hub_root(Path.cwd())
    if hub_root is None:
        print("ERROR: 未找到 Ohmybrain 仓根（含 wiki/ 与 scripts/）", file=sys.stderr)
        return 1

    claude_root = Path.home() / ".claude"
    if not claude_root.is_dir():
        print(f"WARN: ~/.claude 不存在（{claude_root}），全局资源计数将为 0", file=sys.stderr)

    print(f"<!-- Hub 内部规模快照：由 dashboard_snapshot.py 生成 | hub={hub_root} -->")
    print(render(hub_root, claude_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
