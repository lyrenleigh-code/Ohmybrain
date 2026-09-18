---
type: topic
created: 2026-05-24
updated: 2026-09-18
tags: [dashboard, 生态, 状态, 实时]
---

# Ohmybrain 生态 Dashboard

跨仓状态快照。**非实时**（需手动 / 半自动同步），但比"散在各处看"快。

> 上次同步：**2026-09-18**（**派生登记 | AUVNetModem**：面向五U 组网条件的水声通信机详细设计（TechReq，engineering-hardware 子型第二例，A 算法 + B 硬件，依赖 AUVNetCoop / UWAcomm / AUVProposal，git `c37e2ce`，ADR-050）——用户裁通信机详细设计从 AUVNetCoop 单列、范围 A + B；SPEC-001 框架 v0 待裁 D1~D10；CANON 级联：活跃 37→38 / TechReq×8→×9 / ADR ~049→~050 / memory 112→115（project 73→74；另补登 09-18 上一会话两条 PowerShell feedback 35→37）/ `MEMORY.md` 索引 →116 行；后台会话在分支 `reg/auvnetmodem` 登记，AUTO-GIT-SNAPSHOT `--gen` 同步重打）
>
> 来源：本页是聚合视图。各项目仓有独立 wiki/log.md，本页 link 而不复制。各项目「当前焦点」的 session 日期 / HEAD 锚点抽自 auto-memory 索引（`~/.claude/projects/D--Claude/memory/MEMORY.md`），见 [[memory-index]]。
>
> **stale 标记约定**：项目「当前焦点」session 日期距今 **> 30 天** 视为 stale（标 🕸️），需要主动回访确认状态；@2026-08-24（入会审计十六重算）标 🕸️ 者：CooperativeDetection（05-09，107 天）/ PaperReview（05-09，107 天，dirty=7 或在评中）/ DigitalTwinGuide（业务自 05-13 停滞约 103 天；08-18 仅 backup_push 快照收口 commit，非业务推进）/ UWAnet（05-25，91 天，前期调研无 session）/ UWAprojDoc（05-29，87 天）/ SonarSim（06-04，81 天）/ CooperativeASW（06-04，81 天）/ PaperTrans（06-16，69 天）/ UWCombatPlatform（06-26，59 天）；DigitalTwin1plusN 已退役（🗑️ ADR-041）不再计；**旗舰 carve-out**：UWAcomm（08-23 活跃）/ USBL / UWAcomm_usbl / USBL_hw 算法-硬件主线维持 🟢；**阻塞非遗忘不标**：CommSimSupport（等官方模板 54 天）/ OceanEnvSupport（等 D1-D5 决断 46 天）/ EnvDataClassify（待 SPEC-001，32 天，本轮踩阈）/ **ImgSonarTwin（07-20，35 天，本轮踩阈——等用户全文审+xlsx 裁决）** / **AUVSurvey（07-25，30 天，本轮踩阈——等用户增删型谱清单）**；**工具族 SHIPPED 稳态不标**：FieldKit / FlowGen / AnthropicPPT（06-15 交付态）/ IconForge（🟡 未实装）；Patents 🟡 候选但 dirty=93 待回访 commit（56 天）。

## 仓库 git 快照（脚本生成）

<!-- AUTO-GIT-SNAPSHOT:START -->
> 脚本生成 @2026-09-18 17:11（`python scripts/dashboard_snapshot.py --gen`），**git 事实以本表为准**；上方手写行只承担业务叙事。远程列：`名✓`=已同步 / `名+N`=本地领先 N / **无远程**=单点风险。

| 仓库 | 分支 | HEAD | 静默 | dirty | 远程 |
|------|------|------|------|-------|------|
| `TechReq/AUVNetModem` | `main` | `c37e2ce` 2026-09-18 | 0d | 0 | **无远程** |
| `TechReq/EnvDataClassify` | `main` | `a7de7b2` 2026-07-23 | 57d  🕸️? | 1 | gitlab✓ |
| `TechReq/SonarFOM` | `main` | `9456931` 2026-08-12 | 37d  🕸️? | 0 | gitlab✓ |
| `TechReq/SonarSim` | `main` | `2a0ebf3` 2026-06-04 | 106d  🕸️? | 0 | gitlab✓ |
| `TechReq/USBL` | `main` | `accc52a` 2026-05-25 | 116d  🕸️? | 3 | gitlab✓ / origin✓ |
| `TechReq/USBL_hw` | `main` | `eb7252a` 2026-07-17 | 63d  🕸️? | 14 | gitlab+6 |
| `TechReq/UWAcomm` | `main` | `53e41e7` 2026-09-02 | 16d | 2 | gitlab+1 / origin+24 |
| `TechReq/UWAcomm_usbl` | `main` | `73cf223` 2026-06-09 | 101d  🕸️? | 22 | gitlab✓ |
| `TechReq/UWAnet` | `main` | `e3b45c5` 2026-05-25 | 116d  🕸️? | 2 | gitlab✓ / origin✓ |
| `DocProcess/AcousticLiteracy` | `main` | `7447ca4` 2026-09-14 | 4d | 2 | **无远程** |
| `DocProcess/AUVNetCoop` | `main` | `de9ee3a` 2026-09-18 | 0d | 3 | **无远程** |
| `DocProcess/AUVProposal` | `main` | `609d09c` 2026-09-17 | 1d | 29 | gitlab✓ |
| `DocProcess/AUVSlopeMCM` | `main` | `82b78b8` 2026-09-11 | 7d | 24 | **无远程** |
| `DocProcess/AUVSurvey` | `main` | `6a79e02` 2026-07-25 | 55d  🕸️? | 10 | gitlab✓ |
| `DocProcess/CommSimSupport` | — | 无 git | — | — | — |
| `DocProcess/CooperativeASW` | `main` | `5da5de1` 2026-06-04 | 106d  🕸️? | 0 | gitlab✓ |
| `DocProcess/CooperativeDetection` | `master` | `6113b96` 2026-05-09 | 132d  🕸️? | 0 | gitlab✓ |
| `DocProcess/CoupledMultiOrder` | `main` | `401b4b4` 2026-08-07 | 42d  🕸️? | 0 | gitlab✓ |
| `DocProcess/DeepSeaIndustry` | `main` | `97fa2c3` 2026-08-30 | 19d | 15 | **无远程** |
| `DocProcess/DigitalTwinGuide` | `master` | `4d9746e` 2026-08-18 | 31d  🕸️? | 0 | gitlab✓ |
| `DocProcess/ImgSonarTwin` | `main` | `5300532` 2026-07-20 | 60d  🕸️? | 1 | gitlab✓ |
| `DocProcess/OceanEnvSupport` | `main` | `15833b0` 2026-07-09 | 71d  🕸️? | 0 | gitlab✓ |
| `DocProcess/PaperReview` | `master` | `b3568f6` 2026-05-09 | 132d  🕸️? | 7 | gitlab✓ |
| `DocProcess/papers` | `?` | **0 commit** | — | 19 | — |
| `DocProcess/PaperTrans` | `main` | `ed1a7ad` 2026-06-16 | 94d  🕸️? | 0 | gitlab✓ |
| `DocProcess/Pricing` | `main` | `fef4f28` 2026-05-25 | 116d  🕸️? | 15 | gitlab✓ |
| `DocProcess/ProductPortfolio` | `main` | `a4696f9` 2026-09-16 | 2d | 1 | **无远程** |
| `DocProcess/SoSCommSupport` | `main` | `0cc3677` 2026-09-14 | 4d | 0 | **无远程** |
| `DocProcess/UUVCommSwarmSim` | `main` | `84fe9c9` 2026-09-13 | 5d | 26 | **无远程** |
| `DocProcess/UWAcommTrial` | — | 无 git | — | — | — |
| `DocProcess/UWAprojDoc` | `master` | `eed5374` 2026-05-29 | 112d  🕸️? | 2 | gitlab✓ |
| `DocProcess/UWCombatPlatform` | `main` | `3ce4928` 2026-06-26 | 84d  🕸️? | 0 | gitlab✓ |
| `DocProcess/VisioForge` | `main` | `07f40cd` 2026-08-18 | 31d  🕸️? | 0 | gitlab✓ |
| `DocProcess/XiaojingLaunch` | `main` | `0b30cd3` 2026-09-08 | 10d | 0 | **无远程** |
| `Tools/AnthropicPPT` | `main` | `438c57e` 2026-06-15 | 95d  🕸️? | 14 | gitlab✓ |
| `Tools/FieldKit` | `main` | `5a9d75b` 2026-06-15 | 95d  🕸️? | 0 | gitlab✓ |
| `Tools/FlowGen` | `main` | `385072e` 2026-06-15 | 95d  🕸️? | 10 | gitlab✓ |
| `Tools/IconForge` | `main` | `a6b361a` 2026-05-29 | 112d  🕸️? | 0 | gitlab✓ |
| `Tools/MetalDinoForge` | `?` | **0 commit** | — | 24 | — |
| `Tools/ObsidianStyleLab` | `main` | `e48dabf` 2026-06-16 | 94d  🕸️? | 16 | **无远程** |
| `Tools/ppt-master` | `main` | `54ef7c7` 2026-06-23 | 87d  🕸️? | 6 | origin✓ |
| `Tools/SlotForge` | — | 无 git | — | — | — |
| `Patents` | `master` | `8654521` 2026-09-06 | 12d | 122 | **无远程** |
| `Ohmybrain` | `main` | `efa0b24` 2026-09-16 | 2d | 3 | gitlab+19 / origin+19 |
| `ohmybrain-core` | `main` | `844ee8c` 2026-05-25 | 116d  🕸️? | 20 | gitlab✓ / origin✓ |
<!-- AUTO-GIT-SNAPSHOT:END -->

## 仓 / 项目状态总览

### TechReq / 水声通信算法仿真

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **UWAcomm** | 🟢 活跃开发 | 7 通信体制持续迭代（07-15 S2C 第 7 体制 Phase 1 全通，增益 2.16dB vs G_R 2.57 + OTFS 公共链接入）；07-13 逐模块校验战役（01-03 收口）+ ChannelDemo 演示外发包；07-21 Codex 版本三路审查（0 CRIT/HIGH）+ Jakes 基准逐 seed 复现后项目暂停（恢复待办 5 项）；08-03 `5df75c8` streaming P5 lifecycle race 修复 + evidence manifest 封存（memory 未回填）→ **main `b66c918`（08-23）：三体制服务工程化收官——DSSS/FH-MFSK/S2C 服务 L1-L4 + C1-C5 校验 + 收官文档，spec/plan 归档（用户终审通过），分支回 main，dirty=0**（origin 落后 23 待 push） | `D:\Claude\TechReq\UWAcomm` |
| **USBL** | 🟢 活跃开发 | 超短基线自定位；2026-04-25 H8 spec draft（等答 D1-D4，H7 未起）；**2026-05-25 main `accc52a`：D-OQ-1 链路预算 / D-OQ-2 多深度标定两跨项目回流专题（回流自 UWAcomm_usbl）+ README mermaid 三章节**（auto-memory 仅 project_usbl_h8_drafting，待回填） | `D:\Claude\TechReq\USBL` |
| **UWAnet** | 🟡 前期调研 | 水声组网协议 (Aqua-Sim-NG / ns-3)，尚无 session 锚点 | `D:\Claude\TechReq\UWAnet` |
| **UWAcomm_usbl** 🔒 | 🟢 活跃 | 整机原型样机 + 总集成（2026-04-25 派生）；calibration 分支 06-03/05/07 CAGE5 5 元阵东南大学水池实测 DOA 调试（CBF 优于 TDOA，方位泛化 1.2-1.9°，worktree HEAD `c8adb32`（06-08，GCC 加权变体 + GCC-TDOA vs CBF 分析/PHAT DOA；`c6d608e`/06-05 后 +2 commit 本地未 push，gitlab 仍 `c6d608e`）；**main `73cf223`：硬件功能接口图 v3 + SPEC-003 接口定义**（2026-06-01 收发三板架构后续；dashboard 原仅记 calibration 线） | `D:\Claude\TechReq\UWAcomm_usbl` |
| **SonarSim** 🔒 | 🕸️ 待回访 | 主动声呐界面仿真（显控台 + 探测链路，MATLAB App Designer，无依赖，手动模式，2026-06-03 派生）；SPEC-001 已实现跑通（单发同频干扰混响强度图，11 个 .m，T1-T4 单测过）+ 2026-06-04 绝对定标升级（接声呐方程）+ 18km 长程场景；已 commit+push 内网 gitlab lilin/SonarSim；**HEAD `2a0ebf3`（06-04）后 75 天无新 commit @2026-08-18 标 🕸️**（下游 SonarFOM 引用其参数口径仍活跃） | `D:\Claude\TechReq\SonarSim` |
| **USBL_hw** 🔒 | 🟢 活跃 | USBL 硬件设计（**engineering-hardware 子型首例**，2026-06-10 派生，手动模式，ADR-026）；**设计决策层基本全冻结**：收发链 TX+RX 全 first-pass（NeUB-816 实测闭环 TVR~146.8dB@12kHz→190dB 仅需~184W / 功放路线 a；2026-06-12 平台重构去 Zynq→分布式 ARM 控制板+采集 FPGA-A 数字直驱）+ SPEC 成熟度 001/002 first-pass·003 third-pass·004 confirmed·005 first-pass（005 因平台重构降级重开）；2026-06-15 S0 发射链仿真签核 + 方案完整性审查；**2026-06-16~23 方案设计说明书成稿化**（v1.0 终稿 `82ae586` 已 push + v1.1 通信章 §5.2 深扩写 / 公式 OMML 原生化 / 图重画）+ SPEC-006 收发半双工+值班 + SPEC-007 五板号统一 + 板2 timing 平台重构落盘 + 询证函 send-pack 全面同步 + §算法/§阵列校准并入；HEAD `eb7252a`（07-17，快照归档：阵型设计笔记+电源板方案笔记+简化说明书入库；前承 `e72aa09` 07-09 两源摄入（声为板卡方案+天大框图）+ 概览 PPT 增对标参考章），**已建内网 gitlab 远程**（lilin/USBL_hw），dirty=6；**2026-06-23 写权交接回 Codex**；剩余全属外部依赖（江苏水声 NeUB-816 大信号 + 供应商询证 + 耐压 FEA + 水池实测） | `D:\Claude\TechReq\USBL_hw` |
| **SonarFOM** 🔒 | 🟢 活跃 | 声呐效能 FOM 品质因数表计算（2026-07-21 派生，template-engineering，MATLAB，依赖 SonarSim 🔒，手动模式，ADR-036）；07-22-23 推进：水文五档分类 `classifyHydrology`（会聚区/表面声道/中等/强跃层/浅海，单测 7/7 + 真实 nc 对拍 9/9，commit `7bbfadd`）+ SPEC-002 BELLHOP TL(R) 传播链路（复用 raw AcousticModel，单点+批量五档跑通；诊断出会聚区需 ±40° 声线角度，±18° 默认漏 CZ 声线）+ **08-12 `9456931` 通信信道场计算与 AUV 通信指标声场支撑**（memory 未回填）；本地 main 无远程，dirty=0 | `D:\Claude\TechReq\SonarFOM` |
| **EnvDataClassify** 🔒 | 🔴 刚派生 | 环境数据分类（2026-07-23 派生，template-engineering，MATLAB/Python，依赖 SonarFOM 🔒，手动模式，ADR-037）；海洋环境数据（声速剖面/水文条件等）自动分类；脚手架就位（SOP §1 派生 + 占位符全清 + §6 验证全过 + git init `a7de7b2`），分类实现未启动，待 SPEC-001（分类对象/特征/方法）；本地 main 无远程 | `D:\Claude\TechReq\EnvDataClassify` |
| **AUVNetModem** 🔒 | 🔴 刚派生 | 面向五U 组网条件的水声通信机详细设计（2026-09-18 派生，template-engineering + 硬件目录扩展 = engineering-hardware 子型第二例，MATLAB，依赖 AUVNetCoop 🔒 / UWAcomm / AUVProposal 🔒，手动模式，ADR-050）；A 算法（体制 / 帧结构 / 链路预算 / 链路级仿真 / 物理层模型参数包）+ B 硬件（换能器 / 功放 / 接收前端 / 数字平台）；上游目标 3–9 kHz·10 km·≥300 bit/s 与 15–25 kHz·1 km·≥1 kbit/s、单次误包率 ≤10%；派生当日采集：既有资产全为 8–16 kHz 口径、两型 U 无硬件事实、平台发射 3～6 kHz 与五U 3–9 kHz 有出入；SPEC-001 框架 v0 待裁 D1~D10；本地 main `c37e2ce` 无远程 | `D:\Claude\TechReq\AUVNetModem` |

> 另：`projects/usbl-s1/` 是 USBL S1 仿真平台 **autonomous workflow dry-run（2026-04-22，Phase 0-4 全 PASS）的归档性质导航页**，非独立项目（USBL 权威入口仍是 `projects/usbl/`），故不单列状态行。

### DocProcess / 文档工作区（全私人）

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **Pricing** 🔒 | 🟢 活跃 | 军用软件四号文报价（jy-pricing skill 驱动） | `D:\Claude\DocProcess\Pricing` |
| **UWAprojDoc** 🔒 | 🕸️ 待回访 | 水声专项方案；2026-05-29 业务场景 C1-C6 全套（C5 区域预警 / C6 编队协同探潜 使命级新增 + 六详章 + ch04§4.1.4 覆盖矩阵 + 独立场景 docx）；已 commit（HEAD `eed5374`，05-29 尾注；本地未 push，dirty=2）；**05-29 后 81 天无新 commit @2026-08-18 标 🕸️**（v17 已交付，待回访确认收尾/暂停） | `D:\Claude\DocProcess\UWAprojDoc` |
| **CooperativeDetection** 🔒 | 🕸️ 待回访 | 4 专题 12 课题方案（2026-05-08 派生）；HEAD `6113b96`（05-09，101 天未动 @2026-08-18，dirty=0） | `D:\Claude\DocProcess\CooperativeDetection` |
| **PaperReview** 🔒 | 🕸️ 待回访 | 学位论文外审（中文）；2026-05-09 派生，HEAD `b3568f6`（101 天无新 commit @2026-08-18，工作树 dirty=7——可能在评中，待回访确认） | `D:\Claude\DocProcess\PaperReview` |
| **DigitalTwinGuide** 🔒 | 🕸️ 停滞 | 数字孪生实施指南方法论；2026-05-13 首版宋体 docx + 4 步 pandoc pipeline；**08-18 backup_push 首 commit 收口（`4d9746e`，45 文件全入库，dirty=0，gitlab 已 push）**；**业务自 05-13 后无推进（约 103 天 @2026-08-24，待回访）** | `D:\Claude\DocProcess\DigitalTwinGuide` |
| **DigitalTwin1plusN** 🔒 | 🗑️ 已退役 | 「1+N」水下集群数字孪生体系方案（2026-05-25 派生，同日 v0-v5 可研报告 docx 交付，12 commit 本地无远程）；**2026-08-18 用户确认删除工作区退役（ADR-041，体系首例）**——目录与本地 git 历史一并移除，活跃 30→29 / DocProcess×17→×16；本行保留为墓碑追溯 | ~~`D:\Claude\DocProcess\DigitalTwin1plusN`~~ |
| **VisioForge** 🔒 | 🟡 起步 | 通用 Visio 出图工作区（2026-06-02 派生，复用全局 flowgen-* 8 skill）；首批 6 张 SN 效能预报图 1:1 高保真复刻（自建 scripts/replica_lib2.py）；**08-18 backup_push 首 commit 收口（`07f40cd`，dirty=0，gitlab 已 push）** | `D:\Claude\DocProcess\VisioForge` |
| **CooperativeASW** 🔒 | 🕸️ 待回访 | UWAprojDoc「编队协同探潜配置仿真与效能评估分系统」单列细化独立 docx 方案（2026-06-03 派生，DEPENDS_ON=UWAprojDoc）；全文 17 章 223k 字 + 24 图全细化 + docx 969KB/100 页；2026-06-04 图件大改（I 族接口图 + build_docx A4 fit-to-box）；commit `f46b16d`+`5da5de1`（本地未 push）；**06-04 后 75 天无新 commit @2026-08-18 标 🕸️**（交付后待回访） | `D:\Claude\DocProcess\CooperativeASW` |
| **PaperTrans** 🔒 | 🕸️ 待回访 | 外文论文英译中翻译工作区（2026-06-15 派生，template-document SOP，手动模式）；一篇=一spec=一译稿，wiki 术语表+翻译规范两页种子；**首篇全书译稿收尾归档（23 单元草稿 + 367 页 PDF 待终审，HEAD `ed1a7ad`/06-16），本地 main 无远程**；**06-16 后 63 天无新 commit @2026-08-18 标 🕸️**（终审状态待回访） | `D:\Claude\DocProcess\PaperTrans` |
| **UWAcommTrial** 🔒 | 🟢 活跃 | UWAcomm 多模通信机通信距离性能湖上试验大纲（2026-06-24 派生，template-document，依赖 UWAcomm）；完善既有大纲（补目的 / 依据 / 对象 / 判据 / 组织 / 安全 / 数据归档）+ 13 张记录表逐表分页附件；**v1 已交付归档，SPEC-001 已 archive，源仓无 git** | `D:\Claude\DocProcess\UWAcommTrial` |
| **UWCombatPlatform** 🔒 | 🕸️ 待回访 | 水下作战试验平台建设方案 + 报价（2026-06-25 派生，template-document，全链路六环节：AUV论证仿真 / 硬件国产化 / 感知通信 / 水池半实物 / 智能对抗集群 / 应用验证；依赖 UWAcomm/SonarSim/USBL）；2026-06-26 六环节重构命名定稿（HEAD `3ce4928`，「作战世界模型」术语锁定）+ 6 平台技术路线 + 交接 Codex；**draft-v2 主稿仍 WIP**（仅②核心引擎样章成稿，勿读作"方案已成稿"）；**06-26 后 53 天无新 commit @2026-08-18 标 🕸️**（Codex 交接后停滞待回访）；🔒 本地无远程，涉密 docx gitignore | `D:\Claude\DocProcess\UWCombatPlatform` |
| **CommSimSupport** 🔒 | 🟡 脚手架 | 通信机仿真使用支持（项目/课题立项）申报书（2026-07-01 派生，template-document，依赖 UWAcomm）；SPEC-001 临时骨架就位（申报书通用结构，待官方模板放 `raw/` 并 `/ingest` 对齐必填项后起草）；**撰写未启动，git 未 init 无远程**（登记面 2026-07-09 追溯补齐，ADR-033）；**派生后 48 天撰写未启动 @2026-08-18**（阻塞在官方模板未投料，非遗忘） | `D:\Claude\DocProcess\CommSimSupport` |
| **OceanEnvSupport** 🔒 | 🟡 设计待决 | 海洋环境数据作战保障方案文档（2026-07-09 派生，template-document，依赖 UWAprojDoc/CooperativeDetection，ADR-034）；核心资产=月尺度高精度预报数据，规模 3000 万；**同日 F-1 架构设计落 wiki/topics**（五场景/六分系统/四阶段两期/经费双口径，设计 workflow 9 agent），🟡 等用户决断 D1-D5（D2 核心资产口径最关键）→ SPEC-001；撰写未启动；本地 main 无远程（HEAD `15833b0`，07-09 同日 +1 commit，pin 原记 `22f9aa0` 已刷新）；**40 天停等 D1-D5 @2026-08-18**（阻塞在用户决断，非遗忘） | `D:\Claude\DocProcess\OceanEnvSupport` |
| **ImgSonarTwin** 🔒 | 🟢 活跃 | 图像声呐数字孪生方案文档（2026-07-18 派生，template-document，依赖 DigitalTwinGuide/DigitalTwin1plusN（后者已退役 ADR-041），ADR-035）；**07-18 全文初稿（F-1/F-2 + 620 万报价）→ 07-19 成品化（5 图 + §3.5 + build_docx 管线 OLE 嵌入/自动编号 + 正式化 65 处）→ 07-20 Codex 复审 11 项处置收口（HEAD `5300532`，dirty=1）**；剩用户全文审 + xlsx 裁决；本地 main 无远程 | `D:\Claude\DocProcess\ImgSonarTwin` |
| **AUVProposal** 🔒 | 🟢 活跃 | AUV 项目立项论证（2026-07-24 派生，template-document，依赖 AUVSurvey，手动模式，ADR-038）；07-24 SPEC-001 confirmed + 初稿七章后持续重迭代：55 项审计收口（32 元舷侧阵全链重设计）→ 三专项论证成稿 → 四论证去附件化融入正文 → SPEC-021 主动探测处理链 MATLAB 信号级仿真套件 → 08-16 SPEC-022~025 主动探测三论证 + 0816 修订版方案成稿（`58c44b8`）→ 08-17 SPEC-026 汉江构型舱段重划（七舱段作废→六舱段 6.52m/Ø620，D1-D8 定案）→ **08-20~23 SPEC-027~031 连番落地（`15f3dba` 08-23）：壁 C/E 非水密+时统归平台+能源终裁 12 号图 0820 贯通版 / 0821-0822 走线图重出+附件重排四件+面阵 37 元全线同步 / SPEC-030 布置大挪移全链 / SPEC-031 物料清单核对版 / 0823 晚 W40 重号收口+术语统一+图族字号提档重嵌** → **08-24~28 续批（HEAD `b7d0921` 08-28，+4 commit）：SPEC-032/033 全生命周期文档管理规范（六阶段树 + 质量管理流程版）+ 表 1.1 291 项转录 + 34 份模板按指南目次重建 + 齐套目录落 `ProjectManagement/` / SPEC-034 换能器技术规格书 V0.2 + SPEC-035 整艇软件工作流程 V0.1 / 0827 批次舱段重排 + 能源口径同步（SPEC-036）全套出图 + 过程性文件归位规则 / SPEC-037 软件体系架构 + 软件流程 V0.4 + 平台板卡按方案乙回归 / SPEC-038 v4 架构图改基线口径入方案 + 能源章补全 + 图源 Visio 化**；dirty=4（0827 修订版方案 docx ×2 + 供电拓扑 vsdx + 0828 研制技术协议未提交）；旧待裁 ±1dB/阵型/多 ping 口径；gitlab 已配（08-18 backup_push） | `D:\Claude\DocProcess\AUVProposal` |
| **AUVSurvey** 🔒 | 🟢 活跃 | AUV 广泛调研（2026-07-24 派生，template-document，无依赖、下游 AUVProposal，手动模式，ADR-039）；07-24 SPEC-001 confirmed + 6 专题页；**07-25 SPEC-002 型制两轮深化（第 7 页 10 节）+ 15 PDF 入库（HEAD `6a79e02`，dirty=10）**；门槛项=型谱清单用户增删（32→15~25）→ 02-draft；本地 main 无远程 | `D:\Claude\DocProcess\AUVSurvey` |
| **CoupledMultiOrder** 🔒 | 🟢 活跃 | 多阶耦合智能艇群阶跃式协控汇报（2026-08-05 派生，template-document，无依赖，手动模式，ADR-040）；派生时方向待细化，后定为**智能艇群阶跃式协控**；主交付物=汇报 PPT 59 页（V5→V10 迭代，用户手改 V5→V6 后克制修订 + 通俗化 68 条）+ 解说词管线（58~59 页）+ 补充说明 docx；**08-07 git init `401b4b4`**（汇报稿工具链与 SPEC-001~004，成品与素材约 1 GB gitignore），dirty=0，无远程 | `D:\Claude\DocProcess\CoupledMultiOrder` |
| **DeepSeaIndustry** 🔒 | 🟡 待口径 | 深海技术产业促进申报书撰写（2026-08-30 派生，template-document，无依赖，手动模式，ADR-042）；申报口径（类别 / 主管部门 / 官方模板）待用户提供材料入 raw/ 后落 SPEC-001，沿用「主交付物待定先搭架子」先例；SOP §6 验证全过 + git init `97fa2c3`（2 commit，本地 main 无远程）；撰写未启动 |
| **XiaojingLaunch** 🔒 | 🟢 活跃 | 小鲸100 V3.0 发布会材料（2026-08-31 派生，template-document，无依赖，手动模式，ADR-043）；**派生当日 SPEC-001 首轮+二轮交付**：解说词微调版 docx（14+3 处改动，附录逐条可回退）+ PPT 框架版 17 页（16:9 深海蓝，15 素材占位框，备注 17/17 带解说词），raw 3 源料入库（解说词框架/研制任务书/公司总体介绍 PPT），HEAD `2ee3f7d`（2 commit，本地 main 无远程）；待素材替换占位 + 真实量化数据 + 用户 PowerPoint 视觉终检 | `D:\Claude\DocProcess\XiaojingLaunch` |
| **AUVSlopeMCM** 🔒 | 🟡 待口径 | AUV 坡上扫雷（2026-09-04 派生，template-document，无依赖，手动模式，ADR-045）；主交付物形态（方案 docx / 汇报 PPT / 双交付）、受众、任务口径（坡度范围 / 雷型 / AUV 平台 / 探测-识别-处置链路边界）待与用户讨论——议题落 wiki/topics → SPEC-001；SOP §6 验证全过 + git init `723d2fb`（1 commit，本地 main 无远程）；撰写未启动 | `D:\Claude\DocProcess\AUVSlopeMCM` |
| **UUVCommSwarmSim** 🔒 | 🟢 第 4 章终审中 | UUV 通信组网与集群控制一体化仿真软件（2026-09-13 派生，template-document，无依赖，手动模式，ADR-046）；主交付物形态（软件研制方案 docx / 申报书 / 需求规格说明书 / 汇报 PPT）、受众、口径（通信体制 × 组网协议 × 集群控制三域一体化边界、仿真粒度）待与用户讨论——议题落 wiki/topics → SPEC-001；UWAcomm / UWAnet / CoupledMultiOrder 可查询复用不构成依赖；SOP §6 验证全过 + git init `d06f8f4`（1 commit，本地 main 无远程）；撰写未启动 | `D:\Claude\DocProcess\UUVCommSwarmSim`；**09-14**：第 4 章成稿 `84fe9c9`（三层 8 模块 34 功能，9 图 Visio OLE + 16 表 32 页，参照 SoSCommSupport 丰富化，假设 B1~B5 待裁）待第七轮终审 |
| **SoSCommSupport** 🔒 | 🟡 待口径 | 体系通信保障（2026-09-13 派生，template-document，无依赖，手动模式，ADR-047；目录名代拟，用户可改）；主交付物形态（保障方案 docx / 论证报告 / 申报书 / 汇报 PPT）、受众、口径（「体系」边界——纳入的平台 / 节点 / 链路；保障层次——通信体制 × 组网协议 × 频谱资源 × 抗干扰 × 中继接力 × 环境适配 × 保障组织流程）待与用户讨论——议题落 wiki/topics → SPEC-001；UWAcomm / UWAnet / UWAprojDoc / CooperativeDetection / OceanEnvSupport / UUVCommSwarmSim 可查询复用不构成依赖；SOP §6 验证全过 + git init `d3831e3`（1 commit，本地 main 无远程）；撰写未启动 | `D:\Claude\DocProcess\SoSCommSupport` |
| **AUVNetCoop** 🔒 | 🟢 框架终裁 | 协同探测型 AUV 组网协同系统（2026-09-14 派生，template-document，依赖 AUVProposal，手动模式，ADR-048）；以 AUVProposal 1 t 级 / 2000 m 三艇协同探测型 AUV 为平台底座、硬件零改动，承接研制技术协议 §2.2「后续可扩展」5 项 + G8 U 间组网协议缺口：艇间水声组网协议栈（TDMA 超帧 / 寻址中继 / 6 类消息）+ 多艇协同定位（OWTT）与协同探测任务闭环 + 多艇协同验证环境；主交付物《协同探测型AUV组网协同系统研制技术协议》（6 章，复用 AUVProposal 构建管线）；SPEC-001 框架同日终裁 D1~D9 全按推荐（3+1 实装 / ≤8 协议 / ≥10 仿真 / 母艇网关 / 硬件零改动 / UUVCommSwarmSim 仅引用）；划界：不写仿真软件设计（UUVCommSwarmSim）/ 不做四化五层（SoSCommSupport）/ 避「多阶·阶跃·耦合度」（CoupledMultiOrder）；SOP §6 验证全过 + git init `5a6bbfc`（1 commit，本地 main 无远程）；下一步 PLAN-001 → raw 摄入 → 论证 1、2 | `D:\Claude\DocProcess\AUVNetCoop` |
| **ProductPortfolio** 🔒 | 🟢 收尾修订版待终审 | 公司产品体系梳理（2026-09-15 派生，template-document，依赖 XiaojingLaunch、参照 AcousticLiteracy，手动模式，ADR-049）；派生当日收窄为**海涛100 产品线**（体系 docx SPEC-001 挂起）；decision-001 海涛定位（主线 A / 海涛引擎 + 小鲸接口 / 删载荷支撑 / 训练参照 sxsy / 定位「一套引擎 · 三级仿真 · 两条闭环」+ 价值「效果先算清 · 方案再选定 · 训练有数据」）+ decision-002 小鲸两级口径；**09-16 完整版**：Codex 16 页（.mjs）与 Claude 20 页（v15.3 原模板 + 原生架构图）并存 → Codex 审阅清单 A~D + 第二轮 R1~R6 由 Claude 实施 → `output/海涛100_产品发布会_完整版_claude_收尾修订版.pptx` 待用户终审（P11 通信原理验证案例 + V3 P14 原图 / P9 原生表格 / P13 二期设计示意 / P7·P17 闭环返回线 / P15 准快全通评 / P19 删未确认联系人）；待用户给联系人 / 二期截图 / 封面措辞；HEAD `a4696f9`（12 commit，本地 main 无远程） | `D:\Claude\DocProcess\ProductPortfolio` |
| **AcousticLiteracy** 🔒 | 🟡 待讨论 | 声学素养提升项目（2026-08-31 派生，template-document，无依赖，手动模式，ADR-044）；主交付物形态（教材/讲义/课程 PPT/系列文档）、受众、范围待与用户讨论——议题落 wiki/topics → SPEC-001；SOP §6 验证全过 + git init `88a7379`（1 commit，本地 main 无远程）；撰写未启动 | `D:\Claude\DocProcess\AcousticLiteracy` |

### Tools / 跨项目工具

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **FlowGen** | 🟢 活跃 | 需求→Visio/Mermaid 出图工具族；2026-06-01 阶段1 系统架构图（commit `5372721` 已 push gitlab）+ 2026-06-02 阶段2-A 逻辑架构图 + 2026-06-04 archmap business/data-functional/interface(I 族)/stdflow 多 renderer + 新 archmap skill + 2026-06-15 M5-pro 专业正交路由流程图 + 逐 skill 详解 PPT（HEAD `385072e`，gitlab/main） | `D:\Claude\Tools\FlowGen` |
| **AnthropicPPT** | 🟢 活跃 | FIELDBOOK PPT 模板（2026-05-23 派生，design_tokens + 8 helpers + 9 layout + skill `anthropic-ppt`）；2026-06-15 新增 `styled_diagram`（Calibration Field 消费者②，native pptx 风格层 + 4 图种，HEAD `438c57e`/gitlab）；**2026-06-24 降级（Plan A/ADR-030）**：PPT 生成迁 ppt-master + `fieldbook` 模板，本项目降为 FIELDBOOK 设计源 + 归档（modify_v4→legacy，skill 改路由） | `D:\Claude\Tools\AnthropicPPT` |
| **IconForge** | 🟡 未实装 | 自然语言→图标 SVG 生成工具（2026-05-29 派生后暂停，HEAD `a6b361a` 66 文件未实装；已评估 samzong/ai-icon-generator，恢复后下一步 M1 spec） | `D:\Claude\Tools\IconForge` |
| **FieldKit** | 🟢 活跃 | 「校准场 / Calibration Field」图示风格系统（2026-06-15 派生，template-tool SOP 脚手架，借鉴 pbakaus/impeccable）；共享 design kit（tokens + kit.css + sonar motif + 氛围层 baker）→ 消费者①HTML→PNG/PDF 生成器（flow + composition，暗 Lacquer Instrument + 亮 Paper Field 双调色板）SHIPPED v1 + 消费者②AnthropicPPT styled_diagram 布局族 SHIPPED v2；HEAD `5a9d75b`（06-15，扩 3 图种 layered/cover/sequence + 字体系统），已建内网 gitlab 远程（lilin/FieldKit，已 push）；skill `calibration-field` 已注册 | `D:\Claude\Tools\FieldKit` |

> 🔌 **第三方 vendored（不计入活跃项目数）**：`ppt-master`（`Tools/ppt-master`，hugohe3/ppt-master 30.8k★ MIT）= 通用 PPT deck 引擎（agent 手写 SVG → 原生 DrawingML）；**FIELDBOOK 已迁为其 `fieldbook` brand + deck 模板**（Plan A / ADR-030，2026-06-24）。跑其脚本需用户授权。

### 专利工作区（私人）

| 项目 | 状态 | 当前焦点（最近 session / 锚点） | 路径 |
|------|------|---------|------|
| **Patents** 🔒 | 🟡 候选 | 私密专利交底书工作区（**本地 git**，2026-06-29 init `53bd96d`，仅本地无远程）；6 候选交底书：iusbl-jacobian / otfs-spread-pilot / usbl-cage5-3d-hybrid-doa / turbo-vamp-warmstart / wideband-digital-direct-drive / no-oracle-multimode-blind-rx；**06-29 后 50 天无新 commit 且 dirty=93 @2026-08-18**（大量工作树改动未入库，待回访 commit 裁定） | `D:\Claude\Patents` |

### 母仓 / Hub

| 仓 | 状态 | 最近动态 | 路径 |
|---|------|------|------|
| **Ohmybrain** (本仓 = Hub) | 🟢 活跃 | 持续入会自检维护（自检四~十六，2026-06-10~08-24，每轮 dimension 对账 + CANON 级联 + 反模式收口）；**HEAD `4de5ee8`（08-24 审计十六补记）**，本轮入会审计（十七，2026-08-29，距上轮 5 天，用户显式要求）：**CANON 级联收口 14 处**（memory 97→99 / feedback 28→30 / skills 32→33——「审计后窗口」反模式**第 5 次复发**：08-26 session 2 条新 feedback memory 漏级联 + 本 session 新装 skill archify）+ memory-index 2 指针补登 + dimension-C 漂移收口 2（AUVProposal `15f3dba`→`b7d0921` 08-28 / Hub 自身行自指滞后）+ AUTO 快照 `--gen` 重打 @08-29 + **新 skill `archify` 登记**（同域冲突 `architecture-diagram` 待裁）；**两 remote（gitlab/github）均停 `3908359`（06-29），本地领先 8 commit + 本轮批次待 push 授权**；架构史锚：2026-06-09 协作协议层（`7b7fa9d`，**ADR-024**） | `D:\Claude\Ohmybrain` |
| **ohmybrain-core** (母仓) | 🟢 活跃 | 三模板就位；候选下沉队列见 [[core-update-queue]] | `D:\Claude\ohmybrain-core` |

## Hub 内部规模快照（2026-06-29）

> 由 `scripts/dashboard_snapshot.py` 统计生成（wiki 子目录页数 / scripts / 本地 skills / agents / rules / memory）。skill 一栏区分**本地两层**：磁盘 SKILL.md 与叠加 plugin/marketplace 注入后的可见总数。

| 指标 | 数值 | 说明 |
|------|------|------|
| wiki 内容页 | **113** | 20 concepts + 8 entities + 12 architecture + 1 agents + 1 workflows + 5 topics + 4 explorations + 37 source-summaries + 25 mcp-entities + 0 comparisons |
| wiki 总文件 | **115** | 113 内容页 + 根 `index.md` + `log.md` |
| 自动化脚本 | **28** | `scripts/*.py` 全量（2026-08-30 +log_wiki_read / wiki_usage / retire_memory；含 dashboard_snapshot.py `--gen`；2026-08-18 +backup_push.py 双轨备份） |
| Hooks | **9 + 2** | Hub 9（3 阻断 + 4 提醒 + 1 注入 + 1 记录，见下表）+ 工作区级 2（见表下注） |
| 全局 skill（本地） | **32** | `~/.claude/skills/` 含 SKILL.md 的目录（34 个目录中 32 个有 SKILL.md） |
| 全局 skill（注入后可见） | **90+** | 本地 32 叠加 `ecc:*` plugin / marketplace 注入后；裸写 90+ 会掩盖本地真实规模，故两层并列 |
| 全局 agent | **55** | `~/.claude/agents/*.md` |
| rules 目录 | **15** | common / zh / web + 12 语言（cpp/csharp/dart/golang/java/kotlin/perl/php/python/rust/swift/typescript） |
| Memory 条目 | **115** | 4 类：user 1 / feedback 37 / project 74 / reference 3（见 [[memory-index]]；最新含 DeepSeaIndustry / XiaojingLaunch / AcousticLiteracy / AUVSlopeMCM / UUVCommSwarmSim / SoSCommSupport / AUVNetCoop / ProductPortfolio / AUVNetModem init + PPT autofit / pptx COM 导图 / endParaRPr 次序 / open-newline 截断 / docx 配图素样式 feedback 条目） |
| MCP servers | **6** | context7 / exa / github / memory / playwright / sequential-thinking |

> ADR 不是独立文件，集中存放在 [[decision-log]]（章节形式 ADR-001~035）。

## Hub Hooks 当前状态

| Hook | 脚本 | 类型 | 触发 |
|------|------|------|------|
| 🔴 阻断 | `check_raw_write.py` | PreToolUse Edit/Write | raw/ 写入拦截 |
| 🔴 阻断 | `check_private_tags.py` | PreToolUse Edit/Write | `<private>` 标签拦截 |
| 🔴 阻断 | `check_index_log_sync.py` | Stop | wiki 改动但 index/log 未同步 |
| 🟡 提醒 | `post_wiki_write.py` | PostToolUse | 写入 wiki 后自动 lint |
| 🟡 提醒 | `raw_ingest_reminder.py` | PostToolUse Bash | Bash 触及 raw/ 提醒 |
| ⚪ 记录 | `log_wiki_read.py` | PostToolUse Read/Bash | wiki 页读取事件 → `.usage/wiki_reads.jsonl`（I4 读取即投票，2026-08-30） |
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
- [[memory-index]] — auto-memory 97 条目索引（本页 session 锚点来源）
- [[core-update-queue]] — Hub → core 下沉候选队列
- [[decision-log]] — ADR-001~034 决策记录
