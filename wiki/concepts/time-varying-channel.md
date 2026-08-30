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

## 实战结论（memory 蒸馏 @2026-08-18，源=UWAcomm 2026-04~05 session 簇）

- **连续谱 Jakes 是体制无关的灾难分界**：离散多普勒/hybrid-K 场景 6 体制 BER 全 0%，同参数连续谱 Jakes 下 SC-FDE fd=1Hz 47%、OTFS fd=5Hz 33-44%、SC-TDE fd=1Hz 非单调——解法都在**协议层**（pilot/training 结构），不是估计器调参。— UWAcomm 04-26/04-27
- **软符号-BEM 判决反馈存在鸡蛋耦合**：静态 PASS 掩盖不了时变下「软符号错→BEM 错→更错」正反馈（fd=1Hz 50% 灾难）；破局=**独立干净观测**（pilot 段 pre-Turbo BEM），且存在硬阈值 pilot≥CP 长度（吞吐 -50% 是物理代价，由 max_tau/blk_fft 比决定）。— UWAcomm 04-24/04-26
- **迭代精化的前提是误差随迭代衰减**：fd=1Hz Jakes 下估计器 deterministic bias 不衰减，iter refinement 把 bias 逐轮翻倍（反向收敛）——deterministic bias 场景应 iter=0 + 一次性 calibration。— UWAcomm 04-25
- **HFM 并非 Doppler-invariant，但其 deterministic 残差可当信道指纹用**（dtau_diff 唯一值触发 fd-specific calibration）。— UWAcomm 04-25 V5.6
- **DSSS 时变路径必须 DBPSK + DCD 差分检测，相干 Rake 必败**：残余 CFO 1.08Hz@fd=1Hz 在 5s 帧上累积 35+ rad，训练段 h_est 到数据段失效（Rake-MRC BER~47%）；符号率 ~194 sym/s 相位跟踪不可行。TX 参考符号 + XOR 预编码（多 1 符号），RX Rake 解扩后相邻符号相位差判决，软 LLR = −real(diff_corr)/nv_diff 送 Viterbi；代价 ~3dB 由 14.9dB 扩频增益承担，fd=1Hz coded 0%@0dB+。— UWAcomm 2026-04-11 旧 memory `feedback_dsss_dcd`（08-29 误回流副本，撤回前蒸馏 @2026-08-30）
- **2026-04-11 六体制 Jakes 基线矩阵（static / fd=1Hz / fd=5Hz）**：SC-FDE V4.0 0% / 0.20%@5dB / 50%；OFDM V4.3 0%@5dB+ / ~1%@15dB+ / 50%；SC-TDE V5.1 0%@10dB+ / 0.76%@15dB / ~45%；DSSS V1.0 0%@−15dB+ / 0%@0dB+ / ~36%；FH-MFSK V1.0 0%@10dB+ / 0%@5dB+ / **0%@0dB+**（唯一 Jakes fd=5Hz 全通，非相干代价 750bps）；OTFS V2.0 ~5.4kbps 0%@10dB+ ×3（fd=5Hz 仅离散 Doppler / Rician K≥5，Jakes ~50%）。SC-FDE V4.0 两级分离帧 `[HFM+|HFM-|LFM1|LFM2|data]` oracle fd=5Hz 0.24%@5dB 证链路本身正确，瓶颈全在盲 α 估计。— UWAcomm 2026-04-11 旧 memory `project_v4v5_conversion / project_sync_refactor`（08-29 误回流副本，撤回前蒸馏 @2026-08-30）

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
