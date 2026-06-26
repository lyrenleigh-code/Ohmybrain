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

import argparse
import io
import re
import sys
from pathlib import Path

# Windows 控制台默认 gbk，wiki 文本含非 gbk 字符 / 输出含符号——统一 UTF-8 stdout，
# 避免作 Stop hook 时 UnicodeEncodeError 崩溃（同 check_memory_log_gap.py 处理）。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# wiki 子目录展示顺序（与 ecosystem-dashboard 表一致）。
# 仅用于「已知分类」的排序；实际统计由 discover_wiki_subdirs 自动发现 wiki/ 下
# 所有子目录——新增分类（如 2026-06-09 的 agents/ workflows/）会自动计入并追加，
# 不再像旧硬编码列表那样静默漏算（避免「新增 wiki 分类后脚本未同步」的部分登记）。
PREFERRED_ORDER = [
    "concepts",
    "entities",
    "architecture",
    "agents",
    "workflows",
    "topics",
    "explorations",
    "source-summaries",
    "mcp-entities",
    "comparisons",
]

# memory 文件名前缀 → 类型标签
MEMORY_PREFIXES = ["user", "feedback", "project", "reference"]

# projects/ 下不计入「活跃项目数」的导航卡（母仓 + 归档 dry-run 导航，非独立业务项目）。
# 派生方式：活跃项目数 = projects/ 导航卡总数 − 本集合中实际存在者。
# 安全性：本集合若过期（未来新增一个非项目导航卡），活跃数会被**高报** →
# --check 报「页面写 N，实跑应为 N+1」LOUD 失配，提示人工把新卡加进本集合；
# 不会像硬编码白名单漏项那样静默**漏算**（与 audit-3 WIKI_SUBDIRS 静默低报相反，方向安全）。
NON_PROJECT_NAV = {
    "ohmybrain-core",  # 母仓 / 模板源，单列「母仓 / Hub」段，不计业务活跃项目
    "usbl-s1",         # USBL S1 autonomous dry-run 归档性质导航页（非独立项目）
}


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


def discover_wiki_subdirs(wiki: Path) -> list[str]:
    """自动发现 wiki/ 下所有子目录。已知分类按 PREFERRED_ORDER 排序，
    未知分类（未来新增）按字母序追加在后，确保不会静默漏算。"""
    if not wiki.is_dir():
        return list(PREFERRED_ORDER)
    actual = {d.name for d in wiki.iterdir() if d.is_dir()}
    ordered = [s for s in PREFERRED_ORDER if s in actual]
    extra = sorted(actual - set(PREFERRED_ORDER))
    return ordered + extra


def count_wiki(hub_root: Path) -> tuple[dict[str, int], int, int, int, list[str]]:
    """返回 (各子目录页数, 内容页合计, 根文件数, 总文件数, 子目录顺序)。"""
    wiki = hub_root / "wiki"
    subdirs = discover_wiki_subdirs(wiki)
    per_dir = {sub: count_md(wiki / sub) for sub in subdirs}
    content_total = sum(per_dir.values())
    root_files = count_md(wiki)  # 根级 index.md / log.md
    grand_total = content_total + root_files
    return per_dir, content_total, root_files, grand_total, subdirs


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


def count_nav_cards(hub_root: Path) -> int:
    """projects/ 下导航卡（子目录）总数。"""
    proj = hub_root / "projects"
    if not proj.is_dir():
        return 0
    return sum(1 for d in proj.iterdir() if d.is_dir())


def count_active_projects(hub_root: Path) -> int:
    """活跃项目数 = projects/ 导航卡 − NON_PROJECT_NAV 中实际存在者。
    （papers 无导航卡故天然不计；第三方 vendored ppt-master 无导航卡亦不计。）"""
    proj = hub_root / "projects"
    if not proj.is_dir():
        return 0
    return sum(
        1 for d in proj.iterdir() if d.is_dir() and d.name not in NON_PROJECT_NAV
    )


def count_docprocess_projects(hub_root: Path) -> int:
    """DocProcess 子项目数 = conventions §9 私人项目表中 `| `DocProcess/...` 行数。
    conventions §9 是 DocProcess 项目的权威枚举（每个登记项目一行），用作 ground-truth
    校验 system-overview「DocProcess×N」token。简单行前缀计数，格式变则返回 0 → --check
    失配 LOUD（不静默）。"""
    f = hub_root / "wiki" / "architecture" / "conventions.md"
    if not f.is_file():
        return 0
    return len(re.findall(r"(?m)^\| `DocProcess/", f.read_text(encoding="utf-8")))


def render(hub_root: Path, claude_root: Path) -> str:
    per_dir, content_total, root_files, wiki_total, subdirs = count_wiki(hub_root)
    scripts_n = count_glob(hub_root / "scripts", "*.py")
    skill_dirs, skill_with_md = count_skills(claude_root)
    agents_n = count_agents(claude_root)
    rules_n = count_rules(claude_root)
    mem_counts, mem_total = count_memory(claude_root)

    wiki_breakdown = " + ".join(
        f"{per_dir[s]} {s}" for s in subdirs
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


# ---------------------------------------------------------------------------
# CANON 计数校验（--check）
# ---------------------------------------------------------------------------
# 「部分登记」反模式：CANON 计数（memory / scripts / wiki 页数等）在多处 wiki
# 现态页冗余冗写，某处 bump 后漏级联到其他处 → 反复 stale（2026-05-31 / 06-09×3
# / 06-10 / 06-14 自检连续命中）。lint_wiki.py 只查孤儿页不查计数，是结构性盲区。
#
# 本注册表把「哪个页面的哪个数字应等于哪个实跑值」显式编码：每条 = (相对 hub 根的
# 路径（wiki/* 或 README.md）, 单捕获组正则, ground-truth 键, 标签)。--check 逐条
# read+findall，捕获数 ≠ 实跑值即报 stale；正则未命中即报「模式失配」（页面措辞变了）。
#
# 只扫现态页（wiki + README，**不扫 log.md**），故历史 log 里的旧计数（如 "78→79"）
# 不会误报。新增 CANON 冗写点时在此追加一行即可。
CANON_CHECKS: list[tuple[str, str, str, str]] = [
    # --- memory 总数 ---
    ("wiki/architecture/conventions.md", r"auto-memory (\d+) 个", "mem_total", "memory 总数"),
    ("wiki/concepts/anti-patterns.md", r"memory 共 (\d+) 个", "mem_total", "memory 总数"),
    ("wiki/concepts/anti-patterns.md", r"共 (\d+) 个原始源", "mem_total", "memory 总数"),
    ("wiki/index.md", r"(\d+) 条 auto-memory", "mem_total", "memory 总数"),
    ("wiki/architecture/three-tier-architecture.md", r"恒久（(\d+) 条）", "mem_total", "memory 总数"),
    ("wiki/topics/ecosystem-dashboard.md", r"Memory 条目 \| \*\*(\d+)\*\*", "mem_total", "memory 总数"),
    # --- memory project 子计数 ---
    ("wiki/architecture/conventions.md", r"project (\d+) / reference", "mem_project", "memory project 子数"),
    ("wiki/concepts/anti-patterns.md", r"project (\d+) / reference", "mem_project", "memory project 子数"),
    ("wiki/topics/ecosystem-dashboard.md", r"project (\d+) / reference", "mem_project", "memory project 子数"),
    # --- scripts ---
    ("wiki/architecture/conventions.md", r"Hub 当前 (\d+) 个 \.py", "scripts", "scripts 数"),
    ("wiki/topics/ecosystem-dashboard.md", r"自动化脚本 \| \*\*(\d+)\*\*", "scripts", "scripts 数"),
    ("README.md", r"自动化脚本 \| (\d+) \|", "scripts", "scripts 数"),
    # --- wiki 内容页 / 总文件 ---
    ("wiki/index.md", r"页面总数：(\d+)", "wiki_content", "wiki 内容页"),
    ("wiki/topics/ecosystem-dashboard.md", r"wiki 内容页 \| \*\*(\d+)\*\*", "wiki_content", "wiki 内容页"),
    ("wiki/topics/ecosystem-dashboard.md", r"wiki 总文件 \| \*\*(\d+)\*\*", "wiki_total", "wiki 总文件"),
    ("wiki/architecture/conventions.md", r"Hub wiki 当前共 \*\*(\d+) 个 \.md\*\*", "wiki_total", "wiki 总文件"),
    # --- agents / rules / skills（本地）---
    ("wiki/topics/ecosystem-dashboard.md", r"全局 agent \| \*\*(\d+)\*\*", "agents", "agents 数"),
    ("wiki/architecture/conventions.md", r"agents (\d+) 个 \.md", "agents", "agents 数"),
    ("wiki/topics/ecosystem-dashboard.md", r"rules 目录 \| \*\*(\d+)\*\*", "rules", "rules 目录数"),
    ("wiki/architecture/conventions.md", r"rules (\d+) 个目录", "rules", "rules 目录数"),
    ("wiki/topics/ecosystem-dashboard.md", r"全局 skill（本地） \| \*\*(\d+)\*\*", "skills_local", "本地 skill 数"),
    ("wiki/architecture/conventions.md", r"skills 本地 (\d+) 个", "skills_local", "本地 skill 数"),
    # --- 项目登记数（活跃项目 / DocProcess）---
    # 「部分登记」反模式连续 7 轮主犯：新项目派生后「活跃项目数 / DocProcess×N」
    # 只 bump 部分 canon 页。此前 CANON_CHECKS 不机检项目登记面（self-check 7/8 surface
    # 未根治），靠人工 grep 兜底。ground-truth：活跃数=导航卡−非项目卡；DocProcess 数=
    # conventions §9 行数（见 count_active_projects / count_docprocess_projects）。
    ("wiki/architecture/system-overview.md", r"\| \*\*活跃项目数\*\* \| (\d+) \|", "active_projects", "活跃项目数"),
    ("wiki/architecture/system-overview.md", r"DocProcess×(\d+)", "docprocess_projects", "DocProcess 项目数"),
]


def compute_ground_truth(hub_root: Path, claude_root: Path) -> dict[str, int]:
    _, content_total, _, wiki_total, _ = count_wiki(hub_root)
    _, skill_with_md = count_skills(claude_root)
    mem_counts, mem_total = count_memory(claude_root)
    return {
        "mem_total": mem_total,
        "mem_project": mem_counts.get("project", 0),
        "mem_feedback": mem_counts.get("feedback", 0),
        "scripts": count_glob(hub_root / "scripts", "*.py"),
        "wiki_content": content_total,
        "wiki_total": wiki_total,
        "agents": count_agents(claude_root),
        "rules": count_rules(claude_root),
        "skills_local": skill_with_md,
        "active_projects": count_active_projects(hub_root),
        "docprocess_projects": count_docprocess_projects(hub_root),
    }


def run_check(hub_root: Path, claude_root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    """返回 (问题列表, 通过列表, 实跑值)。问题非空即有 CANON 漂移或措辞失配。"""
    gt = compute_ground_truth(hub_root, claude_root)
    issues: list[str] = []
    oks: list[str] = []
    for relpath, pattern, key, label in CANON_CHECKS:
        f = hub_root / relpath
        expected = gt[key]
        if not f.is_file():
            issues.append(f"[缺文件] {relpath}（期望 {label}={expected}）")
            continue
        found = re.findall(pattern, f.read_text(encoding="utf-8"))
        if not found:
            issues.append(f"[模式失配] {relpath} ::{label}：正则未命中，措辞可能变了，需更新 CANON_CHECKS 或人工核对 → {pattern}")
            continue
        bad = sorted({v for v in found if int(v) != expected})
        if bad:
            issues.append(f"[计数 stale] {relpath} ::{label}：页面写 {bad}，实跑应为 {expected}")
        else:
            oks.append(f"[OK] {relpath} ::{label}={expected}（{len(found)} 处）")
    return issues, oks, gt


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ohmybrain 生态规模快照 / CANON 计数一致性校验"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="校验 wiki 各处 CANON 计数与实跑值是否一致（不一致 stdout 提醒，始终 exit 0；可作 Stop hook）",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="--check 时打印每条检查（含通过项）",
    )
    args = parser.parse_args()

    hub_root = find_hub_root(Path(__file__).resolve().parent)
    if hub_root is None:
        hub_root = find_hub_root(Path.cwd())
    if hub_root is None:
        print("ERROR: 未找到 Ohmybrain 仓根（含 wiki/ 与 scripts/）", file=sys.stderr)
        return 1

    claude_root = Path.home() / ".claude"

    if args.check:
        issues, oks, gt = run_check(hub_root, claude_root)
        if args.verbose:
            for line in oks:
                print(line)
        if issues:
            print(
                f"[CANON-check] {len(issues)} 处 CANON 计数不一致 / 失配"
                f"（实跑：memory {gt['mem_total']} / project {gt['mem_project']} · "
                f"scripts {gt['scripts']} · wiki 内容页 {gt['wiki_content']}/{gt['wiki_total']} · "
                f"agents {gt['agents']} · rules {gt['rules']} · skills {gt['skills_local']} · "
                f"活跃项目 {gt['active_projects']} / DocProcess {gt['docprocess_projects']}）："
            )
            for line in issues:
                print(f"  - {line}")
            print("  → 修正后重跑 `python scripts/dashboard_snapshot.py --check` 应静默。")
        elif args.verbose:
            print("[CANON-check] ✓ 全部一致")
        return 0  # 提醒型：始终 exit 0（Stop hook 安全，Windows 友好）

    if not claude_root.is_dir():
        print(f"WARN: ~/.claude 不存在（{claude_root}），全局资源计数将为 0", file=sys.stderr)

    print(f"<!-- Hub 内部规模快照：由 dashboard_snapshot.py 生成 | hub={hub_root} -->")
    print(render(hub_root, claude_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
