---
type: source-summary
created: 2026-08-18
updated: 2026-08-18
tags: [agent-harness, 开源框架, DeepSeek, 插件架构, 国产化, 内网部署, Cordis]
source_type: repo
---

# deepseek-ai/deepseek-harness（dsh）

- **来源**：<https://github.com/deepseek-ai/deepseek-harness>（MIT，2026-08-13 创建，5 天 151k star，developer preview 迭代中有破坏性变更）
- **日期**：2026-08-18 ingest（README + docs/architecture.md + docs/subsystems/ 清单 + skills.md 细读）
- **一句话**：DeepSeek 开源的 **agent harness 框架**——「一切皆插件」（基于 Cordis），把 Claude Code 引擎层的全部概念做成可替换插件树；`npx @deepseek-ai/dsh web` 起 Web UI（127.0.0.1:3080）。

## 架构要点

- **Cordis 插件树**：无特权核心——model adapter、工具注册表、session log、agent loop 本身全是插件，注册即「可逆 effect」（插件卸载时回卷）。扩展 = 挂插件，不 patch 核心。
- **Profile / Bundle 分层组合**：运行实例 = 有序层叠的插件树（`dsh-base` 底座 → `dsh-web-app`/`dsh-headless` → profile 的 `cordis.patch.yml` → home 层 → `--patch` overlay），任意配置行可被上层 patch 替换。`--dump-config` 可打印实际 boot 树。
- **Turn/Step 事件流**：turn = 多个 step（一次模型请求 + 其工具调用）；`agent/pre-step`（改写/拒绝输入）→ prompt 组装 → `llm/stream` → `tools/pre-execute → execute → post-execute` waterfall 事件链，三域事件（durable session 事件 / live agent 事件 / capability 缝隙事件）。
- **Session log 单一事实源**：append-only，「model-visible means logged」运行时不变量——凡进入模型请求的内容必须可从 log 重建；fork/resume/transcript/telemetry 全部由此派生。
- **Capability seam（能力缝）**：Service Definition + Provider + Consumer 三角；换一个 provider 全产品跟着换（如文件系统+子进程指向远程 sandbox，Bash/PTY/LSP 一起迁移）。
- **Skill registry 分层**：host 全局层 + per-scope 层，就近层同名 skill 直接胜出——与 Claude Code「项目级覆盖全局级」同构；skill 是「可选指令」非 session 事件，由模型面 `skill` 工具消费。

## 子系统清单（≈45 个 docs/subsystems/*）

skills / subagent / workflow / plan / commands / schedule / compaction / sandbox / approval / permission-presets / goal / jobs / session-* 族 / LSP / shell / terminal / token-meter / spill / storage / user-questions 等；MCP client、hook bridges、第三方 memory MCP 见 `.agents/notes/implemented/`。**几乎是 Claude Code 概念面的开源镜像**。

## 与本工作区的对照（为何值得记）

- **定位差一层**：dsh 造的是 harness **引擎**（竞品 Claude Code / Codex CLI）；Ohmybrain 体系是骑在引擎上的**知识与工序层**（Hub wiki 闭环 / specs-plans-handoff / CANON 登记机检）——理论上可整体迁移到 dsh 之上。详见 [[../concepts/harness-engineering]]。
- **同构点**：分层 skill registry ↔ 全局/项目 skills；hook bridges ↔ Pre/PostToolUse/Stop hooks；subagent seam ↔ agent 池；profile/bundle patch ↔ rules 分层（特定覆盖通用）。
- **他们的 dogfood 工序**：仓库带 `.agents/notes/`（archived/implemented 按 feature/process/architecture 分类的开发笔记）+ AGENTS.md + CLAUDE.md——用 agent 开发 dsh 自身，与本体系 `specs/active→archive` + 交接单神似，可作工序对标样本。
- **内网国产化候选**：dsh + DeepSeek 模型 = 内网「类 Claude Code」开源底座选项，与 [[zhongan-llm-platform-ppt]]（昇腾 910B + 国产模型商用方案）同属「内网 AI 底座对标」组；关联 UWAcomm_usbl 十二月国产化线。

## 待观察

- developer preview，兼容性不稳定；Python SDK / jsonrpc-agent 最小变体可跑 benchmark。
- 5 天 151k star 的生态动能异常强，`dsh-plugin` topic 社区插件值得定期回访。
