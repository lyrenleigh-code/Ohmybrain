---
type: architecture
created: 2026-05-24
updated: 2026-05-24
tags: [ADR, 决策, log]
---

# 决策记录 (ADR-style)

跨仓重大架构决策的累积记录。**比 git log 更高粒度**（合并多次 commit），**比 memory 更结构化**（含动机 / 选项 / 后果）。

最新在上。

---

## ADR-007 · 2026-05-24 · Hub 大脑哲学澄清

### 触发

V4 PPT 编制过程发现 Hub wiki 描述与 ohmybrain-core/workflows/ 不一致；user 反馈"Hub 没起到大脑的作用"。

### 决策

明确三仓哲学：
- **Ohmybrain (Hub) = 大脑**（主动 · 接收反馈 + 决策 + 更新模板）
- **项目 = 需求牵引**（业务驱动）
- **ohmybrain-core = 被动模板**（被 Hub 更新）

### 实现

新建 wiki 页：
- [[three-tier-architecture]] — 哲学定义
- [[dual-loop]] — 4+4 闭环
- [[hub-as-brain]] — 大脑功能定位 + 8 类 gap
- 8 个 dedicated 页（本页 + anti-patterns / workflow-glossary / harness-resources / memory-index / conventions / ecosystem-dashboard / roadmap）

修 [[system-overview]] 三处不一致。

### 后果

- ✓ wiki 成为 single source of truth
- ✓ 不必再回 ohmybrain-core 翻 template/
- ⚠ 维护成本：需要持续填充 dedicated 页（roadmap）

---

## ADR-006 · 2026-05-23 · AnthropicPPT 项目派生

### 触发

CC算法开发-v4.pptx 编制过程沉淀 FIELDBOOK 风格 + 9 layout + design tokens，值得复用。

### 决策

派生 `D:\Claude\Tools\AnthropicPPT` 项目，把全过程沉淀为 templates/ + scripts/legacy/ + skill `anthropic-ppt`。

### 实现

- 提取 design tokens（10 色 + 6 字体 + 8 字号 + 网格）
- 提取 helpers（set_run_font / add_text / add_rect / add_arrow / chrome / card / col_number_tag）
- 提取 9 张章节封面图（V4 真实）+ 透明化版
- skill 关键词触发（PPT / 幻灯片 / 演讲）

### 后果

- ✓ 新做 PPT 直接 skill 触发，不重写 build 脚本
- ⚠ templates/layouts/ 还未完全参数化封装

---

## ADR-005 · 2026-04-26 · SC-FDE Phase 4+5 协议层突破

### 触发

SC-FDE jakes fd=1Hz 50% 灾难率长期未解。

### 决策

把 pilot 长度从 64 提升到 128（= blk_cp），突破协议层 limitation。

### 实现

UWAcomm `modem_decode_scfde.m` V4.1+LS fallback，HEAD=47770b0。

### 后果

- ✓ fd=1Hz 47% → 3.37%（14× 改善）
- ⚠ 但 2026-05-16 回归测试 fd=1Hz 50% 再次出现，algo B 待 RCA

---

## ADR-004 · 2026-04-23 · 单根因审计法形成

### 触发

DSSS V1.2 audit：43% BER 灾难率，"plan C 时变性"是假根因。

### 决策

D9/D10 toggle + 跨 4 runner audit 形成单一根因定位法。

### 实现

写入 memory `feedback_single_root_cause_audit`，限 MATLAB 算法 RCA 不外推。

### 后果

- ✓ 0% 灾难率（单一函数 fix 解决）
- ✓ 跨多次 RCA 复用（SC-TDE V5.4 / SC-FDE V4.1）

---

## ADR-003 · 2026-04-17 · 三仓架构定型

### 触发

单仓臃肿（业务 + 知识 + 模板混在一起），难维护。

### 决策

拆分为 `ohmybrain-core (母仓)` + `project-*` + `ohmybrain (Hub)` 三仓。

### 实现

参见 [[ohmybrain-three-tier-seed]] 详细设计。

### 后果

- ✓ 职责清晰
- ⚠ 模板下沉需手动同步（per 2026-04-15 log）
- 后续 → ADR-007 哲学澄清

---

## ADR-002 · 2026-04-14 · wiki-ingester agent 引入

### 触发

主会话 ingest 长论文污染上下文。

### 决策

引入 wiki-ingester sub-agent，独立上下文摄入复杂资料。

### 实现

`~/.claude/agents/wiki-ingester.md` 全局 + 项目本地副本（契约源头）。

### 后果

- ✓ 主会话上下文不被污染
- ⚠ 后台 subagent Write/Bash 权限受限，需主会话代写（feedback_subagent_write_permission）

---

## ADR-001 · 2026-04-12 · Ohmybrain 体系初版

### 决策

搭建一体化仓库 + wiki 骨架 + hooks + slash commands 作为单仓原型。

### 后果

- ✓ 工具链打通（Obsidian + Whisper + Firecrawl + Zotero）
- → ADR-003 拆分为三仓

---

## ADR 格式（写新条目时遵守）

```
## ADR-XXX · YYYY-MM-DD · 简短标题

### 触发
（什么问题催生这个决策）

### 决策
（决定做什么，含可选方案对比）

### 实现
（具体改了什么，新建什么文件 / 接口 / 流程）

### 后果
（积极 ✓ 和潜在 ⚠ 两面）
```

## 相关页面

- [[hub-as-brain]] — 大脑功能定位
- [[three-tier-architecture]] — 三仓哲学
- [[../topics/roadmap]] — 决策 → 未来 roadmap
