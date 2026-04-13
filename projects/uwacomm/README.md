# UWAcomm

> 水声通信算法仿真平台 — MATLAB 全栈，6 种通信体制，13 模块

- **仓库**：github.com/lyrenleigh-code/UWAcomm
- **本地**：`D:\Claude\TechReq\UWAcomm`
- **状态**：活跃开发中
- **规模**：186 个 MATLAB 文件，25830 行代码，13 个模块

## 体制进度

| 体制 | 状态 | 性能 |
|------|------|------|
| **SC-TDE** | V5.1 | static 0%@10dB+, fd=1Hz 0.76%@15dB |
| **SC-FDE** | V4.0 | static 0%, fd=1Hz 盲 0.20% |
| **OFDM** | V4.3 固化 | fd=1Hz ~1%@15dB+, 鲁棒架构 |
| **OTFS** | V2.0 | 离散 Doppler: 0%@10dB+, LMMSE-BCCB |
| **DSSS** | V1.0 | static 0%@-15dB+, 96.8bps |
| **FH-MFSK** | V1.0 | fd=5Hz 0%@0dB+, 全信道可工作 |

## 模块架构

```
TX: 02编码 → 03交织 → 04调制 → [05扩频|06多载波] → 09成形 → 08帧组装
CH: 13信道仿真 → 09上变频 → +噪声
RX: 09下变频 → 10多普勒补偿 → 08同步 → 07信道估计均衡 → 12Turbo迭代 → 03解交织 → 02译码
```

| 模块 | 核心能力 | 函数数 |
|------|---------|--------|
| 01 信源编解码 | Huffman + 量化 | 4 |
| 02 信道编解码 | 卷积/LDPC/Turbo + SISO(BCJR) | 10 |
| 03 交织 | 随机/块/卷积交织 | 6 |
| 04 调制 | QAM/MFSK 映射 | 4 |
| 05 扩频 | DSSS/FH/CSK + Gold/Kasami/Walsh | 17 |
| 06 多载波 | OFDM/OTFS/SC-FDE + CP | 15 |
| 07 信道估计均衡 | LS/MMSE/OMP/SBL/GAMP/BEM + TDE/FDE/OTFS 均衡 | 37 |
| 08 同步 | LFM/HFM/ZC + 帧同步/CFO/相位跟踪 | 20 |
| 09 波形 | RRC 成形 + 上下变频 + FSK + DA/AD | 8 |
| 10 多普勒 | xcorr/CAF/ZoomFFT 估计 + spline/CFO/ICI 补偿 | 12 |
| 11 阵列 | DAS/MVDR 波束形成 + ULA 信道 | 6 |
| 12 Turbo 迭代 | 4 体制 Turbo 均衡调度 + 跨块 | 5 |
| 13 端到端 | 信道仿真 + TX/RX chain + 各体制测试 | 7 |

## 关键技术结论

1. 散布导频是精度决定性因素（比算法选择影响大 10-20dB）
2. BEM(DCT)+散布导频最优
3. FDE 在长时延信道下全面优于 TDE（5dB 编码增益）
4. 两级分离架构有效（多普勒估计与定时解耦）
5. Jakes 连续谱确认为伪瓶颈，离散 Doppler 下 6 体制全可工作
6. FH-MFSK 唯一全信道可工作体制

## 待办

| 项 | 优先级 |
|----|--------|
| 离散 Doppler 全体制 BER 矩阵 | 高 |
| OTFS 通带 2D 脉冲整形 | 高 |
| OTFS 两级同步架构 | 高 |
| SC-TDE fd=1Hz 优化 | 中 |

## 项目内导航

- **wiki**: `wiki/index.md` — 37 页（模块概览 + 函数索引 + 调试日志）
- **框架文档**: `wiki/architecture/system-framework.md`
- **仪表盘**: `wiki/dashboard.md`
- **MOC**: `wiki/uwacomm-moc.md`

## Hub wiki 关联

- [underwater-acoustic-communication](../../wiki/concepts/underwater-acoustic-communication.md)
- [channel-estimation-and-equalization](../../wiki/concepts/channel-estimation-and-equalization.md)
- [message-passing-algorithms](../../wiki/concepts/message-passing-algorithms.md)
- [ofdm-and-otfs](../../wiki/concepts/ofdm-and-otfs.md)
- [time-varying-channel](../../wiki/concepts/time-varying-channel.md)
