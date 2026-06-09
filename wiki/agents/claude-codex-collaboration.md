---
type: agent
created: 2026-06-09
updated: 2026-06-09
tags: [agent协作, claude-codex, worktree, 审查契约, 完成契约]
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
