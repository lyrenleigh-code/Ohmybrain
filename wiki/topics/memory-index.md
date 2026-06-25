---
type: topic
created: 2026-05-24
updated: 2026-06-24
last-sync: 2026-06-24
tags: [memory, 索引, auto-memory]
---

# Memory 条目索引

`~/.claude/projects/D--Claude/memory/` 下 auto-memory 条目按类型 + 主题分类的索引。**事实源在 `MEMORY.md`**（每行一条目），本页是 Hub wiki 中的 mirror 视图，按类型聚合。

> 不复制 memory 完整内容（避免双写），本页只索引 + 简短描述 + link 到 memory 文件。

> **计数口径（@2026-06-25）**：auto-memory 共 **86 个**条目文件（外加 `MEMORY.md` 索引本身 = 目录 87 个 `.md`）。分布：user **1** / feedback **21** / project **61** / reference **3**。下方各类型标题计数与此严格一致。
>
> 注：`MEMORY.md` 索引行中「flowgen-vsdx M5 升级」一条指向 `~/.claude/skills/flowgen-vsdx/SKILL.md`（skill 文件，**非 memory 条目**），不计入总数。

## 按类型分类

### user（用户画像 · 1 条）

- [user_profile](../../../../../zazn/.claude/projects/D--Claude/memory/user_profile.md) — UWA 研究者 / MATLAB 主力 / Windows+bash / 中文 / 专家主导 / 并行优先

### feedback（行为指导 · 21 条）

按主题分组：

**Git / 安全（2）**
- `feedback_git_confirmation` — commit/push/delete/force 必须明确授权
- `feedback_pat_after_exposure` — PAT 暴露后用一次即停

**UWAcomm 算法工作流（7）**
- `feedback_uwacomm_testing_boundary` — 不代跑单元测试 / 不代下结论 / 每 checkpoint 停
- `feedback_uwacomm_path` — `D:\Claude\TechReq\UWAcomm` 不是 `D:\TechReq`
- `feedback_uwacomm_worktree_ownership` — main/codex/claude 三路边界
- `feedback_uwacomm_claude_branch_autonomous` — claude 分支允许代跑 + 代决策
- `feedback_uwacomm_codex_compare_method` — codex worktree 对比方法（V7+ 头注约定）
- `feedback_uwacomm_ui_ber_diagnose_order` — UI BER 异常先验直接链路
- `feedback_uwacomm_skip_otfs` → OTFS 重启（撤销 2026-04-21 skip）

**UWAcomm_usbl worktree（1）**
- `feedback_uwacomm_usbl_worktree_ownership` — 双 worktree main/design

**算法 RCA / MATLAB 出图（4）**
- `feedback_single_root_cause_audit` — D9/D10 toggle + 跨 runner audit（限 MATLAB 算法 RCA）
- `feedback_matlab_inf_bug` — MATLAB inf 字面量触发 struct 转换错误，用 0 替代
- `feedback_comp_resample_carrier_phase` — passband 时间伸缩等效反载波相位 / baseband 需手动补
- `feedback_matlab_interactive_figs` — 出图用 `matlab -r` 桌面会话弹交互窗（非 -batch 存 PNG）；绘图写成 poolData/ 可复用函数（view_td/view_analysis）（2026-06-05 新增）

**Claude Code Harness（2）**
- `feedback_project_local_agent_not_invocable` — 项目 .claude/agents/*.md 不在 subagent_type 列表
- `feedback_subagent_write_permission` — 后台 subagent Write/Bash 常被拒，主会话代写

**Ohmybrain / 文档工作流（5）**
- `feedback_ohmybrain_workflow` — 硬工序 `specs→plans→discussion→code`
- `feedback_ohmybrain_self_improvement` — 进入 Ohmybrain 项目第一件事 = 完善自己（2026-05-24 新增）
- `feedback_sync_to_core_lessons` — /sync-to-core 首次实战：queue 须先 diff 再决定（2026-05-24 新增）
- `feedback_doc_visual_diversification` — 流程图不能统一布局换数据
- `feedback_doc_flowgen_only` — 方案 / 方法论文档图必走 flowgen-* skill

### project（项目状态 · 61 条）

按项目分组：

**UWAcomm（18）**
- `project_uwacomm` — 6-scheme UWA sim 稳定画像（路径 / 模块 / 工作流 / wiki）
- `project_uwacomm_2026-04-23_session` — 14 commit 收尾
- `project_uwacomm_2026-04-24_session` — SC-TDE V5.4 / DSSS V1.2 audit / SC-FDE sps+GAMP
- `project_uwacomm_2026-04-25_session` — V5.5 fd=1Hz / V5.6 HFM calibration
- `project_uwacomm_2026-04-26_session` — SC-FDE Phase 4+5 突破 14×
- `project_uwacomm_2026-04-27_session` — OTFS 重启移植 + P4 routing
- `project_uwacomm_2026-04-28_session` — P4 UI ↔ codex 对齐
- `project_uwacomm_2026-05-01_session` — P4 UI 稳定性 + V3.0 解耦
- `project_uwacomm_2026-05-03_session` — UI 50% RCA + Phase 2 bench fix
- `project_uwacomm_2026-05-04_session` — simple UI v2.0 / jakes V2.0 / OTFS K×2 / SC-FDE V4.1
- `project_uwacomm_2026-05-06_session` — OTFS 4-27 漏登 + Phase 4 BER FAIL 归档
- `project_uwacomm_2026-05-12_session` — claude+codex 175 文件吸收
- `project_uwacomm_2026-05-16_session` — rx_stream_p4 接口移植 + 双回归 RCA
- `project_uwacomm_e2e_benchmark` — E2E benchmark S1 完成
- `project_uwacomm_p3_ui` — P3 UI 遗留
- `project_uwacomm_alpha_refinement` — α 补偿改造
- `project_uwacomm_sctde_cfo_rca` — SC-TDE+DSSS CFO RCA 闭环
- `project_uwacomm_scfde_phase3b2` — SC-FDE Phase 3b.2 归档

**UWAcomm_usbl（13）**
- `project_uwacomm_usbl_init` — 项目初始化
- `project_uwacomm_usbl_techdesign` — SPEC-001 技术设计
- `project_uwacomm_usbl_scope` — 项目范围 2026-05-06
- `project_uwacomm_usbl_hardware_facts_2026-05-11` — VPX / 哈工程 / 厦门
- `project_uwacomm_usbl_2026-05-12_session` — 三件事并行
- `project_uwacomm_usbl_2026-05-13_session` — V0.8 大纲
- `project_uwacomm_usbl_2026-05-16_session` — _v2 反向 diff + _v3 重 build
- `project_uwacomm_usbl_2026-05-22_session` — 笔记 ingest + 差异对照 + 阵型决议
- `project_uwacomm_usbl_2026-06-01_session` — 水听器收发三板架构（SPEC-003 通用平台分置）
- `project_uwacomm_usbl_pooldata_2026-06-03` — calibration poolData 实测 DOA + W1/W2 校准流水线（CAGE5 5 元阵）
- `project_uwacomm_usbl_pooldata_6-04_2026-06-05` — 6-04 东南大学水池 CBF 校准验证（CBF 优于 TDOA）
- `project_uwacomm_usbl_doa_debug` — 1.9m DOA 调试（hilbert 包络修 abs-MF 检峰 bug）
- `project_uwacomm_usbl_poolData_gcc_cbf_2026-06-07` — GCC-TDOA vs CBF 实测深析

**USBL（1）**
- `project_usbl_h8_drafting` — H8 起草中断点
- `project_usbl_hw_init` — USBL_hw 派生（USBL 硬件设计，engineering-hardware 子型首例，🔒 无远程，ADR-026，2026-06-10 新增）

**DocProcess / UWAprojDoc（4）**
- `project_uwaprojdoc` — UWAprojDoc 状态
- `project_uwaprojdoc_2026-05-01_session` — 原型 ingest
- `project_uwaprojdoc_2026-05-22_session` — v17 final 33.2MB
- `project_uwaprojdoc_2026-05-29_session` — C1-C6 业务场景全套（C5/C6 使命级新增 + 六详章 + 独立场景 docx，commit ad59ef8）

**DocProcess / PaperReview（1）**
- `project_paperreview_init` — PaperReview 初始化

**DocProcess / DigitalTwinGuide（1）**
- `project_digitaltwinguide` — DigitalTwinGuide 初始化（数字孪生方法论文档）

**DocProcess / DigitalTwin1plusN（1）**
- `project_digitaltwin1plusn_init` — 「1+N」水下集群数字孪生体系（1 大 U + 24 小 U，双层孪生，P1-P11 决议，7 commit，2026-05-25 新增）

**DocProcess / VisioForge（1）**
- `project_visioforge_init` — 通用 Visio 出图工作区（复用 flowgen-* 8 skill，6 张 SN 效能预报图 1:1 复刻 + replica_lib2.py，2026-06-02 新增）

**DocProcess / CooperativeASW（1）**
- `project_cooperativeasw_init` — UWAprojDoc 编队协同探潜分系统单列细化 docx（17 章 223k 字 + 24 图 + I 族接口图，DEPENDS_ON=UWAprojDoc，2026-06-03 新增）

**DocProcess / PaperTrans（1）**
- `project_papertrans_init` — PaperTrans 派生（外文论文英译中翻译工作区，template-document，一篇=一spec=一译稿 + 术语单一可信源，🔒 无远程，2026-06-15 新增）

**DocProcess / UWAcommTrial（1）**
- `project_uwacommtrial_init` — UWAcommTrial 派生（UWAcomm 多模通信机通信距离湖上试验大纲，template-document，依赖 UWAcomm，完善大纲 + 13 表分页附件，v1 已交付归档，🔒 源仓无 git，2026-06-24 派生 / 2026-06-25 补登）

**DocProcess / UWCombatPlatform（1）**
- `project_uwcombatplatform_init` — UWCombatPlatform 派生（水下作战试验平台建设方案+报价，template-document，全链条 6 模块，依赖 UWAcomm/SonarSim/USBL，🔒 本地无远程，涉密 docx gitignore，2026-06-25 派生，初稿 6/26）

**TechReq / SonarSim（1）**
- `project_sonarsim_init` — 主动声呐界面仿真 MATLAB（SPEC-001 跑通单发同频干扰混响强度图 + 接声呐方程，2026-06-03 新增）

**Tools 系（9）**
- `project_flowgen_init` — FlowGen 初始化
- `project_flowgen_m8_drafting` — FlowGen M8-replica 中断点（PNG→Visio，视觉识图精度待提升）
- `project_flowgen_m8_layered_replica` — FlowGen M8 分系统架构图复刻（2026-05-29 9/9 张高保真 Visio，DRY 共享引擎 + 模型库异构 renderer）
- `project_flowgen_archmap_b2_layered` — FlowGen archmap L 族（阶段1 系统架构图 commit 5372721 已 push + 阶段2-A 逻辑架构图，冷蓝 renderer 5 增量 + compact 三档 fill，2026-06-01~02）
- `project_flowgen_archposter_ppt_restyle` — archposter 民国风→冷蓝 PPT 风重塑 + 反向工程 Visio 方法论（2026-05-30）
- `project_anthropic_ppt_init` — AnthropicPPT 初始化（2026-05-23）
- `project_iconforge_init` — IconForge 初始化（自然语言→图标 SVG，派生后暂停，2026-05-29）
- `project_ppt_master_adoption_2026-06-24` — 采纳 ppt-master(30.8k★ MIT)作通用 PPT 引擎 + FIELDBOOK 迁 brand/deck 模板 + AnthropicPPT 降级（Plan A，ADR-030，**第三方 vendored 不计活跃项目**，2026-06-24 新增）

**Ohmybrain Hub（6）**
- `project_ohmybrain_ecosystem` — 三仓架构 + Obsidian vault + 关键约定
- `project_ohmybrain_uwa_doppler_ingest` — 6 篇 UWA Doppler 论文 ingest
- `project_ohmybrain_2026-05-24_session` — PPT V4 + AnthropicPPT 派生 + 13 dedicated 页 + 三模板 + /sync-to-core 实战 + 三仓 push（2026-05-24 新增）
- `project_ohmybrain_agent_collab_protocol` — Claude+Codex 协作协议层（3 wiki 页 + 根 AGENTS.md + specs/plans/handoff/wiki 文件接口，ADR-024，2026-06-09 新增）
- `project_ohmybrain_2026-06-10_audit4` — 入会自检（四）：queue 收口（high 清空）+ uwaprojdoc 导航补建 + 5 日期 log 补登全清 + 审计误报 3 例（2026-06-10 新增）
- `project_ohmybrain_2026-06-24_audit6` — 入会自检（六）：5 维 workflow 审计（44 agent / 33 confirmed / 1 refuted）+ PaperTrans 补登（dashboard/system-overview/memory-index/ADR-029）+ USBL_hw 进展刷新（→c7c07da/71 commit）+ CANON 级联（skills 31→32 / memory 81→83）+ CooperativeDetection/PaperReview 标 🕸️（2026-06-24 新增）

> 注：`project_uwacomm`（含 13 条 session 条）+ `project_uwacomm_usbl`（含 13 条）+ `project_uwaprojdoc`（含 3 条）等高频项目的多日 session 条目均计入上方分组，加 Tools 系 7 + VisioForge/CooperativeASW/SonarSim/USBL_hw/PaperTrans/UWAcommTrial/UWCombatPlatform 各 1 + Ohmybrain Hub session 3 条（2026-06-09 / 2026-06-10 / 2026-06-24）+ Tools 系 +1 FieldKit +1 ppt-master，合计 61。

### reference（参考 · 3 条）

- `reference_otfs_pilot_tradeoff` — OTFS 3 方案（Impulse/ZC/Superimposed）PAPR-NMSE tradeoff
- `reference_uwacomm_obsidian` — UWAcomm 调试日志位置（迁至 wiki/debug-logs/）
- `reference_hub_three_channels` — Hub 三通道指导（~/.claude 全局层 / wiki query / core template，2026-05-24 新增）

## 按主题分类（cross-cutting）

> 同一 memory 条目可出现在多个主题下（cross-cutting 索引，非互斥分类）。

### OTFS / SC-FDE 体制演进

UWA 通信各体制（SC-TDE / DSSS / SC-FDE / OTFS）跨 session 的版本迭代主线：

- `project_uwacomm_alpha_refinement` — 双 LFM + 迭代 refinement + 4 体制推广（起点）
- `project_uwacomm_sctde_cfo_rca` — SC-TDE V5.4 + DSSS V1.2 CFO RCA 闭环
- `project_uwacomm_scfde_phase3b2` — SC-FDE Phase 3b.2 BEM 判决反馈
- `project_uwacomm_2026-04-26_session` — SC-FDE Phase 4+5 pilot=128 突破 14×
- `project_uwacomm_2026-04-27_session` — OTFS 重启移植（rx_otfs / spread-pilot / clip-PAPR）
- `project_uwacomm_2026-05-04_session` — SC-FDE V4.1 高 SNR 修复（117×）+ jakes V2.0
- `project_uwacomm_2026-05-06_session` — OTFS 漏登补登 + Phase 4 BER FAIL 归档
- `reference_otfs_pilot_tradeoff` — OTFS 导频 3 方案物理参考
- `feedback_uwacomm_skip_otfs` — OTFS 重启决策

### worktree 三路 / 多 agent 协作

- `feedback_uwacomm_worktree_ownership`
- `feedback_uwacomm_claude_branch_autonomous`
- `feedback_uwacomm_codex_compare_method`
- `feedback_uwacomm_usbl_worktree_ownership`
- `project_uwacomm_2026-05-12_session`（175 文件吸收案例）
- `project_uwacomm_2026-05-16_session`（双回归 RCA）

### 算法 RCA 方法论

MATLAB 算法 root-cause-analysis 的工具 + 边界：

- `feedback_single_root_cause_audit` — D9/D10 toggle + 跨 runner audit（核心方法）
- `feedback_uwacomm_testing_boundary` — 写完停下等用户跑，不代下结论
- `feedback_uwacomm_ui_ber_diagnose_order` — UI BER 异常先验直接链路
- `feedback_comp_resample_carrier_phase` — passband/baseband 载波相位差异
- `feedback_matlab_inf_bug` — inf 字面量 struct 转换坑

### 文档可视化（flowgen 系）

所有方案 / 方法论文档的图统一走 flowgen* skill 体系：

- `feedback_doc_flowgen_only` — 8 个 flowgen* skill 决策树分流（核心约束）
- `feedback_doc_visual_diversification` — 按业务真实结构匹配模式，禁统一布局换数据
- `project_flowgen_init` — FlowGen 工具初始化
- `project_flowgen_m8_drafting` — M8-replica PNG→Visio 中断点
- `project_flowgen_archmap_b2_layered` — archmap L 族系统/逻辑架构图 renderer（2026-06-01~02）
- `project_uwaprojdoc_2026-05-22_session` — 8 张 sub-N data-flow Visio 风 PNG/VSDX 实战
- `project_uwacomm_usbl_2026-05-13_session` — V0.8 大纲附录 13 张数据记录表

### doc pipeline / pandoc 产线

DocProcess 系 docx 生成的固化 pipeline 与反向 diff 经验：

- `project_digitaltwinguide` — 4 步 pandoc pipeline（normalize / pandoc / three_line / clean_indent）
- `project_uwaprojdoc_2026-05-22_session` — v17 final 17 章 146 图嵌入基线
- `project_uwacomm_usbl_2026-05-13_session` — 继承 2020 南海大纲样式 + 122 表全边框
- `project_uwacomm_usbl_2026-05-16_session` — _v2 反向 diff + _v3 8 步 build pipeline
- `feedback_uwacomm_usbl_worktree_ownership` — _v2 被用户改过需先反向 diff

### Hub 演化 / 知识闭环

- `project_ohmybrain_ecosystem` — 三仓架构（Hub=大脑 / project=业务 / core=模板）
- `project_ohmybrain_2026-05-24_session` — Hub 13 dedicated 页 + 三模板落地
- `reference_hub_three_channels` — 三通道指导（全局层 / wiki query / core template）
- `feedback_ohmybrain_self_improvement` — 进入 Hub 先完善自己
- `feedback_ohmybrain_workflow` — specs→plans→discussion→code 硬工序
- `feedback_sync_to_core_lessons` — /sync-to-core queue 先 diff 再决定
- `project_anthropic_ppt_init` — 从 PPT V4 沉淀派生工具

### 数字孪生体系（DocProcess 重型方案）

- `project_digitaltwinguide` — 数字孪生实施指南方法论（首份种子 = 20 吨级 AUV）
- `project_digitaltwin1plusn_init` — 「1+N」集群双层孪生体系（1 大 U + 24 小 U，"I 看 II 打"）

### USBL 实测 DOA / 阵列校准（2026-06 实测线）

UWAcomm_usbl calibration 分支 poolData/ 实测数据 DOA 估计与阵列校准（独立于合成仿真）：

- `project_uwacomm_usbl_2026-06-01_session` — 水听器收发三板架构（SPEC-003）
- `project_uwacomm_usbl_pooldata_2026-06-03` — poolData 实测 DOA + W1/W2 校准流水线
- `project_uwacomm_usbl_pooldata_6-04_2026-06-05` — 6-04 CBF 校准验证（CBF 优于 TDOA）
- `project_uwacomm_usbl_doa_debug` — 1.9m DOA hilbert 包络修 abs-MF bug
- `project_uwacomm_usbl_poolData_gcc_cbf_2026-06-07` — GCC-TDOA vs CBF 实测深析
- `feedback_matlab_interactive_figs` — MATLAB 出图用交互窗（view_td/view_analysis 函数）

## Memory ↔ Hub wiki 对应关系

| Memory 类型 | Hub wiki 对应位置 |
|-----------|------------------|
| feedback_* | [[anti-patterns]]（提炼后的反模式合集） |
| project_* | [[ecosystem-dashboard]]（项目状态） |
| reference_* | [[workflow-glossary]]（术语 + tradeoff 参考） |
| user_profile | 不在 wiki（隐私） |

## 维护节奏

- memory 是**主动**沉淀（每会话产生新条目）
- Hub wiki 是**被动**索引（季度更新本页同步）
- 不双向同步 — memory 是事实源，wiki 是索引视图
- **last-sync: 2026-06-25**（计数已对齐 CANON：feedback 21 / project 61 / reference 3 / user 1 / 总 86）

## 相关页面

- [[hub-as-brain]] — 大脑功能定位
- [[memory-stack]] — 5 层 memory 栈完整说明
- [[anti-patterns]] — feedback 提炼的反模式合集
- [[ecosystem-dashboard]] — project_* 状态总览
- [[workflow-glossary]] — reference_* 术语 + tradeoff
