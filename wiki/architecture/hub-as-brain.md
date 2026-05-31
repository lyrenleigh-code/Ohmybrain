---
type: architecture
created: 2026-05-24
updated: 2026-05-29
tags: [大脑, Hub, 元架构, single-source-of-truth]
---

# Hub 作为大脑

定义 Ohmybrain Hub 作为系统大脑应该**统御什么**，对比当前实现 vs 缺口，给出 roadmap。

> **本系列共 9 页 = 1 入口页（本页 `hub-as-brain`） + 8 个 dedicated 页**（对应下表 8 类信息）。本页是顶层入口，持续维护；8 个 dedicated 页承载各类详情。

## 大脑应该统御的 8 类信息

「Hub 是否有汇总」列附各 dedicated 页的**最后更新 / 完整度回链快照**（@2026-05-29 自检批次后）。

| # | 类别 | 为什么是"大脑"职责 | 当前承载位置 | Hub 是否有汇总（页 · 最后更新 · 完整度） |
|---|------|-------------------|------------|---------------|
| 1 | **反模式 / 经验合集** | 跨项目共享教训，避免重蹈 | `~/.claude/projects/D--Claude/memory/feedback_*` 20 条 | ✓ [[anti-patterns]] · 2026-05-29 · 实质填充 |
| 2 | **工作流术语表** | V→V→V / PMF / 单根因审计 / archive 等术语跨场景使用 | 散在 memory + 各项目 CLAUDE.md | ✓ [[workflow-glossary]] · 2026-05-29 · 实质填充 |
| 3 | **生态 dashboard** | 哪些项目活跃 / 归档 / wip，hooks 状态，wiki 规模 | system-overview 里一张表，不够动态 | ✓ [[ecosystem-dashboard]] · 2026-05-29 · 实质填充 |
| 4 | **决策记录 ADR** | 重大架构决策（三仓哲学澄清、双闭环 4 步对齐等） | 散在 log.md / memory / git history | ✓ [[decision-log]] · 2026-05-31 · 实质填充（ADR-001~020，章节形式） |
| 5 | **跨项目约定** | 命名 / 目录 / commit / PR 风格 | 散在 `~/.claude/rules/`（15 个目录）+ 各项目 CLAUDE.md | ✓ [[conventions]] · 2026-05-29 · 实质填充 |
| 6 | **Harness 全景** | Hooks (Hub 8 + 各项目 N) / Skills (本地 31 / 注入 90+) / Rules (15 目录) / Agents (55) | 散在 `~/.claude/skills/` + 各项目 .claude/ | ✓ [[harness-resources]] · 2026-05-29 · 实质填充 |
| 7 | **memory 条目索引** | 67 个 auto-memory 文件没在 Hub 中出现 | `MEMORY.md`（索引 67 行）但与 Hub wiki 脱节 | ✓ [[memory-index]] · 2026-05-29 · 实质填充 |
| 8 | **演化时间线 + roadmap** | 里程碑 + 下一步 = 大脑的"过去 + 未来" | system-overview 里程碑表，无 roadmap | ✓ [[roadmap]] · 2026-05-29 · 实质填充 |

> **本页（入口）** · 2026-05-29 · 75% → 已刷新（计数对齐 CANON + 状态/roadmap 与现状对齐）。

### CANON 权威计数（@2026-05-29，所有跨页计数以此为准）

| 资源 | 权威值 | 拆解 |
|------|--------|------|
| **auto-memory 文件** | 67 个 | user 1 / feedback 20 / project 43 / reference 3（`MEMORY.md` 索引 67 行） |
| **本地 skills** | 33 目录，其中 31 含 SKILL.md | `~/.claude/skills/` |
| **可见 skills（注入后）** | **90+** | 本地 31 叠加 `ecc:*` plugin / marketplace 注入；**必须区分"本地 31 vs 注入 90+"两层，不可裸写 90+** |
| **全局 agents** | 55 个 `.md` | `~/.claude/agents/` |
| **rules 目录** | 15 个 | common / zh / web + 12 语言（cpp/csharp/dart/golang/java/kotlin/perl/php/python/rust/swift/typescript） |
| **Ohmybrain wiki** | 106 个 `.md` | 根 index+log 2 + 104 内容页（architecture 11 / concepts 20 / entities 8 / explorations 4 / mcp-entities 25 / source-summaries 31 / topics 5 / comparisons 0） |
| **Ohmybrain scripts** | 22 个 `.py` | `scripts/` |

> **ADR 存放**：决策记录在 [[decision-log]] **内**以章节形式呈现（ADR-001~020），**非独立文件**；引用一律用 `[[decision-log]]`，不要写 `[[ADR-00x]]` 这类悬空链接。

## 大脑设计原则

### 1. Single Source of Truth (SSOT)

每个事实**只在一处定义**，其他地方引用。Hub wiki 是定义点。例子：
- "V→V→V 是什么" → [[workflow-glossary]]（唯一定义）；其他文档用 [[workflow-glossary#vvv-递进]] 引用
- "三仓哲学" → [[three-tier-architecture]]（唯一定义）
- "权威计数口径" → 本页 § CANON 权威计数（其他页引用，不各自重数）

### 2. 索引层 vs 详情层分离

参考 [[thedotmack-claude-mem]] 的三层渐进披露：
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
| 大脑功能页（本系列 9 页 = 1 入口 + 8 dedicated） | workflows/* 工作流定义文件 |

> ohmybrain-core 不写新规则，只 store Hub 决定下沉的模式。

### 5. Hub 指导每个 project 的通道（两条主通道 + 一条弱触发）

「Hub = 大脑」不仅是被动知识终点，更是**主动指导**所有运行中 project 的中枢。口径以 [[three-tier-architecture#hub-指导项目的两条通道]] 为准：**两条主通道**（全局层 + wiki query）真正服务"运行中项目"，**第三条 core template 是弱触发**，只影响新派生项目。三者对比：

| 通道 | 主/弱 | 时效 | 范围 | 例 |
|------|------|------|------|---|
| **1 全局层** `~/.claude/rules+skills+agents+memory` | 主 | **实时**（会话启动加载）| 所有 project 自动覆盖 | 改 rules/common/code-review.md → 所有项目下次会话立即生效 |
| **2 wiki query** | 主 | 按需（project 主动 pull）| 仅当前查询项目 | project 在 `knowledge.query` 时来读 Hub wiki |
| **3 core template** | 弱 | **延迟**（下次派生才生效）| 仅新派生项目 | 改 core/template/.claude/skills/ → 新派生项目继承 |

> **关键认知**：通道 1 才是 Hub "实时指导" project 的主路径。通道 3（core template）只影响**新派生**项目，对已运行项目无作用，故归为"弱触发"。

**通道 3 的同步机制**：Hub → core 不是自动的，需要 user 主动决策 + 手动同步（或用 `/sync-to-core` 命令辅助）。详见 [[core-update-mechanism]]。当前 pending 候选见 [[core-update-queue]]。

## 8 类 gap 的优先级

按"信息散得最严重 + 复用频率最高"排序：

| 优先级 | 类别 | 现状散度 | 复用频率 | 备注 |
|--------|------|---------|---------|------|
| **P0** | [[workflow-glossary]] | 散在 memory + 各 CLAUDE.md | 极高 | 几乎每次会话都用到 V→V→V / archive / promote 等术语 |
| **P0** | [[anti-patterns]] | 散在 20 条 feedback_* memory | 极高 | 防止重蹈过往坑 |
| **P0** | [[harness-resources]] | 散在 ~/.claude + 项目 .claude | 高 | 不知道有什么 skill / hook 可用 |
| **P1** | [[memory-index]] | 散在 MEMORY.md（不在 Hub wiki） | 高 | 让 Hub 与 memory 形成双索引 |
| **P1** | [[decision-log]] | 散在 log.md + memory + git | 中 | 复盘和 onboarding 用 |
| **P1** | [[conventions]] | 散在 rules + CLAUDE.md | 中 | 新项目派生时核对 |
| **P2** | [[ecosystem-dashboard]] | 散在多处 | 中低 | 偶尔需要"全景" |
| **P2** | [[roadmap]] | 散在 user 头脑中 | 中低 | 季度复盘用 |

## 当前状态（2026-05-29）

8 个 dedicated 页已于 **2026-05-29 自检批次全部实质填充完成**（不再是 2026-05-24 的"骨架待填"）：P0 三页（[[workflow-glossary]] / [[anti-patterns]] / [[harness-resources]]）、P1 三页（[[memory-index]] / [[decision-log]] / [[conventions]]）、P2 两页（[[ecosystem-dashboard]] / [[roadmap]]）均已含完整章节 + 与 CANON 对齐的计数。本页 `hub-as-brain` 作为顶层入口同批刷新（计数对齐 CANON、状态/roadmap 与现状对齐）。

至此「大脑应该统御的 8 类信息」全部从"✗ 散"转为"✓ 有汇总"，本系列 9 页（1 入口 + 8 dedicated）形成闭环。

### 下一步 roadmap（从"建页"转向"自动化 + 维护"）

dedicated 页已全部建成，重心转为**保持新鲜 + 降低维护成本**：

- **dashboard 自动化**：写 `scripts/dashboard_snapshot.py`，自动扫 `~/.claude/`（memory / skills / agents / rules 计数）+ wiki 规模，刷新 [[ecosystem-dashboard]] 与本页 CANON 表，避免手数过时。
- **promote queue 自动扫描**：扩展脚本扫各项目 memory / wiki 的"待回流"标记，自动汇入 [[core-update-queue]]，减少漏 promote。
- **季度复盘**：每季度核对 8 个 dedicated 页计数 / 状态 vs 现状，更新 [[roadmap]] 里程碑；CANON 权威计数随之刷新。
- **断链巡检**：定期 `python scripts/lint_wiki.py`，确保 9 页互链与 [[decision-log]] / [[core-update-queue]] 等回链不悬空。

## 相关页面

- [[three-tier-architecture]] — 三仓哲学 + 通道口径（Hub 大脑定位的基础）
- [[dual-loop]] — 双工作流闭环（大脑统御的核心工作流）
- [[system-overview]] — 系统总览
- [[memory-stack]] — 5 层 memory 栈
- [[core-update-mechanism]] — 通道 3 同步机制
- [[core-update-queue]] — 通道 3 pending 候选
