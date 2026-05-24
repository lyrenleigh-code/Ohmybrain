---
type: topic
created: 2026-05-24
updated: 2026-05-24
tags: [memory, 索引, auto-memory]
---

# Memory 条目索引

`~/.claude/projects/D--Claude/memory/` 下 auto-memory 条目按类型 + 主题分类的索引。**事实源在 `MEMORY.md`**（每行一条目），本页是 Hub wiki 中的 mirror 视图，按类型聚合。

> 不复制 memory 完整内容（避免双写），本页只索引 + 简短描述 + link 到 memory 文件。

## 按类型分类

### user（用户画像 · 1 条）

- [user_profile](../../../../../zazn/.claude/projects/D--Claude/memory/user_profile.md) — UWA 研究者 / MATLAB 主力 / Windows+bash / 中文 / 专家主导 / 并行优先

### feedback（行为指导 · 15+ 条）

按主题分组：

**Git / 安全**
- `feedback_git_confirmation` — commit/push/delete/force 必须明确授权
- `feedback_pat_after_exposure` — PAT 暴露后用一次即停

**UWAcomm 算法工作流**
- `feedback_uwacomm_testing_boundary` — 不代跑单元测试 / 不代下结论 / 每 checkpoint 停
- `feedback_uwacomm_path` — `D:\Claude\TechReq\UWAcomm` 不是 `D:\TechReq`
- `feedback_uwacomm_worktree_ownership` — main/codex/claude 三路边界
- `feedback_uwacomm_claude_branch_autonomous` — claude 分支允许代跑 + 代决策
- `feedback_uwacomm_codex_compare_method` — codex worktree 对比方法（V7+ 头注约定）
- `feedback_uwacomm_ui_ber_diagnose_order` — UI BER 异常先验直接链路
- `feedback_uwacomm_skip_otfs` → OTFS 重启
- `feedback_uwacomm_usbl_worktree_ownership` — 双 worktree main/design

**算法 RCA**
- `feedback_single_root_cause_audit` — D9/D10 toggle + 跨 runner audit（限 MATLAB 算法 RCA）
- `feedback_matlab_inf_bug` — MATLAB inf 字面量触发 struct 转换错误，用 0 替代
- `feedback_comp_resample_carrier_phase` — passband 时间伸缩等效反载波相位 / baseband 需手动补

**Claude Code Harness**
- `feedback_project_local_agent_not_invocable` — 项目 .claude/agents/*.md 不在 subagent_type 列表
- `feedback_subagent_write_permission` — 后台 subagent Write/Bash 常被拒，主会话代写

**Ohmybrain 工作流**
- `feedback_ohmybrain_workflow` — 硬工序 `specs→plans→discussion→code`
- `feedback_doc_visual_diversification` — 流程图不能统一布局换数据
- `feedback_doc_flowgen_only` — 方案 / 方法论文档图必走 flowgen-* skill

### project（项目状态 · 30+ 条）

按项目分组：

**UWAcomm**（最多）
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

**UWAcomm_usbl**
- `project_uwacomm_usbl_init` — 项目初始化
- `project_uwacomm_usbl_techdesign` — SPEC-001 技术设计
- `project_uwacomm_usbl_scope` — 项目范围 2026-05-06
- `project_uwacomm_usbl_hardware_facts_2026-05-11` — VPX / 哈工程 / 厦门
- `project_uwacomm_usbl_2026-05-12_session` — 三件事并行
- `project_uwacomm_usbl_2026-05-13_session` — V0.8 大纲
- `project_uwacomm_usbl_2026-05-16_session` — _v2 反向 diff + _v3 重 build

**USBL**
- `project_usbl_h8_drafting` — H8 起草中断点

**DocProcess 系**
- `project_uwaprojdoc` — UWAprojDoc 状态
- `project_uwaprojdoc_2026-05-01_session` — 原型 ingest
- `project_uwaprojdoc_2026-05-22_session` — v17 final 33.2MB
- `project_paperreview_init` — PaperReview 初始化
- `project_digitaltwinguide` — DigitalTwinGuide 初始化

**Tools 系**
- `project_flowgen_init` — FlowGen 初始化
- `project_flowgen_m8_drafting` — FlowGen M8-replica 中断点
- `project_anthropic_ppt_init` — AnthropicPPT 初始化 (2026-05-23)

**Ohmybrain Hub**
- `project_ohmybrain_ecosystem` — 三仓架构 + Obsidian vault + 关键约定
- `project_ohmybrain_uwa_doppler_ingest` — 6 篇 UWA Doppler 论文 ingest

### reference（参考 · 5+ 条）

- `reference_otfs_pilot_tradeoff` — OTFS 3 方案 PAPR-NMSE tradeoff
- `reference_uwacomm_obsidian` — UWAcomm 调试日志位置

## 按主题分类（cross-cutting）

### V→V→V 工作流相关

- `project_uwacomm_2026-04-25_session` (V5.5 / V5.6)
- `project_uwacomm_2026-04-26_session` (SC-FDE Phase 4+5)
- `feedback_uwacomm_testing_boundary` (PMF 双指标边界)
- `feedback_single_root_cause_audit` (RCA 方法)

### worktree 三路相关

- `feedback_uwacomm_worktree_ownership`
- `feedback_uwacomm_claude_branch_autonomous`
- `feedback_uwacomm_codex_compare_method`
- `feedback_uwacomm_usbl_worktree_ownership`
- `project_uwacomm_2026-05-12_session` (175 文件吸收案例)

### Hub 演化相关

- `project_ohmybrain_ecosystem`
- `project_anthropic_ppt_init` (2026-05-23 触发 hub-as-brain 系列)
- `feedback_ohmybrain_workflow`

## Memory ↔ Hub wiki 对应关系

| Memory 类型 | Hub wiki 对应位置 |
|-----------|------------------|
| feedback_* | [[../concepts/anti-patterns]]（提炼后的反模式合集） |
| project_* | [[ecosystem-dashboard]]（项目状态） |
| reference_* | [[../concepts/workflow-glossary]]（术语 + tradeoff 参考） |
| user_profile | 不在 wiki（隐私） |

## 维护节奏

- memory 是**主动**沉淀（每会话产生新条目）
- Hub wiki 是**被动**索引（季度更新本页同步）
- 不双向同步 — memory 是事实源，wiki 是索引视图

## 相关页面

- [[../architecture/hub-as-brain]] — 大脑功能定位
- [[../architecture/memory-stack]] — 5 层 memory 栈完整说明
- [[../concepts/anti-patterns]] — feedback 提炼的反模式合集
