---
type: exploration
created: 2026-04-12
updated: 2026-04-12
tags: [Zotero, 整理, 研究地图]
---

# Zotero 文件夹重组方案

基于 [[research-map]] 的 10 个研究方向，重新梳理 Zotero 原有 64 个文件夹。

## 问题诊断

当前文件夹存在以下问题：

1. **命名不统一** — 中英文混用，缩写不一致（如 `Hign-Rate`、`TV—UWA`）
2. **粒度不一致** — 有的按期刊分（IEEE TSP）、有的按主题分（doppler）、有的按项目分（叠加导频2023改）
3. **边界模糊** — `A-UWAComms` 与 `水声通信——我的阅读记录` 高度重叠（192 篇共现）
4. **未归类条目多** — 986 篇论文不在任何文件夹中

## 重组方案：两层结构

### 第一层：按研究方向（对应 wiki 概念页）

| 新文件夹 | 对应概念页 | 合并原文件夹 |
|----------|-----------|-------------|
| `01-水声通信` | [[underwater-acoustic-communication]] | A-UWAComms, 水声通信——我的阅读记录, Acoustic&Sonar, JASA, IEEE JOE, UWA Signal Processing |
| `02-信道估计与均衡` | [[channel-estimation-and-equalization]] | ChannelEstimation, Equalization, doppler, Superimposed Pilot, 叠加导频2023改, 频率估计 |
| `03-信号处理` | [[signal-processing-fundamentals]] | SignalProcessing, IEEE TSP, IEEE SPL, SP Magazine, IEEE JSTSP |
| `04-消息传递算法` | [[message-passing-algorithms]] | MessagePassing, MessagePassing&FatorGraph, FactorGraphs, AMP, AMP_Introduction, Turbo, EP, GMM-AMP, IRC-MIMO-AMP |
| `05-移动通信` | [[mobile-communication]] | MobileCommunication, WirelessComms, Comms, IEEE TWC, IEEE TCOM, IEEE CM, IEEE WC, IEEE WCL |
| `06-OFDM与OTFS` | [[ofdm-and-otfs]] | OTFS, MIMO-OTFS, Hign-Rate, QAM Signal |
| `07-数学与优化` | [[mathematical-optimization]] | Mathematics, Basic&Tool, MATLAB |
| `08-时变信道` | [[time-varying-channel]] | TimeVaryingSPorComm, TV—UWA |
| `09-MIMO与阵列` | [[mimo-and-array-processing]] | Array&MIMO |
| `10-机器学习` | [[machine-learning-methods]] | Machine Learning, 稀疏贝叶斯学习, 深度学习 |

### 第二层：保留的功能性文件夹

| 文件夹 | 用途 | 说明 |
|--------|------|------|
| `_参考书目` | 教材和专著 | 合并 Michael I. Jordan推荐以及我认为的好书, reference |
| `_综述` | 综述类论文 | 保留 Review，从各方向中提取综述论文 |
| `_团队汇报` | 组会和汇报材料 | 合并 TeamReports, 汇报 |
| `_期刊浏览` | 按期刊浏览用 | 保留 Proceedings of the IEEE 等，作为浏览入口 |
| `_近期阅读` | 当前阅读队列 | 保留 近期文献阅读，定期清空归类 |
| `_博士论文` | 学位论文 | 保留 博士论文 |
| `_待整理` | 暂未归类 | 收纳当前 986 篇未归类条目 |

## 执行步骤

### 步骤 1：在 Zotero 中创建新文件夹

在 Zotero 中创建上述 10 + 7 个文件夹。编号前缀确保排序。

### 步骤 2：批量移动

可以用 Zotero 的批量操作：
1. 点击原文件夹（如 `A-UWAComms`）
2. 全选（Ctrl+A）
3. 拖拽到新文件夹（如 `01-水声通信`）
4. 重复直到所有原文件夹清空

### 步骤 3：处理未归类条目

1. 在 Zotero 中点击「未归类条目」视图
2. 按标题/标签逐批归入对应方向文件夹
3. 实在无法归类的放入 `_待整理`

### 步骤 4：删除空文件夹

所有原文件夹清空后，右键删除。

### 步骤 5：同步验证

重组后运行：
```
python3 scripts/import-zotero.py
```
重新生成论文清单，与 wiki 研究地图对齐。

## 预期效果

| 指标 | 当前 | 重组后 |
|------|------|--------|
| 文件夹数 | 64 | 17 |
| 命名风格 | 中英混杂 | 统一中文+编号 |
| 未归类条目 | 986 | <100 |
| 与 wiki 对应 | 无 | 每个文件夹对应一个概念页 |

## 来源

- [[research-map]]
- [[zotero]]
- Zotero 论文库分析 (2026-04-12)
