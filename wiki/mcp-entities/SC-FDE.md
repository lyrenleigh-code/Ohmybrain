---
type: scheme
cssclass: type-scheme
tags: [mcp-graph, scheme]
autogen: generate_mcp_entities.py
---

# SC-FDE

> ⚠️ 自动生成。手动改会被脚本覆盖。如需个人笔记，另建伴生文件。

**Entity type**: `scheme`

## Observations

- 改前 α 上限 <1e-4
- 改后 α 上限 3e-2（含 3 patch 突破）
- A2 α=5e-4 BER 0%
- D α=+3e-2 BER 5.4%
- 3 patch: TX tail pad + CP 阈值门禁 + 正向精扫

## 入边（被指向）

- 被 [[UWAcomm]] **实装**

## 出边（指向）

- **采用** → [[est_alpha_dual_chirp]]
- **采用** → [[iterative-refinement]]

## 相关

- [[_index|MCP Entities 索引]]
- [[memory-graph]] — Mermaid 快照
- [[memory-stack]] — 记忆栈 5 层总览
