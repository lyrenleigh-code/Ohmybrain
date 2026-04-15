---
type: exploration
created: 2026-04-14
updated: 2026-04-14
tags: [Ohmybrain, Agent-架构, Claude-Code, Hermes, 启发, 规划]
---

# Ohmybrain Agent 架构启发录

基于对 [[claude-code-best-practice]] 和 [[nousresearch-hermes-agent]] 两份参考实现的对照阅读，抽取对 Ohmybrain 本仓架构的启发。按**现在就能做 / 值得规划 / 记在本子里**分档。

## 背景

Ohmybrain 当前定位：个人知识库 + 跨项目 Hub，承载 `raw/`（只读原料）、`wiki/`（跨项目知识）、`projects/`（项目导航）。不承载项目代码。下游项目：UWAcomm / UWAnet / USBL 三个 MATLAB 工程。执行引擎：[[claude-code|Claude Code]]。

两个参考实现代表两种取向：

- **Claude Code**（Anthropic 官方）：押"官方深度集成"——IDE、订阅、`/ultraplan` 云端执行。代价是绑定 Anthropic
- **Hermes Agent**（Nous Research，MIT）：押"模型/部署/平台自由"——7 种模型接入、6 种终端后端、16 个消息平台。代价是自建运维

---

## 1. 架构层启发（值得规划）

### 1.1 Context 管理改成可插拔

**现状**：Ohmybrain 依赖用户**手动触发** `/query` 或靠 rules 写"回答前先检索 wiki"——模型遵循率不可靠。

**参考**：
- Hermes v0.9.0 新增 `plugins/context_engine/` slot，context 管理成为可替换插件
- Claude Code 通过 skill `paths:` glob 实现"访问匹配文件时自动激活"

**落地方向**：把 wiki 检索做成**每轮自动注入命中页**的 context engine（或至少 `paths: "wiki/**"` 的 skill），让知识检索从"会话行为"升级为"会话基础设施"。

### 1.2 双层架构意识

**现状**：所有约束都压在 `.claude/settings.json` 一层。

**参考**：
- Hermes 区分**主 agent hooks**（`tools/` 生命周期）和 **gateway hooks**（`gateway/hooks.py` + `gateway/builtin_hooks/`）
- Claude Code 未做此区分

**落地方向**：Ohmybrain 的"Obsidian 同步、GitHub 推送、Zotero 查询"本质上是**边界层**——未来接更多外部系统时，边界 hook 要和主循环 hook 分层，别都堆在一起。

---

## 2. 机制层启发（值得规划）

### 2.1 Command / Agent / Skill 三分

**现状**：`.claude/commands/` 下所有工作流都是 Command——无论是简单查表还是多步决策。

**参考**：三种扩展机制各有适用场景（详见 [[skills-vs-commands]]）。

**落地方向**：

| 现在（全是 Command）            | 应该是                                      | 原因                                       |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| `/ingest` 整体 Command      | Command 做入口编排 + Agent 做"读-判-分类-交叉引用"多步决策 | Agent 独立上下文不污染主会话，可配 `memory: user` 积累经验 |
| `llm-wiki.md` rule        | Skill `paths: "wiki/**"`                 | 自动激活，不再依赖规则遵循                            |
| `/promote-answer`         | 保持 Command                               | 用户显式触发的写回动作，不应自动触发                       |
| `check_raw_write.py` hook | 保留为 hook                                 | 确定性执行 > 文档规则                             |

### 2.2 agentskills.io 开放标准兼容

**参考**：Hermes 遵循 [agentskills.io](https://agentskills.io) 开放标准，26 个领域 skill 可在不同 agent 间互通。Claude Code 使用私有格式。

**落地方向**：Ohmybrain 自写 skill 时 frontmatter 尽量对齐开放标准——成本很低，收益是"不被单一 CLI 绑死"。这和 Ohmybrain 作为**跨项目 Hub 的中立立场**一致。

### 2.3 单一 CommandDef 表驱动多终端

**参考**：Hermes 用一张 `CommandDef` 列表驱动 CLI + 16 个消息平台 + autocomplete + help——加别名只需改 `aliases` 元组，其它文件零改动。

**记在本子里**：Ohmybrain 当前只有 CLI 入口，暂不需要。但未来如果做 Obsidian 插件 / Telegram bot / 任意 MCP 客户端入口——**唯一正确姿态**是单一命令表。

---

## 3. 质量层启发（现在就能做）

### 3.1 Prompt Caching Must Not Break

**参考**：Hermes AGENTS.md 把这条写成硬政策——**禁止会话中途**改上下文、改工具集、重载 memory、重建 system prompt。唯一可改的时机是 **context compression**。破坏缓存 = 成本剧增。

**检查清单**（Ohmybrain 当前实现待审查）：
- [ ] `/ingest` 是否在会话中途重建 system prompt？
- [ ] `/promote-answer` 是否会重载 memory？
- [ ] 各 skill 激活时是否改动已有工具集？

### 3.2 CLAUDE.md 长度监控

**参考**：Claude Code 团队经验——单个 CLAUDE.md **< 200 行** 时模型遵循度最高。

**当前状态**：
- `D:\Claude\CLAUDE.md` ~20 行 ✅
- `D:\Claude\Ohmybrain\CLAUDE.md` ~50 行 ✅
- 各子项目 CLAUDE.md 需监控

**注意祖先上行加载**：从 `UWAcomm/` 启动 Claude 会**同时加载** `D:\Claude\CLAUDE.md` + `D:\Claude\Ohmybrain\CLAUDE.md`（如果 Ohmybrain 在其路径上）——监控**总和**别超限。

### 3.3 硬编码路径会破坏 profile 隔离

**参考**：Hermes 为此花了 PR #3575 修 5 个 bug。所有 `~/.hermes` 路径统一走 `get_hermes_home()` 访问器，依赖 `HERMES_HOME` 环境变量。

**落地方向**：审查 Ohmybrain `scripts/` 下 Python 脚本，如有 `Path.home() / ".claude"` 的硬编码，改用环境变量 + 统一访问器。未来多开 profile 时才不出血案。

### 3.4 立即可补的 4 个 Hook

- **`PostToolUse: Write|Edit`** on `wiki/**` → 自动跑 `scripts/lint_wiki.py`
- **`PostToolUse: Write|Edit`** on `wiki/index.md` → 跑 `check_index_log_sync.py`
- **`SessionStart`** → 注入 `wiki/log.md` 最近 3 条 + 当前活跃项目
- **`Stop`** → 提示是否要 `/promote-answer` 写回 Hub

---

## 4. 远期记录（暂不动）

- **Trajectory 采集**：`trajectory_compressor.py` 给了未来微调私有小模型的路径。会话压成训练数据——现在没必要，未来值得
- **Skin engine**：每个子项目一套 banner 色/spinner——纯数据驱动，零代码改动
- **Serverless 持久化**：若 Ohmybrain 将来需要云端常驻（如定时同步），参考 Hermes 的 Modal/Daytona 模式——空闲休眠、触发唤醒

---

## 5. 关键决策

**Ohmybrain 架构向 Hermes 学，日用依赖 Claude Code。**

- **架构学 Hermes**：开放标准（agentskills.io）、插件化（context engine slot）、profile 隔离（HERMES_HOME 模式）、双层 hook
- **日用依赖 Claude Code**：Opus 4.6 + 1M context + OAuth 复用订阅

两者并不冲突——Hermes 本身支持用 Claude Code OAuth 接 Opus 4.6（`hermes model` → Anthropic → OAuth → 读 Claude Code 凭据库）。**用 Claude Code 跑日常，架构思想抄 Hermes**。

---

## 6. 优先级建议

### P0 立即可做

- [x] 补 4 个 hook（见 §3.4）——2026-04-14 完成，详见下文
- [x] 审查 `/ingest` / `/promote-answer` 是否破坏 prompt cache（见 §3.1）——/ingest 纯指令型无 cache 问题；Hub 本身无 /promote-answer（是下游项目指令）
- [x] 审查 `scripts/` 路径硬编码（见 §3.3）——仅 2 处 `~/Zotero/`，是外部工具 fixed path，不属于 profile 隔离问题，保留

### P0 实施记录（2026-04-14）

新建 3 个 hook 脚本 + 更新 `.claude/settings.json`:

| Hook 类型 | 脚本 | 行为 | 阻断 |
|----------|------|------|------|
| `PreToolUse: Edit\|Write` | `check_raw_write.py`（已有） | `raw/` 写入拦截 | 是 |
| `PostToolUse: Edit\|Write` | `post_wiki_write.py`（新建） | `wiki/**/*.md` 写后自动 `lint_wiki` | 否（仅提示） |
| `SessionStart` | `session_context.py`（新建） | 注入 log.md 最近 3 条 + 项目列表 | N/A |
| `Stop` | `check_index_log_sync.py`（已有，wire up） | wiki/ 变更则 index/log 必须同步 | 是 |
| `Stop` | `commit_reminder.py`（新建） | 有未提交 wiki/ 变更则提醒 git commit | 否 |

冒烟测试通过：3 项目检出、24 处 wiki 未提交变更识别、post-write lint 正确按 path 分流。

### Prompt Cache 审查结论（2026-04-14）

检查 `.claude/commands/ingest.md`：

- `/ingest` 是**纯指令型 Command**——告诉模型做什么，不改工具集、不重载 memory、不重建 system prompt
- 会话全程只有 Read/Write/Edit/Bash 这些常驻工具，无中途 toolset 切换
- 符合 Hermes "Prompt Caching Must Not Break" 政策

Hub 本身无 `/promote-answer` 命令（见 `ingest.md` 末尾："Hub 的 ingest 不存在向上回流"）。`/promote-answer` 是下游项目（UWAcomm/USBL/UWAnet）的指令，审查应在各项目仓内单独进行。

### Path 硬编码审查结论（2026-04-14）

`grep -rn "Path.home\|expanduser\|~/.claude" scripts/` 结果：

- `scripts/import-zotero.py:20` — `DEFAULT_ZOTERO_DIR = os.path.expanduser("~/Zotero/storage")`
- `scripts/zotero_cleanup.py:77` — `db = os.path.expanduser("~/Zotero/zotero.sqlite")`

两处都是**外部工具（Zotero 桌面应用）的固定安装路径**，非 profile-scoped state——不属于 Hermes PR #3575 修的那类 bug。保留。

### P1 本月值得做

- [x] `llm-wiki.md` rule → skill（`paths: "wiki/**"` 自动激活）——2026-04-14 完成
- [x] `/ingest` 抽出自治多步部分为 Agent——2026-04-14 完成，详见下文
- [x] `/ingest` 增加 inline / agent 路径分流 + 用户预先询问——2026-04-14 完成，详见下文（来源：[[wiki-ingester-ab-test-dingjie-2020]] 结尾新 P1-3 候选）

### P1-1 实施记录：llm-wiki rule → skill（2026-04-14）

**迁移**：
- 新建 `~/.claude/skills/llm-wiki/SKILL.md`，frontmatter 含 `paths: wiki/**`——仅在触及 wiki/ 文件时自动激活，不再污染非 wiki 会话上下文
- 原 `~/.claude/rules/common/llm-wiki.md` 改写为过渡期占位，指向新 skill 位置

**内容升级**（修复 stale 引用）：
- 老 rule 引用 `D:\Obsidian\workspace\` PARA 结构（已被 Ohmybrain 取代）
- 新 skill 对齐 Ohmybrain 实际 wiki 结构（concepts / entities / source-summaries / topics / architecture / explorations / comparisons）
- 增加 **Promote（下游 → Hub 回流）** 章节——老 rule 没有
- 明确 Hub vs 下游项目角色差异

**效果**：
- 本次会话 Claude Code 已识别到新 skill（system-reminder 列表出现 `llm-wiki`）
- 下次启动时 skill 将根据 `paths` glob 仅在处理 wiki/ 文件时加载
- 非 wiki 会话不再加载此协议内容——节省上下文

**待办**：
- 观察 1-2 周无回归后，可删除 `~/.claude/rules/common/llm-wiki.md` 占位文件（手动操作）

### P1-2 实施记录：/ingest 抽出 wiki-ingester Agent（2026-04-14）

**职责拆分**：

| 阶段 | 执行方 | 原因 |
|-----|-------|------|
| Step 1（识别/扫描 raw/） | 主会话 Command | 用户交互入口 |
| **Step 2-4（提取 / 写页 / 交叉引用）** | **wiki-ingester Agent** | 自治多步决策，独立上下文，大仓库不污染主会话 |
| Step 5（同步 index.md） | 主会话 Command | 用户可见的审计点 |
| Step 6（追加 log.md） | 主会话 Command | 变更记录用户必须看到 |
| Step 7（lint + sync check） | 主会话 Command | 最终验证 |

**新建文件**：

- `.claude/agents/wiki-ingester.md`——Agent 定义：`acceptEdits` 权限 + `inherit` 模型 + 全工具（Read/Write/Edit/Grep/Glob/Bash，hooks 兜底）
- `.claude/commands/ingest.md`——重写为编排型 Command：Step 1 + 调 Agent + Step 5-7

**输出契约**：

Agent 必须返回**结构化 markdown 报告**：元数据、新建页面列表、更新页面列表、一句话摘要（供 log.md 用）、备注（异常情况）。主会话依赖这个格式解析后做 Step 5-6。

**安全 + 审计设计**：

- 读写 raw/ 仍被 PreToolUse hook `check_raw_write.py` 拦截（对 Agent 同样生效）
- Agent 每次写 wiki/*.md 仍自动触发 PostToolUse lint
- `acceptEdits` 模式只在 Agent 内生效（autonomous），主会话权限不受影响
- Step 5-6 留在主会话——**index/log 变化用户一定看得到**，不会因为 Agent 在独立上下文就错过审计

**预期收益**：

- 摄入大代码仓（如 hermes-agent 4k commits 的情况）时，主会话上下文**不再被 README + 子目录扫描填满**
- Step 2-4 出错（slug 冲突、概念边界不清）时，Agent 独立报告，主会话决策清晰
- 未来给 Agent 加 `memory: user` 可让"摄入决策经验"跨会话积累

**待观察**：

- Agent 的"一句话摘要"质量是否稳定——若抽摘不准，主会话写进 log.md 的内容会失真
- 结构化输出契约是否可靠——若 Agent 格式漂移，主会话 Step 5-6 的解析会失败
- 若发现问题，调整 Agent prompt 中的"输出契约"段落

### P1-3 实施记录：/ingest 路径分流（2026-04-14）

**动机**：A/B 报告（[[wiki-ingester-ab-test-dingjie-2020]]）结论——新 agent 架构对长论文/大仓强（+182% 行数），但对**短笔记 / 小文章**重型 agent 划不来（~300s+ / ~124k tokens 起步）。需要在 `/ingest` 里加一层分流，短资料走主会话内联（llm-wiki skill 已经 `paths: wiki/**` 自动激活），长资料保持走 Agent。

**改动**（仅 `.claude/commands/ingest.md`，无新文件）：

| 位置 | 改动 |
|------|------|
| 架构图 | 新增 Step 1.5 + Step 2-4 分两路径 |
| 新 Step 1.5 | 规模预判表（文本 / PDF / 仓库 / 视频的 短/长 阈值 + 测量命令） + AskUserQuestion 显式询问 |
| Step 2-4 | 拆成"路径 A inline"和"路径 B agent"两小节，产出**同构的"摄入报告"契约** |
| 报告契约 | 从 Agent 专属升级为两条路径共用（元数据 / 新建页面 / 更新页面 / 一句话摘要 / 备注）——Step 5-7 机械消费无需区分路径 |
| 批量摄入 | 增加"批次统一策略"：`全部 inline` / `全部 agent 并行` / `逐个询问`；并行 agent 约束明文化（子 agent 只写 source-summary，主会话汇总后批量 cross-ref） |
| frontmatter description | 反映双路径 |

**关键设计取舍**：

- **规模预判只作默认高亮，必须始终询问**——因为"这次想快"或"这次想细"能推翻规模判断（如小笔记用户仍可能想让 agent 多挖关联）
- **报告契约两路径共用**——Step 5-7 是路径无关的，未来再加第三条路径（比如 MCP 服务化摄入）也能复用
- **批量模式的"统一策略"减少打扰**——8 份论文不用问 8 次

**预期收益**：

- 短资料处理从 `~300s+` 降到 `<30s` 主会话内联
- 长资料仍保留 agent 独立上下文保护 + 并行能力（4/14 USBL 8 篇并行已验证）
- 用户拥有路径决定权——规模阈值只是提示

**待观察**：

- 规模阈值（5k 字 / 10 页 / 15 min）是否合理——用实际使用统计调整
- AskUserQuestion 的交互体验——是否每次都默认项就够用
- 是否有资料"看起来短但其实难"需要特别标注（比如数学密集的 4 页论文）

### P2 下一阶段

- [ ] Wiki 检索做成 pluggable context engine
- [ ] Skill frontmatter 对齐 agentskills.io 标准

### P3 远期记录

- [ ] 单一 CommandDef 驱动多终端（需要新终端入口时启动）
- [ ] Trajectory 采集 + 微调私有模型
- [ ] Skin engine

---

## 相关资源

- [[claude-code-best-practice]] — Claude Code 最佳实践参考仓摘要
- [[nousresearch-hermes-agent]] — Hermes Agent 摘要
- [[subagents-orchestration]] — 三机制编排
- [[skills-vs-commands]] — 三机制决策树
- [[claude-hooks-architecture]] — Hook 架构
- [[claude-code]] — 执行引擎实体页
- [[harness-engineering]] — harness 设计基础

## 补充参考

- [[yizhiyanhua-ai-fireworks-tech-graph]] — Skill 工程化范本。在"现在就能做 Sec.3" 可追加：给 wiki-ingester agent 加 Pre-Tool-Call Checklist + Error Recovery Protocol；"值得规划 Sec.2.1" 可追加：llm-wiki 三层化（基于 [[skill-layered-resources]] 概念）。
