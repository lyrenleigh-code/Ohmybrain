---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [信道估计, 均衡, 多普勒, 叠加导频, 接收机]
---

# 信道估计与均衡

## 定义

信道估计与均衡是通信接收机中消除信道影响、恢复发送信号的两个核心环节。信道估计获取信道的冲激响应或频率响应，均衡器利用信道估计结果补偿码间干扰（ISI）。在水声通信中，由于信道的长时延扩展和快速时变性，这两个问题尤其具有挑战性。

## 核心问题

- **稀疏信道估计**：水声信道通常具有稀疏结构，如何利用稀疏性提升估计精度
- **时变信道跟踪**：信道在一个数据包内持续变化，需要实时跟踪
- **导频设计与开销**：导频占用有限带宽资源，叠加导频（Superimposed Pilot）可减少开销
- **多普勒估计与补偿**：需要联合估计时延-多普勒扩展
- **判决反馈均衡（DFE）**：利用已判决符号辅助均衡，但存在错误传播问题
- **Turbo 均衡**：将均衡器与信道译码器迭代交互，逼近信道容量
- **计算复杂度**：实时处理要求高效算法设计

## 关键技术

- 最小均方误差（MMSE）均衡
- 判决反馈均衡（DFE）
- Turbo 均衡（均衡-译码联合迭代）
- 压缩感知（CS）稀疏信道估计
- 基扩展模型（BEM）时变信道建模
- 叠加导频（Superimposed Pilot）方案
- 自适应算法（LMS、RLS）
- 因子图上的消息传递均衡

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| ChannelEstimation | ~150 | 信道估计核心论文 |
| Equalization | ~100 | 均衡技术论文 |
| doppler | ~40 | 多普勒效应处理 |
| Superimposed Pilot | ~45 | 叠加导频相关 |

总计约 **335 篇**，与 Turbo 文件夹有 13 篇交叉（Turbo 均衡方向）。

## 相关概念

- [[underwater-acoustic-communication]] — 信道估计与均衡服务于水声通信系统
- [[message-passing-algorithms]] — 消息传递框架下的信道估计与均衡
- [[signal-processing-fundamentals]] — 估计理论和自适应滤波是基础工具
- [[time-varying-channel]] — 时变信道是信道估计的核心难点
- [[ofdm-and-otfs]] — OFDM 系统中的信道估计有特殊结构
- [[mathematical-optimization]] — 优化方法用于导频设计和估计器设计

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[uwacomm]] — 模块 07 实现了 15+ 种估计算法（LS/MMSE/OMP/SBL/GAMP/AMP/VAMP/Turbo-VAMP/BEM/DD-BEM/Kalman 等）和 10+ 种均衡器（TDE/FDE/OTFS 三类）
