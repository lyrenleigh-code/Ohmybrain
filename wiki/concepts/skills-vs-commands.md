---
type: concept
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, Skill, Command, Agent, 对比]
---

# Skills vs Commands vs Agents — 三机制对比

## 核心差异

Claude Code 有三种功能扩展机制，差异点在**上下文位置**、**触发方式**、**可见性**：

| 维度 | Agent | Command | Skill |
|------|-------|---------|-------|
| 文件位置 | `.claude/agents/<name>.md` | `.claude/commands/<name>.md` | `.claude/skills/<name>/SKILL.md` |
| **上下文** | 独立子代理进程 | 主会话内联 | 主会话内联（可 `context: fork` 改为子代理） |
| **用户触发** | 不在 `/` 菜单（通过 Agent tool 或被代理调用） | `/command-name` | `/skill-name`（除非 `user-invocable: false`） |
| **Claude 自动触发** | ✅ 通过 `description` | ❌ | ✅ 通过 `description`（除非 `disable-model-invocation: true`） |
| 参数 | `prompt` 参数 | `$ARGUMENTS`、`$0`、`$1` | `$ARGUMENTS`、`$0`、`$1` |
| 动态上下文注入 | ❌ | ✅ `` !`command` `` | ✅ `` !`command` `` |
| 独立上下文 | 始终 | 从不 | 可选（`context: fork`） |
| 模型覆盖 | `model:` | `model:` | `model:` |
| 工具限制 | `tools:` / `disallowedTools:` | `allowed-tools:` | `allowed-tools:` |
| Hooks | `hooks:` | — | `hooks:` |
| 记忆 | `memory:`（user/project/local） | — | — |
| 可预加载 Skill | ✅ `skills:` | — | — |
| MCP servers | `mcpServers:` | — | — |

## 决策树

```
需要独立上下文 / 自治多步 / 持久记忆？
    ├─ 是 → Agent
    └─ 否 ↓
用户显式触发 / 不希望自动调用？
    ├─ 是 → Command（永不自动）
    └─ 否 ↓
希望 Claude 根据意图自动调用？
    └─ Skill（默认即可自动）
```

## 何时用 Command

- 需要**用户显式触发**的工作流入口
- 工作流涉及**编排**其他 Agent / Skill
- 希望**上下文精简**——命令内容在用户触发前不进入会话上下文

**例**：`/weather-orchestrator`——用户触发，先问 °C/°F，再调 Agent，再调 Skill。

## 何时用 Agent

- 任务是**自治多步**——需要探索、决策、执行
- 需要**上下文隔离**——工作不污染主会话
- 需要**跨会话持久记忆**（learn-over-time 型代理）
- 通过 Skill **预加载领域知识**但不占主上下文
- 任务要在**后台**或 **git worktree** 运行
- 需要**工具限制**或**不同权限模式**

**例**：`weather-agent`——独立上下文、预加载 `weather-fetcher` skill、工具受限、自治取数。

## 何时用 Skill

- 希望 Claude **根据用户意图自动调用**——skill description 注入主上下文用于语义匹配
- 任务是**可复用过程**，可被多处调用（command、agent、Claude 自身）
- 需要给特定 Agent **预加载**领域知识

**例**：`weather-svg-creator`——用户问"给我做张天气卡"时 Claude 自动调用；也可从 command 里调。

## 解析优先级

当同一意图有多个机制匹配时，Claude 倾向**最轻量**的方案：

```
1. Skill（内联，无上下文开销）      ← 最优先
2. Agent（独立上下文，自治）         ← skill 不可用或任务复杂时
3. Command（永不自动，只等用户打 /） ← 仅在用户显式触发时
```

## 工作示例："当前时间是多少？"

同一仓库同时定义了 `time-command`、`time-agent`、`time-skill`，用户输入 "What is the current time?"：

| 机制 | 是否触发 | 原因 |
|------|---------|------|
| `time-command` | ❌ | 命令**永不**自动触发；除非用户打 `/time-command` |
| `time-agent` | ⚠ 可能 | description 匹配，Claude 可能通过 Agent tool 启动，但**占独立上下文**——对简单任务偏重 |
| `time-skill` | ✅ 最可能 | description 匹配，**内联执行无上下文开销**——最轻量匹配 |

**如果 skill 设了 `disable-model-invocation: true`** → Agent 成了唯一自动可用选项，Claude 会启 `time-agent`（代价：一次性开独立上下文只为跑一行 bash）。

**如果 skill 和 agent 都禁了自动调用** → 没有任何机制自动触发，Claude 退回通用知识直接跑 `TZ='Asia/Karachi' date`。用户需打 `/time-command` 或 `/time-skill` 显式用。

## Frontmatter 对照

### Agent（16 字段）

```yaml
---
name: my-agent
description: Use this agent PROACTIVELY when...
tools: Read, Write, Edit, Bash
model: sonnet
maxTurns: 10
permissionMode: acceptEdits
memory: user
skills:
  - my-skill
---
```

### Command（13 字段）

```yaml
---
description: Do something useful
argument-hint: [issue-number]
allowed-tools: Read, Edit, Bash(gh *)
model: sonnet
---
```

### Skill（13 字段）

```yaml
---
name: my-skill
description: Do something when the user asks for...
argument-hint: [file-path]
disable-model-invocation: false
user-invocable: true
allowed-tools: Read, Grep, Glob
model: sonnet
context: fork
agent: general-purpose
paths: "src/**/*.ts"
---
```

关键 Skill 专属字段：

- `disable-model-invocation: true` → 禁止 Claude 自动调用，只能用户 `/` 触发
- `user-invocable: false` → 从 `/` 菜单隐藏，变成**背景知识**（常用于让 Agent 预加载）
- `paths: "src/**/*.ts"` → glob 限定自动激活范围，Claude 只在处理匹配文件时才加载

## 官方内置

### 5 个 bundled skills

- `simplify` — 代码复用/质量/效率审查
- `batch` — 批量跑命令
- `debug` — 调试失败命令
- `loop` — 周期运行提示词/命令（最长 3 天）
- `claude-api` — Claude API / Anthropic SDK 开发辅助

### 5 个官方 subagents

`general-purpose`、`Explore`、`Plan`、`statusline-setup`、`claude-code-guide`。

### 69 个官方 slash commands

分类：Auth（5）、Config（11）、Context（7）、Debug（6）、Export（2）、Extensions（8）、Memory（1）、Model（6）、Project（5）、Remote（10）、Session（8）。

## 对 Ohmybrain 的启示

当前 `.claude/commands/` 下的 `/ingest`、`/lint-wiki` 等：

- **保留为 Command**（用户显式触发的工作流入口）
- **但内部可以调 Agent**：ingest 新论文的"读-分类-交叉引用-写回"可改为 Agent（自治多步 + 独立上下文）
- **把 llm-wiki.md rule 抽成 skill**：用 `paths: "wiki/**"` 让 Claude 在改 wiki 时自动激活

## 相关概念

- [[subagents-orchestration]] — Agent 深入 + 编排模式
- [[claude-hooks-architecture]] — 三种机制都可挂 hooks

## 开放 Skill 标准：agentskills.io

Anthropic Claude Code 的 skill 是**私有格式**。[[nousresearch-hermes-agent|Hermes Agent]] 实现了 [agentskills.io](https://agentskills.io) 开放规范——26 个领域 skill 开箱即用（autonomous-ai-agents / data-science / devops / github / mcp / media / research / security 等），可在不同 agent 之间互通。若 Ohmybrain 想保持 skill 可移植性，值得关注这个标准。

## 来源

- 核心对比报告：`raw/repos/claude-code-best-practice/reports/claude-agent-command-skill.md`
- Subagent 规格：`raw/repos/claude-code-best-practice/best-practice/claude-subagents.md`
- Command 规格：`raw/repos/claude-code-best-practice/best-practice/claude-commands.md`
- Skill 规格：`raw/repos/claude-code-best-practice/best-practice/claude-skills.md`
- 开放标准参考：[[nousresearch-hermes-agent]]（agentskills.io 兼容实现）
- 相关 summary：[[claude-code-best-practice]]
- 相关实体：[[claude-code]]
