---
type: entity
created: 2026-04-12
updated: 2026-04-14
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

- **Hooks 机制**：PreToolUse / PostToolUse / Stop 等 15 个生命周期事件，将规则编码为自动化约束——详见 [[claude-hooks-architecture]]
- **三种扩展机制**：Agent / Command / Skill 各司其职——详见 [[skills-vs-commands]]
- **子代理编排**：Command → Agent → Skill 分层编排模式——详见 [[subagents-orchestration]]
- **CLAUDE.md**：仓库级操作手册，定义 agent 的行为边界（祖先上行加载、后代懒加载）
- **Agent Memory**（v2.1.33+）：子代理持久记忆，`user/project/local` 三种 scope
- **Tasks**（v2.1.16+，取代旧 TodoWrite）：跨会话任务持久化 + 依赖图

## 在 my-brain 中的位置

```
原始资料 → 收集工具 → Claude Code（ingest/harness）→ wiki/ → Obsidian/GitHub
```

## 参考实现库

`raw/repos/claude-code-best-practice` 是 shanraisshan 维护的 Claude Code 最佳实践参考仓（GitHub Trending #1，对标 v2.1.101）。每条 best practice 对应可直接抄改的实现：

- 9 篇 best-practice（frontmatter 清单 + 官方表）
- 9 篇深度 reports（三机制对比、agent memory、global vs project 等）
- Command → Agent → Skill 天气系统编排示例
- 5 个推荐日常 MCP 配置、完整 `.claude/` 样板

详见 [[claude-code-best-practice]]。

## 来源

- [[my-brain-setup-plan.md|搭建计划]] — 定义了 Claude Code 在三阶段中的核心角色
- [[toolchain.md|工具链指南]] — 描述了 Claude Code 作为执行引擎的具体职责
- [[claude-code-best-practice]] — shanraisshan 维护的最佳实践参考库
