---
type: architecture
created: 2026-04-12
updated: 2026-06-09
tags: [架构, 三仓, Hub, 模板, 闭环, harness]
---

# 系统架构总览

## 定位

Ohmybrain 体系采用**三仓架构**：**Hub (大脑 · 主动)** + **project-* (需求牵引 · 业务驱动)** + **ohmybrain-core (被动模板)**。

**哲学**（详见 [[three-tier-architecture]]）：

- **Ohmybrain (本仓) = 大脑**：知识沉淀、决策、模板演化的中枢
- **项目 = 需求牵引**：实际业务在此发生，是整个生态的演进驱动力
- **ohmybrain-core = 被动模板**：项目模板存储，由 Hub 主动更新

> ⚠️ core 不是"源头"，Hub 才是。core 只是 Hub 把成熟模式打包供新项目复用的副本。

事实源：[[three-tier-architecture]]（哲学澄清） + [[ohmybrain-three-tier-seed]]（设计笔记）+ 本仓根 `CLAUDE.md`。

> **演化历史**：早期（2026-04-12 前）曾是 *"LLM Wiki + 开发工程 + Claude Code Harness 一体化单仓"* 设计（见 [[my-brain-setup-plan]] / `raw/notes/agent_knowledge_repo_template.md`），后拆分为本文档描述的三仓结构；2026-05-24 哲学澄清为 Hub 主动 + project 牵引 + core 被动。

## 三仓结构

```
┌────────────────────────────────┐       复制派生       ┌──────────────────────┐
│  ohmybrain-core (被动模板)      │ ─────────────────→  │  project-*           │
│  ├ template-engineering/       │  cp -r template-*/  │  子项目仓（自包含）    │
│  ├ template-document/      🔒  │                      │  D:\Claude\<area>\   │
│  └ template-tool/              │                      │  按类型分 3 area     │
│  D:\Claude\ohmybrain-core      │                      │  TechReq/DocProcess/ │
└────────────────────────────────┘                      │  Tools/              │
       ↑                                                 └──────────┬───────────┘
       │ Hub 主动 update                                              │
       │ template-*/                                                  │ /promote-answer
       │ (通道 3 延迟)                                                 ↓
┌──────────────────────────────────────────────────────────────────────────────┐
│  ohmybrain (Hub · 大脑·主动)                                                  │
│  ├ wiki/ 跨项目知识 + 决策                                                    │
│  ├ projects/ 项目导航                                                         │
│  └ 通过 ~/.claude/ 全局层实时指导所有 project (通道 1)                          │
│  D:\Claude\Ohmybrain                                                          │
└──────────────────────────────────────────────────────────────────────────────┘
```

> **2026-05-24 拆分**：原 `template/` 拆为 3 模板对应 3 类项目（engineering / document / tool）。详见 [[project-types]]。

### 当前实例

| 角色 | 仓库 | 本地路径 | 状态 |
|------|------|---------|------|
| 母仓 | `ohmybrain-core` | `D:\Claude\ohmybrain-core` | 活跃 |
| Hub | `ohmybrain`（本仓） | `D:\Claude\Ohmybrain` | 活跃 |
| **TechReq/** | | | **水声通信算法仿真** |
| 项目仓 | `UWAcomm` | `D:\Claude\TechReq\UWAcomm` | 活跃开发（MATLAB 6 体制） |
| 项目仓 | `USBL` | `D:\Claude\TechReq\USBL` | 活跃开发 |
| 项目仓 | `UWAnet` | `D:\Claude\TechReq\UWAnet` | 前期调研 |
| 项目仓 🔒 | `UWAcomm_usbl` | `D:\Claude\TechReq\UWAcomm_usbl` | 派生 2026-04-25，内网 Internal（UWAcomm+USBL 联合仿真） |
| 项目仓 🔒 | `SonarSim` | `D:\Claude\TechReq\SonarSim` | 派生 2026-06-03（主动声呐界面仿真，MATLAB App Designer，手动模式） |
| **DocProcess/** 🔒 | | | **文档处理工作区，全部私人项目** |
| 项目仓 🔒 | `Pricing` | `D:\Claude\DocProcess\Pricing` | 活跃（军用软件四号文报价） |
| 项目仓 🔒 | `UWAprojDoc` | `D:\Claude\DocProcess\UWAprojDoc` | 派生 2026-04-28（水声专项方案技术文档撰写） |
| 项目仓 🔒 | `CooperativeDetection` | `D:\Claude\DocProcess\CooperativeDetection` | 派生 2026-05-08（水下分布式协同探测 4 专题 12 课题） |
| 项目仓 🔒 | `PaperReview` | `D:\Claude\DocProcess\PaperReview` | 派生 2026-05-09（学位论文外审） |
| 项目仓 🔒 | `DigitalTwinGuide` | `D:\Claude\DocProcess\DigitalTwinGuide` | 派生 2026-05-13（数字孪生项目实施指南方法论） |
| 项目仓 🔒 | `DigitalTwin1plusN` | `D:\Claude\DocProcess\DigitalTwin1plusN` | 派生 2026-05-25（「1+N」集群数字孪生体系） |
| 项目仓 🔒 | `VisioForge` | `D:\Claude\DocProcess\VisioForge` | 派生 2026-06-02（通用 Visio 出图工作区，复用 flowgen-* 8 skill） |
| 项目仓 🔒 | `CooperativeASW` | `D:\Claude\DocProcess\CooperativeASW` | 派生 2026-06-03（UWAprojDoc 编队协同探潜分系统单列细化 docx，DEPENDS_ON=UWAprojDoc） |
| **Tools/** | | | **跨项目工具** |
| 项目仓 | `FlowGen` | `D:\Claude\Tools\FlowGen` | 派生 2026-04-23（自然语言→Visio/Mermaid 出图工具族；flowgen-* Visio skill 活跃，Mermaid 主入口未实装） |
| 项目仓 | `IconForge` | `D:\Claude\Tools\IconForge` | 派生 2026-05-29（自然语言→图标 SVG，未实装） |
| 项目仓 | `AnthropicPPT` | `D:\Claude\Tools\AnthropicPPT` | 派生 2026-05-23（FIELDBOOK PPT 模板，skill `anthropic-ppt`） |
| **Patents/** 🔒 | | | **专利交底书工作区（无 git）** |
| 项目仓 🔒 | `Patents` | `D:\Claude\Patents` | 3 候选交底书（iusbl-jacobian / otfs-spread-pilot / usbl-cage5-3d-hybrid-doa） |
| **导航占位** | | | |
| Hub 占位 | `usbl-s1` | `projects/usbl-s1/` 仅 | dry-run 子项目（autonomous-new-project-workflow P2 实测，无对应主仓） |

## 三层职责

### 1. `ohmybrain-core`（母仓/模板）

> 定义"默认应该长什么样"。提供可复制的 harness + 工作流。

```
ohmybrain-core/
├── README.md
├── docs/
│   └── new-project-sop.md        # 新项目启动 SOP
├── template-engineering/          # TechReq/*：算法 / 仿真 / 硬件设计
├── template-document/             # DocProcess/*：文档 / 方案 / 报告
└── template-tool/                 # Tools/*：工具 / skill / template
    ├── AGENTS.md                  # Agent 协作入口
    ├── CLAUDE.md                  # 项目级指令
    ├── .claude/                   # rules / skills / commands / agents / hooks
    ├── specs/active/              # 任务 spec
    ├── plans/active/              # 实现计划
    ├── handoff/active/            # Claude Code / Codex 交接单
    ├── raw/                       # 原始资料（只读）
    ├── wiki/                      # 知识层（index.md + log.md）
    ├── scripts/                   # 自动化脚本
    └── workflows/                 # knowledge + 类型特化闭环
```

**使命**：把 Hub 已确认成熟的模式下沉为三类可复制项目骨架。模板更新只影响后续新派生项目；已运行项目通过全局规则、Hub query 或手动同步吸收变化。

### 2. `project-*`（项目仓，自包含）

> "这次具体做什么、交付什么"。每个项目有完整 harness + wiki + 代码。

```
project-*/
├── CLAUDE.md                      # 项目级指令
├── .claude/                       # 从 core 派生的 harness（可项目级定制）
├── wiki/                          # 项目级知识
│   ├── concepts/                  #   领域概念
│   ├── modules/                   #   模块设计/函数索引
│   ├── debug-logs/                #   调试日志
│   ├── conclusions.md             #   技术结论累积
│   ├── index.md / log.md
│   └── ...
├── specs/{active,archive}/        # 任务 spec
├── plans/                         # 实现计划
├── src/ or modules/               # 代码（按项目规则组织）
├── tests/                         # 测试
├── scripts/                       # 自动化（继承 + 项目补充）
└── raw/                           # 项目原始资料（只读）
```

**独立性**：每个项目仓自包含、可单独 clone、单独开发。不依赖 Hub 或 core 运行。

### 3. `ohmybrain`（Hub，本仓）

> "把所有项目串起来看"。**无 src/ 无 specs/**——不承载业务。

```
Ohmybrain/
├── CLAUDE.md                      # Hub 入口
├── TODO.md                        # 观察期配置试点等
├── projects/                      # 📍 项目导航（19 个）
│   ├── uwacomm/README.md          #   TechReq/
│   ├── usbl/README.md
│   ├── uwanet/README.md
│   ├── uwacomm_usbl/README.md     #   TechReq/ 🔒
│   ├── sonarsim/README.md         #   TechReq/ 🔒
│   ├── pricing/README.md          #   DocProcess/ 🔒
│   ├── CooperativeDetection/README.md
│   ├── paperreview/README.md
│   ├── digitaltwinguide/README.md
│   ├── digitaltwin1plusn/README.md
│   ├── visioforge/README.md       #   DocProcess/ 🔒
│   ├── CooperativeASW/README.md   #   DocProcess/ 🔒
│   ├── flowgen/README.md          #   Tools/
│   ├── iconforge/README.md
│   ├── anthropicppt/README.md
│   ├── ohmybrain-core/README.md   #   母仓
│   ├── patents/README.md          #   Patents/ 🔒（无 git）
│   └── usbl-s1/README.md          #   dry-run 子项目（无主仓）
├── raw/                           # 跨项目原始资料（只读）
├── wiki/                          # 📍 跨项目知识层
│   ├── concepts/                  #   跨项目抽象（水声通信/USBL定位/Claude-Code Skill/...）
│   ├── entities/                  #   工具 + 项目
│   ├── source-summaries/          #   论文/文章/仓库摘要
│   ├── architecture/              #   架构页（本文件）
│   ├── agents/ / workflows/       #   协作协议层（Claude Code + Codex）
│   ├── topics/ / explorations/ / comparisons/ / mcp-entities/
│   ├── index.md / log.md
├── scripts/                       # Hub 特有（import-zotero/readwise/theses + 通用 lint 等）
└── .claude/
    ├── agents/wiki-ingester.md    #   摄入 agent（主会话委托）
    ├── commands/ingest.md         #   /ingest 命令
    └── settings.json              #   Hub 自己的 hooks
```

**Hub 特有**：不派生自 core 模板（角色与项目不同），但沿用相同 wiki/ + raw/ 约定。skill 层（`llm-wiki`）走**全局 `~/.claude/skills/`**，覆盖 Hub 与所有项目。

## 数据流

### 初始化与演进流

```
1. ohmybrain-core 维护 `template-engineering/`、`template-document/`、`template-tool/`
2. 新项目启动：按类型复制对应 `template-*` → `D:\Claude\TechReq|DocProcess|Tools\<新项目>/`
   （见 ohmybrain-core/docs/new-project-sop.md）
3. 项目在本仓内独立闭环（知识 + 开发）
4. 有价值的 harness 改进经 Hub 评估后回写到对应 `ohmybrain-core/template-*/`（经验回流 A）
5. 跨项目结论 /promote-answer → ohmybrain Hub wiki/（经验回流 B）
6. Hub 提供统一入口（projects/ + wiki/）
```

### 知识闭环（4 步 · 项目内）

详见 [[dual-loop]] § knowledge 闭环。简表：

```
ingest → query → promote → review
                              ↓
                       弱触发新 ingest
```

| 步骤 | 动词 | 触发 | 工具 | 产出 |
|------|------|------|------|------|
| **01** | `ingest` | 新资料进入 `raw/` | `/ingest` 或 wiki-ingester agent | `wiki/source-summaries/` |
| **02** | `query` | 用户领域问题 | 3 层渐进披露 | "wiki 记录" vs "通用知识"分类回答 |
| **03** | `promote` | 跨项目可复用结论 | `/promote-answer`（仅下游） | Hub wiki 新页 |
| **04** | `review` | 定期（周/月） | 人工 + `lint_wiki.py` | 整理 + 触发新 ingest |

**约束**：Hub 无 `/promote-answer`（终点）；`raw/` 只读（hook 拦截）；`<private>` 标签拦截外泄。

### 开发闭环（4 步 · 项目内，Hub 不涉及）

详见 [[dual-loop]] § engineering 闭环。简表：

```
spec → plan → implement → validate
                              ↓
                       弱触发新 spec
```

| 步骤 | 动词 | 触发 | 产出 |
|------|------|------|------|
| **01** | `spec` | 新 task（knowledge 已 ready） | `specs/active/<slug>.md` |
| **02** | `plan` | spec 复杂或跨多文件 | `plans/active/<slug>.md` |
| **03** | `implement` | plan 完成或直接 code | 可工作代码 + commit |
| **04** | `validate` | code 完成 | spec 进入 `specs/archive/` |

> Phase 0：`module-design` 不在 4 步闭环内，是新模块设计 / 非平凡重构的前置文档。
>
> **Hub 无 specs/ 无 src/**——不承载业务。

## Harness 机制（三仓一致）

Claude Code 通过 `.claude/` + 全局 `~/.claude/` 共同保障行为一致：

| 层 | 位置 | 作用 | 触发 |
|----|------|------|------|
| **Global Rules** | `~/.claude/rules/common/*.md` | 跨项目通用规范（coding-style / git / testing / ...） | 主会话启动时加载 |
| **Project Rules** | `项目/.claude/rules/*.md` | 项目级路径规则（wiki.md / raw.md / engineering.md） | 读取对应路径自动加载 |
| **Global Skills** | `~/.claude/skills/{llm-wiki,...}/SKILL.md` | 跨项目技能（llm-wiki 带 `paths: wiki/**` 自动激活） | 触发关键词或路径匹配 |
| **Project Skills** | `项目/.claude/skills/*/SKILL.md` | 项目特有技能（UWAcomm 5 个：ingest/plan/implement/lint/promote-answer） | 用户显式调用 |
| **Agents** | `项目/.claude/agents/*.md` | 子代理（Hub: wiki-ingester） | 主会话委托 |
| **Hooks** | `项目/.claude/settings.json` → `scripts/*.py` | 强制行为（Pre/Post/Stop/SessionStart） | 工具调用时 |

### Hub hooks（2026-05-12 实际状态）

| Hook | 脚本 | 类型 | 作用 |
|------|------|------|------|
| **PreToolUse**（Edit/Write）| `check_raw_write.py` | 🔴 阻断 | raw/ 写入拦截 |
| **PreToolUse**（Edit/Write）| `check_private_tags.py` | 🔴 阻断 | `<private>` 标签写入拦截 |
| **PostToolUse**（Edit/Write）| `post_wiki_write.py` | 🟡 提醒 | 写入 wiki 后自动 lint |
| **PostToolUse**（Bash）| `raw_ingest_reminder.py` | 🟡 提醒 | Bash 触及 raw/ 时提醒 `/ingest` |
| **SessionStart** | `session_context.py` | 🟢 注入 | 载入会话上下文 |
| **Stop** | `check_index_log_sync.py` | 🔴 阻断 | wiki/ 变更但 index/log 未同步 |
| **Stop** | `commit_reminder.py` | 🟡 提醒 | wiki 未 commit 提醒 |
| **Stop** | `check_memory_log_gap.py` | 🟡 提醒 | memory 日期 vs wiki/log.md 缺口（2026-05-12 新增） |

阻断型 3 个 / 提醒型 4 个 / 注入型 1 个，详见 Hub `CLAUDE.md §Hook Exit Code Strategy`。

> **工作区级 hook ×2**（2026-06-10 新增，脚本托管 Hub `scripts/` 走 git、仅注册 `D:/Claude` 会话根 settings，不计入上表 Hub 8）：`check_push_readme.py` 🔴 PreToolUse(Bash)——工作区内任意仓 `git push` 前检查 README* 是否随之更新，未更新 exit 2 阻断（`SKIP_README=1` 前缀逃生）；`calendar_reminder.py` 🟡 Stop——今日 `calendar/YYYY-MM-DD *.md` 未建则提醒（stamp 节流 ≥4h 一次）。

## 工具链

```
原始资料来源              采集工具              沉淀位置
──────────────            ──────────────       ──────────────
论文             →       [[zotero]]        →   raw/papers/ (项目或 Hub)
网页文章         →       [[readwise-reader]]→   raw/articles/
YouTube/视频     →       [[firecrawl]]     →   raw/videos/
本地视频         →       [[whisper]]       →   raw/videos/
代码仓库         →       [[github]]        →   raw/repos/
                                                    ↓
                                           [[claude-code]]
                                         ingest / harness / agents
                                                    ↓
                                              项目 wiki/
                                                    ↓
                                         /promote-answer (选择性)
                                                    ↓
                                               Hub wiki/
                                                    ↓
                                    +───────────────┴──────────────+
                                  [[obsidian]]                 [[github]]
                                (可视化浏览)              (CI/CD、版本同步)
```

详细工具链见 [[toolchain]]。

## 当前规模（2026-06-09）

| 指标 | 数值 | 说明 |
|------|------|------|
| **Hub wiki 页数** | 107 | concepts 20 + entities 8 + source-summaries 31 + mcp-entities 25 + explorations 4 + topics 5 + architecture 12 + agents 1 + workflows 1 + comparisons 0（详见 `wiki/index.md`） |
| **活跃项目数** | 18 | TechReq×6（UWAcomm / USBL / UWAnet / UWAcomm_usbl🔒 / SonarSim🔒 / USBL_hw🔒）+ DocProcess×8（Pricing / UWAprojDoc / CooperativeDetection / PaperReview / DigitalTwinGuide / DigitalTwin1plusN / VisioForge / CooperativeASW，全 🔒）+ Tools×3（FlowGen / IconForge / AnthropicPPT）+ Patents🔒 |
| **模板 skill 数** | 5 | ingest/plan/implement/lint/promote-answer（core + 下游继承） |
| **全局 skill（Hub 用）** | 1 | `llm-wiki`（`paths: wiki/**` 自动激活） |
| **wiki-ingester agent** | 2 副本 | 全局 `~/.claude/agents/`（invocable，2026-05-12 起）+ 项目本地（契约源头 + git 跟踪） |
| **Zotero 论文数** | ~3 179 | 清理后 |
| **自动化脚本（Hub）** | 24 | `scripts/` 全量（含 `dashboard_snapshot.py`；2026-06-10 +2 工作区级 hook 脚本） |

## 演进里程碑

| 日期 | 里程碑 |
|------|--------|
| 2026-04-12 | 单仓原型搭建：一体化仓库 + wiki 骨架 + hooks + slash commands |
| 2026-04-12 | 工具链打通：Obsidian + Whisper + Firecrawl + Zotero |
| 2026-04-12 | Zotero 清理：-1634 重复，生成 10 方向研究地图 |
| 2026-04-12~13 | 摄入 UWAcomm 首个项目 + 工程闭环（rules/skills/hooks/CI） |
| 2026-04-?? | **架构拆分**：单仓 → `ohmybrain-core + project-* + ohmybrain(hub)` 三仓 |
| 2026-04-14 | wiki-ingester agent + `/ingest` Step 1.5 规模分流 |
| 2026-04-15 | 基础设施下发：hook 绝对路径 + raw_ingest_reminder 同步到 core + 3 下游 |
| 2026-04-15 | 摄入 ECC（Everything Claude Code）生产级参考 |
| 2026-04-17 | 架构页重写：反映三仓现状 |
| 2026-04-21 | autonomous-new-project-workflow 落地（P1 dry-run UWAnet） |
| 2026-04-22 | 6 篇 UWA Doppler 论文并行摄入 + `doppler-estimation-methods` concept |
| 2026-04-23 | FlowGen 派生（首个 Tools/ 项目） |
| 2026-04-25 | UWAcomm_usbl 派生（首个内网 Internal 项目） |
| 2026-04-28 | UWAprojDoc 派生（DocProcess 文档撰写工作区） |
| 2026-05-08~09 | CooperativeDetection / PaperReview 派生（DocProcess 私人项目） |
| 2026-05-12 | `/ingest` 路径 B 修复 + memory→Hub log 缺口工具链（L1+L2+L3）+ 架构页同步 |
| 2026-05-25 | DigitalTwin1plusN 派生（「1+N」集群数字孪生体系，DocProcess🔒） |
| 2026-05-29 | IconForge 派生（自然语言→图标 SVG，Tools/） |
| 2026-06-02 | VisioForge 派生（通用 Visio 出图工作区，DocProcess🔒） |
| 2026-06-03 | SonarSim 派生（主动声呐界面仿真 MATLAB，TechReq🔒）+ CooperativeASW 派生（UWAprojDoc 协同探潜分系统单列细化 docx，DocProcess🔒） |
| 2026-06-09 | Claude+Codex 协作协议层落地（3 协议页 + agents/ + workflows/ 新分类 + 双 agent 文件接口） |
| 2026-06-10 | USBL_hw 派生（USBL 硬件设计，engineering-hardware 子型首例，TechReq🔒）+ 工作区级 hook ×2（push README 检查 / calendar 提醒） |

## 相关页面

- [[ohmybrain-three-tier-seed]] — 三仓架构设计笔记（本页事实源）
- [[research-map]] — 研究方向全景地图（概念侧切片）
- [[toolchain]] — 工具链详细指南
- [[my-brain-setup-plan]] — 初始单仓搭建计划（历史参考）
- [[uwacomm]] — 首个从 core 派生的项目实体
- [[ohmybrain-agent-architecture-insights]] — 架构演进中的 agent/skill 决策（P0-P3 行动项）
- [[document-protocol]] — 项目文档结构协议（工作区地图/Hub/项目状态三层 + 标准骨架 + L0-L3 迁移级别）
