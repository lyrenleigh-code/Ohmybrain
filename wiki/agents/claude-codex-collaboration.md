---
type: agent
created: 2026-06-09
updated: 2026-06-09
tags: [agent协作, claude-codex, worktree, 并发写, commit边界, 审查契约, 完成契约]
---

# Claude + Codex 协作协议

> 最后更新：2026-06-09

本文定义 Claude Code 和 Codex 在 `D:\Claude` 中如何协作。

## 运行原则

Claude Code 和 Codex 应共享文件，而不是依赖临时上下文。二者之间的稳定接口是：

```text
specs/active/   -> 要做什么
plans/active/   -> 怎么做
handoff/active/ -> 谁从什么状态继续
wiki/           -> 长期知识
```

## 默认角色

| Agent | 最适合承担 |
|---|---|
| Claude Code | 需求澄清、架构设计、研究综合、长文档、初版 spec/plan |
| Codex | 实现、重构、测试、本地验证、代码审查 |

小任务中任一 agent 都可以承担另一方的工作；大任务应保持分工显式。

## 协作模式

### 串行交接

适合任务边界清晰时使用。

```text
Claude Code -> spec/plan
Codex -> 实现/测试
Claude Code 或 Codex -> 审查
```

### 并行探索

适合路线不确定时使用。

```text
worktrees/<project>-claude/
worktrees/<project>-codex/
```

双方独立探索，最后由用户选择要合并的路线。

### 实现 + 红队审查

适合高风险任务。

```text
Agent A 负责实现。
Agent B 审查正确性、缺失测试、隐藏假设和路径风险。
```

## Worktree 规则

- 并行工作必须使用不同 worktree，或使用明确隔离的文件边界。
- 除非任务明确要求，不修改另一个 agent 的 worktree。
- 合并竞争版本时必须说明采用哪一版，不做无来源的复制粘贴。
- 交接单必须记录下一步以哪个 worktree 为权威来源。

## 同仓并发写（无法 worktree 隔离时）

Worktree 规则解决「不同分支隔离探索」。但有些仓**无法 worktree 隔离**——典型是 **Ohmybrain Hub**（单一共享知识仓，两个 agent 都要往里写、且都碰 `index.md` / `log.md` / `conventions.md` 这类基础设施文件），以及任何被指定为单一事实源的项目主仓。这类仓的并发写须遵守：

- **串行写优先**：同一时间只有一个 agent 主动批量写该仓。动手前先 `git status` 看是否有他方在飞改动；有则先协调，不并行硬写。
- **共享基础设施文件**：
  - `wiki/log.md` **append-only**——各 agent 在顶部追加自己的条目，不改写他人条目（天然可并存）。
  - `wiki/index.md` 的计数 / 描述是**共享冲突区**——谁改了计数，谁负责最后跑 `lint_wiki.py` / `dashboard_snapshot.py` 核对全站一致；后写者先读最新再改，不覆盖他人描述行。
- **写前重读**：编辑共享文件（`index.md` / `log.md` / `conventions.md` 等）前重读当前内容，防「modified since read」覆盖。

## commit 边界

> 来源教训（2026-06-09）：一次 promote 与一次并行「文档结构口径同步」在同一工作树混到 18→28 文件，`git add -u` 一把抓到对方仍在写的半成品；且 `index.md` / `log.md` 共享，无法只挑单方的行提交。

- **commit 前必 `git status`**：确认暂存范围只含本任务改动。工作树若含他方未提交 / 仍在增长的改动，**停下与用户确认 commit 范围**，不盲 `git add -A` / `-u` 把他方半成品一并提交。
- **不在移动目标上 commit**：若文件数仍在变化（他方 pass 仍在写），等其稳定再提交。
- **共享仓 commit / push 须用户明确授权**（重申 [[../architecture/conventions]] §5 破坏性操作）；push 远程逐次授权，私有项目禁 push 公开远程（§9 红线）。
- 合并 / 连带提交他方改动前，在 commit message 或交接单注明哪些改动属哪一方。

## 审查契约

有用的审查从问题开始，而不是从表扬开始。

每条问题应包含：

- 文件路径
- 具体风险
- 建议修复或验证方式
- 必要时标注严重级别

如果没有发现问题，也要说明仍然存在的测试缺口。

## 完成契约

agent 声称任务完成前，应检查：

- 相关 spec 的验收标准
- 相关 plan 的检查项
- 本地测试或验证命令
- 如果修改了 wiki，确认 `wiki/index.md` 和 `wiki/log.md` 已同步
- 如果不再需要另一方继续，归档 handoff

## 相关页面

- [[../architecture/document-protocol]] — 本协作所依赖的文档结构协议
- [[../workflows/agent-handoff]] — 串行交接 / 并行探索时的交接单流程
- [[../architecture/conventions]] — 跨项目约定（§10 worktree 归属映射）
- [[../architecture/dual-loop]] — 双工作流闭环（串行交接 = engineering 闭环的 agent 分工版）
