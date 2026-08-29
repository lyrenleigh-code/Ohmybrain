---
type: source-summary
created: 2026-08-29
updated: 2026-08-29
tags: [agent-harness, 开源框架, OpenAI, Codex, agentskills, 跨引擎复用, Rust]
source_type: repo
---

# openai/codex（Codex Harness 开源）

- **来源**：<https://github.com/openai/codex>（Apache-2.0，Rust，2025-04-13 创建，本次核验 @2026-08-29 时 119,584 star / 1,747 fork，`pushed_at` 当日——高频迭代）
- **日期**：2026-08-29 ingest（仓库树 + `codex-rs/` crate 清单 + README + `developers.openai.com/codex/skills` 细读；**未克隆源码**，架构判断基于目录结构与官方文档）
- **一句话**：2026-08-20 OpenAI 把 **Harness——Codex 的引擎本体**——连同 `app-server`（执行引擎服务）、`codex exec`（CLI）、**Codex SDK** 一并开源，从「开源客户端」变成「开源引擎」，可自由改造嵌入商用。

> **口径声明**：star 数、许可证、crate 清单、skills 路径与格式均**已亲核**（GitHub API + 官方文档）。ARC-AGI-3 分数 13.3%→38.3%（token 消耗降至 1/6）一说**仅见于转载稿**，未在官方页核实，**不作为本页结论使用**。

## 为何值得记

这是本工作区 harness 对照组的**第三个数据点**，且是唯一与日常工序直接耦合的一个——Codex 是本体系双 agent 协作协议里的另一半（见 [[../agents/claude-codex-collaboration]]）。此前只能把 Codex 当黑盒使用，引擎开源后其扩展面（hooks / skills / memories / worktree）可被直接读取与对照。

## 架构面（`codex-rs/` crate 结构反推）

仓库根：`codex-rs/`（Rust 主体）+ `codex-cli/` + `sdk/` + `docs/` + `AGENTS.md`（自身也用 agent 开发，dogfood 工序同 dsh）。构建走 Bazel + Nix flake。

按域归拢的关键 crate：

| 域 | crate | 对照本体系 |
|---|---|---|
| 引擎/执行 | `app-server` · `app-server-protocol` · `app-server-transport` · `app-server-daemon` · `exec` · `exec-server` · `core` · `core-api` | Claude Code 引擎层（闭源），dsh 的 Cordis 内核 |
| 扩展机制 | `skills` · `hooks` · `plugin` · `core-plugins` · `mcp-server` · `rmcp-client` | 本工作区 32 skill + 8 Hub hook + MCP 池 |
| 多 agent | `agent-roles` · `agent-graph-store` · `collaboration-mode-templates` · `thread-manager-sample` | agents 池 + 交接单 + 写权互斥锁 |
| 会话/记忆 | `memories` · `thread-store` · `rollout` · `rollout-trace` · `history` · `message-history` | auto-memory + session log |
| 隔离/安全 | `sandboxing` · `execpolicy` · `linux-sandbox` · `windows-sandbox-rs` · `bwrap` · `process-hardening` · `guardian-context` · `shell-escalation` | 权限模式 + PreToolUse 阻断 hook |
| 工程面 | `worktree` · `git-utils` · `file-watcher` · `apply-patch` · `code-mode`(+host/protocol/runtime) | worktree 三路隔离工序 |

**`worktree` 是原生 crate 而非外挂**——本工作区 UWAcomm / UWAcomm_usbl 的多 worktree 隔离目前靠人工约定 + memory 守则（auto-memory `feedback_uwacomm_worktree_ownership`），值得看它把哪些约定固化进了引擎。

## 最有操作价值的一条：skills 走开放标准

Codex 的 skill **不是私有格式**，而是 [agentskills.io](https://agentskills.io) 「开放代理技能标准」：

```
my-skill/
├── SKILL.md          # 必需：frontmatter(name + description) + 指令正文
├── scripts/          # 可选
├── references/       # 可选
├── assets/           # 可选
└── agents/openai.yaml  # 可选：UI 配置 / 依赖声明
```

扫描优先级（近者胜）：`$CWD/.agents/skills` → `$REPO_ROOT/.agents/skills` → `$HOME/.agents/skills` → `/etc/codex/skills` → 内置。触发分**显式**（`$skill-name` 或 `/skills`）与**隐式**（按 `description` 自动匹配）——与 Claude Code「description 决定触发质量」同构。

**结论：与本工作区 `~/.claude/skills/` 的 32 个 skill 结构同构，存在跨引擎复用可能。** 活证据是 [[tt-a1i-archify]]——同一份 SKILL.md 同时声明支持 Claude Code / Cursor / Codex CLI / OpenCode。

差异要点（迁移前须验）：
- **路径不同**：`.agents/skills` vs `.claude/skills`，需软链或复制，无自动互认。
- **`paths:` 触发**（本工作区 `llm-wiki` 依赖的路径自动激活）是 Claude Code 扩展字段，**开放标准未收录**，跨引擎会失效。
- flowgen 家族依赖 **pywin32 + 本机 Visio COM**，与引擎无关，理论上跨引擎可用；但其 SKILL.md 里的 Claude 专有约定（Skill 工具调用形态）需实测。

## 与已有对照组的关系

| 引擎 | 开源状态 | 内核语言 | 扩展哲学 |
|---|---|---|---|
| Claude Code | 闭源（harness 不开放） | — | skills / hooks / subagents / MCP 四机制并列 |
| [[deepseek-ai-deepseek-harness]] | MIT，全开源 | TypeScript（Cordis） | **一切皆插件**，无特权核心 |
| **openai/codex** | **Apache-2.0，引擎开源（2026-08-20）** | **Rust** | crate 分域 + 开放 skill 标准 + SDK 外嵌 |

三者共同印证 [[../concepts/harness-engineering]] 的跨引擎设计模式表（分层覆盖 / 生命周期 hook / 子代理隔离 / 单一事实源 / 按需加载指令）——五项在三个引擎里全部出现，可视为 harness 的**收敛式设计**。

内网国产化线上，Codex 与 [[deepseek-ai-deepseek-harness]] 属同一候选组（自建底座），与 [[zhongan-llm-platform-ppt]]（商用平台采购）构成两条路线。

## 待观察 / 下一步

- **跨引擎 skill 复用实测**：取 1 个无 Claude 专有依赖的 skill（如 `tech-requirements`）软链到 `$HOME/.agents/skills` 验证 Codex 能否加载——这是把 32 skill 资产从单引擎解绑的最小验证。
- `worktree` / `agent-roles` / `collaboration-mode-templates` 三 crate 的实现，对照本体系交接单 + 写权互斥协议是否有可借鉴的固化方式。
- SDK（`sdk/`）可否作为 UWAcomm 类长流程仿真的批处理编排入口（对照现有 MATLAB runner 工序）。
- 高频迭代（当日仍在推），架构结论需定期回访。

## 相关页面

- [[../concepts/harness-engineering]] — 本页的概念归属（造 harness vs 用 harness 两层）
- [[deepseek-ai-deepseek-harness]] · [[zhongan-llm-platform-ppt]] — 对照组另两员
- [[tt-a1i-archify]] — 跨引擎 skill 的活证据
- [[../concepts/skills-vs-commands]] · [[../concepts/skill-layered-resources]] — skill 机制与分层判据
- [[../agents/claude-codex-collaboration]] — 本体系双 agent 分工协议
- [[../entities/claude-code]] — 对照引擎
