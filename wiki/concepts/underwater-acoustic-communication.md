---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [水声通信, 水下通信, 声学, 通信系统]
---

# 水声通信系统

## 定义

水声通信（Underwater Acoustic Communication, UWA Communication）是利用声波在水下环境中传输信息的通信技术。由于电磁波在水中衰减极快，声波成为水下中远距离通信的唯一实用载体。该方向是整个研究体系的核心主干，涵盖物理层到系统层的全栈技术。

## 核心问题

- **多径效应严重**：水声信道的多径时延扩展可达数十毫秒，远超无线电信道
- **时变特性剧烈**：收发平台运动、海面波动和内波导致信道快速变化
- **带宽极其有限**：可用带宽通常仅数 kHz，远低于无线电通信
- **多普勒效应显著**：声速仅约 1500 m/s，收发相对运动导致严重的多普勒频移和扩展
- **高误码率与低信噪比**：环境噪声（航运、生物、风浪）和传播损耗使信号检测困难
- **系统实时性要求**：接收机需要在有限的计算资源下完成复杂的信号处理

## 关键技术

- 水声信道建模与仿真（射线追踪、统计信道模型）
- 调制解调技术（单载波、OFDM、扩频）
- 自适应接收机设计（联合信道估计与检测）
- 编码与交织策略（Turbo 码、LDPC 码）
- 多普勒补偿与重采样
- 网络协议设计（MAC 层、路由）
- 实海试验与系统验证

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| A-UWAComms | ~500+ | 水声通信核心论文 |
| JASA | ~200+ | 美国声学学会期刊论文 |
| IEEE JOE | ~150+ | IEEE 海洋工程期刊论文 |
| Acoustic&Sonar | ~100+ | 声学与声呐相关 |
| 水声通信阅读记录 | 192 | 已精读的水声通信论文（与 A-UWAComms 交叉） |

总计约 **1120 篇**，占论文库的 35%，是最大的研究方向。

## 相关概念

- [[channel-estimation-and-equalization]] — 水声通信中信道估计与均衡是接收机的核心模块
- [[signal-processing-fundamentals]] — 信号处理为水声通信提供理论工具
- [[ofdm-and-otfs]] — OFDM 和 OTFS 是水声通信的重要调制方案
- [[time-varying-channel]] — 时变信道处理是水声通信的关键挑战
- [[mimo-and-array-processing]] — MIMO 技术用于提升水声通信速率和可靠性
- [[message-passing-algorithms]] — 消息传递算法用于水声接收机的迭代检测

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[uwacomm]] — 水声通信方向的核心实现项目，MATLAB 全栈仿真平台，覆盖 6 种通信体制的完整端到端链路
- [[uwanet-protocol-sim-note]] — UWAnet 项目前期调研笔记（协议栈 + Aqua-Sim-NG + Slotted ALOHA 案例 + 1 月学习路线）
- [[sun-2020-dsss-passband-doppler]] — DSSS 体制在长时 packet 下符号级多普勒跟踪的哈工程代表作，把"多普勒=时间伸缩"这一水声特有物理前提工程化
- [[wei-2020-dual-hfm-speed-spectrum]] — 中科院声学所 2020 IEEE SPL，双 HFM 前导 + 频域速度谱扫描的高精度多普勒估计方法
- [[muzzammil-2019-cpofdm-doppler-interp]] — UWA 低声速大多普勒场景下 CP-OFDM α 细估计的三种三点插值方法
- [[lalevee-2025-dichotomous-doppler]] — OCEANS 2025，水声调制解调器 FPGA 二叉树多普勒估计实现
- [[yangyang-2026-uwa-otfs-nonuniform-doppler]] — 宽带 UWA（fc/B ≈ O(1)）场景下的 OTFS 系统完整设计与南海 5.5 km 海试验证
- [[zhengtonghui-2025-dd-mmse-teq]] — 单载波水声通信 DD 域 Turbo 均衡的丹江口湖试 4.076 kbps/2 km/8 通道实测
- [[doppler-estimation-methods]] — 跨 6 篇论文抽取的水声多普勒估计方法学集合（2026-04-22）
