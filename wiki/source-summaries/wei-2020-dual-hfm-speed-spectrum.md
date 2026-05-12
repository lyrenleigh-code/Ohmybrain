---
type: source-summary
created: 2026-04-22
updated: 2026-04-22
tags: [水声通信, 多普勒估计, HFM信号, 速度谱扫描, 频域算法, 高精度估计, IEEE_SPL]
source_type: paper
source_path: D:/Claude/TechReq/UWAcomm/raw/papers/Doppler_Estimation_Based_on_Dual-HFM_Signal_and_Speed_Spectrum_Scanning.pdf
source_project: UWAcomm
---

# Doppler Estimation Based on Dual-HFM Signal and Speed Spectrum Scanning

> **引用**：Wei, R., Ma, X., Zhao, S., & Yan, S. (2020). Doppler Estimation Based on Dual-HFM Signal and Speed Spectrum Scanning. *IEEE Signal Processing Letters*, 27, 1740-1744. DOI: 10.1109/LSP.2020.3020222
>
> **通讯作者**：Xiaochuan Ma（maxc@mail.ioa.ac.cn）
>
> **实验场景**：Thousand Island Lake（千岛湖）, China, March 2018；换能器水下 3 m + 两浮标水听器 1.5 m；运动平台 2.15 m/s。

## 来源信息

| 项 | 值 |
|----|----|
| 作者 | Runyu Wei（魏润宇）/ Xiaochuan Ma（马晓川）/ Shiduo Zhao（赵世铎，学生会员）/ Shefeng Yan（颜世峰，高级会员） |
| 机构 | 中科院声学所（IACAS）水下机器人信息技术重点实验室 + 中国科学院大学 |
| 期刊 | IEEE Signal Processing Letters, Vol. 27（SCI Q2, IF≈3.2）|
| 资助 | 国家自然科学基金 61725106（杰青）+ 中国科学院青年创新促进会 |
| 页数 | 5 页（一般 IEEE SPL 快报，篇幅受限但推导完整）|
| 接收日期 | 2020-06-11，修订 2020-08-02，发表 2020-08-28 |

## 核心观点

1. **"Doppler invariance + 频谱关系"是 HFM 测速的两块基石** —— HFM 信号在尺度伸缩 k = c/(c+v) 下可近似为"时移 + 相位旋转" `s(kt) ≈ s(t-ε(k))·exp(jϑ(k))`（Eq.4）；再结合 HFM 频谱关系 `S(T,f) ≈ C(T)·(1/f)·exp(...)`（Eq.5），就能通过 **频谱-时移对偶** 把速度信息嵌入 `|X(f)|²` 中的周期分量。这两条性质是后续所有频域 HFM 多普勒估计方法的起点。
2. **采样率不是估计精度的硬上限——频域扫描可突破时域分辨率** —— 传统双 HFM 时延差法的速度分辨率 `ε_v = c/(T+T_e+2f₀/M) · 1/fs` 被采样频率 `fs` 限制，因为 IFFT 输出时域是离散的。而 **速度谱扫描 Y(v) = ∫ U(f)·exp(j2πf(c₁v+c₂))df**（Eq.21）本质是"在一维连续速度轴上做 IDFT"，分辨率只受扫描步长限制。这等于把"快速但粗糙的 IFFT 粗搜"升级为"连续精细的 1D 扫描"。
3. **U(f) 是去模板化的纯周期信号** —— 统计量 `U(f) = f⁴|X(f)|²/(S(f))²`（Eq.14）中 `f⁴|S(f)|⁴ = C⁴` 是与 `f` 无关的常数，所以 U(f) 剥离了 HFM 模板响应，只留下三项：两个确定性差分 HFM 项 + 一个**与速度相关的单周期复指数项**（Eq.15）。这是论文最精巧的数学动作——它把"在匹配滤波峰值里找时延"转化为"在频域找周期"，而频域周期的相位比时域峰位更精细。
4. **参数选型不是随意——`Te > 0` 与 `Tseg > 2(2T+Te)` 是推导结果** —— 两个不等式（Eq.18/19）保证两个差分 HFM 干扰项不遮蔽真正的速度周期分量。Te>0 要求双 HFM 之间**必须**有间隔（不能紧贴），Tseg>2(2T+Te) 要求 FFT 前必须 zero-padding 到信号长度的 **两倍以上**。这是"理论推导约束工程参数"的教科书范例，不是经验值。
5. **速度谱扫描成本：粗搜（IFFT）+ 精搜（1D scan）分阶段** —— 论文明示 "a practicable procedure is to use IFFT for a rough search first, and then use spectrum scanning for high-precision search"。全局 1D 连续扫描代价高，但"先 IFFT 粗搜 → 围绕峰值做窄范围扫描"把复杂度降到 O(N log N + 窄扫步数)，仍然实时可用。这也是 UWAcomm 项目 `est_alpha_dual_hfm_vss.m` 的实现范式（粗步 dv=0.5 + 精步 dv=0.02）。
6. **千岛湖海试实际差距仅 ~0.04 m/s** —— 估计 `v̂ = -2.092 m/s`，GPS 真值 `v = -2.13 m/s`，误差 ~1.8%。在 60 帧连续数据上，RMSE 相比传统 matched-filter 法和 CPM 法有进一步下降（Table I + Fig.5）。**海试而非仅仿真**，可信度高。
7. **HFM 的 Doppler 不变性是"近似"而非严格** —— Rect(t/T) vs Rect(kt/T) 在大多普勒或窄带时不可忽略；Murray 2019（参考文献 [15]）提出"扩展 HFM 匹配滤波器"纠正此偏差。UWAcomm 项目做 α 迭代 refinement 时也观察到单次 HFM estimator 在 α≈±1.7e-2 下有 1-5% 相对误差，与此理论偏差性质一致。
8. **本文方法适用于"双 HFM 作为 preamble"的帧结构** —— UMD-HFM（Up-Mute-Down-HFM）前导是方法的前提条件。纯 LFM 方案需要改造（LFM 没有 Doppler 不变性，相似推导不直接成立）。这也解释了为什么 UWAcomm 项目在 2026-04-22 把双 LFM estimator 推广为双 HFM + 速度谱时需要专门的 spec（`2026-04-21-hfm-velocity-spectrum-refinement.md`）。

## 核心贡献

| 创新点 | 解决的问题 | 技术性质 |
|--------|-----------|---------|
| 速度谱函数 Y(v)（Eq.21）— 1D 连续速度扫描取代 IFFT 时域峰位搜索 | 时域时延差法的 ε_v 被 fs 限制 | 算法创新 |
| 统计量 U(f) = f⁴·\|X(f)\|²/(S(f))²（Eq.14）— 剥离 HFM 模板，提取速度周期项 | \|X(f)\|² 中的 HFM 频谱占主导，直接 FFT 无法分辨速度 | 数学构造 |
| 参数选型不等式（Eq.18-19）— Te>0 + Tseg>2(2T+Te) | 差分 HFM 干扰项遮蔽速度周期 | 理论约束 |
| 粗搜（IFFT）+ 精搜（1D scan）的分阶段搜索 | 全局连续扫描成本过高 | 工程优化 |
| 千岛湖海试 60 帧验证，RMSE 优于传统方法 | 海试而非仅仿真 | 实验验证 |

## 主要方法

### 步骤 1：HFM 信号的两条关键性质（§II）

**Doppler 不变性**（Eq.4）：

$$s(kt) \approx s(t - \varepsilon(k)) \cdot \exp(j\vartheta(k))$$

其中 $\varepsilon(k) = \frac{f_0}{M}(\frac{1}{k}-1)$, $\vartheta(k) = -2\pi \frac{f_0^2}{M} \ln k$。尺度伸缩 ≈ 时移 + 相位。

**频谱关系**（Eq.5，在 (f_l, f_h) 内近似有效）：

$$S(T, f) = C(T) \cdot \frac{1}{f} \cdot \exp\left(j2\pi \frac{f_0}{M}(f_0 \ln f - f + \varphi(T))\right)$$

由 Parseval 定理和 Fourier 导数性质可得"频谱伸缩 ↔ 时域导数"对偶（Eq.6）。

### 步骤 2：统计量 U(f) 的构造（§III Eq.14）

接收信号 $x(t) = A \cdot s_t(k(t-\tau))$，其 `|X(f)|²` 频谱含三项：HFM 模板响应项 + 与速度相关的周期项 + 共轭项（Eq.13）。

定义 `U(f) = f⁴·|X(f)|²·(S(f))²`（paper 原式；实际实现惯用 `U = f⁴·|X|²/S²`）。

利用 $f \cdot S(f) = C \cdot \exp(...)$（Eq.5 整理），`f⁴|S(f)|⁴ = C⁴` 与 f 无关，于是 U(f) 化简为（Eq.15）：
- 第 1 项：`2C²·(f·S(f))²` — 差分 HFM 确定性分量
- 第 2 项：`(f·S(f))⁴·exp(j2πf·Δτ)·exp(-j2ϑ(k))` — **含速度信息的周期项**（Δτ = τ₂-τ₁）
- 第 3 项：`C⁴·exp(-j2πf·Δτ)·exp(j2ϑ(k))` — 共轭周期项

### 步骤 3：速度谱扫描（§III Eq.21）

定义速度谱函数：

$$Y(v) = \int_f U(f) \cdot \exp(j2\pi f (c_1 v + c_2)) \, df$$

其中 $c_1 = \frac{(T+T_e)+2f_0/M}{c}$, $c_2 = T+T_e$（常数）。

估计：$\hat{v} = \arg\max_{v \in (v_1, v_2)} |Y(v)|$（Eq.22）

### 步骤 4：参数选型约束（§III Eq.18-19）

- `Te > 0`：发射双 HFM 之间留间隔（否则两个差分 HFM 重叠）
- `Tseg > 2(2T + Te)`：FFT 前 zero-padding 到信号长度 2 倍以上（否则差分 HFM 遮蔽速度周期项）

### 步骤 5：实施流程（算法框图）

```
rx signal
  ├→ matched filter → 粗定位双 HFM 帧
  ├→ 截取含双 HFM 的信号段 + zero-pad 到 Tseg
  ├→ FFT → X(f)
  ├→ 计算 S(f) = FFT(down-HFM template, zero-padded to N)
  ├→ 构造 U(f) = f⁴·|X(f)|²/(S(f))²，只保留 f ∈ (f_l, f_h)
  ├→ 粗搜（IFFT on U）→ 粗估 Δτ
  ├→ 精搜（Y(v) 1D scan, v ∈ v_range, step = dv_fine）→ v̂ = argmax |Y(v)|
  └→ α̂ = -v̂/c（转通信链路的 α 惯例）
```

## 关键结果

### 仿真（§IV Fig.2）

- 参数：`f_l=4 kHz, f_h=8 kHz, T=Te=25 ms, fs=50 kHz, v=2 m/s, c=1500 m/s, Tseg=300 ms`
- 无噪下 IFFT(U(f)) 峰值精确落在 Δτ ≈ T+Te，两个差分 HFM 干扰项分别落在 (-T, T) 和 (-2T-Δτ, 2T-Δτ) → 验证 Eq.16 推导正确

### 海试（§IV Fig.3-5, Table I）

- 地点：千岛湖，2018-03
- 配置：换能器 3 m 深 + 两浮标（水听器 1.5 m 深），GPS 参考；运动速度 2.15 m/s
- 信号：`f_l=10 kHz, f_h=15 kHz, T=Te=25.6 ms, fs=80 kHz`，每 2 s 一帧
- 单帧结果（Fig.4c）：`v̂ = -2.092 m/s`，真值 `v = -2.13 m/s`，误差 ~0.04 m/s
- 60 帧 RMSE（Table I）：**本文方法 < CPM 方法 < 传统 matched-filter 方法**

### 性能优势来源

1. **参数选型准则降低差分 HFM 干扰**（peak detection 更干净）
2. **速度谱扫描突破 `ε_v = c/(T+Te+2f₀/M)/fs` 采样率极限**（连续估计）

## 对 Ohmybrain / UWAcomm 的启发（双层）

### 对 UWAcomm 项目的直接借鉴（技术层，与 2026-04-22 α 补偿改造强相关）

1. **速度谱扫描方法已在 UWAcomm 落地** —— `modules/10_DopplerProc/src/Matlab/est_alpha_dual_hfm_vss.m`（2026-04-21 实现）严格按本文 Eq.14/21 推导；该函数是 UWAcomm 高精度多普勒估计的核心新增，`spec = 2026-04-21-hfm-velocity-spectrum-refinement.md`。
2. **与现有"双 LFM + 时延差 + 迭代 refinement"的性能对比是当前项目的首要 benchmark** —— UWAcomm 2026-04-20 已实现 `est_alpha_dual_chirp.m`（双 LFM + 时延差 + 三点插值）并完成 A2 α=5e-4 BER 48.7%→0% 的验证；2026-04-22 又在此基础上增加 `est_alpha_dual_hfm_iter.m`（通带 resample + 残余估计 + 自适应早停 + 阻尼）。本文的速度谱方法是**频域替代方案**，应做正面对比：
   - **时延差法**：轻量（FFT 2 次 + 峰位搜索），但精度被 fs 限制
   - **速度谱扫描**：重（粗搜 + 精搜扫描），但精度不受 fs 限制
   - **迭代 refinement**：以时延差单次估计为基 + resample 累积，精度收敛到 HFM estimator 的底噪 ~5e-5
3. **UWAcomm 当前迭代 refinement 的"震荡"问题可能来自 HFM 不变性的近似偏差** —— 本文 §II 末尾明确 Rect(kt/T) 近似在大 v 时不成立，Murray 2019 扩展 HFM 匹配滤波器纠正此偏差。UWAcomm 当前在 α≈±1.7e-2 下单次 estimator 相对误差 1-5%，迭代震荡可能与此近似误差在 resample 后反复累积有关。**可尝试的改进方向**：引入 Murray 扩展 HFM 模板、或切换到本文的速度谱方法（不依赖时延差的离散性）。
4. **Te>0 + Tseg>2(2T+Te) 参数选型约束需写入 UWAcomm sync 模块文档** —— `modules/08_Sync/sync_dual_hfm.m` 和 `gen_hfm.m` 当前默认 Te>0，但未明示这是论文的必要条件；建议在 README 和 `wiki/modules/08_Sync/08_同步与帧结构.md` 加一节标注这两个不等式的物理含义，防止后续调参时无意破坏。
5. **粗搜 + 精搜的两阶段范式可推广到其他多普勒估计模块** —— UWAcomm `est_alpha_dsss_symbol.m`（Sun-2020）和 `est_alpha_passband_chirp.m` 都可以借鉴"IFFT 粗搜 + 1D 窄扫精搜"的成本控制策略，避免全局连续扫描。
6. **HFM 的符号惯例需要特别小心**（up+down vs down+up 帧顺序影响 sign_eps） —— UWAcomm `est_alpha_dual_hfm_vss.m` 第 56 行的 `sign_eps` 逻辑来源于此：paper 默认 "down+gap+up"（Eq.9），c_1 公式用 `+2f₀/M`；若帧为 "up+gap+down"，需用 `-2f₀/M`。这是极易出错的地方，必须在模块测试和 spec 中明示。
7. **千岛湖海试参数（f_l=10 kHz, f_h=15 kHz, T=25.6 ms, fs=80 kHz）可作为 UWAcomm 真实信号仿真的锚点** —— UWAcomm 当前仿真用 fc=12 kHz, bw≈8 kHz，与 paper 海试配置接近。可用 paper 参数做 UWAcomm end-to-end 的"参考实现对齐"测试。
8. **精度天花板 vs 计算成本的工程判断** —— 速度谱扫描"粗步 0.5 m/s + 精步 0.02 m/s"在 v ∈ (-112, +112) m/s 下粗搜 ~450 点、精搜 300 点；约 750 次复数向量点积，单次约 10-50 ms（CPU 粗估）。**若实时性要求 <10 ms**，则时延差法仍然首选，速度谱作为 off-line 精度基准。UWAcomm P3 流式场景建议沿用时延差 + 迭代 refinement，离线 benchmark 用速度谱。

### 跨项目（Hub 层）价值

9. **"频域周期 vs 时域峰位"的分辨率对偶是通用原理** —— 本文揭示：时域峰位搜索精度受采样率限制；频域做周期估计可跳过采样率限制（类似"在连续频率轴上做 DFT 取峰"优于"在离散时间轴上做 IFFT 取峰"）。这条原理在 **USBL 时延估计**（yumin-2006 的互相关三点插值）、**OTFS 延迟-多普勒估计**、**雷达目标速度测量** 等场景都有对偶形式。
10. **"剥离模板、提取周期"的数学范式** —— U(f) = f⁴|X|²/S² 是去模板化的核心操作，把"匹配滤波输出的峰位"转换为"频域周期的相位"。这一思路可推广到：
    - **DSSS 的 chip-rate 估计**（剥离 PN 码模板，估计码率偏差）
    - **OFDM 的 CFO 估计**（剥离子载波结构，估计残余频偏）
    - **阵列 DOA 估计**（剥离阵列响应模板，估计来向相位）
11. **"理论推导产出工程参数"的文档范式** —— 本文 Eq.18-19 从 Eq.16 的时域冲激位置反推参数选型约束，是教科书式的"理论→工程"推导。UWAcomm 后续 spec 模板可借鉴此风格（不等式推导替代经验值）。
12. **中科院声学所的千岛湖湖试环境是国内水声算法公认的 "mild" 测试场** —— 水深 ~30-100 m、盐度低（淡水）、噪声低、风浪弱、反射边界（湖底+湖面）简单——论文 Fig.2 的 0.04 m/s 级精度在千岛湖较容易达到，**真实海况下精度会下降 3-10 倍**。Hub 后续摄入其他中科院声学所论文时，注意环境标签区分（湖试/近海/深海）。
13. **"Doppler invariance"是 HFM 相比 LFM 的真正优势** —— LFM 在大多普勒下时频分布会倾斜变形，HFM 保持形状（只时移 + 相移）。这在宽带大动态场景（如水声通信 α > 1e-2）是**决定性优势**。Hub 涉及"远距离高速水声"场景时（UWAcomm, USBL, UWAnet），应优先考虑 HFM 前导而非 LFM。

### 与 UWAcomm 当前实现的详细对比

| 维度 | UWAcomm 现状（2026-04-22） | Wei-2020 方法 | 差距与改造方向 |
|------|--------------------------|---------------|---------------|
| 前导信号 | 双 LFM（`gen_hfm.m` 默认 HFM，但历史用 LFM 对齐） | 双 HFM（UMD-HFM） | 需确认 `gen_hfm.m` 默认是否为 HFM；若为 LFM 近似，大 α 下精度有损 |
| 估计方法 | 时延差（`est_alpha_dual_chirp.m`） + 迭代 refinement（`est_alpha_dual_hfm_iter.m`） | 速度谱扫描（`est_alpha_dual_hfm_vss.m` 已实现） | 速度谱已落地，缺 **正面 benchmark**（相同 α 范围、相同 SNR 下对比 RMSE + 计算时间） |
| 分辨率 | 时延差 ε_v = c/(T+Te+2f₀/M)/fs（受 fs 限制） + 三点插值到 ~0.1·ε_v | 速度谱 dv_fine=0.02 m/s（不受 fs 限制） | 速度谱精度下限 = dv_fine，可更精细 |
| 迭代精度 | 迭代 refinement 收敛到 ~5e-5（HFM estimator 底噪） | 单次速度谱 ~0.02 m/s ≈ α≈1.3e-5 | 速度谱单次即可达到 UWAcomm 迭代 refinement 的收敛精度 |
| 大 α 鲁棒性 | α≥1e-2 断崖 + α<0 不对称（见 `diag_alpha_pipeline.m`） | 理论上 \|v\|/c<<1 近似；极大 α 未测试 | 都存在 HFM 不变性近似偏差；**改造方向**：Murray 2019 扩展匹配滤波器 |
| 计算成本 | 低（FFT 2 次 + 峰位搜索） | 高（粗搜 O(N log N) + 精搜 ~300 点扫描） | 时延差 → 实时帧同步；速度谱 → 离线高精度 refine |
| 适用场景 | P3/P4 流式接收（实时性优先） | 离线 benchmark / 高精度 off-line refine | 分工使用；UWAcomm benchmark 模块应同时挂载两者 |
| 帧结构假设 | 不定（需查 `sync_dual_hfm.m`） | down-gap-up（paper Eq.9） | **关键**：UWAcomm `est_alpha_dual_hfm_vss.m` 已用 `sign_eps` 兼容，但需在 spec 和 README 明示 |

## 相关概念

- [[underwater-acoustic-communication]] — UWA 通信系统的多普勒估计关键组件；本文方法已成为 UWAcomm 的多普勒估计核心之一
- [[time-varying-channel]] — 多普勒估计是时变水声信道处理的前置步骤；准确的 α 是后续 resample / BEM 信道估计的前提
- [[signal-processing-fundamentals]] — FFT / IFFT / 1D 频域扫描 / Parseval 定理是本方法的基础工具
- [[channel-estimation-and-equalization]] — 多普勒补偿是信道均衡前的必备步骤；α 估计精度直接影响后续均衡性能

## 相关资料

### 项目内衔接

- UWAcomm 项目视角（更侧重工程实现细节）：`D:\Claude\TechReq\UWAcomm\wiki\source-summaries\wei-2020-dual-hfm-speed-spectrum.md`
- MATLAB 实现：`D:\Claude\TechReq\UWAcomm\modules\10_DopplerProc\src\Matlab\est_alpha_dual_hfm_vss.m`
- 对应 spec：`D:\Claude\TechReq\UWAcomm\specs\active\2026-04-21-hfm-velocity-spectrum-refinement.md`
- 对应 plan：`D:\Claude\TechReq\UWAcomm\plans\hfm-velocity-spectrum-refinement.md`
- 对比基线（时延差）：`est_alpha_dual_chirp.m` + `est_alpha_dual_hfm_iter.m`（UWAcomm 2026-04-22 α 补偿改造）
- α 断崖诊断：`wiki/modules/10_DopplerProc/大α-pipeline-不对称诊断.md`

### 关键参考文献（paper 引用链）

- Rihaczek 1966（[13]）—— Doppler-tolerant 信号波形奠基
- Yang & Sarkar 2006（[14]）—— HFM Doppler-invariance 严格证明
- Murray 2019（[15]）—— 扩展 HFM 匹配滤波器纠正 Rect(kt/T) 近似偏差（**UWAcomm 后续改造的潜在工具**）
- Kroszczynski 1969（[16]）—— HFM 频谱的 incomplete gamma function 精确表达
- Stojanovic et al. 1994（[1]）—— 水声相干通信奠基；经典相关器组 Doppler 估计
- Sharif et al. 2000（[3]）—— 块 Doppler 估计（LFM 前后插入法）
- Zhao et al. 2019（[12]）—— 同组前作：CPM 方法（本文的 baseline 之一）
- Xin et al. 2018（[11]）—— UMD-HFM 前导设计
