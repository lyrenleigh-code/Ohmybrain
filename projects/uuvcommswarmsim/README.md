# UUVCommSwarmSim 🔒

> UUV 通信组网与集群控制一体化仿真软件项目文档工作区（主交付物形态 / 受众 / 口径待讨论，先搭架子）

- **仓库**：`D:\Claude\DocProcess\UUVCommSwarmSim`
- **类型**：document（`template-document` 派生，2026-09-13，ADR-046）
- **状态**：🟢 第 4 章成稿终审中（2026-09-14 丰富化版待第七轮终审）
- **依赖**：无（通信体制仿真可查 [[../uwacomm/README|UWAcomm]]、组网协议仿真可查 [[../uwanet/README|UWAnet]]、集群协控口径可查 [[../coupledmultiorder/README|CoupledMultiOrder]]，查询不构成依赖）
- **git**：本地 `main` `84fe9c9`（2026-09-13 第 4 章成稿 + 五轮回改；09-14 丰富化版未 commit），无远程（🔒 私人，禁 push 公开仓）

## 当前焦点

2026-09-13 派生当日：参考件第 4 章摄入（仅参考、要重设计）→ 用户组成草案（三层 8 模块）→ SPEC-001 总体框架（A1~A7 用户确认）→ 第 4 章「总体技术设计方案」成稿 + 五轮终审回改（Visio OLE 可编辑图 / 小四 22 磅 / 正式化 / 图件消交叉 / 图 4 泳道 / 表格零缩进），commit `84fe9c9`。

2026-09-14：用户「参考 SoSCommSupport 总体框架设计写丰富些」→ 逐节对照后扩为 9 图 16 表 32 页约 2.34 万字（三级组成 F1~F34 / 算法与协议库表 / 技术·部署·数据架构 / 流程步骤表·各层子流程·控制步时序图·6 工况实例化 / 接口分类与约定），新假设 B1~B5（C++ 混合调度内核 + 插件库 / Linux 目标环境 / 联合运行主时钟 / HDF5 记录）待裁。待办：

1. 用户第七轮终审 → 03-validate 回改 → 04-archive
2. 《技术要求》件入 `raw/` → 表 3 指标与协议 / 算法数量对齐、技术选型与运行环境核定
3. 第 5 章模块详细设计 SPEC-002
## 相关

- Hub 登记：ADR-046（[[../../wiki/architecture/decision-log]]）· [[../../wiki/topics/ecosystem-dashboard]]
- auto-memory：`project_uuvcommswarmsim_init`
