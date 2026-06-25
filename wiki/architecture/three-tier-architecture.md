---
type: architecture
created: 2026-05-24
updated: 2026-06-09
tags: [架构, 三仓, 哲学, Hub, 大脑]
---

# 三仓架构

## 哲学

三仓不是 "模板派生项目派生 Hub" 的线性下游，而是 **以 Hub 为大脑 + 项目为需求牵引 + core 为被动模板** 的中枢辐射结构。

| 角色 | 仓库 | 定位 | 主动性 |
|------|------|------|--------|
| **大脑 / 中枢** | `Ohmybrain` (本仓) | 知识沉淀、决策、模板演化的中枢 | **主动** — 接收反馈 + 主动更新 core |
| **需求牵引 / 业务驱动** | `project-*`（UWAcomm / USBL / DocProcess / ...） | 实际业务在此发生，是整个生态的演进驱动力 | **主动** — 业务需求催生新工作流 / 新结论 |
| **被动模板（3 类）** | `ohmybrain-core` | 项目模板存储（**engineering / document / tool**），提供新项目派生起点 | **被动** — 等待 Hub 更新对应 template-*/ |

**关键澄清**：core 不是"源头"。Hub 才是。core 只是 Hub 把成熟模式打包供新项目复用的副本。

### core 三模板（2026-05-24 拆分）

```
ohmybrain-core/
├── template-engineering/   ──派生──► TechReq/    (UWAcomm / USBL / UWAnet / ...)
├── template-document/      ──派生──► DocProcess/ 🔒 (UWAprojDoc / Pricing / ...)
└── template-tool/          ──派生──► Tools/      (FlowGen / IconForge / AnthropicPPT)
```

详见 [[project-types]]。Hub 主动更新这 3 个 template-*/ 中任一个（详见本页 § Hub 指导项目的两条通道 § 通道 3）。

## 数据流向

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│                    Ohmybrain (大脑 · 中枢)                     │
│                                                                │
│      ┌──── wiki/ ──── concepts / architecture ──── promote ┐  │
│      │                                                      │  │
│      │                  ↑ /promote-answer                   │  │
│      │           (跨项目可复用知识沉淀)                       │  │
│      │                                                      │  │
└──────┼──────────────────────────────────────────────────────┼──┘
       │                                                      │
       │ 更新 template-*/                                      │
       │ (模式成熟后按类型下沉)                                │
       ↓                                                      │
┌──────────────────────┐                                      │
│  ohmybrain-core      │                                      │
│  template-* 副本存储  │                                      │
└──────────┬───────────┘                                      │
           │                                                  │
           │ cp -r template-*/                                │
           │ (新项目派生)                                      │
           ↓                                                  │
┌────────────────────────────────────────────────┐            │
│                                                │            │
│  project-*  (UWAcomm / USBL / DocProcess / ...) │            │
│  需求牵引 · 业务驱动                            │            │
│                                                │            │
│  · 项目内独立闭环（knowledge + engineering）      │ ─────────-─┘
│  · 跨项目可复用结论 → /promote 回流到 Hub        │
│  · 新工作流模式 → Hub 整理后下沉到 core           │
│                                                │
└────────────────────────────────────────────────┘
```

### 单向流动的边界

1. **Hub 不向上回流到 core**：Hub 是终点，但它**主动决策**哪些下沉到 core
2. **project 不直接更新 core**：项目的新工作流先回流 Hub，由 Hub 评估后才更新对应 core `template-*`
3. **core 不主动派生项目**：派生是 user 在新项目时主动按类型复制 `ohmybrain-core/template-*`

## Hub 指导项目的两条通道

「Hub = 大脑」不只是被动的知识终点，还要**主动指导每个运行中的 project**。这不是通过更新 core 模板（那只影响**新派生**的项目），而是通过两条独立通道：

### 通道 1：全局层 `~/.claude/`（主动 · 实时 · 影响所有 project）

```
~/.claude/
├── rules/common/*       → 每个会话启动时自动加载（在 system prompt 中）
├── rules/zh/*           → 同上（中文版本）
├── skills/*             → 关键词 / 路径触发，所有项目共享
├── agents/*             → 主会话可委托（如 wiki-ingester）
├── projects/.../memory/ → auto-memory 跨会话恒久（86 条）
└── settings.json        → 全局 hooks / 配置
```

**特点**：
- Hub 大脑维护这一层（user 在 Hub 会话中决策 + 写入）
- 每个 project 启动 Claude Code 时自动加载，**无需 project 显式引用**
- 是 Hub "实时指导" project 的真正路径
- 不需要 project 派生时重新复制 `template-*`，已运行的项目立即生效

### 通道 2：Hub wiki query（被动 · 按需 · 项目主动来查）

```
project 工作时 → knowledge.query → 主会话读 Hub wiki/ → 决策
```

**特点**：
- 项目主动发起（每次需要时查）
- 不实时下发，按需 pull
- 走 `knowledge.query` 闭环步骤（详见 [[dual-loop]] § 02 query）

### 通道 3（弱触发）：core template 更新

```
Hub 决定 → 更新 ohmybrain-core/template-*/ → 影响"下次派生的新项目"
```

**特点**：
- **只影响新派生的项目**，对已运行的项目无作用
- 弱触发，定期下沉成熟模式
- 通道 1 (rules/skills) 才是真正的"实时下发"

### 三条通道对比

| 通道 | 时效 | 范围 | 触发 |
|------|------|------|------|
| **1 全局层** | 实时（启动时加载）| 所有 project 自动覆盖 | Hub 主动维护 |
| **2 wiki query** | 按需（project 查询）| 仅查询时的项目 | project 主动 pull |
| **3 core template** | 延迟（下次派生）| 仅新派生项目 | Hub 主动下沉 + user 派生 |

> **回答常见困惑**：当 user 改了某个 best practice，怎么让所有项目立即遵守？写到 `~/.claude/rules/common/<topic>.md` —— 通道 1 立即生效。写到 `ohmybrain-core/template-*/` 只影响**新项目**。

## 三仓的"被动 / 主动"对照

| 动作 | 主动方 | 被动方 |
|------|--------|--------|
| 启动新项目 | user（业务需求） | core 提供 template-* |
| 项目内闭环 | project（业务驱动） | — |
| 跨项目结论沉淀 | project + Hub 协同（`/promote-answer`） | Hub wiki/ |
| 模板演化 | Hub（大脑决策） | core template-*（被更新） |
| 模式下沉 | Hub | core |
| 知识检索 | user（query） | Hub wiki/ |

## 与传统"中心化"对比

传统 mono-repo / monolith 是 **中心控制一切**。三仓的"大脑"哲学不同：

- **Hub 是中枢，不是中心**：它不持有业务代码（无 `src/` 无 `specs/`），只持有知识与决策权
- **项目是 leaf node，但又是业务驱动的源头**：每个项目自包含、可独立 clone、独立开发，业务需求从这里冒出
- **core 是 read-mostly 的副本**：它的存在是为了快速复制，不是为了主动控制

## 为什么这样设计

| 反模式 | 三仓应对 |
|--------|---------|
| 单仓臃肿（业务 + 知识 + 模板混在一起） | **拆**：业务在 project，知识在 Hub，模板在 core |
| 多项目漂移（各项目独立演化无沉淀） | **回流**：project → Hub（promote） |
| 模板锁定（template 老化项目跟着烂） | **下沉**：Hub 主动更新 core template-*，新项目得到最新模式 |
| 知识无中枢（找不到跨项目结论） | **大脑**：Hub wiki/ 作为唯一跨项目知识入口 |

## 相关页面

- [[system-overview]] — 系统总览（含三仓 ASCII 图 + 数据流 + Harness 机制 + 当前规模）
- [[dual-loop]] — 双工作流闭环（knowledge 4 步 + engineering 4 步 + 触发关系）
- [[memory-stack]] — 5 层 memory 栈（与三仓正交，覆盖 Claude Code 长期记忆）
- [[ohmybrain-three-tier-seed]] — 三仓架构设计笔记（事实源）

## 演化记录

- **2026-04-12 前**：单仓原型（一体化仓库，业务 + 知识 + 模板混在一起）
- **2026-04-12 ~ 17**：架构拆分为三仓，初版强调 "core → project → hub" 线性下游
- **2026-05-24**：哲学澄清，明确 Hub 为大脑（主动）、project 为需求牵引（驱动）、core 为被动模板（被更新）
- **2026-06-09**：同步三模板 + Agent 协作目录口径，旧 `template/` 单模板表达改为 `template-*`
