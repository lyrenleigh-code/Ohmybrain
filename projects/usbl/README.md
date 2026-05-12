# USBL

> 超短基线水下自定位系统 — 算法 + 硬件 + 标定 三线并行，MATLAB 原型 → C/C++ 产品化

- **仓库**：github.com/lyrenleigh-code/USBL（GitLab 内网镜像 http://192.168.10.100:8880/lilin/USBL）
- **本地**：`D:\Claude\TechReq\USBL`
- **状态**：活跃开发中（截至 2026-04-26，HEAD `b8a8cc4`）

## 系统关键参数

| 参数 | 值 | 备注 |
|------|---|------|
| 中心频率 | **12 kHz** | 2026-04-19 由 10 kHz 更新（依据 NEUB-816 9 项测试） |
| 波长 λ | 12.5 cm | c = 1500 m/s |
| 阵列形态 | **CAGE5 笼式五元立体阵** | 4 立柱 + 1 中央 + 双盘支撑（旧 5 元 UCA d=20cm 概念已废） |
| 信号体制 | LFM | BW=4 kHz, τ=100 ms |
| 最大作用距离 | ≥ 10 km | |
| 定位精度 | 优于斜距 1% | |
| 接收灵敏度（实测） | -200 dB re 1V/μPa | 8-16 kHz 平坦，变化 <1 dB |
| 通道一致性（12 kHz） | 幅度 ±0.5 dB / 相位 ±3.6° | M2 走软件校正 |
| 应答器源级 | 185 dB | 应答器模式，链路预算用单程 TL |

## 模块划分（19 模块 4 线，方案 B）

走 spec → plan → implement → validate 闭环，每模块一张 spec 卡（`specs/active/<MOD>.md`）。

| 线别 | 数量 | 编号 | 范围 |
|------|------|------|------|
| **A 算法线** | 7 | A1-A7 | 信号链 / DOA / 声速 / 坐标 / 融合 / 导航 / 目标定位 |
| **H 硬件线** | 7 | H1-H6 + H8 | 换能器 / 阵列 / 应答器 / 采集 / 结构 / 联调 / **ICD（H8 起草中）** |
| **M 测量校准线** | 5 | M1-M5 | 阵型几何 / 电声一致性 / 安装 / 在线重构 / 年度 SOP |
| **S 系统线** | 2 | S1-S2 | 仿真平台 / 试验平台 |

### 算法线当前状态（2026-04-26）

| 编号 | 模块 | 状态 |
|------|------|------|
| A1 | 信号与测距链路 | 🟡 in-progress (M1) |
| A2 | DOA 估计套件 | 🟡 in-progress (M1/M2) |
| A3 | 声速与声线跟踪 | 🟢 完成（重构 + 8 case 测试通过） |
| A4 | 坐标变换与 iUSBL 解算 | 🟢 完成（逆变换 + Jacobian） |
| A5 | 多潜标融合与 GDOP | 🟢 完成（核心融合 + 野值剔除 + Huber） |
| A6 | 组合导航 IEKF/EKF/UKF（紧耦合，INS+DVL）| 🟡 in-progress (M4-M6) |
| A7 | 目标定位（主动应答） | 🟡 in-progress (M2/M4/M5) |

### 起草进行中

- **H8 ICD spec drafting**（2026-04-25 起）：spec draft 落地，等用户答 D1-D4；H7 未起

## 技术决策

| 决策 | 选择 | 理由 |
|------|------|------|
| DOA 主力算法 | **ML 两级搜索** | 单快拍最优，全局搜索天然解模糊 |
| DOA 辅助算法 | 相位比较法 | 交叉验证 + 残差质量指标 |
| DOA 解模糊 | CBF | 粗估计基底 |
| 链路预算 | 单程 TL | 应答器模式 SL=185dB |
| 阵列形态 | **CAGE5 笼式立体阵** | 工程图 + 垂直指向性双重佐证（2026-04-19） |
| 平面阵 DOA | xy 分量 LS，u_z 由单位球约束恢复 | 维持几何约束 |

## 项目内导航

- **wiki**：`wiki/index.md`（15+ 页）
- **仪表盘**：`wiki/dashboard.md`
- **MOC**：`wiki/usbl-moc.md`
- **模块索引**：`TODO.md`（19 模块状态速查）
- **文献综述**：`wiki/topics/usbl-literature-review.md`（9 篇论文摘要）
- **研制计划**：`wiki/topics/lr-usbl-development-plan.md`（五阶段+硬件并行+11 重难点）
- **硬件 spec**：`wiki/topics/usbl-hardware-spec.md`（HW-1~HW-6）

## Hub wiki 关联

- [usbl-positioning](../../wiki/concepts/usbl-positioning.md) — USBL 定位概念（从本项目 promote）
- [mimo-and-array-processing](../../wiki/concepts/mimo-and-array-processing.md)
- [signal-processing-fundamentals](../../wiki/concepts/signal-processing-fundamentals.md)
