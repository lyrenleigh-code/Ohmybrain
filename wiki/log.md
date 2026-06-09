# 变更日志

> 记录每次对 wiki 的操作，最新的在最上面。

---

## [2026-06-09] promote | 紧凑阵 DOA 实测经验脱敏回流（usbl-positioning + mimo-and-array-processing）

`/promote-answer` 跨项目回流（入会自检 P1「找跨项目可 promote 的结论」）。把某紧凑基阵受控水域实测 DOA 调试的可复用结论，经 [[architecture/conventions]] §9 脱敏后写入两个**既有** concept 页，**页面总数不变 107**（仅内容增补 + `updated`→2026-06-09）。

**源**：私人内网项目实测线归档（5 篇 RCA / 对比 / 口径文档），及用户审定的 4 篇项目 memory 综述。**双 workflow 核验**：Phase 1（4 agent 并行核验 7 篇归档 + 规划落点，与 memory 综述零冲突、已识别并丢弃被推翻的中间结论）→ 主会话起草 → Phase 2（3 lens 对抗验证：脱敏泄漏 / 过度断言+陈旧值 / 事实支撑+跨页重复，均 pass_with_fixes、无 critical）。

**落点分工**（防跨页重复，交叉处 wikilink 互引而非各写一遍）：
- [[concepts/usbl-positioning]] §实测经验（USBL 应用角度，5 条）：校准收益取决于接入的 DOA 模态 / CBF 现场精度优于群时延 TDOA（带单目标·低中多径·整带相干条件）/ 分辨率≠精度 / 校准「可迁移 vs 条件内拟合」/ 密角栅格+多工况覆盖设计建议。
- [[concepts/mimo-and-array-processing]] §实测经验（通用阵列处理，6 条）：群时延 vs 波束/载波相位两种 DOA 模态 / 小孔径模态天花板换估计器无法突破 / abs 实信号检峰载波假象→hilbert+抛物亚样点 / GCC-PHAT 预白化+限带 cycle-skip / 鲁棒共识失效边界（低抖动≠高可信）/ 正交阵解耦病态维度。

**脱敏要点**（§9 五步，用户审后写入）：剥项目名/型号/试验地点/数据集编号/脚本名/commit/内网路径；数值降量级+带条件（避免精确数值簇成可反推指纹）；抹「两距离/距离翻倍」数据集结构指纹；阵型泛化为「紧凑基阵」；不携任何私有仓/worktree 反链。修复 Phase 2 抓到的跨页重复（usbl 模态论压成应用结论+wikilink）+ 因果篡改（~度级 RMS 不归因「校准只消平滑偏置」）+ 软化「不能突破」绝对措辞 + 拆分「同角稳定性 vs 跨工况泛化」。

**沉淀**：据本次实践补 [[architecture/conventions]] §9 警示「**数值簇 = 可反推指纹**」——单个数值像量级，但成簇 + 实验结构仍可反推唯一试验，脱敏须抹数据集结构指纹、leak-safety 优先于 credibility。

**核验**：`lint_wiki.py` ✓ / 页面总数不变 107 / 两页 `updated` 已同步 + conventions §9 增警示。

---

## [2026-06-09] maintenance | 项目文档结构口径同步：三模板 + handoff + 硬件设计子型

按用户要求整理当前项目文档结构，采用**文档口径同步**而非目录迁移：不移动 `TechReq/`、`DocProcess/`、`Tools/`、`worktrees/`、`Patents/`、`Ohmybrain/`、`ohmybrain-core/` 等既有根路径，只更新会指导后续行动的入口、SOP、架构说明和下沉队列。

**同步内容**：

- **P0 入口文档**：更新 `D:/Claude/CLAUDE.md`、`Ohmybrain/README.md`、`Ohmybrain/CLAUDE.md`、`ohmybrain-core/README.md`、`ohmybrain-core/docs/new-project-sop.md`，统一为 `template-engineering/`、`template-document/`、`template-tool/` 三模板派生口径；任务状态入口统一为 `specs/active/` + `plans/active/` + `handoff/active/`。
- **新项目 SOP**：删除旧 `ohmybrain-core/template/` 单模板流程，改为按项目类型派生；新增 **engineering-hardware** 子型，单独硬件设计项目仍从 `template-engineering/` 派生到 `TechReq/<name>/`，再补 `design/`、`bom/`、`datasheets/`、`prototypes/` 等硬件资料目录。
- **架构页**：同步 `project-types`、`system-overview`、`three-tier-architecture`、`dual-loop`、`conventions`、`core-update-mechanism`、`hub-as-brain`、`memory-graph` 等当前说明页，把旧 `template/`、`plans/<slug>.md` 改成 `template-*` 与 `plans/active/<slug>.md`。
- **操作索引页**：同步 `harness-resources`、`core-update-queue`、`workflow-glossary`、`ecosystem-dashboard`，避免 `/sync-to-core`、derive 术语和 harness 来源继续指向旧路径。
- **项目导航**：补 `projects/patents/README.md` 私密项目卡；`system-overview` 的 `projects/` 导航入口计数更新为 18。
- **Hub 索引**：更新 `wiki/index.md` 相关条目描述；页面总数保持 107，无新增 wiki 页。

**保留原则**：`decision-log`、历史 `source-summaries`、旧探索记录中的 `template/` 若属于历史事实，不做重写，避免污染时间线。

---

## [2026-06-09] maintenance | 入会自检（三）：脚本侧 + CANON 计数「部分登记」收尾 + 3 历史遗留收口

入会自检（memory `feedback_ohmybrain_self_improvement`）。承接同日审计（二）commit `538b00c`（已 push gitlab，工作树干净）。P0 核对 log/MEMORY/roadmap 后，**针对性对抗验证**（538b00c 后无新 commit / 新 memory，markdown 全站 wiki 计数已一致 107/109，故不重跑全量 workflow 审计已验证状态）抓到两处审计（二）遗留的 **「部分登记」straggler**，并经用户裁决收口 3 个历史遗留项。

**Finding 1 · 脚本侧部分登记（concrete bug）**：`scripts/dashboard_snapshot.py` 实时报 **内容页 105**，而 markdown 全站为 107——根因是其 `WIKI_SUBDIRS` 硬编码列表**未含审计（二）新建的 `agents/` + `workflows/` 两分类**。脚本本应是 markdown 计数的对齐基准，却低报 2，**反向风险**：下次有人「按脚本输出对齐 markdown」会把 107 错改回 105。修法选**自愈式**（`discover_wiki_subdirs` 自动发现 wiki 全部子目录，已知分类按 `PREFERRED_ORDER` 排序、未来新分类按字母序追加），从根上消除「新增 wiki 分类 → 脚本静默漏算」。实跑：内容页 105→**107**、breakdown 与 [[topics/ecosystem-dashboard]] 表逐项一致。lint 只查孤儿页、不查计数，故此前一直放过。

**Finding 2 · CANON memory 计数部分登记**：审计（二）新增 memory `project_ohmybrain_agent_collab_protocol`（77→78 / project 52→53），但 **CANON 计数只传播到 [[topics/memory-index]]**，**11 处其他位置仍停在 77/52**。核验实文件数确为 **78**（user 1 / feedback 21 / **project 53** / reference 3；MEMORY.md 索引 79 行 = 78 memory + 1 个 flowgen-vsdx skill 指针）后，统一传播 78/53：`conventions §0` / `hub-as-brain`（gap7 + CANON 表 + dashboard 实跑行，3 处）/ `anti-patterns`（正文 + 相关页，2 处）/ `three-tier-architecture` / `index` / `ecosystem-dashboard`（规模表 + 相关页，2 处）/ `roadmap`（dashboard 实跑行）。

**3 历史遗留收口（审计「一」surface、用户本次裁决全做）**：

1. **Patents 🔒 登记进 Hub 视图**：根 `D:/Claude/CLAUDE.md` 有 Patents 但 Hub `CLAUDE.md` 映射表 + [[topics/ecosystem-dashboard]] 缺（system-overview / conventions §9 早已含，活跃项目 17 也早已计入）。补 Hub `CLAUDE.md` 映射行 + dashboard 新增「专利工作区」子段（🟡 候选 / 无 git / 3 候选交底书）。
2. **根 `D:/Claude/CLAUDE.md` worktree 表补 `UWAcomm_usbl-calibration` 行**（Hub conventions §10 早已 4 行，根文件仅 3 行；calibration/v1.x CAGE5 阵元位置 LS 校准，HEAD `eae7080` 未 push）。**根文件改动经用户授权**。
3. **FlowGen archmap 族单列 ADR-025**（事件 2026-06-01~04，追溯登记）：[[architecture/decision-log]] 新增 ADR-025（L 族分层架构图 archmap_layered + I 族 hub-spoke archmap_interface + business/data/stdflow renderer，托管于 flowgen-archposter）。**编号取舍**：采用 **append-only 稳定 ID**（不重排既有编号，避免 024→025 跨页引用级联失效，正是 [[log]] 2026-05-29 重编号教训），ADR-025 按事件日期排在 ADR-024(06-09) 与 ADR-023(06-03) 之间，**编号与位置不严格对应**已在起点声明显式说明。级联：起点声明范围 + **10 处 `ADR-001~024`→`~025`**（conventions×2 / hub-as-brain×2 / workflow-glossary×2 / harness-resources / ecosystem-dashboard×2）+ roadmap 里程碑补 2026-06-04 行。

**核验**：`lint_wiki.py` ✓ / `dashboard_snapshot.py` 实跑 内容页 107 + memory 78 / grep 全站零残留（无 `~024` 范围引用、无 `77`·`project 52` memory 计数）。**本批已 commit + push gitlab main**（用户授权；GitHub origin 暂不动，仍停在 `6e4fedf` 落后 gitlab，待后续统一）。

> **新增反模式认知**（→ memory）：「部分登记」触发面再泛化——不只「新项目派生」「新增 wiki 页/分类」，**「新增 memory 条目」同样会漏传 CANON 计数**，且 **CANON 计数的验证脚本本身也可能成为漏登对象**（脚本硬编码枚举 = stale 源）。lint 不查计数是结构性盲区，须靠 `dashboard_snapshot.py` 实跑 + grep 后置核验。

---

## [2026-06-09] maintenance | 入会自检一致性审计（二）：协作协议层「部分登记」收尾

入会自检（memory `feedback_ohmybrain_self_improvement`）。承接上一条「协作协议层落地」——该批 3 新页 + index/log + 根 AGENTS.md 已就位（104→107），但 log 自承「lint_wiki.py 待本轮补齐后统一运行」，属典型**「部分登记」反模式**（与 06-04 `6e4fedf` 漏同步同源）：3 新页把页数推到 107，但**规模表 / 枚举 / 新页约定全未收尾**。

ultracode 用 workflow 系统审计（6 cluster 并行 → 逐 finding 对抗验证，37 agent / 188 tool-use）对照权威源（`index.md` 107 + 实时文件系统 + `conventions §3`），产出 **31 处已验证 finding（0 refuted）**。主会话代写修复 **Group 1-4（19 处机械/合规，is_judgment_call=false）**：

- **计数 / 枚举（8 处，6 文件）**：`system-overview`（§当前规模 104→107 + Hub 目录树补 agents/workflows/mcp-entities）、`conventions`（§2 callout 106→109）、`ecosystem-dashboard`（内容页 104→107 / 总文件 106→109）、`hub-as-brain`（CANON 表 + line119 dashboard 实跑值）、`workflow-glossary`（口径 callout 106→109）、`memory-stack`（Layer5 粒度行补新分类）。全部 architecture 11→12 + agents 1 + workflows 1。
- **新页约定合规（3 页 × 2）**：3 新页原 frontmatter=0 / wikilink=0，**直接违反 conventions §3**（必含 type/created/updated/tags + ≥1 wikilink）→ 补 YAML frontmatter（type 按目录单数取 architecture/agent/workflow）+ 末尾「相关页面」（wikilinks 5/4/3）。
- **交叉链（4 处）**：`system-overview`/`conventions`/`dual-loop`/`hub-as-brain` 的「相关页面」补链入 3 新页，打破 agents/workflows 两新分类的孤岛。
- **既存 stale 顺带（1 处）**：`roadmap` §P0 `ADR-001~020`→`~023`（上一轮 7b7fa9d 补登 021~023 时漏改）。

lint 通过、全站无残留 104/106。**Group 5 判断项经用户裁决全部采纳并应用**：① 新增 **ADR-024**（Claude+Codex 协作协议层）+ roadmap / system-overview 各加 2026-06-09 里程碑行 + 级联 bump 全站「ADR-001~023」**当前范围**引用→「~024」（decision-log 起点声明 / hub-as-brain×2 / conventions×2 / workflow-glossary×2 / ecosystem-dashboard×2 / harness-resources，共 10 处；roadmap §P0「补齐历史」与 dashboard 历史 ADR-021~023 描述不动）；② 新增 memory `project_ohmybrain_agent_collab_protocol` + MEMORY.md 索引 + memory-index 计数 77→78 / project 52→53；③ commit + push gitlab main（连带上一 commit `7b7fa9d`）。

---

## [2026-06-09] architecture | Claude Code + Codex 协作协议层落地

承接用户提出的「Claude Code 和 Codex 联合使用场景」与「整个文档结构重新构建」需求，本次采用**文档协议层重构**，不移动任何既有代码/项目根路径。

**新增 3 个 Hub 协议页**：
- `wiki/architecture/document-protocol.md` — 标准项目骨架、三层文档职责、路径安全、状态所有权、迁移级别（默认 L0+L1）
- `wiki/agents/claude-codex-collaboration.md` — Claude Code / Codex 分工、串行交接、并行探索、红队 review、worktree 边界
- `wiki/workflows/agent-handoff.md` — `handoff/active/` 交接单触发条件、模板、归档标准

**根入口更新**：
- `D:/Claude/AGENTS.md` 从单纯引用 `CLAUDE.md` 扩展为 agent 协作入口，指向三页协议文档并明确 raw 只读、wiki index/log 同步、并行 worktree 边界。
- `D:/Claude/CLAUDE.md` 增加「Agent 协作协议层」，声明 `specs/active/ + plans/active/ + handoff/active/` 为任务状态入口。

**路径策略**：本轮只补协议与目录骨架，不迁移 `TechReq/`、`DocProcess/`、`Tools/`、`worktrees/`、`Ohmybrain/`、`ohmybrain-core/` 等项目根，避免脚本、Obsidian 链接、worktree、历史 wiki 引用失效。

`index.md` 页面总数更新为 107。`lint_wiki.py` 待本轮全部模板/目录补齐后统一运行。

---

## [2026-06-09] maintenance + new-project | 入会自检一致性审计：补登 3 新项目 + 计数 67→77 + ADR-021~023

入会自检（memory `feedback_ohmybrain_self_improvement`）。P0/P1 发现：上次自检 2026-06-01 后 8 天派生了 **3 个新项目**，但 commit `6e4fedf`（2026-06-04）**只**把它们注册到 Hub `CLAUDE.md` 映射 + `projects/` 导航卡，**未**同步 dashboard / system-overview / decision-log / roadmap / memory-index / 各处计数。ultracode 模式下用 workflow 系统审计（6 cluster 并行 → 逐 cluster 对抗验证，12 agent）对照权威源（`D:/Claude/CLAUDE.md` + `MEMORY.md` + 实时文件系统），产出 **56 处已验证 finding**（36 high / 14 med / 6 low），主会话代写修复。

**3 新项目补登**（new-project 类，2026-06-04 commit `6e4fedf` 实际注册，本次补齐全部 Hub 视图）：
- **VisioForge** 🔒（2026-06-02，DocProcess，派生自 template-document，DEPENDS_ON 无）—— 通用 Visio 出图工作区，复用全局 flowgen-* 8 skill；自建 `scripts/replica_lib2.py`（Visio 动态直角连接器 `GlueTo(PinX)` + 真圆柱 4 段组合），首批 6 张 SN 效能预报图 1:1 复刻；git init -b main 首 commit 未提交。memory `project_visioforge_init`。
- **SonarSim** 🔒（2026-06-03，TechReq，派生自 template-engineering，无依赖）—— 主动声呐界面仿真（MATLAB App Designer 显控台 + 探测链路）；SPEC-001 已实现跑通（单发同频干扰混响强度图，11 个 .m，T1-T4 单测过）+ 2026-06-04 接声呐方程绝对定标 + 18km 长程场景归档；已 commit+push 内网 gitlab `lilin/SonarSim`。memory `project_sonarsim_init`。
- **CooperativeASW** 🔒（2026-06-03，DocProcess，派生自 template-document，DEPENDS_ON=UWAprojDoc）—— UWAprojDoc「编队协同探潜配置仿真与效能评估分系统」单列细化成 standalone docx（17 章 223k 字 + 24 图 + 969KB/100 页）；2026-06-04 图件大改催生 `archmap_interface.py`（I 族接口图）skill；commit `f46b16d`+`5da5de1` 本地未 push。memory `project_cooperativeasw_init`。

**计数对齐 CANON @2026-06-09**：memory **67→77**（project **43→52** / feedback **20→21** / user 1 / reference 3）波及 dashboard 规模快照 / hub-as-brain CANON 表 + 8 类职责表 / anti-patterns / memory-index / conventions §0 / index.md。活跃项目 **14→17**（system-overview）；wiki 内容页保持 **104**（3 项目皆 🔒/Tools，不进 Hub 公开内容页）。

**ADR-021/022/023 新增**（decision-log，最新在上）：ADR-023 CooperativeASW / ADR-022 SonarSim / ADR-021 VisioForge；起点声明 + 4 页范围标注 `ADR-001~020`→`ADR-001~023` 级联同步（decision-log / ecosystem-dashboard ×2 / hub-as-brain ×2 / conventions ×2）。roadmap 里程碑补 3 行（06-02/03）+ system-overview 演进里程碑补 4 行（05-25/05-29/06-02/06-03）。

**stale 锚点刷新**：dashboard UWAcomm_usbl `2026-05-22/50bec65`→`2026-06-07/c6d608e`（pooldata 实测 DOA 线，CBF 优于 TDOA）；FlowGen `🟡 未实装/2026-05-13`→`🟢 活跃/2026-06-04 archmap 族扩展`。memory-index 补 9 project（UWAcomm_usbl 8→13 + Tools 6→7 + 新 3 项目组）+ 1 feedback（`feedback_matlab_interactive_figs`）+ 新增「USBL 实测 DOA / 阵列校准」cross-cutting 主题。

**遗留（surface 给用户裁决，未自行改动）**：① Patents 🔒（无 git）在 `D:/Claude/CLAUDE.md` 列出，但 Hub CLAUDE.md 映射 + dashboard 未登记（system-overview / conventions §9 已含）—— 是否补登统一口径待定；② conventions §10 worktree 表 4 行 vs 根 `D:/Claude/CLAUDE.md` 3 行（缺 `UWAcomm_usbl-calibration`），根文件补登待用户授权（沿 2026-05-31 遗留观察）；③ FlowGen archmap 族是否单列独立 ADR 待定。

`lint_wiki.py` 待跑。**本批未 commit**（git 操作待用户授权，memory `feedback_git_confirmation`）。

---

## [2026-06-01] maintenance | 入会自检 P0 pass — 无改动

进入 Hub 起手自检（memory `feedback_ohmybrain_self_improvement`），用户选轻量收尾。

**P0 核对**：
- `log.md` 最新 = 2026-05-31 C 阶段（修正 50 处残留 stale + ADR-020 + AnthropicPPT 入册），**已 commit `e23f7de`，工作区干净**——上条 entry 末尾"本批仍未 commit"为当时快照，后续已授权提交（历史 entry 不改）。
- `MEMORY.md` 末尾与 wiki 同步（flowgen-archposter 2026-05-30 / m8-layered-replica 2026-05-29），无日期缺口。
- `roadmap.md` P0「8 dedicated 页填充」8 项全 ✅，焦点已转 P1。

距上次自检 1 天，无残留需修。本次仅记此 entry 保留连续性，无其他改动。

---

## [2026-05-31] maintenance | 入会自检 C 阶段：workflow 审计修正 50 处 2026-05-29 残留 stale + ADR-020

承接 2026-05-29 B 阶段（8 dedicated 页并行填充，其 log 自承"并行各 agent 互不知情引入新一批 stale"）。ultracode 模式下用 workflow 系统性审计 + 主会话代写修复。

**触发**：入会自检（memory `feedback_ohmybrain_self_improvement`），P0/P1 自检发现 2026-05-29 整批仍未 commit + 多处残留不一致。

**审计编排**：1 个后台 workflow，8 cluster 并行审计 → 逐 cluster 对抗式验证（16 agent / 158 工具调用），对照权威源（`D:/Claude/CLAUDE.md` 项目清单 + `MEMORY.md` + 实时文件系统 + git log）。产出 **50 处确认问题**（30 high / 16 med / 4 low，候选 53 经验证去伪 3）。

**修复（13 文件）**：

- **计数对齐 CANON @2026-05-31**：memory **63→67**（project **39→43**，索引 64→67 行）波及 dashboard / hub-as-brain（CANON 表 + 8 类表）/ anti-patterns / memory-index / conventions callout；wiki 页数 **86→104** / 活跃项目 **9→13** / 脚本 **19→22** / 项目导航 **10→13**（system-overview）。
- **roadmap**：P0「8 dedicated 页填充」8 项全部 `[ ]`→`[x]`（2026-05-29 已做却未勾）+ 里程碑表补 2026-05-29 行（IconForge 派生 + B 阶段）。
- **IconForge（2026-05-29 派生）补登**：dashboard Tools 段 + system-overview 项目表/ASCII 导航 + Hub/根 `CLAUDE.md` 映射 + README 派生树 + memory-index Tools 系（3→6，含补 orphan）。
- **ADR-020 新增**（decision-log）：IconForge 项目派生；起点声明 + 6 页范围标注 `ADR-001~019`→`ADR-001~020` 级联同步。
- **stale 交叉引用**：decision-log ADR-016 错引 `ADR-013`→`ADR-007`（SC-FDE 突破）；UWAprojDoc dashboard/memory-index 锚点 2026-05-22→**2026-05-29 C1-C6**（commit ad59ef8）；conventions §10 补 calibration worktree 行 + `V0.4→V0.x`；坏 wikilink `single-root-cause-audit`→`decision-log`；Hub CLAUDE.md `H:\UWAcomm`→`D:\Claude\TechReq\UWAcomm` + 补 3 DocProcess 项目。
- **memory-index 组求和调和**：既有 off-by-one（UWAcomm_usbl 标 7 实 8）修正；新增 4 条 project（iconforge / archposter / m8_layered_replica / uwaprojdoc_2026-05-29）使组合计 = 43。
- **MEMORY.md orphan 补索引**：`project_flowgen_m8_layered_replica.md`（磁盘有 / 索引漏）补一行，使 disk 43 = 索引一致。

**AnthropicPPT 跨源不一致 → 已裁决（用户选 a：补入权威源）**：AnthropicPPT 原在磁盘 + memory + Hub dashboard/README，但缺失于 `D:/Claude/CLAUDE.md` 项目清单（projects/ 亦无 nav card）。审计判定为跨源不一致并 surface，用户裁定其为正式 Tools 项目 → 补入 `D:/Claude/CLAUDE.md` Tools 区 + 建 `projects/anthropicppt/README.md` nav card + Hub 各处回填一致（活跃项目 13→**14** / Tools×2→×3 / system-overview 项目表+ASCII / three-tier + project-types 例 / Hub CLAUDE.md 映射）。

> **遗留观察（未动，仅记录）**：`D:/Claude/CLAUDE.md` Worktrees 表仅 3 行，缺 `worktrees/UWAcomm_usbl-calibration`（已据 memory `feedback_uwacomm_usbl_worktree_ownership` 补入 conventions §10）；该根文件补登待用户授权。

`lint_wiki.py` ✓ / `dashboard_snapshot.py` 实时核对全绿 / 页面总数不变 104（纯内容修正）。**本批 + 2026-05-29 B 阶段整批仍未 commit**（git 操作待用户授权，memory `feedback_git_confirmation`）。

---

## [2026-05-29] maintenance | 入会自检 B 阶段：8 dedicated 页填充 + 跨页事实同步 + ADR 扩充

承接 2026-05-24 建的 8 dedicated 页骨架，ultracode 模式下用 workflow 并行填充 + 跨页事实校正。

**触发**：入会自检（memory `feedback_ohmybrain_self_improvement`）。先并行审计 8 页完整度（平均 67%，32 处过期事实），再并行填充。

**8 页填充**（各页 updated → 2026-05-29）：
- `concepts/anti-patterns` 55% → 新增「首次触发事件」列 + 遍历 20 条 feedback 补全 + 新增协作边界/文档/agent 工具链三类反模式
- `architecture/decision-log` 45% → 补 12 条历史 ADR（ADR-008~019），全表按日期序重排，**编号 ADR-001~019 连续**
- `topics/ecosystem-dashboard` 55% → 数据刷新 + 各项目 session/HEAD 锚点 + 落地 `scripts/dashboard_snapshot.py`
- `topics/harness-resources` 70% → skills 本地 31/注入 90+ 两层 + agents 55 全列 + rules 15 目录
- `architecture/conventions` 78% → §10 worktree 5 行归属映射表 + §9 私人项目扩到全部 🔒 + 脱敏 promote 5 步
- `topics/memory-index` 75% → 计数精确(63) + 补 5 条新增 + cross-cutting 主题 3→7
- `concepts/workflow-glossary` 80% → 补算法领域名词组 + CC 协作术语 + flowgen 8 子 skill
- `architecture/hub-as-brain` 75% → 状态/roadmap 改「8 页已填充」+ CANON 权威计数表

**跨页事实同步（CANON @2026-05-29）**：feedback 20 / memory 63 / 本地 skills 31(注入 90+) / agents 55 / rules 15 目录 / scripts 22 / wiki 106(104 内容页)。修正多页「60+/90+」过期计数。

**ADR 重编号波及修复**：decision-log 改日期序 ADR-001~019 后，roadmap 里程碑表 4 处错位编号（007→018 / 006→017 / 005→007 / 004→005）+ 5 页「ADR-001~007」范围标注全部对齐为 ADR-001~019。这是并行填充各 agent 互不知情引入的新一批 stale，后置核验抓到。

**新增脚本**：`scripts/dashboard_snapshot.py`（共 22 个 .py），统计 wiki/scripts/skills/agents/rules/memory 规模输出 markdown 表，供 dashboard 手动对齐。

**编排**：3 个后台 workflow（审计 8 agent + 填充 8 agent），主会话代写落盘（subagent Write 受限 + wiki hook 需主会话触发，memory `feedback_subagent_write_permission`）。

`lint_wiki.py` ✓ / 页面总数不变（纯内容填充）。未 commit。

---

## [2026-05-25] new-project | DigitalTwin1plusN 派生

DocProcess 类私人子项目第 6 个（依次：Pricing / UWAprojDoc / CooperativeDetection / PaperReview / DigitalTwinGuide / **DigitalTwin1plusN**），「1+N」水下集群数字孪生体系方案撰写工作区。

**关键事实**：
- **主交付物**：《「1+N」水下集群数字孪生体系方案》—— docx 方案/报告，回答"1 中心 + 24 节点的数字孪生体系怎么搭、孪生什么、孪生到什么粒度"
- **体系构成**：1 艘百吨级大 U（指挥/通信中继/任务规划/数据汇聚枢纽）+ N=24 艘 1 吨级小 U（探测/扫描/编队/分布式作业）
- **孪生维度**：本体孪生（单艇平台/部件级）+ 集群孪生（编队/通信网络/任务协同/态势感知）**双层并行**
- **关联姊妹**：[[../../../DocProcess/DigitalTwinGuide]]（方法论指南，可参考但不形式化依赖；本项目专注「1+N」实例化）
- 派生自 `ohmybrain-core/template-document/`（首例采用"三模板拆分"后 document 模板的 DocProcess 子项目），HEAD=e97b8c2，main 分支（SOP §3 main 约定首例）

**Hub 影响**：
- `projects/digitaltwin1plusn/README.md` 已就位（项目导航卡片，标注 🔒 私人项目硬约束）
- DigitalTwin1plusN 不进 Hub 公开 wiki（私人 DocProcess 系），方法论结论沉淀走 `<private>` 标签或私人区域
- raw/ 全空待投入种子；后续 spec 起稿待用户投料

---

## [2026-05-25] maintenance | 入会自检数据同步

按 memory `feedback_ohmybrain_self_improvement` 约定执行入会自检，发现并修复 3 项数据不一致：

- **孤儿页补注册**：`concepts/vsdx-reverse-engineering-workflow.md`（2026-05-10 建立但从未注册 index.md），加入 Concepts 段（紧跟 skill-layered-resources）
- **ecosystem-dashboard 规模快照刷新**：日期 2026-05-24 → 2026-05-25；wiki 页数 67 → **104**；分类细分由 "18 concepts + 8 entities + 31 source-summaries + 1 topic + 5 architecture + 4 exploration" 修正为 "20 concepts + 8 entities + 11 architecture + 5 topics + 4 explorations + 31 source-summaries + 25 mcp-entities"
- **index.md 头部描述修正**：原描述 "ingest Anthropic Founder's Playbook v3" 是 2026-05-22 的事件、与同步日期 2026-05-25 不匹配，改为本次自检事由

`scripts/sync_index.py` 同时把页面总数从 89 → 104（之前未及时同步 2026-05-24 三仓哲学澄清 + dedicated 页扩展）。

`python scripts/lint_wiki.py` 由"1 个孤儿页"转为 ✓ 通过。

---

## [2026-05-24] sync-to-core 首次实战 | Q-003 wiki-ingester 下沉

`/sync-to-core` 命令 2026-05-24 早间建立后第一次实战使用。

**处理**: Q-003 wiki-ingester agent 契约

**评估其他 high priority**:
- Q-001 check_index_log_sync.py: Hub vs core diff 40 bytes (EOL 差异)，trivial **skip**
- Q-002 check_private_tags.py: Hub vs core diff **空**，已 in sync 跳过
- Q-003 wiki-ingester.md: core 不存在 → **CREATE** ✓ 本次
- Q-004 ~/.claude/rules/common/llm-wiki.md: **REJECT** — source 是 deprecated 占位（已迁移到 skill），core 那份是活规则方向错

**Q-003 实施**:
- cp `D:\Claude\Ohmybrain\.claude\agents\wiki-ingester.md` (8734 bytes)
- 加到 3 个模板（knowledge.ingest 跨类型通用）:
  - `template-engineering/.claude/agents/`
  - `template-document/.claude/agents/`
  - `template-tool/.claude/agents/`
- ohmybrain-core commit `4902412` (3 files, 558 insertions)

**Queue 更新**: Q-003 从 pending 移到"已下沉历史"段，记录 commit 4902412

**首次实战教训**:
- queue 中候选**先 diff** 才知道真假需要 sync（4 个 high priority 实际只 1 个真需要）
- 3 模板拆分后 cp 目标需要 1→3 扩展，knowledge 通用类型默认全加
- 命令 8 步流程清晰可用 ✓

---

## [2026-05-24] implementation | ohmybrain-core 三模板拆分**已实施**

承接早间 project-types.md 设计，授权后实施 ohmybrain-core 仓拆分：

**ohmybrain-core commits**:
- `a560fef` feat: autonomous-new-project-workflow 落地 + GitLab 迁移辅助（pending 改动先 commit）
- `247986a` feat: 三模板拆分 — engineering / document / tool（189 文件 / +6039 行）
- 已 push gitlab/main

**拆分结果**：
- `template-engineering/` (原 template/，git mv 保留 history) → 派生到 `TechReq/`
- `template-document/` (新建，workflows/document/ 4 步 + output/ 占位 + 私人强调) → 派生到 `DocProcess/`
- `template-tool/` (新建，workflows/tool/ 5 步 + templates/ + output/sample/) → 派生到 `Tools/`

**Hub wiki 同步**：
- `wiki/architecture/three-tier-architecture.md` 加 § core 三模板段
- `wiki/architecture/system-overview.md` 三仓 ASCII 图更新（含 template-engineering / -document / -tool）
- `wiki/architecture/project-types.md` 实施记录段（待实施 → 已实施）

**已派生项目**（UWAcomm / UWAprojDoc / FlowGen / AnthropicPPT 等）**不受影响**，他们已 cp 走独立演化。新项目派生直接选对应模板。

---

## [2026-05-24] architecture | 三类项目模板设计（待 ohmybrain-core 拆分实施）

User 反馈：项目实际分 3 类（开发 / 文档 / 工具），当前 core 只有 1 个通用模板，派生后各项目自行注释"哪些不用"。

**新加 1 个 wiki 页**：
- `wiki/architecture/project-types.md` — 三类项目识别 + 对比表（目录/工作流/skill/hooks/commit 风格）+ 文档撰写闭环（spec → draft → validate → archive）+ 工具开发闭环（design → implement → test → register-skill → docs）+ ohmybrain-core 拆分 plan

**设计决策**（待 user 授权动 ohmybrain-core 仓后实施）：
- 现 `ohmybrain-core/template/` → 改名 `template-engineering/`
- 新建 `ohmybrain-core/template-document/`（删 src/tests/evals + 加 output/ + 改 CLAUDE.md）
- 新建 `ohmybrain-core/template-tool/`（删 tests/evals + 加 templates/ output/sample/ + skill 注册流程）
- 派生命令变 `cp -r template-<type>/ → 新项目`，零调整开始

未实施时机：等 user 授权动 ohmybrain-core 仓。

---

## [2026-05-24] mechanism | Hub → core 同步机制 + `/sync-to-core` 命令

延续 hub-as-brain 通道 3 (core template 延迟下沉)，明确"Hub 怎么去帮忙更新 ohmybrain-core"的机制。当前现状是**手动同步散在 user 头脑中没清单**。

**新加 2 个 wiki 页**：
- `wiki/architecture/core-update-mechanism.md` — 同步机制详细规约：什么下沉（通用 skill/hook/rule/workflow/结构/CLAUDE.md）/ 什么不下沉（Hub 专属/项目特化/私人/含 secrets）/ 触发信号（≥ 2 项目验证 / ADR 标 downstream / review 决议 / 哲学澄清）/ 候选标记方式（frontmatter / inline 注释 / queue 页）/ 同步步骤（手动 6 步 + 半自动 /sync-to-core）/ 安全约束
- `wiki/topics/core-update-queue.md` — pending 队列（12 candidate 含 high/medium/low priority + 反例 4 条 + 评估标准 + 维护节奏）

**新加 1 个命令**：
- `.claude/commands/sync-to-core.md` — `/sync-to-core` Hub 专属命令：8 步流程（读 queue / 选 candidate / 比对 diff / 安全检查 / 生成 commit msg / 等授权 / apply / 更新 queue）

**关联**：
- 与 `/ingest`（raw → wiki）和 `/promote-answer`（项目 → Hub）构成"知识三段流"
- 通道 3 现在有明确实现路径，不再"散在 user 头脑中"
- user 反馈"Hub 怎么去更新 core" 的直接回应

---

## [2026-05-24] architecture | Hub 大脑功能 8 gap 补强（dedicated 9 页框架）

延续早间的三仓 + 双闭环加强，user 反馈深层问题："Hub 没起到大脑作用，有信息遗漏"。识别 8 类散在各处的关键信息，建立 1 + 8 = 9 个 dedicated 页框架：

**顶层入口**：
- `wiki/architecture/hub-as-brain.md` — 大脑功能定位：8 类 gap + 设计原则（SSOT / 索引-时序-详情三层 / 反馈式更新 / 与 core 边界）+ 优先级 + roadmap

**8 个 dedicated 页骨架**（含种子内容，详细填充见 [[roadmap]] P0）：
- `wiki/concepts/anti-patterns.md` — 跨项目反模式合集（feedback_* 60+ 条提炼，按阶段 Research/Build/RCA/Promote/全阶段分类）
- `wiki/concepts/workflow-glossary.md` — 工作流术语表（V→V→V / PMF / 单根因审计 / archive / promote 等 + 算法研究 + Claude Code 协作术语）
- `wiki/topics/ecosystem-dashboard.md` — 跨仓状态快照面板
- `wiki/architecture/decision-log.md` — ADR-style 决策记录（含 7 条历史 ADR）
- `wiki/architecture/conventions.md` — 10 类跨项目约定（命名 / 目录 / commit / 工作流 / Hooks / Worktree / 私人项目）
- `wiki/topics/harness-resources.md` — Hooks + Skills + Rules + Agents + MCP 全景索引
- `wiki/topics/memory-index.md` — auto-memory 60+ 条按类型 + 主题聚合
- `wiki/architecture/roadmap.md` — 18 月里程碑 + P0/P1/P2/P3 roadmap

**关联**：
- 触发源：本次 PPT 编制 + 哲学澄清后 user 进一步反馈
- 后续：roadmap P0 详细化各页（持续）
- memory `project_anthropic_ppt_init` 已记录该项目派生背景

---

## [2026-05-24] architecture | 三仓哲学澄清 + 双闭环 dedicated 页

PPT 编制过程暴露 Hub wiki 三仓结构 + 双闭环描述不清，需查 `ohmybrain-core/template/workflows/` 才搞清楚。本次做 3 件事：

**新加 2 页**：
- `wiki/architecture/three-tier-architecture.md` — 哲学澄清：**Hub = 大脑·主动**，**project = 需求牵引·业务驱动**，**ohmybrain-core = 被动模板**（被 Hub 更新）。明确 core 不是"源头"而是"成熟模式打包供新项目复用的副本"。数据流向：project → wiki 反馈 → Hub → 更新 template/ → core → 新项目派生。
- `wiki/architecture/dual-loop.md` — knowledge 闭环 4 步（ingest / query / promote / review）+ engineering 闭环 4 步（spec / plan / implement / validate）+ 跨闭环触发关系完整 ASCII 图。module-design 明确归 phase 0 不算闭环内。

**修 1 页**：
- `wiki/architecture/system-overview.md`
  - 顶部"定位"加哲学说明，引用 [[three-tier-architecture]]
  - 知识闭环表加 review 第 4 步
  - 开发闭环从模糊"0-5 阶段"改为明确"4 步 + phase 0 module-design"

**关联**：触发源为 `D:\Claude\Tools\AnthropicPPT` 编制 V4 PPT 时发现 system-overview 描述与 core 不一致。

---

## [2026-05-23] new-project | AnthropicPPT 派生（log 补登）

Tools/AnthropicPPT 从 CC算法开发-v4 PPT 沉淀派生（2026-05-29 自检补登此前缺失的 log entry）。

- 主交付：Anthropic FIELDBOOK 风 PPT 模板（python-pptx，16:9，纸张色 + 铁锈红 严肃中英混排）
- 含 design_tokens + 8 helpers + 9 layout + skill `anthropic-ppt`（关键词触发 PPT/幻灯片/演讲/slides/pptx）
- memory `project_anthropic_ppt_init`；对应 [[decision-log]] ADR-017
- Hub 影响：仅 [[ecosystem-dashboard]] / [[roadmap]] 引用，无新 wiki 内容页

---

## [2026-05-22] ingest | article：The Founder's Playbook v3 (Anthropic, 2026)

Anthropic 官方 marketing playbook ingest 到 Hub：36 页 / 7 章，"AI-Native 创业"四阶段（Idea/MVP/Launch/Scale）+ 三表面（Chat/Cowork/Code）方法论。**对水声研究者不直接 actionable，但 5 条工程方法论可迁移**（CLAUDE.md as architectural memory / devil's advocate as default / scope doc 写"deliberately does not do" / 三表面分工 / Sean Ellis 40% PMF test）。

- 新建 source-summary: `wiki/source-summaries/anthropic-2026-founders-playbook.md`
- 更新 cross-ref（3 处，仅追加 wikilink 行）：
  - `wiki/entities/claude-code.md` § 来源
  - `wiki/concepts/subagents-orchestration.md` § 来源
  - `wiki/architecture/memory-stack.md` § 相关页面（独立 validation L2 层）

更新 index.md（页面总数 88 → 89）。

inline 路径执行（用户选）；按默认协议 ≤200 行 + ≤5 cross-ref + 仅追加 wikilink，未新建 concept/entity，未改写已有段落。

---

## [2026-05-16] backfill | UWAcomm + UWAcomm_usbl session（log 补登）

2026-05-29 自检补登 2 个 skip-or-log-only 缺口（项目侧 session 快照，详见 memory，不复述细节）：

- **UWAcomm**：rx_stream_p4 接口移植（claude worktree 4 commit `d74c0a2`+`3d6d0b5` 未 push）+ 双回归 RCA（test 1+2 algo A FAIL / test 5 fd=1Hz 50% 回归 vs `a291af4`）；对应 [[decision-log]] ADR-016
- **UWAcomm_usbl**：_v2 反向 diff 锁定用户唯一改动 §A.6 → 折中 7 列 + 8 步 build pipeline 生 _v3.docx

---

## [2026-05-13] new-project | DigitalTwinGuide 派生

DocProcess 类私人子项目第 5 个（依次：Pricing / UWAprojDoc / CooperativeDetection / PaperReview / **DigitalTwinGuide**），数字孪生项目实施指南撰写工作区（方法论文档型）。

**关键事实**：
- **主交付物**：《数字孪生项目实施指南》—— 回答"数字孪生项目怎么做"的方法论文档
- **首份种子材料**：`raw/notes/20吨级AUV数字孪生体系构建与运行支持技术课题指南.md`（25 KB / 233 行）
- **首版 docx**：宋体版完成，4 步 pandoc pipeline（normalize / pandoc / three_line / clean_indent）固化在 `.tmp/`
- **样板 reference**：AUV 课题指南种子 + 多智能体样板
- **覆盖范围**：希望同类水下平台 / 装备数字孪生课题可复用
- 派生自 `ohmybrain-core/template/`，HEAD 63 init（docx 仍 stage 未 commit）

**Hub 影响**：
- `projects/digitaltwinguide/README.md` 已就位（项目导航卡片，标注 🔒 私人项目硬约束）
- `CLAUDE.md` 项目仓库映射追加 1 行
- DigitalTwinGuide 不进 Hub 公开 wiki（私人 DocProcess 系），方法论结论沉淀走 `<private>` 标签或私人区域

---

## [2026-05-09] new-project | PaperReview 派生

DocProcess 类私人子项目第 4 个（依次：Pricing / UWAprojDoc / CooperativeDetection / **PaperReview**），学位论文外审工作区。

**关键事实**：
- 「英文」语义注：项目名 PaperReview 本身是英文，但**材料语言**为中文——评审意见也用中文撰写
- HEAD b3568f6 / 手动模式（非闭环）
- 当前在评水声专硕一份

**Hub 影响**：`projects/paperreview/README.md` 已就位（项目导航）。Hub 不收任何评审材料原文（私人项目硬约束）。

---

## [2026-05-03] tool | flowgen-vsdx skill M5 升级 — PPT 风格高级模板

`~/.claude/skills/flowgen-vsdx/` 升级 M5 模式：

- 新增 `templates/ppt_business_flow.py` — 用于复杂业务架构图
- 覆盖模式：多分支扇出 / 共用基础设施 / 双反馈环 / 旁路 / 路径外 label
- M4 默认 GraphViz 自动布局保留作简单图回退

**跨项目可复用**：UWAprojDoc 等方案文档场景已开始用 M5；其他项目方案文档可直接接入。flowgen 5 skill 决策树见 `~/.claude/skills/flowgen*/SKILL.md`。

**配套约定**（memory `feedback_uwaprojdoc_flowgen_only` + `feedback_doc_visual_diversification`）：方案文档流程图必须走 flowgen* 5 个 skill 之一，禁止 matplotlib mock / 手画 SVG；图的视觉必须按业务真实结构匹配模式（线性/并行/反馈/扇出/汇聚），决策文案必须业务化。

---

## [2026-04-28] new-project | UWAprojDoc 派生

DocProcess 类私人子项目第 2 个，水声项目某专项方案技术文档撰写工作区。

**v0 docx 完整落地**（派生当日同步完成）：
- 4.8 MB
- 8 分系统 33 模块独立小节
- 60 张图含 33 模块流程图 5 模式竖向
- HEAD=48f4324

**后续进展**（2026-05-01）：
- 原型 ingest（HTML + PROJECT_SPEC）
- 5 wiki 页 + 业务流程/运用场景 7 议题（F1-F7）待决——框架定型后才落 `wiki/topics/`

**Hub 影响**：私人项目，材料不进 Hub。导航页可选（看用户是否要 `projects/uwaprojdoc/`）。

---

## [2026-04-25] new-project | UWAcomm_usbl 派生（内网 Internal）

TechReq/UWAcomm_usbl 完成 SOP 派生：水声通信 + USBL 联合定位/通信仿真，依赖 UWAcomm + USBL 双源。

**关键事实**：
- 内网 GitLab Internal 可见（非公开）
- 混合模式（参考 UWAcomm + USBL 两路）
- 派生当日未实装代码

**后续进展（节选，详见 memory）**：
- 2026-04-25 SPEC-001 批 0+1 完成（M1 8 文件 70k 字 C 档），3 冲突待决
- 2026-05-06 项目范围定型：整机原型样机 / 总集成枢纽 / 3 人 / 5 月水池 PoC + 6 月海试 + 12 月国产化；Phase α 借厦大 + Phase β 双线替换
- 2026-05-11 双工作树归属约定（main=原窗口 / design/v1.x=design 修订）+ 硬件路径事实颠覆估时（VPX 已到位 / 哈工程软件无所有权 / UWAcomm 仅 MATLAB → α/β/γ/δ/ε 五选一）
- 2026-05-12 三件事并行（自研全链 PC+ATA-L8+iPotest / 哈工程整机 / 厦门 USBL）+ 距离 15m + CAGE5 5 元 + V0.7 大纲 2338 行 + SPEC-002 试验前预演 334 行

**Hub 影响**：`projects/uwacomm_usbl/README.md` 已就位。Hub 不收内部内容（Internal 项目硬约束）。

---

## [2026-04-19 ~ 2026-05-11] backfill | UWAcomm/USBL 23 天主线进展补帐

借 L3 `diff_memory_log.py` 工具补这段时间未及时沉淀的项目侧进展（Hub 视角时间轴，不复述 memory 详细记录）。

### UWAcomm 主线（11 个 session）

- **04-19** S1 E2E benchmark 完成（7 工具 + 11 runner）
- **04-24** SC-TDE V5.4 post-CFO fix（50%→0.29%）+ DSSS V1.2 audit（43%→0%，"单一根因"方法学）
- **04-25** V5.5 fd=1Hz iter R5 + V5.6 HFM-signature calibration 4/5 PASS；SC-FDE Phase 3b.2 软符号-BEM 鸡蛋耦合 4 路线 A/B/C/D 待决
- **04-26** SC-FDE 协议层突破 jakes fd=1Hz 50% limitation：pilot=128(=blk_cp) 47%→3.37%（**14×**）
- **04-27** SC-TDE 收尾 + OTFS 重启（撤销 04-21 skip，移植 codex rx_chain/spread-pilot/clip-PAPR）+ P4 scheme routing 4/4 PASS
- **04-28** P4 UI ↔ codex 对齐 + Jakes 接通 + RX α 符号 V6→V7 + α refinement 移植
- **05-01** P4 UI 稳定性 4 fix（51%→0%）+ V3.0 解耦 blk_cp/blk_fft + V4.0 预设（K=31 直接链路 0.68%）
- **05-03** UI 50% RCA H5 命中（jakes 假 α）+ Phase 3 P5/P6 整批移植（8 commit 27 文件已 push）
- **05-04** simple UI v2.0（tx/rx_simple_ui classdef + 4 模式 + 流式 chunk）+ jakes V2.0 passband-native（Hilbert+SoS）+ SC-FDE V4.1 高 SNR 修复（pass 50.23%→**0.43%** 117× / SNR=80 48.71%→0.53% 94×）+ 24/24 矩阵全 PASS
- **05-06** OTFS 4-27 漏登补登 + Phase 4 BER FAIL 归档（hann × 6 trial 全退化 +1.9~+14.8 pp，loopback 2.78e+01 vs rect 1.26e-15，**维持 rect 默认**）

### USBL 主线

- **04-25** H8 spec draft 落地，等用户答 D1-D4；H7 未起

### 跨项目教训（候选 promote，留待 /promote-answer 单独决策）

无日期 feedback 已分类（详见 `draft/log-draft-2026-05-12.md`）：
- UWAcomm `feedback_comp_resample_carrier_phase` — passband real time-scaling 等效反载波相位；baseband complex 需手动补偿
- UWAcomm `feedback_uwacomm_ui_ber_diagnose_order` — UI BER 异常先 diag 绕开 UI 链验算法
- UWAcomm `feedback_uwacomm_codex_compare_method` — BER 异常先 diff codex worktree
- UWAcomm `reference_otfs_pilot_tradeoff` — Impulse/ZC/Superimposed 三方案 PAPR-NMSE tradeoff
- 通用 `feedback_doc_visual_diversification` — 方案文档视觉差异化
- 通用 `feedback_uwaprojdoc_flowgen_only` — 流程图统一走 flowgen* skill

### Hub 影响

本次补帐只加 log entry，不新建 concept/source-summary。跨项目教训如需独立成 concept，由用户后续单独促发。页面总数不变（86）。

---

## [2026-05-12] refactor | D:/Claude 顶层目录大整理（方案 C）

执行用户授权的"方案 C"目录重组：18 顶层项 → 14 顶层项，精简 4。涉及 6 次 mv + 3 次 git worktree move + 全局 path 引用同步。

**移动操作**：
- `DocHub/` → `Archive/DocHub/`（2026-04-13 归档项目入归档容器）
- `worktrees/{usbl-redo,uwanet-redo}/` → `Archive/worktrees-redo/`（autonomous-workflow P1/P2 dry-run 产物）
- `open-design/` → `External/open-design/`（第三方 nexu-io/open-design fork，先 kill 占着的 dev server PID 34776+WINWORD×2）
- `scripts/migrate-to-gitlab.sh` → `ohmybrain-core/scripts/`（顶层零散脚本归位 + 删空 scripts/）
- `TechReq/UWAcomm-claude` → `worktrees/UWAcomm-claude`（`git worktree move`）
- `TechReq/UWAcomm-codex` → `worktrees/UWAcomm-codex`（`git worktree move`）
- `TechReq/UWAcomm_usbl-design` → `worktrees/UWAcomm_usbl-design`（PowerShell Move-Item + 手工修 .git/worktrees/.../gitdir registration）

**新增容器**（含 README 说明用途）：
- `Archive/` — 归档历史/dry-run/已取代项目
- `External/` — 第三方仓库（与个人项目隔离）

**新增 worktree 命名空间**：`D:/Claude/worktrees/` 集中 3 个活跃 worktree（UWAcomm-claude / UWAcomm-codex / UWAcomm_usbl-design），TechReq/ 只放 4 个主项目（USBL / UWAcomm / UWAcomm_usbl / UWAnet）

**path 引用同步**（C7）：
- `D:/Claude/CLAUDE.md` 项目清单重写为 4 分组（主项目 12 / Worktrees 3 / 工具周边 3 / 第三方与归档 3）
- `D:/Claude/AGENTS.md` 改为 `@CLAUDE.md`（Codex 与 Claude Code 单一事实源，零漂移）
- `D:/Claude/.claude/settings.local.json` 33 处 allowlist 路径替换（git -C / matlab -batch / cp 等命令）
- 5 个 memory 文件：feedback_uwacomm_{worktree_ownership,usbl_worktree_ownership,claude_branch_autonomous,codex_compare_method} + project_ohmybrain_ecosystem
- MCP graph：`~/.claude/memory/graph.jsonl` DocHub entity observations + Hub mcp-entities/DocHub.md 同步

**架构页同步**（A1 已含）：
- `wiki/architecture/system-overview.md` 项目实例表 4 → 10 + ASCII 树 + 演进里程碑加 04-21~05-12 events

**风险事件**：
- open-design dev server PID 34776 跑了 5 天（用户授权后 kill）
- 2 个 WINWORD 进程锁 docx（用户授权 Stop）
- PowerShell Move-Item 中途失败留半移状态，用 `cmd rd /s /q` 清残留

**未做**（follow-up）：
- 历史孤儿页 `concepts/vsdx-reverse-engineering-workflow.md`（与本次无关，保留）
- Ohmybrain `CLAUDE.md` 项目仓库映射只列 GitHub 映射 8 项目（私人/无 git 项目未列，按设计如此）

页面总数不变（88，纯路径同步无新建/删除）。

---

## [2026-05-12] promote | OTFS pilot tradeoff + MATLAB pitfalls 沉淀到 Hub

从 memory 跨项目可复用 reference/feedback 类挑出 2 条 promote 到 Hub source-summary：

**新建**：
- `wiki/source-summaries/uwacomm-otfs-pilot-tradeoff.md` ← memory `reference_otfs_pilot_tradeoff`（2026-04-14 UWAcomm 实测）
  - Impulse / ZC / Superimposed 三方案 PAPR-NMSE 对照表 + 物理解释 + 选型指南 + Superimposed SIR 公式
  - 适用范围：任何项目恢复 OTFS 时的 pilot 设计参考
- `wiki/source-summaries/matlab-pitfalls.md` ← memory `feedback_matlab_inf_bug`
  - 起点 pitfall：`inf` 字面量触发"double→struct"转换错误的 path 污染陷阱
  - 设计为生长性集合，后续累积 pitfall 时追加

**更新**：
- `wiki/concepts/ofdm-and-otfs.md` 来源段追加 `[[uwacomm-otfs-pilot-tradeoff]]`
- `wiki/index.md` Source Summaries 段加 2 行；页面总数 86 → **88**

**未 promote 的 3 条 candidate**（重审后归项目侧）：
- `feedback_uwacomm_path` — UWAcomm 路径事实（项目特定，不跨项目）
- `reference_uwacomm_obsidian` — UWAcomm debug-logs 位置（项目特定）
- `feedback_ohmybrain_workflow` — UWAcomm spec→plan→code 工序（Hub 全局 CLAUDE.md 已描述，UWAcomm 是应用案例）

---

## [2026-05-12] tool | scripts/sync_agent.py 防 wiki-ingester 双副本漂移

L1 修复后留下的同步债务一次性补上。

- **源头**：`.claude/agents/wiki-ingester.md`（项目本地，git 跟踪，契约权威）
- **镜像**：`~/.claude/agents/wiki-ingester.md`（全局，invocable handle）
- **机制**：SHA-256 比对。`--sync` 源→镜像；`--check` 漂移 exit 1 适合 hook；默认报告 + 修复指引

**接入 Stop hook**：`.claude/settings.json` Stop 段追加 `python scripts/sync_agent.py --check`，会话结束自动检查漂移（exit 0 同步 / exit 1 漂移 stderr 提示）。

**当前状态**：✓ 已同步（hash `6bd73309c569`）。

**未来场景**：编辑项目本地 wiki-ingester.md 后 Stop 时 stderr 提示 `python scripts/sync_agent.py --sync` 修复。

---

## [2026-05-12] doc | system-overview.md + CLAUDE.md hook 清单同步

架构总览页过期 25 天（updated 2026-04-17），CLAUDE.md hook 清单只列阻断型 3 个，本次一次性同步。

**system-overview.md**：
- 项目实例表 4 → **10 项目**：补 UWAcomm_usbl / UWAprojDoc / CooperativeDetection / PaperReview / FlowGen / usbl-s1（分 TechReq / DocProcess🔒 / Tools / 导航占位 四组）
- 目录 ASCII 树同步 10 个 projects/ README
- §Hub hooks 表 5 → **8 hook**（补 `check_private_tags` / `check_memory_log_gap`，加阻断/提醒/注入类型列）
- §当前规模：49 → **86 页** / 4 → **9 项目** / 17 → **19 scripts**
- §演进里程碑：补 04-21 ~ 05-12 共 7 个事件

**CLAUDE.md `§Hook Exit Code Strategy`**：阻断型 3 个清单 → 完整 8 hook 表（阻断 3 / 提醒 4 / 注入 1）。

---

## [2026-05-12] hook | scripts/check_memory_log_gap.py Stop hook 提醒沉淀缺口

新增 Stop hook `scripts/check_memory_log_gap.py`（~60 行，提醒型 exit 0），会话结束时自动检查 memory→Hub log 缺口：

- 复用 L3 的解析逻辑（INDEX_LINE_RE + DATE_RE）
- 只在"缺口最近日期 ≤ 7 天内"才提示（避免老欠账反复刷屏）
- stdout 一句话 + 跑 `diff_memory_log.py` 指令；exit 0 不阻断（Windows Terminal tab 友好）

**接入**：`.claude/settings.json` Stop hook 段追加为第 3 条（前两条：`check_index_log_sync.py` 阻断型 / `commit_reminder.py` 提醒型）。

**首次试运行**（手动 `python scripts/check_memory_log_gap.py`）：
```
[memory→Hub] 12 个日期 memory 有但 wiki/log.md 缺，其中 3 个在最近 7 天内（最近：2026-05-11）
  详情：python scripts/diff_memory_log.py --out draft/log-draft-2026-05-12.md
```

**与阻断型 hook 的边界**：memory→Hub 不是机械 1:1 转（session 摘要不必都进 Hub），强制阻断会误伤——所以选提醒型。决策权在用户。

---

## [2026-05-12] tool | scripts/diff_memory_log.py 批量回流缺口报告

新增脚本 `scripts/diff_memory_log.py`（~150 行）——对照 auto-memory `MEMORY.md` 与 Hub `wiki/log.md`，找出未沉淀到 Hub 的项目侧记录。

**逻辑**：
- 解析 MEMORY.md 索引行（`- [Title](file.md) — description` 格式，49 条）
- 提取日期：先 desc 抽 `YYYY-MM-DD`，fallback 从文件名抽（覆盖 `project_*_2026-04-23_session.md` 这种）
- 对照 wiki/log.md 已记录日期（H2 header）
- 按前缀分类建议动作：`promote-candidate` / `log-only` / `review` / `skip` / `skip-or-log-only`

**首次运行结果**（draft 写到 `draft/log-draft-2026-05-12.md`，gitignored）：
- memory 49 条 → 28 条带日期 + 21 条无日期
- Hub log.md 9 个日期 → **12 个缺口日期**（2026-04-19 ~ 2026-05-11，最近 23 天最严重）
- 缺口含：UWAcomm 6 session（04-24 ~ 05-06）+ UWAprojDoc（04-28 + 05-01）+ UWAcomm_usbl（04-25/05-06/05-11）+ PaperReview（05-09）+ flowgen-vsdx M5（05-03）+ USBL H8（04-25）

**用法**：
```bash
python scripts/diff_memory_log.py               # stdout
python scripts/diff_memory_log.py --out FILE   # 写到文件
```

**配套**：`draft/` 已加入 `.gitignore`。Draft 报告供用户审核，挑选后手工 merge 进 log.md / 走 `/promote-answer`。

**动机**：L1 修复了 `/ingest` 工序后，需要补 20 天历史欠账——但 memory→Hub 不是 1:1 转移（session 摘要不必都进 Hub，跨项目结论才进），脚本只产 draft + 分类建议，决策权留给用户。

---

## [2026-05-12] fix | /ingest 路径 B 工序修复（TODO 2026-04-22 关闭）

修复挂了 20 天的 `/ingest` 路径 B 工序，让 `wiki-ingester` agent 真正可调用：

- **迁全局**：`cp .claude/agents/wiki-ingester.md ~/.claude/agents/wiki-ingester.md` — 全局副本作为 invocable handle（项目本地版保留为契约源头 + git 跟踪点）
- **commands/ingest.md 路径 B 段重写**：加 "首选调用 + Fallback 内联契约 + 主会话代写后备" 三层兜底
  - 首选：`subagent_type="wiki-ingester"`（全局副本，2026-05-12 起可用）
  - Fallback：`subagent_type="general-purpose"` + prompt 内联 "Read `~/.claude/agents/wiki-ingester.md` 作为契约"
  - 后备：subagent Write 被拒时，agent 把完整 markdown 内联到报告，主会话 Glob 验证后代写落盘（2026-04-22 6 篇 doppler 实测 5/6 命中此后备）
- **未做**（遗留）：项目本地 vs 全局副本同步机制——目前手动双改，未来视漂移频率写 `scripts/sync_agent.py`

**动机**：过去 19 天（2026-04-23 后）Hub log.md 0 条新 entry，对比 memory 中 11 个 UWAcomm session + UWAprojDoc / UWAcomm_usbl / PaperReview / CooperativeDetection 等项目记录——`/ingest` 路径 B 失效导致沉淀工序高摩擦，本次先修工序基础设施，后续 L3 写批量回流脚本补 20 天历史欠账。

页面总数不变（纯基础设施修复，不涉 wiki 内容）。

---

## [2026-04-23] new-project | FlowGen 完整 SOP 派生

新项目 **FlowGen** 完整走完 `ohmybrain-core/docs/new-project-sop.md` §1-§6（手动模式，非闭环）：

- **§1 派生**：`cp -r D:/Claude/ohmybrain-core/template/. D:/Claude/Tools/FlowGen/`（保留了会话早前浅克隆的 `raw/repos/mermaid/` + 我手写的 `raw/repos/README.md`）
- **§1.5 补齐**：`mkdir -p specs/{active,archive} plans src tests evals`
- **§2 配置 CLAUDE.md**：替换占位符（slug=flowgen / 描述=需求→Mermaid 流程图 LLM 工具 / 分类=Tools/），增加 FlowGen 特有约束（单用户、无 UI、仅 flowchart、Claude API 核心、参考仓 mermaid-js）
- **§3 git init + 首 commit**：`init: 从 ohmybrain-core 模板初始化 FlowGen`；.gitignore 追加 `raw/repos/*/` 忽略外部参考仓
- **§4 注册 Hub**：新建 `projects/flowgen/README.md`，更新 Hub CLAUDE.md 项目映射表 + 根 `D:/Claude/CLAUDE.md` 项目清单（加 Tools/ 分类）
- **§6 验证**：dirs OK / 占位符 OK / `lint_wiki.py` + `validate_task.py` 双通过

**分类新增**：首个 `D:/Claude/Tools/` 下项目。区别于 `TechReq/`（算法研究）+ `DocProcess/`（文档处理）。未来跨项目工具都放这里。

**后续工作不在本 Hub 会话进行** — 用户将在 FlowGen 项目 Claude Code 会话内起 spec / plan / M1 MVP 实施。

---

## [2026-04-23] ingest | mermaid-js/mermaid 代码仓（FlowGen 项目参考源）

通过 `/ingest` 路径 B（`general-purpose` agent 替身 + 内联 wiki-ingester 契约）把 mermaid-js/mermaid 代码仓摄入到 Hub：

- **新建 source-summary**：`wiki/source-summaries/mermaid-js-mermaid.md` — Knut Sveidqvist 2014+ 维护的 JS 图表渲染器，MIT，monorepo × 8 package × 27 图类型，v11.14.0 核心
- **cross-ref**（只追加 wikilink，严守默认预算）：
  - `wiki/architecture/memory-graph.md`「相关页面」段 — 本页两张图谱就用其 `flowchart LR` DSL
  - `wiki/entities/obsidian.md`「来源」段 — Obsidian 原生 Mermaid 预览
- **未执行的提案**（等主会话决策）：
  - 新建 concept `diagram-as-code`（归纳 Mermaid / PlantUML / D2 / Graphviz DSL 族通性）
  - 新建 concept `visual-regression-testing`（Argos 截图 diff 模式）
  - 派生 concept `diagram-orchestration-pattern`（Mermaid detectType + loadDiagram 调度器，可迁移 FlowGen 核心）

**源路径特殊说明**：raw 在 `D:/Claude/Tools/FlowGen/raw/repos/mermaid`（FlowGen 项目 raw/，**不在 Hub raw/**）— 因 FlowGen 项目未完整派生，只起了 raw/repos/ 骨架就先摄入，Hub 侧直接跨目录读取源仓。符合"Hub 收录跨项目参考"职能。

**agent 调用模式**：本次 subagent 的 Write/Edit 全部一次通过（无需主会话代写 fallback），是近期少见的 subagent 权限全绿。

**页面总数**：84 → 85。

---

## [2026-04-23] MCP graph 扩展 | 新增 Ohmybrain 生态图谱（A 图）

MCP knowledge graph 从单主题（UWAcomm α 补偿栈）扩展为双主题：

- **图谱 A — Ohmybrain 生态**（8 实体 + 11 关系）：ohmybrain-core / Ohmybrain / UWAcomm / USBL / UWAnet / Pricing / DocHub / calendar。关系含派生 / 知识回流 / template 反哺 / projects 导航 / 已被取代
- **图谱 B — UWAcomm α 补偿栈**（17 实体 + 23 关系，2026-04-23 早已建，无改动）

**共享节点**：UWAcomm + Ohmybrain 在两图均出现，通过累加 observation 承载两视角（不建双节点）。方案 A（同节点加观测）落地。

**落地产物**：
- MCP graph 23 实体 + 34 关系（`~/.claude/memory/graph.jsonl`，56 行）
- `wiki/mcp-entities/` 更新：17→23 个 entity 笔记（+`ohmybrain-core` / `USBL` / `UWAnet` / `Pricing` / `DocHub` / `calendar`）
- `architecture/memory-graph.md` 重写：双主题结构，两张 Mermaid + 共享节点段
- index.md 追加 6 个 Repo / Ecosystem 条目

**页面总数**：78 → 84（+6 entity）。

**⚠️ 技术债**：MCP server 当前仍写 npx cache（`AppData/Local/npm-cache/_npx/`），因 `MEMORY_FILE_PATH` env 改动需要 Claude Code **重启**才生效。本次通过 `cp` 手动同步 npx cache → 稳定路径，**下次重启后自动走稳定路径**。

---

## [2026-04-23] 记忆栈补齐 | user 画像 + Git 红线 + Session Bootstrap

记忆栈审查发现 3 个空白，全部补齐：

- **auto-memory `user_profile.md`** — 首条 user 类记忆，结构化画像（身份/技术栈/环境/语言/工作风格/协作偏好）
- **auto-memory `feedback_git_confirmation.md`** — 明文化 Git 破坏性操作红线，列 🔴 必授权 / 🟢 可直接 / 授权信号 / 永久红线四段
- **wiki `memory-stack.md` 新增"新会话 Bootstrap 清单"节** — 自动加载层 / 按任务触发读取 / 启动自检三段，加速 context 压缩后的重启

**MEMORY.md** 追加 2 条索引（current 18 条，+2）。

---

## [2026-04-23] MCP graph wikilink 投影（17 实体笔记 + 1 索引）

新增 `wiki/mcp-entities/`（18 `.md`），把 MCP 知识图谱投影为 Obsidian wikilink 网络，供 **Juggl / Extended Graph / 原生 graph view** 可视化。每个 entity 一篇，frontmatter 带 `type` + `cssclass: type-<type>`（按 project / hub / scheme / technique / paper 分类），`[[wikilink]]` 互链体现 in/out 关系。

**新增脚本**：`scripts/generate_mcp_entities.py` — 从 `C:/Users/zazn/.claude/memory/graph.jsonl` 读 MCP graph 自动生成 entity 笔记。可重复运行（覆盖模式），MCP graph 变更后重跑。

**页面总数**：60 → 78（+17 entity + 1 _index）。

---

## [2026-04-23] 架构页 | MCP 知识图谱 Mermaid 快照

新建 `architecture/memory-graph.md`，把当前 MCP memory graph（17 实体 + 23 关系，UWAcomm α 补偿技术栈）渲染成 Mermaid 供 Obsidian 预览。含实体/关系清单表、颜色分层（project/hub/scheme/technique/paper）、状态标记（SC-TDE 待修、OTFS 暂停虚线）。

**背景**：MCP 数据已从 npx cache（易失）迁到稳定路径 `C:\Users\zazn\.claude\memory\graph.jsonl`，配合 `MEMORY_FILE_PATH` env 配置。本页作可视化入口，刷新方式为"让 Claude 重绘"（目前手动，脚本化 TODO）。

**页面总数**：59 → 60。

---

## [2026-04-23] 架构页 | 记忆栈首次全面文档化

新建 `architecture/memory-stack.md`，把 Claude Code 的"长期记忆"收口为 5 层栈：全局 CLAUDE.md / 项目 CLAUDE.md / auto-memory / MCP graph / Hub wiki。含逐层详解、决策树、当前状态、维护节奏、已知权衡。

**上下文**：用户本次会话（从进入 Ohmybrain 开始）ABCD 四步：
- A 清理 auto-memory：剥离 `project_uwacomm.md` 过期 TODO；压缩 `project_uwacomm_p3_ui.md` 为遗留清单；`feedback_otfs_pilot_tradeoff` → `reference_otfs_pilot_tradeoff`
- B 新建 `~/.claude/CLAUDE.md`（全局默认偏好）
- C 首建 MCP memory 图谱（UWAcomm α 补偿栈，17 实体 + 23 关系）
- D 本页（记忆栈 architecture 文档化收口）

**页面总数**：58 → 59；最后更新：2026-04-22 → 2026-04-23。

---

## [2026-04-22] ingest | 6 篇 UWA 多普勒论文批量摄入（并行 agent 模式）

对 `D:/Claude/TechReq/UWAcomm/raw/papers/` 下 6 篇多普勒估计相关论文做 Hub 层批量摄入，路径 B（6 个 general-purpose agent 并行，代替 wiki-ingester 因本地 agent 调不出）。

**新建 source-summary**（6 篇）：
- `source-summaries/sun-2020-dsss-passband-doppler.md` — DSSS 符号级通带多普勒跟踪（Sun/Hong/Cui/Liu, 哈工程, JCIN 2020）
- `source-summaries/wei-2020-dual-hfm-speed-spectrum.md` — 双 HFM 速度谱扫描多普勒估计（Wei/Ma/Zhao/Yan, 中科院声学所, IEEE SPL 2020）
- `source-summaries/muzzammil-2019-cpofdm-doppler-interp.md` — CP-OFDM 多普勒尺度 α 插值法（Muzzammil/Wan/Jia/Qiao, 哈工程, ICICSP 2019）
- `source-summaries/lalevee-2025-dichotomous-doppler.md` — FPGA 二叉树多普勒估计（Lalevée et al., ISEN-Brest, OCEANS 2025）
- `source-summaries/yangyang-2026-uwa-otfs-nonuniform-doppler.md` — UWA-OTFS 非均匀多普勒 OG-BSOMP-MLE（Yang/Ma 哈工程, IEEE JOE 2026）
- `source-summaries/zhengtonghui-2025-dd-mmse-teq.md` — SC 水声 DD 域 MMSE Turbo 均衡（Zheng/He/Jing/Yan, 西工大, IEEE JOE 2025）

**新建 concept**（1 个）：
- `concepts/doppler-estimation-methods.md` — 跨 6 篇论文抽取的水声多普勒估计方法学集合（波形/结构/工程三维分类）

**更新 concept**（9 个，追加 wikilink）：
- `concepts/underwater-acoustic-communication.md` + 7 条
- `concepts/time-varying-channel.md` + 7 条
- `concepts/signal-processing-fundamentals.md` + 7 条
- `concepts/channel-estimation-and-equalization.md` + 7 条
- `concepts/ofdm-and-otfs.md` + 3 条
- `concepts/mathematical-optimization.md` + 4 条
- `concepts/usbl-positioning.md` + 2 条
- `concepts/mobile-communication.md` + 3 条
- `concepts/message-passing-algorithms.md` + 1 条
- `concepts/mimo-and-array-processing.md` + 1 条

**更新 entity**（1 个）：
- `entities/uwacomm.md` — 追加 6 篇相关论文 block

**摄入模式说明**：
- **路径 A/B 选择**：用户选 agent 并行（路径 B）
- **wiki-ingester 缺陷**：项目本地 agent `.claude/agents/wiki-ingester.md` 未被 Claude Code subagent_type 识别，改用 `general-purpose` 替身 + prompt 内联完整契约
- **权限问题**：subagent 的 Write 权限被 harness 拒绝（6 个中 5 个，1 个第 3 次重试成功），主会话代为落盘
- **批次约束**：6 个 agent 只写自己的 source-summary，cross-ref 全部走"提案"段，主会话汇总去重后统一应用，避免 race condition（USBL 8 篇并行模式复用）
- **跨会话记忆观察**（TODO §3）：MEMORY.md / CLAUDE.md / SessionStart summary 确实注入 subagent（"信息层"传递有效），但 Write/Bash 等"能力层"权限不随记忆传递 —— 证明 `memory: user` frontmatter 即使生效也只管信息不管权限

更新 index.md（页面总数 51 → 58；最后更新 2026-04-21 → 2026-04-22）。

---

## [2026-04-22] P2 完成 | USBL-S1 autonomous workflow 第 2 次验证

**Phase P2 方法论验证完成**：USBL-S1 Simulation Platform 作为 autonomous-new-project-workflow 的第 2 次实测，验证 workflow **不依赖特定技术栈**（首例 UWAnet 是 C++/ns-3，本次是 MATLAB/Monte Carlo）。

**成果显著优于首例**：

| 维度 | UWAnet 首例（P1） | USBL-S1（P2） |
|---|---|---|
| Phase 3 首轮 | FAIL 需 v2 | **PASS 92/100** |
| Phase 4 首轮 | FAIL（Bash 权限） | **PASS 91→100 修后** |
| 壁钟 / Token / $ | 75min / 530k / $7 | **55min / 450k / $6.5** |
| Agent 调用 | 5 | **4** |

**新发现 Pitfalls**（补到 [[explorations/autonomous-new-project-workflow]]）：
- **#10** Wikilink 根目录路径歧义（Obsidian vault 根 vs fs 相对路径）
- **#11** MATLAB 脚本 matlab_invoke 结构限制（.m 无 shebang）

**Hub 新增**：
- `projects/usbl-s1/README.md` — P2 dry-run 导航入口（独立于 `projects/usbl/`）
- `explorations/autonomous-new-project-workflow.md` — 追加 Pitfalls #10/#11 + §后续路径 P2 标 ✅

**Worktree**：`D:/Claude/worktrees/usbl-redo/`（USBL 主仓全程 never_touch，未改动）

**下一步建议**：
- **P2-matlab-branch（新）**：基于本次经验抽 `template/prompts/goal.yaml.matlab-sim.tpl` + `template/.claude/settings.local.matlab.json.example`，下次 MATLAB 项目开箱用
- **P3（远期）**：封装 `/new-project` command

---

## [2026-04-21] P1 完成 | 闭环套件模板化到 ohmybrain-core

继本日 UWAnet dry-run 验证后，把完整闭环套件抽到 `ohmybrain-core/template/`，下次新建项目开箱即用。

**新增**：
- `template/prompts/goal.yaml.tpl`（~135 行，Jinja 占位符版，含 v2 rubric 4 项硬约束）
- `template/prompts/planner.md`（从 UWAnet 复制，通用）
- `template/prompts/evaluator.md`（从 UWAnet 复制，含 v2 约束验证）
- `template/prompts/README.md`（启动流程 + 占位符清单 + 实测预算 + 坑位提示）
- `template/.claude/settings.local.json.example`（Bash 白名单，修 Pitfall #7）

**更新**：
- `template/CLAUDE.md`（新增"## 闭环模式（可选）"段落指向 prompts/ 和 `.claude/settings.local.json.example`）
- `ohmybrain-core/docs/new-project-sop.md`（新增 §8 闭环模式启动章节）

**效果**：下次开新项目 `cp -r template/. <worktree>/` 后只需：
1. 填 goal.yaml 占位符（~5 个必填）
2. 复制 `settings.local.json.example` → `settings.local.json`
3. 启动 Phase 3 Planner

**不需要**重新设计 rubric、prompt、红线、预算，全部继承 UWAnet 首轮 dry-run 的校准值。

**exploration 页状态更新**：`wiki/explorations/autonomous-new-project-workflow.md` §后续路径 P1 → ✅ 已完成。

---

## [2026-04-21] phase4-5 dry-run | UWAnet 闭环完整走通（真装机 PASS）

基于本日上午方法论设计，下午完成完整闭环 dry-run：Phase 1 scaffold → Phase 2 ingest (reuse) → Phase 3 Planner v1/v2 + Eval v1/v2 → Phase 4 Generator + Eval + **真装机**。

**Phase 3 实测数据（GAN harness 首次验证）**：
- 两轮 Planner/Evaluator 迭代：Eval 独立分 v1=83 → v2=92 (**Δ+9 真收敛**)
- Planner 自评虚报从 v1 的 +10 降到 v2 的 +3（**校准改善 70%**）
- Evaluator 独立 grep 验证抓到 5 个裸 wikilink + 1 处散文化 EC + 循环引用 3 类漏洞
- Rubric v1 → v2 加严（+4 约束：`wikilink_resolvable` / `exit_criteria_format` / `success_criteria_rules` / `interface_table_rules`）

**Phase 4 实测数据（真装机）**：
- WSL2 Ubuntu 20.04 + ns-3.41 (shallow, tag lock) + Aqua-Sim-NG (rmartin5 官方) 全装
- 2015/2015 构建目标，0 error（第一轮 `-Werror=parentheses` 挂 2 处，patch 2 行源码 + `CXXFLAGS=-Wno-error` 修复）
- 验证通过：hello-simulator ✅ / JmacTest ✅ / broadcastMAC_example ✅ / VBF ✅ / smoke_test.py (stub) ✅

**累计成本**：~$7 / ~75 min 壁钟（含人工干预：sudo NOPASSWD 配置 + patch aqua-sim-ng 2 行源码）

**沉淀到 Hub 的可复用资产**：
- `projects/uwanet/prompts/goal.yaml` v2（4 项新 rubric 约束）
- `projects/uwanet/prompts/planner.md + evaluator.md`
- `scripts/extract_pdf.py`（跨项目 PDF ingest 工具）
- `wiki/explorations/autonomous-new-project-workflow.md`（本日已更新：+实测段 + 3 个新 Pitfall）

**本次发现的 3 个新 pitfall（详见 exploration 页）**：
- **#7** Subagent Bash 运行时隐式拦截（需 `.claude/settings.local.json` 显式 allow）
- **#8** Upstream 代码与新 GCC 不兼容（`-Werror=parentheses`，需 patch + `CXXFLAGS=-Wno-error`）
- **#9** ns-3.41 API 变更（`./ns3 show examples` 废弃、target 名必须 CamelCase）

**UWAnet 项目状态**：前期调研阶段 → **M1 环境搭建已跑通**，下一步 M2 源码阅读。

**未做**（defer）：
- smoke_test.py STUB_MODE=False 实现（`rubric.m1_environment` stub 已满足，真模式属于 M2 事）
- `.claude/settings.local.json` Bash 白名单模板化到 `ohmybrain-core/template/`（下个项目时做）
- ns-3.41 target 命名规则补到 `wiki/source-summaries/ns3-documentation-index.md`（UWAnet 侧 TODO）

页面总数不变（纯内容追加 + exploration 页内部扩充）。

---

## [2026-04-21] explore + promote | 自主新建项目工作流方法论

**背景**：本日会话从"非工作时段让 agent 无人值守推进项目"这一诉求出发，针对 UWAnet 重建场景设计了一套"一行目标 → M1 落地"的自主闭环。沉淀本次设计决策为跨项目可复用资产。

**Hub wiki 产出**：
- 新建 `explorations/autonomous-new-project-workflow.md`（~200 行）— 7 阶段 DAG + 3 种闭环模式（Verification / Santa / GAN）+ rubric 设计原则 + 预算四层约束 + 红线/升级 + 6 个 pitfalls + 可复用资产清单 + P0-P3 后续路径
- 链入 5 个已有页：[[harness-engineering]]、[[subagents-orchestration]]、[[claude-hooks-architecture]]、[[ohmybrain-agent-architecture-insights]]、[[system-overview]]、[[skills-vs-commands]]

**Hub projects 产出**（导航层，非 wiki 层）：
- `projects/uwanet/prompts/goal.yaml` — 闭环权威驱动（含 pre_ingested_summaries、预算混搭、红线、升级）
- `projects/uwanet/prompts/planner.md` — `gan-planner` prompt，产 PRD + 架构 + 里程碑 + 风险
- `projects/uwanet/prompts/evaluator.md` — `gan-evaluator` prompt，独立 grep 硬验证 + rubric 打分 + 反馈
- `projects/uwanet/prompts/README.md` — 套件说明 + 阶段映射 + 使用方式

**Hub scripts 新增**：
- `scripts/extract_pdf.py` — PyMuPDF 实现的 PDF 文本提取（批量 + 单文件），补齐本机无 `pdftoppm` 的短板，**未来所有项目 ingest PDF 可复用**

**UWAnet 项目侧**（本次顺带完成）：
- /ingest `raw/papers/` 4 篇 + `raw/courses/NS3资料/` 14 份 PDF（用上述 `extract_pdf.py`）
- 产出 5 份 source-summary：`ns3-installation-guide` / `ns3-documentation-index` / `aqua-sim-family` / `slotted-fama-mac` / `janus-standard`
- UWAnet `wiki/index.md` 页面总数 2 → 7；`wiki/log.md` 追加同日条目

**跨项目启发（核心）**：
- **调试期 vs 闭环期共存**：分层自动化（已完成模块挂闭环 / 在调模块半自动 / 基础设施层随时可上）
- **GAN + Verification 组合**比单一闭环稳：前者管"好不好"后者管"对不对"
- **迭代上限比 token 上限更关键**：token 设再大，死循环一样烧光
- **Evaluator 必须独立 grep 验证，不信 Planner 自评**

**Defer**（未做）：
- 新建 `gan-harness` / `verification-loop` concept 页 — 单源（仅本次会话），待首次 dry-run 产出实测数据再独立成 concept
- 抽 `goal.yaml` 结构到 `ohmybrain-core/template/prompts/` — 等 UWAnet 真跑一次完整闭环后再做
- 封装成 `.claude/skills/new-project-loop/` — P2，需 2 个以上项目验证

**接续动作**：等用户在 worktree `uwanet-redo` 发起 Phase 1+2 dry-run，验证闭环。

更新 `index.md`（50 → 51）。

---

## [2026-04-17] apply | claude-mem 5 条可迁移模式落地（P0/P1/P2/P3）

基于 [[thedotmack-claude-mem]] summary 中的 5 条推荐优先级，在 Hub + ohmybrain-core + 3 下游全面落地（不安装 claude-mem 本体，仅借鉴模式）。

**P0 · `<private>` tag hook**（已完成）
- 新建 `scripts/check_private_tags.py`（74 行，`dataclass(frozen=True)` + 正则扫描 + PreToolUse 阻断）
- 保护范围：`wiki/**` + `projects/**`；放行 `raw/**` 及项目内部路径
- 阻断行为：exit 2 + stderr 提示 3 种处理方式
- 自测 7/7 通过（protected + private tag / 放行 / Edit / multiline / 非 Write 工具 / malformed JSON）
- 部署：Hub `scripts/` + `ohmybrain-core/template/scripts/` + UWAcomm/USBL/UWAnet `scripts/`
- settings.json 接入：5 位置全部追加为 PreToolUse Edit|Write matcher 的第 2 个 hook
- 下游烟测 3/3 pass

**P1a · llm-wiki §Query 改三层渐进披露**（已完成）
- 改写 `~/.claude/skills/llm-wiki/SKILL.md` §Query：Step 1 索引（读 index.md）→ Step 2 时序上下文（读 log.md + frontmatter）→ Step 3 详情（≤3 页 Read）
- 加入反模式清单：跳过 index 直接 grep 全文 / 一次读 5+ 页面 / 重复覆盖
- 目标：约 10× token 节省（对照 claude-mem `search → timeline → get_observations` 模式）

**P1b · plan-task / implement-task 重写**（已完成）
- `plan-task/SKILL.md`：加 Phase 0 Documentation Discovery + Subagent Reporting Contract（sources/findings/snippets/confidence+gaps，无证据则拒绝重派）+ "COPY from docs, don't invent" 硬约束 + 每阶段 Allowed APIs + Anti-patterns
- `implement-task/SKILL.md`：改为 Orchestrator 协议，每阶段部署 Implementation / Verification / Anti-pattern / Commit 4 个子代理，commit only if verified
- 部署：`ohmybrain-core/template/.claude/skills/` + UWAcomm/USBL/UWAnet `.claude/skills/`

**P2 · CLAUDE.md 补 Exit Code Strategy 段**（已完成）
- Hub / ohmybrain-core/template / UWAcomm / USBL / UWAnet CLAUDE.md 全部补段
- 表格化 0/1/2 语义 + 4 条设计原则（宽松优先 / 阻断谨慎 / 提醒用 exit 0 / Windows Terminal tab 注意）
- 列出当前阻断型 hook：`check_raw_write` + `check_private_tags` + `check_index_log_sync`

**P3 · mode 系统 UWAcomm 试点**（已完成）
- 新建 `TechReq/UWAcomm/.claude/modes/matlab-zh.json`（结构化抽取 Language & Conventions + MATLAB 测试调试流程 + Git 约定）
- 新建 `.claude/modes/README.md` 说明模式清单 + 现状 vs 最终形态 + 兼容性注记
- **当前形态**：mode 文件作为可追溯的结构化镜像，CLAUDE.md 仍是主事实源（避免两处分叉）
- **未运行时切换**：Claude Code 无 env-var 驱动 prompt 切换，待首个 mode 分叉场景出现时再决方案（YAGNI）
- CLAUDE.md 加一行"当前模式：matlab-zh"指针

**新基础设施清单**（Hub 视角）：
| 类型 | 新增 |
|------|------|
| Hook 脚本 | 1（`check_private_tags.py`）|
| Skill 重写 | 2（`plan-task` / `implement-task`，均在 core/template + 3 下游）|
| 全局 Skill 改动 | 1（`llm-wiki` §Query 三层协议）|
| CLAUDE.md 增补 | 5（Hub + core + 3 下游）|
| 新目录 | 1（UWAcomm `.claude/modes/`）|

**Defer**（未做）：
- claude-mem 本体安装（明确决定不装，见本日对话）
- Chroma 向量搜索 / worker service / SQLite observation DB（过度工程）
- 运行时 mode 切换（YAGNI，待分叉场景）

---

## [2026-04-17] ingest | thedotmack-claude-mem（Claude Code 持久记忆插件）

摄入 `raw/repos/claude-mem`（Alex Newman / AGPL-3.0 / v12.1.6，211 MB，TypeScript+Bun+SQLite+Chroma+React UI）——Trendshift 收录、Awesome Claude Code 提及的跨会话记忆插件。

**产物**：
- 新建 `source-summaries/thedotmack-claude-mem.md`（~180 行），5 条可迁移模式 + 4 条不建议借鉴 + 4 范本对照表 + 5 条推荐落地优先级
- 追加 wikilink 到 3 页：[[claude-hooks-architecture]]（生命周期活例）/ [[subagents-orchestration]]（Subagent Contract 范本）/ [[entities/claude-code]]（插件生态代表）

**核心启发**（按借鉴优先级）：
- **P0**：`<private>` 标签 + hook 层脱敏——1 个 Python 脚本即可自动隔离 Pricing 🔒 类私项目
- **P1**：`mem-search` 的**三层渐进披露检索**（search → timeline → get_observations，~10× token 节省）可直接移植到 `llm-wiki` skill
- **P1**：`make-plan` / `do` 的 **Phase 0 Documentation Discovery + Subagent Reporting Contract**（sources / findings / snippets / confidence+gaps）给 `plan-task` / `implement-task` skill 强约束
- **P2**：CLAUDE.md §Exit Code Strategy 明文契约（0=success / 1=non-blocking / 2=blocking + Windows Terminal tab 哲学）
- **P3**：36 个 `code--{lang}.json` mode 系统（语言层与功能层分离）

**不建议借鉴**：Chroma 向量搜索（49 页规模 grep 足够）/ worker service + React UI（过度工程，Obsidian 足够）/ SQLite observation DB（与 Ohmybrain 主动 ingest 哲学正交）/ AGPL-3.0（商用不友好）。

**新建 concept 提案**（defer）：`progressive-disclosure-retrieval`——"索引→时序上下文→详情"三层检索模式。单源当前，待再找 1 个独立源（Anthropic Context Engineering 官方文档？）再创建。

**遵守的约束**：summary 180 行（预算 ≤200）/ 更新 3 页（预算 ≤5）/ 仅追加 wikilink（无 H2 小节）/ 不新建 concept。

更新 index.md（49 → 50）。

---

## [2026-04-17] rewrite | architecture/system-overview.md 反映三仓架构

**触发**：Task 4 核查中发现 `system-overview.md` 仍描述**单仓一体化架构**（2026-04-12 创建时的早期设计），与当前实际的 `ohmybrain-core + project-* + ohmybrain(hub)` 三仓架构不符。

**产出**：
1. 摄入 `raw/notes/ohmybrain_core_hub_projects_diagram.md`（206 行）→ 新建 `source-summaries/ohmybrain-three-tier-seed.md`（作为架构页事实源）
2. 重写 `architecture/system-overview.md`：
   - 定位改为三仓架构
   - 加入当前实例映射表（UWAcomm / USBL / UWAnet / Pricing + core + hub）
   - 三层职责详述（母仓/项目仓/Hub）
   - 数据流：初始化演进流 + 知识闭环 + 开发闭环
   - Harness 机制：拆分 global/project 两级（rules/skills/agents/hooks）
   - Hub hooks 实际状态表（2026-04-17 check_raw_write / post_wiki_write / raw_ingest_reminder / session_context / check_index_log_sync / commit_reminder）
   - 当前规模表：49 页 / 4 项目 / 17 脚本
   - 演进里程碑补"架构拆分"事件
3. 保留"演化历史"段落显式标注：早期单仓设计 → 三仓拆分
4. 追加 wikilink：[[ohmybrain-three-tier-seed]]、[[ohmybrain-agent-architecture-insights]]

**未改**：`toolchain.md` / `research-map.md` / `my-brain-setup-plan` 保留原文 —— 它们要么与架构层无关（工具链），要么是历史快照（setup-plan）。

更新 index.md（48 → 49，并更新 architecture 条目描述）。

---

## [2026-04-17] ingest | uwanet-protocol-sim-note（UWAnet 前期调研种子笔记）

摄入 `raw/notes/uwanet-protocol-sim.md`（282 行学习笔记）——UWAnet 项目前期调研的**主种子文档**，项目当前处于"前期调研阶段"尚无代码产出。

**产物**：
- 新建 `source-summaries/uwanet-protocol-sim-note.md`（~90 行），核心观点 5 条（协议栈分层 / 平台选择 / 环境搭建 / Slotted ALOHA 案例 / Claude Code 加速时间对比）
- 追加 wikilink 到 [[underwater-acoustic-communication]] 的"来源"段（UWA 网络作为 UWA 通信的组网延伸）
- 未修改 [[uwacomm]] 实体页——uwacomm 与 uwanet 是并列项目，不互相从属

**新建 concept 提案**（待决策）：
- `uwa-networking` — 锚定 MAC / 路由 / 传输层协议 + 仿真平台（Aqua-Sim-NG / DESERT）+ 水声网络理论
- **当前 defer**：单源，待 UWAnet 项目产出 ≥2 个实测结论后再创建

**待后续同步**（本次未做）：
- `entities/uwacomm.md` 规模数据陈旧（186→258 文件 / 13→14 模块），与 [2026-04-17 projects/uwacomm 同步] 同源，下次摄入/触碰时顺带更新

更新 index.md（47 → 48）。

---

## [2026-04-17] ingest | cocoon-ai-architecture-diagram（Claude Skill 极简单用途范本）

摄入 `raw/architecture-diagram-generator/`（Cocoon AI / MIT / v1.0，2025-12 提交）——Claude.ai 官方支持的架构图生成 skill，仅 1 个 `SKILL.md` (163 行) + 1 个 `template.html` (319 行) + `.zip` 分发包。

**产物**：
- 新建 `source-summaries/cocoon-ai-architecture-diagram.md`（95 行），核心观点 4 条
- 追加 wikilink 到 3 个已有页：[[skill-layered-resources]] / [[yizhiyanhua-ai-fireworks-tech-graph]] / [[entities/claude-code]]
- 未新建 concept（单源 + 内容与现有 skill-layered-resources 直接对照）

**关键启发**：作为 [[yizhiyanhua-ai-fireworks-tech-graph]] 的**极简反例**，补足了 [[skill-layered-resources]] 的边界——**单风格 + 单输出类型的 skill 不必三层分离**，全塞主 SKILL.md 反而决策更清晰。判据补充为"≥2 个正交维度才值得分层"。

**遵守的约束**：summary 95 行（预算 ≤200）/ 更新 3 页（预算 ≤5）/ 仅追加 wikilink 行（无 H2 小节）/ 不新建 concept。

更新 index.md（46 → 47）。

---

## [2026-04-17] sync | projects/uwacomm/README.md 同步下游进度

Hub 项目导航页滞后下游 2 天，本次同步 UWAcomm 2026-04-15~17 进展：
- 规模：186 文件 25 830 行 → **258 文件 38 649 行**
- 模块数：13 → **14**（新增 14_Streaming 流式仿真框架）
- 体制表：补充各体制已接入 `modem_dispatch` 统一 API（OFDM / SC-TDE / SC-FDE / FH-MFSK）
- 新增 4 条关键技术结论（流式相关：passband 原生信道 / hybrid 帧检测 / FH-MFSK 软判决 LLR / 多径展宽极限）
- 替换"待办"为当前 9 条活跃 spec 方向（deoracle / OTFS 三项 / 流式 P4-P6 / UI polish/refactor）
- 项目内导航：wiki 37 → 40 页，补 `conclusions.md` + `comparisons/e2e-test-matrix.md`

仅 `projects/` 导航页变更，不涉及 wiki/ 本体——不更新 index.md 页数。

---

## [2026-04-15] sync | 基础设施改进下发母仓 + 3 下游项目

把本日 Hub 完成并验证的两类基础设施改进同步到 `ohmybrain-core/template` + `TechReq/{USBL, UWAcomm, UWAnet}`。

**P0（4 位置）**：
- `settings.json` 所有 hook 命令改 `python "$CLAUDE_PROJECT_DIR/scripts/xxx.py"`（消除相对路径 CWD bug，4 位置各 0 处相对路径残留）
- 新增 `scripts/raw_ingest_reminder.py`（1576 bytes，Hub 副本）+ `settings.json` 挂 `PostToolUse.Bash` matcher

**P1（3 下游）**：
- 母仓 `workflows/engineering/00-module-design.md` 回填到 USBL / UWAcomm / UWAnet——此前"先在母仓沉淀，明确后再回填"的决定，经 wiki-ingester spec 验证获得足够信心后放行

**Defer**：
- **P2 · wiki-ingester agent 下游化**——下游一般只走 `/promote-answer`，暂不建 `.claude/agents/`
- **母仓→已派生项目的增量同步机制**——本次手动同步可行但不可持续，未来需要工具化

**Hub 本仓不受影响**（Hub 早先已单独落地 P0，此次仅分发给另外 4 个位置）。

---

## [2026-04-15] validate+ingest | everything-claude-code（wiki-ingester spec 验证测试）

测试对象：`raw/repos/affaan-m-everything-claude-code`（Affaan Mustafa/MIT/黑客松冠军，v1.10.0，**1963 文件 / 20+ 子目录，比 fireworks 大 40×**）。

**验证目的**：测最新收紧的 wiki-ingester spec 预算约束在大型仓库下是否仍然生效。

**测试设计**：最小 prompt（仅 `raw_path: xxx`，无任何扩展关键词），验证默认行为。

**结果对照**：

| 指标 | fireworks 基线 | 本次 ECC | 目标 | 结果 |
|------|-------------|---------|------|------|
| 耗时 | 56 min | **7.6 min** | ≤15 min | ✅ -86% |
| Tool uses | 74 | 38 | ≤25 | ⚠️ 超目标 13 |
| Tokens | 203k | 126k | ≤80k | ⚠️ 超目标 46k |
| Summary 行数 | 383 | 205 | ≤200 | ⚠️ 超 5 行 |
| 新建 concept | 1 | 0 | 0-1 | ✅ 严守 |
| 更新页面 | 9 | 5 | ≤5 | ✅ 卡在上限 |

**遵守的约束**：不新建 concept ✓ / 更新页数 ≤5 ✓ / 大幅减少耗时 ✓

**违规（spec 约束没挡住）**：agent 在 4 个已有 concept/entity 页**都加了 `## H2` 级新小节**（"生产级规模化范本" / "规模化工程实践：ECC 48 agents 生态" / "生产级验证：ECC 的 Skills-First 策略" / "运行时门控扩展：ECC Hook Profile"），违反 spec 的"不加新小节"硬约束——本应只追加 wikilink 行。

**产出**：
- 新建 `source-summaries/affaan-m-everything-claude-code.md`（205 行）
- 更新 4 个已有页（加 H2 小节 + 追加 wikilink）—— **应该只追加 wikilink**

**初步结论**：耗时约束有效（-86%），结构约束（不加小节）**仍需进一步强化**——spec 的措辞歧义或软约束强度不足。下一步候选：把"不加小节"改为绝对禁令 + 动作后自检。

更新 index.md（45 → 46）。

---

## [2026-04-15] ingest | fireworks-tech-graph（Claude Code Skill 工程化范本）

用 `/ingest` 新架构（Step 1.5 询问→选 agent→wiki-ingester 独立上下文执行 Step 2-4）摄入 `raw/repos/yizhiyanhua-ai-fireworks-tech-graph`（yizhiyanhua-ai/MIT/npm v1.0.4，7 视觉风格 + 14 图类型的 SVG 生成 skill）。

**产物**：
- 新建 `source-summaries/yizhiyanhua-ai-fireworks-tech-graph.md` — 7 条可迁移模式（三层资源 / 触发关键词 / Pre-Tool-Call Checklist / Error Recovery Protocol / UML 映射表 / npm 打包 / 多 runtime 兼容）
- 新建 `concepts/skill-layered-resources.md` — 三层资源分离作为独立概念（fireworks 正例 + Ohmybrain `llm-wiki` 当前反例）
- 追加 wikilink 到 7 个已有页（`skills-vs-commands` / `claude-hooks-architecture` / `subagents-orchestration` / `entities/claude-code` / `source-summaries/claude-code-best-practice` / `source-summaries/nousresearch-hermes-agent` / `explorations/ohmybrain-agent-architecture-insights`）

**Defer**：未新建 `skill-packaging` concept——单源（仅 fireworks）且 Ohmybrain 暂无打包需求。

**摄入过程发现的 harness bug**（由 agent 诚实报告）：`.claude/settings.json` 里 `python scripts/check_raw_write.py` 用相对路径——CWD 在子仓时找不到脚本。下文另一 log 条目处理。

更新 index.md（43 → 45）。

---

## [2026-04-15] spec | wiki-ingester 预算与默认行为约束

基于 fireworks-tech-graph 摄入超预算事后检视（56 min / 74 tool uses / 203k tokens / 383 行 summary，vs dingjie 基线 6 min），收紧 `.claude/agents/wiki-ingester.md` spec（133 → 187 行）+ 同步 `.claude/commands/ingest.md`：

**新增约束**：
- **输出预算**：默认 summary ≤200 行 / 核心观点 5-8 条 / 启发 6-10 条 / 更新 ≤5 页
- **阅读预算**：repo 默认只读 README + 顶层 tree + SKILL/package 前 100 行；不读 `references/*` / `templates/*` / `scripts/*` 正文
- **交叉引用默认**：仅在已有页"来源"段追加一行 `[[slug]]`，**禁止**擅自加"## 小节"或修改段落
- **新建 concept/entity**：默认不擅建，走"备注提案"路径等主会话决策

**扩展通道**（user_intent 关键词显式授权）：`depth: full` / `new_concepts_ok` / `new_entities_ok` / `allow_new_sections` / `allow_paragraph_edit` / `wide_cross_ref`

**把反例写进 spec**：Step 4 明文记录 fireworks 越界案例 + 预期降幅（56 min → 10-15 min），用具体数字而非抽象约束来锚定 agent 行为。

**未做**（候选更大改造，见 P1+ 候选）：分阶段 agent（summary-agent + cross-ref-applier ×N 并行）。先观察 spec 级改进是否足以逼住越界。

---

## [2026-04-15] fix | Hook 脚本改绝对路径 + 新增 raw/ ingestion 检测

修复两个 harness 监督盲区：

**① Hook 脚本相对路径问题**：`.claude/settings.json` 所有 hook 命令从 `python scripts/xxx.py` 改为 `python $CLAUDE_PROJECT_DIR/scripts/xxx.py`，避免 CWD 切换（如 Bash `cd raw/repos/xxx`）后 hook 找不到脚本。

**② 新增 `raw_ingest_reminder.py`（PostToolUse on Bash）**：检测 `git clone` / `curl -o raw/` / `wget -P raw/` / `cp/mv ... raw/` 等命令触及 `raw/` 的场景，stdout 提醒"raw/XXX 已新增，建议运行 `/ingest raw/XXX`"。动机：本次对话中"把这个项目放到 raw 中"用 `git clone` 扩充 raw/ 未触发 `/ingest`——自然语言 ≠ 显式命令，现在靠 hook 兜底。

---

## [2026-04-14] P1-3 | /ingest 路径分流（inline vs agent 二选一）

给 `/ingest` 加 Step 1.5：处理前**预判资料规模**（文本 < 5k 字 / PDF < 10 页 / 仓库模块数 / 视频 < 15 min）+ 通过 AskUserQuestion 询问用户选 **inline 主会话内联** 还是 **agent 委托 wiki-ingester**。两条路径产出**同构的"摄入报告"契约**，Step 5-7 机械消费、路径无关。批量模式支持"统一策略"（全部 inline / 全部 agent 并行 / 混合逐个询问）。

动机来自 A/B 报告 [[wiki-ingester-ab-test-dingjie-2020]] 结尾："新 agent 架构对短资料 ~300s+ / ~124k tokens 起步不划算"——需要一层规模分流。规模阈值只作默认高亮，**始终显式询问**，让用户保留"这次想快"或"这次想细"的决定权。

**改动**：仅 `.claude/commands/ingest.md`（无新 agent/skill/script） + 本仓 `wiki/explorations/ohmybrain-agent-architecture-insights.md` 追加 §P1-3 实施记录。

---

## [2026-04-14] batch-ingest | USBL 项目剩余 8 篇论文并行摄入

用新架构 `wiki-ingester`（本会话 general-purpose 模拟）并行处理 USBL 项目 raw/papers/ 下剩余 8 篇中文博士/期刊论文。主会话做 Step 1（任务分发）和 Step 5-7（批量 cross-ref + index/log + lint）。

**并行约束设计**：8 个 agent 只写自己的 source-summary，**不**编辑 concept/index/log，cross-ref 提案在返回报告中；主会话批量应用——成功避免 race condition。

**新建 8 个 source-summary**：
- `hexutao-usbl-quad-array` — 改进四元立体阵 + EKF 降噪（何旭涛等 2025 期刊）
- `guoyu-2024-lie-group-nav` — 李群 SINS/DVL/USBL 组合（郭瑜博士 2024）
- `liufeng-2024-passive-localization` — 被动定位 + 因子图（刘峰博士 2024）
- `zhengcuie-usbl-docking` — AUV 对接三段式（郑翠娥博士 ~2007-2010）
- `yangbaoguo-2013-usbl-calibration` — 观测方程三性质校准（杨保国博士 2013）
- `quzhenzhao-2024-usbl-precision` — 五元阵多构型融合（蘧振超等 2024 短文）
- `huangjian-2019-lbl-usbl` — LBL/USBL 组合六技术（黄健博士 2019）
- `yumin-2006-lr-usbl` — 国内首代 LR-USBL（喻敏博士 863 项目 2006）

**批量更新 7 个 concept**：
- `usbl-positioning`（+8 wikilink，共 9 篇溯源完整）
- `mimo-and-array-processing`（+8 wikilink）
- `signal-processing-fundamentals`（+9 wikilink，首次建立论文溯源）
- `mathematical-optimization`（+5 wikilink，首次建立论文溯源）
- `channel-estimation-and-equalization`（+3 wikilink）
- `message-passing-algorithms`（+1 wikilink，刘峰因子图）
- `time-varying-channel`（+1 wikilink，黄健移动场景）

**未新建 concept**（3 个候选 defer）：
- `lie-group-navigation`（仅 guoyu 一个源，待积累）
- `passive-acoustic-localization`（仅 liufeng 一个源）
- `lbl-positioning`（仅 huangjian 一个源）
- `integrated-acoustic-navigation`（7 篇涉及但主题过泛，暂不抽）

**并行成本**：8 agent 同时跑，~700s 总耗时（最慢的 huangjian/liufeng ~670s），总 ~1M subprocess tokens，主会话只收到 8 份 ~200 行报告。

**观察 / 发现**：
- hexutao 实为 2025 期刊短文（非博士论文），slug 保留原命名
- zhengcuie PDF OCR 后年份信息缺失，frontmatter 保守标"~2007-2010"
- yumin PDF 为扫描件无 text layer，agent 依赖 USBL 项目版参数表 + 项目 lit-review 构造摘要（诚实报告），事实面准确
- 多个 agent 自发用 PyMuPDF 命令行绕过 Claude Code pdftoppm 失败问题，经验一致
- 多个 agent 指出可能新建 concept 但主动判断"单源不足，defer"——判断力符合策划者预期

更新了 `index.md`（页面总数 35 → 43），9 篇论文完整溯源到 Hub。

---

## [2026-04-14] explore | 新架构 A/B 对比报告

基于丁杰 2020 论文实测结果（上一条日志），撰写完整 A/B 对比分析：`explorations/wiki-ingester-ab-test-dingjie-2020.md`。

- **定量**：行数 +182%，核心章节 +80%，跨项目启发 +167%
- **定性**：新产出保留数学公式与 9 行商用设备表；"启发"分项目/Hub 两层；诚实报告 PDF 编码处理问题
- **架构验证**：Agent 独立上下文不污染主会话（124k tokens 隔离）、输出契约稳定、Hook 兜底有效、交叉引用判断合理
- **代价**：350s / 124k tokens——对长论文/大仓值得，对小资料不划算
- **反馈**：发现 spec 可优化点（"核心观点"结构应明文要求，agent 这次靠运气做对了）

更新了 `index.md`（页面总数 34 → 35）。

---

## [2026-04-14] ingest+test | 丁杰 2020 USBL 博士论文（wiki-ingester 新架构首次实测）

首次用新架构（wiki-ingester Agent 在独立上下文做 Step 2-4，主会话做 Step 1 & 5-7）摄入一篇博士论文。由于本会话 Claude Code agent 清单在启动时已快照，新 `wiki-ingester` 未注册——改用 `general-purpose` agent 内联 spec 模拟（等效行为，次会话原生可用）。

- **新建 source-summary**：`source-summaries/dingjie-2020-compact-usbl.md`（127 行，含商用 USBL 设备参数表 9 行 + 3 项方法的数学描述 + 8 条跨项目启发）
- **更新 concepts**：`concepts/usbl-positioning.md`（追加 `[[dingjie-2020-compact-usbl]]` 到来源段）、`concepts/mimo-and-array-processing.md`（追加同上）
- **未新建 concept**：基线分解法未独立成 concept，原因见 source-summary 摘要（与 usbl-positioning 强耦合，避免孤岛页）

与老处理（USBL 项目 wiki 的 dingjie-2020-compact-usbl.md，45 行）对比：新架构产出更细致（+182%），保留了数学推导与原表，但体现 Hub 跨项目视角而非项目集成视角。详细对比见后续探索页。

更新了 `index.md`（页面总数 33 → 34）。

---

## [2026-04-14] P1-2 | /ingest 抽出 wiki-ingester Agent

将 `/ingest` Command 中 Step 2-4（提取 / 写页 / 交叉引用）委托给新建 `wiki-ingester` 子代理。主会话只做 Step 1（扫描入口）和 Step 5-7（index/log 同步 + lint）。独立上下文保护主会话不被大仓库 README 填满；index/log 变化保留在主会话确保用户审计可见。

新建文件：
- `.claude/agents/wiki-ingester.md` — Agent 定义（acceptEdits + inherit model + 结构化输出契约）
- `.claude/commands/ingest.md` — 重写为编排型 Command（Step 1 → 调 Agent → Step 5-7）

同步更新 `explorations/ohmybrain-agent-architecture-insights.md` P1-2 `[x]` + 实施记录。

---

## [2026-04-14] P1-1 | llm-wiki rule → skill 迁移

将全局 `~/.claude/rules/common/llm-wiki.md` 迁移为 skill `~/.claude/skills/llm-wiki/SKILL.md`，带 `paths: wiki/**` 自动激活。顺便修复老 rule 中的 stale DocHub/`D:\Obsidian\workspace` PARA 引用，对齐 Ohmybrain 当前 wiki 结构，新增 Promote 章节。老 rule 改为过渡期占位，验证无回归后可手动删除。本会话 Claude Code 已识别到新 skill。

同步更新 `explorations/ohmybrain-agent-architecture-insights.md` P1 第一项为 `[x]` + 实施记录。

---

## [2026-04-14] P0 | 补 hook + cache/path 审查

完成架构启发录 P0 三项：

- 新增 3 脚本 + 1 settings.json 改动：`post_wiki_write.py`（PostToolUse，wiki/ 自动 lint 非阻断）、`session_context.py`（SessionStart，注入最近 3 条 log + 项目列表）、`commit_reminder.py`（Stop，wiki 未提交提醒）；并把已有 `check_index_log_sync.py` 接入 Stop hook
- Cache 审查：`/ingest` 纯指令型、无 toolset 切换、无 memory 重载——符合 "Prompt Caching Must Not Break"
- Path 审查：scripts/ 仅 2 处 `~/Zotero/` 硬编码，属外部工具 fixed path，保留

同步更新 `explorations/ohmybrain-agent-architecture-insights.md` P0 三项为 `[x]`。

---

## [2026-04-14] create | Ohmybrain 架构启发录

基于 [[claude-code-best-practice]] + [[nousresearch-hermes-agent]] 对照阅读，创建 `explorations/ohmybrain-agent-architecture-insights.md`——分 4 档（架构层 / 机制层 / 质量层 / 远期）+ 4 级优先级（P0 立即可做 / P1 本月 / P2 下一阶段 / P3 远期）。核心判断：**架构向 Hermes 学（开放、插件化、profile 隔离），日用依赖 Claude Code（Opus 4.6 + 1M + OAuth）**。

更新了 `index.md`（页面总数 32 → 33）。

---

## [2026-04-14] ingest | Hermes Agent 开源代理

对 `raw/repos/hermes-agent`（Nous Research，MIT，v0.9.0 / tag `v2026.4.13`）执行 ingest，创建 1 个新 summary + 更新 3 个概念页：

- **1 个 source-summary 页**：`source-summaries/nousresearch-hermes-agent.md` — Hermes Agent 全景，含 10 个可借鉴模式（单一 CommandDef 驱动多终端 / Prompt Caching 硬约束 / HERMES_HOME profile 隔离 / token lock / tool schema 禁跨引 / agent-level 工具拦截 / 可插拔 context engine / 6 终端后端 + serverless / gateway hooks / RL trajectory 采集）与 Claude Code 对比表 + 6 项对 Ohmybrain 的连接点
- **更新 3 个概念页**（追加 Hermes 作为同范式另一实现的参考段落）：
  - `concepts/subagents-orchestration.md` — `delegate_tool` 对比
  - `concepts/skills-vs-commands.md` — agentskills.io 开放标准
  - `concepts/claude-hooks-architecture.md` — gateway hooks 双层架构

更新了 `index.md`（页面总数 31 → 32）。

---

## [2026-04-14] ingest | Claude Code 最佳实践参考仓

对 `raw/repos/claude-code-best-practice`（shanraisshan 维护，对标 v2.1.101）执行深度 ingest，创建 4 个新 wiki 页面 + 更新 1 个实体页：

- **1 个 source-summary 页**：`source-summaries/claude-code-best-practice.md` — 整仓摘要，含三机制对比、配置优先级、MCP 推荐、Agent Memory、Tasks、Agent Teams、对 Ohmybrain 的启示
- **3 个概念页**：
  - `concepts/subagents-orchestration.md` — 子代理 16 字段 frontmatter + Command→Agent→Skill 编排 + 天气示例 + Agent Teams
  - `concepts/skills-vs-commands.md` — 三机制决策树 + 解析优先级 + "当前时间" 示例 + frontmatter 对照
  - `concepts/claude-hooks-architecture.md` — 15 个生命周期事件 + 作用域层级 + Boris Cherny hook 用法 + 对本仓候选 hook
- **更新 1 个实体页**：`entities/claude-code.md` — 追加三种扩展机制、Agent Memory、Tasks 能力段落，链到新 concept 和 summary

更新了 `index.md`（页面总数 27 → 31）。

---

## [2026-04-13] promote | USBL 定位知识回流

从 USBL 项目 (`D:\Claude\TechReq\USBL`) 回流跨项目知识：

- **新建概念页**：`concepts/usbl-positioning.md` — USBL 技术链路、六层研究体系、商用设备参数表、关键工程经验
- **更新概念页**：`concepts/mimo-and-array-processing.md` — 追加 USBL 阵列处理交叉引用
- **来源**：USBL 项目 9 篇论文文献综述

---

## [2026-04-12] create | 系统架构总览

创建 `architecture/system-overview.md`，文档化六层结构、双闭环（知识+开发）、Harness 机制和工具链架构图。同步升级工程体系：新增 specs/plans/tasks/evals/ 目录、.claude/rules/ 路径规则、.claude/skills/ 技能定义、bash hooks、CI workflow。

---

## [2026-04-12] ingest | UWAcomm 水声通信仿真平台

对 `raw/repos/UWAcomm` 项目执行 ingest，创建了 2 个新 wiki 页面并更新了 6 个概念页：

- **1 个 source-summary 页**：`source-summaries/uwacomm.md` — 项目摘要，含 6 种通信体制性能对比、13 个模块职责、关键技术和端到端信号流
- **1 个实体页**：`entities/uwacomm.md` — 项目实体页，含完整模块架构、性能数据和技术特色
- **更新 6 个概念页**（在来源部分追加 UWAcomm 实现信息）：
  - `concepts/underwater-acoustic-communication.md` — 核心实现项目
  - `concepts/channel-estimation-and-equalization.md` — 15+ 种估计算法 + 10+ 种均衡器
  - `concepts/ofdm-and-otfs.md` — OFDM/OTFS/SC-FDE 多载波变换
  - `concepts/message-passing-algorithms.md` — AMP/VAMP/Turbo-VAMP/MP 消息传递算法
  - `concepts/mimo-and-array-processing.md` — ULA 阵列接收处理
  - `concepts/time-varying-channel.md` — BEM/DD-BEM/Kalman 时变估计 + 多普勒补偿

更新了 `index.md`（页面总数 22 → 24）。

---

## [2026-04-12] create | Zotero 重组方案

基于研究地图生成 Zotero 文件夹重组方案 `explorations/zotero-reorganization.md`，将 64 个文件夹精简为 17 个（10 个研究方向 + 7 个功能性文件夹）。

---

## [2026-04-12] ingest | 3 份原始资料 + 7 个实体页

对 raw/ 目录下 3 份已有资料执行 ingest，创建了 10 个新 wiki 页面：

- **3 个 source-summary 页** `source-summaries/` 目录下：
  - `my-brain-setup-plan.md` — 搭建计划摘要，提取三阶段方案核心内容
  - `toolchain.md` — 工具链指南摘要，梳理各工具职责和架构
  - `zotero-library-catalog.md` — 论文库清单摘要，统计规模和主题分布
- **7 个实体页** `entities/` 目录下：
  - `claude-code.md` — 执行引擎
  - `obsidian.md` — 可视化层
  - `zotero.md` — 论文管理
  - `readwise-reader.md` — 文章收集
  - `whisper.md` — 本地视频转录
  - `firecrawl.md` — YouTube 视频转 markdown
  - `github.md` — 同步与自动化

更新了 `index.md`（页面总数 11 → 21）。

---

## [2026-04-12] create | 研究地图与概念页

基于 Zotero 论文库分析（~3179 篇论文），创建了 11 个 wiki 页面：

- **研究全景地图** `topics/research-map.md` — 展示 10 个研究方向的层次结构、交叉关系和论文分布
- **10 个概念页** `concepts/` 目录下：
  - `underwater-acoustic-communication.md` — 水声通信系统（~1120篇）
  - `channel-estimation-and-equalization.md` — 信道估计与均衡（~335篇）
  - `signal-processing-fundamentals.md` — 信号处理基础（~328篇）
  - `message-passing-algorithms.md` — 消息传递与因子图（~225篇）
  - `mobile-communication.md` — 移动通信（~95篇）
  - `ofdm-and-otfs.md` — OFDM与OTFS调制（~64篇）
  - `mathematical-optimization.md` — 数学与优化（~30篇）
  - `time-varying-channel.md` — 时变信道处理（~22篇）
  - `mimo-and-array-processing.md` — MIMO与阵列处理（~21篇）
  - `machine-learning-methods.md` — 机器学习方法（~2篇）

所有页面使用 `[[wikilink]]` 互相链接，更新了 `index.md`。

---

- 2026-04-12: 初始化 my-brain 仓库，创建目录结构和基础文件
