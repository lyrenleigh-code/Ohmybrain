---
type: source-summary
created: 2026-05-22
updated: 2026-05-22
tags: [anthropic, claude-code, claude-cowork, ai-native-startup, agentic-engineering, methodology]
source_type: article
concept: [[claude-code]]
---

# The Founder's Playbook v3 (Anthropic, 2026) — Building an AI-Native Startup

- **来源**：Anthropic 官方 marketing playbook（claude.ai/resources）
- **日期**：2026
- **类型**：article（电子书 / 手册）
- **原始文件**：[`raw/articles/The-Founders-Playbook_v3.pdf`](../../raw/articles/The-Founders-Playbook_v3.pdf)（36 页 / 476 KB / 7 章）
- **slug**：anthropic-2026-founders-playbook

## TL;DR

Anthropic 发布的"AI-Native 创业方法论"：把传统四阶段（Idea / MVP / Launch / Scale）按"founder = agent 编排者"假设重映射。核心论点是 Claude 三表面（Chat / Cowork / Code）覆盖 founder 全栈工作。**对水声研究者不是直接 actionable，但其中"agentic technical debt + CLAUDE.md 持久架构上下文 + scope doc + devil's advocate"4 条工程方法论可迁移到任何 agent-driven 工程项目**。

## 章节结构

| 章 | 主题 | 阶段 |
|---|---|---|
| 1 | The startup lifecycle, rebooted for 2026 | 全局 |
| 2 | What it means to be a founder is changing | 角色 |
| 3 | Idea Stage | 验证 |
| 4 | MVP Stage | 构建 |
| 5 | Launch Stage | 增长 |
| 6 | Scale Stage | 系统化 |
| 7 | Same job, new rules | 收尾 |

## 核心观点

1. **Founder = orchestrator of agents**（Ch.2）：注意力从 IC（individual contributor）上移到"想法 + 方向 + 编排"。AI 让"懂代码会 build"和"懂业务有想法"之间的墙坍塌。
2. **三表面分工模型**（Ch.2）：Chat 快问快答 / Cowork 多源知识工作 + 文件夹 + connectors / Code agentic 编程。同一 Claude，三种 workspace。
3. **Idea 阶段的 confirmation bias 升级风险**（Ch.3）：agentic coding 让"有想法 → 立刻 build prototype → 把 prototype 存在当 validation"变得致命容易。antidote 是把同样的 AI 反向用作 devil's advocate。
4. **MVP 阶段 CLAUDE.md 是必备架构记忆**（Ch.4）：无 CLAUDE.md → 每次 session 重新推断架构决策 → AI 生成的代码漂移 → "agentic technical debt 复利"。这是 [[memory-stack]] L2 层的强 validation。
5. **Scope creep 零摩擦 → 写下"deliberately does not do"**（Ch.4）：build cost 跌到接近零，scope creep 失去自然抑制。antidote 是 pre-build scope doc + feature amendment criteria（什么证据足够触发追加）。
6. **MVP security 不可推迟**（Ch.4）：agentic 生成的代码 functional 不 secure；pre-launch security review 是 minimum responsible threshold。Claude Code Security beta 可做首过。
7. **Sean Ellis 40% + effort test 双 PMF 指标**（Ch.4）：前者问"如果不能用了你失望吗"≥40%；后者看"retention 是 founder 推还是 product 拉"。
8. **Scale moat = 累积深度 × 数据飞轮 × 工作流 lock-in**（Ch.6）：CLAUDE.md 把 founder domain expertise 编码进产品；用户行为数据时间锁定；用户在产品上 build 的自动化 = 切换成本。三者复利。
9. **AI compresses quarters into weeks，bottleneck 从"能 build 什么"转为"选择 build 什么"**（Ch.7）。

## 可迁移结论（5 条工程方法论）

1. **CLAUDE.md as architectural memory**：每个 agentic 项目必须有 CLAUDE.md，写下架构决策 + 边界 + tradeoff，每次 session 开始时 reload，结束时追加 decisions log。这与 [[memory-stack]] L2 层一致，文章给出 founder 视角强 validation。
2. **Devil's advocate as default AI mode**：默认让 AI 反向论证你的假设；ask Claude to make the strongest case against your idea。与 wiki-ingester 的"审视性 ingest"可形成对称机制。
3. **Pre-build scope doc + "deliberately does not do"**：项目启动时写下"不做什么"清单 + 新功能 amendment criteria（什么证据足够触发追加）。
4. **Three Claude surfaces 分工模型**：Chat 用于跨工具快问答；Cowork 用于多源知识工作；Code 用于 codebase 内 agentic 工作。Ohmybrain 用户目前用 Code + Chat，Cowork 未用——可选评估。
5. **Sean Ellis 40% PMF test**：把"如果不能用了你失望吗"作为算法 / 工具产品的 evaluation rubric 一条；与 effort test（系统是被推还是被拉）对照。

## 与 Ohmybrain 已有页面的连接

- [[memory-stack]] L2 层（项目级 CLAUDE.md）：文章独立 validation。
- [[claude-code]] entity：Anthropic 自己对其 product surface 的官方编排。
- [[subagents-orchestration]]：founder = orchestrator 是 subagent-orchestration 的人格化映射。
- [[harness-engineering]]：scope doc + architectural memory 是 harness 工程的具体落地形态。

## 反模式与告警

文章在 MVP 章列出 4 大失败模式，**对水声研究者也适用**（按 [[feedback_uwacomm_testing_boundary]] 的"不代下结论"原则反向印证）：

| 反模式 | 表现 | 对应用户 memory |
|---|---|---|
| Mistaking building for validating | 把 prototype 存在当 PMF 证据 | feedback_uwacomm_testing_boundary 的"不代下结论"完全同向 |
| Premature scaling | 在 PMF 之前优化扩展 | UWAcomm 用 V→V→V 递进版本是反例（先 V5.4 fix RCA 才动 V5.5） |
| Zero-friction scope creep | agentic 让加 feature 接近零成本 | UWAcomm 的 plan C 时变证伪反例（探索过早分支） |
| Insecure by inexperience | 不做 security review 就 ship | 不直接对应（用户算法仿真无外部用户） |

## 不适用部分

文章面向商业 startup（CAC / LTV / IPO / GTM / SOC 2 / GDPR / 客户对接 / Sean Ellis test）。这些**对 UWA 算法仿真和水声项目仿真不直接适用**——用户场景是"研究 + 算法演化"，没有客户 / 营收。但工程方法论部分（CLAUDE.md / scope doc / devil's advocate / agentic technical debt）**全适用**。

## 引用摘录

> The bottlenecks are no longer what you can build, but what you choose to build.（Ch.7 收尾）

> The intelligence in the system is yours. The prime directive at this stage is keeping your sense-making ahead of your building.（Ch.3 Premature scaling）

> Without specs and architectural constraints written down somewhere the AI can read, each session re-derives foundational decisions from scratch, and those decisions drift.（Ch.4 Agentic technical debt —— 这是 [[memory-stack]] 的 founder 视角表述）

## 元信息

- 出版方：Anthropic（claude.ai/resources）
- 出版日期：2026（v3）
- 长度：36 页
- 提及产品：Claude (Chat)、Claude Cowork、Claude Code、Agent SDK、Claude Code Security (beta)、MCP
- 案例参引：HumanLayer (YC F24)、Ambral (W25)、Vulcan Technologies (S25)、GC AI、Carta Healthcare、Anything、Cogent、Airtree、Duvo、Zingage、Kindora、Wordsmith
