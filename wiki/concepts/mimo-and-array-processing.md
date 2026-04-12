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
