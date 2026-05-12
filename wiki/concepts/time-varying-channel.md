---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [时变信道, 双色散, 信道跟踪, 水声信道]
---

# 时变信道处理

## 定义

时变信道处理方向专门研究快速变化的通信信道的建模、估计和补偿方法。水声信道是典型的双色散（doubly-dispersive）信道——同时存在时延扩展和多普勒扩展。该方向聚焦于信道时变性带来的特殊挑战，是水声通信区别于常规无线通信的关键技术难点。

## 核心问题

- **双色散信道建模**：联合时延-多普勒扩展的数学描述
- **基扩展模型（BEM）**：用有限基函数参数化时变信道
- **块内信道变化**：一个数据包内信道持续演变的处理策略
- **非平稳信道**：统计特性随时间变化的信道
- **时变系统辨识**：在线跟踪时变系统参数
- **时变信道下的接收机设计**：联合多普勒补偿与检测

## 关键技术

- 基扩展模型（BEM）：多项式、傅里叶、离散椭球序列
- 卡尔曼滤波信道跟踪
- 时频分析方法
- 自适应滤波（变步长 LMS/RLS）
- 时变 OFDM 接收（ICI 均衡）
- 多普勒分集利用
- 分段准静态近似

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| TimeVaryingSPorComm | ~15 | 时变信号处理与通信 |
| TV—UWA | ~7 | 时变水声信道 |

总计约 **22 篇**。论文数虽少，但该方向的核心问题渗透在信道估计、均衡和 OFDM 等多个方向中。

## 相关概念

- [[underwater-acoustic-communication]] — 时变性是水声信道的核心特征
- [[channel-estimation-and-equalization]] — 时变信道估计与跟踪
- [[ofdm-and-otfs]] — OTFS 调制天然匹配双色散信道，OFDM 受时变性影响严重
- [[signal-processing-fundamentals]] — 自适应滤波和时频分析是关键工具
- [[mobile-communication]] — 移动通信中也存在时变信道，但程度远轻于水声

## 实验结论（fd=10Hz ICI 极限量化）

> 2026-04-12 更新：模块 07 doppler_rate 修正后首次量化 fd=10Hz 下的系统 ICI 极限。

fd=10Hz (doppler_rate=8.33e-4) + oracle alpha 补偿后：
- **oracle BER 在高 SNR 非单调反弹**：10dB=0.73% → 15dB=3.28% → 20dB=3.65%
- 说明即使信道完美已知，ICI 残余也无法被均衡器消除
- BEM(DCT) 在 5dB 达到最优点（1.15%），之后随 SNR 升高反而恶化
- **结论：fd=10Hz 是当前系统架构（BEM+LMMSE-IC）的硬天花板，改善需要更根本的方法（如 OTFS DD 域处理）**

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[uwacomm]] — 模块 07 实现了 BEM(CE/DCT)/DD-BEM/T-SBL/SAGE/Kalman 时变信道估计，模块 10 实现了两级分离多普勒估计与 spline/CFO/ICI 补偿
- [[uwacomm]] — fd=10Hz ICI 极限量化数据 (2026-04-12)
- [[huangjian-2019-lbl-usbl]] — 移动 USBL 定位中航迹畸变、信道时变、测量野值是同一工程现实的多层表现
- [[sun-2020-dsss-passband-doppler]] — 把 α=v/c 作为符号级时变参数跟踪的典型实现，与块估计假设相对
- [[wei-2020-dual-hfm-speed-spectrum]] — 水声时变信道下多普勒 α 估计的频域方案，突破采样率对速度分辨率的限制
- [[muzzammil-2019-cpofdm-doppler-interp]] — CP-OFDM 下共享 α 多径信道的 α 估计与补偿
- [[lalevee-2025-dichotomous-doppler]] — 针对多普勒频移时变的实时估计与补偿方法
- [[yangyang-2026-uwa-otfs-nonuniform-doppler]] — "重采样消除主多普勒 + 建模残留 Doppler 因子 b_p"的分层时变信道处理范式
- [[zhengtonghui-2025-dd-mmse-teq]] — 双色散信道在 DD 域的稀疏化表示是性能增益的物理基础
- [[doppler-estimation-methods]] — 水声多普勒估计方法学集合 concept（2026-04-22）
