---
type: source-summary
created: 2026-04-14
updated: 2026-04-14
tags: [AI-Agent, Hermes, Nous-Research, Skill, Self-Improving, MCP, Messaging]
source_type: repo
---

# Hermes Agent — Nous Research 自改进开源 AI Agent

## 来源信息

- **仓库**：`github.com/NousResearch/hermes-agent`
- **本地路径**：`raw/repos/hermes-agent`
- **许可**：MIT
- **最新版本**：v0.9.0（tag `v2026.4.13`，2026-04-13 发布）
- **规模**：4,069 commits、~3,000 测试、63k+ 行（仅 v0.8 → v0.9 就 487 commits / 269 merged PRs）
- **官方文档**：`hermes-agent.nousresearch.com/docs`
- **构建方**：[Nous Research](https://nousresearch.com)（开源 LLM 研究团体，Hermes 系列模型的背后）

## 核心观点

1. **唯一自带学习循环的 Agent**：执行复杂任务后自主创建 skill、用中更新 skill、定期 "nudge" 持久化知识、FTS5 跨会话搜索自己历史对话、通过 [Honcho](https://github.com/plastic-labs/honcho) 辩证式用户建模跨会话深化对"你是谁"的理解
2. **不绑定设备/厂商**：`hermes model` 一键换模型（Nous Portal / OpenRouter 200+ 模型 / z.ai / Kimi / MiniMax / OpenAI / 自建端点），6 种终端后端（local / Docker / SSH / Daytona / Singularity / Modal），Modal & Daytona 提供**无服务器持久化**——空闲时休眠、触发时唤醒，$5/月 VPS 就能跑
3. **到处都能说话**：16 个消息平台统一网关——Telegram / Discord / Slack / WhatsApp / Signal / Matrix / Email / SMS / iMessage（BlueBubbles）/ DingTalk / Feishu / WeChat / WeCom / Mattermost / Home Assistant / Webhooks
4. **Skills 是开放标准**：兼容 [agentskills.io](https://agentskills.io) 开放规范，仓内自带 26 个领域 skill 合集
5. **可编程 Agent 循环**：`delegate_tool` 派生隔离子代理并行工作；可写 Python 脚本通过 RPC 调工具，把多步管道折叠成零上下文成本的单轮
6. **Cron 内建**：自然语言描述的定时任务 + 任意平台投递——"每日汇报 / 夜间备份 / 周度审计" 全跑无人值守
7. **研究友好**：Batch trajectory generation、Atropos RL environments、trajectory compression——为训练下一代工具调用模型留足接口（`tinker-atropos/` 子模块）

## 架构核心

### 入口层次

```
hermes (TUI, cli.py)         ─┐
hermes gateway (run.py)      ─┼─→ AIAgent (run_agent.py) ─→ handle_function_call (model_tools.py)
acp_adapter (VS Code / Zed / JetBrains) ─┘                    ↓
                                                    tools/registry.py + tools/*.py (~40+)
```

### 核心类

- **`AIAgent`** (`run_agent.py`)：同步 `run_conversation()` 循环，`max_iterations=90`，支持 `platform` 区分 CLI / Telegram / …，OpenAI 格式消息 + `reasoning` 字段存思维链
- **`HermesCLI`** (`cli.py`)：Rich banner + prompt_toolkit autocomplete + **KawaiiSpinner**（表情动画 + `┊` 活动流）
- **`SessionDB`** (`hermes_state.py`)：SQLite 会话库 + FTS5 全文搜索
- **`registry`** (`tools/registry.py`)：中央工具表——schema 收集、dispatch、可用性检查、错误包装。所有 handler **必须**返回 JSON 字符串
- **`COMMAND_REGISTRY`** (`hermes_cli/commands.py`)：单一 `CommandDef` 列表驱动所有下游（CLI / Gateway / Telegram BotCommand / Slack subcommand / autocomplete / help）

### 主要包（代码仓 tree 提炼）

| 包 | 职责 | 亮点 |
|------|-----|------|
| `agent/` | 代理内部 | prompt_builder、context_compressor、prompt_caching、memory_manager、**smart_model_routing**、**error_classifier**、insights |
| `hermes_cli/` | CLI 子命令与向导 | `main.py` 入口、**skin_engine**（CLI 主题）、setup 向导、`model_switch` 统一管道 |
| `tools/` | 40+ 工具实现 | mcp_tool（~1050 行）、delegate_tool（子代理派生）、browser_tool（Browserbase）、code_execution_tool、file/web/memory/todo tools、**approval.py**（危险命令检测）、**path_security.py** |
| `gateway/` | 消息网关 | 16 个 `platforms/` 适配器、hooks、pairing（DM 配对验证）、sticker_cache、stream_consumer |
| `acp_adapter/` | Agent Communication Protocol 服务 | VS Code / Zed / JetBrains 集成 |
| `cron/` | 内置调度器 | `jobs.py` + `scheduler.py` |
| `environments/` | RL 训练环境 | Atropos base env、agentic_opd_env、web_research_env、hermes_swe_env |
| `plugins/` | 可插拔槽位 | context_engine、memory（pluggable context engine 是 v0.9.0 新增） |
| `skills/` | 内置 26 个领域 skill 合集 | autonomous-ai-agents / creative / data-science / devops / diagramming / dogfood / domain / email / feeds / gaming / gifs / github / inference-sh / leisure / mcp / media / mlops / note-taking / productivity / red-teaming / research / smart-home / social-media / software-development / apple / index-cache |

## 可借鉴模式

### 1. 单一命令表驱动多终端

`CommandDef` 一处添加，CLI process_command / Gateway dispatch / Telegram menu / Slack subcommand / autocomplete / help 全部自动联动。加别名只需改 `aliases` 元组，**其它文件零改动**。这是 "single source of truth" 的教科书实践——值得在 Ohmybrain 的 commands 体系借鉴。

### 2. Prompt Caching 硬约束

项目 AGENTS.md 明确写入"**Prompt Caching Must Not Break**"作为政策：禁止会话中途改上下文、改工具集、重载内存、重建 system prompt——破坏缓存的代价是**成本剧增**。唯一可改上下文的时机是 **context compression**。这是长会话 agent 成本控制的第一性原理。

### 3. Profile（多实例隔离）

`HERMES_HOME` 环境变量 + `_apply_profile_override()` 在任何模块导入前设置，所有 119+ 处 `get_hermes_home()` 自动作用域化。Hardcode `~/.hermes` 会**破坏 profile 隔离**（AGENTS.md 中列为已知陷阱，PR #3575 修了 5 个类似 bug）。对 Ohmybrain 多项目共享 `.claude/` 状态的设计有直接借鉴价值。

### 4. Token Lock 防撞车

网关平台适配器如果用独占凭据（bot token / API key），必须 `acquire_scoped_lock()` / `release_scoped_lock()`——防止两个 profile 同时用同一 token。`gateway/platforms/telegram.py` 是范式参考。

### 5. Tool Schema 描述不可硬编码跨工具引用

tool schema description **不得**提及另一 toolset 的工具名——那些工具可能因缺 API key / 禁用 toolset 而不可用，模型会幻觉调用不存在的工具。需要跨引用时在 `get_tool_definitions()` 中动态注入。

### 6. Agent-level 工具在 dispatch 前拦截

`todo` / `memory` 这类影响 agent 自身状态的工具，在 `run_agent.py` 里拦截 `handle_function_call()`——见 `todo_tool.py` 范式。保持了工具系统的一致性，又允许代理级特殊处理。

### 7. 可插拔 Context Engine（v0.9.0 新增）

Context 管理成为 `hermes plugins` 的一个 slot，可替换成自定义实现——过滤、摘要、领域特定上下文注入。对需要定制上下文策略的场景（如 Ohmybrain 的 wiki 上下文注入）是直接模板。

### 8. 6 种终端后端 + 无服务器持久化

`environments/`（local / docker / ssh / modal / daytona / singularity）——同一个 agent 代码跑在不同基础设施。**Daytona & Modal 的无服务器模式**：空闲休眠，触发唤醒，近零闲置成本——值得学习的 agent 部署模式。

### 9. 消息网关 hooks + builtin_hooks

`gateway/hooks.py` + `gateway/builtin_hooks/` 是一套独立于主 agent 循环的 hook 系统，典型用途：background 进程完成通知、状态事件、交付确认。和主 agent 的 hook 分层。

### 10. 自带 RL 训练接口

`environments/` 下有多个 Atropos RL env、batch_runner、trajectory_compressor——**把 agent 本身当训练数据源**，为下一代工具调用模型提供 trajectory。这是生产级 agent 从"用"到"训"的闭环，罕见于开源项目。

## 对比 Claude Code（一句话）

| 维度 | Claude Code | Hermes Agent |
|-----|-------------|--------------|
| 定位 | Anthropic 官方 CLI（闭源，订阅） | Nous Research 开源 agent（MIT，自部署） |
| 模型 | 绑定 Anthropic（Opus/Sonnet/Haiku） | 任意（Nous Portal / OpenRouter / z.ai / Kimi / MiniMax / OpenAI / 自建） |
| 运行环境 | 主要本地 CLI + 少量云（`--web`） | 6 后端 + 无服务器持久化 + 16 消息平台 |
| 自改进 | Auto-memory（主 Claude 写）、agent memory | **Skill 自主创建/自改进 + Honcho 用户建模 + FTS5 自搜** |
| Skill 标准 | 私有格式（`.claude/skills/*/SKILL.md`） | [agentskills.io](https://agentskills.io) **开放标准兼容** |
| 子代理 | `Agent` tool + subagent 定义 | `delegate_tool` + 隔离子代理 + 可编程 RPC |
| Cron | `/loop` + `/schedule`（上限 3 天） | 内置调度器，无限期，16 平台投递 |

两者都是**"Command / Agent / Skill + Hooks + Memory + MCP"** 范式的实现，互相可以抄架构。Claude Code 的优势在官方支持和深度 IDE 集成；Hermes 的优势在**模型自由 + 部署自由 + 自改进闭环 + 消息平台覆盖**。

## OpenClaw 迁移通道

Hermes 提供 `hermes claw migrate` 一键从 OpenClaw 导入 SOUL.md / MEMORY.md / USER.md / 自定义 skill / 命令 allowlist / 消息设置 / API keys / TTS 资产 / workspace AGENTS.md。对用户：降低切换成本；对设计者：**值得注意的生态兼容性姿态**。

## 与 Ohmybrain 的连接点

1. **Skill 系统范式**：Hermes 的 `~/.hermes/skills/` + agentskills.io 兼容可作为 Ohmybrain `.claude/skills/` 的参照——尤其 26 领域 skill 合集是直接的借鉴素材
2. **单一 CommandDef 驱动多终端**：若未来 Ohmybrain 同时要在 CLI / 移动端 / Obsidian 插件中暴露一套命令，这是现成模板
3. **Profile 隔离**：Ohmybrain 多项目共享 `ohmybrain-core/template/` 但各项目有独立 `.claude/` 状态的设计，可参考 `HERMES_HOME` + `get_hermes_home()` 模式
4. **Context Engine 插槽**：把 wiki 检索做成 pluggable context engine（"每轮自动注入 wiki 命中"）比硬编码在 skill 里更干净
5. **Trajectory 采集**：`trajectory_compressor.py` 给我们一个思路——Ohmybrain 的会话可以保存成训练数据，未来微调私有模型
6. **CLI skin engine**：若 Ohmybrain 想做可定制的终端皮肤（比如每个项目不同 banner 色），直接抄 `hermes_cli/skin_engine.py`

## 相关概念

- [[subagents-orchestration]] — Hermes 的 `delegate_tool` 是同一编排范式的另一实现
- [[skills-vs-commands]] — Hermes skill 与 agentskills.io 开放标准
- [[claude-hooks-architecture]] — Hermes 的 gateway hooks 是平行架构
- [[harness-engineering]] — Hermes 自身即是一套成熟 agent harness

## 相关实体

- [[claude-code]] — 对标产品

## 引用摘录

> **The only agent with a built-in learning loop** — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions.

> Run it on a **$5 VPS**, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

> **Prompt Caching Must Not Break** — Do NOT implement changes that would alter past context mid-conversation, change toolsets mid-conversation, or reload memories / rebuild system prompts mid-conversation. Cache-breaking forces dramatically higher costs.

> DO NOT hardcode `~/.hermes` paths. Use `get_hermes_home()` for code paths and `display_hermes_home()` for user-facing messages. This was the source of **5 bugs fixed in PR #3575**.

## 相关范本（打包哲学对照）

- [[yizhiyanhua-ai-fireworks-tech-graph]] — Claude Code 私有 skill 格式 + npm 打包可分发（vs 本仓的 agentskills.io 开放标准）。两种打包哲学对照：开放互通 vs 私有分发。
