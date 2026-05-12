---
type: source-summary
created: 2026-05-12
updated: 2026-05-12
tags: [OTFS, pilot, PAPR, NMSE, tradeoff, 水声通信]
source_type: note
---

# UWAcomm OTFS Pilot 三方案 PAPR-NMSE Tradeoff

## 主题

OTFS 调制三种 pilot 方案（Impulse / ZC / Superimposed）的根本 tradeoff——**PAPR vs NMSE vs 实现复杂度**——基于 UWAcomm 项目 2026-04-14 实测数据沉淀。OTFS 当前在 UWAcomm 暂停（详见 memory `feedback_uwacomm_skip_otfs` / 2026-04-27 重启），本页作物理参考供任何项目恢复 OTFS 工作时直接调用。

## Tradeoff 对照表

| 方案 | PAPR | NMSE @15dB | 工程问题 |
|------|------|-----------|---------|
| **Impulse** | 17 dB | -42 dB | 时域周期性尖刺（每 sub_block 一个） |
| **ZC 序列** | 6.6 dB | -37 dB | 边缘延迟阴影落数据区致 E2E BER 差 5-10 dB |
| **Superimposed** | 8.8 dB | -15 dB（天花板） | data 干扰主导，需 Turbo 软 LLR 反馈 |

## 物理解释

Impulse pilot 能量 = sqrt(N_data) ≈ 43 集中在单 DD 点，经 OTFS 变换后每子块峰值 V/sqrt(N) = 7.6，导致 PAPR 高。

**降 PAPR 的两条路径**：
- 扩散能量（ZC / Superimposed）— 牺牲 NMSE
- 增加复杂度（Superimposed + Turbo）— 需要 Turbo 环路集成

## 选型指南（OTFS 恢复时）

| 场景 | 推荐方案 | 注意事项 |
|------|---------|---------|
| 主要关注 BER 且 PAPR 可容忍 | **Impulse** | 最简单，NMSE 最好 |
| 主要关注 PAPR 降低 | **ZC 序列** | 需修复 `embed_sequence` 让 guard 覆盖延迟阴影 `[pl-gl, pl+gl+L_max]` |
| 已有 Turbo 框架且想 PAPR + NMSE 折中 | **Superimposed** | 需 Turbo 环内集成（软 LLR + 迭代），独立估计器有 -15dB 天花板，不适合非 Turbo 场景 |

## 关键公式

- **Superimposed 数据干扰 SIR** = NM × pilot_power / data_power（处理增益后）
- 当 pilot_power = 0.2 时 SIR ≈ 26 dB

## UWAcomm 项目实现文件（参考）

| 文件 | 功能 |
|------|------|
| `ch_est_otfs_zc` | LS pinv(S) 反解 Toeplitz |
| `ch_est_otfs_superimposed` | MMSE 均衡 + 硬判决 + SPUC 迭代 |

## 跨项目启发

- **任何 OTFS 项目设计 pilot 时**：三方案不是"选最好"而是"选符合主要约束"——PAPR / NMSE / 软迭代复杂度三角
- **NMSE 天花板现象**：Superimposed 的 -15 dB 天花板是 SIR 限制，单纯调参数无法突破，必须靠 Turbo 软反馈把数据干扰减弱
- **延迟阴影问题**（ZC 特有）：guard 区设计必须覆盖整个延迟扩展，否则 NMSE 数字漂亮但 E2E BER 退化

## 相关概念

- [[ofdm-and-otfs]] — OTFS 调制概念页
- [[doppler-estimation-methods]] — UWA 多普勒估计方法学
- [[underwater-acoustic-communication]] — 水声通信总览

## 来源

- UWAcomm 项目 2026-04-14 实测数据
- memory `reference_otfs_pilot_tradeoff`（项目侧记录，本页为 Hub 沉淀）
