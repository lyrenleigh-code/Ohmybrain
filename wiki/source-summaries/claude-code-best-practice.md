---
type: source-summary
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, 最佳实践, Agent, Skill, Command, Hook, MCP]
source-type: reference-repository
source-path: raw/repos/claude-code-best-practice
---

# Claude Code Best Practice — 参考实现库

## 来源信息

- **类型**：参考/模板仓库（GitHub Trending #1）
- **上游**：`github.com/shanraisshan/claude-code-best-practice`
- **本地路径**：`raw/repos/claude-code-best-practice`
- **对标版本**：Claude Code v2.1.101（2026-04-13）
- **定位**：从 vibe coding 走向 agentic engineering 的配置最佳实践集

## 核心价值

这是一个 **"可直接运行的最佳实践参考"**：每条最佳实践（`best-practice/*.md`）对应一个真实可用的实现（`.claude/` 目录下的 agent/command/skill/hook 文件）。不是文档，是**可抄可改的模板**。

## 目录地图

| 目录 | 内容 | 用途 |
|------|------|------|
| `best-practice/` | 9 篇最佳实践清单（frontmatter + 官方表） | subagents / commands / skills / memory / MCP / settings / power-ups / CLI flags |
| `implementation/` | 对应 best-practice 的落地实现 | 每个 `*-implementation.md` 指向仓内实际 `.claude/*` 文件 |
| `reports/` | 9 篇深度报告 | 三种扩展机制对比、agent memory、global vs project、CLAUDE 在大 monorepo 的加载、Chrome vs DevTools 等 |
| `tips/` | 7 篇 tips（Boris Cherny 为主） | 高手用法，按发布时间组织 |
| `orchestration-workflow/` | Command → Agent → Skill 工作流示例 | 天气系统：SVG 生成 + 外部 API 调用 |
| `agent-teams/` | Agent Teams 多代理协作示例 | v2.1.90+ 实验特性 |
| `.claude/` | 仓内完整配置 | agents/commands/skills/hooks/rules 完整可运行样板 |
| `.mcp.json` | MCP 服务器配置 | 推荐的 5 个日常 MCP 服务器配置示例 |
| `changelog/` | Claude Code 版本变更归档 | 按特性分类 |

## 三种扩展机制速览

Claude Code 提供三种功能扩展机制，差异核心在**上下文隔离**与**触发方式**：

| 维度 | Agent（子代理） | Command（命令） | Skill（技能） |
|------|----------------|----------------|--------------|
| 文件路径 | `.claude/agents/<name>.md` | `.claude/commands/<name>.md` | `.claude/skills/<name>/SKILL.md` |
| 上下文 | 独立进程（隔离） | 主会话内联 | 主会话内联（可 `context: fork`） |
| 自动触发 | ✅ 通过 `description` | ❌ 仅用户 `/` 显式 | ✅ 通过 `description` |
| `/` 菜单可见 | ❌ | ✅ 总是 | ✅ 默认可见 |
| Frontmatter 字段数 | 16 | 13 | 13 |
| 可预加载 Skill | ✅ `skills:` | ❌ | ❌ |
| 持久记忆 | ✅ `memory: user/project/local` | ❌ | ❌ |

完整对比见 [[skills-vs-commands]]。

## 核心模式：Command → Agent → Skill

仓内用一个天气系统示例演示分层编排模式：

```
/weather-orchestrator (Command，入口，询问 °C/°F)
    ↓ Agent tool
weather-agent (Agent，独立上下文 + 预加载 weather-fetcher skill)
    ↓ Skill tool
weather-svg-creator (Skill，生成 SVG 文件)
```

关键解耦原则：**Command 编排 / Agent 取数 / Skill 输出**，每层单一职责。详见 [[subagents-orchestration]]。

## Frontmatter 字段要点

### Subagent（16 字段）

必填：`name`、`description`（含 `"PROACTIVELY"` 可鼓励自动调用）。
关键可选：`tools`（支持 `Agent(agent_type)` 限制可生成的子代理）、`skills`（启动时注入完整 skill 内容）、`memory`（`user/project/local`）、`mcpServers`、`hooks`、`isolation: "worktree"`、`effort`、`maxTurns`、`initialPrompt`。

### Command（13 字段）

关键：`allowed-tools`（本命令激活时免权限弹窗的工具白名单）、`context: fork`（启用隔离子代理）、`shell`（`bash`/`powershell`）、`paths`（glob 限定激活范围）。

### Skill（13 字段）

与 Command 几乎同构，核心差异：可被 Claude 自动调用（除非 `disable-model-invocation: true`）、可用 `user-invocable: false` 变为背景知识只给 Agent 预加载。

## 配置优先级（从高到低）

```
1. 命令行 flag
2. .claude/settings.local.json    (项目 / 个人 / git-ignored)
3. .claude/settings.json          (项目 / 团队共享)
4. ~/.claude/settings.local.json  (全局 / 个人)
5. ~/.claude/settings.json        (全局 / 默认)
6. managed-settings.json          (组织强制，不可覆盖)
```

`deny` 规则拥有最高安全优先级，低优先级的 `allow` 无法覆盖。完整对比见 `reports/claude-global-vs-project-settings.md`。

## CLAUDE.md 在 Monorepo 的加载

- **祖先上行加载**：启动时从 CWD 向文件系统根部遍历，所有 `CLAUDE.md` 立即加载
- **后代懒加载**：子目录的 `CLAUDE.md` 只在读取该目录文件时加载
- **兄弟目录**：永不加载
- **全局层**：`~/.claude/CLAUDE.md` 对所有会话生效

含义：根目录放共享规范，子目录放组件特有规范，`CLAUDE.local.md` 放个人偏好（加入 `.gitignore`）。

## 日常推荐的 MCP 服务器（5 个）

| MCP | 用途 | 场景 |
|-----|------|------|
| **Context7** | 拉取最新库文档注入上下文 | 防止幻觉过时 API |
| **Playwright** | 浏览器自动化 | UI 测试、截图、表单验证 |
| **Claude in Chrome** | 连接真实 Chrome | 前端调试最有效 |
| **DeepWiki** | 抓 GitHub 仓库结构文档 | 快速理解陌生项目 |
| **Excalidraw** | Prompt → 手绘架构图 | 设计文档配图 |

> Reddit 用户原话："之前装了 15 个 MCP 觉得越多越好，最后日常只用 4 个。" MCP 不是越多越好。

## Agent Memory（v2.1.33）

每个子代理可有独立持久记忆：

| Scope | 存储位置 | 适用 |
|-------|---------|------|
| `user` | `~/.claude/agent-memory/<agent>/` | 跨项目知识（推荐默认） |
| `project` | `.claude/agent-memory/<agent>/` | 团队共享的项目知识 |
| `local` | `.claude/agent-memory-local/<agent>/` | 个人的项目知识 |

启动时加载 `MEMORY.md` 前 200 行，Agent 自行读写更新。与 `CLAUDE.md`（人写，全局可读）、auto-memory（主 Claude 写，主 Claude 读）互补。

## Tasks 系统（v2.1.16，取代旧 TodoWrite）

存储在 `~/.claude/tasks/`（本地文件系统），支持依赖图、跨会话共享（`CLAUDE_CODE_TASK_LIST_ID` 环境变量）、崩溃恢复。工具：`TaskCreate`、`TaskGet`、`TaskUpdate`、`TaskList`。

## Agent Teams（v2.1.90+，实验特性）

多个 Claude Code 会话协同工作。启用：

```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

配置在 `~/.claude/teams/{team-name}/`，支持 in-process（默认）和 split panes（需 tmux / iTerm2）。

## 工作流最佳实践（仓主经验）

1. 单个 `CLAUDE.md` 保持 < 200 行，模型遵循度更高
2. 用 Command 编排工作流，而不是做独立 Agent
3. 创建**功能特定**的子代理 + 预加载 skill，而非通用代理
4. 上下文用到 ~50% 时手动 `/compact`
5. 复杂任务先进入 `plan` 模式
6. 多步任务用**人工把关的 task list**
7. 拆子任务到能在 50% 上下文内完成的粒度
8. 提交：**每个文件单独一个 commit**（便于 review/revert/cherry-pick）

## Boris Cherny 高价值 tips（摘要）

- `/loop 5m /babysit`、`/loop 30m /slack-feedback` 等让 Claude 全天跑后台作业
- Hooks 用途：`SessionStart` 动态加载上下文、`PreToolUse` 日志化所有 bash 命令、`PermissionRequest` 路由到 WhatsApp 远程批准、`Stop` 自动续跑
- 前端工作**一定给 Claude 一个浏览器**（Chrome 扩展 / Desktop 内置浏览器）
- `/branch` 或 `claude --resume <id> --fork-session` 分叉会话
- Desktop app 自动启动并在内置浏览器测试 web server

完整 tips 在 `tips/claude-boris-15-tips-30-mar-26.md`。

## 关键报告

- `reports/claude-agent-command-skill.md` — 三机制对比，含 "当前时间" 示例演示解析优先级
- `reports/claude-agent-memory.md` — Agent memory frontmatter 详解
- `reports/claude-global-vs-project-settings.md` — 全局 vs 项目配置的完整对照
- `reports/claude-skills-for-larger-mono-repos.md` — 大 monorepo 中 Skill 的发现机制
- `reports/claude-in-chrome-v-chrome-devtools-mcp.md` — 浏览器调试 MCP 对比
- `reports/claude-advanced-tool-use.md` — Tool use 进阶
- `reports/claude-agent-sdk-vs-cli-system-prompts.md` — Agent SDK vs CLI 的 system prompt 差异
- `reports/llm-day-to-day-degradation.md` — LLM 日常退化观察

## 对 Ohmybrain 的启示

1. **三机制选择**：当前 Ohmybrain `.claude/` 主要是 `rules/` 和 `commands/`，考虑把 `/ingest`、`/promote-answer`、`/lint-wiki` 中涉及 **自主探索 + 多步决策** 的部分改为 Agent，让其在独立上下文运行
2. **Skill 化高频知识**：`llm-wiki.md` rule 中的 ingest/query/lint 协议可以抽成 skill（`paths:` 限定在 `wiki/**`），让 Claude 自动匹配
3. **Agent Memory**：给 code-reviewer 类代理加 `memory: user`，积累跨项目 review 经验
4. **MCP 参考**：仓内 `.mcp.json` 给出干净的 5 MCP 配置示例，可借鉴精简本仓 MCP
5. **Tasks 系统**：本会话已在用，替代了旧 TodoWrite

## 派生概念页

- [[subagents-orchestration]] — 子代理编排模式（Command → Agent → Skill）
- [[skills-vs-commands]] — Skill vs Command vs Agent 三机制对比
- [[claude-hooks-architecture]] — Hooks 架构与生命周期事件

## 来源

- 参考仓库：`raw/repos/claude-code-best-practice/README.md` + `best-practice/*` + `reports/*`
- 主要对接上游：`code.claude.com/docs/en/`（Claude Code 官方文档）
- 相关实体：[[claude-code]]

## 相关范本

- [[yizhiyanhua-ai-fireworks-tech-graph]] — 单一 Skill 深度范本（本仓侧重配置集总，fireworks 侧重单 skill 工程化）
