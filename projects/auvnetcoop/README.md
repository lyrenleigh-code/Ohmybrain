# AUVNetCoop 🔒

> 协同探测型 AUV 组网协同系统项目文档工作区——以 AUVProposal 1 t 级 / 2000 m 三艇协同探测型 AUV 为平台底座、硬件零改动，承接研制技术协议 §2.2「后续可扩展」5 项 + G8 U 间组网协议缺口：艇间水声组网协议栈（TDMA 超帧 / 寻址中继 / 6 类消息）+ 多艇协同定位（OWTT）与协同探测任务闭环 + 多艇协同验证环境。主交付物 《协同探测型AUV组网协同系统研制技术协议》。

- **仓库**：`D:\Claude\DocProcess\AUVNetCoop`
- **类型**：document（`template-document` 派生，2026-09-14，ADR-048）
- **状态**：🟢 框架终裁（SPEC-001 D1~D9 全按推荐）
- **依赖**：[[../auvproposal/README|AUVProposal]]（平台基线《技术要求》09-04 版 + 五论证 + 研制技术协议体例 + docx 构建管线）；查询复用不构成依赖：[[../auvsurvey/README|AUVSurvey]] / [[../uwanet/README|UWAnet]] / [[../uuvcommswarmsim/README|UUVCommSwarmSim]]（仅作验证工具引用）/ [[../coupledmultiorder/README|CoupledMultiOrder]]（术语避让）
- **下游派生**：[[../auvnetmodem/README|AUVNetModem]]（2026-09-18，ADR-050）——通信机详细设计（算法 + 硬件）单列；本项目只保留「物理层模型接口」，由其回物理层模型参数包；两段链路目标或 MAC 约束若变更须同步其 SPEC-001 §1
- **git**：本地 `main` `5a6bbfc`，无远程（🔒 私人，禁 push 公开仓）

## 当前焦点

派生当日（2026-09-14）：框架先行——`specs/active/2026-09-14-SPEC-001-project-framework.md`（平台继承 09-04 基线 / 立项抓手 / 兄弟项目划界 / 6 分系统研究内容 / 指标初拟 / 6 章大纲 / 10 图件 / 4 前置论证），用户同日终裁 D1~D9 全按推荐（`wiki/topics/decision-001-framework-ruling.md`）。待办：

1. PLAN-001：资料拉齐 + 论证顺序 + 章节顺序
2. AUVProposal 关键源入 `raw/` → `/ingest`（技术要求 09-04 版 / 五论证 md / 声学使用场景概述 / 整艇软件工作流程梳理）
3. 前置论证 1（组网时隙与能量）、2（中继覆盖），沿 AUVProposal 五论证体例
4. 章节 draft（6 章，复用 `build_protocol_proposal.py` + `style_base_协议.docx` + Visio OLE）

## 划界

- 不写仿真软件设计（UUVCommSwarmSim）/ 不做四化五层平台（SoSCommSupport）/ 不用「多阶 · 阶跃 · 耦合度」术语（CoupledMultiOrder）/ 不做专题课题拆分（CooperativeDetection）
- 平台事实一律取 AUVProposal 09-04 基线（六舱段 / 艏 37 元 / 每舷 32 基元 / 39.6 kWh / 单一 VPX），禁引 08-03 旧口径

## 相关

- Hub 登记：ADR-048（[[../../wiki/architecture/decision-log]]）· [[../../wiki/topics/ecosystem-dashboard]]
- auto-memory：`project_auvnetcoop_init`
