# AUVNetModem 🔒

> 面向五U 组网条件的水声通信机详细设计——为 AUVNetCoop 建设方案 v1.8 的两段水声链路（下层 3–9 kHz / 5–10 km / ≥300 bit/s；上层 15–25 kHz / ≤1 km / ≥1 kbit/s；单次误包率 ≤10%，均为上游目标值）设计通信机：A 算法（体制 / 帧结构 / 链路预算 / MATLAB 链路级仿真 / 物理层模型参数）+ B 硬件（换能器 / 功放 / 接收前端 / 数字平台 / 结构供电）。

- **仓库**：`D:\Claude\TechReq\AUVNetModem`
- **类型**：engineering-hardware 子型（`template-engineering` + 硬件目录扩展，2026-09-18 派生，ADR-050；USBL_hw 之后第二例）
- **状态**：🟡 框架待裁（SPEC-001 v0，D1~D10）
- **依赖**：[[../auvnetcoop/README|AUVNetCoop]]（需求源：五U 两段链路目标 + TDMA / ALOHA / FDMA 对物理层的约束 + 物理层模型接口）；[[../uwacomm/README|UWAcomm]]（算法底座，公开仓，本项目资料不回流）；[[../auvproposal/README|AUVProposal]]（平台基线《技术要求》09-04 版 + 通信指标论证）。查询复用不构成依赖：[[../usbl_hw/README|USBL_hw]]（收发链 / 数字平台 / 耐压壳设计先例）/ [[../uwacomm_usbl/README|UWAcomm_usbl]] / [[../uwanet/README|UWAnet]]（物理层抽象接口做法）/ [[../uwacommtrial/README|UWAcommTrial]]
- **git**：本地 `main` `c37e2ce`，无远程（🔒 私人，禁 push 公开仓）

## 当前焦点

派生当日（2026-09-18）：用户问「组网条件下的水声通信机详细设计是单独做项目还是怎么弄」→ 建议单列 → 用户裁「A 和 B 都要包含，放 TechReq 下」。两路只读采集沉淀为项目 wiki 2 页（上游输入事实 / 既有资产盘点），SPEC-001 项目框架 v0 成文。待办：

1. 用户裁 D1~D10（硬件对象范围 / 下层发射带宽口径 / 探测型 AUV 接收形态 / 首轮体制候选池 / UWAcomm 复用方式 / 信道输入 / A·B 顺序 / 写入权 / 对 AUVNetCoop 回写）
2. 裁决后 PLAN-001：资料拉齐（上游关键源入 `raw/`）+ WP 顺序
3. M1 需求基线 + 与 AUVNetCoop 的接口约定 → M2 五U 几何链路预算与信道论证 → M3 体制选型与帧结构（带宽与功率口径冻结点）→ M4 链路级仿真与物理层模型参数包 → M5 硬件 first-pass → M6 方案设计说明书

## 划界

- 五U 场景、MAC、组网协议、网络级数字仿真、建设方案文本归 AUVNetCoop；通用多体制算法库归 UWAcomm；单艇平台总体归 AUVProposal；USBL 定位前端硬件归 USBL_hw
- 与 AUVNetCoop 的接口为双向、只交换文档：上游给需求与约束，本项目回物理层模型参数包；AUVNetCoop 本期验收不含通信机硬件研制，本项目硬件线为独立工作线
- 平台事实一律取 AUVProposal 09-04 基线；需求事实一律取 AUVNetCoop v1.8 / SPEC-012，其旧 SPEC-L1 / L2 算例不作五U 结论

## 相关

- Hub 登记：ADR-050（[[../../wiki/architecture/decision-log]]）· [[../../wiki/topics/ecosystem-dashboard]]
- auto-memory：`project_auvnetmodem_init`
