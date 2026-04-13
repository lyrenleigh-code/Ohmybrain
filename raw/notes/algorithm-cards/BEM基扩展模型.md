---
aliases: [BEM, Basis Expansion Model, CE-BEM, DCT-BEM]
tags: [算法, 信道估计, 时变信道]
---

# BEM 基扩展模型

> 用有限个基函数展开时变信道，将无限维时间连续问题转化为有限维参数估计。

---

## 原理

时变信道 $h(n,p)$ 在一个数据块内用 $Q+1$ 个基函数线性展开，将 $N \times P$ 个未知量压缩到 $(Q+1) \times P$ 个 BEM 系数。DCT 基在有限帧内频谱泄漏最小，优于 CE 基。

## 关键公式

$$h(n,p) = \sum_{q=0}^{Q} c(q,p) \cdot b_q(n)$$

$$\text{DCT基：} b_q(n) = \cos\left(\frac{\pi q (2n+1)}{2N}\right)$$

$$\mathbf{c} = (\mathbf{B}^H \mathbf{B} + \lambda \mathbf{I})^{-1} \mathbf{B}^H \mathbf{y}_{\text{obs}}$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `bem_type` | `'dct'` | DCT 优于 CE（有限帧频谱泄漏小） |
| Q (基函数数) | $2\lceil f_d N / R_s \rceil$ | 过小→建模误差，过大→过参数化 |
| 散布导频 | 簇长=max_delay+50, 间隔300 | 提供时域观测 |

## 适用条件与局限

- **适用**：块级时变信道，配合散布导频效果最优
- **局限**：快变信道需密集导频；块间不连续产生边界效应
- **性能**：DCT+散布导频比仅训练增益 **+21.7dB @5Hz**

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `ch_est_bem` | [[07_信道估计与均衡]] |
| UWAcomm | `ch_est_bem_dd` | [[07_信道估计与均衡]] |

## 参考文献

- [[giannakis1998basis]]

## 相关调试经验

- [[SC-TDE调试日志]] — 时变信道 BEM+散布导频调试
- [[时变信道估计与均衡调试笔记]] — DD-BEM 重估计

## 相关算法

- [[MMSE-IC最小均方误差干扰消除]] — BEM 输出喂入 MMSE-IC 均衡
