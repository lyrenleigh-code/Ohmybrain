---
type: architecture
created: 2026-04-12
updated: 2026-05-12
tags: [架构, 三仓, Hub, 模板, 闭环, harness]
---

# 系统架构总览

## 定位

Ohmybrain 体系采用**三仓架构**：**母仓模板** + **项目仓** + **Hub**。三者职责分离、数据单向流动，共享同一套 Claude Code harness 模板。

事实源：[[ohmybrain-three-tier-seed]]（架构设计笔记）+ 本仓根 `CLAUDE.md` 项目映射表。

> **演化历史**：早期（2026-04-12 前）曾是 *"LLM Wiki + 开发工程 + Claude Code Harness 一体化单仓"* 设计（见 [[my-brain-setup-plan]] / `raw/notes/agent_knowledge_repo_template.md`），后拆分为本文档描述的三仓结构。

## 三仓结构

```
┌──────────────────────┐       复制派生       ┌──────────────────────┐
│  ohmybrain-core      │ ─────────────────→  │  project-*           │
│  母仓 / 模板          │                      │  子项目仓（自包含）    │
│  D:\Claude\ohmybrain- │ ←─── 经验回流 ───── │  D:\Claude\TechReq\  │
│  core                │                      │  {UWAcomm,USBL,...}  │
└──────────────────────┘                      └──────────┬───────────┘
                                                          │ 索引
                                                          │ 跨项目结论
                                                          ↓ /promote-answer
                                              ┌──────────────────────┐
                                              │  ohmybrain (Hub)     │
                                              │  知识库 + 项目导航     │
                                              │  D:\Claude\Ohmybrain │
                                              └──────────────────────┘
```

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
| **DocProcess/** 🔒 | | | **文档处理工作区，全部私人项目** |
| 项目仓 🔒 | `Pricing` | `D:\Claude\DocProcess\Pricing` | 活跃（军用软件四号文报价） |
| 项目仓 🔒 | `UWAprojDoc` | `D:\Claude\DocProcess\UWAprojDoc` | 派生 2026-04-28（水声专项方案技术文档撰写） |
| 项目仓 🔒 | `CooperativeDetection` | `D:\Claude\DocProcess\CooperativeDetection` | 派生 2026-05-08（水下分布式协同探测 4 专题 12 课题） |
| 项目仓 🔒 | `PaperReview` | `D:\Claude\DocProcess\PaperReview` | 派生 2026-05-09（学位论文外审） |
| **Tools/** | | | **跨项目工具** |
| 项目仓 | `FlowGen` | `D:\Claude\Tools\FlowGen` | 派生 2026-04-23（自然语言→Mermaid 流程图，未实装） |
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
└── template/                      # 👇 从此派生
    ├── CLAUDE.md
    ├── .claude/
    │   ├── rules/                 # 路径特定规则（wiki/raw/engineering/specs）
    │   ├── skills/                # 5 个技能（ingest/plan/implement/lint/promote-answer）
    │   ├── commands/              # ingest.md + promote.md
    │   └── settings.json          # 跨平台 Python hooks
    ├── raw/                       # 10 子目录骨架（只读）
    ├── wiki/                      # 知识层（index.md + log.md）
    ├── scripts/                   # 8 个自动化脚本
    ├── workflows/
    │   ├── knowledge/             # 4 步（ingest→query→promote→review）
    │   └── engineering/           # 5 步（module-design→spec→plan→implement→validate）
    └── .github/workflows/
```

**使命**：变更模板即可一次性升级所有下游项目的 harness（目前靠手动同步 per 2026-04-15 log）。

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
├── projects/                      # 📍 项目导航（10 个）
│   ├── uwacomm/README.md          #   TechReq/
│   ├── usbl/README.md
│   ├── uwanet/README.md
│   ├── uwacomm_usbl/README.md     #   TechReq/ 🔒
│   ├── pricing/README.md          #   DocProcess/ 🔒
│   ├── CooperativeDetection/README.md
│   ├── paperreview/README.md
│   ├── flowgen/README.md          #   Tools/
│   ├── ohmybrain-core/README.md   #   母仓
│   └── usbl-s1/README.md          #   dry-run 子项目（无主仓）
├── raw/                           # 跨项目原始资料（只读）
├── wiki/                          # 📍 跨项目知识层
│   ├── concepts/                  #   跨项目抽象（水声通信/USBL定位/Claude-Code Skill/...）
│   ├── entities/                  #   工具 + 项目
│   ├── source-summaries/          #   论文/文章/仓库摘要
│   ├── architecture/              #   架构页（本文件）
│   ├── topics/ / explorations/ / comparisons/
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
1. ohmybrain-core 维护 template/
2. 新项目启动：cp -r ohmybrain-core/template/ → D:\Claude\TechReq\<新项目>/
   （见 ohmybrain-core/docs/new-project-sop.md）
3. 项目在本仓内独立闭环（知识 + 开发）
4. 有价值的 harness 改进回写到 ohmybrain-core/template/（经验回流 A）
5. 跨项目结论 /promote-answer → ohmybrain Hub wiki/（经验回流 B）
6. Hub 提供统一入口（projects/ + wiki/）
```

### 知识闭环（项目内）

```
raw/ → ingest → wiki/ → query ↻
                ↓ promote（跨项目价值时）
            Hub wiki/
```

| 阶段 | 触发 | 工具 | 约束 |
|------|------|------|------|
| **收集** | 资料放入 `raw/{papers,articles,repos,...}` | 手动 / 脚本（import-zotero/readwise/theses） | raw/ 只读；PreToolUse hook 强制 |
| **摄入** | `/ingest <路径>` | Hub 用 `wiki-ingester` agent；下游项目用 skill | 预算：≤200 行 summary / ≤5 页更新 |
| **查询** | 用户提问 | 主会话读 wiki/ | 分"wiki 记录"vs"通用知识" |
| **沉淀** | `/promote-answer`（下游专属） | 下游 skill | Hub 是终点，无 `/promote-answer` |
| **审查** | 定期 | `lint_wiki.py` + `check_index_log_sync.py` | PostToolUse + Stop hook 强制 |

### 开发闭环（项目内，Hub 不涉及）

```
spec → plan → implement → test → validate → archive
       └──→ wiki/ 同步 ←──┘
```

详见各项目的 `workflows/engineering/`（0-5 阶段：module-design / spec / plan / implement / validate）。**Hub 无 specs/ 无 src/**。

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

## 当前规模（2026-05-12）

| 指标 | 数值 | 说明 |
|------|------|------|
| **Hub wiki 页数** | 86 | concepts + entities + source-summaries + mcp-entities + explorations + topics + architecture + comparisons（详见 `wiki/index.md`） |
| **活跃项目数** | 9 | TechReq×4（UWAcomm / USBL / UWAnet / UWAcomm_usbl🔒）+ DocProcess×4（Pricing / UWAprojDoc / CooperativeDetection / PaperReview，全 🔒）+ Tools×1（FlowGen） |
| **模板 skill 数** | 5 | ingest/plan/implement/lint/promote-answer（core + 下游继承） |
| **全局 skill（Hub 用）** | 1 | `llm-wiki`（`paths: wiki/**` 自动激活） |
| **wiki-ingester agent** | 2 副本 | 全局 `~/.claude/agents/`（invocable，2026-05-12 起）+ 项目本地（契约源头 + git 跟踪） |
| **Zotero 论文数** | ~3 179 | 清理后 |
| **自动化脚本（Hub）** | 19 | `scripts/` 全量（+ 2026-05-12 加 `diff_memory_log.py` / `check_memory_log_gap.py`） |

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
| 2026-05-12 | `/ingest` 路径 B 修复 + memory→Hub log 缺口工具链（L1+L2+L3）+ 架构页同步（本次更新） |

## 相关页面

- [[ohmybrain-three-tier-seed]] — 三仓架构设计笔记（本页事实源）
- [[research-map]] — 研究方向全景地图（概念侧切片）
- [[toolchain]] — 工具链详细指南
- [[my-brain-setup-plan]] — 初始单仓搭建计划（历史参考）
- [[uwacomm]] — 首个从 core 派生的项目实体
- [[ohmybrain-agent-architecture-insights]] — 架构演进中的 agent/skill 决策（P0-P3 行动项）
