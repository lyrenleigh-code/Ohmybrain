---
type: concept
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, Agent, 编排, 架构]
---

# Claude Code 子代理编排

## 定义

子代理（subagent）是在**独立上下文窗口**中运行的自治代理。通过 `description` 可被主 Claude 自动调用（PROACTIVELY），也可通过 `Agent` 工具显式调用。与 Command / Skill 不同，子代理拥有独立的上下文、工具集、模型、权限模式和持久记忆。

## 何时用子代理

- 任务是**自治多步**的——代理要探索、决策、执行，不需要每步都请示
- 需要**上下文隔离**——工作不污染主会话窗口
- 需要**跨会话持久记忆**（比如持续学习的 code reviewer）
- 想通过 Skill 预加载**领域知识**而不占主上下文
- 任务适合**后台运行**或在 **git worktree** 中隔离执行
- 需要**工具限制**或**不同的权限模式**（`acceptEdits`、`plan` 等）

## Subagent Frontmatter（16 字段）

| 字段 | 说明 |
|------|------|
| `name` | 唯一标识（小写、连字符） |
| `description` | 何时调用。包含 `"PROACTIVELY"` 可鼓励主 Claude 自动调用 |
| `tools` | 工具白名单。支持 `Agent(agent_type)` 限制可生成的子代理 |
| `disallowedTools` | 工具黑名单 |
| `model` | `sonnet` / `opus` / `haiku` / 完整 ID / `inherit`（默认） |
| `permissionMode` | `default` / `acceptEdits` / `auto` / `dontAsk` / `bypassPermissions` / `plan` |
| `maxTurns` | 最大代理轮次 |
| `skills` | 启动时预加载的 skill 列表（完整内容注入上下文，而非只注册） |
| `mcpServers` | 本子代理专用的 MCP 服务器 |
| `hooks` | 本子代理作用域的生命周期 hooks |
| `memory` | 持久记忆作用域：`user` / `project` / `local` |
| `background` | `true` = 始终后台运行 |
| `effort` | 覆盖会话的 effort level（`low`/`medium`/`high`/`max`） |
| `isolation` | `"worktree"` = 在临时 git worktree 中运行（无改动自动清理） |
| `initialPrompt` | 作为主会话代理运行时（`--agent`）自动提交的首条用户 turn |
| `color` | CLI 显示颜色 |

## 官方内置子代理（5 个）

| Agent | Model | Tools | 用途 |
|-------|-------|-------|------|
| `general-purpose` | inherit | 全部 | 复杂多步任务默认代理 |
| `Explore` | haiku | 只读 | 代码库快速探索搜索 |
| `Plan` | inherit | 只读 | 规划模式下的先研究后设计 |
| `statusline-setup` | sonnet | Read/Edit | 配置状态栏 |
| `claude-code-guide` | haiku | Glob/Grep/Read/WebFetch/WebSearch | 回答 Claude Code / SDK / API 问题 |

## Command → Agent → Skill 编排模式

三种扩展机制分层配合，形成清晰的编排流：

```
用户触发 /command
    ↓
Command 编排工作流（主上下文，处理用户交互）
    ↓
Command 调 Agent（独立上下文，自治取数/决策）
    ↓
Agent 用预加载的 Skill（agent skill，作为领域知识）
    ↓
Command 调 Skill（直接调用，负责生成输出）
```

### 参考示例：天气系统

```
/weather-orchestrator (Command)
  │ 询问用户 °C / °F
  │
  ├─ Agent tool ──→ weather-agent (Agent)
  │                   预加载 skill: weather-fetcher
  │                   从 Open-Meteo 取温度
  │                   返回 temp + unit
  │
  └─ Skill tool ──→ weather-svg-creator (Skill)
                      生成 weather.svg + output.md
```

关键设计原则：

1. **两种 skill 模式**：agent skill（预加载成代理的领域知识）vs skill（通过 Skill tool 独立调用生成输出）
2. **Command 做协调**：处理用户交互、调度 Agent / Skill
3. **Agent 做取数**：在独立上下文中自治决策，不污染主上下文
4. **Skill 做输出**：接收主上下文数据，生成最终产物
5. **单一职责**：Fetch（Agent）→ Render（Skill），每层职责清晰

## 子代理约束

> 子代理**不能**通过 bash 命令启动其他子代理。必须使用 `Agent` 工具（v2.1.63 起从 `Task` 改名，`Task(...)` 仍是别名）：

```
Agent(subagent_type="agent-name", description="...", prompt="...", model="haiku")
```

**提示工程要点**：子代理定义中对工具使用要**明确**。避免用"launch"等模糊动词——可能被误解为 bash 命令。

## 并行代理（Agent Teams，v2.1.90+ 实验）

多个子代理可在同一代码库上并行工作。启用：

```json
// ~/.claude/settings.json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

配置目录：`~/.claude/teams/{team-name}/`。模式：
- **In-process**（默认）：所有队友运行在同一终端
- **Split panes**：每个队友一个独立面板，需 tmux 或 iTerm2（VS Code 终端不支持）

对于独立可并行的子任务（如同时跑安全审查 + 性能审查 + 类型检查），单条消息中发起多个 `Agent` 工具调用可获得自然并行。

## 与 Ohmybrain 的连接

- 本仓已有 `/ingest`、`/promote-answer`、`/lint-wiki` 等 Command
- 候选重构：将**自治探索型**的部分（如 ingest 新论文需要读-判-分类-交叉引用）抽成 Agent
- 给 code-reviewer 类代理设 `memory: user`，跨项目积累审查经验

## 相关概念

- [[skills-vs-commands]] — 三机制选择决策
- [[claude-hooks-architecture]] — 生命周期 hooks（子代理也有独立 hooks 作用域）

## 同源范式的另一实现：Hermes Agent

[[nousresearch-hermes-agent|Hermes Agent]]（Nous Research 开源）用 **`delegate_tool`** + 隔离子代理实现同样的编排：子代理独立进程、父代理可通过 RPC 编程式调用工具把多步管道折叠成零上下文成本的单轮。值得对照学习的差异点：

- Hermes 子代理派生更偏**程序化**（可脚本化，不靠模型决策）
- 子代理活动通过 `delegate_task` 向父传播——见其 `agent/display.py` 和 `_run_single_child()` 实现
- 单一 `CommandDef` 列表驱动多终端（CLI / 16 消息平台 / autocomplete），同一套编排跨平台复用


## 子代理内部自律：Pre-Tool-Call + Error Recovery

除编排模式外，单个子代理内部也需要**失败处理协议**。[[yizhiyanhua-ai-fireworks-tech-graph]] 示范了两段硬规约：

- **Pre-Tool-Call Checklist**：工具调用前过 3 个 YES/NO 问题（完整命令？全部参数？语法无误？），任一 NO 就 STOP 不调工具
- **Error Recovery Protocol**：第一次分析根因、第二次切换方法、第三次停并报告；明令 Never retry 同一失败命令

**对 Ohmybrain 直接对症**：`wiki-ingester` agent 遇 PDF 乱码会反复重试 PyMuPDF。移植此协议可立即堵住。预估 30 分钟可完成。详见 [[yizhiyanhua-ai-fireworks-tech-graph]] 的"对 Ohmybrain 的启发 §3"。

## 规模化工程实践：ECC 48 agents 生态

[[affaan-m-everything-claude-code|Everything Claude Code (ECC)]] 把子代理编排从"3-5 个典型代理"推到 **48 个生产级代理**的规模，形成可直接复用的生态样本：

- **分工颗粒**：除 planner / architect / tdd-guide / code-reviewer 等通用代理外，按**语言**拆 reviewer + build-resolver 对（typescript / python / go / java / kotlin / rust / cpp / dart / csharp / php / perl），按**场景**拆专精代理（`loop-operator` 自治循环、`harness-optimizer` harness 配置调优、`chief-of-staff` 通讯分诊、`silent-failure-hunter` 无声失败扫雷、`seo-specialist` 运营、`gan-evaluator/generator/planner` 三元对抗工作流）
- **记忆分层**：结合 Claude Code v2.1.33+ 原生 Agent Memory（user/project/local）+ ECC 独有的 **Instinct 系统**（PreToolUse observer hook + confidence scoring 累积 + `/evolve` 聚类为 skill），形成"短期原生记忆 + 长期学习循环"双层
- **启示**：Ohmybrain 现有 wiki-ingester 单代理可按该模式拆分——论文、代码仓、视频转录各自独立代理（可预加载对应 skill），配合 `memory: user` 跨摄入累积经验。

## 来源

- 参考仓库：`raw/repos/claude-code-best-practice/best-practice/claude-subagents.md`
- 编排示例：`raw/repos/claude-code-best-practice/orchestration-workflow/orchestration-workflow.md`
- 对比报告：`raw/repos/claude-code-best-practice/reports/claude-agent-command-skill.md`
- Agent Memory：`raw/repos/claude-code-best-practice/reports/claude-agent-memory.md`
- 另一实现参考：[[nousresearch-hermes-agent]]
- 生产级规模化范本：[[affaan-m-everything-claude-code]]（48 agents + instinct 系统）
- Phase 0 + Subagent Reporting Contract 范本：[[thedotmack-claude-mem]]（make-plan / do 强约束）
- 相关实体：[[claude-code]]
- 相关 summary：[[claude-code-best-practice]]、[[affaan-m-everything-claude-code]]
- 子代理自律范本：[[yizhiyanhua-ai-fireworks-tech-graph]]（Pre-Tool-Call Checklist + Error Recovery Protocol）
- founder 视角的 orchestrator 人格化：[[anthropic-2026-founders-playbook]]（Anthropic 2026，founder = orchestrator of agents 命题）
