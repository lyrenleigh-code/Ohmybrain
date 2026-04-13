# OTFS

> 正交时频空（Orthogonal Time Frequency Space）— 时延-多普勒域通信技术
> 项目实现：[[06_多载波变换]]（OTFS调制/解调/导频） [[07_信道估计与均衡]]（DD域估计+MP均衡） [[12_迭代调度器]]（OTFS Turbo）
> 参考论文集：`refrence/OTFS/`（8篇IEEE论文）
> 综合架构文档：`refrence/OTFS/OTFS_Architecture.html`

#OTFS #领域知识

---

## 一、核心概念

OTFS 在**时延-多普勒（DD）域**而非时频域放置信息符号。DD域中信道表现为**准静态稀疏**（少量非零点），即使在高速移动场景下也保持稳定。

### DD域输入输出关系

$$Y[k,l] = \sum_{p} h_p \cdot X\!\left[(k - k_p) \bmod N,\; (l - l_p) \bmod M\right] + W[k,l]$$

其中 $(k_p, l_p)$ 是第 $p$ 径的多普勒-时延索引，$h_p$ 是复增益。

---

## 二、调制/解调

### 2.1 DFT方法（两步）

**ISFFT（DD→TF）**:
$$X_{\text{tf}}[n,m] = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} x_{\text{dd}}[k,m] \cdot e^{j2\pi nk/N}$$

**Heisenberg变换（TF→时域）**:
$$s_n = \text{IFFT}(X_{\text{tf}}[n,:]) \cdot \sqrt{M}$$

### 2.2 Zak变换（一步等效）

$$S = \text{ifft2}(X_{\text{dd}}) \cdot \sqrt{NM}$$

DFT和Zak方法数学等价。

> 参考：Hadani, R. et al. "Orthogonal time frequency space modulation", IEEE WCNC (2017) [^1] — **OTFS奠基论文**

---

## 三、DD域信道估计

### 3.1 嵌入式导频方案

| 方案 | 原理 | 频谱效率 | 参考 |
|------|------|---------|------|
| **Impulse** | 单脉冲+矩形保护区 | 低（大guard） | Raviteja (2018) [^2] |
| **Superimposed** | 导频叠加在数据上 | **高** | Mishra et al. (2022) [^3] |
| **Sequence** | ZC序列替代脉冲 | 中 | Shen et al. (2019) [^4] |
| **Data-aided** | 单导频+判决反馈迭代 | 高 | Yuan et al. (2021) [^5] |
| **Adaptive** | guard区自适应信道扩展 | 自适应 | 项目实现 |

保护区设计：

$$\text{guard\_l} = \max(\text{delay\_spread}) + 1, \quad \text{guard\_k} = \max(\text{doppler\_spread}) + 1$$

> **项目经验**：guard区必须防止数据泄漏，导频需功率boost，nv用有效噪声。见 CLAUDE.md。

---

## 四、DD域均衡/检测

### 4.1 消息传递（MP）

在DD域因子图上进行高斯近似BP：

$$\mu_{m \to n} = \frac{Y(m) - \sum_{n' \neq n} h_{n'} \mu_{n' \to m}}{h_n}$$

$$v_n = \left(\frac{1}{v_{\text{prior}}} + \sum_m \frac{|h_m|^2}{\sigma^2_{m \to n}}\right)^{-1}$$

> 参考：Raviteja et al. "Interference cancellation and iterative detection for OTFS", IEEE TWC (2018) [^2]

### 4.2 UAMP检测

2D FFT加速的统一近似消息传递。

> 参考：Yuan et al. "Iterative detection for OTFS space-time coding", IEEE TWC (2022) [^6]

### 4.3 DD域Turbo均衡

双层迭代：
- **内层**：MP-BP（10次BP迭代）
- **外层**：Turbo循环（MP ↔ BCJR）

> 参考：Zhang et al. "Delay-Doppler domain decision feedback turbo equalization", Phys. Commun. (2022) [^7] — **水声通信应用**

---

## 五、与OFDM的关系

| 维度 | OFDM | OTFS |
|------|------|------|
| 信息域 | 时频(TF) | 时延-多普勒(DD) |
| 信道表现 | 频选+时变（复杂） | **准静态稀疏**（简洁） |
| 多普勒鲁棒性 | 差（ICI） | **强** |
| 实现基础 | IFFT/FFT | ISFFT+IFFT / 2D-IFFT |
| 信道估计 | 逐子载波 | DD域导频（全局有效） |

---

## 参考论文集（`refrence/OTFS/`）

[^1]: Hadani, R. et al. "Orthogonal time frequency space modulation." IEEE WCNC, 2017. — **奠基论文**
[^2]: Raviteja, P. et al. "Interference cancellation and iterative detection for OTFS modulation." IEEE TWC, 2018. — **MP检测**
[^3]: Mishra, H.B. et al. "OTFS channel estimation and data detection designs with superimposed pilots." IEEE TWC, 2022. — **叠加导频**
[^4]: Shen, W. et al. "Channel estimation for OTFS systems." IEEE TSP, 2019. — **3D-SOMP稀疏估计**
[^5]: Yuan, W. et al. "Data-aided channel estimation for OTFS systems with a single pilot." IEEE WCL, 2021. — **数据辅助估计**
[^6]: Yuan, Z. et al. "Iterative detection for OTFS space-time coding." IEEE TWC, 2022. — **UAMP+2D-FFT**
[^7]: Zhang, Y. et al. "Delay-Doppler domain decision feedback turbo equalization." Phys. Commun., 2022. — **DD域Turbo+UWA**
[^8]: Wei, Z. et al. "OTFS modulation: A promising next-generation waveform." IEEE Wireless Commun., 2021. — **综述/6G展望**
[^9]: K.P., A. & Murthy, C.R. "Orthogonal delay scale space modulation." IEEE TSP, 2022. — **ODSS宽带扩展**
