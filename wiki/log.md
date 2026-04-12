# 变更日志

> 记录每次对 wiki 的操作，最新的在最上面。

---

## [2026-04-12] create | 系统架构总览

创建 `architecture/system-overview.md`，文档化六层结构、双闭环（知识+开发）、Harness 机制和工具链架构图。同步升级工程体系：新增 specs/plans/tasks/evals/ 目录、.claude/rules/ 路径规则、.claude/skills/ 技能定义、bash hooks、CI workflow。

---

## [2026-04-12] ingest | UWAcomm 水声通信仿真平台

对 `raw/repos/UWAcomm` 项目执行 ingest，创建了 2 个新 wiki 页面并更新了 6 个概念页：

- **1 个 source-summary 页**：`source-summaries/uwacomm.md` — 项目摘要，含 6 种通信体制性能对比、13 个模块职责、关键技术和端到端信号流
- **1 个实体页**：`entities/uwacomm.md` — 项目实体页，含完整模块架构、性能数据和技术特色
- **更新 6 个概念页**（在来源部分追加 UWAcomm 实现信息）：
  - `concepts/underwater-acoustic-communication.md` — 核心实现项目
  - `concepts/channel-estimation-and-equalization.md` — 15+ 种估计算法 + 10+ 种均衡器
  - `concepts/ofdm-and-otfs.md` — OFDM/OTFS/SC-FDE 多载波变换
  - `concepts/message-passing-algorithms.md` — AMP/VAMP/Turbo-VAMP/MP 消息传递算法
  - `concepts/mimo-and-array-processing.md` — ULA 阵列接收处理
  - `concepts/time-varying-channel.md` — BEM/DD-BEM/Kalman 时变估计 + 多普勒补偿

更新了 `index.md`（页面总数 22 → 24）。

---

## [2026-04-12] create | Zotero 重组方案

基于研究地图生成 Zotero 文件夹重组方案 `explorations/zotero-reorganization.md`，将 64 个文件夹精简为 17 个（10 个研究方向 + 7 个功能性文件夹）。

---

## [2026-04-12] ingest | 3 份原始资料 + 7 个实体页

对 raw/ 目录下 3 份已有资料执行 ingest，创建了 10 个新 wiki 页面：

- **3 个 source-summary 页** `source-summaries/` 目录下：
  - `my-brain-setup-plan.md` — 搭建计划摘要，提取三阶段方案核心内容
  - `toolchain.md` — 工具链指南摘要，梳理各工具职责和架构
  - `zotero-library-catalog.md` — 论文库清单摘要，统计规模和主题分布
- **7 个实体页** `entities/` 目录下：
  - `claude-code.md` — 执行引擎
  - `obsidian.md` — 可视化层
  - `zotero.md` — 论文管理
  - `readwise-reader.md` — 文章收集
  - `whisper.md` — 本地视频转录
  - `firecrawl.md` — YouTube 视频转 markdown
  - `github.md` — 同步与自动化

更新了 `index.md`（页面总数 11 → 21）。

---

## [2026-04-12] create | 研究地图与概念页

基于 Zotero 论文库分析（~3179 篇论文），创建了 11 个 wiki 页面：

- **研究全景地图** `topics/research-map.md` — 展示 10 个研究方向的层次结构、交叉关系和论文分布
- **10 个概念页** `concepts/` 目录下：
  - `underwater-acoustic-communication.md` — 水声通信系统（~1120篇）
  - `channel-estimation-and-equalization.md` — 信道估计与均衡（~335篇）
  - `signal-processing-fundamentals.md` — 信号处理基础（~328篇）
  - `message-passing-algorithms.md` — 消息传递与因子图（~225篇）
  - `mobile-communication.md` — 移动通信（~95篇）
  - `ofdm-and-otfs.md` — OFDM与OTFS调制（~64篇）
  - `mathematical-optimization.md` — 数学与优化（~30篇）
  - `time-varying-channel.md` — 时变信道处理（~22篇）
  - `mimo-and-array-processing.md` — MIMO与阵列处理（~21篇）
  - `machine-learning-methods.md` — 机器学习方法（~2篇）

所有页面使用 `[[wikilink]]` 互相链接，更新了 `index.md`。

---

- 2026-04-12: 初始化 my-brain 仓库，创建目录结构和基础文件
