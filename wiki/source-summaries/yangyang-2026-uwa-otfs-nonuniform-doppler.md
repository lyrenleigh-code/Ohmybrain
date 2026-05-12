---
type: source-summary
created: 2026-04-22
updated: 2026-04-22
tags: [UWAcomm, OTFS, 水声通信, 非均匀多普勒, 信道估计, 块稀疏, off-grid, BSOMP, MLE, 延迟多普勒域, 海试]
source_type: paper
source_path: D:/Claude/TechReq/UWAcomm/raw/papers/Underwater_Acoustic_OTFS_With_Nonuniform_Doppler_Shifts_Modeling_and_Off-Grid_Block-Sparse_Channel_Estimation_Algorithm.pdf
source_project: UWAcomm
---

# Underwater Acoustic OTFS With Nonuniform Doppler Shifts: Modeling and Off-Grid Block-Sparse Channel Estimation Algorithm

> **引用**：Yang, Y., Ma, L., Liu, S., Qiao, G., Song, Y., & Li, T. (2026). *Underwater Acoustic OTFS With Nonuniform Doppler Shifts: Modeling and Off-Grid Block-Sparse Channel Estimation Algorithm*. IEEE Journal of Oceanic Engineering, 51(1), 641-658.
>
> **DOI**: 10.1109/JOE.2025.3599256
>
> **通讯作者**：Lu Ma (malu@hrbeu.edu.cn)

## 来源信息

| 项 | 值 |
|-----|-----|
| 作者 | Yang Yang, Lu Ma, Songzuo Liu, Gang Qiao, Yang Song, Tong Li |
| 机构 | 哈尔滨工程大学 水声工程学院 + 水声技术国家重点实验室 + 三亚南海创新发展基地（Ma/Liu/Qiao） |
| 期刊 | IEEE Journal of Oceanic Engineering（Associate Editor: M. Stojanovic） |
| 接收 / 接受 | 2024-12-10 收稿 → 2025-04-03 / 2025-06-23 修订 → 2025-07-21 接受 → 2025-11-10 在线 → 2026-01 刊出 |
| 卷期 | Vol. 51, No. 1, pp. 641-658 |
| 页数 | 18 页（正文 + 三个附录 + 59 条参考文献） |
| 资助 | 国家重点研发 2023YFC3010800 + NSFC 62271161 + 山东省重点研发 2022CXGC020409 + 水声技术国重 2023-JCJQ-LB-072-08 |
| PDF 路径 | `D:/Claude/TechReq/UWAcomm/raw/papers/Underwater_Acoustic_OTFS_With_Nonuniform_Doppler_Shifts_Modeling_and_Off-Grid_Block-Sparse_Channel_Estimation_Algorithm.pdf`（5.4 MB） |

## 核心观点

1. **UWA-OTFS 的关键区别于无线 OTFS：载频接近带宽导致"宽带非均匀多普勒"** —— 无线 OTFS 场景下窄带 + 单径假设使所有子载波共享一个小数多普勒；水声 OTFS 中 `fc/B ≈ O(1)`（论文仿真 `fc=3 kHz, B=2 kHz`），每条传播路径具有独立的多普勒因子 α_p，时间压缩/拉伸效应不可忽略，需要在 DD 域完整建模残留多普勒因子（residual Doppler factor）的影响，而非沿用窄带近似。
2. **重采样不是万能的，"重采样 + 残留 Doppler 因子"是新范式** —— 传统做法用 LFM 预估 α̂ 做时域重采样补偿主多普勒；论文正视重采样后残留的 `b_p = (1+α_p)/(1+α̂) − 1` 仍在多径间分布（0 均值，跨路径不同），明确把 b_p 作为一等公民引入 DD 域输入输出关系的推导，把"主多普勒压缩/展宽"与"残留多普勒引起的 IDI"解耦。
3. **DD 域闭式模型 + 多项式近似是降维突破口** —— 对含 `e^{j2π(n/N)·k_{bp,m'}}` 的求和项（子载波索引耦合的多普勒项），引入 `Σ_{j=0}^{J} e^{j2π(n/N)·α(j)}` 形式的多项式近似（J=M-1），把 m' 子载波求和重组为对所有子载波共同承担的 `k_{bp,j} = NT·b_p·(f_c + j/T)` 的和式，得到 Eq.(20) 的统一闭式表达。这一步把"非均匀多普勒的每子载波微分"转化为"可计算的多项式基展开"。
4. **UWA-OTFS 在 DD 域呈现块稀疏（block-sparse）结构** —— 残留 Doppler 因子引起 Doppler 轴能量泄漏，对每条路径 p 集中在 `q ∈ [-N_{j,p}, N_{j,p}]` 区间（论文示 `q=4 处衰减 25 dB`），延迟轴仍是稀疏脉冲。因此等效信道矩阵呈现"沿延迟轴单点、沿多普勒轴小带状"的块状稀疏结构——这是后续 BSOMP 算法的数学基础，也是"可以只用 BSOMP 替代 OMP 并获得精度-复杂度平衡"的原因。
5. **OG-BSOMP-MLE 两步走：块 OMP 做粗估 + MLE 多项式拟合做细估** —— 第一步用块正交匹配追踪在 DD 网格上定位路径块（得延迟 l̂_τ 和整数频移粗估），第二步在路径块上用极大似然在一维 b_t 上做网格化搜索 + 抛物线拟合 + 精细化二次搜索，得到残留 Doppler 因子的连续值估计。这种"粗定位 + 细拟合"回避了 SBL 的高维稀疏恢复，同时拿到连续 off-grid 精度。
6. **收敛准则用"最大相关 / 平均相关 ≈ 4"作为噪声判据** —— 根据极值理论，N=M=1024 的 i.i.d. 高斯变量其最大值期望约为均值的 4 倍，论文据此定义 `η = max(|X_p^H r_t|) / (4·mean(|X_p^H r_t|))`，`η < 1` 即认为残差是噪声主导，终止迭代。这个统计准则优于固定阈值，对 SNR 自适应。
7. **复杂度结构：O(M_T·N_T·N_p² + (M_b+N_b)·N_p·MN)，显著低于 OG-SBL 的 O(5·M_τ²·N_v²·M_T·N_T)** —— 其中 N_p = 2ω+1 = 9（路径块大小）远小于 M_T·N_T。论文的本质是"以块稀疏+MLE 替代全域 SBL 稀疏恢复"，把 SBL 的 O(M_τ²·N_v²·...) 瓶颈化为 O(N_p·MN) 的一维拟合成本。
8. **仿真关键参数：`fc=3 kHz, B=2 kHz, M=256, N=16, T_cp=30 ms, 4QAM, rate=1971 bps`；Doppler 扩展 σ_v 分三档（0.05/0.15/0.75 m/s 对应温和/中等/严重）** —— 信道 5 径指数延迟（6 ms 均值，30 ms 最大扩展），路径速度在 `[v_0 − √3·σ_v, v_0 + √3·σ_v]` 均匀分布。`σ_v` 越大，OG-BSOMP-MLE 相对 OG-SBL 优势越明显，因为 SBL 假设子载波共享单一小数多普勒（仅在 σ_v 温和时成立）。
9. **海试：2024 年 5 月南海 5.5 km 水深，接收 1100 m，发射 30 m，拖曳 2 m/s，31 包数据** —— 中心频率 3 kHz，2000 bps OTFS，M=256, N=24。LFM 前后对比粗估 α̂，DD 域用 OG-BSOMP-MLE 估残留 b_p。多径主分量 b_p ≈ 0（主多普勒已被重采样消除），次径因海面海底多次散射而与相对速度反相关，印证重采样零均值假设。
10. **OTFS 相比 OFDM 在水声移动场景的实测优势** —— 同等带宽与通信速率（1200 bps）下，OFDM 用插值型超规模 FFT 补偿非均匀多普勒 + MMSE 均衡 + 1/2 LDPC，OTFS 用 OG-BSOMP-MLE + 单抽头 TF 域 MMSE + 1/2 LDPC。OTFS 原始 BER 始终低于 OFDM，多数包在 LDPC 后可成功译码。原理：DD 域每符号经历完整 TF 域信道→天然时频分集增益 + 对突发干扰鲁棒。
11. **带宽受限下多普勒容限与延迟估计范围的内在耦合** —— 对 `B=4 kHz, fc=6 kHz, v=2 m/s`，`Δf = B/M ≥ f_shift = 8 Hz` 的约束把最大延迟估计限定到 12.5 ms（对水声远不够）。因此**重采样做主多普勒预处理是工程必选**，再用 OG 方法补精度。这揭示了 UWA-OTFS 参数设计的约束三角：M（多普勒分辨率）↔ 1/Δf（延迟估计范围）↔ 信号带宽 B。
12. **两假设值得注意：延迟轴落整数格 + 残留 Doppler 零均值** —— 前者来自"延迟分辨率 1/B（0.5 ms）远小于多径延迟间隔（≥ 6 ms）"，后者来自"重采样消除了 α_p 的非零均值"。这两个假设在中窄带 B=2 kHz 场景成立，**但当 σ_v 很大导致延迟轴也展宽时，步骤 4 的 delay-by-max 定位法失效**——论文坦承这是算法上限。

## 核心贡献

| 创新点 | 解决的问题 | 性质 |
|--------|-----------|------|
| 含残留 Doppler 因子 b_p 的 UWA-OTFS DD 域闭式输入输出关系推导（Eq.11-20, Appx A-C） | 无线 OTFS 窄带假设在水声不适用，需建模子载波间的非均匀多普勒 | 信道建模 |
| UWA-OTFS 等效信道 DD 域"块稀疏"性质证明（延迟轴单点 + 多普勒轴带状） | 为低复杂度信道估计提供数学前提 | 信道性质 |
| OG-BSOMP-MLE 两步信道估计算法（BSOMP 粗估 + MLE 多项式拟合细估） | OMP/threshold 受限于格点精度，OG-SBL 复杂度过高 | 算法 |
| 极值理论给出的 `η<1` 自适应停止准则 | 取代固定残差阈值，对 SNR 自适应 | 算法工程化 |
| 南海 5.5 km 水深 + 2 m/s 拖曳 + 31 包 OTFS 海试数据集与 BER 验证 | 现有 UWA-OTFS 文献实测数据稀缺（[24] 仅 1 m/s） | 海试验证 |
| 2 kHz 窄带 + 3 kHz 中心频率下的 UWA-OTFS vs OFDM 同速率对照 | 量化 OTFS 在水声移动的实测优势 | 对比基准 |

## 主要方法

### 方法 1：DD 域闭式输入输出关系推导（Sec. III + Appx A-C）

**链路**：UWA 多径信道 (Eq.5) → 时域重采样 (Eq.6) → 匹配滤波 TF 域 (Eq.10) → 辛傅里叶变换到 DD 域 (Eq.14-15) → 多项式近似简化 (Eq.17-20)

**关键技术点**：
- **ICI 与 ISI 分离**：`H_{n,m}[n',m']` 仅在 `n'=n`（ICI，当前符号）与 `n'=n-1`（ISI，前符号）时非零；分别给出积分区间 `t'' ∈ [n·b_p·T + τ_p']/(1+b_p) → T]`（ICI）和 `[0 → (n-1)·b_p·T + τ_p']/(1+b_p)`（ISI）
- **频移索引**：`b_p·f_m' = k_{bp,m'}/(NT)` 把子载波相关的多普勒映射到 DD 域 Doppler 轴索引
- **多项式拟合核心**：`Σ_{m'=0}^{M-1} e^{-j2π(m'/M)·σ}·e^{j2π(n/N)·k_{bp,m'}}` ≈ `M·δ([σ]_M)·Σ_{j=0}^{J} e^{j2π(n/N)·α(j)}`，在 σ=0（延迟落整数格）时精确，α(j) = k_{bp,j} = NT·b_p·(f_c + j/T)
- **最终表达** Eq.(20) 用 `β_{kl}(p,j,k') = (e^{-j2π(k-k'-k_{bp,j})}-1)/(e^{-j(2π/N)(k-k'-k_{bp,j})}-1)` 的 Dirichlet 核形式给出 `y[k,l]` 对 `x[k', [l-l_{τp}]_M]` 的线性变换

### 方法 2：块稀疏模型推导（Sec. IV.A）

- 路径 p 的 DD 域增益对索引 q 的幅值满足 `|h_{gain}(q)| ≤ |ζ_{pj}|·Σ_j |r(q)|`，其中 `r(q) = Σ_n e^{-j2π(n/N)(-q-⟨k_{bp,j}⟩)}`
- 峰值在 `q=0`，`q=4` 处衰减 25 dB（仿真 `b_p ∈ [−10⁻⁴, 10⁻⁴], N=24`）
- **块宽 2·N_{j,p}+1 = 9 足以覆盖每条路径 99.7% 能量**，成为 BSOMP 的自然块参数

### 方法 3：OG-BSOMP-MLE 算法（Algorithm 1）

**输入**：感知矩阵 X_p（大小 `M_T·N_T × M_T·N_T`），观测 y，稀疏度 P，块参数 ω=4

**迭代**：
1. **块选择**（BSOMP core）：`λ_t = argmax_l |⟨r_{t-1}, x_l⟩|`
2. **支撑扩展**：`Λ_t = {λ_t ± ω}`（总 `N_p = 2ω+1 = 9` 列）
3. **最小二乘增益估计**：`ĥ_t(Λ_t) = (X_p(Λ_t)^T X_p(Λ_t))^{-1} X_p(Λ_t)^T r_{t-1}`
4. **延迟估计**：`l̂_{τt} = argmax |ĥ_t(Λ_t)|`
5. **残留 Doppler MLE**：
   - 初选：`N_b` 个粗网格点 `b_t^{(i)} ∈ [b_{min}, b_{max}]`，计算误差 `E(b_t^{(i)}) = Σ_q (|ĥ_t(Λ_t)| − |h_{gain}(q, b_t^{(i)})|)²`
   - 二次多项式拟合 `[a_0, a_1, a_2]^T = (A^T A)^{-1} A^T E`，若 `a_2 > 0` 取极值 `b* = −a_1/(2a_2)`，clip 到 `[b_{min}, b_{max}]`
   - 精细搜索：`M_b` 个细网格点在 `[b* − δ, b* + δ]` 内，δ = (b_max − b_min)/N_b
   - 最终 `b̂_t = argmin E(b_t,fine^{(j)})`
6. **残差更新**：`r_t = r_{t-1} − X_p·ĥ_t`；若 `η = max|X_p^H r_t|/(4·mean|X_p^H r_t|) < 1` 则终止

**算法哲学**：用**粗一维搜索 + 抛物线拟合**代替 SBL 的高维稀疏贝叶斯求解，在路径块上定位 b_t，既避免 grid mismatch 又规避 SBL 矩阵求逆。

### 方法 4：对照算法

| 算法 | DD 域格点 | Off-grid 精度 | 复杂度 | 特点 |
|------|----------|---------------|--------|------|
| OMP [57] | 整数格点 | 无 | O(M_T·N_T·N_p²) | 基线 |
| Threshold-based [56] | 整数格点 | 无 | 低 | 等效 OMP 第一步 |
| OG-SBL [33] | 虚拟细格 | 有（SBL 推断） | O(5·M_τ²·N_v²·M_T·N_T) | 精度高但贵 |
| **OG-BSOMP-MLE（本文）** | 整数格点 + 连续 b_t | 有（1D 多项式拟合） | O(M_T·N_T·N_p² + (M_b+N_b)·N_p·MN) | 精度接近 OG-SBL，复杂度远低 |

## 关键数据 / 结果

### 仿真 NMSE（Fig. 6, σ_v=0.15 m/s, v_0=3 kn）

- OMP / Threshold：NMSE 基本饱和在 −5 dB 左右（因 IDI）
- OG-SBL：随 SNR 提升持续下降
- **OG-BSOMP-MLE：高 SNR 下优于 OG-SBL**，在 SNR=20 dB 附近差距最明显

### 原始 BER（Fig. 9-10）

| 条件 | OMP/Threshold | OG-SBL | OG-BSOMP-MLE |
|------|---------------|--------|--------------|
| v_0=3 kn, σ_v=0.05 m/s | 饱和 ~10⁻¹ | 较好 | 与 OG-SBL 相当 |
| v_0=3 kn, σ_v=0.15 m/s | 饱和 ~10⁻¹ | 中等 | 高 SNR 略优 |
| v_0=3 kn, σ_v=0.75 m/s | 严重退化 | 退化 | **最优**（优势明显） |
| v_0=15/30 kn, σ_v=0.15 m/s | 退化 | 退化 | 较稳 |

**关键结论**：OG-BSOMP-MLE 在 σ_v 增大（Doppler 扩展严重）时优势拉开，因为 OG-SBL 的"均匀频移"假设失效。

### 海试（Fig. 20-22, South China Sea, 5.5 km 水深, 2 m/s）

- 31 包数据中，残留 b_p 主径近 0、次径与相对速度反相关（符合 Eq.6 理论）
- 31 包 BER 对照：OG-BSOMP-MLE 始终低于 OMP，平均约低 0.5-1 个数量级
- OTFS vs OFDM（1200 bps 同速率）：OTFS 原始 BER 更低，LDPC 后大多数包可解码；OFDM 在高多普勒条件下 BER 劣化显著
- 星座图（Fig. 21）：OMP 估计残留相位失真明显，OG-BSOMP-MLE 星座簇更清晰

## 对 Ohmybrain / UWAcomm 项目的启发（双层）

### 对 UWAcomm 项目的直接借鉴（技术层）

1. **UWAcomm 模块 07 (OTFS) 的 DD 域导频估计应升级到"残留 Doppler + 块稀疏"范式** —— 当前实现如假设均匀多普勒或仅做 OMP 整数格估计，应该直接照搬 Algorithm 1 的两步流程（BSOMP 粗估 + MLE 抛物线拟合）；闭式 Eq.(20) 可直接实现为查表型基函数 h_{gain}(q, b_t)。
2. **`η = max / (4·mean) < 1` 作为 OMP 家族迭代停止准则** —— 这是所有基于 CS 的信道估计（UWAcomm 模块 06/07/08）都应采用的无超参停止条件，替换掉经验阈值 ε。
3. **UWAcomm 已有的双 LFM α 精估（2026-04-22 项目记录）可与本文 MLE 二阶多项式拟合结合** —— 项目已做的"迭代 refinement"和论文的"MLE 抛物线 + 精细搜索"本质同构。可把双 LFM α̂_1, α̂_2 结果作为粗网格初值，在 DD 域再做 b_p 精调；这是项目 `alpha_refinement` 任务的自然延续。
4. **UWAcomm 的"四体制对照 benchmark"（2026-04-19 S1）应引入 OG-SBL 与 OG-BSOMP-MLE 作为 OTFS 对照** —— 论文已证明 OG-BSOMP-MLE 与 OG-SBL 在精度-复杂度维度的对照关系，UWAcomm benchmark 可直接复用这个对照基线构建 OTFS 体制的"估计算法库"。
5. **仿真参数 `fc=3kHz, B=2kHz, M=256, N=16, 4QAM` 可作为 UWAcomm OTFS 模块的默认基准场景** —— 与 UWAcomm 现有场景设定兼容，方便做 reproducibility 测试。
6. **"延迟整数格 + 残留 Doppler 连续"假设的分界线：σ_v ≤ 0.15 m/s** —— 超过这个阈值（≈ 5.8 节 BER 曲线衰减开始明显），论文算法失效。UWAcomm 如要覆盖 σ_v > 0.5 m/s 的极端场景，需要做延迟轴的联合 off-grid 估计——这是论文的上限与未来方向。
7. **同频率同速率 OTFS vs OFDM 的对比应是 UWAcomm 最终 benchmark 的核心图** —— 用 `B=2 kHz, fc=3 kHz, rate=1200 bps, σ_v` 三档 + LDPC 前后 BER 四象限，直接复刻 Fig. 14/22 的对照风格。
8. **海试设计参考**：**5.5 km 水深 + 拖曳 2 m/s + 每 6 min 发一包共 31 包** 是一个可实现的最小海试配置，UWAcomm 若将来要做外场验证，这个配方可作为模板。

### 跨项目（Hub 层）价值

9. **"宽带系统中非均匀多普勒建模"是水声/太赫兹/卫星通信共性问题** —— 论文 [49] 引用了 LEO 卫星 + 太赫兹超大规模 MIMO 的相关工作，证明 UWA 中的 α·f 频散与太赫兹 THz-MIMO、LEO 卫星高移动性面临相同数学结构（`fc/B ≈ O(1)`）。这个跨领域共性使得本文的 DD 域块稀疏 + OG-MLE 方法可迁移到 UWAnet 未来的 THz 水声混合链路、USBL 高移动性定位。
10. **"粗网格搜索 + 抛物线拟合 + 精细网格搜索"是普适的一维参数估计范式** —— 在 USBL 三点插值（喻敏 2006）、UWAcomm α 精估、本论文 b_t 估计中反复出现，是信号处理中"低复杂度连续参数估计"的经典套路。应沉淀为 Hub 层的通用方法卡。
11. **"block-sparse + OMP → BSOMP"是稀疏结构匹配的一类普适改造** —— 凡是"稀疏主骨架 + 每骨架点小邻域扩散"的物理结构（多径 + 多普勒泄漏、DOA + 阵列校准误差、雷达距离-速度检测），都可以套用本文"BSOMP 粗定位 + MLE 模型拟合精细化"的两步式。这是对 [[mathematical-optimization]] 概念卡中"稀疏恢复"类别的重要补充。
12. **极值理论的 `max/mean ≈ 4` 停止准则是一个被低估的普适工具** —— 对 i.i.d. 高斯变量的极值分布理论给出的统计判据，可以替换掉各种 CS 类算法中的经验阈值。Hub 层应有一个"无参数停止准则"合集。
13. **DD 域（延迟-多普勒）作为双域物理信道表示的哲学深化** —— 不仅是 OTFS，任何双离散（doubly-dispersive）信道（水声移动、雷达-通信一体化 ISAC、星地链路）都在 DD 域呈现稀疏或块稀疏结构。这使 DD 域成为"高移动性 + 多径"通信场景的共同语言，值得在 Hub 层单独做一个 DD 域建模的概念卡。
14. **"重采样补主项 + 建模残差"是工程化信号补偿的典型范式** —— 不追求单步完美补偿，分两层：粗补偿（重采样）消除主要能量，精补偿（MLE）处理残差。这是比 USBL 论文（喻敏 2006）"非线性 LS → 逐次 LS → M 估计"更通用的"分层残差建模"思想，可抽象到 Hub 层。
15. **"closed-form + polynomial approximation" 让复杂积分变可计算**的推导哲学 —— 论文 Eq.(17) 的 Dirichlet 核近似是核心技巧：遇到含子载波索引耦合的求和，先做多项式展开，再用 δ 函数折叠，最终化归到 `Σ e^{j2π α(j)}` 的有限和形式。这个技巧值得沉淀为 UWAcomm 与 UWAnet 未来建模的标准套路。

## 相关概念

- [[ofdm-and-otfs]] — 本论文是 UWA-OTFS 的标杆工作（IEEE JOE 2026），"非均匀多普勒建模 + DD 域块稀疏 + OG-BSOMP-MLE"是 OTFS 信道估计的水声专用分支
- [[channel-estimation-and-equalization]] — OG-BSOMP-MLE 是"块稀疏 CS + 极大似然"两步范式的代表，补充了传统 OMP/SBL 之外的第三条路线
- [[time-varying-channel]] — 残留 Doppler 因子 b_p 的建模是时变信道描述的精细化版本，揭示了"重采样后剩余时变性"的本质
- [[underwater-acoustic-communication]] — `fc/B ≈ O(1)` 的宽带特征是 UWA 有别于无线通信的核心物理约束，本论文给出了该约束下的 OTFS 系统完整设计
- [[signal-processing-fundamentals]] — Dirichlet 核、多项式近似、极值理论停止准则都是信号处理基础方法在 UWA-OTFS 中的集成
- [[mathematical-optimization]] — MLE + 抛物线拟合 + 精细搜索的分层优化，以及 `η < 1` 的统计停止准则，都是稀疏优化的实用工程化
- [[mobile-communication]] — UWA-OTFS 正是为"水下高移动性平台通信"而生；2 m/s 海试对应中低速水下载体

## 相关资料

- UWAcomm 项目 wiki（若建）：`D:/Claude/TechReq/UWAcomm/wiki/source-summaries/yangyang-2026-uwa-otfs-nonuniform-doppler.md`
- UWAcomm 模块 07 (OTFS) 当前实现：`D:/Claude/TechReq/UWAcomm/src/modules/07_*`（导频结构设计参考本论文 Sec. IV.A + Fig. 4）
- UWAcomm α 精估改造（2026-04-22 记录）：双 LFM + 迭代 refinement，与本论文 MLE 二阶拟合互补
- UWAcomm E2E benchmark（2026-04-19 S1 完成）：7 工具 + 11 runner，未来 S2-S4 可引入本论文作为 OTFS 体制的估计基线
- 同作者团队（Lu Ma, Songzuo Liu 哈工程组）其他 UWA-OFDM/OTFS 论文（ref [3][8][59]）：`D:/Claude/TechReq/UWAcomm/raw/papers/`
- Berger-Zhou 2010 UWA 信道稀疏估计（ref [4], IEEE TSP）：CS 框架在 UWA 的奠基工作，本论文多处引用其信道模型
