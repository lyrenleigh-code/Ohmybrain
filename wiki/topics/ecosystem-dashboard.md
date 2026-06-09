---
type: topic
created: 2026-05-24
updated: 2026-06-09
tags: [dashboard, 生态, 状态, 实时]
---

# Ohmybrain 生态 Dashboard

跨仓状态快照。**非实时**（需手动 / 半自动同步），但比"散在各处看"快。

> 上次同步：**2026-06-09**（方式：入会自检一致性审计 workflow 补登 3 新项目 SonarSim/VisioForge/CooperativeASW + 刷新 UWAcomm_usbl/FlowGen 焦点 + `scripts/dashboard_snapshot.py` 重算规模表 memory 67→77）
>
> 来源：本页是聚合视图。各项目仓有独立 wiki/log.md，本页 link 而不复制。各项目「当前焦点」的 session 日期 / HEAD 锚点抽自 auto-memory 索引（`~/.claude/projects/D--Claude/memory/MEMORY.md`），见 [[memory-index]]。
>
> **stale 标记约定**：项目「当前焦点」session 日期距今 **> 30 天** 视为 stale（标 🕸️），需要主动回访确认状态；本表锚点皆 ≤ 30 天（最早 UWAnet 仅前期调研无 session）。

## 仓 / 项目状态总览

### TechReq / 水声通信算法仿真

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **UWAcomm** | 🟢 活跃开发 | 6 通信体制 V→V→V 持续迭代；2026-05-16 rx_stream_p4 接口移植（claude worktree 4 commit `d74c0a2`+`3d6d0b5` 未 push）+ 双回归 RCA（algo A FAIL / fd=1Hz 50% 回归 vs `a291af4`） | `D:\Claude\TechReq\UWAcomm` |
| **USBL** | 🟢 活跃开发 | 超短基线自定位；2026-04-25 H8 spec draft 落地，等用户答 D1-D4，H7 未起 | `D:\Claude\TechReq\USBL` |
| **UWAnet** | 🟡 前期调研 | 水声组网协议 (Aqua-Sim-NG / ns-3)，尚无 session 锚点 | `D:\Claude\TechReq\UWAnet` |
| **UWAcomm_usbl** 🔒 | 🟢 活跃 | 整机原型样机 + 总集成（2026-04-25 派生）；2026-06-01 SPEC-003 水听器收发三板架构（通用平台分置）+ 06-03/05/07 CAGE5 5 元阵东南大学水池实测 DOA 调试（CBF 优于 TDOA，方位泛化 1.2-1.9°）；HEAD `c6d608e`+（pooldata 实测线已 push gitlab） | `D:\Claude\TechReq\UWAcomm_usbl` |
| **SonarSim** 🔒 | 🟢 活跃 | 主动声呐界面仿真（显控台 + 探测链路，MATLAB App Designer，无依赖，手动模式，2026-06-03 派生）；SPEC-001 已实现跑通（单发同频干扰混响强度图，11 个 .m，T1-T4 单测过）+ 2026-06-04 绝对定标升级（接声呐方程）+ 18km 长程场景；已 commit+push 内网 gitlab lilin/SonarSim | `D:\Claude\TechReq\SonarSim` |

### DocProcess / 文档工作区（全私人）

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **Pricing** 🔒 | 🟢 活跃 | 军用软件四号文报价（jy-pricing skill 驱动） | `D:\Claude\DocProcess\Pricing` |
| **UWAprojDoc** 🔒 | 🟢 活跃 | 水声专项方案；2026-05-29 业务场景 C1-C6 全套（C5 区域预警 / C6 编队协同探潜 使命级新增 + 六详章 + ch04§4.1.4 覆盖矩阵 + 独立场景 docx）；已 commit `ad59ef8`（本地未 push） | `D:\Claude\DocProcess\UWAprojDoc` |
| **CooperativeDetection** 🔒 | 🟢 活跃 | 4 专题 12 课题方案（2026-05-08 派生） | `D:\Claude\DocProcess\CooperativeDetection` |
| **PaperReview** 🔒 | 🟢 活跃 | 学位论文外审（中文）；2026-05-09 派生，HEAD `b3568f6`，当前在评水声专硕一份 | `D:\Claude\DocProcess\PaperReview` |
| **DigitalTwinGuide** 🔒 | 🟢 活跃 | 数字孪生实施指南方法论；2026-05-13 首版宋体 docx + 4 步 pandoc pipeline，63 init + docx 仍 stage 未 commit | `D:\Claude\DocProcess\DigitalTwinGuide` |
| **DigitalTwin1plusN** 🔒 | 🟡 起步 | 「1+N」水下集群数字孪生体系方案（2026-05-25 派生）；P1-P11 概念决议（P11 暂缓）+ 3 spec，HEAD `234eb11`（7 commit） | `D:\Claude\DocProcess\DigitalTwin1plusN` |
| **VisioForge** 🔒 | 🟡 起步 | 通用 Visio 出图工作区（2026-06-02 派生，复用全局 flowgen-* 8 skill）；首批 6 张 SN 效能预报图 1:1 高保真复刻（自建 scripts/replica_lib2.py）；git init -b main 首 commit 未提交 | `D:\Claude\DocProcess\VisioForge` |
| **CooperativeASW** 🔒 | 🟢 活跃 | UWAprojDoc「编队协同探潜配置仿真与效能评估分系统」单列细化独立 docx 方案（2026-06-03 派生，DEPENDS_ON=UWAprojDoc）；全文 17 章 223k 字 + 24 图全细化 + docx 969KB/100 页；2026-06-04 图件大改（I 族接口图 + build_docx A4 fit-to-box）；commit `f46b16d`+`5da5de1`（本地未 push） | `D:\Claude\DocProcess\CooperativeASW` |

### Tools / 跨项目工具

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **FlowGen** | 🟢 活跃 | 需求→Visio/Mermaid 出图工具族；2026-06-01 阶段1 系统架构图（commit `5372721` 已 push gitlab）+ 2026-06-02 阶段2-A 逻辑架构图 + 2026-06-04 archmap business/data-functional/interface(I 族)/stdflow 多 renderer + 新 archmap skill | `D:\Claude\Tools\FlowGen` |
| **AnthropicPPT** | 🟢 活跃 | FIELDBOOK PPT 模板（2026-05-23 派生，design_tokens + 8 helpers + 9 layout + skill `anthropic-ppt`） | `D:\Claude\Tools\AnthropicPPT` |
| **IconForge** | 🟡 未实装 | 自然语言→图标 SVG 生成工具（2026-05-29 派生后暂停，HEAD `a6b361a` 66 文件未实装；已评估 samzong/ai-icon-generator，恢复后下一步 M1 spec） | `D:\Claude\Tools\IconForge` |

### 母仓 / Hub

| 仓 | 状态 | 最近动态 | 路径 |
|---|------|------|------|
| **Ohmybrain** (本仓 = Hub) | 🟢 活跃 | 2026-06-09 入会自检一致性审计：补登 3 新项目（SonarSim/VisioForge/CooperativeASW）到 dashboard/system-overview/decision-log(ADR-021~023)/roadmap/memory-index + 计数 67→77 + 刷新 UWAcomm_usbl/FlowGen 焦点。上游 commit `6e4fedf`（2026-06-04 注册 3 新项目导航卡 + CLAUDE.md 映射），本批尚未 commit | `D:\Claude\Ohmybrain` |
| **ohmybrain-core** (母仓) | 🟢 活跃 | 三模板就位；候选下沉队列见 [[core-update-queue]] | `D:\Claude\ohmybrain-core` |

## Hub 内部规模快照（2026-06-09）

> 由 `scripts/dashboard_snapshot.py` 统计生成（wiki 子目录页数 / scripts / 本地 skills / agents / rules / memory）。skill 一栏区分**本地两层**：磁盘 SKILL.md 与叠加 plugin/marketplace 注入后的可见总数。

| 指标 | 数值 | 说明 |
|------|------|------|
| wiki 内容页 | **104** | 20 concepts + 8 entities + 11 architecture + 5 topics + 4 explorations + 31 source-summaries + 25 mcp-entities + 0 comparisons |
| wiki 总文件 | **106** | 104 内容页 + 根 `index.md` + `log.md` |
| 自动化脚本 | **22** | `scripts/*.py` 全量（含 dashboard_snapshot.py） |
| Hooks | **8** | 3 阻断 + 4 提醒 + 1 注入（见下表） |
| 全局 skill（本地） | **31** | `~/.claude/skills/` 含 SKILL.md 的目录（33 个目录中 31 个有 SKILL.md） |
| 全局 skill（注入后可见） | **90+** | 本地 31 叠加 `ecc:*` plugin / marketplace 注入后；裸写 90+ 会掩盖本地真实规模，故两层并列 |
| 全局 agent | **55** | `~/.claude/agents/*.md` |
| rules 目录 | **15** | common / zh / web + 12 语言（cpp/csharp/dart/golang/java/kotlin/perl/php/python/rust/swift/typescript） |
| Memory 条目 | **77** | 4 类：user 1 / feedback 21 / project 52 / reference 3（见 [[memory-index]]） |
| MCP servers | **6** | context7 / exa / github / memory / playwright / sequential-thinking |

> ADR 不是独立文件，集中存放在 [[decision-log]]（章节形式 ADR-001~023）。

## Hub Hooks 当前状态

| Hook | 脚本 | 类型 | 触发 |
|------|------|------|------|
| 🔴 阻断 | `check_raw_write.py` | PreToolUse Edit/Write | raw/ 写入拦截 |
| 🔴 阻断 | `check_private_tags.py` | PreToolUse Edit/Write | `<private>` 标签拦截 |
| 🔴 阻断 | `check_index_log_sync.py` | Stop | wiki 改动但 index/log 未同步 |
| 🟡 提醒 | `post_wiki_write.py` | PostToolUse | 写入 wiki 后自动 lint |
| 🟡 提醒 | `raw_ingest_reminder.py` | PostToolUse Bash | Bash 触及 raw/ 提醒 |
| 🟡 提醒 | `commit_reminder.py` | Stop | wiki 未 commit 提醒 |
| 🟡 提醒 | `check_memory_log_gap.py` | Stop | memory 与 wiki/log 缺口提醒 |
| 🟢 注入 | `session_context.py` | SessionStart | 载入会话上下文 |

详细见 [[system-overview]] § Harness 机制 与 [[harness-resources]]。

## Promote 队列（候选回流到 Hub）

下游项目中 wiki/* 含"跨项目可复用"标注但未 promote 的条目。**与 [[core-update-queue]] 区分**：本节是「项目 → Hub wiki」的知识回流（promote-answer）；core-update-queue 是「Hub → ohmybrain-core/template」的机制下沉（sync-to-core）。

> TODO 用脚本扫描 `D:\Claude\TechReq\*\wiki\` 和 `D:\Claude\DocProcess\*\wiki\`（除 🔒 标识）

候选示例（人工识别，截至 2026-05-29）：

- UWAcomm `wiki/conclusions.md` 中"高 SNR clamp 算法适用边界"（参见 [[decision-log]] 相关 ADR）
- USBL `wiki/concepts/cage5-3d-doa.md` 中"立体阵 3D 几何"算法描述
- DocProcess/UWAprojDoc 中"4 步 pandoc pipeline"（文档自动化方法论，可去敏后 promote）

## 自动同步机制

`scripts/dashboard_snapshot.py`（纯标准库，`pathlib` 跨平台）统计并打印「Hub 内部规模快照」markdown 表到 stdout，供本页手动粘贴对齐。覆盖范围：

- wiki 各子目录 `*.md` 页数 + 根文件 + 总计
- `scripts/*.py` 数量
- `~/.claude/skills/` 含 SKILL.md 的目录数（本地两层之「本地」层）
- `~/.claude/agents/*.md` 数量
- `~/.claude/rules/` 目录数
- `~/.claude/projects/D--Claude/memory/` 各前缀类型（user/feedback/project/reference）文件数

用法：`python scripts/dashboard_snapshot.py`，将输出表替换本页「Hub 内部规模快照」。「当前焦点」session 锚点仍需手动从 [[memory-index]] 抽取（脚本不解析 memory 内容）。

## 待办（人工维护）

- TODO 每周末扫一次本页，标记状态变化 + 刷新 stale（>30 天）标记
- TODO 扩展 `scripts/dashboard_snapshot.py` 解析各项目 log.md latest 状态（当前仅统计规模）
- TODO promote 队列脚本化扫描（替代人工识别）

## 相关页面

- [[system-overview]] — 系统架构总览（含规模表）
- [[hub-as-brain]] — 大脑功能定位
- [[harness-resources]] — Hooks / Skills / Rules 全景
- [[memory-index]] — auto-memory 77 条目索引（本页 session 锚点来源）
- [[core-update-queue]] — Hub → core 下沉候选队列
- [[decision-log]] — ADR-001~023 决策记录