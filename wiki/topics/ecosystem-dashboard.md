---
type: topic
created: 2026-05-24
updated: 2026-06-14
tags: [dashboard, 生态, 状态, 实时]
updated: 2026-06-24
---

# Ohmybrain 生态 Dashboard

跨仓状态快照。**非实时**（需手动 / 半自动同步），但比"散在各处看"快。

> 上次同步：**2026-06-24**（方式：ultracode 入会自检（六）5 维 workflow 审计 + 逐 finding 对抗验证（44 agent / 33 confirmed / 1 refuted / 5 uncertain）；**USBL_hw 行刷新**（`32ae044`/38→`c7c07da`/71 commit，已建 gitlab 远程，写权交回 Codex）+ **PaperTrans 补登状态行**（06-15 派生当日漏登）+ CANON memory 81→83 / project 56→58 / skills 31→32 多页级联 + **CooperativeDetection / PaperReview 标 🕸️**（>30 天）+ FieldKit/FlowGen/AnthropicPPT 锚点刷新；UWAcomm / USBL / UWAcomm_usbl / DigitalTwin1plusN 四行 git 未动、memory 回填仍 pending）
>
> 来源：本页是聚合视图。各项目仓有独立 wiki/log.md，本页 link 而不复制。各项目「当前焦点」的 session 日期 / HEAD 锚点抽自 auto-memory 索引（`~/.claude/projects/D--Claude/memory/MEMORY.md`），见 [[memory-index]]。
>
> **stale 标记约定**：项目「当前焦点」session 日期距今 **> 30 天** 视为 stale（标 🕸️），需要主动回访确认状态；@2026-06-24 标 🕸️ 者：DigitalTwinGuide（init 起 master 无 commit，停滞约 42 天）/ CooperativeDetection（05-09 commit，46 天）/ PaperReview（05-09 commit，46 天，工作树 dirty=7 或在评中待确认）；其余锚点 ≤ 30 天（最早 UWAnet 仅前期调研无 session）。

## 仓 / 项目状态总览

### TechReq / 水声通信算法仿真

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **UWAcomm** | 🟢 活跃开发 | 6 通信体制 V→V→V 持续迭代；2026-05-16 rx_stream_p4 接口移植（claude worktree 4 commit `d74c0a2`+`3d6d0b5` 未 push）+ 双回归 RCA（algo A FAIL / fd=1Hz 50% 回归 vs `a291af4`）；**main `ba03e8a` 已落「6 体制水池试验验证」里程碑**（commit 标题：5 实测 BER=0 + OTFS sim 验证；结论待用户复核，auto-memory 尚停 05-16 待回填） | `D:\Claude\TechReq\UWAcomm` |
| **USBL** | 🟢 活跃开发 | 超短基线自定位；2026-04-25 H8 spec draft（等答 D1-D4，H7 未起）；**2026-05-25 main `accc52a`：D-OQ-1 链路预算 / D-OQ-2 多深度标定两跨项目回流专题（回流自 UWAcomm_usbl）+ README mermaid 三章节**（auto-memory 仅 project_usbl_h8_drafting，待回填） | `D:\Claude\TechReq\USBL` |
| **UWAnet** | 🟡 前期调研 | 水声组网协议 (Aqua-Sim-NG / ns-3)，尚无 session 锚点 | `D:\Claude\TechReq\UWAnet` |
| **UWAcomm_usbl** 🔒 | 🟢 活跃 | 整机原型样机 + 总集成（2026-04-25 派生）；calibration 分支 06-03/05/07 CAGE5 5 元阵东南大学水池实测 DOA 调试（CBF 优于 TDOA，方位泛化 1.2-1.9°，HEAD `c6d608e` 已 push gitlab）；**main `73cf223`：硬件功能接口图 v3 + SPEC-003 接口定义**（2026-06-01 收发三板架构后续；dashboard 原仅记 calibration 线） | `D:\Claude\TechReq\UWAcomm_usbl` |
| **SonarSim** 🔒 | 🟢 活跃 | 主动声呐界面仿真（显控台 + 探测链路，MATLAB App Designer，无依赖，手动模式，2026-06-03 派生）；SPEC-001 已实现跑通（单发同频干扰混响强度图，11 个 .m，T1-T4 单测过）+ 2026-06-04 绝对定标升级（接声呐方程）+ 18km 长程场景；已 commit+push 内网 gitlab lilin/SonarSim | `D:\Claude\TechReq\SonarSim` |
| **USBL_hw** 🔒 | 🟢 活跃 | USBL 硬件设计（**engineering-hardware 子型首例**，2026-06-10 派生，手动模式，ADR-026）；**设计决策层基本全冻结**：收发链 TX+RX 全 first-pass（NeUB-816 实测闭环 TVR~146.8dB@12kHz→190dB 仅需~184W / 功放路线 a；2026-06-12 平台重构去 Zynq→分布式 ARM 控制板+采集 FPGA-A 数字直驱）+ SPEC 成熟度 001/002 first-pass·003 third-pass·004 confirmed·005 first-pass（005 因平台重构降级重开）；2026-06-15 S0 发射链仿真签核 + 方案完整性审查；**2026-06-16~23 方案设计说明书成稿化**（v1.0 终稿 `82ae586` 已 push + v1.1 通信章 §5.2 深扩写 / 公式 OMML 原生化 / 图重画）+ SPEC-006 收发半双工+值班 + SPEC-007 五板号统一 + 板2 timing 平台重构落盘 + 询证函 send-pack 全面同步 + §算法/§阵列校准并入；HEAD `c7c07da`（06-23）共 71 commit，**已建内网 gitlab 远程**（lilin/USBL_hw，ahead 3 未 push），工作树有未提交改动；**2026-06-23 写权交接回 Codex**；剩余全属外部依赖（江苏水声 NeUB-816 大信号 + 供应商询证 + 耐压 FEA + 水池实测） | `D:\Claude\TechReq\USBL_hw` |

> 另：`projects/usbl-s1/` 是 USBL S1 仿真平台 **autonomous workflow dry-run（2026-04-22，Phase 0-4 全 PASS）的归档性质导航页**，非独立项目（USBL 权威入口仍是 `projects/usbl/`），故不单列状态行。

### DocProcess / 文档工作区（全私人）

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **Pricing** 🔒 | 🟢 活跃 | 军用软件四号文报价（jy-pricing skill 驱动） | `D:\Claude\DocProcess\Pricing` |
| **UWAprojDoc** 🔒 | 🟢 活跃 | 水声专项方案；2026-05-29 业务场景 C1-C6 全套（C5 区域预警 / C6 编队协同探潜 使命级新增 + 六详章 + ch04§4.1.4 覆盖矩阵 + 独立场景 docx）；已 commit（HEAD `eed5374`，05-29 尾注；`ad59ef8` 为其同 session 祖先，本地未 push，dirty=2） | `D:\Claude\DocProcess\UWAprojDoc` |
| **CooperativeDetection** 🔒 | 🕸️ 待回访 | 4 专题 12 课题方案（2026-05-08 派生）；HEAD `6113b96`（05-09，>30 天未动，dirty=0） | `D:\Claude\DocProcess\CooperativeDetection` |
| **PaperReview** 🔒 | 🕸️ 待回访 | 学位论文外审（中文）；2026-05-09 派生，HEAD `b3568f6`（>30 天无新 commit，工作树 dirty=7——可能在评中，待回访确认） | `D:\Claude\DocProcess\PaperReview` |
| **DigitalTwinGuide** 🔒 | 🕸️ 停滞 | 数字孪生实施指南方法论；2026-05-13 首版宋体 docx + 4 步 pandoc pipeline，docx 仍 stage 未 commit（dirty=65）；**init 起 master 无 commit，停滞约 42 天，待回访** | `D:\Claude\DocProcess\DigitalTwinGuide` |
| **DigitalTwin1plusN** 🔒 | 🟢 活跃 | 「1+N」水下集群数字孪生体系方案（2026-05-25 派生）；P1-P11 概念决议（P11 暂缓）+ 3 spec；**同日（05-25 晚）v0-v5 完整可研报告 docx 落地（4 步 pandoc pipeline，报价表按 V1.0 格式），HEAD `234eb11`→`c866bb7`（12 commit，本地无远程）**（auto-memory 待回填同日 docx 延续） | `D:\Claude\DocProcess\DigitalTwin1plusN` |
| **VisioForge** 🔒 | 🟡 起步 | 通用 Visio 出图工作区（2026-06-02 派生，复用全局 flowgen-* 8 skill）；首批 6 张 SN 效能预报图 1:1 高保真复刻（自建 scripts/replica_lib2.py）；git init -b main 首 commit 未提交 | `D:\Claude\DocProcess\VisioForge` |
| **CooperativeASW** 🔒 | 🟢 活跃 | UWAprojDoc「编队协同探潜配置仿真与效能评估分系统」单列细化独立 docx 方案（2026-06-03 派生，DEPENDS_ON=UWAprojDoc）；全文 17 章 223k 字 + 24 图全细化 + docx 969KB/100 页；2026-06-04 图件大改（I 族接口图 + build_docx A4 fit-to-box）；commit `f46b16d`+`5da5de1`（本地未 push） | `D:\Claude\DocProcess\CooperativeASW` |
| **PaperTrans** 🔒 | 🟢 活跃 | 外文论文英译中翻译工作区（2026-06-15 派生，template-document SOP，手动模式）；一篇=一spec=一译稿，wiki 术语表+翻译规范两页种子；**首篇全书译稿收尾归档（23 单元草稿 + 367 页 PDF 待终审，HEAD `ed1a7ad`/06-16），本地 main 无远程** | `D:\Claude\DocProcess\PaperTrans` |

### Tools / 跨项目工具

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **FlowGen** | 🟢 活跃 | 需求→Visio/Mermaid 出图工具族；2026-06-01 阶段1 系统架构图（commit `5372721` 已 push gitlab）+ 2026-06-02 阶段2-A 逻辑架构图 + 2026-06-04 archmap business/data-functional/interface(I 族)/stdflow 多 renderer + 新 archmap skill + 2026-06-15 M5-pro 专业正交路由流程图 + 逐 skill 详解 PPT（HEAD `385072e`，gitlab/main） | `D:\Claude\Tools\FlowGen` |
| **AnthropicPPT** | 🟢 活跃 | FIELDBOOK PPT 模板（2026-05-23 派生，design_tokens + 8 helpers + 9 layout + skill `anthropic-ppt`）；2026-06-15 新增 `styled_diagram`（Calibration Field 消费者②，native pptx 风格层 + 4 图种，HEAD `438c57e`/gitlab） | `D:\Claude\Tools\AnthropicPPT` |
| **IconForge** | 🟡 未实装 | 自然语言→图标 SVG 生成工具（2026-05-29 派生后暂停，HEAD `a6b361a` 66 文件未实装；已评估 samzong/ai-icon-generator，恢复后下一步 M1 spec） | `D:\Claude\Tools\IconForge` |
| **FieldKit** | 🟢 活跃 | 「校准场 / Calibration Field」图示风格系统（2026-06-15 派生，template-tool SOP 脚手架，借鉴 pbakaus/impeccable）；共享 design kit（tokens + kit.css + sonar motif + 氛围层 baker）→ 消费者①HTML→PNG/PDF 生成器（flow + composition，暗 Lacquer Instrument + 亮 Paper Field 双调色板）SHIPPED v1 + 消费者②AnthropicPPT styled_diagram 布局族 SHIPPED v2；HEAD `5a9d75b`（06-15，扩 3 图种 layered/cover/sequence + 字体系统），已建内网 gitlab 远程（lilin/FieldKit，已 push）；skill `calibration-field` 已注册 | `D:\Claude\Tools\FieldKit` |

### 专利工作区（私人）

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **Patents** 🔒 | 🟡 候选 | 私密专利交底书工作区（**无 git**，禁 `git init` 避免泄露草稿历史）；3 候选交底书：iusbl-jacobian / otfs-spread-pilot / usbl-cage5-3d-hybrid-doa | `D:\Claude\Patents` |

### 母仓 / Hub

| 仓 | 状态 | 最近动态 | 路径 |
|---|------|------|------|
| **Ohmybrain** (本仓 = Hub) | 🟢 活跃 | 2026-06-09 两批：(1) 入会自检一致性审计补登 3 新项目（SonarSim/VisioForge/CooperativeASW）+ 计数 67→77（commit `7b7fa9d`）；(2) **Claude+Codex 协作协议层**（document-protocol / claude-codex-collaboration / agent-handoff + agents//workflows/ 新分类 + 根 AGENTS.md，**ADR-024**）+ 入会自检审计二修协议层「部分登记」stale（wiki 计数 104→107 跨 6 文件 + 3 新页 §3 合规 + 4 交叉链 + memory 77→78）。本批 commit + push gitlab main | `D:\Claude\Ohmybrain` |
| **ohmybrain-core** (母仓) | 🟢 活跃 | 三模板就位；候选下沉队列见 [[core-update-queue]] | `D:\Claude\ohmybrain-core` |

## Hub 内部规模快照（2026-06-24）

> 由 `scripts/dashboard_snapshot.py` 统计生成（wiki 子目录页数 / scripts / 本地 skills / agents / rules / memory）。skill 一栏区分**本地两层**：磁盘 SKILL.md 与叠加 plugin/marketplace 注入后的可见总数。

| 指标 | 数值 | 说明 |
|------|------|------|
| wiki 内容页 | **107** | 20 concepts + 8 entities + 12 architecture + 1 agents + 1 workflows + 5 topics + 4 explorations + 31 source-summaries + 25 mcp-entities + 0 comparisons |
| wiki 总文件 | **109** | 107 内容页 + 根 `index.md` + `log.md` |
| 自动化脚本 | **24** | `scripts/*.py` 全量（含 dashboard_snapshot.py；2026-06-10 +2 工作区级 hook 脚本） |
| Hooks | **8 + 2** | Hub 8（3 阻断 + 4 提醒 + 1 注入，见下表）+ 工作区级 2（见表下注） |
| 全局 skill（本地） | **32** | `~/.claude/skills/` 含 SKILL.md 的目录（34 个目录中 32 个有 SKILL.md） |
| 全局 skill（注入后可见） | **90+** | 本地 32 叠加 `ecc:*` plugin / marketplace 注入后；裸写 90+ 会掩盖本地真实规模，故两层并列 |
| 全局 agent | **55** | `~/.claude/agents/*.md` |
| rules 目录 | **15** | common / zh / web + 12 语言（cpp/csharp/dart/golang/java/kotlin/perl/php/python/rust/swift/typescript） |
| Memory 条目 | **83** | 4 类：user 1 / feedback 21 / project 58 / reference 3（见 [[memory-index]]；含 2026-06-24 自检 session + PaperTrans init 条目） |
| MCP servers | **6** | context7 / exa / github / memory / playwright / sequential-thinking |

> ADR 不是独立文件，集中存放在 [[decision-log]]（章节形式 ADR-001~029）。

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

> **工作区级 ×2**（2026-06-10，仅注册 `D:/Claude` 会话根，脚本托管 Hub `scripts/`）：`check_push_readme.py` 🔴 PreToolUse Bash（push 前 README 同步检查，`SKIP_README=1` 逃生）；`calendar_reminder.py` 🟡 Stop（每日 calendar 日志提醒，4h 节流）。
>
> **其他 settings 注册的操作/一致性 guard（不计入上表策展 8）**：`agent_writelock.py`（PreToolUse 写锁 + Stop 释放）；`sync_agent.py --check`（Stop，agent 同步）；**`dashboard_snapshot.py --check`（Stop，2026-06-14 新增——CANON 计数校验，显式注册表逐条比对 wiki 计数 token vs 实跑值，不一致才提醒，根治计数级联反复）**。

详细见 [[system-overview]] § Harness 机制 与 [[harness-resources]]。

## Promote 队列（候选回流到 Hub）

下游项目中 wiki/* 含"跨项目可复用"标注但未 promote 的条目。**与 [[core-update-queue]] 区分**：本节是「项目 → Hub wiki」的知识回流（promote-answer）；core-update-queue 是「Hub → ohmybrain-core/template-*」的机制下沉（sync-to-core）。

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
- [[memory-index]] — auto-memory 83 条目索引（本页 session 锚点来源）
- [[core-update-queue]] — Hub → core 下沉候选队列
- [[decision-log]] — ADR-001~029 决策记录
