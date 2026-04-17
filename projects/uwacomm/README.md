# UWAcomm

> 水声通信算法仿真平台 — MATLAB 全栈，6 种通信体制，14 模块

- **仓库**：github.com/lyrenleigh-code/UWAcomm
- **本地**：`D:\Claude\TechReq\UWAcomm`
- **状态**：活跃开发中
- **规模**：258 个 MATLAB 文件，38 649 行代码，14 个模块（截至 2026-04-17）

## 体制进度

| 体制 | 版本 | 静态 | fd=1Hz (Jakes) | 离散 Doppler (disc-5Hz) | hyb-K10 |
|------|------|------|----------------|-------------------------|---------|
| **SC-TDE** | V5.1 | 0%@20dB | 0.76%@15dB | **0%@5dB+** | **0%@5dB+** |
| **SC-FDE** | V4.0 | 0% | 0.20%（盲估） | 0.88%@10dB | 0%@10dB+ |
| **OFDM** | V4.3 固化 | 0% | ~1%@15dB | **0%@10dB+** | **0%@10dB+** |
| **OTFS** | V2.0 | 0%@5dB+ | 0%@10dB+ | **0%@10dB+** | 0.27%@10dB |
| **DSSS** | V1.0 | 0%@-15dB+ | 0%@0dB | **0%@-10dB+** | **0%@-10dB+** |
| **FH-MFSK** | V1.0 | 0%@10dB | 0%@5dB | **0%@0dB** | **0%@0dB** |

4 体制（OFDM / SC-TDE / SC-FDE / FH-MFSK）已接入流式框架 `modem_dispatch` 统一 API（2026-04-15/16）。

## 模块架构

```
TX: 02编码 → 03交织 → 04调制 → [05扩频|06多载波] → 09成形 → 08帧组装
CH: 13信道仿真 → 09上变频 → +噪声
RX: 09下变频 → 10多普勒补偿 → 08同步 → 07信道估计均衡 → 12Turbo迭代 → 03解交织 → 02译码
14: 流式仿真框架（loopback / detect / 统一 modem / 调度）
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
| 14 流式仿真 | passband 原生信道 + hybrid 检测 + modem 统一调度 + UI | 25 |

## 关键技术结论

1. 散布导频是精度决定性因素（比算法选择影响大 10-20dB）
2. BEM(DCT)+散布导频最优
3. FDE 在长时延信道下全面优于 TDE（5dB 编码增益）
4. 两级分离架构有效（多普勒估计与定时解耦）
5. Jakes 连续谱确认为伪瓶颈，离散 Doppler 下 6 体制全可工作
6. FH-MFSK 唯一全信道可工作体制
7. **接收端禁用发射端参数**（oracle 仅作 baseline，已上升为硬约束）
8. **流式 passband 原生信道**（`gen_uwa_channel_pb`）避免 baseband 下变频概念混乱
9. **流式帧检测 hybrid 优于纯阈值**（首帧绝对最大锚定 + 后续窗口本地最大）
10. **FH-MFSK 软判决 LLR** 显著改善衰落鲁棒性，但多径展宽 > 50% 符号时长仍崩

## 当前开发方向

| 方向 | spec / 状态 |
|------|------------|
| 去 oracle 接收参数化 | `2026-04-16-deoracle-rx-parameters` 活跃 |
| OTFS 通带 2D 脉冲整形 | `2026-04-13-otfs-pulse-shaping` 活跃 |
| OTFS 两级同步架构 | `2026-04-13-otfs-sync-architecture` 活跃 |
| OTFS 散布导频 | `2026-04-14-otfs-spread-pilot` 活跃 |
| 流式 P4 scheme routing | `2026-04-15-streaming-p4-scheme-routing` 活跃 |
| 流式 P5 并发 | `2026-04-15-streaming-p5-concurrent` 活跃 |
| 流式 P6 AMC | `2026-04-15-streaming-p6-amc` 活跃 |
| P3 demo UI 美化/重构 | `2026-04-17-p3-demo-ui-polish` + `refactor` 活跃（SC-FDE 待收敛） |

## 项目内导航

- **wiki**: `wiki/index.md` — 40 页（模块概览 + 函数索引 + 调试日志 + E2E 测试矩阵）
- **框架文档**: `wiki/architecture/system-framework.md`（v6）
- **技术结论**: `wiki/conclusions.md`（26 条累积）
- **仪表盘**: `wiki/dashboard.md`
- **MOC**: `wiki/uwacomm-moc.md`
- **E2E 测试矩阵**: `wiki/comparisons/e2e-test-matrix.md`

## Hub wiki 关联

- [underwater-acoustic-communication](../../wiki/concepts/underwater-acoustic-communication.md)
- [channel-estimation-and-equalization](../../wiki/concepts/channel-estimation-and-equalization.md)
- [message-passing-algorithms](../../wiki/concepts/message-passing-algorithms.md)
- [ofdm-and-otfs](../../wiki/concepts/ofdm-and-otfs.md)
- [time-varying-channel](../../wiki/concepts/time-varying-channel.md)
- [uwacomm](../../wiki/entities/uwacomm.md)
