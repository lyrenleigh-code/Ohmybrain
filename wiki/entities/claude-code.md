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

单一 Skill 深度范本：[[yizhiyanhua-ai-fireworks-tech-graph]]（yizhiyanhua-ai / MIT）示范 Skill 工程化的 7 条可迁移模式——三层资源分离、frontmatter 触发关键词、Pre-Tool-Call Checklist、Error Recovery Protocol、UML 覆盖映射表、npm 打包可分发、多 runtime 兼容。

生产级规模化范本：[[affaan-m-everything-claude-code|Everything Claude Code (ECC)]]（affaan-m / MIT / 黑客松冠军）—— 48 agents + 183 skills + 79 commands + 8 种 hooks × 12 语言生态的**可直接部署生产配置包**，与 best-practice 的"教科书参考"形成互补。独有机制：Instinct 系统（confidence scoring 增量学习）、Search-First 开发（写代码前强制研究）、Hook Runtime Controls（`ECC_HOOK_PROFILE` 运行时门控）、跨 Harness DRY Adapter（Cursor / Codex / OpenCode 复用同一套 hooks 脚本）、AgentShield 安全扫描。

## 来源

- [[my-brain-setup-plan.md|搭建计划]] — 定义了 Claude Code 在三阶段中的核心角色
- [[toolchain.md|工具链指南]] — 描述了 Claude Code 作为执行引擎的具体职责
- [[claude-code-best-practice]] — shanraisshan 维护的最佳实践参考库
- [[affaan-m-everything-claude-code]] — Affaan Mustafa 维护的生产级配置包（ECC）
- Skill 工程化范本：[[yizhiyanhua-ai-fireworks-tech-graph]]
- 单用途极简 Skill 范本：[[cocoon-ai-architecture-diagram]]（Cocoon AI / MIT，架构图生成）
- 持久记忆插件：[[thedotmack-claude-mem]]（Alex Newman / AGPL-3.0，hook+worker+MCP 三层架构）
- 官方 founder 方法论：[[anthropic-2026-founders-playbook]]（Anthropic 2026 v3，三表面 Chat/Cowork/Code 分工 + CLAUDE.md as architectural memory）
