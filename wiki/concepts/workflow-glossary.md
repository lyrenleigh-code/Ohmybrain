---
type: concept
created: 2026-05-24
updated: 2026-05-24
tags: [术语, glossary, 工作流]
---

# 工作流术语表

跨项目工作流相关术语的中文 / 英文 / 缩写定义。这里是 single source of truth，其他文档引用。

## 核心动词（来自 [[../architecture/dual-loop]]）

| 英文 | 中文 | 含义 | 闭环位置 |
|------|------|------|---------|
| `ingest` | 摄入 | 把 raw/ 资料转化为 wiki/source-summaries/ 条目 | knowledge 闭环 step 01 |
| `query` | 查询 | 用户领域问题，主会话查 Hub wiki + memory | knowledge 闭环 step 02 |
| `promote` | 回流 / 上汇 | 跨项目可复用结论从 project → Hub | knowledge 闭环 step 03 |
| `review` | 复盘 | 定期审 wiki/log.md，整理 / 触发新 ingest | knowledge 闭环 step 04 |
| `spec` | 任务规约 | 单职责任务定义，目标 / 范围 / verification | engineering 闭环 step 01 |
| `plan` | 计划 | 复杂任务的分阶段实现计划 | engineering 闭环 step 02 |
| `implement` | 实施 | 写代码 + commit | engineering 闭环 step 03 |
| `validate` | 验证 | 业务指标验证 + 用户终审 | engineering 闭环 step 04 |
| `archive` | 归档 | 完成的 spec 从 `specs/active/` → `specs/archive/` | engineering.validate 之后的整理动作 |

## 算法研究核心术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **V→V→V 递进** | 逐版闭环迭代（每个 V = 一次完整 RCA + fix + verify），不跳号、不并行 | UWAcomm 工作流 |
| **PMF 双指标** | "过版"判定双标准：① 上一 V RCA 完成 ② 5 项回归 test 全通过 | Anthropic Founder's Playbook 创业 PMF 类比 |
| **单根因审计** (Single Root Cause Audit) | D9/D10 toggle 开关 + 跨 runner audit 把症状定位到单一根因，拒绝多根因混淆 | `feedback_single_root_cause_audit`，限 MATLAB 算法 RCA 不外推 |
| **plan C 时变证伪** | RCA 反例：把"信道时变性"作为假根因绕过单一函数 fix 的 anti-pattern | 同上 memory 条目 |
| **RCA** | Root Cause Analysis 根因分析。**不是 engineering 闭环的 4 步之一**，而是 `validate` 失败时进入的**子环节**：找单一根因 → fix → 重新 validate。配合 V→V→V，每个 V = 一次完整 RCA + fix + verify。 | 算法工作流通用 |
| **过版 / passing version** | 通过 PMF 双指标，进入下一 V 的判定 | 与 V→V→V 配套 |

## Claude Code 协作术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **三表面** (Three Surfaces) | Chat（频次最高补充）/ Cowork（中频协作）/ Code（核心实现） | Anthropic Founder's Playbook |
| **agentic 技术债** | 多 worktree 漂移、不周期性集成产生的合并债 | V4 PPT S36 worktree 三路 |
| **代下结论 反模式** | Claude 自主下"work / 完成 / 闭环"判断，本应用户做 | `feedback_uwacomm_testing_boundary` |
| **三层渐进披露** | 查 wiki 时按 `index → log → 详` 三层逐步打开，每次 Read ≤3 页 | claude-mem 启发 |
| **5 层 memory 栈** | Global CLAUDE.md / Project CLAUDE.md / auto-memory / MCP graph / Hub wiki | [[../architecture/memory-stack]] |

## 仓 / 项目层级术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **Hub / 大脑** | Ohmybrain 本仓，知识中枢 | [[../architecture/three-tier-architecture]] |
| **核心 / core** | ohmybrain-core 母仓，被动模板 | 同上 |
| **项目仓 / project-*** | UWAcomm / USBL / DocProcess/* 等业务驱动方 | 同上 |
| **worktree 三路隔离** | main（用户主导）/ exp（Claude 自主）/ dev（Codex 并行）三路 worktree | V4 PPT S36 |
| **派生 / derive** | `cp -r ohmybrain-core/template/` 新建项目 | new-project-sop.md |

## 反模式 / 行为约束术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **confirmation bias** | 问 Claude 找支持已有信念的证据，Claude 顺着走 | [[anti-patterns]] |
| **scope creep** | 实施时偷偷加 spec 未定义需求 | 同上 |
| **disconfirming evidence** | 反向证据，挑战已有信念的事实 | 同上 |

## hooks / 自动化术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **PreToolUse hook** | 工具调用前拦截（如 `check_raw_write.py`） | Claude Code |
| **PostToolUse hook** | 工具调用后触发（如 `post_wiki_write.py`） | 同上 |
| **Stop hook** | 会话结束时检查（如 `check_index_log_sync.py`） | 同上 |
| **SessionStart hook** | 会话开始注入上下文 | 同上 |

## 文档 / wiki 术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **single source of truth (SSOT)** | 一个事实只在一处定义，其他地方引用 | [[../architecture/hub-as-brain]] |
| **wikilink** | `[[slug]]` 跨页引用语法（Obsidian 兼容） | wiki 规则 |
| **frontmatter** | YAML metadata 头部（type / created / updated / tags） | 同上 |

## 相关页面

- [[../architecture/dual-loop]] — 双闭环动词的来源
- [[anti-patterns]] — 反模式合集（含 anti-pattern 术语）
- [[../architecture/hub-as-brain]] — 大脑功能定位
- [[../architecture/memory-stack]] — 5 层 memory 栈详细
