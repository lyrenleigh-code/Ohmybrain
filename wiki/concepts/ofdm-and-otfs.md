---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [OFDM, OTFS, 多载波调制, 高速率, QAM]
---

# OFDM 与 OTFS 调制

## 定义

OFDM（正交频分复用）和 OTFS（正交时频空间）是两种多载波调制技术。OFDM 将宽带信道分解为多个窄带子信道，在频域实现简单均衡；OTFS 在时延-多普勒域放置信息符号，天然适配双色散信道。该方向聚焦于这两种调制方案在水声通信中的应用与改进。

## 核心问题

- **OFDM 在水声信道中的载波间干扰（ICI）**：多普勒效应破坏子载波正交性
- **OTFS 的时延-多普勒域信号处理**：如何在时延-多普勒域高效检测
- **OFDM 的高峰均功率比（PAPR）**：影响功放效率
- **频域信道估计**：导频设计与插值方案
- **MIMO-OFDM / MIMO-OTFS**：多天线与多载波的结合
- **高速率传输**：QAM 调制阶数选择与误码率权衡
- **多普勒补偿策略**：OFDM 系统的多普勒预补偿

## 关键技术

- CP-OFDM / ZP-OFDM 系统设计
- OTFS 调制/解调（ISFFT/SFFT）
- 时延-多普勒域信道估计
- ICI 消除与均衡
- PAPR 抑制技术
- 自适应比特/功率加载
- MIMO-OFDM 空频编码
- MIMO-OTFS 检测算法

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| OTFS | ~25 | OTFS 调制技术 |
| MIMO-OTFS | ~15 | MIMO-OTFS 系统 |
| Hign-Rate | ~14 | 高速率传输方案 |
| QAM Signal | ~10 | QAM 信号处理 |

总计约 **64 篇**。

## 相关概念

- [[underwater-acoustic-communication]] — OFDM 和 OTFS 是水声通信的重要调制方案
- [[channel-estimation-and-equalization]] — 多载波系统中的信道估计与均衡
- [[time-varying-channel]] — OTFS 天然适配时变双色散信道
- [[mimo-and-array-processing]] — MIMO-OFDM 和 MIMO-OTFS 系统
- [[message-passing-algorithms]] — OTFS 检测中的消息传递方法
- [[mobile-communication]] — OFDM 技术源自移动通信

## 实战结论（memory 蒸馏 @2026-08-18，源=UWAcomm OTFS 2026-04~05 实测）

- **OTFS pilot 三方案 tradeoff 实测**：superimposed 的优势只有 PAPR（16.8→8.9 dB）和数据率（+10%），BER 不优于 impulse——按链路预算瓶颈选，不按论文默认选（另见 memory `reference_otfs_pilot_tradeoff`）。— UWAcomm 04-27/05-06
- **OTFS 脉冲成形 hann 全线退化**（static 0%→11%，各 fading 一致变差），维持 rect；「更平滑的窗」直觉在 DD 域不成立。— UWAcomm 05-06 Phase 4 FAIL 归档
- **OTFS 对连续谱 Jakes 同样灾难**（fd=5Hz 33-44%），与 SC-FDE 同构，DD 域表征不豁免连续谱问题——见 [[time-varying-channel]] 实战结论。— UWAcomm 04-27
- JSON 序列化会把 1×2 行向量还原成 2×1 列（`jsondecode`），OTFS meta 维度必须显式校正——跨语言/跨进程传参数矩阵的通用坑。— UWAcomm 05-04
- **OTFS DD 域实现五硬约束**：x_dd 第二维必须是时延索引（modulate 行 FFT / demodulate 行 IFFT，否则信道延迟只表现为相位旋转）；CP 必须 per-sub-block 而非帧级（帧级 CP 引入跨子块 β=exp(-j2πk/N)，BCCB 模型失效）；LMMSE 输出送 LLR 的必须是原始 x_mmse 而非星座解映射值（否则 coded BER > uncoded）；Turbo 先验方差 guard/data 统一（guard 设 1e-6 会拉低全局 v_x 过度正则化）；LMMSE 内部 SIC 只 1 轮，多轮交外层 Turbo（无 Onsager 修正低 SNR 发散）。旧规则仍有效：不用 RRC（ISI 破坏 DD 关系）/ 导频 boost √N_data / cp_len 留余量（8→32 静态 BER 2.64%→1.35%）。— UWAcomm 2026-04-11 旧 memory `feedback_otfs_pitfalls`（08-29 误回流副本，撤回前蒸馏 @2026-08-30）
- **DD 网格 M 是 fd 上限与均衡质量的折中，减 M 不一定改善**：BCCB 要求子块内信道恒定 fd·T_sub≪1（M=64@fs=6k → T_sub=10.67ms，fd=5Hz 已 19° 相位变化）；M 减半频率 bin 减半 → 信道零点比例翻倍 → LMMSE 更差。oracle 不一定优于估计：fd=5Hz 全 guard 响应给出 ~80 径 LMMSE/MP 都处理不了，自适应阈值估计（static <10% 用 3σ / 时变 >10% 用 1σ，guard 区 median 估噪底）反而更好。— UWAcomm 2026-04-11 旧 memory `feedback_otfs_pitfalls`（08-29 误回流副本，撤回前蒸馏 @2026-08-30）
- **UAMP 对 BCCB 结构无优势**：LMMSE per-frequency 权重 D*/(|D|²+λ) 已最优，UAMP uniform 权重更粗糙，单次 ≈ LMMSE 且 Turbo 集成不稳定（内部 5 轮迭代放大先验误差）——坚持 LMMSE。**通带 interpft 整帧上采样触发 Gibbs 振铃**（子块边界不连续 → sinc 振铃尖刺），修复 = 逐子块独立 interpft + 升余弦过渡。— UWAcomm 2026-04-11 旧 memory `feedback_otfs_pitfalls`（08-29 误回流副本，撤回前蒸馏 @2026-08-30）
- **OFDM 均衡必须逐子载波 MMSE-IC 且 nv_k 用 nv_post 兜底**：标量 mu 的 `eq_mmse_ic_fde` 对频选信道不适用；高 SNR 时好子载波 nv_k→0 使 scale_k→∞、LLR 过度自信（fd=1Hz@25dB 3.81%），须用 CP 已知符号实测残差方差 nv_post 作 nv_k 下限；OFDM 比 SC-FDE 标量 MMSE-IC 更敏感（后者天然平均了子载波差异）。信道估计高 SNR 用 OMP 不用 GAMP（tau_s 发散，static@15dB+ 46%）。— UWAcomm 2026-04-11 旧 memory `feedback_ofdm_equalizer`（08-29 误回流副本，撤回前蒸馏 @2026-08-30）

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[uwacomm]] — 模块 06 实现了 OFDM/OTFS/SC-FDE 多载波变换，模块 07 实现了 OTFS DD 域导频估计和 LMMSE-BCCB/MP 消息传递均衡
- [[muzzammil-2019-cpofdm-doppler-interp]] — CP-OFDM 多普勒尺度 α 的自相关闭式表达 + 三种三点插值细化
- [[yangyang-2026-uwa-otfs-nonuniform-doppler]] — IEEE JOE 2026 UWA-OTFS 标杆：非均匀多普勒闭式建模 + DD 域块稀疏 + OG-BSOMP-MLE 信道估计
- [[zhengtonghui-2025-dd-mmse-teq]] — SC 发 + DD 接机的体制重组，引入 van der Werf 2024 的 OSDM=OTFS 等价证明
- [[uwacomm-otfs-pilot-tradeoff]] — UWAcomm OTFS 三方案（Impulse/ZC/Superimposed）PAPR-NMSE-复杂度 tradeoff 参考（2026-04-14 实测）
