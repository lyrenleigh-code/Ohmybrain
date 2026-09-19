---
type: topic
created: 2026-05-24
updated: 2026-09-18
last-sync: 2026-09-15
tags: [memory, 索引, auto-memory]
---

# Memory 条目索引

`~/.claude/projects/D--Claude/memory/` 下 auto-memory 条目按类型 + 主题分类的索引。**事实源在 `MEMORY.md`**（每行一条目），本页是 Hub wiki 中的 mirror 视图，按类型聚合。

> 不复制 memory 完整内容（避免双写），本页只索引 + 简短描述 + link 到 memory 文件。

> **计数口径（@2026-09-19）**：auto-memory 共 **125 个**条目文件（外加 `MEMORY.md` 索引本身 = 目录 126 个 `.md`）。分布：user **1** / feedback **45** / project **76** / reference **3**。下方各类型标题计数与此严格一致。
>
> 注：`MEMORY.md` 索引行中「flowgen-vsdx M5 升级」一条指向 `~/.claude/skills/flowgen-vsdx/SKILL.md`（skill 文件，**非 memory 条目**），不计入总数。

## 按类型分类

### user（用户画像 · 1 条）

- [user_profile](../../../../../zazn/.claude/projects/D--Claude/memory/user_profile.md) — UWA 研究者 / MATLAB 主力 / Windows+bash / 中文 / 专家主导 / 并行优先

### feedback（行为指导 · 45 条）

按主题分组：

**Git / 安全（2）**
- `feedback_git_confirmation` — commit/push/delete/force 必须明确授权
- `feedback_pat_after_exposure` — PAT 暴露后用一次即停

**UWAcomm 算法工作流（7）**
- `feedback_uwacomm_testing_boundary` — 测试跑不跑按用户当次要求 / 不代下结论 / 每 checkpoint 停（2026-09-19 改裁）
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

**Claude Code Harness（4）**
- `feedback_project_local_agent_not_invocable` — 项目 .claude/agents/*.md 不在 subagent_type 列表
- `feedback_subagent_write_permission` — 后台 subagent Write/Bash 常被拒，主会话代写
- `feedback_bash_heredoc_backslash` — Bash 工具把 heredoc 里反斜杠折叠、Python 内联把控制符变 NUL；含反斜杠路径改用 Edit/Write（2026-08-26 新增）
- `feedback_open_newline_truncation` — Python `open(p, 'w', newline=坏值)` 先截断文件再抛 ValueError，脚本曾被清成 0 字节；写回一律 `newline=chr(10)`，补丁前 cp 备份（2026-09-09 新增）

**Ohmybrain / 文档工作流（16）**
- `feedback_ohmybrain_workflow` — 硬工序 `specs→plans→discussion→code`
- `feedback_verify_state_before_citing` — 引用状态前先核验仓库（不引用交接单等快照文档的过时数字）
- `feedback_never_overwrite_user_edits` — **强约束**：用户手改产物不可覆盖，生成前必检 mtime（AUVProposal 两次覆盖教训，2026-07 新增）
- `feedback_ppt_autofit_growth` — PPT autofit 框会长高压人：改文案判据看「长高后底边净距」，收尾跑逐行 diff（2026-08 新增）
- `feedback_pptx_endparaRPr_run_order` — XML 级插 run 落到 `endParaRPr` 之后会被 PowerPoint 静默丢弃；QA 必须扫元素次序（2026-09-01 新增，09-04 计数已含、指针本轮补登）
- `feedback_pptx_com_render_check` — PPT 改完用本机 PowerPoint COM 导 PNG 自查，别再说无渲染；断言查不出溢出/折行（2026-09-03 新增，09-04 计数已含、指针本轮补登）
- `feedback_doc_figure_plain_style` — 方案/建设类 docx 配图默认工程素样式：白底黑线直角框、宋体正文/黑体标题、字号以嵌入后看得清为准；雅黑加粗+圆角+灰底+阴影 = AI 感，整套图风格一致（2026-09-10 新增；09-19 改裁字号 + 并入出图细则 9 条）
- `feedback_docx_container_rebuild` — Word 报损坏但包结构无缺失＝容器问题，移植 python-docx 干净容器可救（2026-08 新增）
- `feedback_path_form_vs_location` — 用户给路径样例说「写成这样的形式」= 改文档里的路径写法，不是迁目录树；移整树前先问（AUVProposal 误迁 78 文件教训，2026-08-26 新增）
- `feedback_ohmybrain_self_improvement` — 进入 Ohmybrain 项目第一件事 = 完善自己（2026-05-24 新增）
- `feedback_sync_to_core_lessons` — /sync-to-core 首次实战：queue 须先 diff 再决定（2026-05-24 新增）
- `feedback_memory_retire_deindex` — memory 退役=去索引不销毁（`retire_memory.py` → Hub `raw/memory-retired/`，不直接 rm）
- `feedback_doc_visual_diversification` — 流程图不能统一布局换数据
- `feedback_doc_flowgen_only` — 方案 / 方法论文档图必走 flowgen-* skill
- `feedback_inplace_edit_no_version` — 修订保留版本号、不覆盖上一版，交付归档后再整理历史版本（2026-06-27 新增；09-19 用户改裁，取代原「就地改不留版本号」）
- `feedback_flowgen_palette_full_persist` — flowgen 默认配色更新需 4 处完整固化：.py 默认 + SKILL 正文 + frontmatter + 项目副本（2026-07 新增）
- `feedback_visio_headless_orphan_lock` — flowgen 渲染 SaveAs 报 [只读] = headless COM 孤儿进程占锁，仅杀无窗口标题者再重渲（2026-07 新增）
- `feedback_powershell_remove_item_hook_tokens` — 含 `Remove-Item` 的 PowerShell 命令里出现 `*` / `/` / 通配 / 正则会被系统路径保护 hook 误拦；测量与删除拆两条命令（2026-09-18 新增，指针本轮补）
- `feedback_elevated_powershell_script_pitfalls` — 提权 PowerShell 脚本四坑：RunAs 用 `-File` 包装；PS5.1 中文脚本须 UTF-8 BOM；robocopy 用 `/L` 退出码判一致；`*>` 日志是 UTF-16（2026-09-18 新增，指针本轮补）
- `feedback_discussion_rhythm` — 讨论与确认节奏：「先讨论」时不动文件、先图后文、待裁项编号+推荐、commit=只提交不续做（2026-09-19 会话记录扫描补登）
- `feedback_reporting_clarity` — 汇报清晰：交付首行给绝对路径、不用自创代号、说完成前列已做/未做、要文字就在对话里给（2026-09-19 补登）
- `feedback_formal_doc_writing` — 正式文档写作：书面公文体独立成文、关键技术写论证链、指标不用概率、公式可编辑符号全定义（2026-09-19 补登）
- `feedback_consistency_and_sources` — 口径与依据：分清底稿和参考、改一处口径全链同步、依据有出处推断要标注、先取自有项目口径（2026-09-19 补登）
- `feedback_docx_format` — docx 版式与交付：沿用用户样式、宋体小四三线表、交付前冻结域去批注不压图、外审稿用修订模式（2026-09-19 补登）
- `feedback_visio_layout_selfcheck` — Visio 连线图交付前整版几何自检 + 源数据核验；用户手调先回灌脚本再重渲（2026-09-19 补登）
- `feedback_sim_engineering_delivery` — 仿真与工程交付：本项目实际参数、反直觉先查设置、附 run_all / VS Code 命令、可配置有拓扑（2026-09-19 补登）
- `feedback_archify_dataflow_dense_layout` — archify 详细流程图改用 dataflow 类型的版式经验（2026-09-02 写于 AcousticLiteracy 零散库，09-19 收入主库）

### project（项目状态 · 76 条）

按项目分组：

**UWAcomm（11）**
- `project_uwacomm` — 6-scheme UWA sim 稳定画像（路径 / 模块 / 工作流 / wiki）
- `project_uwacomm_chronicle_2026H1` — 04-23~05-16 十二 session 合并编年（2026-08-18 蒸馏：可复用结论落 Hub 四 concept 页「实战结论」节，逐日细节见 UWAcomm 仓 git/wiki）
- `project_uwacomm_e2e_benchmark` — E2E benchmark S1 完成
- `project_uwacomm_p3_ui` — P3 UI 遗留
- `project_uwacomm_alpha_refinement` — α 补偿改造
- `project_uwacomm_sctde_cfo_rca` — SC-TDE+DSSS CFO RCA 闭环
- `project_uwacomm_scfde_phase3b2` — SC-FDE Phase 3b.2 归档
- `project_uwacomm_linux_engineering_audit` — Linux 工程化四路核验（唯一硬阻塞 = 18 个 PoolTest 硬路径 + 三线分岔盘点，交接单已给 Codex，2026-07-09 新增）
- `project_uwacomm_2026-07-13_session` — 逐模块校验战役（01-03 收口）+ ChannelDemo 演示+外发包（2026-07-13 新增）
- `project_uwacomm_2026-07-15_session` — S2C 第 7 体制 Phase 1 全通 + OTFS 公共链接入（2026-07-15 新增）
- `project_uwacomm_2026-07-21_session` — Codex 版本三路审查（0 CRIT/HIGH）+ Jakes 基准逐 seed 复现，项目暂停待办 5 项（2026-07-21 新增）
- `project_uwacomm_three_scheme_timevarying_diagrams` — 三体制抗时变梳理 + archify 图（UWAcomm main `53e41e7`，2026-09-02 写于 AcousticLiteracy 零散库，09-19 收入主库）
- `project_uwacomm_cport_d3000m_latency` — cport 在飞腾 D3000M 卡顿三层成因与整改（`e4c22af`，2026-09-04 写于 AcousticLiteracy 零散库，09-19 收入主库）

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

**USBL（2）**
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

**DocProcess / DigitalTwin1plusN（1，项目已退役）**
- `project_digitaltwin1plusn_init` — 「1+N」水下集群数字孪生体系（1 大 U + 24 小 U，双层孪生，P1-P11 决议，2026-05-25 新增；**项目工作区 2026-08-18 用户确认删除退役**）

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

**DocProcess / CommSimSupport（1）**
- `project_commsimsupport_init` — CommSimSupport 派生（通信机仿真使用支持申报书，template-document，依赖 UWAcomm，脚手架就位撰写未启动，git 未 init，2026-07-01 派生）

**DocProcess / OceanEnvSupport（1）**
- `project_oceanenvsupport_init` — OceanEnvSupport 派生（海洋环境数据作战保障方案，月尺度预报核心资产，F-1 六分系统架构落 wiki/topics，等 D1-D5 决断，2026-07-09 派生）

**DocProcess / ImgSonarTwin（1）**
- `project_imgsonartwin_init` — ImgSonarTwin 派生（图像声呐数字孪生方案，ADR-035；07-18 全文初稿 → 07-19 成品化 build_docx 管线，剩 Codex 审计 + 用户全文审，2026-07-18 派生）

**DocProcess / AUVProposal（1）**
- `project_auvproposal_init` — AUVProposal 派生（AUV 项目立项论证《AUV 项目建议书》docx，依赖 AUVSurvey，ADR-038；08-17 汉江构型舱段重划 SPEC-026 六舱段定案，2026-07-24 派生）

**DocProcess / AUVSurvey（1）**
- `project_auvsurvey_init` — AUVSurvey 派生（AUV 广泛调研，下游 AUVProposal，ADR-039；SPEC-001+6 专题页 + SPEC-002 型制深化 + 15 PDF 入库，门槛=型谱清单用户增删，2026-07-24 派生）

**DocProcess / CoupledMultiOrder（1）**
- `project_coupledmultiorder_init` — CoupledMultiOrder 派生（多阶耦合智能艇群阶跃式协控，ADR-040；主交付物=汇报 PPT 59 页 V5→V6 克制修订 + 解说词 + 补充说明 docx，2026-08-05 派生）

**DocProcess / DeepSeaIndustry（1）**
- `project_deepseaindustry_init` — DeepSeaIndustry 派生（深海技术产业促进申报书，ADR-042；申报口径待定先搭架子，git `97fa2c3`）

**DocProcess / XiaojingLaunch（1）**
- `project_xiaojinglaunch_init` — XiaojingLaunch 小鲸100 V3.0 发布会材料（ADR-043；派生当日 SPEC-001 交付：解说词微调版 + PPT 框架 17 页，git `2ee3f7d`）

**DocProcess / AUVSlopeMCM（1）**
- `project_auvslopemcm_init` — AUVSlopeMCM 派生（AUV 坡上扫雷，ADR-045；主交付物形态/任务口径待讨论先搭架子，无依赖，git `723d2fb`）

**DocProcess / UUVCommSwarmSim（1）**
- `project_uuvcommswarmsim_init` — UUVCommSwarmSim 派生（UUV 通信组网与集群控制一体化仿真软件，ADR-046；主交付物形态/受众/口径待讨论先搭架子，无依赖，git `d06f8f4`）

**DocProcess / SoSCommSupport（1）**
- `project_soscommsupport_init` — SoSCommSupport 派生（体系通信保障，ADR-047；目录名代拟可改；主交付物形态/受众/口径待讨论先搭架子，无依赖，git `d3831e3`）

**DocProcess / AUVNetCoop（1）**
- `project_auvnetcoop_init` — AUVNetCoop 派生（协同探测型 AUV 组网协同系统，ADR-048；主交付物《协同探测型AUV组网协同系统研制技术协议》，AUVProposal 三艇 AUV 平台底座，SPEC-001 框架同日终裁 D1~D9，依赖 AUVProposal，git `5a6bbfc`）

**DocProcess / ProductPortfolio（1）**
- `project_productportfolio_init` — ProductPortfolio 派生（公司产品体系梳理，ADR-049；主交付物《公司产品体系梳理》docx，依赖 XiaojingLaunch，种子 4 份 + 口径基线页 + SPEC-001 D1~D6 待裁，git `2a0a591`）

**DocProcess / AcousticLiteracy（1）**
- `project_acousticliteracy_init` — AcousticLiteracy 派生（声学素养提升项目，ADR-044；口径待讨论先搭架子，git `88a7379`）

**Patents（1）**
- `project_patents_2026-06-29` — 4 候选模板化重构 + 首次本地 git init（53bd96d 仅本地无远程；07-11 检阅时实际已 6 候选目录）

**个人 / HR（1）**
- `project_halfyear_summary_2026h1` — 2026 上半年个人工作总结成稿（算法组自评，D:\文档，4 项重点 + 声载荷负责人口径 + docx 构建管线，2026-07-11 新增）

**TechReq / SonarSim（1）**
- `project_sonarsim_init` — 主动声呐界面仿真 MATLAB（SPEC-001 跑通单发同频干扰混响强度图 + 接声呐方程，2026-06-03 新增）

**TechReq / SonarFOM（1）**
- `project_sonarfom_init` — SonarFOM 派生（声呐效能 FOM 品质因数表计算，依赖 SonarSim，ADR-036，git init `fb00819`，2026-07-21 派生）

**TechReq / EnvDataClassify（1）**
- `project_envdataclassify_init` — EnvDataClassify 派生（海洋环境数据分类：声速剖面/水文，依赖 SonarFOM，ADR-037，git init `a7de7b2`，2026-07-23 派生）

**TechReq / AUVNetModem（1）**
- `project_auvnetmodem_init` — AUVNetModem 派生（面向五U 组网条件的水声通信机详细设计，A 算法 + B 硬件，engineering-hardware 子型，依赖 AUVNetCoop / UWAcomm / AUVProposal，ADR-050，git init `c37e2ce`，SPEC-001 框架 v0 待裁 D1~D10，2026-09-18 派生）

**Tools 系（9）**
- `project_flowgen_init` — FlowGen 初始化
- `project_flowgen_m8_drafting` — FlowGen M8-replica 中断点（PNG→Visio，视觉识图精度待提升）
- `project_flowgen_m8_layered_replica` — FlowGen M8 分系统架构图复刻（2026-05-29 9/9 张高保真 Visio，DRY 共享引擎 + 模型库异构 renderer）
- `project_flowgen_archmap_b2_layered` — FlowGen archmap L 族（阶段1 系统架构图 commit 5372721 已 push + 阶段2-A 逻辑架构图，冷蓝 renderer 5 增量 + compact 三档 fill，2026-06-01~02）
- `project_flowgen_archposter_ppt_restyle` — archposter 民国风→冷蓝 PPT 风重塑 + 反向工程 Visio 方法论（2026-05-30）
- `project_anthropic_ppt_init` — AnthropicPPT 初始化（2026-05-23）
- `project_iconforge_init` — IconForge 初始化（自然语言→图标 SVG，派生后暂停，2026-05-29）
- `project_ppt_master_adoption_2026-06-24` — 采纳 ppt-master(30.8k★ MIT)作通用 PPT 引擎 + FIELDBOOK 迁 brand/deck 模板 + AnthropicPPT 降级（Plan A，ADR-030，**第三方 vendored 不计活跃项目**，2026-06-24 新增）
- `project_fieldkit_init` — FieldKit 派生（校准场/Calibration Field 图示风格系统，共享 kit + HTML 生成器 v1 + styled_diagram v2，ADR-027/028，2026-06-15 新增；此前计数已含、bullet 漏列，2026-08-18 补列）

**Ohmybrain Hub（7）**
- `project_ohmybrain_ecosystem` — 三仓架构 + Obsidian vault + 关键约定
- `project_ohmybrain_uwa_doppler_ingest` — 6 篇 UWA Doppler 论文 ingest
- `project_ohmybrain_2026-05-24_session` — PPT V4 + AnthropicPPT 派生 + 13 dedicated 页 + 三模板 + /sync-to-core 实战 + 三仓 push（2026-05-24 新增）
- `project_ohmybrain_agent_collab_protocol` — Claude+Codex 协作协议层（3 wiki 页 + 根 AGENTS.md + specs/plans/handoff/wiki 文件接口，ADR-024，2026-06-09 新增）
- `project_ohmybrain_2026-06-10_audit4` — 入会自检（四）：queue 收口（high 清空）+ uwaprojdoc 导航补建 + 5 日期 log 补登全清 + 审计误报 3 例（2026-06-10 新增）
- `project_ohmybrain_2026-06-24_audit6` — 入会自检（六）：5 维 workflow 审计（44 agent / 33 confirmed / 1 refuted）+ PaperTrans 补登（dashboard/system-overview/memory-index/ADR-029）+ USBL_hw 进展刷新（→c7c07da/71 commit）+ CANON 级联（skills 31→32 / memory 81→83）+ CooperativeDetection/PaperReview 标 🕸️（2026-06-24 新增）
- `project_ohmybrain_ccppt_v16` — CC 方法论 PPT v16 定稿（63 页终版，内网章 + 案例实证化，md→Edge 截图管线 / docx 抽图 / 锁冲突旁路换入，2026-07-04 新增）

> 注：各分组小计（@2026-08-18）：UWAcomm 11 + UWAcomm_usbl 13 + USBL 2 + UWAprojDoc 4 + PaperReview/DigitalTwinGuide/DigitalTwin1plusN(退役)/VisioForge/CooperativeASW/PaperTrans/UWAcommTrial/UWCombatPlatform/CommSimSupport/OceanEnvSupport/ImgSonarTwin/AUVProposal/AUVSurvey/CoupledMultiOrder 各 1（计 14）+ Patents 1 + 个人/HR 1 + SonarSim/SonarFOM/EnvDataClassify 各 1（计 3）+ Tools 系 9 + Ohmybrain Hub 7 = **65**。

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
- `reference_otfs_pilot_tradeoff` — OTFS 导频 3 方案物理参考
- `feedback_uwacomm_skip_otfs` — OTFS 重启决策

### worktree 三路 / 多 agent 协作

- `feedback_uwacomm_worktree_ownership`
- `feedback_uwacomm_claude_branch_autonomous`
- `feedback_uwacomm_codex_compare_method`
- `feedback_uwacomm_usbl_worktree_ownership`

### 算法 RCA 方法论

MATLAB 算法 root-cause-analysis 的工具 + 边界：

- `feedback_single_root_cause_audit` — D9/D10 toggle + 跨 runner audit（核心方法）
- `feedback_uwacomm_testing_boundary` — 测试跑不跑按用户当次要求，不代下结论
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
- **last-sync: 2026-08-18（第二轮·蒸馏）**（计数已对齐 CANON：feedback 28 / project 65 / reference 3 / user 1 / 总 97；同日第一轮补登 14 指针后，第二轮首次 memory→wiki 蒸馏：UWAcomm 12 条逐日 session 并入 `project_uwacomm_chronicle_2026H1`，可复用结论落 4 concept 页「实战结论」节）

## 相关页面

- [[hub-as-brain]] — 大脑功能定位
- [[memory-stack]] — 5 层 memory 栈完整说明
- [[anti-patterns]] — feedback 提炼的反模式合集
- [[ecosystem-dashboard]] — project_* 状态总览
- [[workflow-glossary]] — reference_* 术语 + tradeoff
