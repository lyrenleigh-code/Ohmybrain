---
aliases: [BCJR, MAP译码, SISO译码, Log-MAP, Max-Log-MAP]
tags: [算法, 信道编码, Turbo]
---

# BCJR 前向后向 MAP 译码

> 在 Trellis 网格上进行前向 α 递推与后向 β 递推，精确计算信息比特后验 LLR，Turbo 均衡核心组件。

---

## 原理

遍历卷积码的所有状态转移，计算每个信息比特为 0 或 1 的后验概率之比（LLR）。前向递推累积历史信息，后向递推累积未来信息，两者结合给出最优软判决。

## 关键公式

$$\gamma(t, s \to s') = (2u-1) \cdot L_a/2 + \sum_i (2c_i-1) \cdot L_{c_i}/2$$

$$\alpha(s, t+1) = \max^*_{s': s' \to s} [\alpha(s', t) + \gamma(t, s' \to s)]$$

$$\beta(s, t) = \max^*_{s': s \to s'} [\beta(s', t+1) + \gamma(t, s \to s')]$$

$$L_{\text{post}}(t) = \max^*_{u=1} [\alpha + \gamma + \beta] - \max^*_{u=0} [\alpha + \gamma + \beta]$$

## 参数选择

| 参数 | 典型值 | 选择依据 |
|------|--------|---------|
| `gen_polys` | [7,5] 或 [171,133] | [7,5] 低复杂度 $d_{\text{free}}=5$；[171,133] NASA 标准 |
| `decode_mode` | `'max-log'` | 快速，损失 0.2~0.5dB；`'log-map'` 精确 |

## 适用条件与局限

- **适用**：Turbo 均衡中软信息交换的核心，所有体制通用
- **局限**：Max-Log 比 Log-MAP 损失 0.2~0.5dB；复杂度 O(N·S)，S=状态数
- **性能**：软判决比硬判决约 **2dB 编码增益**

## 实现

| 项目 | 函数 | 位置 |
|------|------|------|
| UWAcomm | `siso_decode_conv` | [[02_信道编解码]] |

## 参考文献

- [[bahl1974optimal]]

## 相关算法

- [[MMSE-IC最小均方误差干扰消除]] — Turbo 中 BCJR 与 MMSE-IC 交替迭代
