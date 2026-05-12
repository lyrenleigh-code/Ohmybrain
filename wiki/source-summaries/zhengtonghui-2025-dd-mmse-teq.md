---
type: source-summary
created: 2026-04-22
updated: 2026-04-22
tags: [水声通信, 单载波, Turbo均衡, 时延多普勒域, OTFS, MMSE, 时变信道, 因子图, 信道估计, IEEE-JOE, 丹江口湖试]
source_type: paper
source_path: D:/Claude/TechReq/UWAcomm/raw/papers/Delay-Doppler_Domain_Turbo_Equalization_for_Single-Carrier_Underwater_Acoustic_Communications.pdf
source_project: UWAcomm
---

# 单载波水声通信的时延-多普勒域 Turbo 均衡（DD-MMSE-TEQ）

> **引用**：Zheng T., He C., Jing L., Yan Q. (2025). *Delay-Doppler Domain Turbo Equalization for Single-Carrier Underwater Acoustic Communications*. IEEE Journal of Oceanic Engineering, 50(2), 1500-1517. DOI: 10.1109/JOE.2024.3508027.
>
> **作者单位**：西北工业大学海洋科学与技术学院（何成兵团队，海洋研究院），西安 / 太仓
> **投稿**：2024-02-21 / 修改 2024-07-17 / 录用 2024-10-22 / 在线 2025-01-08

## 来源信息

| 项 | 值 |
|-----|-----|
| 第一作者 | 郑通辉（Tonghui Zheng，NPU 博士生） |
| 通讯作者 | 何成兵（Chengbing He，NPU 教授） |
| 合著 | 敬连友（Lianyou Jing，副教授）、严前坤（Qiankun Yan，硕士生） |
| 基金 | NSFC 62071383 / 62471397；中央高校基本科研业务费 23GH02027；声学科学技术重点实验室稳定支持 JCKYS2024604SSJS010 |
| 页数 | 18 页（7 节 + 参考文献 41 条） |
| 刊物 | IEEE JOE, vol.50, no.2, 2025 年 4 月 |
| 实验 | 丹江口水库 2022-07，2 km 通信距离 |
| PDF 路径 | `D:/Claude/TechReq/UWAcomm/raw/papers/Delay-Doppler_Domain_Turbo_Equalization_for_Single-Carrier_Underwater_Acoustic_Communications.pdf` |

## 核心观点

1. **"SC 低 PAPR + OTFS 抗时变"的混搭是本文的中心论点** —— OTFS 虽然在 DD 域将时变信道转化为准静态信道、鲁棒性优，但它本质是**预编码的 OFDM**，PAPR 几乎与 OFDM 相当，在水声功放非线性区间工作时效率受损。作者把 DD 域均衡从调制层拉到接收机层：**发端保持单载波（SC）的低 PAPR**，只把 DD 变换作为接收机的一个处理域插入到均衡环节，等于"借 OTFS 的鲁棒性，不付 OTFS 的 PAPR 代价"。
2. **DD 域变换是"把时变看成稀疏"的线性代数重写，不改变信息本身** —— 对同一单载波信号，时域信道矩阵 `H_T = Σ h_p Π^{l_p} Δ^{κ_p}` 是稠密的时变矩阵（Π 循环移位代表时延、Δ 对角相位代表多普勒）；通过 `H_DD = (F_N ⊗ I_M) H_T (F_N^H ⊗ I_M)` 这个 Kronecker 结构的酉变换，DD 域信道矩阵变成稀疏的准静态表示。Kronecker 乘 Fourier 的结构是关键：**保留时延循环性、只对多普勒做 N 点 DFT**，比 OTFS 的 SFFT 少一层 M 点 IDFT，因此 SC 接收到 DD 的映射更紧凑。
3. **跨域软信息交互是性能的真正来源，而非 DD 变换本身** —— 消融对比（Fig. 4-5）清楚表明：首次迭代时 DD-MMSE-TEQ 仅比 FD-MMSE-TEQ 略优（差距小），但经过 3 次迭代后 DD-MMSE-TEQ 比 FD-MMSE-TEQ 高一个数量级、OSNR 增益约 2 dB，迭代增益约 4 dB。作者对此解释为：**DD 域均衡把时域连续突发错误打散到 DD 域不同位置**，使下一次迭代时时域译码器看到的是"近似独立同分布"的错误图样——Turbo 码假设错误独立，这是它工作的必要前提，DD 变换相当于为 Turbo 码**人工重建了"独立性"假设**。
4. **MMSE + 先验抵消 + Woodbury 矩阵恒等是标准 Turbo MMSE 套路，但矩阵求逆是复杂度瓶颈** —— 均衡器 `f_k^H = h_k^H Ψ^{-1}`（公式 33）需要对 `Ψ = H_DD V H_DD^H + σ I` 做一次 MN×MN 矩阵求逆，复杂度 O(K³)。作者用 Woodbury 恒等式把单符号更新降为 `β_k f_k` 的标量缩放（公式 35），但整体仍为 O(K³)——这是 SC-DD 相对 FD-DFE 的 O(K) 的根本代价。作者在结论里坦承"低复杂度处理仍是开放问题"，直接暗示这是后续工作空间。
5. **Tüchler-Koetter 2002 的"消自先验"技巧被复用到 DD 域** —— 公式 34 把 `x_DD(k) = 0, v_k = 1` 代入以消除自身先验的影响，保证外信息与先验严格独立，这是 Turbo 均衡器能收敛、不发散的必要条件。这个小细节在 DD 域同样适用，说明 DD 域 MMSE 的"消自先验"等价于时域 Tüchler 2002 的操作，没有新理论，只有域的搬迁。
6. **块长 K 的两端陷阱：太短 = 分数多普勒/时延严重、太长 = 准静态假设失效** —— Fig. 6 显示 K=1024 → 2048 时 DD-MMSE-TEQ 性能提升，但 K=4096 时性能开始下降；FD-MMSE-TEQ 则从 K=1024 起就持续恶化。这说明 DD 域有一个"甜蜜区间"：帧长足以让 `κ_p = ν_p · T_f` 接近整数（抑制 fractional Doppler leakage），但又不能长到让信道本身在帧内发生明显漂移。**这个 sweet spot 应由 Doppler 相干时间与多径时延扩展共同决定**，作者没给封闭公式，是工程调参经验。
7. **DD 域信道的天然稀疏性是性能提升的物理基础** —— Fig. 3 和 Fig. 10 清楚显示：时域信道矩阵稠密、时变复杂，而同样信道在 DD 域呈现"几个离散亮点"的稀疏模式（每个多径对应一个 (τ_p, ν_p) 坐标的 delta）。这个稀疏结构意味着 `H_DD` 大部分元素为零，矩阵求逆的实际运算量远低于 O(K³) 的理论上界——**这也是 OTFS/OSDM 社区共同的设计起点**。
8. **OSDM 与 OTFS 等价，论文接纳了 2024 年 van der Werf 的这个证明** —— 参考文献 [32] 引用了 Signal Processing 2024 年 van der Werf 等人的 "On the equivalence of OSDM and OTFS"（该论文 2024 年才在线）。作者把 OSDM-UWAC（Ebihara 2014, 2016；Han 2019）与 OTFS-UWAC 视为同一数学对象的不同命名，这是学术综述上的重要共识。DD-MMSE-TEQ 的位置因此是：**不是第四种 DD 域方案，而是"SC + DD 接收机"的第一种系统化设计**（区别于"OTFS/OSDM = DD 调制 + DD 接收"）。
9. **丹江口湖试 4.076 kbps / 2 km / 8 元垂直水听阵是国内 DD 域 UWA 通信的最高公开指标之一** —— 4 kbps 水声通信在 2 km 距离并非高速率（对比：本实验 6 kHz 带宽 / 16 kHz 载波 / QPSK / RSC 1/2 码 / 每帧 13568 符号 / 15 帧 138240 比特），但**移动通信（船速 2-4 节）+ 近水面（3-7 m）+ 浅水多径（50 m 水深）** 这三个条件叠加是非常严苛的。8 通道 2 次迭代实现 BER < 10^-4（近无错）是可靠性层面的强结果，但作者没报告单通道高速率的收敛性（即单通道 4 kbps 是否可行未验证）。
10. **作者对 FD-DFE (Benvenuto-Tomasin 2005)、FD-TEQ-IterCE (Chen-Wang-Zheng 2017)、TDDA-TEQ (Xi-Yan-Xu 2018)、TDMSER-TEQ (Xi 2021, Gong 2013) 四个 baseline 的公平对比是论文可信度的基石** —— 尤其 FD-MMSE-TEQ [19] 是 Y.R. Zheng 团队 2017 年的高质量工作，与作者"师承/同侪"关系明显（作者也多次引 Zheng）。实验中 FD-MMSE-TEQ 在静态信道下已接近 DD-MMSE-TEQ，说明 DD 域变换的增益主要在**高多普勒场景**兑现，静态场景下"过度工程化"。这界定了 DD-MMSE-TEQ 的适用边界：**船速 > 2 节 或 v_max > 2.5 Hz 多普勒** 才值得付 O(K³) 的复杂度。

## 核心贡献

| 创新点 | 解决的问题 | 性质 |
|--------|-----------|------|
| **单载波发射 + DD 域接收机 Turbo 均衡**（DD-MMSE-TEQ）| OTFS 的高 PAPR vs SC 在时变信道下的性能瓶颈 | 体制重组 |
| **Kronecker Fourier 变换写出 SC 信号的 DD 域输入-输出关系**（公式 20-27）| 以往 DD 域方法绑定 OTFS/OSDM 发送端，SC 发送+DD 接收的映射关系缺失 | 数学建模 |
| **跨域（DD ↔ 时域）软信息交互**通过酉变换实现 | Turbo 迭代时错误突发破坏码字独立性假设 | 算法设计 |
| **Woodbury 恒等降低单符号更新复杂度** | DD 域 MMSE 每符号需独立求逆 | 数值优化 |
| **丹江口湖试端到端验证**（4.076 kbps / 2 km / 8 通道 / BER < 10^-4）| 仿真与实测脱节问题 | 工程验证 |

## 主要方法

### 方法 1：DD 域信道建模（Sec III-A, III-B）

- **双色散信道连续模型**：`h(τ, ν) = Σ_p h_p δ(τ - τ_p) δ(ν - ν_p)`，P 条路径各有复增益 h_p、时延 τ_p = l_p/B、多普勒 ν_p = κ_p/T_f（整数化）
- **时域信道矩阵**：`H_T = Σ_p h_p Π^{l_p} Δ^{κ_p}`，其中 Π 是 MN×MN 前向循环移位矩阵（表时延），Δ 是 MN×MN 对角矩阵 diag(1, ω, ω², ..., ω^(MN-1)) 其中 ω = e^(j2π/MN)（表多普勒相位累积）
- **DD 域信道矩阵**：`H_DD = (F_N ⊗ I_M) H_T (F_N^H ⊗ I_M)`，通过对多普勒维度做 N 点 DFT（Kronecker 提出"只变换一半"）
- **DD 域输入-输出关系**（公式 27）：`Y_DD[m,n]` 可写为 `(m - l_p) mod M, (n - κ_p) mod N` 位置上 `X_DD` 的线性组合，多径表现为 DD 平面上的 2D 卷积+相位旋转

### 方法 2：DD 域 MMSE 均衡（Sec III-C 前半）

- **Wigner 变换**：对接收信号 r 按列重排为 M×N 矩阵 Y_T，再对每列做 M 点 DFT 得时频域 Y_TF（公式 28）
- **SFFT**：对 Y_TF 做列 IDFT + 行 DFT 得 DD 域 Y_DD（公式 29）——与标准 OTFS 接收端相同
- **MMSE 均衡器闭式解**：`f_k^H = h_k^H Ψ^{-1}`，其中 `Ψ = H_DD V H_DD^H + σ I`，V 是符号先验方差对角阵（公式 32b, 33）
- **消自先验** + Woodbury 降维：见公式 34-36
- **调制不在 DD 域**：因此均衡输出要逆变换回时域再计算 LLR（公式 37）

### 方法 3：跨域软信息交互与 Turbo 迭代（Sec III-C 后半 + Algo 1）

- **高斯近似 LLR**：假设均衡后符号 `x̂(k) ~ CN(μ_k α_i, ς_k²)`，其中 μ_k, ς_k² 由均衡器的信道条件数和先验方差决定（公式 39-43）
- **外信息 LLR**（公式 44）：对 QPSK，`Le(d_k,1) = 2√2 · [1 + (1-v_k)ξ_k] · Re{x̂(k)} / (1 - v_k ξ_k)`
- **去交织 → RSC 译码 → 后验 LLR → 减先验 → 交织 → 作为新先验**（外部环路）
- **先验更新**（公式 47-48）：`x̄(k) = Σ α_i · P(d|LLR)`，`v_k = 1 - |x̄(k)|²`，然后通过酉变换送回 DD 域（公式 49）
- **跨域关键公式**：`X_DD = F_M^H X_TF F_N = I_M X_T F_N`（先验平均从时域映射到 DD 域的同一个酉变换）
- **Algo 1 执行 I_max 次**：每次先用当前 x̄ 和 v 构造 H_DD（或复用）+ MMSE 求 x̂_DD，再逆变换、译码、更新 x̄/v

### 方法 4：仿真设置（Sec IV）

- **Qarabaqi-Stojanovic 2013 统计信道模型**：距离 5 km，载频 12 kHz，带宽 6 kHz，水深 50 m，收发机均 ~25 m 深，相对速度 10 节
- 最大时延扩展 10 ms ≈ 80 符号周期，多普勒频移 ~1.5 Hz
- RSC 1/2 + [5,7] 生成多项式 + QPSK + K=MN=1024 + 256 导频
- 对比：FD-MMSE-TEQ [19]、conventional OTFS

### 方法 5：湖试设置（Sec V-A）

- **地点**：河南丹江口水库，2022 年 7 月
- **收阵**：8 元垂直水听阵，阵元间距 0.25 m，顶阵元深约 20 m
- **发射机**：静止时深约 20 m；移动时（2-4 节）深 3-7 m
- **载频 16 kHz，采样 48 kHz，带宽 6 kHz**
- **帧结构**：138240 比特 / 15 帧，每帧 12 个数据块 + 1 个 PN 导频块，每块 768 QPSK 数据 + 256 PN，QPSK 符号共 13568
- **双段 LFM 同步**：每段 6 kHz / 0.1 s，用于粗多普勒估计与补偿
- **三个实测子实验**：DJKC1R2（静态）、DJKE1R1（移动 ~2.5 Hz 多普勒）、DJKG1R2（移动，多普勒更剧，时延扩展 ~30 ms）
- 帧长 T_f = 2.2613 s → 数据速率 R = (N_t - N_p) · R_c · log₂M / T_f = 4.076 kbps

## 关键数据 / 结果

### 仿真：DD-MMSE-TEQ vs FD-MMSE-TEQ（Fig. 4）

| SNR | 迭代次数 | FD-MMSE-TEQ BER | DD-MMSE-TEQ BER | 增益 |
|-----|---------|-----------------|-----------------|------|
| 2 dB | 3 次 | ~10^-2 | ~10^-3 | **约一个数量级** |
| 高 SNR | 3 次 | ~ | ~ | 迭代增益约 4 dB vs FD |

### 湖试 BER（三个实验 × 多通道数 × 多方法）

| 实验 | 收通道数 | DD-MMSE-TEQ (3 iter) | FD-MMSE-TEQ | TDDA/TDMSER |
|------|---------|---------------------|-------------|-------------|
| DJKC1R2（静态）| 1 | < 10^-1 | > 10^-1 | > 10^-1 |
| DJKC1R2 | 8 | < 10^-4（近无错）| 类似 | > 10^-3 |
| DJKE1R1（移动 ~2.5 Hz）| 1 | < 10^-1 | > 10^-1 | 失败 |
| DJKE1R1 | 8 | 近无错 | 次优 | 差 |
| DJKG1R2（移动重多普勒）| 8 | ~10^-4 | ~10^-3 | ~10^-1 |

### PAPR（Fig. 7b，CCDF）

- **SC < OTFS < OFDM** —— SC 显著低于另外两者，验证保留 SC 发送端的核心价值

### 复杂度（Table V）

| 方法 | 复杂度 |
|------|--------|
| TDDA-TEQ / TDMSER-TEQ | O(I_max · (L_f + L_b) · K) + tanh 额外 |
| FD-MMSE-TEQ [19] | O(3 · K · (1 + ½ log₂ K)) |
| **DD-MMSE-TEQ（本文）** | **O(I_max · K³)** —— 矩阵求逆主导 |

### 对比方法与引用关系

| 方法 | 来源 | 关键特征 |
|------|------|---------|
| TDDA-TEQ | Xi-Yan-Xu 2018, JASA | 时域直接自适应双向 Turbo |
| TDMSER-TEQ | Xi 2021 + Gong 2013 | 最小符号错误率准则，曼里亚纳海沟实测 |
| FD-MMSE-TEQ | Chen-Wang-Zheng 2017, JOE | 频域 Turbo + 迭代信道估计 + MIMO |
| Benvenuto-Tomasin 2005 | TCOM | 频域 DFE 基础公式 [12] |
| Tüchler-Singer-Koetter 2002 | TSP | MMSE 先验均衡基础公式 [39] |
| Hama-Ochiai 2024 arXiv | arXiv 2403.16453 | SC DD 域均衡独立并行工作 [36] |
| Hong-Thaj-Viterbo 2023 | Elsevier book | DD 通信教科书 [35] |
| Qarabaqi-Stojanovic 2013 | JOE | 统计信道模型 [41] |

## 对 Ohmybrain / UWAcomm 项目的启发

### 对 UWAcomm 项目的直接借鉴（技术层）

1. **"SC 发 + DD 接"的体制选择可填补 UWAcomm 的 SC-FDE 与 OTFS 之间的空白** —— 根据 UWAcomm 现有 6 体制 benchmark（记忆卡记录 SC-FDE/OFDM/SC-TDE/DSSS/OTFS 在 fd=1/5 Hz 的 BER），DD-MMSE-TEQ 应作为"第 7 体制"被系统性加入；它弥补了 SC-FDE 在高多普勒下失效（fd=5 Hz 时 50% BER）与 OTFS 高 PAPR 的两难。
2. **DD 域矩阵构造代码可直接复用 α 补偿 refinement 管线** —— UWAcomm 最近的 α 补偿改造（记忆卡 `project_uwacomm_alpha_refinement.md`，fd130f7）推广了双 LFM + 迭代 refinement，这个 refinement 的一致性与论文 Sec V-A 的"双段 LFM 粗多普勒估计 + 补偿"完全同构，说明 UWAcomm 已具备该论文实验侧的软硬件能力。
3. **"Woodbury 恒等"是 MMSE 均衡器实现的必备技巧** —— UWAcomm 的 MMSE 相关模块若尚未用 Woodbury 降维，每块符号独立求逆会造成严重性能问题；应检查 `mmse_equalizer`、`turbo_eq` 等函数是否已落实该优化。
4. **"消自先验"技巧应纳入所有 Turbo 均衡器** —— 论文公式 34 来自 Tüchler-Koetter 2002，UWAcomm 的 `turbo_equalizer` 若未做这一步，迭代会出现 Lₐ 与 Lₑ 不独立导致的早期收敛停滞或发散。
5. **SC-DD benchmark 套件的设计** —— UWAcomm 的 E2E benchmark（记忆卡 `project_uwacomm_e2e_benchmark.md`，S1 完成）可扩展一个 `run_sc_dd_mmse_teq.m`，对比 FD-MMSE-TEQ 在 fd=1/2/5 Hz 下的 BER-SNR 曲线，复现论文 Fig. 4 作为验证锚点。
6. **DD 域信道稀疏性诊断面板** —— 论文 Fig. 3/10 的"同一信道在时域稠密、DD 域稀疏"对比图是可视化 debug 的黄金模式；UWAcomm 的 P3 UI（记忆卡 `project_uwacomm_p3_ui.md`）可增加"DD 域 sparsity 诊断"tab，将时域 H(τ,t) 与 DD 域 H(τ,ν) 并排显示。
7. **K=MN sweet spot 的 benchmark sweep** —— 论文 Fig. 6 做了 K=1024/2048/4096 的对比，UWAcomm 应在仿真 runner 里做同类 sweep，给用户提供"给定 Doppler 范围 → 推荐块长"的工程参考表。
8. **数据速率评估模板** —— 论文公式 51 `R = (N_t - N_p) · R_c · log₂M / T_f` 是标准的"去除导频/码率/调制"的速率计算，UWAcomm 的 benchmark harness 应以此为标准输出字段（不只是 BER）。

### 跨项目（Hub 层）价值

9. **"低 PAPR + DD 鲁棒性"的体制重组思维可推广到 UWAnet** —— 水声组网的各节点同样受制于功放非线性，UWAnet（前期调研）未来若做节点链路设计，应优先考虑"发射端保 SC / 接收端用 DD"的思路，而非默认 OTFS。
10. **"以 Kronecker 酉变换打散错误突发"是 Turbo 迭代的通用加速器** —— 这个思路不限于水声：任何 Turbo 接收机（5G URLLC、卫星通信、深空 DSN）都面临"时域错误突发破坏独立性"的问题，DD 域变换是一种"独立性重建"手段，可与交织器、UEP（不等保护）等并列为独立的工具箱条目。
11. **"复杂度 vs 性能"的可视化论文结构值得学习** —— 论文把"O(K³) 的代价换取一个数量级的 BER 提升"摆在 Sec VI（而非隐藏在结论里）的诚实做法，是工程性投稿的标准叙事。Ohmybrain 未来的技术文档（PRD/tech_doc）可参考这个"先强调限制、再强调价值"的分段。
12. **"OSDM = OTFS"的形式等价证明（van der Werf 2024）值得作为独立知识条目收录** —— 这个证明消解了 10 年来两社区的术语对立，是 DD 域通信的"范畴论统一"；Ohmybrain wiki 应建立独立页记录（建议作为 `ofdm-and-otfs` concept 的一个小节或 entity 页）。
13. **"软信息跨域交换"的设计哲学** —— 论文的核心是"让 Turbo 码的两个模块分别活在各自最优的域里"（均衡 @DD、译码 @时域），用酉变换桥接。这是一种**"不强求统一域，而强求等距同构"**的设计哲学，可作为未来"多域信号处理"研究的范式。
14. **湖试（淡水水库）作为海试前的低成本预演** —— 丹江口实验揭示了一条 Ohmybrain 生态可借鉴的实验路线：**水库实验 → 近海实验 → 远海实验**，通过浅水+短距离模拟长时延+强多普勒，验证算法后再投入海试。适用于 UWAcomm 和 USBL 项目的未来外场实验。
15. **"作者同校同门梯队发表"的学术生态观察** —— NPU-何成兵-敬连友-郑通辉的同校导师-学生梯队，与同一团队之前的工作（参考文献 [15] Jing 2022 Applied Acoustics；[26] Jing 2022 Applied Acoustics 二维被动时反 OTFS）构成了清晰的学术积累线。对 Ohmybrain 的启示：**跟踪一个高质量团队的系列工作比跟踪单篇热点论文更有价值**，NPU 何成兵组值得作为 UWAC 的重点作者被持续追踪。

## 相关概念

- [[channel-estimation-and-equalization]] — 本论文是 SC 体制下 Turbo 均衡器的最新代表作，公式 31-36 的 MMSE + 先验 + Woodbury 是标准 Turbo 均衡器设计流程在 DD 域的搬迁
- [[ofdm-and-otfs]] — 论文明确把 DD-MMSE-TEQ 与 OTFS/OSDM 做并列对比，并引入 van der Werf 2024 "OSDM = OTFS" 的等价证明
- [[time-varying-channel]] — 双色散信道的 DD 域稀疏化是本论文性能增益的物理基础
- [[underwater-acoustic-communication]] — 4.076 kbps / 2 km / 8 通道 丹江口实验是该体制的首次公开实测验证
- [[message-passing-algorithms]] — Turbo 迭代的"外信息交换"与消息传递在因子图上的本质一致；论文是 MMSE-Turbo 范式的 DD 域实例
- [[mathematical-optimization]] — Woodbury 恒等用于降低矩阵求逆复杂度，拉格朗日乘子 + MMSE 准则是传统 Turbo 均衡的核心优化工具

## 相关资料

- UWAcomm 现有 6 体制 benchmark：记忆卡 `project_uwacomm_e2e_benchmark.md`（S1 完成 7 工具 + 11 runner）
- UWAcomm α 补偿 refinement：记忆卡 `project_uwacomm_alpha_refinement.md`（双 LFM + 迭代 refinement + 4 体制推广 + DSSS Sun-2020，fd130f7）
- UWAcomm P3 UI 重构：记忆卡 `project_uwacomm_p3_ui.md`（深色科技风 + 通信声纳主题，SC-FDE 未收敛待排查）
- UWAcomm 项目跳过 OTFS 的记忆：`feedback_uwacomm_skip_otfs.md`（SC-DD 体制不受此影响，可独立评估）
- 相关水声通信 UWAC 论文（待摄入）：Jing 2022 AA（2D 被动时反 OTFS）、Han 2019 JOE（OSDM 逐矢量均衡）、Chen-Wang-Zheng 2017 JOE（FD-MMSE-TEQ，本文主 baseline）
- 综述性教材：Hong-Thaj-Viterbo (2023) *Delay-Doppler Communications: Principles and Applications*（Elsevier，值得系统性摄入作为 DD 域通信的基础知识锚点）
