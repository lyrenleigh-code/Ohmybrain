---
aliases: [MP, Message Passing, OTFS-MP, BP均衡]
tags: [算法, 均衡, OTFS]
---

# MP 消息传递 OTFS 均衡

> 在 DD 域因子图上实现高斯近似 BP 算法：观测节点与数据节点间迭代传递均值/方差消息。

---

## 原理

OTFS 的 DD 域输入输出关系天然稀疏（仅 P 条路径产生干扰），构建二部因子图后，通过高斯近似消息传递迭代求解每个数据符号的后验均值和方差。

## 关键公式

$$\mu_{m \to n} = \frac{Y(m) - \sum_{n' \neq n} h_{n'} \mu_{n' \to m}}{h_n}$$

$$\sigma^2_{m \to n} = \frac{\sigma_w^2 + \sum_{n' \neq n} |h_{n'}|^2 v_{n' \to m}}{|h_n|^2}$$

$$v_n = \left(\frac{1}{v_{\text{prior}}} + \sum_m \frac{|h_m|^2}{\sigma^2_{m \to n}}\right)^{-1}$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `max_iter` | 10 | 通常足够收敛 |
| `prior_mean/var` | Turbo 时由译码提供，单独=0/1 | 软信息接口 |

## 适用条件与局限

- **适用**：OTFS 信号处理最优，DD 域稀疏表示天然
- **局限**：路径数 P 增大时因子图环路加长，BP 近似精度下降
- **简化版**：用 MMSE 近似降至 O(P·NM)

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `eq_otfs_mp` | [[07_信道估计与均衡]] |
| UWAcomm | `eq_otfs_mp_simplified` | [[07_信道估计与均衡]] |

## 参考文献

- [[raviteja2018interference]]

## 相关调试经验

- [[OTFS调试日志]] — DD 域索引和 per-sub-block CP 问题

## 相关算法

- [[GAMP广义近似消息传递]] — 同属消息传递框架
