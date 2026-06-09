---
type: architecture
created: 2026-05-24
updated: 2026-06-09
tags: [ADR, 决策, log]
---

# 决策记录 (ADR-style)

跨仓重大架构决策的累积记录。**比 git log 更高粒度**（合并多次 commit），**比 memory 更结构化**（含动机 / 选项 / 后果）。

最新在上。

> **起点声明**：**2026-04-12 为 Ohmybrain 体系起点（ADR-001），此前无历史 ADR**。本页对每个 [[roadmap]] 里程碑追溯一条 ADR，编号 ADR-001 ~ ADR-023 连续。早于体系初版的工作（各 project 仓库自身的历史）不在本累积记录范围内。

---

## ADR-023 · 2026-06-03 · CooperativeASW 项目派生

### 触发

UWAprojDoc「编队协同探潜配置仿真与效能评估分系统」（父方案第 9 章）需扩写成可独立交付的分系统 docx 方案，做更深细化；素材（5 功能模块 docx + 编队素材）已就位。

### 决策

派生 `D:\Claude\DocProcess\CooperativeASW`（私人，从 template-document 派生，**DEPENDS_ON=UWAprojDoc**）——把父方案一个分系统单列成 standalone 子方案。硬约束：成文 standalone（禁提与总系统/父方案关系），主线 = 战术「执行→优化→选择」贯穿全篇，图走 flowgen-* skill。

### 实现

- 全文 17 章 ≈ 223k 字 + 24 图全细化 + 24 图注；docx 969 KB / 100 页（合稿器 `build_docx.py` A4 fit-to-box）
- 2026-06-04 图件大改：图 4-1/1-2 改 I 族接口图（**催生 `archmap_interface.py` skill**）+ 24 图 workflow 并行细化 + 5 组成图紧凑化
- commit `f46b16d`（文字稿）+ `5da5de1`（0604 图件大改 / 行为决策树），本地未 push

### 后果

- ✓ 首例「父方案分系统单列成 standalone 子方案」+ DEPENDS_ON 依赖链建立
- ✓ I 族接口图 archmap_interface skill 借此孵化（回流全局 flowgen-archposter）
- ⚠ 图 + docx push 待内网私有库；mod6/7 细化与若干指标来源待补

> memory `project_cooperativeasw_init`。

---

## ADR-022 · 2026-06-03 · SonarSim 项目派生

### 触发

主动声呐界面仿真（显控台 + 探测链路）需独立工作区，验证 App Designer model/view 解耦范式（沿用 UWAcomm 14_Streaming 先例）。

### 决策

派生 `D:\Claude\TechReq\SonarSim`（私人，从 template-engineering 派生），MATLAB App Designer，无依赖，手动模式；用户授权自主代跑（类 claude 分支），但保留"不代下结论"边界。

### 实现

- 3 wiki 种子页（声呐方程双体制 / model-view-pipeline / 参考综述，项目本地非 Hub）
- SPEC-001 已实现跑通：单发同频干扰混响强度图，11 个 `.m`（waveform_gen / beamform_fan / matched_filter / build_cube / render_reverb_map …），T1-T4 单测过
- 2026-06-04 绝对定标升级（接声呐方程，物理量 dB）+ 18km 长程场景归档（SPEC-001 闭环）
- 已 commit + push 内网 gitlab `lilin/SonarSim`

### 后果

- ✓ template-engineering 模板派生验证（区别于 DocProcess 系 template-document）
- ✓ SPEC-001 仿真目标 SNR 复现声呐方程（±0.1 dB），"假"消除
- ⚠ 后续 GUI 化 / CFAR / PPI / MVDR 抑旁瓣线待续

> memory `project_sonarsim_init`。

---

## ADR-021 · 2026-06-02 · VisioForge 项目派生

### 触发

各项目按需产 `.vsdx` 出图缺一个通用工作区；flowgen-* 8 skill 已成熟但 replica 复刻图能力（容器 / 正交连线 / 圆柱）不足。

### 决策

派生 `D:\Claude\DocProcess\VisioForge`（私人，从 template-document 派生，DEPENDS_ON 无）作通用 Visio 出图工作区，复用全局 flowgen-* 8 skill；高保真复刻走项目本地增强渲染器（不改全局 skill）。

### 实现

- 自建 `scripts/replica_lib2.py`：容器框 + Visio 动态直角连接器（`GlueTo(PinX)` 自动正交）+ 真圆柱 4 段 z-order 组合 + `page.Export` PNG 自检
- 首批 6 张 SN 效能预报图 1:1 高保真复刻（各图 `scripts/hf_<slug>.py` 手建 SPEC）
- git init -b main，首 commit 未提交（待授权）

### 后果

- ✓ 「flowgen-replica 不足时走项目本地增强渲染器」范式确立
- ⚠ 首 commit 待授权未提交；MVP 脚本保留对照

> memory `project_visioforge_init`。

---

## ADR-020 · 2026-05-29 · IconForge 项目派生

### 触发

PPT / 方案文档高频需要图标；自然语言→矢量图标（SVG）的 LLM 直出能力缺口。同构 `flowgen-vsdx` skill 的"LLM 即生成器"范式可复用到图标域。

### 决策

派生 `D:\Claude\Tools\IconForge`（私人，tool 类，从 `ohmybrain-core/template-tool/` 派生）。评估 `samzong/ai-icon-generator` 后判定其位图 SaaS 路线不作骨架（可借风格 / ICNS / prompt），LLM 直出矢量自研。派生后即**暂停**，恢复时下一步 M1 spec。

### 实现

- HEAD=a6b361a，66 文件未实装（手动模式）
- 同步：dashboard Tools 段 + memory-index Tools 系 + roadmap 里程碑 + Hub / 根 `CLAUDE.md` 项目映射
- 同日（2026-05-29）并行：入会自检 B 阶段 8 dedicated 页实质填充 + 本页 ADR 重排为连续编号（见 [[roadmap]] 2026-05-29 行）

### 后果

- ✓ Tools 系第 3 个工具项目（继 FlowGen 2026-04-23 / AnthropicPPT 2026-05-23 之后）
- ✓ template-tool 模板第二次派生验证
- ⚠ 派生后暂停，未实装；恢复节奏待定

---

## ADR-019 · 2026-05-25 · DigitalTwin1plusN 项目派生

### 触发

「1+N」水下集群数字孪生体系（1 艘百吨级大 U + 24 艘小 U）需独立工作区，且 DigitalTwinGuide 已沉淀方法论可作上游参考。

### 决策

派生 `D:\Claude\DocProcess\DigitalTwin1plusN`（私人项目），**首例采用 template-document 模板**派生；先做概念决议再落 spec，不直接起草正文。

### 实现

- ingest + **P1-P11 概念决议**（P11 暂缓）+ 3 份 spec
- 体系定义：1 大 U（LDUUV 母舰 + 5 职能）+ 8 察打 I（明哨/主动）+ 16 察打 II（暗哨/被动）+ 8 小集群
- 核心战术 **"I 看 II 打" 三段切换**；9 类智能体 × 三层
- 24 个月 4 级试验 + 试验主导 + 缩减海试；自研全栈 + IP 聚焦集群战术
- HEAD=234eb11（7 commit）

### 后果

- ✓ template-document 模板首次实战验证
- ✓ 概念层（P1-P11）先收敛，降低后续正文返工
- ⚠ P11 暂缓项与后续章节耦合度待观察

---

## ADR-018 · 2026-05-24 · Hub 大脑哲学澄清

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

> 注：本条与 ADR-006/ADR-007（旧编号下的同期事件）为同一批 2026-05-24 工作，本次重排后哲学澄清归此条。

---

## ADR-017 · 2026-05-23 · AnthropicPPT 项目派生

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

## ADR-016 · 2026-05-16 · rx_stream_p4 接口移植 + 双回归 RCA

### 触发

UWAcomm-claude worktree 完成 rx_stream_p4 接口移植后，需验证移植未破坏既有体制；多路回归暴露 algo A FAIL 与 fd=1Hz 50% 回归。

### 决策

不立即追改，先把回归结果分类为「接口移植本身」与「上游 algo bug」两类，分别挂 RCA TODO；对 simple UI 侧 algo A FAIL 用加 dither 临时绕过，保留算法层根因待查。

### 实现

- claude worktree 4 commit（d74c0a2 + 3d6d0b5 rx_stream_p4 接口移植）**未 push**
- 落 spec `2026-05-16-rx-stream-p4-interface-restoration.md`
- 回归结果：test 1+2 algo A FAIL（V4.1 + 零噪 + LS fallback trigger 失效三方耦合）/ test 4 ✓ 24/24 + 1 改善 / test 5 fd=1Hz 50% 回归（vs a291af4 baseline 3.37%，14× 退化，algo B 待 RCA）

### 后果

- ✓ 接口移植与算法 bug 分离，避免误把回归归咎于移植
- ⚠ fd=1Hz 50% 回归 = ADR-007（SC-FDE Phase 4+5 突破，旧编号 ADR-005）的 14× 改善被部分抵消，algo B RCA 待观察
- ⚠ algo A 三方耦合根因待观察

---

## ADR-015 · 2026-05-13 · DigitalTwinGuide 项目派生

### 触发

数字孪生项目实施指南（方法论文档）需独立工作区，首份种子为 20 吨级 AUV 课题指南。

### 决策

派生 `D:\Claude\DocProcess\DigitalTwinGuide`（私人项目），沉淀一套可复用的 4 步 pandoc pipeline 作为方法论文档的固定产线。

### 实现

- 首版数字孪生宋体版 docx 完成（基于 AUV 课题指南种子 + 多智能体样板 reference，含五~八章 + 经费表）
- 4 步 pandoc pipeline（normalize / pandoc / three_line / clean_indent）固化在 .tmp/
- 63 init + docx 仍 stage 未 commit

### 后果

- ✓ pandoc 4 步产线可复用于后续方法论文档
- ⚠ docx 与 init 提交挂起，commit 状态待观察

---

## ADR-014 · 2026-05-12 · claude+codex worktree 175 文件吸收

### 触发

UWAcomm 双轨开发（claude / codex worktree）出现分叉；codex 侧有 175 个 claude 缺失的独有文件，需收敛但不能破坏 claude 既有逻辑。

### 决策

claude worktree **吸收 codex 独有 175 文件**，关键算法（modem_decode_scfde V4.1 + LS fallback）走**手动合并**而非整体覆盖；对冲突项逐项做 C 级决策（保留较优实现）。

### 实现

- modem_decode_scfde V4.1 + LS fallback 手动合并（51 行净增 / `info.channel_estimator` 新字段 / claude 高 SNR clamp 与 codex GAMP-bad fallback 正交共存）
- spec 状态分裂修正（archive 追加 codex 2026-04-26 A2 段 + 删 2 active 副本）
- C 级决策：rx_stream_p4 保留 claude 350 行（弃 codex 731 superset）/ simple UI 双轨保留 / spec 取 claude archive
- HEAD=1128350 本地超前 origin 2 commit **未 push**，master 1e545de 不动

### 后果

- ✓ 双轨收敛为单一可用基线，正交逻辑共存不互斥
- ⚠ 4 项回归测试挂高优先 TODO 未跑（直接催生 ADR-016 的回归验证）
- ⚠ 本地超前 origin 未 push，同步状态待观察

---

## ADR-013 · 2026-05-09 · PaperReview 项目派生

### 触发

学位论文外审（中文论文中文评审意见）需独立工作区，与算法/方案项目隔离。

### 决策

派生 `D:\Claude\DocProcess\PaperReview`（私人子项目，手动模式），专做外审；项目名中"英文"指 PaperReview 本身，非材料语言（材料均为中文）。

### 实现

- HEAD b3568f6，手动模式
- 当前在评水声专硕一份

### 后果

- ✓ 外审工作与其它项目彻底隔离
- 后续多份外审复用同一工作区（待观察）

---

## ADR-012 · 2026-05-08 · CooperativeDetection 项目派生

### 触发

水下分布式协同探测方案（4 专题 12 课题）需独立工作区。

### 决策

派生 `D:\Claude\DocProcess\CooperativeDetection`（私人项目），承载 4 专题 12 课题方案文档。

### 实现

- 2026-05-08 从 DocProcess 派生
- 4 专题 12 课题方案 + emf 矢量图（per roadmap P1）

### 后果

- ✓ 协同探测方案独立成仓
- ⚠ 方案文档 + emf 矢量图工作量待观察（roadmap P1 列为待办）

---

## ADR-011 · 2026-05-06 · OTFS 4-27 漏登补登 + Phase 4 BER FAIL 归档

### 触发

OTFS 在 2026-04-27 的移植工作（rx_otfs / PAPR / 扩散 pilot）漏登；同时 Phase 4 hann 窗实验全部退化，需要给出"维持现状"的明确归档结论而非继续试。

### 决策

- 补登 OTFS 4-27 工作到 memory/log
- Phase 4 BER FAIL **归档为负结果**：hann × 6 trial 全退化，**维持 rect 默认**，不再继续 hann 路线

### 实现

- OTFS 4-27 漏登补登（rx_otfs / PAPR / 扩散 pilot）
- Phase 4 BER FAIL 归档（hann × 6 trial 全退化 +1.9~+14.8 pp，loopback 2.78e+01 vs rect 1.26e-15）
- 2 commit（e7f376c + 88fb31b）已 push origin + gitlab

### 后果

- ✓ 负结果显式归档，避免重复试 hann
- ✓ rect 作为默认窗确定
- ⚠ OTFS jakes 5Hz 33% limitation 仍待后续 RCA（待观察）

---

## ADR-010 · 2026-05-04 · SC-FDE V4.1 高 SNR 修复（117× 改善）

### 触发

SC-FDE 在高 SNR（pass / SNR=80）出现 ~50% 灾难率，与"高 SNR 应更好"直觉相悖。

### 决策

定位为高 SNR 下均衡器噪声方差估计与 pre-turbo 触发的耦合问题，采用 `nv_eq` clamp + SNR>25dB 时 disable `trigger_pretturbo` 的双重修复。

### 实现

- SC-FDE V4.1 高 SNR 修复（pass 50.23% → **0.43%**（117×）/ SNR=80 48.71% → 0.53%（94×）；nv_eq clamp + trigger_pretturbo SNR>25dB disable）
- 同期：simple UI v2.0（tx/rx_simple_ui classdef + 4 模式 + 流式 chunk）+ jakes V2.0 passband-native（Hilbert + SoS）+ OTFS K×2 fix
- 24/24 矩阵全 PASS + 详细测试报告
- HEAD 7cd0ed7 已 push origin + gitlab

### 后果

- ✓ 高 SNR 灾难率消除（117× / 94×）
- ✓ 24/24 矩阵全 PASS
- ⚠ pre-turbo 在高 SNR 被 disable 是 trade-off，对低 SNR turbo 增益无影响但耦合根因仍待长期观察

---

## ADR-009 · 2026-05-01 · P4 UI 稳定性 + V3.0 解耦

### 触发

P4 UI 链路 BER 异常（51%）；blk_cp 与 blk_fft 强耦合导致参数难独立调整。

### 决策

- 4 处 fix 修复 P4 UI BER（51% → 0%）
- V3.0 **解耦 blk_cp / blk_fft**，并引入 V4.0 预设降低配置复杂度

### 实现

- 4 fix（51% → 0%）
- V3.0 解耦 blk_cp / blk_fft
- V4.0 预设（K=31 直接链路 0.68%）
- HEAD 86328ba

### 后果

- ✓ P4 UI BER 异常修复
- ✓ blk_cp / blk_fft 可独立配置
- ⚠ UI 实测仍出现 50%，列为 follow-up（→ 2026-05-03 H5 jakes 假 α RCA 命中，待观察延续）

---

## ADR-008 · 2026-04-28 · UWAprojDoc 项目派生

### 触发

水声专项方案技术文档撰写需独立工作区；同期 P4 UI 需与 codex worktree 对齐。

### 决策

派生 `D:\Claude\DocProcess\UWAprojDoc`（私人项目），承载技术文档；P4 UI 侧采用"先 diff codex 再改"的对齐策略。

### 实现

- UWAprojDoc 派生 + 完整 v0 docx 落地（4.8 MB，8 分系统 33 模块独立小节，60 张图含 33 模块流程图 5 模式竖向）；HEAD=48f4324
- UWAcomm 侧：V2.0 透传 + Jakes 接通（gen_uwa_channel）+ RX α 符号 V6→V7 + α refinement 移植；4 modified + 6 untracked 未 commit；HEAD 28a4bc6 未变

### 后果

- ✓ 技术文档独立成仓，v0 docx 完整落地
- ⚠ UWAcomm 侧改动未 commit、待用户实测 BER（待观察）

---

## ADR-007 · 2026-04-26 · SC-FDE Phase 4+5 协议层突破

### 触发

SC-FDE jakes fd=1Hz 50% 灾难率长期未解。

### 决策

把 pilot 长度从 64 提升到 128（= blk_cp），突破协议层 limitation。

### 实现

UWAcomm `modem_decode_scfde.m` V4.1+LS fallback，HEAD=47770b0。

### 后果

- ✓ fd=1Hz 47% → 3.37%（14× 改善）
- ⚠ 但 2026-05-16 回归测试 fd=1Hz 50% 再次出现，algo B 待 RCA（见 ADR-016）

---

## ADR-006 · 2026-04-25 · UWAcomm_usbl 项目派生

### 触发

UWAcomm + USBL 联合仿真（整机原型样机 / 总集成枢纽）需独立工作区，且属内网 Internal。

### 决策

派生 `D:\Claude\TechReq\UWAcomm_usbl`（内网 Internal，混合模式），从 ohmybrain-core SOP 派生；同期 UWAcomm 主线推进 HFM-signature calibration。

### 实现

- TechReq/UWAcomm_usbl 完成 SOP 派生（混合模式，未实装）
- UWAcomm 侧：V5.5 fd=1Hz iter 反向收敛 R5 + V5.6 HFM-signature calibration 4/5 PASS（SNR=20 接近 oracle 0.92% / 6.7%）；spec 保留 active；HEAD c2dede1

### 后果

- ✓ 联合仿真项目独立成仓
- ⚠ 项目未实装；UWAcomm_usbl 后续范围多次演进（3 件事并行 / 硬件路径事实修订），方向待观察

---

## ADR-005 · 2026-04-23 · 单根因审计法形成

### 触发

DSSS V1.2 audit：43% BER 灾难率，"plan C 时变性"是假根因。

### 决策

D9/D10 toggle + 跨 4 runner audit 形成单一根因定位法。

### 实现

写入 memory `feedback_single_root_cause_audit`，限 MATLAB 算法 RCA 不外推。同期 Tools/FlowGen 完成 SOP 派生（Mermaid 流程图生成工具，未实装）。

### 后果

- ✓ 0% 灾难率（单一函数 fix 解决）
- ✓ 跨多次 RCA 复用（SC-TDE V5.4 / SC-FDE V4.1）

---

## ADR-004 · 2026-04-21 · autonomous-new-project-workflow 落地

### 触发

新项目派生缺乏统一 SOP，每次手工搭骨架易遗漏 wiki/raw/scripts/workflows 结构。

### 决策

把"新项目派生"固化为 autonomous workflow，配合 ohmybrain-core/template/ 母仓实现一键派生。

### 实现

- 落地 [[autonomous-new-project-workflow]]（wiki/explorations/）
- dry-run 产物归档（usbl-redo P2 / uwanet-redo P1，per Archive/worktrees-redo）

### 后果

- ✓ 后续 UWAcomm_usbl / UWAprojDoc / CooperativeDetection / PaperReview / DigitalTwinGuide / DigitalTwin1plusN 均沿此 SOP 派生
- ⚠ dry-run 阶段产物为实验性，正式派生流程在后续项目中逐步收敛

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
- 后续 → ADR-018 哲学澄清

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

> **体系起点**：本条为 Ohmybrain 体系的起点，**此前无历史 ADR**。

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
（积极 ✓ 和潜在 ⚠ 两面；不确定的写"待观察"）
```

## 相关页面

- [[hub-as-brain]] — 大脑功能定位
- [[three-tier-architecture]] — 三仓哲学
- [[roadmap]] — 决策 → 未来 roadmap
