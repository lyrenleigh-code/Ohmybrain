---
type: mcp-entities-index
tags: [mcp-graph, 索引]
---

# MCP Entities 索引

[[memory-graph|MCP 知识图谱]] 的 Obsidian wikilink 投影（24 实体 + 36 关系）。

每个 entity 一篇 `.md`，通过 `[[wikilink]]` 互链，供 **Juggl / Extended Graph / 原生 graph view** 可视化。

## 生成元信息

- **数据源**：`C:\Users\zazn\.claude\memory\graph.jsonl`
- **生成脚本**：`scripts/generate_mcp_entities.py`
- **刷新**：改 MCP graph 后重跑脚本（会覆盖所有实体笔记）

## 实体清单

### Project（3）

- [[USBL]]
- [[UWAcomm]]
- [[UWAnet]]

### Knowledge Hub（1）

- [[Ohmybrain]]

### Scheme（通信体制）（6）

- [[DSSS]]
- [[FH-MFSK]]
- [[OFDM]]
- [[OTFS]]
- [[SC-FDE]]
- [[SC-TDE]]

### Technique（技术）（3）

- [[est_alpha_dsss_symbol]]
- [[est_alpha_dual_chirp]]
- [[iterative-refinement]]

### Paper（论文）（6）

- [[lalevee-2025-dichotomous]]
- [[muzzammil-2019-cpofdm]]
- [[sun-2020-dsss-doppler]]
- [[wei-2020-dual-hfm]]
- [[yang-2026-otfs]]
- [[zheng-2025-dd-mmse]]

## Juggl 样式建议

装 Juggl 后，在 `.obsidian/plugins/juggl/graph.css` 加：

```css
.type-project { background-color: #1e3a5f; color: #fff; }
.type-knowledge_hub { background-color: #4c1d95; color: #fff; }
.type-scheme { background-color: #065f46; color: #fff; }
.type-technique { background-color: #7c2d12; color: #fff; }
.type-paper { background-color: #1f2937; color: #e5e7eb; }
```

Juggl 设置里开启 **Read CSS classes from frontmatter** 即可按 `cssclass` 着色。
