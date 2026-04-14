---
type: concept
created: 2026-04-13
updated: 2026-04-13
tags: [USBL, 水声定位, DOA, 阵列处理, 校准]
---

# 超短基线定位 (USBL)

## 定义

超短基线 (Ultra-Short Baseline, USBL) 是一种水声定位技术，利用紧凑基阵（基线 < 0.5m）上多阵元间的相位差/时延差测量目标方位角 (DOA)，结合传播时延测距，确定水下目标三维位置。

## 技术链路

```
信号发射 → 信道传播 → 阵列接收 → 匹配滤波(测距) → DOA估计(测向) →
声线跟踪(声速修正) → 坐标变换(姿态+GPS) → 地理坐标输出
```

## 六层研究体系

1. **声学基阵与信号处理**：阵型设计、信号体制（窄带/宽带）、DOA 算法、抗相位模糊
2. **声速修正与声线跟踪**：有效声速估计、自适应分层声线追踪、声速剖面处理
3. **系统误差校准**：阵型误差修正、安装偏差校准（两步法）、校准航迹设计（需对称）
4. **定位解算与滤波**：单次解算、EKF/UKF 跟踪、异常值剔除
5. **多系统组合导航**：SINS/DVL/USBL 融合、LBL/USBL 异构组合
6. **硬件实现与集成**：换能器、应答器、GAPS 一体化

（来自 USBL 项目文献综述，9 篇论文提炼）

## 商用设备关键参数

| 设备 | 厂商 | 距离 | 精度 | 频段 | 基阵 |
|------|------|------|------|------|------|
| HPT 7000L | Sonardyne | 12 km | 0.12%R | 14-19 kHz | 二维多元 |
| HiPAP 102 | Kongsberg | 10 km | 0.24%R | 10-15 kHz | 三维球面 |
| Posidonia | iXblue | 10 km | 0.2%R | 14-18 kHz | 二维 |
| GAPS | iXblue | 4 km | 0.17%R | 21-30 kHz | 三维四元 |
| iTrack | 中海达 | 3 km | 0.5m+1%D | 15-25 kHz | 二维十字 |

（数据来自丁杰(2020)博士论文）

## 关键工程经验

- **基线分解算法**适用于任意几何构型的多元阵，系统误差可忽略（丁杰 2020）
- **安装校准航迹**需要足够尺度且对称，分两步：先估平均声速，再用去偏形式（杨保国 2013）
- **声线跟踪**对远距（>5km）定位至关重要，自适应分层可控制精度-计算量平衡（杨保国 2013）
- **ML 全局搜索**天然解决 d>λ/2 的相位模糊问题（USBL 项目实测）

## 相关概念

- [[mimo-and-array-processing]] — 阵列信号处理基础，DOA 估计方法
- [[signal-processing-fundamentals]] — 估计理论（CRLB、ML）、卡尔曼滤波
- [[underwater-acoustic-communication]] — 共享水声信道模型和换能器技术

## 来源

- USBL 项目（`D:\Claude\TechReq\USBL`）文献综述，9 篇论文
- 项目详细 wiki：`USBL/wiki/concepts/usbl-positioning.md`
- [[dingjie-2020-compact-usbl]] — 商用 USBL 设备参数表、基线分解声学定位、阵型误差修正、矩阵分解角度校准（丁杰博士论文 2020）的主数据源
- [[hexutao-usbl-quad-array]] — 改进非等距四元立体阵 + EKF 降噪 + 短基线参考解相位模糊，基元减半精度保持（~8‰）
- [[guoyu-2024-lie-group-nav]] — 李群误差定义下 SINS/DVL/USBL 松/紧组合导航：RIE-KF 大初始姿态误差下精度提升 ~10x，BP 网络 USBL 失效重构
- [[liufeng-2024-passive-localization]] — 水下移动节点**被动**定位（只收不发）：虚拟信标网络 + 因子图 + iUSBL 三场景统一范式（浙大 2024）
- [[zhengcuie-usbl-docking]] — USBL 用于 AUV 对接三段式（水面/导引/近程）：脉冲对双频抗模糊 + 矩形应答器阵位姿解算 + 声线跟踪校准
- [[yangbaoguo-2013-usbl-calibration]] — 观测方程三性质（唯一/无偏/方差）统领校准：两步去偏 LS + M 估计 + 声速剖面二维等效误差（哈工程 2013）
- [[quzhenzhao-2024-usbl-precision]] — 五元十字阵分解为多构型并融合（五元 + 四元 + 三元子阵），欧氏中心 + 阈值剔除 + LS 校正三步
- [[huangjian-2019-lbl-usbl]] — LBL/USBL 组合定位跟踪六项关键技术：GCC-NEW 时延估计 + BELLHOP 有效声速 + PSO 未知声速 + Grubbs 融合 + UKF-RTS 平滑（西工大 2019）
- [[yumin-2006-lr-usbl]] — 国内首代 LR-USBL（>4 km）系统研制：窄带 Notch+LMS 相位 + 宽带互相关插值双模 + 水池/海试两级校准（哈工程 863, 2006）
