---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, AI, 执行引擎]
entity_type: tool
---

# Claude Code

Anthropic 出品的 CLI 工具，是 my-brain 系统的**核心执行引擎**。

## 角色定位

在 [[harness-engineering]] + [[llm-wiki]] 系统中，Claude Code 承担所有自动化执行工作：

- 执行 ingest、promote、lint 工作流
- 维护 harness 规则（hooks、slash commands）
- 编程和项目开发（主力）
- 通过 MCP 协议连接外部工具（如 [[firecrawl]]）

## 关键能力

- **Hooks 机制**：PreToolUse / PostToolUse / Stop hooks，将规则编码为自动化约束
- **Slash Commands**：/ingest-source、/lint-wiki、/promote-answer 等自定义命令
- **CLAUDE.md**：仓库级操作手册，定义 agent 的行为边界

## 在 my-brain 中的位置

```
原始资料 → 收集工具 → Claude Code（ingest/harness）→ wiki/ → Obsidian/GitHub
```

## 来源

- [[my-brain-setup-plan.md|搭建计划]] — 定义了 Claude Code 在三阶段中的核心角色
- [[toolchain.md|工具链指南]] — 描述了 Claude Code 作为执行引擎的具体职责
