---
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [移动通信, 无线通信, 5G, 参考技术]
---

# 移动通信

## 定义

移动通信方向涵盖陆地无线/移动通信系统的技术与理论，包括蜂窝网络、WiFi 等无线通信体制。在本研究体系中，移动通信主要作为**参考和借鉴方向**，其成熟的技术方案（如 OFDM、MIMO、Turbo 编码）被移植和适配到水声通信场景中。

## 核心问题

- **无线信道建模**：多径衰落、阴影效应、多普勒扩展
- **多址接入技术**：OFDMA、NOMA、CDMA
- **MIMO 通信**：空间复用、波束成形、空时编码
- **5G/6G 关键技术**：大规模 MIMO、毫米波、超可靠低时延
- **资源分配与调度**：功率控制、子载波分配
- **信道编码**：LDPC、Polar 码

## 关键技术

- OFDM/OFDMA 多载波技术
- MIMO 空时处理
- 自适应调制编码（AMC）
- 混合自动重传（HARQ）
- 多用户检测
- 干扰管理与协调
- 认知无线电与频谱感知

## Zotero 对应文件夹

| 文件夹名 | 大致论文数 | 说明 |
|---------|----------|------|
| MobileCommunication | ~50 | 移动通信综合 |
| WirelessComms | ~30 | 无线通信 |
| Comms | ~15 | 通信通用论文 |

总计约 **95 篇**。作为水声通信的技术参考源。

## 相关概念

- [[underwater-acoustic-communication]] — 移动通信技术向水声通信的迁移
- [[ofdm-and-otfs]] — OFDM 技术源自移动通信领域
- [[mimo-and-array-processing]] — MIMO 技术在移动通信中已高度成熟
- [[channel-estimation-and-equalization]] — 无线信道估计与均衡方法的借鉴
- [[message-passing-algorithms]] — Turbo/LDPC 译码中的消息传递

## 来源

- Zotero 论文库分析 (2026-04-12)
- [[lalevee-2025-dichotomous-doppler]] — AUV 运动导致多普勒效应的嵌入式处理方案
- [[yangyang-2026-uwa-otfs-nonuniform-doppler]] — 水下高移动性（2 m/s）平台 OTFS 实测：相比 OFDM 同速率下 BER 低 0.5-1 数量级
- [[doppler-estimation-methods]] — 移动场景是多普勒估计的主要物理来源
