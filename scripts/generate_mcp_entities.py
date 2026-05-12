#!/usr/bin/env python
"""
从 MCP memory graph（JSONL）生成 Obsidian wikilink 节点笔记。
让 Juggl / Extended Graph / 原生 graph view 能可视化 MCP graph。

用法：
  python scripts/generate_mcp_entities.py

数据源：C:\\Users\\zazn\\.claude\\memory\\graph.jsonl
输出：  D:\\Claude\\Ohmybrain\\wiki\\mcp-entities\\
"""
import json
import sys
import io
from pathlib import Path
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GRAPH_PATH = Path(r"C:/Users/zazn/.claude/memory/graph.jsonl")
OUT_DIR = Path(__file__).resolve().parent.parent / "wiki" / "mcp-entities"

TYPE_ORDER = ["project", "knowledge_hub", "scheme", "technique", "paper"]
TYPE_ZH = {
    "project": "Project",
    "knowledge_hub": "Knowledge Hub",
    "scheme": "Scheme（通信体制）",
    "technique": "Technique（技术）",
    "paper": "Paper（论文）",
}


def load_graph():
    entities, relations = {}, []
    with GRAPH_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            t = obj.get("type")
            if t == "entity":
                entities[obj["name"]] = obj
            elif t == "relation":
                relations.append(obj)
    return entities, relations


def build_edges(relations):
    in_e, out_e = defaultdict(list), defaultdict(list)
    for r in relations:
        out_e[r["from"]].append((r["to"], r["relationType"]))
        in_e[r["to"]].append((r["from"], r["relationType"]))
    return in_e, out_e


def render_entity(name, e, ins, outs):
    etype = e["entityType"]
    obs = e.get("observations", [])
    lines = [
        "---",
        f"type: {etype}",
        f"cssclass: type-{etype}",
        f"tags: [mcp-graph, {etype}]",
        "autogen: generate_mcp_entities.py",
        "---",
        "",
        f"# {name}",
        "",
        f"> ⚠️ 自动生成。手动改会被脚本覆盖。如需个人笔记，另建伴生文件。",
        "",
        f"**Entity type**: `{etype}`",
        "",
        "## Observations",
        "",
    ]
    lines += [f"- {o}" for o in obs] if obs else ["- （空）"]
    lines.append("")
    if ins:
        lines.append("## 入边（被指向）")
        lines.append("")
        lines += [f"- 被 [[{src}]] **{rtype}**" for src, rtype in ins]
        lines.append("")
    if outs:
        lines.append("## 出边（指向）")
        lines.append("")
        lines += [f"- **{rtype}** → [[{dst}]]" for dst, rtype in outs]
        lines.append("")
    lines.append("## 相关")
    lines.append("")
    lines.append("- [[_index|MCP Entities 索引]]")
    lines.append("- [[memory-graph]] — Mermaid 快照")
    lines.append("- [[memory-stack]] — 记忆栈 5 层总览")
    lines.append("")
    return "\n".join(lines)


def render_index(entities, total_rel):
    by_type = defaultdict(list)
    for name, e in entities.items():
        by_type[e["entityType"]].append(name)

    lines = [
        "---",
        "type: mcp-entities-index",
        "tags: [mcp-graph, 索引]",
        "---",
        "",
        "# MCP Entities 索引",
        "",
        f"[[memory-graph|MCP 知识图谱]] 的 Obsidian wikilink 投影（{len(entities)} 实体 + {total_rel} 关系）。",
        "",
        "每个 entity 一篇 `.md`，通过 `[[wikilink]]` 互链，供 **Juggl / Extended Graph / 原生 graph view** 可视化。",
        "",
        "## 生成元信息",
        "",
        "- **数据源**：`C:\\Users\\zazn\\.claude\\memory\\graph.jsonl`",
        "- **生成脚本**：`scripts/generate_mcp_entities.py`",
        "- **刷新**：改 MCP graph 后重跑脚本（会覆盖所有实体笔记）",
        "",
        "## 实体清单",
        "",
    ]
    for etype in TYPE_ORDER:
        if etype not in by_type:
            continue
        lines.append(f"### {TYPE_ZH.get(etype, etype)}（{len(by_type[etype])}）")
        lines.append("")
        lines += [f"- [[{name}]]" for name in sorted(by_type[etype])]
        lines.append("")

    lines += [
        "## Juggl 样式建议",
        "",
        "装 Juggl 后，在 `.obsidian/plugins/juggl/graph.css` 加：",
        "",
        "```css",
        ".type-project { background-color: #1e3a5f; color: #fff; }",
        ".type-knowledge_hub { background-color: #4c1d95; color: #fff; }",
        ".type-scheme { background-color: #065f46; color: #fff; }",
        ".type-technique { background-color: #7c2d12; color: #fff; }",
        ".type-paper { background-color: #1f2937; color: #e5e7eb; }",
        "```",
        "",
        "Juggl 设置里开启 **Read CSS classes from frontmatter** 即可按 `cssclass` 着色。",
        "",
    ]
    return "\n".join(lines)


def main():
    if not GRAPH_PATH.exists():
        print(f"✗ 数据源不存在：{GRAPH_PATH}")
        sys.exit(1)
    entities, relations = load_graph()
    in_edges, out_edges = build_edges(relations)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    count = 0
    for name, e in entities.items():
        path = OUT_DIR / f"{name}.md"
        path.write_text(render_entity(name, e, in_edges[name], out_edges[name]), encoding="utf-8")
        count += 1

    (OUT_DIR / "_index.md").write_text(render_index(entities, len(relations)), encoding="utf-8")
    print(f"✓ 生成 {count} 实体笔记 + 1 索引 @ {OUT_DIR}")


if __name__ == "__main__":
    main()
