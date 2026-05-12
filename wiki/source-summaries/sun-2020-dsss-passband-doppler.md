---
type: source-summary
created: 2026-04-22
updated: 2026-04-22
tags: [水声通信, DSSS, 扩频, 多普勒跟踪, 通带处理, 符号级, 三点余弦插值, 时延估计, 哈工程, CAF, DBPSK]
source_type: paper
source_path: D:/Claude/TechReq/UWAcomm/raw/papers/A_Symbol-Based_Passband_Doppler_Tracking_and_Compensation_Algorithm_for_Underwater_Acoustic_DSSS_Communications.pdf
source_project: UWAcomm
---

# 符号级通带多普勒跟踪与补偿算法（DSSS 水声通信）

> **引用**：Sun D J, Hong X P, Cui H Y, Liu L (2020). *A Symbol-Based Passband Doppler Tracking and Compensation Algorithm for Underwater Acoustic DSSS Communications*. **Journal of Communications and Information Networks**, 5(2): 167-176.
>
> **机构**：哈尔滨工程大学 水声工程学院 / 声学科学与技术实验室 / 海洋信息获取与安全工信部重点实验室
>
> **项目源路径（UWAcomm 项目内）**：`D:/Claude/TechReq/UWAcomm/raw/papers/A_Symbol-Based_Passband_Doppler_Tracking_and_Compensation_Algorithm_for_Underwater_Acoustic_DSSS_Communications.pdf`

## 来源信息

| 项 | 值 |
|-----|-----|
| 第一作者 | 孙大军（Sun Dajun），哈工程水声教授、声呐系统专家 |
| 通讯作者 | 崔宏宇（Cui Hongyu） |
| 共同作者 | Hong Xiaoping（博士生）、Liu Lu（博士后） |
| 发表 | 2020 年 6 月 |
| 期刊 | JCIN（Journal of Communications and Information Networks），通信与信息网络期刊 |
| 页数 | 10 页（Page 167-176） |
| 资助 | NSFC 61701132 / 61601134 / 黑龙江 NSF YQ2019D003 / CSC 201906680039 |
| 章节结构 | I 引言 / II 系统模型（DSSS+时变信道+通带相关） / III 提出算法（同步-时延估计-Doppler估计-解调补偿-参考信号生成-复杂度） / IV 仿真 / V 结论 |
| 体量 | 17 条参考文献，涵盖 CAF / DFE+PLL / 闭锁环 / 宽带补偿 / MBA / CW pilot / 亚采样时延估计等主要路线 |

## 核心观点（Hub 视角）

1. **水声 DSSS 的多普勒问题与窄带无线根本不同** —— UWA 声速仅 1500 m/s，多普勒效应不只是频移 `Δfc = -v/c · fc`，更是信号的时间伸缩 `ΔT = (v/(c-v))·NTb`；DSSS 符号长（秒量级长包），一包内 `α=v/c` 漂移足以让符号边界滑动数个采样点 → 必须把"多普勒"视作**时间伸缩参数**而非单纯频偏，这是跨 DSSS/OFDM/OTFS 所有水声体制共用的物理前提。
2. **符号级跟踪 > 块级估计（对长时 DSSS）** —— 经典做法（Diamant 2012 包头/包尾时差 / Mason 2008 双相同符号频域估计）假定 α 在整个 packet 内近似恒定，对秒级 DSSS 失效；本文把 α 估计细化到每符号粒度，提供动态跟踪能力。这对 UWAcomm 项目的 DSSS 体制改造是直接落地的工程范式。
3. **"通带相关 + 三点余弦插值"是亚采样时延估计的经济解** —— 同 Yu Min 2006 在 LR-USBL 用的 Cespedes 1995 三点抛物线插值血脉相承，但本文用**余弦近似**（因为通带相关峰携带 cosine 调制项 `cos(2π fc τ)`），更贴合信号结构；对采样率 100 kHz 的系统，分辨率可达 1/4 采样（约 2.5 μs），对应速度分辨 0.25 m/s @ 20 dB Es/N0。
4. **通带时延估计精度 > 基带** —— 通带相关输出自带载波 cosine 调制，峰附近曲率由 `fc` 主导（kHz 量级），插值拟合对噪声更抗；基带包络曲率由**等效基带带宽**（chip rate 2500 cps）主导，曲率平缓容易偏。论文图 4 直接对比：通带 2.5 μs vs 基带 20 μs @ 20 dB。这是一个"把 fc 当作测量标尺"的巧思，有信号处理基础层的普适价值。
5. **与符号判决解耦，避免错误传播** —— 与 Johnson 1997 DFE+PLL、Sharif 2000 闭锁环、Singer 2011/2012 宽带迭代方法不同，本文的 Doppler 估计**不依赖已判决的信息符号**（`|ℜ{Rn(τ)}|` 消去 `b(k)` 的调制），因此对解码错误免疫；这是与决策反馈路线最根本的分界。
6. **本地参考信号库的自适应选择** —— 提前生成 K 个带不同 `α̃` 的 dopplerized 参考序列存内存，用一阶低通滤波后的 ᾱn 做离散选择（非连续重采样），工程实现代价低；论文提供"图 2 magnitude-vs-velocity-vs-L 曲线"作为 K 与步长设计的依据（L 越长，α 容忍度越窄）。这对 FPGA / DSP 硬件落地非常友好。
7. **计算复杂度低于 CAF** —— CAF 方法要并行 K 路带不同多普勒因子的相关器，复杂度 `O(2K·m·lb m)`；本文只需一路相关 + 延迟估计器，复杂度 `O(2·m·lb m)`，K 可以很大而本算法几乎不受影响。CAF 退化为"粗同步阶段 one-shot"，不再吃瞬时算力。
8. **BER 仿真：3 dB 性能损失 vs ideal DBPSK** —— 相对 AWGN 理想 DBPSK（无 Doppler），本算法损失约 3 dB；相对"跟踪但不做相位补偿"又再低 2 dB（即相位旋转补偿值 2 dB）；相对传统固定参考+无跟踪的方案，**高 SNR 也有 error floor** → 跟踪+补偿是远距/高速场景的必需品。
9. **与 Zakharov 2019 MBA 叠加导频路线互补** —— 叠加导频方式（superimposed pilot + MBA）本身因自相关运算损 SNR，但不占有效带宽；本文方法占用通带相关算力但不损 SNR。两者可组合（如叠加导频做初始化，本文做精细跟踪）。
10. **论文把"先验多普勒限"写进算法** —— 给定 AUV 平台最大速度 → 先验 α 范围 → 缩窄 `fτ∆τ < π/2` 的搜索窗口 → 提高分辨率。这是把**物理先验注入估计器**的典型案例，对其他基于迭代/搜索的水声参数估计（时延、信道稀疏度）同样可借鉴。

## 核心贡献

| 创新点 | 解决的问题 | 性质 |
|--------|-----------|------|
| 通带相关 + 三点余弦插值的符号级 α 估计 | 块估计法对长时 DSSS 不适用、基带时延估计精度受限 | 信号处理（核心算法） |
| 判决无关的 Doppler 估计（ℜ{Rn} 消 b(k)） | DFE+PLL / 闭锁环 / 宽带迭代的错误传播与星座模糊 | 接收机架构 |
| 本地参考信号库 + 一阶低通 + 自适应选择 | Doppler 变化导致相关幅度下降及 SNR 损失 | 工程实现 |
| 计算复杂度低于 CAF,用 CAF 仅做粗同步 | 动态 Doppler 跟踪的算力可接受性 | 系统复杂度 |
| 先验 Doppler 限细化搜索窗口 | `f τ∆τ < π/2` 相位不模糊条件下的分辨率-范围权衡 | 估计器约束 |

## 主要方法（Hub 抽象层）

### 系统模型（II）

- **DSSS-DBPSK**:`bn = an·bn-1`;`s(t) = Σ b[n]·Σ c[m]·g(t-nTb-mTc)·ej2πfct`; spread sequence 长度 L（实验 L=31 m-sequence）
- **时变信道**:`r(t) = s(t - d(t)/c) + n(t)`;`d(t) = d0 + v0·t + 1/2·a·t²`（恒加速度,论文简化）;推广式:`r(t) = Σ b[n]·Σ c[m]·g((1-v0/c)t - nTb - mTc)·ej2πfc(1-v0/c)t + n(t)`
- **通带相关输出**（核心观测方程）:`Rnr(τ) = b[n]·Rc((1-αn)τ - nTb)·ej2π(1-αn)fc·τ + ω(τ)`;其中 `αn = vn/c`,符号内 α 视为常值

### Step 1：同步与粗 Doppler（III-A）

- CAF 法粗估 α：存储 K 个不同 α̃ 的通带参考，平行相关
- 步长由 L 决定：图 2 给出 L={31, 63, 127} 时 magnitude-vs-velocity 曲线
- 实验场景：L=31，步长 1.2 m/s，速度范围 ±6 m/s → K=11，最大 magnitude loss < 0.5 dB

### Step 2：通带相关（III-A 末）

- 接收两符号窗 `r_n(t), r_{n+1}(t)` 与当前参考 `s̃αn(t)` 做通带 cross-correlation
- 输出 `Rn(τ) ≈ Σ b(k)·Rc(τ-τk)·ej2πfc(1+αk-α̃n)(τ-τk)`（k=n, n+1）

### Step 3：三点余弦插值（III-B）

- 在相关峰附近取 3 个样点 `y₋₁, y₀, y₊₁`
- 模型 `R(τ) ≈ A·cos(2π fc τ)`，用 LS 拟合
- 求 `dR/dτ = 0` → fractional τ
- 要求 `|fc Δτ| < π/2` 以避免相位模糊

### Step 4：Doppler 估计（III-B 末）

- 第 n 和 n+1 符号的时延估计：`τ̃n = fTD(|ℜ{Rn(τ)}|, τ̂n, Δτ)`,`τ̃n+1 = fTD(|ℜ{Rn(τ)}|, τ̃n + (1+α̃n)Tb, Δτ)`
- 瞬时 Doppler：`α̂n+1 = Tb / (τ̃n+1 - τ̃n) - 1`
- 用 `|ℜ{·}|` 去除 `b(k)` 调制 → 判决无关

### Step 5：解调 + 相位补偿（III-C）

- 等效基带 `bn(τ) = Σ b(k)·Rc(τ-kTb)·ej2πfc(αk-α̃n)(τ-τk)`
- 差分符号：`[b̂n, b̂n+1] = [bn(τ̂n), bn(τ̂n+1)]`
- 信息符号：`ân = b̂n+1·b̂n*·e^(-jφn)`,其中 `φn = 2π(1+α̃n)fc(α̂n+1 - α̃n)Tb` 是残余相位旋转

### Step 6：本地参考更新（III-D）

- 一阶 LPF 平滑：`ᾱn = β·α̂n + (1-β)·ᾱn-1`（论文 β=0.6）
- 选择函数：从 K 个存储参考中选与 ᾱn 最近的 α̃n
- 目的：既抑瞬时噪声又避免参考突变

### 复杂度对比（III-E）

| 步骤 | 本文 | CAF |
|------|------|-----|
| 相关 | O(2·m·lb m) | O(2K·m·lb m) |
| 解调 | O(2·m·lb n) | O(2·m·lb n) |
| 时延估计 | O(2·1.5 m) | — |
| Doppler 估计 | O(1) | — |
| 符号判决 | O(1) | O(2·1.5 m) |
| 参考信号生成 | O(1.5 K) | — |

核心收益：避免 CAF 的 K 路并行相关。

## 关键数据 / 结果（IV）

### 仿真参数

| 参数 | 值 | 备注 |
|------|-----|------|
| 载波 fc | 12.5 kHz | 典型 UWA 带 |
| chip rate | 2500 cps | 对应 Tc = 400 μs |
| 采样率 fs | 100 kHz | 40 samples/chip |
| spread seq 长度 L | 31（m-sequence） | 对应 Tb = 12.4 ms |
| 传输符号数 N | 300 | packet 时长 ~3.7 s |
| 声速 c | 1500 m/s | 标准 |
| 初始速度 v0 | 0 m/s | transmitter 从静止起 |
| 加速度 a | 1.95 m/s² | 运动场景 |
| 初始距离 d0 | 100 m | |
| 本地参考数 K | 11 | ±6 m/s / 1.2 m/s |
| LPF 系数 β | 0.6 | |

### 主要性能结果

| 指标 | 本文（通带） | 基带方法 | CAF 方法 |
|------|------------|---------|---------|
| 时延估计误差 @ 20 dB | < 2.5 μs（1/4 采样） | > 20 μs（2 采样） | — |
| 时延估计误差 @ 40 dB | ~0.5 μs | ~5 μs | — |
| 速度估计误差 @ 20 dB | ~0.25 m/s | ~2 m/s | ~0.6 m/s |
| 速度估计误差 @ 40 dB | ~0.02 m/s | ~0.5 m/s | ~0.1 m/s |
| BER vs ideal DBPSK | 3 dB 损失 | — | 5 dB 损失（无相位补偿） |
| 传统无跟踪方法 | — | — | 高 SNR error floor（不收敛） |

### 关键可视化

- **Figure 1**：接收机结构框图（同步+粗 α → 通带相关 → 两符号时延 → α 估计 → LPF → 本地参考选择 → 解调 → 相位补偿 → 符号判决）
- **Figure 2**：magnitude loss vs velocity bias vs spread 序列长度（L=31/63/127），告诉你 K 和步长怎么设
- **Figure 3**：power-delay-profile 时变演化（a）固定参考 vs（b）自适应参考 → 后者相关峰能量稳定，前者随时间衰减
- **Figure 4**：时延估计误差 vs Es/N0（通带 vs 基带）
- **Figure 5**：速度估计误差 vs Es/N0（通带 vs 基带 vs CAF）
- **Figure 6**：BER vs Es/N0（传统 / 仅跟踪不补偿 / CAF / 本文跟踪+补偿 / ideal DBPSK）

## 对 UWAcomm 项目的直接借鉴（2026-04-22 α 补偿改造背景）

1. **符号级 α 跟踪可作为 DSSS 体制的 Doppler 补偿默认方案** —— 项目 2026-04-22 的"α 补偿改造"已落地双 LFM 帧头估计 + 2 次迭代 refinement,但主要服务 SC-FDE;DSSS 通道目前是 Sun 2020 的目标改造对象（UWAcomm MEMORY 提到"DSSS Sun-2020"）。本文提供的**通带相关 + 三点余弦插值**可直接映射到项目的 `modules/10_DopplerProc/` 双 LFM 框架之下作为"每符号 refinement"的替代后端。
2. **"每符号更新 α"是双 LFM 2 次迭代的连续化版本** —— 项目双 LFM 的 refinement 次数有限（2 次）;Sun 2020 相当于把 refinement 颗粒度做到**每符号一次**,适合长时 DSSS packet。两者可并存:双 LFM 做粗估/帧级初始化（对应 Sun 2020 的 CAF 粗同步步骤）,本文算法做符号级精跟踪。
3. **通带相关的亚采样分辨率是"公共 tooling"** —— UWAcomm 的同步（模块 08）、信道时延估计（模块 07）也可受益于"通带相关 + 余弦插值",不必局限于 Doppler 通道。
4. **图 2 的 magnitude-vs-velocity-vs-L 曲线可直接纳入系统设计指南** —— 项目规划 DSSS 本地参考库大小时,直接引用本图给出 step size 与 K 的设计原则。
5. **判决无关估计这一架构哲学** —— 项目 `modules/10_DopplerProc/α补偿pipeline诊断.md` 中观察到的 SC-FDE 与 DSSS pipeline 不对称问题（MEMORY 记录）,很大一部分根源是 DSSS 缺乏"判决无关估计器"。引入 Sun 2020 范式后可降低 DSSS 通道对发射符号的耦合。
6. **LFM 帧头 + 符号级 α 跟踪 + 本地参考库**三件套可沉淀为项目跨体制的"Doppler 补偿中间件" —— SC-FDE、DSSS、OFDM 都能复用同一套 α 跟踪子系统,只在**符号定义与参考信号**上差异化。

## 跨项目（Hub 层）价值

7. **"通带时延估计优于基带"这一结论对 USBL 同样成立** —— USBL 项目 wiki 的 `yumin-2006-lr-usbl` 已将三点插值（Cespedes 1995）纳入工具箱;Sun 2020 把它从"抛物线"升级为"余弦"以匹配通带信号结构,对长程 USBL 通带时延估计是可直接借鉴的小升级。
8. **"窄带相位跟踪 + 宽带时延锚定"范式的 DSSS 版本** —— Yu Min 2006 LR-USBL 的窄带 CW + 宽带 LFM 双模,等价于本文"CAF 粗同步（宽带 LFM 式定位） + 通带相关符号级 α 跟踪（窄带 CW 式细跟踪）"的现代 DSSS 版本。两种范式共享同一物理直觉:宽带锚定绝对参考,窄带跟踪相对动态。
9. **"判决无关 + 本地参考库自适应"是水声估计器的通用设计哲学** —— 可推广到:UWAnet 组网的邻居节点 Doppler 跟踪、USBL 阵列校准中的非决策参数估计、水声导航中 DVL/USBL 组合时的速度跟踪。核心是:**估计的量不能依赖下游判决结果**,否则错误传播毁掉算法。
10. **"物理先验注入估计器"的工程范式** —— 本文把"AUV 最大速度"这一物理先验直接写进 α 搜索范围和相位不模糊条件,这类做法在 USBL 声线跟踪、UWAnet MAC 碰撞避免中都有直接对应。Hub 层可以把它升华为一条通用原则:**先验不只是正则化,它是工程约束**。
11. **"CAF 退化为粗同步"是算法复杂度降阶的典型手法** —— CAF 本身是计算密集型多普勒估计,但一旦有了后续的符号级精估器,CAF 只需 one-shot 完成"初始化"。这种"粗估器+精估器"两段式设计广泛适用于时延估计、信道估计、DOA 估计等场景。USBL 项目的迭代 LS / M 估计校准链也是同一哲学的实例。
12. **哈工程水声团队的"工程落地导向"研究范式** —— 和 Yu Min 2006 LR-USBL、丁杰 2020 紧凑阵、杨保国 2013 校准一样,本文从符号级结构化问题（多普勒伸缩）→ 工程约束（算力、FPGA 可行性）→ 物理先验（v_max）→ 仿真验证的完整链条是哈工程水声系列论文的共同叙事结构。Ohmybrain 的 UWAcomm / USBL / UWAnet 三项目可共享这一叙事模板。

## 相关概念

- [[underwater-acoustic-communication]] — 水声通信核心主干,本文是 DSSS 体制 Doppler 补偿的代表性工作
- [[time-varying-channel]] — 水声时变信道下"时间伸缩 α"而非单纯"频移"的建模与跟踪,本文是符号级跟踪的代表
- [[channel-estimation-and-equalization]] — 虽然本文聚焦 Doppler 而非信道,但"判决无关估计"的哲学直接适用于信道估计中避免决策反馈错误传播
- [[signal-processing-fundamentals]] — 通带相关 + 三点余弦插值、亚采样时延估计、一阶 LPF 平滑等是信号处理基础方法的典型集成;论文引用 Cespedes 1995 抛物线插值的升级形态
- [[mathematical-optimization]] — 最小二乘拟合三点余弦模型、先验约束下的分辨率-范围权衡是估计理论的经典问题
- [[usbl-positioning]] — 与 [[yumin-2006-lr-usbl]] 的"窄带+宽带双模"定位范式共享同样的物理直觉（本文 DSSS 版本 = 宽带 CAF 粗估 + 通带符号级精跟踪）

## 相关资料

- UWAcomm 项目对应摘要（项目视角）：`D:/Claude/TechReq/UWAcomm/wiki/source-summaries/sun-2020-dsss-passband-doppler-tracking.md` — 含项目模块映射、实装路径、与双 LFM 的合成
- UWAcomm 项目 α 补偿改造记录：`D:/Claude/TechReq/UWAcomm/wiki/modules/10_DopplerProc/双LFM-α估计器.md` / `α补偿pipeline诊断.md` / `大α-pipeline-不对称诊断.md`
- 同期水声 Doppler 相关工作：Zakharov 2019 MBA 叠加导频 / Sharif 2000 闭锁环 / Singer 2011/2012 宽带迭代 / Diamant 2012 信号选择
- 同项目 LFM-FPGA 参考：`D:/Claude/TechReq/UWAcomm/wiki/source-summaries/lalevee-2025-dichotomic-doppler-fpga.md` / `muzzammil-2019-cpofdm-doppler-interp.md`
- Hub 同系列哈工程水声论文：[[yumin-2006-lr-usbl]]（LR-USBL 通带 LFM + 窄带 CW + 三点插值的祖型）、[[dingjie-2020-compact-usbl]]、[[yangbaoguo-2013-usbl-calibration]]、[[zhengcuie-usbl-docking]]、[[guoyu-2024-lie-group-nav]]
