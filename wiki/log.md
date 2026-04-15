# 变更日志

> 记录每次对 wiki 的操作，最新的在最上面。

---

## [2026-04-15] sync | 基础设施改进下发母仓 + 3 下游项目

把本日 Hub 完成并验证的两类基础设施改进同步到 `ohmybrain-core/template` + `TechReq/{USBL, UWAcomm, UWAnet}`。

**P0（4 位置）**：
- `settings.json` 所有 hook 命令改 `python "$CLAUDE_PROJECT_DIR/scripts/xxx.py"`（消除相对路径 CWD bug，4 位置各 0 处相对路径残留）
- 新增 `scripts/raw_ingest_reminder.py`（1576 bytes，Hub 副本）+ `settings.json` 挂 `PostToolUse.Bash` matcher

**P1（3 下游）**：
- 母仓 `workflows/engineering/00-module-design.md` 回填到 USBL / UWAcomm / UWAnet——此前"先在母仓沉淀，明确后再回填"的决定，经 wiki-ingester spec 验证获得足够信心后放行

**Defer**：
- **P2 · wiki-ingester agent 下游化**——下游一般只走 `/promote-answer`，暂不建 `.claude/agents/`
- **母仓→已派生项目的增量同步机制**——本次手动同步可行但不可持续，未来需要工具化

**Hub 本仓不受影响**（Hub 早先已单独落地 P0，此次仅分发给另外 4 个位置）。

---

## [2026-04-15] validate+ingest | everything-claude-code（wiki-ingester spec 验证测试）

测试对象：`raw/repos/affaan-m-everything-claude-code`（Affaan Mustafa/MIT/黑客松冠军，v1.10.0，**1963 文件 / 20+ 子目录，比 fireworks 大 40×**）。

**验证目的**：测最新收紧的 wiki-ingester spec 预算约束在大型仓库下是否仍然生效。

**测试设计**：最小 prompt（仅 `raw_path: xxx`，无任何扩展关键词），验证默认行为。

**结果对照**：

| 指标 | fireworks 基线 | 本次 ECC | 目标 | 结果 |
|------|-------------|---------|------|------|
| 耗时 | 56 min | **7.6 min** | ≤15 min | ✅ -86% |
| Tool uses | 74 | 38 | ≤25 | ⚠️ 超目标 13 |
| Tokens | 203k | 126k | ≤80k | ⚠️ 超目标 46k |
| Summary 行数 | 383 | 205 | ≤200 | ⚠️ 超 5 行 |
| 新建 concept | 1 | 0 | 0-1 | ✅ 严守 |
| 更新页面 | 9 | 5 | ≤5 | ✅ 卡在上限 |

**遵守的约束**：不新建 concept ✓ / 更新页数 ≤5 ✓ / 大幅减少耗时 ✓

**违规（spec 约束没挡住）**：agent 在 4 个已有 concept/entity 页**都加了 `## H2` 级新小节**（"生产级规模化范本" / "规模化工程实践：ECC 48 agents 生态" / "生产级验证：ECC 的 Skills-First 策略" / "运行时门控扩展：ECC Hook Profile"），违反 spec 的"不加新小节"硬约束——本应只追加 wikilink 行。

**产出**：
- 新建 `source-summaries/affaan-m-everything-claude-code.md`（205 行）
- 更新 4 个已有页（加 H2 小节 + 追加 wikilink）—— **应该只追加 wikilink**

**初步结论**：耗时约束有效（-86%），结构约束（不加小节）**仍需进一步强化**——spec 的措辞歧义或软约束强度不足。下一步候选：把"不加小节"改为绝对禁令 + 动作后自检。

更新 index.md（45 → 46）。

---

## [2026-04-15] ingest | fireworks-tech-graph（Claude Code Skill 工程化范本）

用 `/ingest` 新架构（Step 1.5 询问→选 agent→wiki-ingester 独立上下文执行 Step 2-4）摄入 `raw/repos/yizhiyanhua-ai-fireworks-tech-graph`（yizhiyanhua-ai/MIT/npm v1.0.4，7 视觉风格 + 14 图类型的 SVG 生成 skill）。

**产物**：
- 新建 `source-summaries/yizhiyanhua-ai-fireworks-tech-graph.md` — 7 条可迁移模式（三层资源 / 触发关键词 / Pre-Tool-Call Checklist / Error Recovery Protocol / UML 映射表 / npm 打包 / 多 runtime 兼容）
- 新建 `concepts/skill-layered-resources.md` — 三层资源分离作为独立概念（fireworks 正例 + Ohmybrain `llm-wiki` 当前反例）
- 追加 wikilink 到 7 个已有页（`skills-vs-commands` / `claude-hooks-architecture` / `subagents-orchestration` / `entities/claude-code` / `source-summaries/claude-code-best-practice` / `source-summaries/nousresearch-hermes-agent` / `explorations/ohmybrain-agent-architecture-insights`）

**Defer**：未新建 `skill-packaging` concept——单源（仅 fireworks）且 Ohmybrain 暂无打包需求。

**摄入过程发现的 harness bug**（由 agent 诚实报告）：`.claude/settings.json` 里 `python scripts/check_raw_write.py` 用相对路径——CWD 在子仓时找不到脚本。下文另一 log 条目处理。

更新 index.md（43 → 45）。

---

## [2026-04-15] spec | wiki-ingester 预算与默认行为约束

基于 fireworks-tech-graph 摄入超预算事后检视（56 min / 74 tool uses / 203k tokens / 383 行 summary，vs dingjie 基线 6 min），收紧 `.claude/agents/wiki-ingester.md` spec（133 → 187 行）+ 同步 `.claude/commands/ingest.md`：

**新增约束**：
- **输出预算**：默认 summary ≤200 行 / 核心观点 5-8 条 / 启发 6-10 条 / 更新 ≤5 页
- **阅读预算**：repo 默认只读 README + 顶层 tree + SKILL/package 前 100 行；不读 `references/*` / `templates/*` / `scripts/*` 正文
- **交叉引用默认**：仅在已有页"来源"段追加一行 `[[slug]]`，**禁止**擅自加"## 小节"或修改段落
- **新建 concept/entity**：默认不擅建，走"备注提案"路径等主会话决策

**扩展通道**（user_intent 关键词显式授权）：`depth: full` / `new_concepts_ok` / `new_entities_ok` / `allow_new_sections` / `allow_paragraph_edit` / `wide_cross_ref`

**把反例写进 spec**：Step 4 明文记录 fireworks 越界案例 + 预期降幅（56 min → 10-15 min），用具体数字而非抽象约束来锚定 agent 行为。

**未做**（候选更大改造，见 P1+ 候选）：分阶段 agent（summary-agent + cross-ref-applier ×N 并行）。先观察 spec 级改进是否足以逼住越界。

---

## [2026-04-15] fix | Hook 脚本改绝对路径 + 新增 raw/ ingestion 检测

修复两个 harness 监督盲区：

**① Hook 脚本相对路径问题**：`.claude/settings.json` 所有 hook 命令从 `python scripts/xxx.py` 改为 `python $CLAUDE_PROJECT_DIR/scripts/xxx.py`，避免 CWD 切换（如 Bash `cd raw/repos/xxx`）后 hook 找不到脚本。

**② 新增 `raw_ingest_reminder.py`（PostToolUse on Bash）**：检测 `git clone` / `curl -o raw/` / `wget -P raw/` / `cp/mv ... raw/` 等命令触及 `raw/` 的场景，stdout 提醒"raw/XXX 已新增，建议运行 `/ingest raw/XXX`"。动机：本次对话中"把这个项目放到 raw 中"用 `git clone` 扩充 raw/ 未触发 `/ingest`——自然语言 ≠ 显式命令，现在靠 hook 兜底。

---

## [2026-04-14] P1-3 | /ingest 路径分流（inline vs agent 二选一）

给 `/ingest` 加 Step 1.5：处理前**预判资料规模**（文本 < 5k 字 / PDF < 10 页 / 仓库模块数 / 视频 < 15 min）+ 通过 AskUserQuestion 询问用户选 **inline 主会话内联** 还是 **agent 委托 wiki-ingester**。两条路径产出**同构的"摄入报告"契约**，Step 5-7 机械消费、路径无关。批量模式支持"统一策略"（全部 inline / 全部 agent 并行 / 混合逐个询问）。

动机来自 A/B 报告 [[wiki-ingester-ab-test-dingjie-2020]] 结尾："新 agent 架构对短资料 ~300s+ / ~124k tokens 起步不划算"——需要一层规模分流。规模阈值只作默认高亮，**始终显式询问**，让用户保留"这次想快"或"这次想细"的决定权。

**改动**：仅 `.claude/commands/ingest.md`（无新 agent/skill/script） + 本仓 `wiki/explorations/ohmybrain-agent-architecture-insights.md` 追加 §P1-3 实施记录。

---

## [2026-04-14] batch-ingest | USBL 项目剩余 8 篇论文并行摄入

用新架构 `wiki-ingester`（本会话 general-purpose 模拟）并行处理 USBL 项目 raw/papers/ 下剩余 8 篇中文博士/期刊论文。主会话做 Step 1（任务分发）和 Step 5-7（批量 cross-ref + index/log + lint）。

**并行约束设计**：8 个 agent 只写自己的 source-summary，**不**编辑 concept/index/log，cross-ref 提案在返回报告中；主会话批量应用——成功避免 race condition。

**新建 8 个 source-summary**：
- `hexutao-usbl-quad-array` — 改进四元立体阵 + EKF 降噪（何旭涛等 2025 期刊）
- `guoyu-2024-lie-group-nav` — 李群 SINS/DVL/USBL 组合（郭瑜博士 2024）
- `liufeng-2024-passive-localization` — 被动定位 + 因子图（刘峰博士 2024）
- `zhengcuie-usbl-docking` — AUV 对接三段式（郑翠娥博士 ~2007-2010）
- `yangbaoguo-2013-usbl-calibration` — 观测方程三性质校准（杨保国博士 2013）
- `quzhenzhao-2024-usbl-precision` — 五元阵多构型融合（蘧振超等 2024 短文）
- `huangjian-2019-lbl-usbl` — LBL/USBL 组合六技术（黄健博士 2019）
- `yumin-2006-lr-usbl` — 国内首代 LR-USBL（喻敏博士 863 项目 2006）

**批量更新 7 个 concept**：
- `usbl-positioning`（+8 wikilink，共 9 篇溯源完整）
- `mimo-and-array-processing`（+8 wikilink）
- `signal-processing-fundamentals`（+9 wikilink，首次建立论文溯源）
- `mathematical-optimization`（+5 wikilink，首次建立论文溯源）
- `channel-estimation-and-equalization`（+3 wikilink）
- `message-passing-algorithms`（+1 wikilink，刘峰因子图）
- `time-varying-channel`（+1 wikilink，黄健移动场景）

**未新建 concept**（3 个候选 defer）：
- `lie-group-navigation`（仅 guoyu 一个源，待积累）
- `passive-acoustic-localization`（仅 liufeng 一个源）
- `lbl-positioning`（仅 huangjian 一个源）
- `integrated-acoustic-navigation`（7 篇涉及但主题过泛，暂不抽）

**并行成本**：8 agent 同时跑，~700s 总耗时（最慢的 huangjian/liufeng ~670s），总 ~1M subprocess tokens，主会话只收到 8 份 ~200 行报告。

**观察 / 发现**：
- hexutao 实为 2025 期刊短文（非博士论文），slug 保留原命名
- zhengcuie PDF OCR 后年份信息缺失，frontmatter 保守标"~2007-2010"
- yumin PDF 为扫描件无 text layer，agent 依赖 USBL 项目版参数表 + 项目 lit-review 构造摘要（诚实报告），事实面准确
- 多个 agent 自发用 PyMuPDF 命令行绕过 Claude Code pdftoppm 失败问题，经验一致
- 多个 agent 指出可能新建 concept 但主动判断"单源不足，defer"——判断力符合策划者预期

更新了 `index.md`（页面总数 35 → 43），9 篇论文完整溯源到 Hub。

---

## [2026-04-14] explore | 新架构 A/B 对比报告

基于丁杰 2020 论文实测结果（上一条日志），撰写完整 A/B 对比分析：`explorations/wiki-ingester-ab-test-dingjie-2020.md`。

- **定量**：行数 +182%，核心章节 +80%，跨项目启发 +167%
- **定性**：新产出保留数学公式与 9 行商用设备表；"启发"分项目/Hub 两层；诚实报告 PDF 编码处理问题
- **架构验证**：Agent 独立上下文不污染主会话（124k tokens 隔离）、输出契约稳定、Hook 兜底有效、交叉引用判断合理
- **代价**：350s / 124k tokens——对长论文/大仓值得，对小资料不划算
- **反馈**：发现 spec 可优化点（"核心观点"结构应明文要求，agent 这次靠运气做对了）

更新了 `index.md`（页面总数 34 → 35）。

---

## [2026-04-14] ingest+test | 丁杰 2020 USBL 博士论文（wiki-ingester 新架构首次实测）

首次用新架构（wiki-ingester Agent 在独立上下文做 Step 2-4，主会话做 Step 1 & 5-7）摄入一篇博士论文。由于本会话 Claude Code agent 清单在启动时已快照，新 `wiki-ingester` 未注册——改用 `general-purpose` agent 内联 spec 模拟（等效行为，次会话原生可用）。

- **新建 source-summary**：`source-summaries/dingjie-2020-compact-usbl.md`（127 行，含商用 USBL 设备参数表 9 行 + 3 项方法的数学描述 + 8 条跨项目启发）
- **更新 concepts**：`concepts/usbl-positioning.md`（追加 `[[dingjie-2020-compact-usbl]]` 到来源段）、`concepts/mimo-and-array-processing.md`（追加同上）
- **未新建 concept**：基线分解法未独立成 concept，原因见 source-summary 摘要（与 usbl-positioning 强耦合，避免孤岛页）

与老处理（USBL 项目 wiki 的 dingjie-2020-compact-usbl.md，45 行）对比：新架构产出更细致（+182%），保留了数学推导与原表，但体现 Hub 跨项目视角而非项目集成视角。详细对比见后续探索页。

更新了 `index.md`（页面总数 33 → 34）。

---

## [2026-04-14] P1-2 | /ingest 抽出 wiki-ingester Agent

将 `/ingest` Command 中 Step 2-4（提取 / 写页 / 交叉引用）委托给新建 `wiki-ingester` 子代理。主会话只做 Step 1（扫描入口）和 Step 5-7（index/log 同步 + lint）。独立上下文保护主会话不被大仓库 README 填满；index/log 变化保留在主会话确保用户审计可见。

新建文件：
- `.claude/agents/wiki-ingester.md` — Agent 定义（acceptEdits + inherit model + 结构化输出契约）
- `.claude/commands/ingest.md` — 重写为编排型 Command（Step 1 → 调 Agent → Step 5-7）

同步更新 `explorations/ohmybrain-agent-architecture-insights.md` P1-2 `[x]` + 实施记录。

---

## [2026-04-14] P1-1 | llm-wiki rule → skill 迁移

将全局 `~/.claude/rules/common/llm-wiki.md` 迁移为 skill `~/.claude/skills/llm-wiki/SKILL.md`，带 `paths: wiki/**` 自动激活。顺便修复老 rule 中的 stale DocHub/`D:\Obsidian\workspace` PARA 引用，对齐 Ohmybrain 当前 wiki 结构，新增 Promote 章节。老 rule 改为过渡期占位，验证无回归后可手动删除。本会话 Claude Code 已识别到新 skill。

同步更新 `explorations/ohmybrain-agent-architecture-insights.md` P1 第一项为 `[x]` + 实施记录。

---

## [2026-04-14] P0 | 补 hook + cache/path 审查

完成架构启发录 P0 三项：

- 新增 3 脚本 + 1 settings.json 改动：`post_wiki_write.py`（PostToolUse，wiki/ 自动 lint 非阻断）、`session_context.py`（SessionStart，注入最近 3 条 log + 项目列表）、`commit_reminder.py`（Stop，wiki 未提交提醒）；并把已有 `check_index_log_sync.py` 接入 Stop hook
- Cache 审查：`/ingest` 纯指令型、无 toolset 切换、无 memory 重载——符合 "Prompt Caching Must Not Break"
- Path 审查：scripts/ 仅 2 处 `~/Zotero/` 硬编码，属外部工具 fixed path，保留

同步更新 `explorations/ohmybrain-agent-architecture-insights.md` P0 三项为 `[x]`。

---

## [2026-04-14] create | Ohmybrain 架构启发录

基于 [[claude-code-best-practice]] + [[nousresearch-hermes-agent]] 对照阅读，创建 `explorations/ohmybrain-agent-architecture-insights.md`——分 4 档（架构层 / 机制层 / 质量层 / 远期）+ 4 级优先级（P0 立即可做 / P1 本月 / P2 下一阶段 / P3 远期）。核心判断：**架构向 Hermes 学（开放、插件化、profile 隔离），日用依赖 Claude Code（Opus 4.6 + 1M + OAuth）**。

更新了 `index.md`（页面总数 32 → 33）。

---

## [2026-04-14] ingest | Hermes Agent 开源代理

对 `raw/repos/hermes-agent`（Nous Research，MIT，v0.9.0 / tag `v2026.4.13`）执行 ingest，创建 1 个新 summary + 更新 3 个概念页：

- **1 个 source-summary 页**：`source-summaries/nousresearch-hermes-agent.md` — Hermes Agent 全景，含 10 个可借鉴模式（单一 CommandDef 驱动多终端 / Prompt Caching 硬约束 / HERMES_HOME profile 隔离 / token lock / tool schema 禁跨引 / agent-level 工具拦截 / 可插拔 context engine / 6 终端后端 + serverless / gateway hooks / RL trajectory 采集）与 Claude Code 对比表 + 6 项对 Ohmybrain 的连接点
- **更新 3 个概念页**（追加 Hermes 作为同范式另一实现的参考段落）：
  - `concepts/subagents-orchestration.md` — `delegate_tool` 对比
  - `concepts/skills-vs-commands.md` — agentskills.io 开放标准
  - `concepts/claude-hooks-architecture.md` — gateway hooks 双层架构

更新了 `index.md`（页面总数 31 → 32）。

---

## [2026-04-14] ingest | Claude Code 最佳实践参考仓

对 `raw/repos/claude-code-best-practice`（shanraisshan 维护，对标 v2.1.101）执行深度 ingest，创建 4 个新 wiki 页面 + 更新 1 个实体页：

- **1 个 source-summary 页**：`source-summaries/claude-code-best-practice.md` — 整仓摘要，含三机制对比、配置优先级、MCP 推荐、Agent Memory、Tasks、Agent Teams、对 Ohmybrain 的启示
- **3 个概念页**：
  - `concepts/subagents-orchestration.md` — 子代理 16 字段 frontmatter + Command→Agent→Skill 编排 + 天气示例 + Agent Teams
  - `concepts/skills-vs-commands.md` — 三机制决策树 + 解析优先级 + "当前时间" 示例 + frontmatter 对照
  - `concepts/claude-hooks-architecture.md` — 15 个生命周期事件 + 作用域层级 + Boris Cherny hook 用法 + 对本仓候选 hook
- **更新 1 个实体页**：`entities/claude-code.md` — 追加三种扩展机制、Agent Memory、Tasks 能力段落，链到新 concept 和 summary

更新了 `index.md`（页面总数 27 → 31）。

---

## [2026-04-13] promote | USBL 定位知识回流

从 USBL 项目 (`D:\Claude\TechReq\USBL`) 回流跨项目知识：

- **新建概念页**：`concepts/usbl-positioning.md` — USBL 技术链路、六层研究体系、商用设备参数表、关键工程经验
- **更新概念页**：`concepts/mimo-and-array-processing.md` — 追加 USBL 阵列处理交叉引用
- **来源**：USBL 项目 9 篇论文文献综述

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
