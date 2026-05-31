---
type: topic
created: 2026-05-24
updated: 2026-05-31
last-sync: 2026-05-31
tags: [memory, 索引, auto-memory]
---

# Memory 条目索引

`~/.claude/projects/D--Claude/memory/` 下 auto-memory 条目按类型 + 主题分类的索引。**事实源在 `MEMORY.md`**（每行一条目），本页是 Hub wiki 中的 mirror 视图，按类型聚合。

> 不复制 memory 完整内容（避免双写），本页只索引 + 简短描述 + link 到 memory 文件。

> **计数口径（@2026-05-31）**：auto-memory 共 **67 个**条目文件（外加 `MEMORY.md` 索引本身 = 目录 68 个文件）。分布：user **1** / feedback **20** / project **43** / reference **3**。下方各类型标题计数与此严格一致。

## 按类型分类

### user（用户画像 · 1 条）

- [user_profile](../../../../../zazn/.claude/projects/D--Claude/memory/user_profile.md) — UWA 研究者 / MATLAB 主力 / Windows+bash / 中文 / 专家主导 / 并行优先

### feedback（行为指导 · 20 条）

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

**算法 RCA（3）**
- `feedback_single_root_cause_audit` — D9/D10 toggle + 跨 runner audit（限 MATLAB 算法 RCA）
- `feedback_matlab_inf_bug` — MATLAB inf 字面量触发 struct 转换错误，用 0 替代
- `feedback_comp_resample_carrier_phase` — passband 时间伸缩等效反载波相位 / baseband 需手动补

**Claude Code Harness（2）**
- `feedback_project_local_agent_not_invocable` — 项目 .claude/agents/*.md 不在 subagent_type 列表
- `feedback_subagent_write_permission` — 后台 subagent Write/Bash 常被拒，主会话代写

**Ohmybrain / 文档工作流（5）**
- `feedback_ohmybrain_workflow` — 硬工序 `specs→plans→discussion→code`
- `feedback_ohmybrain_self_improvement` — 进入 Ohmybrain 项目第一件事 = 完善自己（2026-05-24 新增）
- `feedback_sync_to_core_lessons` — /sync-to-core 首次实战：queue 须先 diff 再决定（2026-05-24 新增）
- `feedback_doc_visual_diversification` — 流程图不能统一布局换数据
- `feedback_doc_flowgen_only` — 方案 / 方法论文档图必走 flowgen-* skill

### project（项目状态 · 43 条）

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

**UWAcomm_usbl（8）**
- `project_uwacomm_usbl_init` — 项目初始化
- `project_uwacomm_usbl_techdesign` — SPEC-001 技术设计
- `project_uwacomm_usbl_scope` — 项目范围 2026-05-06
- `project_uwacomm_usbl_hardware_facts_2026-05-11` — VPX / 哈工程 / 厦门
- `project_uwacomm_usbl_2026-05-12_session` — 三件事并行
- `project_uwacomm_usbl_2026-05-13_session` — V0.8 大纲
- `project_uwacomm_usbl_2026-05-16_session` — _v2 反向 diff + _v3 重 build
- `project_uwacomm_usbl_2026-05-22_session` — 笔记 ingest + 差异对照 + 阵型决议

**USBL（1）**
- `project_usbl_h8_drafting` — H8 起草中断点

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

**Tools 系（6）**
- `project_flowgen_init` — FlowGen 初始化
- `project_flowgen_m8_drafting` — FlowGen M8-replica 中断点（PNG→Visio，视觉识图精度待提升）
- `project_flowgen_m8_layered_replica` — FlowGen M8 分系统架构图复刻（2026-05-29 9/9 张高保真 Visio，DRY 共享引擎 + 模型库异构 renderer）
- `project_flowgen_archposter_ppt_restyle` — archposter 民国风→冷蓝 PPT 风重塑 + 反向工程 Visio 方法论（2026-05-30）
- `project_anthropic_ppt_init` — AnthropicPPT 初始化（2026-05-23）
- `project_iconforge_init` — IconForge 初始化（自然语言→图标 SVG，派生后暂停，2026-05-29）

**Ohmybrain Hub（3）**
- `project_ohmybrain_ecosystem` — 三仓架构 + Obsidian vault + 关键约定
- `project_ohmybrain_uwa_doppler_ingest` — 6 篇 UWA Doppler 论文 ingest
- `project_ohmybrain_2026-05-24_session` — PPT V4 + AnthropicPPT 派生 + 13 dedicated 页 + 三模板 + /sync-to-core 实战 + 三仓 push（2026-05-24 新增）

> 注：`project_uwacomm`（含 13 条 session 条）+ `project_uwacomm_usbl`（含 8 条）+ `project_uwaprojdoc`（含 3 条）等高频项目的多日 session 条目均计入上方分组，合计 43。

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
- **last-sync: 2026-05-31**（计数已对齐 CANON：feedback 20 / project 43 / reference 3 / user 1 / 总 67）

## 相关页面

- [[hub-as-brain]] — 大脑功能定位
- [[memory-stack]] — 5 层 memory 栈完整说明
- [[anti-patterns]] — feedback 提炼的反模式合集
- [[ecosystem-dashboard]] — project_* 状态总览
- [[workflow-glossary]] — reference_* 术语 + tradeoff
