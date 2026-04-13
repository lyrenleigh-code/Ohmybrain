---
aliases: [SBL, Sparse Bayesian Learning, RVM]
tags: [算法, 信道估计, 稀疏重建]
---

# SBL 稀疏贝叶斯学习

> EM 算法迭代学习每个抽头的超参数（方差），无需预知稀疏度，自动驱动非活跃抽头趋零实现稀疏性。

---

## 原理

为每个抽头引入独立的先验方差 $\gamma_i$（超参数），通过 EM 迭代：E 步在当前超参数下计算后验均值和协方差，M 步更新超参数。非活跃抽头的 $\gamma_i$ 自动趋零，实现自动稀疏性。

## 关键公式

$$\text{E步：} \quad \Sigma = \left(\frac{\Phi^H \Phi}{\sigma^2} + \Gamma^{-1}\right)^{-1}, \quad \mu = \Sigma \frac{\Phi^H y}{\sigma^2}$$

$$\text{M步：} \quad \gamma_i = |\mu_i|^2 + \Sigma_{ii}$$

$$\sigma^2 \leftarrow \frac{\|y - \Phi\mu\|^2 + \sigma^2 \sum(1 - \Sigma_{ii}/\gamma_i)}{M}$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `max_iter` | 100 | 通常 20~50 次收敛 |
| `tol` | 1e-6 | $\|\gamma_{\text{new}} - \gamma_{\text{old}}\| / \|\gamma_{\text{old}}\|$ |
| 置零阈值 | $\max(\gamma) \times 10^{-4}$ | 自动剪枝弱抽头 |

## 适用条件与局限

- **适用**：无需预知稀疏度 K，鲁棒性强，EM 理论基础坚实
- **局限**：复杂度 O(iter·N^2·M) 较高；M < N 时协方差矩阵求逆不稳定
- **性能**：@15dB NMSE: **-28.1dB**（略低于 OMP/GAMP，但不需预知 K）

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `ch_est_sbl` | [[07_信道估计与均衡]] |

## 参考文献

- [[wipf2004sparse]]

## 相关算法

- [[GAMP广义近似消息传递]] — 复杂度更低的替代方案
- [[OMP正交匹配追踪]] — 贪心替代方案（需预知 K）
