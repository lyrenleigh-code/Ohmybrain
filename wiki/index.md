# Wiki Index

> 最后更新：2026-04-14
> 页面总数：43

## Concepts（概念页）

- [underwater-acoustic-communication](concepts/underwater-acoustic-communication.md) — 水声通信系统，利用声波在水下传输信息的核心方向（~1120篇）
- [channel-estimation-and-equalization](concepts/channel-estimation-and-equalization.md) — 信道估计与均衡，接收机获取信道响应并消除码间干扰（~335篇）
- [signal-processing-fundamentals](concepts/signal-processing-fundamentals.md) — 信号处理基础，统计信号处理、估计检测等理论方法（~328篇）
- [message-passing-algorithms](concepts/message-passing-algorithms.md) — 消息传递与因子图，概率图模型上的迭代推断算法（~225篇）
- [mobile-communication](concepts/mobile-communication.md) — 移动通信，陆地无线通信技术，水声通信的技术借鉴源（~95篇）
- [ofdm-and-otfs](concepts/ofdm-and-otfs.md) — OFDM与OTFS调制，多载波调制技术在水声通信中的应用（~64篇）
- [mathematical-optimization](concepts/mathematical-optimization.md) — 数学与优化，研究体系的基础工具层（~30篇）
- [time-varying-channel](concepts/time-varying-channel.md) — 时变信道处理，双色散信道的建模估计与补偿（~22篇）
- [mimo-and-array-processing](concepts/mimo-and-array-processing.md) — MIMO与阵列处理，多天线空间域信号处理技术（~21篇）
- [machine-learning-methods](concepts/machine-learning-methods.md) — 机器学习方法，数据驱动的通信方法新兴方向（~2篇）
- [harness-engineering](concepts/harness-engineering.md) — Harness 工程，Claude Code agent harness 的设计与实践
- [usbl-positioning](concepts/usbl-positioning.md) — 超短基线定位，USBL技术链路、商用设备参数、工程经验
- [subagents-orchestration](concepts/subagents-orchestration.md) — Claude Code 子代理编排，16 字段 frontmatter + Command→Agent→Skill 模式
- [skills-vs-commands](concepts/skills-vs-commands.md) — Skill/Command/Agent 三机制对比，决策树 + 解析优先级
- [claude-hooks-architecture](concepts/claude-hooks-architecture.md) — Claude Code Hook 架构，15 个生命周期事件 + 作用域层级

## Entities（实体页）

- [claude-code](entities/claude-code.md) — Claude Code，Anthropic CLI 工具，my-brain 系统的核心执行引擎
- [obsidian](entities/obsidian.md) — Obsidian，基于本地 markdown 的知识管理工具，wiki 的可视化层
- [zotero](entities/zotero.md) — Zotero，开源文献管理工具，论文和 PDF 的专属管理器
- [readwise-reader](entities/readwise-reader.md) — Readwise Reader，网页文章收集和高亮管理工具
- [whisper](entities/whisper.md) — Whisper，OpenAI 开源语音识别模型，本地视频转录工具
- [firecrawl](entities/firecrawl.md) — Firecrawl，网页抓取工具，YouTube 视频转 markdown 的首选方案
- [github](entities/github.md) — GitHub，多设备同步和自动化检查的基础设施
- [uwacomm](entities/uwacomm.md) — UWAcomm，MATLAB 全栈水声通信算法仿真平台，覆盖 6 种通信体制

## Architecture（架构页）

- [system-overview](architecture/system-overview.md) — 系统架构总览，六层结构、双闭环（知识+开发）、Harness 机制、工具链

## Topics（专题页）

- [research-map](topics/research-map.md) — 研究全景地图，展示10个研究方向的层次结构和交叉关系

## Explorations（探索页）

- [zotero-reorganization](explorations/zotero-reorganization.md) — Zotero 文件夹重组方案，基于研究地图将 64 个文件夹精简为 17 个
- [ohmybrain-agent-architecture-insights](explorations/ohmybrain-agent-architecture-insights.md) — 基于 Claude Code Best Practice + Hermes Agent 对照的 Ohmybrain 架构启发录（P0/P1/P2/P3 行动项）
- [wiki-ingester-ab-test-dingjie-2020](explorations/wiki-ingester-ab-test-dingjie-2020.md) — 新架构（wiki-ingester Agent）首次实测 A/B 报告，丁杰 2020 USBL 博士论文

## Comparisons（比较页）

<!-- A vs B 类分析 -->

## Source Summaries（资料摘要页）

- [my-brain-setup-plan](source-summaries/my-brain-setup-plan.md) — my-brain 系统搭建计划，harness + LLM wiki 一体化的三阶段方案
- [toolchain](source-summaries/toolchain.md) — 工具链指南，围绕 harness + LLM wiki 系统的完整工具链架构
- [zotero-library-catalog](source-summaries/zotero-library-catalog.md) — Zotero 论文库结构化清单，5660 篇论文按 64 个文件夹分类
- [uwacomm-summary](source-summaries/uwacomm.md) — UWAcomm 项目摘要，186 个 MATLAB 函数、13 个模块、6 种通信体制
- [claude-code-best-practice](source-summaries/claude-code-best-practice.md) — Claude Code 最佳实践参考仓摘要，三机制对比 + 编排模式 + MCP/Hook/Memory 全景
- [nousresearch-hermes-agent](source-summaries/nousresearch-hermes-agent.md) — Hermes Agent（Nous Research，MIT）自改进开源 Agent，agentskills.io 标准 + 16 消息平台 + 6 终端后端
- [dingjie-2020-compact-usbl](source-summaries/dingjie-2020-compact-usbl.md) — 复杂紧凑型 USBL 定位+阵型+安装三项联合校准（丁杰博士论文, 哈工程 2020），含商用 USBL 设备参数对比表
- [hexutao-usbl-quad-array](source-summaries/hexutao-usbl-quad-array.md) — 改进非等距四元立体阵 USBL + EKF 降噪 + 短基线参考解相位模糊（何旭涛等, 2025 期刊，海底电缆定位应用）
- [guoyu-2024-lie-group-nav](source-summaries/guoyu-2024-lie-group-nav.md) — 李群误差定义下 SINS/DVL/USBL 组合导航（郭瑜博士论文, 哈工程 2024），RIE-KF + MASSMKF + BP 重构
- [liufeng-2024-passive-localization](source-summaries/liufeng-2024-passive-localization.md) — 水下移动节点声学被动定位（刘峰博士论文, 浙大 2024），虚拟信标网络 + 因子图 + iUSBL 三场景统一范式
- [zhengcuie-usbl-docking](source-summaries/zhengcuie-usbl-docking.md) — USBL 用于 AUV 对接三段式（郑翠娥博士论文, 哈工程 ~2007-2010），脉冲对双频抗模糊 + 矩形应答器阵位姿解算
- [yangbaoguo-2013-usbl-calibration](source-summaries/yangbaoguo-2013-usbl-calibration.md) — USBL 安装校准（杨保国博士论文, 哈工程 2013），观测方程三性质统领校准 + 两步去偏 LS + M 估计
- [quzhenzhao-2024-usbl-precision](source-summaries/quzhenzhao-2024-usbl-precision.md) — 五元十字阵多构型数据融合提升精度（蘧振超等, 2024 期刊短文）
- [huangjian-2019-lbl-usbl](source-summaries/huangjian-2019-lbl-usbl.md) — LBL/USBL 组合定位跟踪六项关键技术（黄健博士论文, 西工大 2019）
- [yumin-2006-lr-usbl](source-summaries/yumin-2006-lr-usbl.md) — 国内首代长程 USBL 系统研制（喻敏博士论文, 哈工程 863 项目 2006）
