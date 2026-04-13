---
aliases: [MMSE-IC, Minimum Mean Square Error Interference Cancellation]
tags: [算法, 均衡, Turbo]
---

# MMSE-IC 最小均方误差干扰消除

> Turbo 迭代均衡核心：先用译码反馈软符号做干扰消除，再用 MMSE 滤波器处理残余信号，形成迭代正反馈。

---

## 原理

频域逐子载波处理：用上一轮 BCJR 输出的软符号 $\bar{x}$ 重建并减去 ISI，对残余信号施加 MMSE 权重，输出更新后的软估计送入下一轮 BCJR。

## 关键公式

$$G(k) = \frac{H^*(k) \cdot \sigma_x^2}{|H(k)|^2 \cdot \sigma_x^2 + \sigma_w^2}$$

$$\tilde{x} = \text{IFFT}\{G \cdot (Y - H \cdot \text{FFT}(\bar{x}))\} + \bar{x}$$

$$\mu = \text{mean}(G \cdot H), \quad \tilde{\nu} = \mu(1-\mu)$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `x_bar` | 首次=0, 后续=soft_mapper输出 | 软符号先验 |
| `var_x` | 首次=1, 需下限截断 | `max(var_x, noise_var)` 防数值不稳定 |
| 迭代次数 | 3~6 次 | 增益边际递减 |

## 适用条件与局限

- **适用**：SC-FDE/OFDM Turbo 均衡，直接利用软信息反馈
- **局限**：假设信道块内不变；时变信道需先 BEM 估计再分块 FDE
- **性能**：@20dB SER: **< 0.5%**

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `eq_mmse_ic_fde` | [[07_信道估计与均衡]] |

## 参考文献

- [[tuchler2002minimum]]

## 相关调试经验

- [[SC-FDE调试日志]] — MMSE-IC Turbo 迭代调试
- [[OFDM调试日志]] — OFDM 逐子载波 MMSE-IC

## 相关算法

- [[BCJR前向后向MAP译码]] — Turbo 中 BCJR 与 MMSE-IC 交替迭代
- [[BEM基扩展模型]] — 时变信道下 BEM 估计喂入 MMSE-IC
