---
type: concept
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, Hook, 生命周期, 自动化]
---

# Claude Code Hooks 架构

## 定义

Hook 是在 **Claude Code 代理生命周期特定事件上触发**的用户定义处理器（脚本、HTTP 调用、prompt、agent）。Hook 运行在**代理循环之外**——不消耗模型上下文，不参与推理，但能强制执行规则、注入上下文、拦截操作。

## 核心价值

> Hook 把"请 Claude 记得做 X"转化为"每次都会自动做 X"——**确定性** 替代 **依从性**。

规则写进 CLAUDE.md 依赖模型遵循（概率），hook 写进 settings 由 harness 强制执行（确定）。

## 生命周期事件（15 个）

| 事件 | 触发时机 | 典型用途 |
|------|---------|---------|
| `SessionStart` | 会话启动 | 动态注入上下文（加载最新 log、环境信息、待办任务） |
| `SessionEnd` | 会话结束 | 保存会话摘要、归档 |
| `PreToolUse` | 工具执行前 | 日志记录、参数校验/修改、危险操作拦截 |
| `PostToolUse` | 工具执行后 | 自动格式化（Prettier/eslint）、增量检查、sync index |
| `UserPromptSubmit` | 用户提交消息时 | 预处理提示、加载相关上下文 |
| `Notification` | Claude 发出通知 | 分发到 Slack/WhatsApp/桌面 |
| `Stop` | 会话/任务结束 | 最终 build 验证、"poke" 让 Claude 继续 |
| `SubagentStart` | 子代理启动 | 子代理级别的 onboarding |
| `SubagentStop` | 子代理结束 | 子代理输出后处理 |
| `PreCompact` | 自动压缩前 | 保存关键上下文到持久存储 |
| `Setup` | 首次配置 | 初始化检查 |
| `PermissionRequest` | 权限询问时 | 路由到外部批准（如 WhatsApp）、自动批/拒 |
| `TeammateIdle` | Agent Team 队友空闲 | 派发新任务 |
| `TaskCompleted` | Task 完成时 | 通知、归档、触发后续任务 |
| `ConfigChange` | 配置变更 | 重载、备份 |

## Hook 处理器类型

Hook 值可以是：

- **Shell 命令**：在 stdin 上收到 JSON 事件数据，stdout 作为响应，exit code 2 = 阻断
- **HTTP 端点**：POST JSON 到 URL
- **Prompt**：把一段 prompt 注入当前会话
- **Agent**：启动指定子代理处理事件

## 作用域层级（从窄到宽）

| 作用域 | 配置位置 | 何时生效 |
|-------|---------|---------|
| Skill | skill 的 `hooks:` frontmatter | 仅该 skill 激活时 |
| Subagent | agent 的 `hooks:` frontmatter | 仅该子代理运行时 |
| Command | command 的 `hooks:` frontmatter | 仅该命令执行时 |
| 项目 | `.claude/settings.json` + 项目 hooks 目录 | 本项目所有会话 |
| 用户 | `~/.claude/settings.json` + `~/.claude/hooks/` | 所有项目 |

## 配置示例

### PostToolUse：自动格式化

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "pnpm prettier --write \"$FILE_PATH\""
      }
    ]
  }
}
```

### PreToolUse：拦截超大写入

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "command": "node check-file-size.js",
        "description": "Block writes > 800 lines"
      }
    ]
  }
}
```

处理器读 stdin 上的 JSON（含 `tool_input.content`），超限输出 `exit 2` + stderr 说明原因阻断。

### SessionStart：动态注入上下文

```json
{
  "hooks": {
    "SessionStart": [
      {
        "command": "cat project-state.json && git log -5 --oneline"
      }
    ]
  }
}
```

Claude 启动时 stdout 内容会进入上下文。

### Stop：最终构建验证

```json
{
  "hooks": {
    "Stop": [
      { "command": "pnpm build" }
    ]
  }
}
```

## Boris Cherny 的经典 Hook 用法

1. **`SessionStart`** 每次启动动态注入项目上下文
2. **`PreToolUse`** 日志化模型运行的**每条 bash 命令**（审计 + 回放）
3. **`PermissionRequest`** 路由到 WhatsApp 手机批准/拒绝
4. **`Stop`** 自动"poke" 让 Claude 不要停

## 禁用 Hook

- 全局禁用：`.claude/settings.local.json` 设 `"disableAllHooks": true`
- 单独禁用：在 `hooks-config.json` 里置对应项为 `false`

## 配置层叠

项目层 `hooks-config.json` 是团队共享，个人在 `hooks-config.local.json`（git-ignored）覆盖：

```
hooks-config.local.json  >  hooks-config.json
```

## 与规则/记忆的分工

| 机制 | 性质 | 执行 |
|------|------|------|
| **CLAUDE.md** | 静态规则 | 依赖模型读后遵循（概率） |
| **Rules** (`.claude/rules/`) | 静态规则 | 同上 |
| **Hooks** | 动态处理器 | harness 确定性执行 |
| **Agent memory** | 动态知识 | 代理自己读写 |

**规则归规则，hook 归 hook**：
- 只写文档的规则 → 放 CLAUDE.md
- 必须机器强制的规则（格式化、构建验证、危险操作拦截） → 放 hook

## 对 Ohmybrain 的启示

候选 hook：

1. **`PostToolUse: Write|Edit`** on `wiki/**` → 自动运行 `scripts/lint_wiki.py`
2. **`PostToolUse: Write|Edit`** on `wiki/index.md` → 跑 `sync_index.py` 检查页面数
3. **`SessionStart`** → 注入 `wiki/log.md` 最近 3 条记录 + 当前项目列表
4. **`PreToolUse: Write`** on `raw/**` → 若非用户明确要求则阻断（强化 raw 只读规则）
5. **`Stop`** → 提示是否需要 `/promote-answer` 写回 Hub

## 相关概念

- [[subagents-orchestration]] — 子代理有独立 hook 作用域
- [[skills-vs-commands]] — Skill 和 Command 也各自可挂 hook

## 平行架构：Hermes Agent Gateway Hooks

[[nousresearch-hermes-agent|Hermes Agent]] 在其消息网关层有一套独立 hook 系统（`gateway/hooks.py` + `gateway/builtin_hooks/`），与主 agent 循环解耦。典型用途：background 进程完成通知、状态事件、交付确认。这种**"主循环 hook + 网关 hook 双层"** 的设计值得对照——Claude Code 当前 hook 在代理生命周期层统一，未区分主会话与网关。


## 内部自律的镜像：Skill 的 Pre-Tool-Call Checklist

Hook 是**harness 从外部强制**规则，但同样的哲学也可以做成 **skill 内部自律条款**。[[yizhiyanhua-ai-fireworks-tech-graph]] 范本在 SKILL.md 里硬编码了：

- **Pre-Tool-Call Checklist**：工具调用前逐项过 3 个 YES/NO 问题，任一 NO 就 STOP
- **Error Recovery Protocol**：第一次分析、第二次换方法、第三次停并报告，明令 Never retry

这对 Ohmybrain `wiki-ingester` agent 遇 PDF 乱码时的反复重试问题直接对症。把本应靠 hook 强制的"不要无限重试"写进 skill/agent 内部——**确定性的内化版本**。

两者关系：
- **外部 Hook**：harness 层的**阻断**式约束（不符就 exit 2）
- **内部 Checklist**：skill/agent 内部的**自律**式约束（自己检查后不调工具）
- 理想组合：关键约束用 hook（兜底），常规质量用 checklist（减少 hook 开销）

## 运行时门控扩展：ECC Hook Profile

[[affaan-m-everything-claude-code|Everything Claude Code]] 在基础 hook 架构之上加了**运行时门控**（runtime gating）层，解决"严格模式 vs 探索模式切换"的实际痛点：

```bash
export ECC_HOOK_PROFILE=minimal|standard|strict   # 默认 standard
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"
```

所有 hook 通过 `scripts/hooks/run-with-flags.js` 统一包装，**不需要编辑 hook 文件**即可临时调严格度。实现要点（对 Ohmybrain 可直接迁移）：

- **包装器模式**：`run-with-flags.js` 读环境变量 → 决定是否跳过当前 hook → 继续调用真实 hook 脚本
- **命名约定**：`<event>:<tool>:<hook-id>` 便于 `ECC_DISABLED_HOOKS` 精确门控
- **Profile 语义**：minimal = 只跑关键安全 hook；standard = 默认；strict = 开全部（含 lint / typecheck / format）

**对 Ohmybrain 的启示**：本仓未来可加 `OHMYBRAIN_HOOK_PROFILE=draft|strict`——`draft` 模式下撰写 wiki 时不跑 `lint_wiki.py`（避免频繁打断），`strict` 模式下 commit 前全量跑通。

## 来源

- Claude Code Hook 官方文档：`code.claude.com/docs/en/hooks-guide`
- 参考实现：`raw/repos/claude-code-best-practice/.claude/hooks/`（HOOKS-README、config、scripts）
- 仓主 hooks 仓库：`github.com/shanraisshan/claude-code-hooks`
- Boris tips：`raw/repos/claude-code-best-practice/tips/claude-boris-15-tips-30-mar-26.md` (#4)
- CLAUDE.md hook 事件清单：`raw/repos/claude-code-best-practice/CLAUDE.md`
- 平行架构参考：[[nousresearch-hermes-agent]]（gateway hooks）
- 运行时门控参考：[[affaan-m-everything-claude-code]]（`ECC_HOOK_PROFILE` + `ECC_DISABLED_HOOKS`）
- 相关实体：[[claude-code]]
- 相关 summary：[[claude-code-best-practice]]、[[affaan-m-everything-claude-code]]
- 内部自律范本：[[yizhiyanhua-ai-fireworks-tech-graph]]（Pre-Tool-Call Checklist + Error Recovery Protocol）
- 生命周期活例：[[thedotmack-claude-mem]]（5 hooks + Setup + Exit Code Strategy 明文契约）
