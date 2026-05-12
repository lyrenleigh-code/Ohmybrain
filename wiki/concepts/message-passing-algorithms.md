---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [消息传递, 因子图, AMP, Turbo, EP, 近似推断]
---

# 消息传递与因子图

## 定义

消息传递算法（Message Passing Algorithms）是在因子图（Factor Graph）上进行概率推断的一类迭代算法。通过在图的节点之间传递"消息"（局部边缘分布或似然信息），实现全局后验分布的近似计算。该方向是水声通信接收机设计的核心方法论，将信道估计、均衡、检测、译码等模块统一在概率图模型框架下。

## 核心问题

- **近似消息传递（AMP）**：在大规模系统中实现高效的贝叶斯推断
- **期望传播（EP）**：用高斯近似处理非高斯因子节点
- **Turbo 原理**：通过迭代交换外信息（extrinsic information）逐步提升性能
- **因子图设计**：如何将通信接收机的各模块映射为因子图结构
- **收敛性分析**：迭代算法是否收敛及收敛速度
- **高斯混合模型 AMP（GMM-AMP）**：处理非高斯先验的 AMP 扩展
- **计算复杂度与近似精度的权衡**

## 关键技术

- 置信传播（BP, Belief Propagation）
- 近似消息传递（AMP, Approximate Message Passing）
- 期望传播（EP, Expectation Propagation）
- Turbo 迭代接收（Turbo Equalization/Detection）
- 变分消息传递（VMP, Variational Message Passing）
- 高斯混合 AMP（GMM-AMP）
- MIMO-AMP / IRC-MIMO-AMP
- 联合因子图设计（信道估计 + 检测 + 译码）

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| MessagePassing | ~80 | 消息传递通用理论 |
| AMP | ~40 | 近似消息传递 |
| AMP_Introduction | ~15 | AMP 入门资料 |
| Turbo | ~30 | Turbo 迭代接收 |
| FactorGraphs | ~20 | 因子图理论 |
| EP | ~15 | 期望传播 |
| GMM-AMP | ~15 | 高斯混合 AMP |
| IRC-MIMO-AMP | ~10 | MIMO 系统中的 AMP |

总计约 **225 篇**。MessagePassing 与 AMP 有 13 篇交叉，Equalization 与 Turbo 有 13 篇交叉。

## 相关概念

- [[channel-estimation-and-equalization]] — 消息传递框架下的联合信道估计与均衡
- [[underwater-acoustic-communication]] — 消息传递算法是水声接收机的核心方法
- [[signal-processing-fundamentals]] — 贝叶斯推断是两者的交汇点
- [[ofdm-and-otfs]] — OFDM/OTFS 系统中的消息传递检测
- [[mimo-and-array-processing]] — MIMO 检测中的消息传递方法（IRC-MIMO-AMP）
- [[mathematical-optimization]] — 变分推断与优化的联系

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[uwacomm]] — 模块 07/12 实现了 AMP/VAMP/Turbo-VAMP/Turbo-AMP/GAMP 信道估计和 MP 消息传递 OTFS 均衡，模块 12 实现了 Turbo 迭代均衡调度
- [[liufeng-2024-passive-localization]] — 因子图 + BP / LM 在水声定位的工程化实例：RMF+FG、OSF+FG、VNR-UAL-FG、多层级融合协同定位 FG
- [[zhengtonghui-2025-dd-mmse-teq]] — Turbo 软信息跨域交换（DD 域均衡器↔时域 RSC 译码器）的 MMSE 实例
