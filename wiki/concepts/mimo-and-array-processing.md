---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [MIMO, 阵列处理, 波束成形, 空间分集]
---

# MIMO 与阵列处理

## 定义

MIMO（多输入多输出）与阵列处理方向研究利用多个发射/接收换能器（阵元）进行空间域信号处理的技术。在水声通信中，MIMO 技术可以通过空间复用提高传输速率，或通过空间分集提高通信可靠性。阵列处理则涵盖波束成形、空间滤波和方位估计等经典问题。

## 核心问题

- **水声 MIMO 信道建模**：空间相关性、阵列几何影响
- **MIMO 检测**：在高维信号空间中的最优和次优检测
- **波束成形**：利用阵列增益抑制干扰、提升信噪比
- **空时编码**：联合空间和时间域的编码设计
- **大规模 MIMO 在水声中的可行性**：受限于换能器尺寸和间距
- **阵列校准**：水下阵列的位置不确定性和相位误差

## 关键技术

- 空间复用（V-BLAST、D-BLAST）
- 空时编码（STBC、STFC）
- 自适应波束成形（MVDR、LCMV）
- MIMO 检测（ML、MMSE、球形译码）
- MIMO-OFDM 和 MIMO-OTFS
- 消息传递 MIMO 检测（AMP、EP）
- DOA 估计（MUSIC、ESPRIT）

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| Array&MIMO | ~21 | 阵列信号处理与 MIMO |

总计约 **21 篇**。此外，IRC-MIMO-AMP 文件夹中的部分论文也与此方向密切相关。

## 相关概念

- [[underwater-acoustic-communication]] — MIMO 技术用于提升水声通信性能
- [[message-passing-algorithms]] — MIMO 检测中的消息传递方法（IRC-MIMO-AMP）
- [[ofdm-and-otfs]] — MIMO-OFDM 和 MIMO-OTFS 系统
- [[signal-processing-fundamentals]] — 阵列信号处理是信号处理的核心分支
- [[channel-estimation-and-equalization]] — MIMO 信道估计面临维度灾难
- [[mobile-communication]] — 大规模 MIMO 在移动通信中已成熟

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[uwacomm]] — 模块 11 实现了 ULA 阵列接收预处理和多阵元信道生成（gen_uwa_channel_array）
- [[usbl-positioning]] — USBL 水声定位中的 DOA 估计、波束成形、阵列校准（来自 USBL 项目）
- [[dingjie-2020-compact-usbl]] — 紧凑型声纳阵列的阵型误差修正（有效声速 + 基线长度重构）与复杂阵型 DOA 估计（基线分解法），可迁移至成像声纳、合成孔径声纳
- [[hexutao-usbl-quad-array]] — 长短基线混合拓扑（L=8l 非等距四元）宽频解模糊阵型设计范式
- [[guoyu-2024-lie-group-nav]] — USBL 紧组合以斜距+方位角为量测向量；松/紧组合在噪声协方差正确设置下等价（理论证明+仿真）
- [[liufeng-2024-passive-localization]] — iUSBL（逆 USBL）阵列在 AUV 集群中的 DOA 观测接入协同定位因子图
- [[zhengcuie-usbl-docking]] — 4 元正交平面阵 + 相位差/时延差定位；大孔径抗模糊从阵型冗余转移到频率维度（脉冲对双频）
- [[yangbaoguo-2013-usbl-calibration]] — 四元平面阵 DOA 估计稳健校准；M 估计权值工程化
- [[quzhenzhao-2024-usbl-precision]] — 五元十字阵分解为多基本构型的硬件冗余利用范式，工程化多源观测融合
- [[huangjian-2019-lbl-usbl]] — Hough 变换定位将多种阵列测量（时延/方位）在同一参数空间累加的"参数空间融合"范式
- [[yumin-2006-lr-usbl]] — 8 元 UCA 阵元附加相移标定；DOA 双模（相位差/时延差）
- [[lalevee-2025-dichotomous-doppler]] — 正交信号多信标并行相关是该方法的典型扩展应用（10-30 信标并行跟踪）
