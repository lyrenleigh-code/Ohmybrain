---
type: architecture
created: 2026-05-24
updated: 2026-09-18
tags: [ADR, 决策, log]
---

# 决策记录 (ADR-style)

跨仓重大架构决策的累积记录。**比 git log 更高粒度**（合并多次 commit），**比 memory 更结构化**（含动机 / 选项 / 后果）。

最新在上。

> **起点声明**：**2026-04-12 为 Ohmybrain 体系起点（ADR-001），此前无历史 ADR**。本页对每个 [[roadmap]] 里程碑追溯一条 ADR，编号 ADR-001 ~ ADR-041（含 ADR-031/032/033 追溯）。早于体系初版的工作（各 project 仓库自身的历史）不在本累积记录范围内。
>
> **编号约定**：ADR 编号为 **append-only 稳定 ID**（按登记顺序递增、不复用、不重排）；表按**事件日期降序**排列。绝大多数情况下编号降序 == 日期降序，但 retroactive 追溯条目（如 ADR-025 事件 2026-06-04、2026-06-09 登记）会出现编号与位置不严格对应——这是为避免重编号引发跨页引用级联失效（教训见 [[../log]] 2026-05-29）而做的取舍。

---

## ADR-050 · 2026-09-18 · AUVNetModem 项目派生（TechReq，面向五U 组网条件的水声通信机详细设计）

### 触发

用户在 AUVNetCoop 会话中提出「需要针对这个组网条件下的水声通信机进行详细的设计，单独做一个项目还是怎么弄比较好」。Claude 建议单独立项并给出范围二选一（A 算法 / B 含硬件）；用户裁「A 和 B 都要包含，可以放在 TechReq 下面」。项目名 `AUVNetModem` 为 Claude 代拟（对齐 AUVNetCoop 命名），用户未反对、可改。

### 决策

独立 TechReq 子项目 `TechReq/AUVNetModem` 🔒（本地 main，无远程，手动模式），按 `template-engineering` + 硬件目录扩展派生（**engineering-hardware 子型第二例**，首例 USBL_hw / ADR-026）。**DEPENDS_ON = AUVNetCoop（需求源）/ UWAcomm（算法底座）/ AUVProposal（平台基线 09-04）**。TechReq 第 9 个正式登记项目，活跃项目 37→38。

**不并入 AUVNetCoop 的理由**：AUVNetCoop 为文档类项目（不写代码），建设方案 v1.8 把通信机限定为「物理层模型接口」、本期取消实物集成；详细设计并入会破坏其「仅软件与数字仿真」划界。**不并入 UWAcomm 的理由**：通用算法公开仓（暂停中、写入权 Codex、三 worktree 归属约束），场景专用设计属其应用；先例 UWAcomm_usbl / USBL_hw / UWAcommTrial 均单独派生依赖 UWAcomm。

**接口（双向、只交换文档）**：AUVNetCoop → 本项目 = 两段链路目标（下层 3–9 kHz / 5–10 km / ≥300 bit/s；上层 15–25 kHz / ≤1 km / ≥1 kbit/s；单次误包率 ≤10%）+ MAC 侧约束（TDMA 保护与恢复时间、≤64 B ALOHA 短报文、≥2 路 FDMA 并发接收、中大型 AUV 两段交替收发、单向到达时间测时）；本项目 → AUVNetCoop = 物理层模型参数包 R1~R8（信噪比–误包率关系、完整帧时长、前导检测与测时、恢复时间与多径裕量、子带与隔离度、功率档与能耗、群时延）。

**硬规则**：平台事实只取 AUVProposal《技术要求》09-04 版；需求事实只取 AUVNetCoop v1.8 / SPEC-012，其旧 SPEC-L1 / L2 算例不作五U 结论；UWAcomm / USBL 为公开仓，本项目资料不回流；沿用「用户主导结论」（不代跑单测、不代下结论、逐 checkpoint 停）。

**待裁 D1~D10**：项目名 / 硬件设计对象范围（推荐：新研 = 中大型 AUV 两段通信机 + 中继型 AUV 上层通信机，探测型 AUV 沿用平台湿端与 VPX）/ 下层发射带宽口径（平台 3～6 kHz ↔ 五U 3–9 kHz）/ 探测型 AUV 接收形态 / 首轮体制候选池 / UWAcomm 复用方式 / 五U 信道输入 / A·B 推进顺序 / 写入权与分工 / 对 AUVNetCoop 的回写。

### 实现

- SOP §1 + §1.5 派生（robocopy template-engineering + 11 个硬件目录 + `src/`）；CLAUDE.md / README.md 占位符全清 + 「项目边界」「当前状态」段；`.gitignore` 补 Office 锁文件（`~$*`）与 MATLAB 自动保存规则（AUVNetCoop 同日入库时暴露的坑）
- 两路只读采集 agent → 项目 wiki 0→2 页：`source-summaries/upstream-inputs-five-u-phy`（v1.8 物理层约束 C1~C14 + 探测型 AUV 平台基线 A1~A11 + 旧通信指标论证 B1~B9 + 两型 U 硬件空白 + 20 条输入缺口；TR 关键条款经主会话回源核对）+ `source-summaries/reusable-assets-inventory`（UWAcomm 7 体制 14 模块 / USBL_hw 收发链与平台 / 哈工程实物通信机；**全部 8–16 kHz、fc = 12 kHz 口径**；可直接引用 / 需适配 / 空白三栏）
- SPEC-001 项目框架 v0（需求输入 / 平台输入 / 上游不一致 U1~U4 / 既有资产 / 边界 / 工作包 A1~A6 + B1~B7 + C1 / 指标初拟不预填无依据数值 / 交付物 / 里程碑 M0~M6 / 风险 K1~K6 / 待裁 D1~D10）
- SOP §6 验证全过（dirs / placeholders / lint_wiki / index-log sync / validate_task）；git init -b main：`c37e2ce` 首 commit（87 文件）
- 登记面（派生当日全量）：root / Hub CLAUDE.md + `projects/auvnetmodem/` 导航卡 + AUVNetCoop / AUVProposal 导航卡「下游派生」行 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_auvnetmodem_init` + memory-index 指针；CANON 级联当日收口（活跃 37→38 / TechReq×8→×9 / ADR ~049→~050 / memory 112→115：project 73→74，另补登 09-18 上一会话两条 PowerShell feedback 35→37 / `MEMORY.md` 索引 →116 行），`--check` 静默
- **登记方式**：后台会话受隔离护栏约束，Hub 登记落在 worktree 分支 `reg/auvnetmodem`（基于 main `efa0b24`），待用户 `git merge --ff-only reg/auvnetmodem`

### 后果

- 项目进入 🟡 待裁：下一步用户裁 D1~D10 → PLAN-001（资料拉齐 + WP 顺序）→ M1 需求基线与接口约定
- AUVNetCoop 首次出现下游派生项目；其两段链路目标或 MAC 约束若变更，须同步本项目 SPEC-001 §1；对 AUVNetCoop 仓内的回写（`CLAUDE.md` 关联项目行 + 接口指针页）须另起明确任务（D10）
- 上游口径出入已显式登记：平台通信发射 3～6 kHz（TR:243）↔ 五U 下层 3–9 kHz；功放 6 kW / 2.5%（TR）↔ 5000 W / ≤2%（论证）；脉冲储能 TR:32 与 TR:93 相反——均待用户或 AUVProposal 侧裁定
- **已知未处理漂移**（本轮不动）：AUVNetCoop 导航卡 / dashboard / Hub CLAUDE.md 仍记「研制技术协议 / `5a6bbfc`」，实为建设方案 v1.8、HEAD `de9ee3a`（09-18 同会话经用户授权入库 `c6fce1a` + `de9ee3a`）

---

## ADR-049 · 2026-09-15 · ProductPortfolio 项目派生（DocProcess，公司产品体系梳理）

### 触发

用户提出「新建一个项目，用于公司产品体系梳理，可引用 xiaojinglaunch 那个项目」。AskUserQuestion 四项——目录名 ProductPortfolio / 主交付物《公司产品体系梳理》docx / 种子复制入 raw/materials / 项目首 commit + Hub 登记 commit——均取推荐项。

### 决策

独立 DocProcess 子项目 `DocProcess/ProductPortfolio` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，**DEPENDS_ON = XiaojingLaunch**（产品架构 deck V3 + 2026-09-08「三核独立 · 一体协同」口径决策 + 公司总体介绍 PPT 均为直接输入）。DocProcess 第 24 个正式登记子项目，活跃项目 36→37。

**口径**：公司级产品体系（非单产品）——把海星100（环境数据）/ 海涛100（声学仿真「算、仿、评」）/ 小鲸100（海洋无人平台智控 · 声学 · 能源三核产品族，「装、用、集成」）/ 海若10（开发运维底座）/ 大模型及智能应用平台统一到一张体系架构图 + 一套产品谱系表 + 一致口径（术语沿革 V1→V2→V3→决策）。主交付物《公司产品体系梳理》docx：6 章（总览 / 谱系 / 协同关系 / 共性底座 / 场景映射 / 术语口径）+ 附 A 谱系总表 + 附 B 来源；图件 F1 分层体系图（archmap L 族）/ F2 各线组成图（composition）/ F3 协同关系图（archmap I 族），素样式 Visio OLE，复用 AUVNetCoop 构建管线。

**硬规则**：同一事实以 XiaojingLaunch 09-08 三核决策为准（晚于 deck V3 09-07）；引用不改源；pptx 种子大件（17~424 MB）.gitignore 不入库。

**待裁 D1~D6**：受众 / 产品线范围（大模型平台与在研是否列）/ 口径基准 / 成熟度分级（在研 · 样机 · 可交付 · 已交付）/ 图件形态 / PPT 汇报版。

### 实现

- SOP §1 派生（robocopy template-document，42 目录 / 73 文件）+ 种子 4 份（XiaojingLaunch raw ×3 + Hub `raw/PPT/` 大模型平台介绍 ×1）→ `raw/materials/`
- CLAUDE.md / README.md 占位符全清 + 「当前状态」段 + 硬规则；`wiki/topics/product-system-baseline.md`（`<private>` 抄录固定口径 + 四产品线 + 沿革，项目页面 0→1）+ SPEC-001 + PLAN-001（M0~M6）
- SOP §6 验证全过（dirs / placeholders / lint_wiki / validate_task / sync_index / index-log sync）；git init -b main：`2a0a591` 首 commit（76 文件，pptx 未入）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/productportfolio/` 导航卡 + XiaojingLaunch 导航卡下游派生行（顺手刷新其现态 a94cf00→0b30cd3）+ dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_productportfolio_init` + memory-index 指针；CANON 级联当日收口（活跃 36→37 / DocProcess×23→×24 / ADR ~048→~049 / memory 111→112 / project 72→73）

### 后果

- 项目进入 🟡 待裁：下一步用户裁 D1~D6 → M0 `/ingest` 4 种子 → M2 谱系总表 → 章节 draft
- XiaojingLaunch 首次出现下游派生项目；其 09-08 口径若再变，本项目 baseline 页与第 6 章沿革须同步
- 公司产品体系口径此后以本项目为单一来源；XiaojingLaunch 等对外材料项目应回引本项目谱系表（回流由用户手动裁决，私人项目禁 promote）
- **同日续（2026-09-15）**：用户放 raw/slides 5 份新料（09-14 简化版取代 deck V3 为主口径源；小鲸发布会 v15.3 = 老板认可叙事骨架）→ 海涛定位讨论 → 项目内 decision-001（主线 A 论证研制 / 海涛出引擎、小鲸仿真试验 = 海涛引擎 + 小鲸接口 / 删「声学载荷支撑」/ 训练参照 AcousticLiteracy sxsy 二期、删红蓝对抗 / sxsy 作海涛应用实例 / 定位「一套引擎 · 三级仿真 · 两条闭环」+ 价值「效果先算清 · 方案再选定 · 训练有数据」）+ decision-002（小鲸两级口径：族级三核 + 智控级 v15.3 原样；能力开发留智控，部分覆盖 XiaojingLaunch 09-08 决策 2，上游不回改）→ **用户收窄范围：只做海涛线，交付物改 6 页小鲸版式 PPT**（SPEC-002 / PLAN-002；SPEC-001 体系 docx 挂起）；AcousticLiteracy 升为参照项目（口径来源，只读引用）；HEAD `2b735bc`
- **2026-09-16**：用户要完整版 → Codex 16 页（.mjs 生成器）与 Claude 20 页（v15.3 原模板全骨架 + 原生架构图）并存；Codex 出审阅清单（A 案例页 / B 技术表述 / C 训练成熟度与闭环 / D 联系方式）+ 案例深化稿（V3 P14「某水声通信原理验证」原图）→ Claude 实施 → 第二轮 R1~R6 → `output/海涛100_产品发布会_完整版_claude_收尾修订版.pptx` 待用户终审；分工模式定型：**Codex 审阅出清单、Claude 实施 PPT**；HEAD `a4696f9`

---

## ADR-048 · 2026-09-14 · AUVNetCoop 项目派生（DocProcess，协同探测型 AUV 组网协同系统）

### 触发

用户提出「根据 AUVProposal 项目，写一个组网协同相关的，要把我们这个 U 用上，先出一个项目框架」。两路探查（AUVProposal 平台事实 + 兄弟项目组网协同口径）后在 `Ohmybrain/draft/` 起草项目框架 v0，用户回「你帮我搭建项目吧」；AskUserQuestion 三项：首 commit 授权 / D1~D9 全按推荐 / Hub 一并 commit——均取推荐项。

### 决策

独立 DocProcess 子项目 `DocProcess/AUVNetCoop` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，**DEPENDS_ON = AUVProposal**（平台基线《技术要求》2026-09-04 版 + 五论证 + 研制技术协议体例 + docx 构建管线均为直接输入）。DocProcess 第 23 个正式登记子项目，活跃项目 35→36。

**口径**：装备 / 工程实现口径，AUV 平台侧。以 AUVProposal 的 1 t 级 / 2000 m 三艇协同探测型 AUV 为底座、硬件零改动，承接研制技术协议 §2.2「后续可扩展」5 项（信息增益编队 / 多艇协同定位融合 / 多基地几何优化 / 动态时隙与自主协商 / 角色重构救援）+ wiki G8「U 间组网协议只有物理层」缺口；论证侧硬约束直接继承（三艇以上时分不码分 / 1000 s 超帧 S1~S5 / 单向互定位 O(N) 占声呐预算 20% / 横队并排同向 / 艇间收 30 km 余量 6.94 dB）。主交付物 《协同探测型AUV组网协同系统研制技术协议》（6 章，同单艇协议体例）。

**划界**（与四个兄弟项目）：不写一体化仿真软件设计（UUVCommSwarmSim，仅作验证工具引用）/ 不做四化五层平台与辅助决策（SoSCommSupport）/ 不用「多阶 · 阶跃 · 耦合度」术语、不做消息价值与语义压缩（CoupledMultiOrder）/ 不做专题课题式拆分（CooperativeDetection 专题二）。Hub 层面「AUV 组网协同」为知识空白（`concepts/uwa-networking` 至今未建），私人项目禁 promote。

**D1~D9 终裁（同日）**：目录名 AUVNetCoop / 研制技术协议体例 / 实装 3 艇 + 1 母艇、协议 ≤8 节点、仿真 ≥10 节点 / 母艇作网关节点 / 研究内容全量（含协同探测与任务闭环）/ 硬件零改动 / UUVCommSwarmSim 仅引用 / 先做论证 1（组网时隙与能量）、2（中继覆盖）/ 独立工作区。

### 实现

- 框架先行：`Ohmybrain/draft/AUVNetCoop/项目框架-v0.md` → 派生后转正为 `specs/active/2026-09-14-SPEC-001-project-framework.md`（定位 / 平台继承 / 立项抓手 / 边界 / 6 分系统研究内容 / 指标初拟 / 6 章大纲 / 10 图件 / 4 前置论证 / D1~D9）+ `wiki/topics/decision-001-framework-ruling.md`（项目 wiki 页面 0→1）
- SOP §1 派生（PowerShell robocopy template-document，42 目录 / 73 文件）+ CLAUDE.md / README.md 占位符全清（README 三图留模板占位加注）+ CLAUDE.md「当前状态」段（含「平台事实基线一律取 09-04 版、禁引 08-03 旧口径」硬规则）；模板 wiki/index.md / log.md 为 CRLF，脚本内先归一 LF 再锚点替换
- SOP §6 验证全过；git init -b main：`5a6bbfc` 首 commit（74 文件）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/auvnetcoop/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_auvnetcoop_init` + memory-index 指针；CANON 级联当日收口（活跃 35→36 / DocProcess×22→×23 / ADR ~047→~048 / memory 110→111 / project 71→72）

### 后果

- 项目进入 🟢 框架终裁：下一步 PLAN-001 → AUVProposal 关键源入 raw/ → 论证 1、2 → 章节 draft
- AUVProposal 首次出现下游派生项目（此前仅 AUVSurvey → AUVProposal 单向）；AUVProposal 基线若再变（技术要求版本升级），本项目 SPEC-001 §1 平台继承表须同步
- 组网协同口径在 DocProcess 内现有四个近邻项目，本 ADR 划界表为后续同域派生的避让参照

---

## ADR-047 · 2026-09-13 · SoSCommSupport 项目派生（DocProcess，体系通信保障）

### 触发

用户提出「新建一个项目，项目名称为体系通信保障」（后台会话，用户不在线）。四项未走 AskUserQuestion、按 ADR-046 推荐口径直取：目录名 `SoSCommSupport`（SoS = System-of-Systems 体系 / Comm 通信 / Support 保障，与 OceanEnvSupport / CommSimSupport 命名风格一致；系代拟，用户如另有偏好可改名并同步登记面）、主交付物**待定先搭架子**、无依赖、派生后 git init + 首 commit。

### 决策

独立 DocProcess 子项目 `DocProcess/SoSCommSupport` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 22 个正式登记子项目，活跃项目 34→35。

沿用「主交付物待定也先搭架子」先例（ADR-034/040/042~046）：主交付物形态（保障方案 docx / 论证报告 / 申报书·立项书 / 汇报 PPT）与口径（「体系」边界——纳入的平台 / 节点 / 链路；保障层次——通信体制 × 组网协议 × 频谱与信道资源 × 抗干扰 × 中继接力 × 海洋环境适配 × 保障组织流程；受众）到位后再落 SPEC-001。

**依赖判定**：UWAcomm（通信体制）/ UWAnet（组网协议）/ UWAprojDoc、CooperativeDetection（体系方案模板与口径）/ OceanEnvSupport（作战保障口径）/ UUVCommSwarmSim（通信组网仿真）均可查询复用，按 conventions「查询不构成依赖」口径记为无——本项目是文档工作区，不以任何仓的代码或仿真结果为构建输入。

### 实现

- SOP §1 派生（PowerShell robocopy template-document）+ CLAUDE.md / README.md 占位符全清（README 三图 + 章节产出物清单留模板占位并加「待 SPEC-001 重写」注；prompts/ 闭环套件占位符按惯例保留）+ CLAUDE.md「当前状态」段（含目录名代拟提示）
- SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）
- git init -b main：`d3831e3` 首 commit（72 文件，工作树干净）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/soscommsupport/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_soscommsupport_init` + memory-index 指针；CANON 级联当日收口（活跃 34→35 / DocProcess×21→×22 / ADR ~046→~047 / memory 109→110 / project 70→71）
- 复用 ADR-046 派生 scratchpad 脚本（scaffold / register）改参数直跑，register 先全量校验锚点再一次性落盘

### 后果

- 项目进入 🟡 待口径：下一步先确认目录名，再与用户讨论主交付物形态 + 口径，议题落 wiki/topics，随后 SPEC-001
- 与同日派生的 UUVCommSwarmSim（通信组网 + 集群控制仿真软件）题域相邻：一个是仿真软件文档、一个是体系级保障方案，口径讨论时一并划清边界；若后续以 UWAcomm / UWAnet 仿真结果为直接输入，需回改 DEPENDS_ON（同 CommSimSupport 先例）
- 目录名若改名：同步 3 处 CLAUDE.md + Hub 登记面 8 页 + 导航卡目录 + auto-memory 文件名与 MEMORY.md 指针

---

## ADR-046 · 2026-09-13 · UUVCommSwarmSim 项目派生（DocProcess，UUV 通信组网与集群控制一体化仿真软件）

### 触发

用户提出按文档模板新建项目《UUV通信组网与集群控制一体化仿真软件》。经确认（AskUserQuestion 四项）：目录名 `UUVCommSwarmSim`（UUV + Comm 通信组网 + Swarm 集群控制 + Sim 仿真软件，与 UWAcomm / SonarSim 命名风格一致）、主交付物**待定先搭架子**、无依赖、派生后 git init + 首 commit——四项均取推荐项。

### 决策

独立 DocProcess 子项目 `DocProcess/UUVCommSwarmSim` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 21 个正式登记子项目，活跃项目 33→34。

沿用「主交付物待定也先搭架子」先例（ADR-034/040/042~045）：主交付物形态（软件研制方案 docx / 申报书·立项书 / 需求规格说明书 / 汇报 PPT）与口径（通信体制 × 组网协议 × 集群控制三域如何一体化、仿真粒度、受众）到位后再落 SPEC-001。

**依赖判定**：通信体制仿真（UWAcomm）、组网协议仿真（UWAnet）、集群协控口径（CoupledMultiOrder）均可复用，但按 conventions「查询不构成依赖」口径记为无——本项目是文档工作区，不以三仓代码或仿真结果为构建输入。

### 实现

- SOP §1 派生（PowerShell robocopy template-document，41 目录 / 73 文件；Git Bash 直跑 robocopy 会把 `/E` 等开关做 MSYS 路径转换、只打印用法）+ CLAUDE.md / README.md 占位符全清（README 三图 + 章节产出物清单留模板占位并加「待 SPEC-001 重写」注；prompts/ 闭环套件占位符按惯例保留）+ CLAUDE.md「当前状态」段
- SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）
- git init -b main：`d06f8f4` 首 commit（72 文件；占位符替换用脚本文件 + chr(92) 拼路径规避 heredoc 反斜杠折叠；含 commit 的命令避开 `-n` 字样以免触发 block-no-verify hook）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/uuvcommswarmsim/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_uuvcommswarmsim_init` + memory-index 指针；CANON 级联当日收口（活跃 33→34 / DocProcess×20→×21 / ADR ~045→~046 / memory 108→109 / project 69→70）

### 后果

- 项目进入 🟡 待口径：下一步与用户讨论主交付物形态 + 口径，议题落 wiki/topics，随后 SPEC-001
- 通信 / 组网 / 集群三域在 DocProcess 首次合为一个仿真软件文档口径；若后续文档以 UWAcomm / UWAnet 仿真结果为直接输入，需回改 DEPENDS_ON（同 CommSimSupport 依赖 UWAcomm 先例）

---

## ADR-045 · 2026-09-04 · AUVSlopeMCM 项目派生（DocProcess，AUV 坡上扫雷）

### 触发

用户提出新建文档撰写类项目「AUV坡上扫雷」。经确认（AskUserQuestion 四项）：目录名 `AUVSlopeMCM`（MCM = Mine Countermeasures，与 AUVSurvey / AUVProposal 同族前缀）、主交付物**待定先搭架子**、无依赖、派生后 git init + 首 commit。

### 决策

独立 DocProcess 子项目 `DocProcess/AUVSlopeMCM` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 20 个正式登记子项目，活跃项目 32→33。

沿用「主交付物待定也先搭架子」先例（ADR-034/040/042/043/044）：任务口径（坡度范围 / 雷型 / AUV 平台 / 探测-识别-处置链路边界）与交付形态（方案 docx / 汇报 PPT / 双交付）到位后再落 SPEC-001。

**依赖判定**：AUV 平台调研（AUVSurvey）与整艇架构口径（AUVProposal）可复用，但按 conventions「查询不构成依赖」口径，DEPENDS_ON 记为无——三者是同域并列项目而非上下游。

### 实现

- SOP §1 派生（robocopy template-document，42 目录 / 73 文件）+ CLAUDE.md / README.md 占位符全清（README 三图 + 章节产出物清单留模板占位并加「待 SPEC-001 重写」注）+ CLAUDE.md「当前状态」段
- SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）
- git init -b main：`723d2fb` 首 commit（单 commit；占位符替换在 commit 前用 Edit 工具完成，沿用 ADR-043 规避 heredoc 反斜杠折叠的做法）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/auvslopemcm/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_auvslopemcm_init` + memory-index 指针；**CANON 级联当日收口**（活跃 32→33 / DocProcess×19→×20 / ADR ~044→~045 / memory 103→106 / feedback 31→33 / project 68→69），并**一并清掉进场时已存在的 13 处机检债**（09-02~03 session 漏级联，「审计后窗口」第 6 次复发）

### 后果

- 项目进入 🟡 待口径：下一步与用户讨论主交付物形态 + 任务口径，议题落 wiki/topics，随后 SPEC-001
- AUV 族三项目并列（AUVSurvey 调研 / AUVProposal 立项论证 / AUVSlopeMCM 作战使用），后续若出现真实上下游关系需回改 DEPENDS_ON
- 反水雷（MCM）为 DocProcess 首例任务域

---

## ADR-044 · 2026-08-31 · AcousticLiteracy 项目派生（DocProcess，声学素养提升项目）

### 触发

用户提出新建文本项目「声学素养提升项目」，要求先出项目模板、随后讨论具体口径。经确认（AskUserQuestion 两项）：目录名 `AcousticLiteracy`、派生后 git init + 首 commit；主交付物形态 / 受众 / 范围留待讨论。

### 决策

独立 DocProcess 子项目 `DocProcess/AcousticLiteracy` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无（待讨论后定）。DocProcess 第 19 个正式登记子项目，活跃项目 31→32。

沿用「主交付物待定也先搭架子」先例（ADR-034/040/042/043）；与既有项目差异：本项目为**素养提升 / 知识建设类**（候选形态：教材 / 讲义 / 课程 PPT / 系列科普文档），DocProcess 内首例，口径讨论走 wiki/topics F-N 议题 → decision-N → SPEC-001。

### 实现

- SOP §1 派生（robocopy template-document）+ CLAUDE.md / README.md 占位符全清（README 三图 + 章节表留模板占位并加注）+ CLAUDE.md「当前状态」段
- SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）
- git init -b main：`88a7379` 首 commit（单 commit）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/acousticliteracy/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_acousticliteracy_init` + memory-index 指针；**CANON 级联当日收口**（活跃 31→32 / DocProcess×18→×19 / ADR ~043→~044 / memory 102→103 / project 67→68），不留审计后窗口债

### 后果

- 项目进入 🟡 待讨论：下一步与用户讨论主交付物形态 / 受众 / 范围，议题落 wiki/topics，随后 SPEC-001
- 领域知识底座：Hub wiki 水声 / 声学 concept 页组可复用（查询不构成依赖）

---

## ADR-043 · 2026-08-31 · XiaojingLaunch 项目派生（DocProcess，小鲸发布会材料）

### 触发

用户提出新建文档项目「小鲸发布会材料」。经确认（AskUserQuestion 四项）：目录名 `XiaojingLaunch`、主交付物 = **发布会 PPT + 演讲稿/串词**（具体口径先搭架子）、无依赖、派生后 git init + 首 commit。

### 决策

独立 DocProcess 子项目 `DocProcess/XiaojingLaunch` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 18 个正式登记子项目，活跃项目 30→31。

沿用 OceanEnvSupport（ADR-034）/ CoupledMultiOrder（ADR-040）/ DeepSeaIndustry（ADR-042）先例：**主交付物待定也先搭架子**——发布会主题 / 产品资料到位后再落 SPEC-001。主交付物含 PPT：产出候选走 `Tools/ppt-master` 引擎（ADR-030；先例 CoupledMultiOrder 汇报 PPT）。

### 实现

- SOP §1 派生（robocopy template-document）+ CLAUDE.md / README.md 占位符全清（README 三图 + 章节表留模板占位并加「待 SPEC-001 重写」注）+ CLAUDE.md 新增「当前状态」段
- SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）
- git init -b main：`a94cf00` 首 commit（73 文件；占位符替换在 commit 前完成，单 commit——吸取 ADR-042 heredoc 反斜杠教训改用 Edit 工具）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/xiaojinglaunch/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_xiaojinglaunch_init` + memory-index 指针；**CANON 级联当日收口**（活跃 30→31 / DocProcess×17→×18 / ADR ~042→~043 / memory 101→102 / project 66→67），不留审计后窗口债

### 后果

- 项目进入 🟡 待口径：下一步由用户提供「小鲸」产品资料 / 发布会需求（定位、卖点、日程、受众），摄入后写 SPEC-001 发布会材料大纲
- 发布会/宣传类为 DocProcess 首例；PPT 先例 CoupledMultiOrder（汇报 PPT 59 页，ppt-master 管线）

---

## ADR-042 · 2026-08-30 · DeepSeaIndustry 项目派生（DocProcess，深海技术产业促进申报书）

### 触发

用户提出依据文档类项目模板新建项目，撰写「深海技术产业促进申报书」。经确认（AskUserQuestion 四项）：英文目录名 `DeepSeaIndustry`、主交付物口径**暂不确定先搭架子**、无依赖、派生后 git init + 首 commit。

### 决策

独立 DocProcess 子项目 `DocProcess/DeepSeaIndustry` 🔒（本地 main，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 17 个正式登记子项目，活跃项目 29→30。

沿用 OceanEnvSupport（ADR-034）/ CoupledMultiOrder（ADR-040）先例：**主交付物待定也先搭架子**——申报类别 / 主管部门 / 官方模板到位后再落 SPEC-001，不因口径未定推迟工作区建立。

### 实现

- SOP §1 派生（cp template-document，73 文件）+ CLAUDE.md / README.md 占位符全清（README 三图 + 章节表留模板占位并加「待 SPEC-001 重写」注）+ CLAUDE.md 新增「当前状态」段（待办：官方材料入 raw/ → /ingest → SPEC-001）
- SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）
- git init -b main：`fa4a663` init（73 文件）→ `97fa2c3` README 占位符填充（首 commit 时 README 替换因 Bash heredoc 反斜杠折叠未命中，补 commit 而非 amend）
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/deepseaindustry/` 导航卡 + dashboard 状态行 + 上次同步头 + system-overview 实例表 + 活跃项目数行 + conventions §9 + 本 ADR + roadmap + log/index + auto-memory `project_deepseaindustry_init` + memory-index 指针；**CANON 级联当日收口**（活跃 29→30 / DocProcess×16→×17 / ADR ~041→~042 / memory 100→101 / project 65→66），不留审计后窗口债

### 后果

- 项目进入 🟡 待口径：下一步由用户提供申报通知 / 模板 / 指南，摄入后写 SPEC-001 申报书大纲
- 申报书类先例：CommSimSupport（立项申报书）；骨架参考 [[../source-summaries/lixiang-lunzheng-report-template]]

---

## ADR-041 · 2026-08-18 · DigitalTwin1plusN 项目退役（体系首例项目退役登记）

### 触发

入会审计（十五）dimension-C 全仓 git-HEAD sweep 发现 `D:\Claude\DocProcess\DigitalTwin1plusN` 目录已不存在（Archive/ 无踪、全盘无匹配）。**用户确认系本人删除**（「这个项目删除了，去掉就可以」）。该仓为本地 git 无远程（12 commit，v0-v5 可研报告 docx 已于 2026-05-25 交付），删除即历史一并移除。

### 决策

**退役登记**（体系首例）：从活跃项目清单移除（活跃 30→29 / DocProcess×17→×16），登记面全量去除或加退役注：root/Hub/DocProcess CLAUDE.md 行删除、`projects/digitaltwin1plusn/` 导航卡删除、dashboard 状态行改 🗑️ 退役墓碑、system-overview 实例表行删除 + 活跃项目数行加「已退役」注、conventions §9 行删除。**历史记录逐字不动**（ADR-019 派生记录 / roadmap 里程碑 / log 历史条目保留）；auto-memory `project_digitaltwin1plusn_init` 保留并加退役注（memory 计数不变）。

下游依赖注记：ImgSonarTwin DEPENDS_ON 含 DigitalTwin1plusN（方案参照）——各登记面依赖括注「已退役」，ImgSonarTwin 自身不受阻（参照性依赖，成稿已完成）。

### 后果

- ✓ 登记面与磁盘现实一致；活跃 29 与机检 ground-truth（导航卡 31−2）对齐。
- ⚠ 该项目 12 commit 本地历史随目录删除不可恢复（交付物 docx 若用户另存则在 git 外）。
- ⚠ 体系新增「退役」生命周期状态先例：退役 = 移出活跃计数 + 墓碑行保留追溯，与「归档」（Archive/ 保留目录）区分。

---

## ADR-040 · 2026-08-05 · CoupledMultiOrder 项目派生（DocProcess，多阶耦合方案文档）

### 触发

用户提出新建项目「多阶耦合」。经确认：主交付物为 docx 方案/报告（document 类）、英文目录名 `CoupledMultiOrder`、无依赖。**具体业务方向（多阶耦合指向哪类对象/问题）用户尚未细化**，本轮只建受管工作区。

### 决策

独立 DocProcess 子项目 `DocProcess/CoupledMultiOrder` 🔒（**git 未 init 待授权**，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 17 个正式登记子项目。

沿用 OceanEnvSupport（ADR-034）先例：**主交付物待定也先搭架子**，方向明确后再落 SPEC-001，不因方向未定推迟工作区建立。

### 实现

- SOP §1 派生（robocopy template-document）+ CLAUDE.md/README.md 占位符全清（README 三图 + 章节表留模板占位待 SPEC-001）+ SOP §6 验证全过（placeholders / dirs / lint / validate / sync_index 0 页）。
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/coupledmultiorder/` 导航卡 + dashboard 状态行 + system-overview 实例表/projects 树 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_coupledmultiorder_init` + log；CANON 级联 **活跃 29→30 / DocProcess×16→×17 / ADR range ~039→~040**。

### 后果

- ✓ 「多阶耦合」有受管工作区，raw/ 可即刻投料，wiki/topics 可承接方向议题。
- ⚠ 项目描述当前为占位口径（「方向待细化」），用户明确后需回刷各登记面（同 OceanEnvSupport「主交付物待定」先例）。
- ⚠ git 未 init（待用户授权）；memory CANON 债 +1（`project_coupledmultiorder_init`）留下轮入会自检收口。

---

## ADR-039 · 2026-07-24 · AUVSurvey 项目派生（DocProcess，AUV 广泛调研）+ AUVProposal 依赖联动

### 触发

AUVProposal（ADR-038，同日）派生后，用户提出**先建独立调研项目做广泛 AUV 调研**，调研结论作建议书素材底座。经确认：项目名 AUVSurvey，主交付物**调研报告**（docx），AUVProposal 依赖同步改为 AUVSurvey。

### 决策

独立 DocProcess 子项目 `DocProcess/AUVSurvey` 🔒（git 未 init 待授权，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无、下游=AUVProposal。**AUVProposal DEPENDS_ON 无→AUVSurvey** 同批联动刷新（项目仓 CLAUDE.md/README + 各 Hub 登记面）。DocProcess 第 16 个正式登记子项目。

### 实现

- SOP §1 派生（robocopy template-document）+ CLAUDE.md/README.md 占位符全清（README 三图留模板占位待 SPEC-001）+ SOP §6 验证全过（placeholders / dirs / lint / validate / sync_index 0 页）。
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/auvsurvey/` 导航卡 + dashboard 状态行 + system-overview 实例表/projects 树 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_auvsurvey_init` + log；CANON 级联 **活跃 28→29 / DocProcess×15→×16 / ADR range ~038→~039**。

### 后果

- ✓ AUV 调研有受管工作区；素材流向确立：AUVSurvey（调研）→ AUVProposal（建议书），避免论证与调研素材混仓。
- ✓ 同日推进：SPEC-001 confirmed（D1-D4）+ 首轮 6 路并行调研落 wiki 6 专题页 + Codex 交接单；同日用户授权两仓 git init 首 commit（AUVSurvey `544bc38` / AUVProposal `5045bb3`，本地 main 无远程）。
- ⚠ memory CANON 债 +1（`project_auvsurvey_init`）留下轮入会自检统一收口。

> memory `project_auvsurvey_init`。关联 ADR-038（AUVProposal）。

---

## ADR-038 · 2026-07-24 · AUVProposal 项目派生（DocProcess，AUV 项目立项论证）

### 触发

用户提出新建 DocProcess 项目，论证一个 AUV 项目。经确认：项目名 AUVProposal，主交付物**项目建议书**（docx），无依赖（独立论证）。

### 决策

独立 DocProcess 子项目 `DocProcess/AUVProposal` 🔒（git 未 init 待授权，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=无。DocProcess 第 15 个正式登记子项目。

### 实现

- SOP §1 派生（robocopy template-document）+ CLAUDE.md/README.md 占位符全清（README 三图留模板占位待 SPEC-001）+ SOP §6 验证全过（placeholders / dirs / lint / validate / sync_index 0 页）。
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/auvproposal/` 导航卡 + dashboard 状态行 + system-overview 实例表/projects 树 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_auvproposal_init` + log；CANON 级联 **活跃 27→28 / DocProcess×14→×15 / ADR range ~037→~038**。

### 后果

- ✓ AUV 立项论证有受管工作区。同日推进：三轮讨论 SPEC-001 confirmed + 02-draft 初稿七章（§6 占位）+ Codex 交接单；同日用户授权 git init 首 commit `5045bb3`（本地 main 无远程）。
- ⚠ memory CANON 债 +1（`project_auvproposal_init`）不在本次范围，连同既往挂账留下轮入会自检统一收口。
- ⚠ 同日更新：DEPENDS_ON 无→**AUVSurvey**（用户随即决定先建广泛调研项目，见 ADR-039，各登记面已联动刷新）。

> memory `project_auvproposal_init`。关联 ADR-032（UWCombatPlatform 含 AUV 论证仿真模块，口径可参照但无依赖）、ADR-039（AUVSurvey）。

---

## ADR-037 · 2026-07-23 · EnvDataClassify 项目派生（TechReq，环境数据分类）

### 触发

用户提出新项目「数据分类」，澄清为**环境数据分类**（海洋环境数据：声速剖面/水文条件等的自动分类）。与 SonarFOM 本 session 刚落地的水文五档分类（`classifyHydrology`）高度相关，需独立工作区承接更通用的环境数据分类。

### 决策

独立 TechReq 子项目 `TechReq/EnvDataClassify` 🔒（本地 main 无远程，手动模式），按 `template-engineering` SOP 派生，DEPENDS_ON=SonarFOM 🔒（水文五档分类判据经验参考，引用不复制）。TechReq 第 8 个正式登记子项目。

### 实现

- SOP §1 派生（robocopy template-engineering）+ CLAUDE.md/README.md 占位符全清 + SOP §6 验证全过（placeholders / dirs / lint / validate / sync_index 0 页）+ §3 git init -b main 首 commit `a7de7b2`（用户授权）。
- 登记面（派生当日全量）：root / Hub CLAUDE.md + `projects/envdataclassify/` 导航卡 + dashboard 状态行 + system-overview 实例表/projects 树 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_envdataclassify_init` + log；CANON 级联 **活跃 26→27 / TechReq×7→×8 / ADR range ~036→~037**。

### 后果

- ✓ 环境数据分类有受管工作区；分类实现未启动，待 SPEC-001（分类对象/特征/方法）。
- ⚠ memory CANON 债 +1（`project_envdataclassify_init`）不在本次范围，连同既往挂账留下轮入会自检统一收口（同 ADR-036 先例）。

> memory `project_envdataclassify_init`。关联 ADR-036（SonarFOM）。

---

## ADR-036 · 2026-07-21 · SonarFOM 项目派生（TechReq，声呐效能 FOM 品质因数表计算）

### 触发

用户提出新计算任务「声呐效能 FORM 表计算」（经确认 FORM = FOM 品质因数），需独立工作区承接声呐方程逐项计算 + 作用距离预报表的 MATLAB 实现。

### 决策

独立 TechReq 子项目 `TechReq/SonarFOM` 🔒（本地 main 无远程，手动模式），按 `template-engineering` SOP 派生，DEPENDS_ON=SonarSim 🔒（主动声呐探测链路与场景参数口径参考，引用不复制）。TechReq 第 7 个正式登记子项目。

### 实现

- SOP §1 派生（robocopy template-engineering，72 文件）+ CLAUDE.md / README.md 占位符全清（README 三图留模板占位，待 SPEC-001 重绘）+ SOP §6 验证全过（placeholders / dirs / lint / validate / sync_index 0 页）+ §3 git init -b main 首 commit `fb00819`（用户已授权）。
- 登记面（派生当日全量）：root / Hub CLAUDE.md + `projects/sonarfom/` 导航卡 + dashboard 状态行 + system-overview 实例表 + projects 树 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_sonarfom_init` + log；CANON 级联 **活跃 25→26 / TechReq×6→×7 / ADR range ~035→~036**。

### 后果

- ✓ 声呐效能 FOM 计算有受管工作区；计算实现未启动，待 SPEC-001（FOM 参数口径 + 表格式）。
- ⚠ memory CANON 债 +1（`project_sonarfom_init`）不在本次范围，连同 07-18 已挂账的 95→98 级联留下轮入会自检统一收口（同 ADR-035 先例）。

> memory `project_sonarfom_init`。关联 ADR-022（SonarSim）。

---

## ADR-035 · 2026-07-18 · ImgSonarTwin 项目派生（DocProcess，图像声呐数字孪生方案文档）

### 触发

用户提出新文档项目主题「图像声呐数字孪生」，需独立工作区承接方案文档撰写；主交付物 docx（定稿名待定）。

### 决策

独立 DocProcess 子项目 `DocProcess/ImgSonarTwin` 🔒（本地 main 无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=DigitalTwinGuide（数字孪生实施指南方法论）+ DigitalTwin1plusN（水下集群数字孪生体系方案参照）。DocProcess 第 14 个正式登记子项目。

### 实现

- SOP §1 派生（robocopy 42 目录 / 73 文件）+ CLAUDE.md / README.md 占位符全清（README 三图留模板占位，待 SPEC-001 重绘）+ SOP §6 验证全过（placeholders / lint / validate / sync_index 0 页）。
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/imgsonartwin/` 导航卡 + dashboard 状态行 + system-overview 实例表 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_imgsonartwin_init` + log；CANON 级联 **活跃 24→25 / DocProcess×13→×14 / ADR range ~034→~035**。

### 后果

- ✓ 图像声呐数字孪生方案文档有受管工作区；撰写未启动，待 raw/ 资料摄入 + SPEC-001 章节大纲。
- ⚠ memory CANON（95→98，含进场前已欠的 07-13/07-15 两条 UWAcomm session memory）级联 + memory-index 3 条指针不在本次范围，留下轮入会自检统一收口（同 ADR-034 先例）。

> memory `project_imgsonartwin_init`。关联 ADR-015（DigitalTwinGuide）/ ADR-019（DigitalTwin1plusN）。

---

## ADR-034 · 2026-07-09 · OceanEnvSupport 项目派生（DocProcess，海洋环境数据作战保障方案文档）

### 触发

用户提出新文档项目主题「海洋环境数据作战保障」（水文 / 气象 / 声学环境 / 海底地形底质等环境数据的采集 → 处理 → 产品 → 战场应用保障链路），需独立工作区承接；主交付物类型（建设方案 / 论证申报 / 技术方案）尚未确定，先搭架子。

### 决策

独立 DocProcess 子项目 `DocProcess/OceanEnvSupport` 🔒（**git 未 init**——用户未授权 git 操作，同 CommSimSupport 先例；无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=UWAprojDoc（方案文档体系 / 模板 / build pipeline 参照）+ CooperativeDetection（协同探测论证素材参照）。DocProcess 第 13 个正式登记子项目。

### 实现

- SOP §1 派生（robocopy 42 目录 / 73 文件）+ CLAUDE.md / README.md 占位符全清（README 三图留 ⚠️ 模板占位，待 SPEC-001 重绘）+ SOP §6 验证全过（dirs / placeholders / lint / validate / sync_index 0 页）。
- 登记面（派生当日全量）：root / Hub / DocProcess CLAUDE.md + `projects/oceanenvsupport/` 导航卡 + dashboard 状态行 + system-overview 实例表 + conventions §9 + 本 ADR + roadmap 里程碑 + auto-memory `project_oceanenvsupport_init` + log；CANON 级联 **活跃 22→24 / DocProcess×11→×13 / ADR range ~032→~034**（含 ADR-033 CommSimSupport 追溯补登）。
- 对抗验证 workflow（3 agent：scaffold 0 issue / registration 1 low / completeness 7 findings）驱动本次级联收口。

### 后果

- ✓ 海洋环境数据作战保障文档有受管工作区；SPEC-001 推迟到需求材料 `/ingest` 后立（与 CommSimSupport「临时骨架先立」做法不同，推迟理由已写入项目 CLAUDE.md）。
- ⚠ git 未 init：待用户授权后 `git init -b main` + 首 commit。〔07-09 当日已授权并完成：init + 2 commit（`7424fc0` 脚手架 / `22f9aa0` F-1 架构设计草案）〕
- ⚠ memory CANON（87→9x）存量债 + memory-index 指针不在本次范围，留下轮入会自检统一收口。

> memory `project_oceanenvsupport_init`。关联 ADR-033（CommSimSupport，同批补登）。

---

## ADR-033 · 2026-07-01 · CommSimSupport 项目派生（DocProcess，通信机仿真使用支持立项申报书）〔2026-07-09 追溯补登〕

### 触发

需要以 UWAcomm 多体制水声通信仿真为「使用支持」能力底座，撰写可送审的项目/课题立项申报书。07-01 派生当日仅登 Hub CLAUDE.md 映射 + projects 导航卡（Hub commit `4121506`），其余登记面漏——「部分登记」反模式**第 8 轮复发**；本条为 2026-07-09 OceanEnvSupport 派生对抗验证时追溯补登。

### 决策

独立 DocProcess 子项目 `DocProcess/CommSimSupport` 🔒（git 未 init，无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=UWAcomm。DocProcess 第 12 个正式登记子项目。

### 实现

- 脚手架派生 + SPEC-001 临时骨架（申报书通用结构，待官方模板放入 `raw/` 并 `/ingest` 对齐必填项）+ auto-memory `project_commsimsupport_init`。
- 2026-07-09 补登面：dashboard 状态行 + system-overview 实例表 + conventions §9 + 本 ADR + roadmap 里程碑 + log。

### 后果

- ✓ 申报书撰写有受管工作区；待官方立项申报书模板 ingest 后启动起草。
- ⚠ 派生当日「部分登记」复发（第 8 轮），本批收口；后续派生须按 ADR-032「派生当日全量登记」执行。

> memory `project_commsimsupport_init`。关联 ADR-034（OceanEnvSupport）。

---

## ADR-032 · 2026-06-25 · UWCombatPlatform 项目派生（DocProcess，水下作战试验平台建设方案 + 报价）

### 触发

甲方（水下作战信息实验室，含大型水池）需要**水下作战试验平台建设方案 + 报价**初稿（2026-06-26 截稿），全链条 6 模块（UUV论证仿真 / 硬件国产化 / 感知通信 / 水池半实物 / 智能对抗集群 / 应用验证）。同日 ingest 甲方「综合论证报告模板」脱敏为 Hub `lixiang-lunzheng-report-template`，需独立工作区承接撰写。

### 决策

独立 DocProcess 子项目 `DocProcess/UWCombatPlatform` 🔒（git 本地 main 无远程，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=UWAcomm / SonarSim / USBL（已有水声仿真基础）+ Pricing（4 号文软件报价口径）。DocProcess 第 11 个正式登记子项目。**涉密 docx（甲方原始模板）gitignore `raw/notes/*.docx`，不入 git**。

### 实现

- SOP §1 派生（copy template-document）+ 占位符填充 + git init（本地 🔒，73 文件暂存）+ SPEC-001（建设方案 + 报价大纲）+ 甲方 docx 复制到 `raw/notes/`（gitignore）。
- Hub 全 12 面登记（**派生当日全量，吸取连续 7 轮「部分登记」教训**）：root/Hub/DocProcess CLAUDE.md + `projects/uwcombatplatform/` 导航卡 + dashboard 状态行 + system-overview 实例表 + 本 ADR + roadmap 里程碑 + memory-index + memory `project_uwcombatplatform_init` + log；CANON 级联 活跃 21→22 / DocProcess×10→×11 / memory 85→86 / project 60→61 / ADR range ~031→~032。

### 后果

- ✓ 水下作战平台建设方案有受管工作区，复用已有水声仿真基础 + 立项论证模板 + 4 号文报价口径。
- ✓ 派生当日**全量登记**（不留部分登记）。
- ⚠ scope 限「建设方案 + 报价」（非完整 18 节论证）；技术指标 / 设备清单 / 报价数据待甲方/用户提供（专家主导，不代编）。
- ⚠ 涉密：raw docx 已 gitignore，禁推公开远程。

> memory `project_uwcombatplatform_init`。spec `DocProcess/UWCombatPlatform/specs/active/2026-06-25-uuv-combat-platform-proposal.md`。关联 ADR-031（UWAcommTrial）、同日 ingest 源摘要 `lixiang-lunzheng-report-template`。

---

## ADR-031 · 2026-06-24 · UWAcommTrial 项目派生（DocProcess，UWAcomm 多模通信机通信距离湖上试验大纲）

> **追溯登记**（事件 2026-06-24，2026-06-25 入会自检（七）补登 ADR）：派生当日只登 root/Hub/DocProcess CLAUDE.md ×3 + `projects/` 导航卡，漏 ADR / dashboard / system-overview 实例表 / roadmap / memory-index / log / auto-memory / 活跃项目计数，属「部分登记」反模式连续第 7 轮复发，本次收口。

### 触发

需要一个专门工作区完善 UWAcomm 多模通信机的**通信距离性能湖上试验大纲**，并产 13 张记录表逐表分页附件。依赖 UWAcomm（`D:\Claude\TechReq\UWAcomm` 多体制水声通信算法仿真源）。

### 决策

独立 DocProcess 子项目 `DocProcess/UWAcommTrial` 🔒（**源仓无 git**，手动模式），按 `template-document` SOP 派生，DEPENDS_ON=UWAcomm。DocProcess 第 10 个正式登记子项目（papers 仍未正式登记，见 [[../topics/ecosystem-dashboard]] / 本页待裁）。

### 实现

- SOP §1 派生 + `projects/uwacommtrial/` 导航卡 + memory `project_uwacommtrial_init` + log（事件 2026-06-24）。
- dashboard 状态行 / system-overview 实例表 + 活跃计数 20→21、DocProcess×9→×10 / memory-index project 组（59→60）/ 本 ADR / roadmap 里程碑 / auto-memory 于 **2026-06-25 入会自检（七）补登**（4 维 workflow，18 agent / 14 confirmed / 0 假阴性，主会话逐条复核）。

### 后果

- ✓ 多模通信机通信距离湖上试验大纲有受管工作区，与 UWAcomm 仿真源挂钩。
- ✓ v1 已交付归档（大纲完善：补目的 / 依据 / 对象 / 判据 / 组织 / 安全 / 数据归档 + 13 张记录表逐表分页附件，SPEC-001 已 archive）。
- ⚠ 派生当日「部分登记」漏 8 面——反模式连续第 7 轮复发；根因盲区 = `dashboard_snapshot.py --check` 只机检 memory/skills 计数，**不校验项目登记面 / 活跃计数**（见 [[../log]] 2026-06-25）。

> memory `project_uwacommtrial_init`。关联 ADR-029（PaperTrans 派生，同属 template-document DocProcess 追溯登记）。

---

## ADR-030 · 2026-06-24 · 采纳 ppt-master 作通用 PPT deck 引擎 + FIELDBOOK 迁模板 + AnthropicPPT 降级

### 触发

用户提供 `hugohe3/ppt-master`（30.8k★ MIT）问"怎么借鉴"。`Tools/AnthropicPPT` 的 python-pptx **命令式**生成（`modify_v3/v4_stepN`）每个 deck 重搓一长串脆弱脚本、9 固定 layout 是天花板、品牌锁死 FIELDBOOK。

### 决策

**采纳整个 ppt-master skill**（不重造 30.8k★ 轮子）作通用 PPT 生成引擎；FIELDBOOK 真资产（设计 IP）迁为 ppt-master **`fieldbook` brand + deck 模板**；`AnthropicPPT` 降级为 FIELDBOOK 设计 source-of-truth + 历史归档。ppt-master 定性=**第三方 vendored 工具**（类 [[../architecture/system-overview]] 的 External/open-design，**非 ohmybrain-core 派生项目，不计入"活跃项目数"**），落点 `D:\Claude\Tools\ppt-master`。

### 核心机制

ppt-master = agent **逐页手写 SVG**（LLM 母语，自由版式）→ `svg_to_pptx`（drawingml_converter 包）转**原生 DrawingML**（圆角矩形 rx/ry→prstGeom、文本→可编辑文本框、**零栅格化**）。解耦"设计"与"pptx 机制"。

### 实现

- **保真度 GATE 通过**：手写 FIELDBOOK 测试 SVG → 37 形状 / 0 图片；deck 模板 5 页端到端 → 5/5 原生 / 全 0 图片；用户 PowerPoint 眼检视觉+可编辑性过。
- `fieldbook` **brand**（`templates/brands/fieldbook/`，区别官方 anthropic：纸底非白/铁锈红非 coral/衬线非 sans）+ **deck**（`templates/decks/fieldbook/` 5 SVG，5 agent 并行 authoring + 主会话校验）。
- vendor 到 `Tools/ppt-master`（sparse+blobless clone 只取 skills/ppt-master，精简无 examples，git 可 `update_repo.py`）。
- `anthropic-ppt` skill 改路由到 ppt-master+fieldbook（**复用槽，无新增 skill，本地 skill 仍 32**）。
- `AnthropicPPT` 降级（CLAUDE.md/README banner + `modify_v4_step*`→`scripts/legacy/`）。

### 后果

- ✓ FIELDBOOK PPT 走 SVG-native 引擎，突破固定 layout 天花板，产物原生可编辑。
- ✓ 不重造轮子（30.8k★ 活跃维护 v2.11）。
- ⚠ 跑 ppt-master 外部脚本需**用户授权**（auto-mode classifier 拦新克隆外部代码 + agent 不得自我改 settings 提权）→ 加 `Bash(python scripts/*.py:*)` allow 规则或 `!` 自跑。
- ⚠ 与 flowgen（Visio 可编辑线条图）/ FieldKit（氛围位图，ADR-027/028）边界互补：**ppt-master = 完整 deck**。

> memory `project_ppt_master_adoption_2026-06-24`。spec：`Tools/AnthropicPPT/specs/active/2026-06-24-adopt-ppt-master-plan-a.md`。关联 ADR-017（AnthropicPPT 派生）、ADR-027/028（FieldKit/carve-out）。

---

## ADR-029 · 2026-06-15 · PaperTrans 项目派生（DocProcess，外文论文英译中翻译工作区）

> **追溯登记**（事件 2026-06-15，2026-06-24 入会自检（六）补登 ADR）：派生当日只登 CLAUDE.md ×2 + `projects/` 导航 + log + memory，漏 ADR / dashboard / system-overview / memory-index / 活跃项目计数，属「部分登记」反模式复发，本次收口。

### 触发

需要一个专门的**外文（英文为主）学术论文 → 术语一致中文译稿**工作区（水声 / 通信 / 信号处理领域优先）。翻译与 PaperReview（中文论文外审）、papers（论文写作）域不同，需独立的术语单一可信源 + 单篇 spec 闭环。

### 决策

**独立 DocProcess 子项目** `DocProcess/PaperTrans` 🔒（git 仅本地 main、无远程，手动模式），**按 template-document SOP 派生**。核心约定：**一篇论文 = 一份 spec = 一份译稿**；wiki `glossary.md` 为术语单一可信源；4 步翻译闭环（01-spec → 02-draft → 03-validate → 04-archive）对齐 `workflows/document/`。DocProcess 第 10 个正式登记子项目。

### 实现

- SOP §1 派生（template-document，占位符全清，CLAUDE.md/README 改写为翻译语境）+ wiki 两页种子（`glossary.md` 术语表 + `concepts/translation-conventions.md` 英译中风格指南）+ 单篇 spec 模板。
- Hub 登记：CLAUDE.md ×2 + `projects/papertrans/` 导航卡 + memory `project_papertrans_init` + log（2026-06-15）；**dashboard / system-overview 实例表 / memory-index / 本 ADR / 活跃项目计数 19→20、DocProcess×8→×9 于 2026-06-24 入会自检（六）补登**。

### 后果

- ✓ 外文论文翻译有受管工作区，术语一致性有单一可信源。
- ✓ 首篇已产出全书译稿（23 单元草稿 + 367 页 PDF 待终审，HEAD `ed1a7ad`/06-16）。
- ⚠ 派生当日「部分登记」（漏 5 个登记面）——再次印证新项目派生须过全套登记面 checklist（见 [[../concepts/anti-patterns]] 「部分登记」反模式 + [[../topics/memory-index]]）。

> memory `project_papertrans_init`。关联 ADR-013（PaperReview，同类 DocProcess 手动文档项目）。

---

## ADR-028 · 2026-06-15 · flowgen 风格图例外（styled-figure carve-out）

### 触发

硬规则 `feedback_doc_flowgen_only`（[[../concepts/anti-patterns]]）要求**方案/方法论文档的图一律走 flowgen* 8 skill → Visio .vsdx**，禁 matplotlib mock / 手画 SVG。但 ADR-027 的「校准场 / Calibration Field」图风系统专产**封面 / 章节扉页 / 总览风格配图**（HTML/SVG→PNG/PDF 位图终稿），与该硬规则字面冲突。用户批准开一个**窄口径例外**。

### 决策

对 `feedback_doc_flowgen_only` 增**用户批准的 carve-out**：**非可编辑的风格配图**（封面 / 章节扉页 / 总览 / cover / overview）**可改走校准场路径**（`Tools/FieldKit` HTML/SVG→PNG/PDF 或 `Tools/AnthropicPPT` `templates/styled_diagram.py`）。**判据（须同时满足）**：① 是封面/扉页/总览风格配图，非流程/架构/时序/组成业务线条图；② 产物是位图/PDF 终稿，不需后期在 Visio 改字改框。**回弹规则**：只要是「可编辑线条图」或带「业务流程/架构/时序/组成」语义，即使想风格化也**必须回 flowgen→.vsdx**。本例外**不放宽**「手画 SVG mock 冒充流程图」禁令——校准场是受管的可复用 kit。

### 实现

- memory `feedback_doc_flowgen_only.md`：决策树表后增「风格图例外 / 校准场分流」节 + 例外条件追加交叉引用 bullet。
- skill `flowgen-archposter/SKILL.md`：决策树加 off-ramp 分支 + anti-trigger 表加一行（封面/总览风格图 → `calibration-field`，非 flowgen）。

### 后果

- ✓ 校准场图风系统有合法落地通道，硬规则不再字面冲突。
- ✓ 边界写死「可编辑线条图回弹 flowgen」，防例外被滥用为「风格化冒充流程图」。
- ⚠ 判据靠人工分流（封面/总览 vs 业务线条图），误判风险待观察；anti-trigger 行 + 回弹规则兜底。

> memory `feedback_doc_flowgen_only`。关联 ADR-027（FieldKit 派生）。

---

## ADR-027 · 2026-06-15 · FieldKit 项目派生（Tools，校准场图风系统）

### 触发

方案文档/演示需要一套**风格化封面 / 章节 / 总览配图**能力（非可编辑业务线条图）——flowgen→Visio 擅长可编辑线条图，但产不出有氛围层（冷暗漆面 / 纸感）的位图/PDF 终稿。借鉴 `pbakaus/impeccable` 的「校准场」图风，沉淀为可复用的共享 design kit + 出图消费者。

### 决策

**独立工具项目** `Tools/FieldKit`（git 仅本地 main、无远程，HEAD `aa93de0`），承载「**Calibration Field / 校准场**」图示风格系统，**按 template-tool SOP 派生**——产品包 `fieldkit/` + `kit.css` + `examples/` + `tests/` + 协作层 `specs/`（含 retroactive **SPEC-001**）/`plans/`/`handoff/`/`wiki/`/`.claude/`/`raw/` + `AGENTS.md`/`CLAUDE.md`。**登记沿革**：派生当日先以 lean 工作目录跑通产品（消费者①/② v1/v2），同会话经 Hub 入会自检发现 lean 缺口后**补全 SOP 脚手架 + SPEC-001 retroactive**。独立成项目（非并入 AnthropicPPT）理由：① 横切多消费者的共享 kit；② AnthropicPPT 是既有已登记项目，其 `styled_diagram` 是增能不是新项目。

### 实现

- 新建 `Tools/FieldKit`（lean dir）：共享 kit（design tokens + `kit.css` + sonar motif + `bake_atmosphere.py` 分辨率无关氛围层 baker）。
- **消费者①** = HTML→PNG/PDF 生成器（flow + composition，暗「Lacquer Instrument」+ 亮「Paper Field」双调色板）= SHIPPED v1（`ced9bc6`）。
- **消费者②** = 既有 `Tools/AnthropicPPT` 增 `templates/styled_diagram.py` + 氛围层资产（`56f79da`）= SHIPPED v2（增能，不计新项目）。
- 全局 skill `calibration-field` 已注册（`~/.claude/skills/`，2026-06-15）。
- Hub 登记：CLAUDE.md ×2 + `projects/fieldkit/` 导航卡 + dashboard + system-overview + roadmap + memory `project_fieldkit_init` + log/index（活跃 18→19、Tools×3→×4、导航 19→20、memory 80→81）。

### 后果

- ✓ 风格化封面/总览配图有了受管可复用的 kit；AnthropicPPT 与 FieldKit 互补。
- ✓ 按 template-tool SOP 完整脚手架，specs/plans/handoff/wiki 齐备，跨会话续作有据。
- ⚠ flowgen-lite（消费者③ Visio 骨架版）暂未做（保真天花板低，可选）。
- ⚠ 关联 ADR-028 carve-out 须严守边界：校准场只接非可编辑风格图。

> memory `project_fieldkit_init`。关联 ADR-028、AnthropicPPT（ADR-017）。

---

## ADR-026 · 2026-06-10 · USBL_hw 项目派生（engineering-hardware 子型首例）

### 触发

用户提出新建「USBL硬件设计」项目，并问应作 USBL 分支还是独立项目。

### 决策

**独立项目** `TechReq/USBL_hw` 🔒（手动模式，git 仅本地 main、无远程）。理由：① USBL 主仓是**公开 GitHub 仓**，硬件资料（基阵/电路/BOM/样机）必须私密，不能走其分支；② 交付物域不同（图纸/BOM/datasheet vs MATLAB 算法），二进制设计资料不宜混入算法仓历史；③ 沿 ADR 前一日口径走 **engineering-hardware 子型**（`template-engineering/` + `design/{requirements,schematics,pcb,mechanical,interfaces,reviews}` + `bom/ datasheets/ prototypes/ output/ tests/` 扩展）——子型**首例**，目录结构经实战验证后可升格 `template-hardware`（触发条件：第 2 个纯硬件项目出现时再立独立分类，同 flowgen-archmap「≥2 族成型再独立」判据）。

### 实现

SOP §1+§1.5 派生 + 占位符填充 + CLAUDE.md 项目边界表（阵元校准算法 / CAGE5 实测数据 / 三板架构留 UWAcomm_usbl，硬件本体设计归本项目，跨界引用不复制）+ git init -b main（未 commit，待授权）+ Hub 全量登记（CLAUDE.md ×2 / projects/ 导航 / dashboard / system-overview / roadmap / memory ×3 / log+index）。

---

## ADR-024 · 2026-06-09 · Claude+Codex 协作协议层落地

### 触发

Claude Code 与 Codex 双 agent 在 `D:\Claude` 协作缺乏稳定文件接口，依赖临时聊天上下文；worktree 边界、交接、审查 / 完成契约无成文协议。用户提出「Claude Code 和 Codex 联合使用场景」+「文档结构重新构建」需求。

### 决策

建立「先建文档协议层、不移动代码路径」的协作层：新增 3 个 Hub wiki 页（`document-protocol` / `claude-codex-collaboration` / `agent-handoff`），以 `specs/active` + `plans/active` + `handoff/active` + `wiki` 为双 agent 稳定接口；迁移只做 L0+L1（补 `handoff/`、`AGENTS.md`），L3 移动项目根须用户明确批准。

### 实现

- 新建 `wiki/architecture/document-protocol.md`（三层结构 + 标准项目骨架 + 路径安全 + L0-L3 迁移级别）
- 新建 `wiki/agents/claude-codex-collaboration.md`（默认角色 + 串行 / 并行 / 红队三模式 + worktree / 审查 / 完成契约）——首个 `agents/` 分类页
- 新建 `wiki/workflows/agent-handoff.md`（交接单模板 + 创建 / 归档标准）——首个 `workflows/` 分类页
- 根 `D:\Claude\AGENTS.md` 从单纯 `@CLAUDE.md` 扩展为 agent 协作入口，`CLAUDE.md` 增「Agent 协作协议层」节，均指向这 3 页
- `index.md` 加 Agents / Workflows 两章节 + 页数 104→107，`log.md` 加 [2026-06-09] entry

### 后果

- ✓ 双 agent 协作有了文件级 single source of truth；wiki 新增 `agents/` + `workflows/` 两个分类（架构级，非单项目派生）
- ✓ 入会自检一致性审计（二）配套收尾：6 cluster workflow / 31 finding，修计数 104→107 跨 6 文件 + 3 新页 conventions §3 合规（frontmatter + wikilink）+ 4 处交叉链
- ⚠ 协议层属「先建协议、后迁项目」L0+L1 阶段，各项目根 `handoff/` / `AGENTS.md` 实体补齐待逐项目推进

> memory `project_ohmybrain_agent_collab_protocol`。

---

## ADR-025 · 2026-06-04 · FlowGen archmap 渲染器族扩展

> **追溯登记**：事件发生于 2026-06-01~04，本条于 2026-06-09 入会自检追溯补登。编号 ADR-025（append-only 稳定 ID，不重排既有编号），故本条按事件日期排在 ADR-024（2026-06-09）之后、ADR-023（2026-06-03）之前——**编号与表中位置不严格对应属正常**（见起点声明）。

### 触发

方案 / 文档项目（UWAprojDoc / CooperativeASW / VisioForge 等）对「系统 / 逻辑 / 业务 / 数据 / 功能架构图」「分系统接口图」等高密度架构图需求激增；既有 flowgen-* skill（vsdx / layered / sequence / composition / roadmap / replica / archposter）覆盖不到「水平分层 + 左层头」与「中心辐射 hub-spoke」两类拓扑。

### 决策

不新开独立 skill，而是在 `flowgen-archposter` 内**孵化托管 archmap 渲染器族**，共享冷蓝核 `arch_style_lib.py`；是否最终单列为独立 `flowgen-archmap` skill **暂缓**（待 ≥2 新族成型后再决）。Claude 构造 SPEC → 调本地 Python 模板（archmap 同款模式），不强塞 CLI。

### 实现

- **L 族** `templates/archmap_layered.py`（A3 竖版）：覆盖系统 / 逻辑 / 业务 / 数据 / 功能架构图——水平分层 + 左层头 + 可选（层内子分组 / 顶部价值带 / 底部贯穿带 / 右纵贯穿带 / 层间连接器）；`fill` 三档 auto / max / compact
- **I 族** `templates/archmap_interface.py`（A3 横版）：中心辐射 hub-spoke（由 CooperativeASW 图 4-1/1-2 催生，见 ADR-023）
- business / data-functional / stdflow 多 renderer + fixtures
- 阶段1 系统架构图 commit `5372721`（已 push gitlab）；阶段2-A 逻辑架构图（2026-06-02）；2026-06-04 archmap 多 renderer 落地

### 后果

- ✓ 方案文档「分层 / 接口」两类架构图纳入 flowgen 体系，统一冷蓝 PPT 商务风
- ✓ memory `feedback_doc_flowgen_only`：所有方案 / 方法论文档的图必须走 flowgen* 8 skill 之一
- ⚠ archmap 族是否单列独立 skill 暂未决（托管于 flowgen-archposter）；改共享 lib 影响全族样式
- ⚠ 改共享渲染引擎 `replica_layered_lib.py` 会波及前 7 张「分系统架构图」复刻样式（per memory `project_flowgen_m8_layered_replica`）

> memory `project_flowgen_archmap_b2_layered` / `project_flowgen_archposter_ppt_restyle`。

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
