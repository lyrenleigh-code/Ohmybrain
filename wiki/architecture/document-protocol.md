---
type: architecture
created: 2026-06-09
updated: 2026-06-09
tags: [文档协议, 协作层, 三层结构, 路径安全, 迁移级别]
---

# 文档结构协议

> 最后更新：2026-06-09

本文定义 `D:\Claude` 下各项目共享的文档结构。它是用户、Claude Code 和 Codex 之间的协作层。

## 设计目标

工作区应允许多个 agent 协同工作，而不依赖临时聊天上下文。每个项目把明确的任务状态写入文件，Hub 负责沉淀跨项目长期知识。

## 三层结构

| 层级 | 位置 | 职责 |
|---|---|---|
| 工作区地图 | `D:\Claude\CLAUDE.md` + `AGENTS.md` | 稳定路径、全局规则、agent 入口 |
| Hub 知识 | `Ohmybrain/wiki/` + `Ohmybrain/projects/` | 跨项目记忆、决策、可复用协议 |
| 项目状态 | 项目内 `wiki/`、`specs/`、`plans/`、`handoff/` | 当前任务状态、实现上下文、本地知识 |

## 标准项目骨架

每个活跃项目都应逐步收敛到以下结构：

```text
项目名/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── raw/
├── wiki/
│   ├── index.md
│   └── log.md
├── specs/
│   ├── active/
│   └── archive/
├── plans/
│   ├── active/
│   └── archive/
├── handoff/
│   ├── active/
│   └── archive/
├── workflows/
├── scripts/
└── output/ 或 src/ 或 modules/
```

项目类型决定最终生产目录：

| 类型 | 主要产出 |
|---|---|
| 工程类 | `src/`、`modules/`、`tests/`、仿真输出 |
| 文档类 | `output/` 下的 docx/pdf/vsdx 与章节草稿 |
| 工具类 | `templates/`、已注册 skill、示例输出 |

## 路径安全

本协议刻意避免移动既有项目根目录。移动根目录会影响脚本、wiki 链接、Obsidian 链接、worktree 以及历史笔记中的硬编码路径。

安全变更：

- 新增 `AGENTS.md`、`handoff/`、`plans/active/` 或占位文件。
- 新增 Hub 协议页和项目导航页。
- 更新 `ohmybrain-core/` 模板，让未来项目从一开始就保持一致。

高风险变更：

- 重命名或移动 `TechReq/`、`DocProcess/`、`Tools/`、`worktrees/`、`Ohmybrain/`、`ohmybrain-core/`。
- 在项目根目录之间移动源码。
- 重写历史原始资料路径。
- 未审计调用方就修改依赖当前项目根目录的脚本。

## 状态归属

| 目录 | 主要维护者 | 规则 |
|---|---|---|
| `raw/` | 用户 / 摄入流程 | 默认只读 |
| `wiki/` | agent + 用户 | 结构变更必须更新 `wiki/index.md` 和 `wiki/log.md` |
| `specs/active/` | 规划者 | 说明要做什么 |
| `plans/active/` | 规划者 / 实现者 | 说明怎么做 |
| `handoff/active/` | 双方 agent | 说明谁从哪里继续 |
| `output/` | 交付物生产者 | 只保留有意生成的产物 |

## 迁移级别

使用能解决问题的最低级别。

| 级别 | 范围 | 路径风险 |
|---|---|---|
| L0 | 补齐缺失的 `handoff/` 和 `plans/active/` 目录 | 无 |
| L1 | 增加项目内 `AGENTS.md` 和 README 指引 | 低 |
| L2 | 统一项目 wiki 索引与日志 | 中 |
| L3 | 移动或重命名既有项目根目录 | 高；需要用户明确批准 |

当前默认：**只做 L0 + L1**。

## 相关页面

- [[three-tier-architecture]] — 本协议三层结构的架构源头（Hub / project / core）
- [[../agents/claude-codex-collaboration]] — 在此协议上运行的双 Agent 协作
- [[../workflows/agent-handoff]] — 项目状态层的交接流程
- [[conventions]] — 跨项目约定（命名 / 目录 / wiki 写作）
- [[hub-as-brain]] — Hub 知识层定位
