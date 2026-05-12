---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [数学, 优化, 工具, MATLAB]
---

# 数学与优化

## 定义

数学与优化方向包括通信与信号处理中用到的数学工具、优化理论和数值计算方法。涵盖矩阵论、概率论、凸优化、数值分析以及 MATLAB 仿真工具。该方向是整个研究体系的**基础工具层**，为算法设计和性能分析提供数学支撑。

## 核心问题

- **凸优化与非凸优化**：通信系统中的资源分配和波形设计问题
- **矩阵理论**：随机矩阵、矩阵分解在 MIMO 和信号处理中的应用
- **概率与统计推断**：贝叶斯框架下的估计和检测
- **数值方法**：高效算法实现（FFT、矩阵求逆近似）
- **性能界分析**：信息论界、Cramer-Rao 下界
- **仿真平台搭建**：MATLAB 仿真环境和工具箱

## 关键技术

- 凸优化（SDP、SOCP、线性规划）
- 交替优化（ADMM、块坐标下降）
- 随机优化与随机梯度方法
- 矩阵补全与低秩恢复
- 信息论分析（互信息、信道容量）
- MATLAB 数值仿真
- 蒙特卡洛仿真方法

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| Mathematics | ~15 | 数学理论 |
| Basic&Tool | ~10 | 基础工具和方法 |
| MATLAB | ~5 | MATLAB 相关资源 |

总计约 **30 篇**。虽然论文数较少，但作为基础工具层渗透到所有其他方向。

## 相关概念

- [[signal-processing-fundamentals]] — 信号处理与数学优化紧密交织
- [[channel-estimation-and-equalization]] — 优化方法用于估计器和均衡器设计
- [[message-passing-algorithms]] — 变分推断与优化的深层联系
- [[mimo-and-array-processing]] — 波束成形等问题本质是优化问题
- [[machine-learning-methods]] — 机器学习训练过程就是优化过程

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[guoyu-2024-lie-group-nav]] — SE₂(3) 李群上 SINS 误差建模；左/右不变误差下李代数对数映射；Davenport q 方法大角度安装偏差标定
- [[zhengcuie-usbl-docking]] — 直接求解旋转矩阵（9 参数）避免欧拉角线性化；声线跟踪下以入射角向量为等量的最小二乘建模链条
- [[yangbaoguo-2013-usbl-calibration]] — 改进高斯-牛顿（初值保护）+ 自适应辛普森逆向分层
- [[huangjian-2019-lbl-usbl]] — 改进 PSO（区域划分 + 自适应权重 + 自适应变异）联合估计有效声速 + 目标位置；BELLHOP 迭代有效声速作为不动点迭代
- [[yumin-2006-lr-usbl]] — 非线性 LS / 逐次 LS / M 估计抗差的递进求解链
- [[sun-2020-dsss-passband-doppler]] — 三点余弦模型的 LS 拟合、`|fc·Δτ| < π/2` 相位不模糊约束下的分辨率-范围权衡
- [[yangyang-2026-uwa-otfs-nonuniform-doppler]] — 块稀疏 CS + MLE 分层优化：粗网格 + 二次拟合 + 精细搜索的低复杂度连续参数估计
- [[zhengtonghui-2025-dd-mmse-teq]] — Woodbury 恒等 + 拉格朗日乘子 + MMSE 准则在 DD 域均衡中的联合使用
- [[doppler-estimation-methods]] — MLE/LS/稀疏恢复/二次拟合在多普勒估计中的实例
