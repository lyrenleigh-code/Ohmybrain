---
type: workflow
created: 2026-06-09
updated: 2026-06-10
tags: [交接流程, handoff, agent协作, 工作流, 归档标准]
---

# Agent 交接流程

> 最后更新：2026-06-09

当 Claude Code 和 Codex 需要共同承担一个任务时，使用本流程。

## 何时创建交接单

出现以下情况时，在 `handoff/active/` 创建交接单：

- 一个 agent 开始的工作可能由另一个 agent 继续；
- 一个任务跨多个会话；
- Claude Code 和 Codex 正在不同 worktree 中探索；
- 用户要求“实现 + 独立审查”；
- 任务存在路径、隐私或验证风险。

## 文件命名

```text
handoff/active/YYYY-MM-DD-task-slug.md
```

任务完成后移动到：

```text
handoff/archive/YYYY-MM-DD-task-slug.md
```

## 模板

```markdown
# 交接单：任务标题

## 目标
一句话说明期望结果。

## 背景
- 相关 spec：
- 相关 plan：
- 相关 wiki：

## 当前状态
- 已完成：
- 未完成：
- 阻塞点：

## Agent 分工
- Claude Code:
- Codex:

## 修改边界
允许修改：
禁止修改：

## 关键文件
- `path/to/file`

## 验证方式
- `python scripts/validate_task.py`
- `python scripts/lint_wiki.py`
- 项目特定测试：

## 下一步
- [ ] ...
```

## 交接规则

- 交接单应足够短，能在一分钟内读完。
- 使用精确路径。
- 不把私人原始材料写入公开 Hub 页面。
- 如果任务涉及 `wiki/`，记录 `index.md` 和 `log.md` 是否已更新。
- 如果任务改变了生成物，记录这些生成物是否为有意产出。

## 归档标准

满足以下条件时，将交接单移动到 `handoff/archive/`：

- 面向用户的交付物已经完成；
- 验证状态已经记录；
- 不再存在跨 agent 依赖；
- 任何长期有效的经验已经沉淀到 `wiki/`。

## 知识闭环交接（Hub 特例）

Hub 本身无 `handoff/` 目录（非业务项目，见 [[../architecture/document-protocol]] §三层结构注）。**promote / sync-to-core / ingest 半途中断**时的交接走：

- **Hub `TODO.md`** 留状态行（处理到哪个候选 / 哪一步、阻在什么）；
- **`wiki/log.md`** 下次会话收口时记 entry 闭环；
- core-update-queue / promote 候选本身就是持久状态，**不靠会话上下文**——中断后任何会话可从 queue 页 + TODO 恢复。

## 相关页面

- [[../agents/claude-codex-collaboration]] — 何时进入交接的协作模式判断
- [[../architecture/document-protocol]] — 状态归属（`handoff/active/` 目录规则）
- [[../architecture/dual-loop]] — 双工作流闭环（交接单承载跨会话续作）
