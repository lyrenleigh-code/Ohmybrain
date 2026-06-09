# FlowGen

> 需求到 Mermaid 流程图的自动生成工具 — LLM 驱动，CLI + Claude Code skill 双形态，供跨项目调用

- **仓库**：暂未上 GitHub（私人工具，单用户）
- **本地**：`D:\Claude\Tools\FlowGen`
- **分类**：Tools/（跨项目工具类，区别于 TechReq/ 算法研究项目）
- **状态**：刚完成 SOP 派生（2026-04-23），未开始实装
- **派生自**：历史旧模板；当前同类模板为 `D:\Claude\ohmybrain-core\template-tool\`

## 目标

三种输入形态 → Mermaid flowchart → 嵌入 `.md` / 写文件 / stdout，供 UWAcomm / USBL / UWAnet 等项目调用：

| 输入模式 | 引擎 | 里程碑 |
|---|---|---|
| A 自然语言需求 | Claude API + few-shot | M1 MVP |
| B YAML / JSON 结构化 | 规则 + LLM 兜底 | M2 |
| C MATLAB 代码静态分析 | regex + LLM 摘要 | M3 |

## 典型调用场景

- 写 wiki / spec 嵌入算法流程图：`flowgen text "接收端：HFM 同步→多普勒估计→重采样→CP 去除→信道估计→均衡→译码→BER"`
- UWAcomm 模块调用链可视化：`flowgen matlab modules/13_SourceCode/src/Matlab/rx_main.m`
- USBL 定位链路：`flowgen text "四元阵采集→互相关时延→方位角解算→EKF→输出"`

## 参考源仓（已摄入 Hub）

- **mermaid-js/mermaid** — diagram-as-code 事实标准，本地浅克隆于 `raw/repos/mermaid/`
- 摘要：[[mermaid-js-mermaid]]（Ohmybrain Hub wiki）

## 约束

- **单用户私人工具**：无 auth / 多租户 / 国际化
- **输出仅 Mermaid flowchart**（不含 sequence / class / state / ERD）
- **核心引擎**：Claude API（Opus 4.7 默认，Sonnet 4.6 降本）
- **无 Web UI**：CLI stdout / 文件为主

## 后续工作

spec + plan 的起草、M1 MVP 实施等均**在 FlowGen 项目 Claude Code 会话内**进行，本 Hub README 只做导航。

## 相关

- 记忆：`auto-memory: project_flowgen_init`（待建）
- Hub wiki 源摘要：[[mermaid-js-mermaid]]
- 三仓架构：[[system-overview]]
