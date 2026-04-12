---
type: source-summary
created: 2026-04-12
updated: 2026-04-12
tags: [水声通信, 仿真平台, MATLAB, 项目]
source-type: code-repository
source-path: raw/repos/UWAcomm
---

# UWAcomm — 水声通信算法仿真平台

## 来源信息

- **类型**：代码仓库（MATLAB 全栈项目）
- **路径**：`raw/repos/UWAcomm`
- **规模**：186 个 MATLAB 函数，25,830 行代码，203 次 Git 提交
- **状态**：活跃开发中

## 核心内容

UWAcomm 是一个 MATLAB 全栈水声通信仿真系统，覆盖 6 种通信体制的完整端到端链路。项目采用模块化架构，包含 13 个算法模块，从信源编码到阵列处理全链路覆盖。

### 6 种通信体制

| 体制 | 速率 | 静态信道 BER | fd=1Hz BER | fd=5Hz BER | 特点 |
|------|------|-------------|------------|------------|------|
| SC-FDE | ~6 kbps | 0% | 0.20% | 50% | 频域均衡，两级分离架构 |
| OFDM | ~6 kbps | 0% | ~1% | 50% | 逐子载波 MMSE-IC + DD-BEM |
| SC-TDE | ~6 kbps | 0% | 0.76%@15dB | ~45% | 时域 DFE + BEM 时变估计 |
| DSSS | 96.8 bps | 0%@-15dB | 0%@0dB | ~36% | Rake(MRC) + DBPSK + DCD |
| FH-MFSK | 750 bps | 0%@10dB | 0%@5dB | 0%@0dB | 跳频分集，无需信道估计 |
| OTFS | ~5.4 kbps | 0%@10dB | 0%@10dB | 0%* | DD 域处理，离散 Doppler 最优 |

### 13 个算法模块

| 模块 | 名称 | 函数数（估） | 职责 |
|------|------|------------|------|
| 01 | 信源编码 | ~5 | Huffman + 均匀量化 |
| 02 | 信道编码 | ~8 | 卷积编码 + SISO/BCJR/SOVA 译码 |
| 03 | 交织 | ~3 | 随机交织/解交织 |
| 04 | 调制 | ~5 | BPSK/QPSK/8PSK/16QAM 映射与软判决 |
| 05 | 扩频 | ~6 | Gold/Kasami/Walsh-Hadamard 扩频码 |
| 06 | 多载波 | ~8 | OFDM/OTFS 变换 + CP 操作 |
| 07 | 信道估计与均衡 | **~42** | 最大模块：15+ 种估计算法、10+ 种均衡器 |
| 08 | 同步 | ~12 | 三层同步（帧/符号/位）+ 帧组装 |
| 09 | 波形 | ~10 | RRC 脉冲成形 + 上下变频 + FSK + DA/AD |
| 10 | 多普勒处理 | ~10 | 估计（xcorr/CAF/ZoomFFT）+ 补偿（spline/CFO/ICI） |
| 11 | 阵列处理 | ~5 | ULA 阵列接收预处理 |
| 12 | Turbo 迭代 | ~6 | 4 体制 Turbo 均衡调度 |
| 13 | 端到端仿真 | ~15 | 集成测试 + 公共函数（gen_uwa_channel 等） |

### 关键技术

1. **两级分离多普勒架构**：粗估计（双 LFM 相位差）+ 精估计（CP/训练/空子载波）+ spline 重采样补偿
2. **BEM 时变信道估计**：DCT 基扩展模型，散布导频是精度决定性因素（比算法选择影响大 10-20dB）
3. **DD-BEM 判决辅助**：BCJR 软符号扩展观测集，置信度门控迭代精化
4. **OTFS DD 域处理**：Per-sub-block CP + DD 域导频嵌入 + BCCB 2D-FFT 对角化 LMMSE
5. **Turbo 迭代均衡**：均衡器与 BCJR 译码器的外信息迭代交换，支持 4 种体制

### 端到端信号流

```
TX: 信源 → 卷积编码(R=1/2) → 随机交织 → QPSK 映射
    → [体制相关调制] → RRC 脉冲成形 → 帧组装(LFM+保护间隔+数据) → 上变频
信道: 多径时变信道(gen_uwa_channel) + 通带实噪声
RX: 下变频 → 匹配滤波 → LFM 同步检测 → 两级多普勒估计+补偿
    → 信道估计(BEM/OMP/GAMP) → Turbo 均衡(均衡器⇌BCJR) → 解交织 → 译码
```

## 提取的实体和概念

- **实体**：[[uwacomm]]（项目实体页）
- **相关概念**：
  - [[underwater-acoustic-communication]] — UWAcomm 是水声通信方向的核心实现项目
  - [[channel-estimation-and-equalization]] — 模块 07 实现了 15+ 种估计算法和 10+ 种均衡器
  - [[ofdm-and-otfs]] — 模块 06 实现了 OFDM/OTFS/SC-FDE 多载波变换
  - [[message-passing-algorithms]] — 模块 07/12 实现了 AMP/VAMP/Turbo-VAMP/MP 等消息传递算法
  - [[mimo-and-array-processing]] — 模块 11 实现了 ULA 阵列接收处理
  - [[time-varying-channel]] — 模块 07/10 实现了 BEM/DD-BEM/Kalman 时变估计和多普勒补偿
