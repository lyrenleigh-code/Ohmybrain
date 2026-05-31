---
type: topic
created: 2026-05-24
updated: 2026-05-29
tags: [harness, skills, hooks, rules, agents, MCP]
---

# Harness 全景索引

Claude Code harness 资源全景：**Hooks + Skills + Rules + Agents + MCP**。本页是入口索引，详细在各资源原始文件。

> 大部分 harness 资源在 `~/.claude/` 全局或项目 `.claude/`，本页**只索引不复制**。
>
> 全景计数（@2026-05-29）：本地 skills **33 个目录**（31 含 SKILL.md）/ 全局 agents **55 个 .md** / rules **15 个目录** / MCP **6 个 server**。

## 1. Hooks

### Hub Hooks (8 个)

详见 [[ecosystem-dashboard]] § Hub Hooks 表 + [[../architecture/system-overview]] § Hub hooks。

3 阻断 + 5 提醒/注入：

| Hook | 类型 | 触发时机 |
|------|------|---------|
| `check_raw_write.py` | 🔴 阻断 | PreToolUse Edit/Write |
| `check_private_tags.py` | 🔴 阻断 | PreToolUse Edit/Write |
| `check_index_log_sync.py` | 🔴 阻断 | Stop |
| `post_wiki_write.py` | 🟡 提醒 | PostToolUse Edit/Write |
| `raw_ingest_reminder.py` | 🟡 提醒 | PostToolUse Bash |
| `commit_reminder.py` | 🟡 提醒 | Stop |
| `check_memory_log_gap.py` | 🟡 提醒 | Stop |
| `session_context.py` | 🟢 注入 | SessionStart |

### 项目 Hooks

各项目 `.claude/settings.json` 引用 `scripts/*.py`，模式与 Hub 一致：

- `check_raw_write.py` / `check_private_tags.py` / `lint_wiki.py` / `validate_task.py` 等
- 来源 `ohmybrain-core/template/.claude/`

详见 [[../architecture/conventions]] § 8 Hooks 约定 (Exit code strategy)。

## 2. Skills

Skills 是 harness 中**最易误判计数**的一层，必须区分两层：

| 层 | 计数 | 来源 |
|----|------|------|
| **本地层** | **33 个目录**（31 含 `SKILL.md`，2 个为工件目录无 SKILL.md） | `~/.claude/skills/` 实际落盘 |
| **注入层** | **90+ 个**（含 `ecc:*` 前缀 plugin / marketplace） | SessionStart 注入 plugin skill list 叠加后 |

> ⚠️ 不可裸写「90+ 个全局 skill」——那是注入层叠加 ecc plugin 后的数；本地实体只有 33 目录 / 31 SKILL.md。

### 2.1 本地 Skills（`~/.claude/skills/`，31 个 SKILL.md）

按域分组（共 31 个 SKILL.md，另 2 个目录 `jy-pricing-workspace` / `learned` 是工件目录，无 SKILL.md）：

**文档类（5）**：
- `docx`（Word 文档）/ `pdf`（PDF 读写/OCR/表单）/ `pptx`（幻灯片）/ `xlsx`（电子表格）
- `doc-coauthoring`（结构化协作写文档/proposal/spec）

**FlowGen 系（8）**：
- `flowgen`（自然语言 → Mermaid flowchart）
- `flowgen-vsdx`（→ Visio 流程图 M4）/ `flowgen-layered`（分层架构 M5）/ `flowgen-sequence`（UML 时序 M5）
- `flowgen-composition`（系统组成嵌套 M6）/ `flowgen-roadmap`（项目立项三段式 M7）
- `flowgen-archposter`（四化五层挂图 M7）/ `flowgen-replica`（图片 → vsdx 骨架复刻 M8）

**前端 / 视觉（6）**：
- `frontend-design`（生产级前端界面）/ `web-artifacts-builder`（React+Tailwind+shadcn 复杂 artifact）/ `webapp-testing`（Playwright 测试）
- `architecture-diagram`（暗色架构图 HTML/SVG）/ `canvas-design`（.png/.pdf 平面设计）/ `algorithmic-art`（p5.js 生成艺术）

**品牌 / 风格（3）**：
- `brand-guidelines`（Anthropic 品牌色/字体）/ `theme-factory`（10 套预设主题）/ `slack-gif-creator`（Slack 动图）

**领域特化（3）**：
- `jy-pricing`（军用软件四号文报价）/ `tech-requirements`（MATLAB 算法函数生成）/ `anthropic-ppt`（FIELDBOOK 风 PPT，引用 `Tools/AnthropicPPT/`）

**学习 / 元（3）**：
- `continuous-learning`（会话 → learned skill）/ `continuous-learning-v2`（instinct 学习系统 v2.1）/ `skill-creator`（创建/优化/eval skill）

**其他（3）**：
- `mcp-builder`（构建 MCP server）/ `internal-comms`（内部沟通文档）/ `llm-wiki`（wiki ingest/query/lint/promote 协议，路径触发 `wiki/**`）

> 本地 31 个 SKILL.md 完整清单：algorithmic-art · anthropic-ppt · architecture-diagram · brand-guidelines · canvas-design · continuous-learning · continuous-learning-v2 · doc-coauthoring · docx · flowgen · flowgen-archposter · flowgen-composition · flowgen-layered · flowgen-replica · flowgen-roadmap · flowgen-sequence · flowgen-vsdx · frontend-design · internal-comms · jy-pricing · llm-wiki · mcp-builder · pdf · pptx · skill-creator · slack-gif-creator · tech-requirements · theme-factory · web-artifacts-builder · webapp-testing · xlsx。
> 另 2 个无 SKILL.md 的工件目录：`jy-pricing-workspace`（jy-pricing 运行工作区）/ `learned`（continuous-learning 沉淀输出）。

### 2.2 注入层 `ecc:*` Skills（90+）

SessionStart 注入的 plugin / marketplace skill，叠加在本地 31 个之上后总数达 **90+**。`ecc:` 前缀（Everything Claude Code）覆盖：

- **review / build / test 系**：`code-review` / `verify` / `tdd` / `e2e` / `eval` / `cpp-build` / `cpp-review` / `go-build` / `python-review` / `kotlin-review` / `rust-review` / `flutter-build` 等（多语言对偶）
- **知识 / 会话管理**：`learn-eval` / `prompt-optimize` / `save-session` / `resume-session` / `sessions` / `rules-distill`
- **编排 / 调度**：`loop` / `schedule` / `orchestrate` / `santa-loop` / `multi-plan` / `multi-execute`
- **安全 / 优化**：`safety-guard` / `prompt-optimizer` / `ecc-tools-cost-audit` / `workspace-surface-audit`
- **instinct 系**：`instinct-status` / `instinct-export` / `instinct-import` / `promote` / `prune` / `evolve`

> 这些是**注入而非落盘**——`~/.claude/skills/` 里看不到 `ecc:*` 目录，它们随 plugin 在会话启动时注入。

### 2.3 项目 Skills

各项目 `.claude/skills/` 独立（如 UWAcomm 5 个：ingest / plan / implement / lint / promote-answer）。

来源：`ohmybrain-core/template/.claude/skills/`。

## 3. Rules

### 3.1 Global Rules（`~/.claude/rules/`，15 个目录）

```
~/.claude/rules/
├── README.md                 # 安装 / 分层 / 优先级说明
├── common/                   # 语言无关通用原则（始终加载）
│   ├── agents.md
│   ├── code-review.md
│   ├── coding-style.md
│   ├── development-workflow.md
│   ├── git-workflow.md
│   ├── hooks.md
│   ├── llm-wiki.md
│   ├── ohmybrain-hub.md
│   ├── patterns.md
│   ├── performance.md
│   ├── security.md
│   └── testing.md
├── zh/                       # common 的中文翻译版本
├── web/                      # web / 前端扩展（coding-style/design-quality/hooks/patterns/performance/security/testing）
└── <12 语言目录>             # 语言特定扩展（见下）
```

**12 个语言特定目录**（扩展 common，语言习惯冲突时语言层优先）：

| 语言目录 | 语言目录 | 语言目录 | 语言目录 |
|---------|---------|---------|---------|
| `cpp` | `csharp` | `dart` | `golang` |
| `java` | `kotlin` | `perl` | `php` |
| `python` | `rust` | `swift` | `typescript` |

> 15 个目录 = `common` + `zh` + `web` + 上述 12 语言。`README.md` 是文件不是目录。
> 优先级：语言特定 > common（类比 CSS 特异性 / `.gitignore` 优先级）。

`common/` + 命中语言层在启动时自动加载（进入 system prompt）。

### 3.2 项目 Rules

`项目/.claude/rules/*.md` — 项目级路径规则：
- `wiki.md`（wiki 写作约定）
- `raw.md`（raw 只读约定）
- `engineering.md`（项目工程约定）
- `specs.md`（spec 写作约定）

来源：`ohmybrain-core/template/.claude/rules/`。

## 4. Agents

全局 `~/.claude/agents/` 实有 **55 个 .md**，按职能分组：

**Review 系（13）**：
`code-reviewer` · `security-reviewer` · `cpp-reviewer` · `csharp-reviewer` · `database-reviewer` · `flutter-reviewer` · `go-reviewer` · `healthcare-reviewer` · `java-reviewer` · `kotlin-reviewer` · `python-reviewer` · `rust-reviewer` · `typescript-reviewer`

**Build-Resolver 系（7）**：
`build-error-resolver` · `cpp-build-resolver` · `dart-build-resolver` · `go-build-resolver` · `java-build-resolver` · `kotlin-build-resolver` · `rust-build-resolver` · `pytorch-build-resolver`

**编排 / 规划（6）**：
`planner` · `architect` · `code-architect` · `oracle` · `sisyphus` · `loop-operator`

**文档（3）**：
`doc-updater` · `document-writer` · `docs-lookup`

**探索 / 代码理解（4）**：
`explore` · `code-explorer` · `librarian` · `multimodal-looker`

**质量 / 重构 / 测试（7）**：
`refactor-cleaner` · `code-simplifier` · `e2e-runner` · `tdd-guide` · `pr-test-analyzer` · `silent-failure-hunter` · `performance-optimizer`

**分析 / 设计（4）**：
`comment-analyzer` · `conversation-analyzer` · `type-design-analyzer` · `seo-specialist`

**GAN 三件套（3）**：
`gan-planner` · `gan-generator` · `gan-evaluator`

**开源流水线（3）**：
`opensource-forker` · `opensource-packager` · `opensource-sanitizer`

**前端 / 战略 / 元（5）**：
`frontend-ui-ux-engineer` · `chief-of-staff` · `harness-optimizer` · `wiki-ingester` · `tdd-guide`*

> `wiki-ingester`：全局 invocable + 项目本地（契约源头），长论文 ingest 独立上下文，见 [[../architecture/decision-log]]（ADR-002 ingester 边界）。
> 完整 55 个清单：architect · build-error-resolver · chief-of-staff · code-architect · code-explorer · code-reviewer · code-simplifier · comment-analyzer · conversation-analyzer · cpp-build-resolver · cpp-reviewer · csharp-reviewer · dart-build-resolver · database-reviewer · doc-updater · docs-lookup · document-writer · e2e-runner · explore · flutter-reviewer · frontend-ui-ux-engineer · gan-evaluator · gan-generator · gan-planner · go-build-resolver · go-reviewer · harness-optimizer · healthcare-reviewer · java-build-resolver · java-reviewer · kotlin-build-resolver · kotlin-reviewer · librarian · loop-operator · multimodal-looker · opensource-forker · opensource-packager · opensource-sanitizer · oracle · performance-optimizer · planner · pr-test-analyzer · python-reviewer · pytorch-build-resolver · refactor-cleaner · rust-build-resolver · rust-reviewer · security-reviewer · seo-specialist · silent-failure-hunter · sisyphus · tdd-guide · type-design-analyzer · typescript-reviewer · wiki-ingester。

## 5. MCP Servers

6 个 MCP servers（mcp:: 命名空间），通过 `mcp__plugin_ecc_*` 调用：

| MCP | 用途 | 工具数 |
|-----|------|--------|
| `context7` | 库文档查询 | 2 (resolve-library-id, query-docs) |
| `exa` | 网络搜索 | 2 (web_search, web_fetch) |
| `github` | GitHub API | 28+ (issues / PR / search / commits / 等) |
| `memory` | knowledge graph | 9 (create_entities / relations / observations / 等) |
| `playwright` | 浏览器自动化 | 19+ (navigate / click / type / screenshot / 等) |
| `sequential-thinking` | 多步推理 | 1 (sequentialthinking) |

> 各 MCP server 实体卡片见 wiki `mcp-entities/`（25 篇）。

## 6. 跨资源决策树

| 想做什么 | 优先选 | 详细 |
|---------|-------|------|
| 写流程图 | `flowgen` 系列 | 8 个 skill 按场景分流 |
| 写 PPT | `anthropic-ppt` skill | FIELDBOOK 风格 |
| 查论文 / 文章 | wiki query + Hub source-summaries | [[../architecture/dual-loop]] § query |
| ingest 长论文 | `wiki-ingester` agent | [[../architecture/decision-log]] ADR-002 |
| Code review | `code-review` skill 或 `code-reviewer` agent | 看场景 |
| MATLAB 函数 | `tech-requirements` skill | 项目特化 |
| 写 docx | `docx` 内置 skill | Anthropic 官方 |
| 写 xlsx | `xlsx` 内置 skill | 同上 |
| 跨项目 promote 候选 | [[ecosystem-dashboard]] § Promote 队列 | 手动审查 |

## 7. 加载层次

```
启动 Claude Code
  ↓
SessionStart hook 注入上下文（含 ecc:* skill list 叠加 → 90+）
  ↓
~/.claude/rules/common/* + 命中语言层加载（system prompt）
  ↓
项目/.claude/rules/* 按路径加载（visit wiki/ → wiki.md）
  ↓
本地 31 个 SKILL.md / 55 个 agents / 6 个 MCP 按需调用（关键词 / 显式 / 路径）
  ↓
Hooks 按触发时机执行（PreToolUse / PostToolUse / Stop / SessionStart）
```

## 相关页面

- [[../architecture/hub-as-brain]] — 大脑功能定位
- [[../architecture/system-overview]] § Harness 机制 — 三仓 harness 总览
- [[../architecture/conventions]] — Exit Code Strategy 等
- [[../architecture/decision-log]] — ADR-001~020（ADR 章节，非独立文件）
- [[ecosystem-dashboard]] § Hub Hooks
