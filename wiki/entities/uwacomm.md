---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [项目, 水声通信, 仿真平台, MATLAB]
---

# UWAcomm

## 概述

UWAcomm（Underwater Acoustic Communication Algorithm Simulation Platform）是一个 MATLAB 全栈水声通信算法仿真平台。项目覆盖 6 种通信体制的完整端到端链路，包含 13 个算法模块，实现了从信源编码到阵列处理的全链路信号处理流程。

## 项目规模与技术栈

| 指标 | 数值 |
|------|------|
| 编程语言 | MATLAB（纯 MATLAB 实现，无需额外 Toolbox） |
| 函数文件 | 186 个 |
| 代码总行数 | 25,830 行 |
| 算法模块 | 13 个 |
| Git 提交数 | 203 次 |
| 通信体制 | 6 种 |
| 模块文档（含 LaTeX 推导） | ~5,000 行 |
| 源码路径 | `raw/repos/UWAcomm` |

## 13 个模块的职责和状态

### 01 信源编码（SourceCoding）
- **职责**：信源的压缩编码与解码
- **算法**：Huffman 编码 + 均匀量化
- **状态**：已完成

### 02 信道编码（ChannelCoding）
- **职责**：差错控制编码与软判决译码
- **算法**：卷积编码（R=1/2）+ SISO/BCJR/SOVA 译码器
- **状态**：已完成
- **关键接口**：`conv_encode`, `siso_decode_conv`, `sova_decode_conv`

### 03 交织（Interleaving）
- **职责**：打散突发错误，改善译码性能
- **算法**：随机交织/解交织
- **状态**：已完成
- **关键接口**：`random_interleave`, `random_deinterleave`

### 04 调制（Modulation）
- **职责**：比特到符号的映射与软判决解映射
- **算法**：BPSK/QPSK/8PSK/16QAM 星座映射 + LLR 软判决
- **状态**：已完成
- **关键接口**：`soft_demapper`, `soft_mapper`, `llr_to_symbol`, `symbol_to_llr`

### 05 扩频（SpreadSpectrum）
- **职责**：扩频码生成与解扩
- **算法**：Gold 码、Kasami 码、Walsh-Hadamard 码
- **状态**：已完成

### 06 多载波（MultiCarrier）
- **职责**：多载波调制/解调与循环前缀操作
- **算法**：OFDM（CP-OFDM/ZP-OFDM）、OTFS（ISFFT/SFFT）变换 + CP 添加/移除
- **状态**：已完成
- **关联概念**：[[ofdm-and-otfs]]

### 07 信道估计与均衡（ChannelEstEq）— 最大模块（~42 个函数）
- **职责**：信道响应获取与码间干扰消除
- **状态**：核心功能已完成，持续优化中

**静态信道估计算法**：
- LS / MMSE / OMP（压缩感知）
- SBL（稀疏贝叶斯学习）
- GAMP / AMP / VAMP（[[message-passing-algorithms|消息传递]]类）
- Turbo-VAMP / Turbo-AMP

**时变信道估计算法**：
- BEM-CE / BEM-DCT（[[time-varying-channel|基扩展模型]]）
- DD-BEM（判决辅助 BEM，BCJR 软符号扩展观测集）
- T-SBL / SAGE
- Kalman AR(1)（逐符号信道跟踪）

**OTFS 信道估计**：
- DD 域导频估计 (`ch_est_otfs_dd`)

**均衡器（时域 TDE）**：RLS / LMS / DFE / BiDFE / 线性 RLS

**均衡器（频域 FDE）**：ZF / MMSE-FDE / MMSE-IC / 时变 FDE / BEM-Turbo-FDE

**均衡器（OTFS）**：LMMSE-BCCB / MP 消息传递 / UAMP

- **关联概念**：[[channel-estimation-and-equalization]]

### 08 同步（Sync）
- **职责**：三层同步（帧/符号/位）+ 帧组装与解析
- **算法**：LFM/HFM/ZC/Barker 前导码检测、Gardner/MM TED 符号定时、PLL/DFPT/Kalman 相位跟踪
- **状态**：已完成
- **关键接口**：`sync_detect`(V2 含多普勒补偿), `timing_fine`, `cfo_estimate`, `phase_track`

### 09 波形（Waveform）
- **职责**：脉冲成形、上下变频、FSK 波形、DA/AD 转换
- **算法**：RRC 根升余弦成形/匹配滤波 + 通带/基带变频
- **状态**：已完成
- **关键接口**：`pulse_shape`, `match_filter`, `upconvert`, `downconvert`

### 10 多普勒处理（DopplerProc）
- **职责**：多普勒频移的估计与补偿
- **算法**：
  - 估计：互相关（xcorr）、模糊函数（CAF）、ZoomFFT
  - 补偿：spline 重采样、CFO 旋转、ICI 矩阵补偿
- **状态**：已完成
- **关联概念**：[[time-varying-channel]]

### 11 阵列处理（ArrayProc）
- **职责**：多阵元（ULA）接收预处理
- **算法**：ULA 阵列信道生成 (`gen_uwa_channel_array`)
- **状态**：基础框架已完成
- **关联概念**：[[mimo-and-array-processing]]

### 12 Turbo 迭代处理（IterativeProc）
- **职责**：均衡器与信道译码器之间的迭代信息交换调度
- **算法**：4 体制 Turbo 均衡调度（SC-FDE / SC-TDE / OFDM / OTFS）+ 跨块 Turbo
- **状态**：已完成
- **关联概念**：[[message-passing-algorithms]]

### 13 端到端仿真（SourceCode）
- **职责**：各体制完整链路集成测试
- **内容**：公共函数（gen_uwa_channel 多径时变信道生成）+ 各体制端到端测试脚本
- **状态**：SC-FDE/OFDM 已验证，SC-TDE 代码完成待测试

## 6 种通信体制性能对比

| 体制 | 数据速率 | 静态信道 BER | fd=1Hz BER | fd=5Hz BER | 核心技术 |
|------|---------|-------------|------------|------------|---------|
| **SC-FDE** | ~6 kbps | 0% | 0.20% | 50% | MMSE-IC 频域均衡 + 两级分离多普勒架构 |
| **OFDM** | ~6 kbps | 0% | ~1% | 50% | 逐子载波 MMSE-IC + DD-BEM 时变信道更新 |
| **SC-TDE** | ~6 kbps | 0% | 0.76%@15dB | ~45% | DFE 时域均衡 + BEM(DCT) 时变估计 + 散布导频 |
| **DSSS** | 96.8 bps | 0%@-15dB | 0%@0dB | ~36% | Rake(MRC) 接收 + DBPSK + 解扩增益 |
| **FH-MFSK** | 750 bps | 0%@10dB | 0%@5dB | 0%@0dB | 跳频分集 + 能量检测，无需信道估计 |
| **OTFS** | ~5.4 kbps | 0%@10dB | 0%@10dB | 0%* | DD 域处理 + BCCB 2D-FFT LMMSE，离散 Doppler 最优 |

**性能总结**：
- 高速率体制（SC-FDE/OFDM/SC-TDE/OTFS）在静态信道下均实现 0% BER
- 低速多普勒（fd=1Hz）下，SC-FDE 表现最优（0.20%），SC-TDE 次之（0.76%）
- 高多普勒（fd=5Hz）是所有高速率体制的性能瓶颈
- DSSS 和 FH-MFSK 牺牲速率换取多普勒鲁棒性，FH-MFSK 在全多普勒条件下均实现 0% BER
- OTFS 在离散 Doppler 信道（含分数频移）下实现 0% BER，Jakes 连续谱信道下受限于 BCCB 模型

## 关键技术特色

### 两级分离多普勒架构
- **粗估计**：双 LFM 前导码相位差 → 多普勒因子 alpha
- **精估计**：CP 相关 / 训练序列 / 空子载波 → 残余 CFO
- **补偿**：spline 重采样 + 符号率 CFO 旋转

### BEM 时变信道估计
- DCT 基扩展参数化时变信道，自动 Q 阶选择
- 散布导频是精度决定性因素（比算法选择影响大 10-20dB）
- DD-BEM 判决辅助：BCJR 软符号扩展观测集，置信度 >0.5 门控

### OTFS 延迟-多普勒域处理
- Per-sub-block CP 消除跨子块干扰
- DD 域导频嵌入 + 自适应阈值信道估计
- BCCB 矩阵 2D-FFT 对角化实现低复杂度 LMMSE 均衡

### Turbo 迭代均衡
- 均衡器与 BCJR 译码器的外信息迭代交换
- 支持 SC-FDE / SC-TDE / OFDM / OTFS 四种体制
- 跨块 Turbo 均衡进一步提升性能

## 相关链接

- **研究方向**：
  - [[underwater-acoustic-communication]] — 水声通信系统，UWAcomm 的核心研究方向
  - [[channel-estimation-and-equalization]] — 信道估计与均衡，模块 07 是项目最大模块
  - [[ofdm-and-otfs]] — OFDM 与 OTFS 调制，模块 06 实现多载波变换
  - [[message-passing-algorithms]] — 消息传递算法，AMP/VAMP/Turbo-VAMP/MP 均有实现
  - [[mimo-and-array-processing]] — MIMO 与阵列处理，模块 11 实现 ULA 接收
  - [[time-varying-channel]] — 时变信道处理，BEM/DD-BEM/Kalman 全链路实现
- **资料摘要**：[[uwacomm|source-summary]]
