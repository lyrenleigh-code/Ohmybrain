---
type: concept
created: 2026-04-13
updated: 2026-08-18
tags: [harness, agent, 工程实践, Claude Code]
---

# Harness 工程（Harness Engineering）

> 本页 2026-04-13 建立时为空占位，2026-08-18 入会审计（十五）后随 dsh ingest 实质填充。

**Agent harness** = 包住 LLM 的执行框架：agent loop（多轮工具调用循环）、工具注册与守卫执行、session/上下文管理、权限与沙箱、扩展机制（skills / hooks / subagents / MCP）。**Harness 工程**指两个层面的实践：

1. **造 harness**（引擎层）：实现 loop、工具管线、session log、权限模型本身——如 Claude Code（商用）、[[../source-summaries/deepseek-ai-deepseek-harness]]（开源，「一切皆插件」）。
2. **用 harness 造体系**（配置层）：在现成引擎上搭规则、知识与工序——本工作区的做法：`~/.claude/` rules 分层 + skills + agents 池 + hooks 守卫（见 [[../topics/harness-resources]]）+ Ohmybrain Hub 知识闭环 + specs/plans/handoff 工序（见 [[../architecture/system-overview]]）。

## 关键设计模式（跨引擎通用）

| 模式 | Claude Code | dsh | 本体系应用 |
|---|---|---|---|
| 分层覆盖 | 项目级覆盖全局级 | per-scope 层胜出 host 层 | rules common→zh→语言特定 |
| 生命周期 hook | Pre/PostToolUse/Stop | hook bridges + waterfall 事件 | Hub 8 hook + 工作区 guard |
| 子代理隔离 | subagent_type | subagent capability seam | agents 池 + 交接单 |
| 单一事实源 | transcript | append-only session log（model-visible means logged） | wiki index/log + CANON 机检 |
| 按需加载指令 | skills（paths/触发词） | skill 工具 + 分层 registry | 32 全局 skill + llm-wiki paths 触发 |

## 实战结论（一行 promote）

- **Codex 引擎开源 = 第三个可对照 harness 数据点**：openai/codex（Rust，Apache-2.0，119.6k★）2026-08-20 起把 **app-server / exec / SDK** 一并开源，`codex-rs/` 下含 `hooks` `skills` `memories` `worktree` `agent-roles` `plugin` `sandboxing` 等 crate，与 Claude Code、[[../source-summaries/deepseek-ai-deepseek-harness]] 构成三方对照；**其 skill 走 agentskills.io 开放标准**（`SKILL.md` + `name`/`description` frontmatter，扫描 `$CWD/.agents/skills` → `$REPO_ROOT/.agents/skills` → `$HOME/.agents/skills`），与本工作区 `~/.claude/skills/` 33 个结构同构，**存在跨引擎复用可能**（archify 即同时声明支持 Claude Code 与 Codex）。— 源=openai/codex 仓树 + developers.openai.com/codex/skills，2026-08-29

## 相关页面

- [[subagents-orchestration]] / [[skills-vs-commands]] / [[claude-hooks-architecture]] — Claude Code 侧机制细节
- [[../source-summaries/thedotmack-claude-mem]] — hook exit-code 契约借鉴源
- [[../source-summaries/zhongan-llm-platform-ppt]] — 内网商用平台对标（与 dsh 同属国产化底座候选组）
