---
aliases: [DFE, Decision Feedback Equalizer, BiDFE]
tags: [算法, 均衡, 时域]
---

# DFE 判决反馈均衡

> 前馈+反馈两级结构：前馈补偿首达 ISI，反馈利用已判决符号消除尾部 ISI，RLS 自适应权重。

---

## 原理

前馈滤波器处理接收信号的因果部分，反馈滤波器利用已判决符号（或软符号）消除非因果 ISI。RLS 算法通过递推更新协方差矩阵实现快速收敛。双向 DFE（BiDFE）正向+反向各跑一遍取加权合并。

## 关键公式

$$d(n) = \mathbf{w}_{\text{ff}}^H \mathbf{y}(n) - \mathbf{w}_{\text{fb}}^H \hat{\mathbf{x}}(n-1:-1:n-N_{\text{fb}})$$

$$\mathbf{k} = \frac{\mathbf{P}(n-1) \mathbf{y}}{\lambda + \mathbf{y}^H \mathbf{P}(n-1) \mathbf{y}}$$

$$\mathbf{P}(n) = \frac{\mathbf{P}(n-1) - \mathbf{k} \mathbf{y}^H \mathbf{P}(n-1)}{\lambda}$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `num_ff` | 4 × 信道长度 | 前馈阶数最优值 |
| `num_fb` | max(delays) | 反馈阶数 = 最大时延 |
| `lambda` | 0.9995 | 长序列防止遗忘 |
| `pll_params.enable` | false（静态） | 静态信道必须关闭否则发散 |

## 适用条件与局限

- **适用**：SC-TDE 时域均衡，收敛速度快于 LMS
- **局限**：错误传播在低 SNR 严重；长时延信道不如 FDE
- **性能**：@20dB SER: **< 1%**；BiDFE 可缓解错误传播

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `eq_dfe` | [[07_信道估计与均衡]] |
| UWAcomm | `eq_bidirectional_dfe` | [[07_信道估计与均衡]] |

## 参考文献

- [[]]

## 相关调试经验

- [[SC-TDE调试日志]] — DFE h_est 初始化问题修复

## 相关算法

- [[MMSE-IC最小均方误差干扰消除]] — 频域替代方案
