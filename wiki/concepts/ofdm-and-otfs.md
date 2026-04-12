---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [OFDM, OTFS, 多载波调制, 高速率, QAM]
---

# OFDM 与 OTFS 调制

## 定义

OFDM（正交频分复用）和 OTFS（正交时频空间）是两种多载波调制技术。OFDM 将宽带信道分解为多个窄带子信道，在频域实现简单均衡；OTFS 在时延-多普勒域放置信息符号，天然适配双色散信道。该方向聚焦于这两种调制方案在水声通信中的应用与改进。

## 核心问题

- **OFDM 在水声信道中的载波间干扰（ICI）**：多普勒效应破坏子载波正交性
- **OTFS 的时延-多普勒域信号处理**：如何在时延-多普勒域高效检测
- **OFDM 的高峰均功率比（PAPR）**：影响功放效率
- **频域信道估计**：导频设计与插值方案
- **MIMO-OFDM / MIMO-OTFS**：多天线与多载波的结合
- **高速率传输**：QAM 调制阶数选择与误码率权衡
- **多普勒补偿策略**：OFDM 系统的多普勒预补偿

## 关键技术

- CP-OFDM / ZP-OFDM 系统设计
- OTFS 调制/解调（ISFFT/SFFT）
- 时延-多普勒域信道估计
- ICI 消除与均衡
- PAPR 抑制技术
- 自适应比特/功率加载
- MIMO-OFDM 空频编码
- MIMO-OTFS 检测算法

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| OTFS | ~25 | OTFS 调制技术 |
| MIMO-OTFS | ~15 | MIMO-OTFS 系统 |
| Hign-Rate | ~14 | 高速率传输方案 |
| QAM Signal | ~10 | QAM 信号处理 |

总计约 **64 篇**。

## 相关概念

- [[underwater-acoustic-communication]] — OFDM 和 OTFS 是水声通信的重要调制方案
- [[channel-estimation-and-equalization]] — 多载波系统中的信道估计与均衡
- [[time-varying-channel]] — OTFS 天然适配时变双色散信道
- [[mimo-and-array-processing]] — MIMO-OFDM 和 MIMO-OTFS 系统
- [[message-passing-algorithms]] — OTFS 检测中的消息传递方法
- [[mobile-communication]] — OFDM 技术源自移动通信

## 来源

- Zotero 论文库分析 (2026-04-12)
