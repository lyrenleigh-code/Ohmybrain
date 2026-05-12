---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [信号处理, IEEE TSP, 估计理论, 检测理论]
---

# 信号处理基础

## 定义

信号处理基础涵盖统计信号处理、估计与检测理论、自适应滤波、谱分析等基本理论与方法。作为水声通信研究的理论支撑层，该方向提供了从信号建模到算法设计的完整方法论框架，是其他所有研究方向的共同基础。

## 核心问题

- **统计估计理论**：参数估计的最优性（CRLB）、贝叶斯估计、极大似然估计
- **检测理论**：假设检验、Neyman-Pearson 准则、GLRT
- **自适应滤波**：在非平稳环境中跟踪时变系统
- **谱估计与分析**：功率谱密度估计、时频分析
- **稀疏信号处理**：压缩感知、稀疏恢复算法
- **随机过程**：平稳/非平稳过程建模与分析

## 关键技术

- 维纳滤波、卡尔曼滤波
- LMS/RLS 自适应算法
- 压缩感知与匹配追踪
- 贝叶斯推断方法
- 矩阵分解（SVD、特征分解）
- 时频分析（STFT、小波变换）
- 蒙特卡洛方法（粒子滤波、MCMC）

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| IEEE TSP | ~150 | IEEE 信号处理汇刊论文 |
| IEEE SPL | ~80 | IEEE 信号处理快报 |
| SP Magazine | ~50 | IEEE 信号处理杂志 |
| SignalProcessing | ~48 | Elsevier Signal Processing 期刊 |

总计约 **328 篇**，占论文库的 10%。

## 相关概念

- [[channel-estimation-and-equalization]] — 信号处理理论直接支撑信道估计与均衡
- [[underwater-acoustic-communication]] — 水声通信系统的理论基础
- [[message-passing-algorithms]] — 概率推断是信号处理与消息传递的交汇点
- [[mathematical-optimization]] — 优化理论与信号处理紧密关联
- [[mimo-and-array-processing]] — 阵列信号处理是信号处理的重要分支
- [[machine-learning-methods]] — 机器学习与统计信号处理日趋融合

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[dingjie-2020-compact-usbl]] — 观测方程最小二乘、矩阵分解解耦、非线性模型线性化（USBL 校准的经典估计理论应用）
- [[hexutao-usbl-quad-array]] — EKF 相比低通和自适应残差在 SNR 16-22 dB 声波降噪的相位误差对比（实测表）
- [[guoyu-2024-lie-group-nav]] — 不变 Kalman 滤波 + Statistical Similarity Measure 将 HKF/MCKF/RSTKF 统一为鲁棒滤波数学框架；MASSMKF 多维异质噪声
- [[liufeng-2024-passive-localization]] — FIM/CRLB、EKF/UKF、粒子滤波、LM 非线性最小二乘在水声被动定位的综合应用
- [[zhengcuie-usbl-docking]] — 自适应 Notch 滤波 + LMS 相位估计 + 互谱法时延 + 相位斜率解缠绕 + CRLB 精度天花板
- [[yangbaoguo-2013-usbl-calibration]] — 非线性最小二乘、方程线性化、高斯-牛顿迭代、M 估计抗差实现
- [[quzhenzhao-2024-usbl-precision]] — 欧氏距离中心 + 阈值剔除 + LS 校正三步融合（估计理论 + 鲁棒统计的工程组合）
- [[huangjian-2019-lbl-usbl]] — GCC-NEW 加权函数、Grubbs 异常检测、UKF 非线性滤波、R-T-S 区间平滑的完整工程应用
- [[yumin-2006-lr-usbl]] — 自适应 Notch 滤波、LMS 相位估计、互相关三点插值时延（长程双模估计范式）
- [[sun-2020-dsss-passband-doppler]] — 通带相关 + 三点余弦插值的亚采样时延估计（在 Cespedes 1995 抛物线基础上升级为余弦近似以贴合通带信号结构）
- [[wei-2020-dual-hfm-speed-spectrum]] — 通过"剥离模板后的 f⁴·|X|²/S² 统计量 + 1D 频域扫描"实现连续参数估计，"频域周期 vs 时域峰位"对偶的教科书案例
- [[muzzammil-2019-cpofdm-doppler-interp]] — Dirichlet 核主瓣三点插值（抛物线 / Taylor / atan 三种路径）是通用参数估计范式
- [[lalevee-2025-dichotomous-doppler]] — 滤波器组二分搜索 + 滑窗 FIFO + 相关峰阈值准则的硬件工程样本
- [[yangyang-2026-uwa-otfs-nonuniform-doppler]] — Dirichlet 核、多项式近似、极值理论 max/mean≈4 自适应停止准则的集成应用
- [[doppler-estimation-methods]] — 水声多普勒估计方法学集合，信号处理基础工具的集成展示
