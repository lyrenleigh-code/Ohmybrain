---
type: architecture
created: 2026-05-24
updated: 2026-05-24
tags: [闭环, workflow, knowledge, engineering, 触发关系]
---

# 双工作流闭环

ohmybrain-core 的 `template/workflows/` 定义两个独立但相互触发的工作流闭环。**两者都在 project 内执行**，Hub 不参与具体闭环，但 Hub 接收 `knowledge.promote` 的产出。

## 闭环全图

```
          ┌──────────────────── knowledge 闭环 (4 步) ────────────────────┐
          │                                                                │
          │    01 ingest  ─→  02 query  ─→  03 promote  ─→  04 review     │
          │       ↑                                              │         │
          │       └──── 弱触发（review 提示新资料需 ingest）─────┘         │
          │                                                                │
          └────────────────────────────────────────────────────────────────┘
                              ↑                          ↓
                    跨闭环触发 │                          │ 完成判定
                    (query 完成 │                          │ (validate 后
                    后才能 spec)│                          │  触发 promote)
                              ↓                          ↑
          ┌──────────────── engineering 闭环 (4 步) ──────────────────────┐
          │                                                                │
          │    01 spec  ─→  02 plan  ─→  03 implement  ─→  04 validate    │
          │       ↑                                              │         │
          │       └──── 弱触发（validate 后开启新 task spec）────┘         │
          │                                                                │
          └────────────────────────────────────────────────────────────────┘
```

实线 = 主流；虚线 = 弱触发（不是强依赖，但通常这样流转）。

## knowledge 闭环 (4 步)

来源：`ohmybrain-core/template/workflows/knowledge/`

| 步骤 | 动词 | 触发 | 工具 / 命令 | 产出 |
|------|------|------|-----------|------|
| **01** | `ingest` | 新资料进入 `raw/`（论文 / 文章 / 视频 / 仓库） | `/ingest <路径>` 或 wiki-ingester agent | `wiki/source-summaries/<slug>.md` + cross-ref 到相关 concepts |
| **02** | `query` | 用户提出领域问题 | 主会话 3 层渐进披露：`index → log → 详` | "wiki 记录" vs "通用知识" 分类回答 |
| **03** | `promote` | 项目产出跨项目可复用结论 | `/promote-answer`（**仅下游**项目有此命令） | Hub `wiki/{concepts,entities,...}/` 新页 + Hub index/log 同步 |
| **04** | `review` | 定期（建议周/月） | 人工浏览 `index.md` + `log.md` | 整理 / 合并 / 删过期 / 触发新 ingest |

### 关键约束

- **Hub 没有 `/promote-answer`**：Hub 是 promote 的**终点**，不向上回流
- **`raw/` 永远只读**：所有 ingest 必经 hook 拦截 (`check_raw_write.py`)
- **wiki 改动必同步 index + log**：Stop hook (`check_index_log_sync.py`) 强制
- **`<private>` 标签拦截**：私人项目知识不进公开 Hub (`check_private_tags.py`)

## engineering 闭环 (4 步)

来源：`ohmybrain-core/template/workflows/engineering/`

| 步骤 | 动词 | 触发 | 工具 / 命令 | 产出 |
|------|------|------|-----------|------|
| **01** | `spec` | 新任务开始（query 完成、知识 ready） | 写 `specs/active/<slug>.md`（目标 / 范围 / verification） | spec.md |
| **02** | `plan` | spec 复杂或跨多文件 | 写 `plans/<slug>.md`（分阶段、依赖、风险） | plan.md |
| **03** | `implement` | plan 完成或直接 spec → code | 写 `src/` / `modules/` 代码 | 可工作代码 + commit |
| **04** | `validate` | code 完成、test 跑通 | 验证 BER / NMSE 等业务指标，用户主导终审 | spec 进入 `specs/archive/` |

### 关键约束

- **不代下"完成 / work"结论**：算法 validate 必须用户判定（feedback_uwacomm_testing_boundary）
- **spec 单职责**：一个 spec 只解决一个具体问题，避免 scope creep
- **V→V→V 递进**：每个 V 是一次完整 RCA + fix + verify 闭环，不跳号、不并行
- **PMF 双指标**：上一 V RCA 完成 + 5 项回归 test 全通过，才能"过版"进下一 V

### RCA 子环节（validate 失败时）

`engineering.validate` 不是直接通过/失败二分，而是含一个迭代子环节：

```
04 validate
   ↓
[指标达标?]
   ├─ ✓ → archive（spec 进入 specs/archive/）
   └─ ✗ → 进入 RCA (Root Cause Analysis)
              ↓
         [找单一根因]
              ↓
         [fix + 重新 validate]
              ↓
         回到 implement → 新 V (V→V→V 递进)
```

**RCA ≠ 闭环 4 步之一**，是 validate 失败时的子步骤。详见 [[../concepts/workflow-glossary#RCA]]。

### Phase 0：module-design（可选）

`workflows/engineering/00-module-design.md` 是 phase 0，不算闭环内的循环步骤。用于：

- 新模块设计：规划接口、数据流、依赖
- 非平凡重构：大规模架构调整前的设计文档

phase 0 的产出**先于 01 spec**，但不是每个 task 都需要 module-design。

## 跨闭环触发关系

```
┌─────────── knowledge ───────────┐
│                                  │
│   01 ingest → 02 query           │
│                  ↓                │
│             (knowledge ready)    │
│                  ↓                │
└──────────────────│───────────────┘
                   │
                   ↓ (新任务有了足够调研)
┌──────────────────│───────────────┐
│                  ↓                │
│             01 spec               │
│                ↓                  │
│             02 plan               │
│                ↓                  │
│            03 implement           │
│                ↓                  │
│            04 validate            │
│                ↓                  │
│        (跨项目可复用？)            │
│                ↓ yes              │
└──────────────────│───────────────┘
                   │
                   ↓
┌──────────────────│───────────────┐
│                  ↓                │
│            03 promote             │
│                ↓                  │
│           (Hub wiki 更新)         │
│                ↓                  │
│            04 review              │
│                ↓                  │
│     (新资料 / 新方向？)            │
│                ↓ yes              │
│            01 ingest              │
│                ↓                  │
│  ... 进入下一轮闭环                │
│                                  │
└──────────────────────────────────┘
```

### 何时触发跨闭环

| 当前位置 | 下一步 | 触发条件 |
|---------|--------|---------|
| `knowledge.query` | `engineering.spec` | 知识 ready（已查 + 已读 + 已审 spec 三项定性证据齐备） |
| `engineering.validate` | `knowledge.promote` | 结论跨项目可复用 |
| `engineering.validate` | `engineering.spec`（新 task） | 当前 task 关闭，进入下一 V 或新 task |
| `knowledge.review` | `knowledge.ingest` | review 发现资料空白 / 需要新材料 |

## 两个闭环为什么分开

| 反模式 | 双闭环应对 |
|--------|-----------|
| **跳过 spec 直接 code** | engineering 闭环硬约束 spec 在 implement 之前 |
| **跳过 query 重造轮子** | knowledge 闭环硬约束 query 在 spec 之前 |
| **闭环外跑业务** | 所有 task 必走两个闭环之一，没有"我先随便试试" |
| **闭环交叉污染** | knowledge 写 wiki/source-summaries/；engineering 写 specs/active/；目录隔离 |

## 在 PPT 中的呈现

V4 PPT `CC算法开发-v4.pptx` 把双闭环放在 S09 三仓架构图中，作为 project 仓内部的两条工作流。详见 [[../../Tools/AnthropicPPT/wiki/concepts/slide-layouts]] § 6 Dual-loop diagram。

## 相关页面

- [[three-tier-architecture]] — 三仓架构哲学（Hub = 大脑，project = 需求牵引，core = 被动模板）
- [[system-overview]] — 系统总览（含 Harness 机制 + 当前规模）
- [[memory-stack]] — 5 层 memory 栈（与双闭环正交）
- [[../workflows/agent-handoff]] — Agent 交接流程（双闭环跨 agent / 跨会话续作的交接单载体）
- [[../agents/claude-codex-collaboration]] — Claude+Codex 协作协议（串行交接 = engineering 闭环的 agent 分工版）

## 演化记录

- **2026-04-12**：knowledge 闭环 4 动词 + engineering 闭环 5 步（含 module-design）初版
- **2026-05-24**：明确 engineering 闭环为 4 步（spec / plan / implement / validate），module-design 归 phase 0；显式 4+4 触发关系图
