---
type: concept
created: 2026-05-24
updated: 2026-06-09
tags: [术语, glossary, 工作流]
---

# 工作流术语表

跨项目工作流相关术语的中文 / 英文 / 缩写定义。这里是 single source of truth，其他文档引用。

> 计数口径以 `[[../architecture/system-overview]]` 与 index/log 为准（如 wiki 共 109 个 .md、本地 skill 32 含 SKILL.md / 注入后 90+、agents 55 个等），术语表只描述概念不复述统计。

## 核心动词（来自 [[../architecture/dual-loop]]）

| 英文 | 中文 | 含义 | 闭环位置 |
|------|------|------|---------|
| `ingest` | 摄入 | 把 raw/ 资料转化为 wiki/source-summaries/ 条目 | knowledge 闭环 step 01 |
| `query` | 查询 | 用户领域问题，主会话查 Hub wiki + memory | knowledge 闭环 step 02 |
| `promote` | 回流 / 上汇 | 跨项目可复用结论从 project → Hub | knowledge 闭环 step 03 |
| `review` | 复盘 | 定期审 wiki/log.md，整理 / 触发新 ingest | knowledge 闭环 step 04 |
| `spec` | 任务规约 | 单职责任务定义，目标 / 范围 / verification | engineering 闭环 step 01 |
| `plan` | 计划 | 复杂任务的分阶段实现计划 | engineering 闭环 step 02 |
| `implement` | 实施 | 写代码 + commit | engineering 闭环 step 03 |
| `validate` | 验证 | 业务指标验证 + 用户终审 | engineering 闭环 step 04 |
| `archive` | 归档 | 完成的 spec 从 `specs/active/` → `specs/archive/` | engineering.validate 之后的整理动作 |

## 算法研究核心术语（工作流维度）

| 术语 | 含义 | 来源 |
|------|------|------|
| **V→V→V 递进** | 逐版闭环迭代（每个 V = 一次完整 RCA + fix + verify），不跳号、不并行 | UWAcomm 工作流 |
| **PMF 双指标** | "过版"判定双标准：① 上一 V RCA 完成 ② 5 项回归 test 全通过 | Anthropic Founder's Playbook 创业 PMF 类比 |
| **单根因审计** (Single Root Cause Audit) | D9/D10 toggle 开关 + 跨 runner audit 把症状定位到单一根因，拒绝多根因混淆 | `feedback_single_root_cause_audit`，限 MATLAB 算法 RCA 不外推 |
| **plan C 时变证伪** | RCA 反例：把"信道时变性"作为假根因绕过单一函数 fix 的 anti-pattern | 同上 memory 条目 |
| **RCA** | Root Cause Analysis 根因分析。**不是 engineering 闭环的 4 步之一**，而是 `validate` 失败时进入的**子环节**：找单一根因 → fix → 重新 validate。配合 V→V→V，每个 V = 一次完整 RCA + fix + verify。 | 算法工作流通用 |
| **过版 / passing version** | 通过 PMF 双指标，进入下一 V 的判定 | 与 V→V→V 配套 |

## 算法领域名词（中英文 + 缩写）

> UWA 仿真各 scheme 与指标的统一缩写定义。物理细节见各 [[../concepts/...]] 专页，此处只给一句定义供工作流文档引用。

| 术语 | 英文全称 / 缩写 | 一句定义 | 详见 |
|------|------|------|------|
| **NMSE** | Normalized Mean Square Error 归一化均方误差 | 信道估计 / 重构误差的归一化指标，越小越好；常用 dB 表达 | [[channel-estimation-and-equalization]] |
| **BER** | Bit Error Rate 误码率 | 解调后错误比特占比，端到端性能终判指标 | [[signal-processing-fundamentals]] |
| **CFO** | Carrier Frequency Offset 载波频偏 | 收发载波不一致导致的相位旋转，需估计补偿（post-CFO fix 是 SC-TDE 关键步） | [[doppler-estimation-methods]] |
| **GAMP** | Generalized Approximate Message Passing 广义近似消息传递 | 压缩感知信道估计的消息传递求解器，高 SNR 易发散需 fallback | [[message-passing-algorithms]] |
| **OMP** | Orthogonal Matching Pursuit 正交匹配追踪 | 贪婪稀疏恢复算法，逐次选原子重构稀疏信道 | [[mathematical-optimization]] |
| **jakes 模型** | Jakes Doppler Model | 经典多普勒功率谱 / 时变衰落信道仿真模型，UWA 用其 passband-native 变体（Hilbert+SoS） | [[time-varying-channel]] |
| **preamble** | 前导 / 训练序列 | 帧头已知序列，用于同步、信道估计与 α 估计（training preamble 是 SC-FDE 架构关键） | [[signal-processing-fundamentals]] |
| **passband / baseband** | 通带 / 基带 | 通带为含载波实信号，基带为复包络；passband real time-scaling 等效同时反载波相位，baseband 需手动补 `exp(-j·2π·fc·α·t)` | `feedback_comp_resample_carrier_phase` |
| **SC-FDE** | Single-Carrier Frequency-Domain Equalization 单载波频域均衡 | 单载波 + 频域均衡体制，UWA 多普勒鲁棒主力之一（pilot=blk_cp 是 jakes fd=1Hz 关键突破） | [[ofdm-and-otfs]] |
| **OTFS** | Orthogonal Time Frequency Space 正交时频空 | 时延-多普勒域调制，对高多普勒鲁棒；含 rx_chain / spread-pilot / clip-PAPR 三模块 | [[ofdm-and-otfs]] |
| **DSSS** | Direct-Sequence Spread Spectrum 直接序列扩频 | 扩频码增益换抗干扰，低速可靠链路（Sun-2020 参考实现） | [[underwater-acoustic-communication]] |
| **OFDM** | Orthogonal Frequency-Division Multiplexing 正交频分复用 | 多载波并行传输，对抗多径但对多普勒 / CFO 敏感 | [[ofdm-and-otfs]] |
| **α（多普勒尺度因子）** | Doppler Scale Factor | 收发相对运动引起的时间伸缩比，UWA 宽带不可近似为纯频偏；RX 端按 α 符号方向重采样补偿 | [[doppler-estimation-methods]] |

## Claude Code 协作术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **三表面** (Three Surfaces) | Chat（频次最高补充）/ Cowork（中频协作）/ Code（核心实现） | Anthropic Founder's Playbook |
| **agentic 技术债** | 多 worktree 漂移、不周期性集成产生的合并债 | worktree 三路隔离实践（见下「仓 / 项目层级术语」） |
| **代下结论 反模式** | Claude 自主下"work / 完成 / 闭环"判断，本应用户做 | `feedback_uwacomm_testing_boundary` |
| **subagent / 子代理** | 在**独立上下文窗口**中运行的自治代理，可被主 Claude 自动调用（PROACTIVELY）或显式调用；上下文 / 工具 / 模型 / 记忆均隔离 | [[subagents-orchestration]] |
| **orchestrator / 编排器** | 主会话作为协调者，分发子任务给 subagent 并汇总结果，自身不深入实现 | [[subagents-orchestration]] |
| **general-purpose 替身** | 项目本地 `.claude/agents/*.md` 不在 `subagent_type` 列表时，用 general-purpose 通用代理 + 内联契约顶替 | `feedback_project_local_agent_not_invocable` |
| **Task 并行 / fan-out 扇出** | 同一消息内发起多个独立 Task 调用并行执行（扇出），独立操作一律并行而非顺序 | `~/.claude/rules/common/agents.md` |
| **Skill** | 带 frontmatter + 工作流决策树的可触发能力包，按 `description` / 关键词激活，加载 SKILL.md 入上下文 | [[skills-vs-commands]] |
| **MCP** | Model Context Protocol，外部工具 / 资源接入协议（context7 / exa / github / memory / playwright / sequential-thinking 等通过 `mcp__plugin_ecc_*` 调用） | Claude Code |
| **渐进披露** (progressive disclosure) | Skill / wiki 按 `入口 → 参考 → 资产` 三层逐步打开，只在需要时 Read，避免一次性全量注入 | [[skill-layered-resources]] |
| **三层渐进披露**（wiki 版） | 查 wiki 时按 `index → log → 详` 三层逐步打开，每次 Read ≤3 页 | claude-mem 启发 |
| **context window 管理** | 控制上下文占用：避免最后 20% 做大重构，子代理隔离上下文，渐进披露按需加载 | `~/.claude/rules/common/performance.md` |
| **Workflow 编排** | 由编排脚本 / 主会话按阶段调度 subagent + Skill + Task，串并联组合成多步流程 | [[subagents-orchestration]] |
| **5 层 memory 栈** | Global CLAUDE.md / Project CLAUDE.md / auto-memory / MCP graph / Hub wiki | [[../architecture/memory-stack]] |

## Hub 专有动词 / 名词

| 术语 | 含义 | 来源 |
|------|------|------|
| **promote-answer** | `/promote-answer` 命令，把对话中产生的跨项目可复用结论回流 Hub wiki（= knowledge 闭环 promote 的命令入口） | [[../architecture/dual-loop]] |
| **sync-to-core** | `/sync-to-core` 命令，把 Hub / 项目沉淀的通用约定同步回 ohmybrain-core 母仓模板；queue 须先 diff 再决定，trivial / 已同步 / 反向都要标 | `feedback_sync_to_core_lessons` |
| **ingest** | 把 raw/ 资料摄入为 wiki/source-summaries/ 条目（knowledge 闭环 step 01，亦有 `/ingest` 命令） | [[../architecture/dual-loop]] |
| **dedicated 页** | Hub wiki 中为单一实体 / 概念 / 项目专设的独立页面（如 mcp-entities/ 下每个 MCP 一页），对应 SSOT 颗粒度 | [[../architecture/hub-as-brain]] |
| **worktree 分身** | `git worktree` 派生的并行工作目录，与主仓隔离用于自主迭代 / 并行实验（如 UWAcomm-claude / UWAcomm-codex） | `feedback_uwacomm_worktree_ownership` |

## flowgen 8 子 skill 术语（流程图 / 体系图生成）

> 所有方案 / 方法论文档的图必须走以下 8 个 flowgen* skill 之一，按决策树分流，禁止 matplotlib mock / 手画 SVG（见 memory `feedback_doc_flowgen_only`）。

| 子 skill | 一句用途 |
|------|------|
| **flowgen** | 自然语言 → Mermaid flowchart（轻量文本图，内置语法子集 + few-shot + validate 兜底） |
| **flowgen-vsdx** | 自然语言 → Visio .vsdx 节点+连线流程图（M4，FlowSpec JSON + GraphViz 自动布局） |
| **flowgen-layered** | 自然语言 → Visio .vsdx 分层架构图（M5，自上而下层带 + 左侧竖排标签栏 + PPT 商务风） |
| **flowgen-sequence** | 自然语言 → Visio .vsdx UML 时序图（lifeline + 消息交互，actor ≤ 12，color/bw 两风格） |
| **flowgen-composition** | 自然语言 → Visio .vsdx 系统组成图（纯 contains 嵌套，2-4 层系统→分系统→模块，无连线） |
| **flowgen-roadmap** | 自然语言 → Visio .vsdx 项目立项 / 课题论证路线图（A4 竖版 5 段 + 三段式应用-问题-研究总览） |
| **flowgen-archposter** | 自然语言 → Visio .vsdx 四化五层体系架构挂图（军规 / 民国挂图风，A3 横 / 竖双形态 + 四化纵贯审计） |
| **flowgen-replica** | 图片（PNG/JPG）→ Visio .vsdx 骨架复刻（多模态识图后重建可编辑 .vsdx，唯一图片输入入口） |

## 仓 / 项目层级术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **Hub / 大脑** | Ohmybrain 本仓，知识中枢 | [[../architecture/three-tier-architecture]] |
| **核心 / core** | ohmybrain-core 母仓，被动模板 | 同上 |
| **项目仓 / project-*** | UWAcomm / USBL / DocProcess/* 等业务驱动方 | 同上 |
| **worktree 三路隔离** | main（用户主导）/ exp（Claude 自主）/ dev（Codex 并行）三路 worktree | `feedback_uwacomm_worktree_ownership` |
| **派生 / derive** | 按项目类型复制 `ohmybrain-core/template-engineering/`、`template-document/` 或 `template-tool/` 新建项目 | new-project-sop.md |

## 反模式 / 行为约束术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **confirmation bias** | 问 Claude 找支持已有信念的证据，Claude 顺着走 | [[anti-patterns]] |
| **scope creep** | 实施时偷偷加 spec 未定义需求 | 同上 |
| **disconfirming evidence** | 反向证据，挑战已有信念的事实 | 同上 |

## hooks / 自动化术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **PreToolUse hook** | 工具调用前拦截（如 `check_raw_write.py`） | [[claude-hooks-architecture]] |
| **PostToolUse hook** | 工具调用后触发（如 `post_wiki_write.py`） | 同上 |
| **Stop hook** | 会话结束时检查（如 `check_index_log_sync.py`） | 同上 |
| **SessionStart hook** | 会话开始注入上下文（如 `session_context.py`） | 同上 |

## 文档 / wiki 术语

| 术语 | 含义 | 来源 |
|------|------|------|
| **single source of truth (SSOT)** | 一个事实只在一处定义，其他地方引用 | [[../architecture/hub-as-brain]] |
| **wikilink** | `[[slug]]` 跨页引用语法（Obsidian 兼容） | wiki 规则 |
| **frontmatter** | YAML metadata 头部（type / created / updated / tags） | 同上 |
| **ADR** | Architecture Decision Record 架构决策记录；Hub 中以章节形式（ADR-001~030）存放于 [[../architecture/decision-log]]，引用一律链 decision-log 而非悬空 ADR-N | [[../architecture/decision-log]] |

## 相关页面

- [[../architecture/dual-loop]] — 双闭环动词的来源
- [[anti-patterns]] — 反模式合集（含 anti-pattern 术语）
- [[../architecture/hub-as-brain]] — 大脑功能定位
- [[../architecture/memory-stack]] — 5 层 memory 栈详细
- [[subagents-orchestration]] — subagent / orchestrator / 编排术语来源
- [[skill-layered-resources]] — 渐进披露 / Skill 三层资源来源
- [[../architecture/decision-log]] — ADR-001~030 章节存放处
