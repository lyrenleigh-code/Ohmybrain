---
aliases: [GAMP, Generalized Approximate Message Passing]
tags: [算法, 信道估计, 稀疏重建]
---

# GAMP 广义近似消息传递

> 通过因子图上的迭代消息传递，用高斯近似处理复杂后验分布，支持任意稀疏先验的信道估计。

---

## 原理

在因子图 $y = \Phi h + w$ 上，GAMP 将精确 BP 的高维积分用高斯近似替代：每轮迭代中，观测节点向变量节点传递均值/方差消息，变量节点通过先验函数（如 Bernoulli-Gaussian）更新估计。

## 关键公式

$$\hat{p}(n) = \sum_m |\Phi(m,n)|^2 \cdot \tau_p(m)$$

$$\hat{r}(n) = \hat{x}(n) + \hat{p}(n) \sum_m \Phi^*(m,n) \cdot s(m)$$

$$\hat{x}(n) = g_{\text{in}}(\hat{r}(n),\; \hat{p}(n))$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `max_iter` | 50~100 | 通常 50 次足够收敛 |
| `noise_var` | 需提供或自动估计 | 用于高斯近似 |
| `K_sparse` | `ceil(N/10)` | 稀疏度上限 |

## 适用条件与局限

- **适用**：稀疏信道估计，支持非高斯先验，复杂度 O(MN) 线性
- **局限**：测量矩阵非 i.i.d. 时收敛无保证，此时改用 VAMP/Turbo-VAMP
- **性能**：@15dB NMSE: **-34.2dB**（与 OMP 相当）

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `ch_est_gamp` | [[07_信道估计与均衡]] |

## 参考文献

- [[rangan2011generalized]]

## 相关调试经验

- [[OFDM调试日志#V4.1]] — 高 SNR 震荡问题，改用 OMP

## 相关算法

- [[OMP正交匹配追踪]] — 贪心替代方案
- [[SBL稀疏贝叶斯学习]] — EM 替代方案
