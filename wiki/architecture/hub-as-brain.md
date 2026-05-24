---
type: architecture
created: 2026-05-24
updated: 2026-05-24
tags: [大脑, Hub, 元架构, single-source-of-truth]
---

# Hub 作为大脑

定义 Ohmybrain Hub 作为系统大脑应该**统御什么**，对比当前实现 vs 缺口，给出 roadmap。

## 大脑应该统御的 8 类信息

| # | 类别 | 为什么是"大脑"职责 | 当前承载位置 | Hub 是否有汇总 |
|---|------|-------------------|------------|---------------|
| 1 | **反模式 / 经验合集** | 跨项目共享教训，避免重蹈 | `~/.claude/projects/D--Claude/memory/feedback_*` 60+ 条 | ✗ 散 → ✓ [[anti-patterns]] |
| 2 | **工作流术语表** | V→V→V / PMF / 单根因审计 / archive 等术语跨场景使用 | 散在 memory + 各项目 CLAUDE.md | ✗ 散 → ✓ [[workflow-glossary]] |
| 3 | **生态 dashboard** | 哪些项目活跃 / 归档 / wip，hooks 状态，wiki 规模 | system-overview 里一张表，不够动态 | ✗ 散 → ✓ [[ecosystem-dashboard]] |
| 4 | **决策记录 ADR** | 重大架构决策（三仓哲学澄清、双闭环 4 步对齐等） | 散在 log.md / memory / git history | ✗ 散 → ✓ [[decision-log]] |
| 5 | **跨项目约定** | 命名 / 目录 / commit / PR 风格 | 散在 `~/.claude/rules/` + 各项目 CLAUDE.md | ✗ 散 → ✓ [[conventions]] |
| 6 | **Harness 全景** | Hooks (Hub 8 + 各项目 N) / Skills (90+) / Rules / Agents | 散在 `~/.claude/skills/` + 各项目 .claude/ | ✗ 散 → ✓ [[harness-resources]] |
| 7 | **memory 条目索引** | 60+ 条 auto-memory 没在 Hub 中出现 | `MEMORY.md` 索引但与 Hub wiki 脱节 | ✗ 散 → ✓ [[memory-index]] |
| 8 | **演化时间线 + roadmap** | 里程碑 + 下一步 = 大脑的"过去 + 未来" | system-overview 里程碑表，无 roadmap | ✗ 散 → ✓ [[roadmap]] |

## 大脑设计原则

### 1. Single Source of Truth (SSOT)

每个事实**只在一处定义**，其他地方引用。Hub wiki 是定义点。例子：
- "V→V→V 是什么" → [[workflow-glossary]]（唯一定义）；其他文档用 [[workflow-glossary#vvv-递进]] 引用
- "三仓哲学" → [[three-tier-architecture]]（唯一定义）

### 2. 索引层 vs 详情层分离

参考 [[claude-mem 三层渐进披露]]：
- **索引层** `index.md` — 一行描述 + slug
- **时序层** `log.md` — 时间脉络 + 变更原因
- **详情层** subpage — 完整规约

每个 dedicated 页都遵守这套结构。

### 3. 反馈式更新（不是单次写完）

大脑的内容不是写一次就完。机制：
- **触发**：项目实践中暴露 gap（如本次 PPT 编制暴露双闭环不清）
- **沉淀**：写新页或更新已有页
- **下沉**：模式成熟后下沉到 `ohmybrain-core/template/` 让新项目继承

### 4. 与 ohmybrain-core 的边界

| Hub 承担 | core 承担 |
|---------|----------|
| 决策 / 知识沉淀 / 演化方向 | 模板存储 / 可复制起点 |
| 跨项目反模式 / 术语 / 约定 | 项目骨架文件 |
| 大脑功能页（本系列 9 页） | workflows/* 工作流定义文件 |

> ohmybrain-core 不写新规则，只 store Hub 决定下沉的模式。

### 5. Hub 指导每个 project 的三条通道

「Hub = 大脑」不仅是被动知识终点，更是**主动指导**所有运行中 project 的中枢。详见 [[three-tier-architecture#hub-指导项目的两条通道]]。三通道对比：

| 通道 | 时效 | 范围 | 例 |
|------|------|------|---|
| **1 全局层** `~/.claude/rules+skills+agents+memory` | **实时**（会话启动加载）| 所有 project 自动覆盖 | 改 rules/common/code-review.md → 所有项目下次会话立即生效 |
| **2 wiki query** | 按需（project 主动 pull）| 仅当前查询项目 | project 在 `knowledge.query` 时来读 Hub wiki |
| **3 core template** | **延迟**（下次派生才生效）| 仅新派生项目 | 改 core/template/.claude/skills/ → 新派生项目继承 |

> **关键认知**：通道 1 才是 Hub "实时指导" project 的主路径。通道 3 只影响**新派生**项目，对已运行项目无作用。

**通道 3 的同步机制**：Hub → core 不是自动的，需要 user 主动决策 + 手动同步（或用 `/sync-to-core` 命令辅助）。详见 [[core-update-mechanism]]。当前 pending 候选见 [[../topics/core-update-queue]]。

## 8 类 gap 的优先级

按"信息散得最严重 + 复用频率最高"排序：

| 优先级 | 类别 | 现状散度 | 复用频率 | 备注 |
|--------|------|---------|---------|------|
| **P0** | [[workflow-glossary]] | 散在 memory + 各 CLAUDE.md | 极高 | 几乎每次会话都用到 V→V→V / archive / promote 等术语 |
| **P0** | [[anti-patterns]] | 散在 60+ memory 条 | 极高 | 防止重蹈过往坑 |
| **P0** | [[harness-resources]] | 散在 ~/.claude + 项目 .claude | 高 | 不知道有什么 skill / hook 可用 |
| **P1** | [[memory-index]] | 散在 MEMORY.md（不在 Hub wiki） | 高 | 让 Hub 与 memory 形成双索引 |
| **P1** | [[decision-log]] | 散在 log.md + memory + git | 中 | 复盘和 onboarding 用 |
| **P1** | [[conventions]] | 散在 rules + CLAUDE.md | 中 | 新项目派生时核对 |
| **P2** | [[ecosystem-dashboard]] | 散在多处 | 中低 | 偶尔需要"全景" |
| **P2** | [[roadmap]] | 散在 user 头脑中 | 中低 | 季度复盘用 |

## 当前状态（2026-05-24）

8 个 dedicated 页已经全部建立**骨架**（含 frontmatter + 主章节 + 第一批种子内容），后续逐步填充。本页 `hub-as-brain.md` 作为顶层入口持续维护。

### Gap 填充 roadmap

- **2026-05-24** 9 个文件骨架就位（本批），含 [[three-tier-architecture]] + [[dual-loop]] 已详细完成
- **下一批** P0 三页详细化：[[workflow-glossary]] / [[anti-patterns]] / [[harness-resources]]
- **再下一批** P1 三页：[[memory-index]] / [[decision-log]] / [[conventions]]
- **最后一批** P2 两页：[[ecosystem-dashboard]] / [[roadmap]]

## 相关页面

- [[three-tier-architecture]] — 三仓哲学（Hub 大脑定位的基础）
- [[dual-loop]] — 双工作流闭环（大脑统御的核心工作流）
- [[system-overview]] — 系统总览
- [[memory-stack]] — 5 层 memory 栈
