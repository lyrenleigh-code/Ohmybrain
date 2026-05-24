---
type: topic
created: 2026-05-24
updated: 2026-05-24
tags: [harness, skills, hooks, rules, agents, MCP]
---

# Harness 全景索引

Claude Code harness 资源全景：**Hooks + Skills + Rules + Agents + MCP**。本页是入口索引，详细在各资源原始文件。

> 大部分 harness 资源在 `~/.claude/` 全局或项目 `.claude/`，本页**只索引不复制**。

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

### 全局 Skills（`~/.claude/skills/`）

详见 SessionStart 注入的 skill list（每次会话开始 system reminder 列出）。

按分类摘要（90+ 个全局 skill）：

**LLM 内置 skills (Anthropic 官方)**：
- `algorithmic-art` / `architecture-diagram` / `brand-guidelines` / `canvas-design` / `docx` / `pdf` / `pptx` / `xlsx`
- `frontend-design` / `internal-comms` / `mcp-builder` / `skill-creator` / `slack-gif-creator` / `theme-factory` / `webapp-testing` / `web-artifacts-builder`

**FlowGen 系列 8 个**：
- `flowgen` (Mermaid)
- `flowgen-vsdx` / `flowgen-layered` / `flowgen-sequence` / `flowgen-composition` / `flowgen-roadmap` / `flowgen-archposter` / `flowgen-replica`

**项目特化**：
- `anthropic-ppt`（关键词触发 PPT/幻灯片/演讲，引用 `Tools/AnthropicPPT/`）
- `llm-wiki`（路径触发 wiki/**，引用 `~/.claude/skills/llm-wiki/`）
- `jy-pricing`（军用软件四号文）
- `tech-requirements`（MATLAB 函数生成）

**通用流程 skills**：
- `code-review` / `verify` / `learn-eval` / `prompt-optimize` / `tdd` / `e2e` / `eval`
- `cpp-build` / `cpp-review` / `go-build` / `python-review` / `kotlin-review` / `rust-review` / `flutter-build`
- `loop` / `schedule` / `save-session` / `resume-session` / `sessions`

**ecc:* 系列**（Everything Claude Code）：含 80+ 个 ecc: 前缀 skill，覆盖 review / build / test / 知识管理 / 安全 / 优化

### 项目 Skills

各项目 `.claude/skills/` 独立（如 UWAcomm 5 个：ingest / plan / implement / lint / promote-answer）。

来源：`ohmybrain-core/template/.claude/skills/`。

## 3. Rules

### Global Rules（`~/.claude/rules/`）

```
~/.claude/rules/
├── common/
│   ├── agents.md
│   ├── code-review.md
│   ├── coding-style.md
│   ├── development-workflow.md
│   ├── git-workflow.md
│   ├── hooks.md
│   ├── llm-wiki.md
│   ├── ohmybrain-hub.md (新加)
│   ├── patterns.md
│   ├── performance.md
│   ├── security.md
│   └── testing.md
├── zh/                      # 中文翻译版本
└── web/                     # web-specific extensions
    ├── coding-style.md
    ├── design-quality.md
    ├── hooks.md
    ├── patterns.md
    ├── performance.md
    ├── security.md
    └── testing.md
```

启动时自动加载（在 system prompt 中）。

### 项目 Rules

`项目/.claude/rules/*.md` — 项目级路径规则：
- `wiki.md`（wiki 写作约定）
- `raw.md`（raw 只读约定）
- `engineering.md`（项目工程约定）
- `specs.md`（spec 写作约定）

来源：`ohmybrain-core/template/.claude/rules/`。

## 4. Agents

| Agent | 位置 | 用途 |
|-------|------|------|
| `wiki-ingester` | `~/.claude/agents/` (全局 invocable) + 项目本地（契约源头） | 长论文 ingest 独立上下文 |
| `code-reviewer` | 全局 | 代码审查 |
| `security-reviewer` | 全局 | 安全审查 |
| `planner` | 全局 | 计划制定 |
| `tdd-guide` | 全局 | TDD 引导 |
| `python-reviewer` / `go-reviewer` / `rust-reviewer` / 等 | 全局 | 语言特定 review |
| `Explore` / `Plan` | 内置 | 探索 / 规划 |

详见 `~/.claude/agents/` 完整 list 或 system 注入的 agent 列表。

## 5. MCP Servers

6 个 MCP servers（mcp:: 命名空间），通过 `mcp__plugin_ecc_*` 调用：

| MCP | 用途 | 工具数 |
|-----|------|--------|
| `context7` | 库文档查询 | 2 (resolve-library-id, query-docs) |
| `exa` | 网络搜索 | 2 (web_search, web_fetch) |
| `github` | GitHub API | 28+ (issues / PR / search / commits / 等) |
| `memory` | knowledge graph | 9 (create_entities / relations / observations / 等) |
| `playwright` | 浏览器自动化 | 19 (navigate / click / type / screenshot / 等) |
| `sequential-thinking` | 多步推理 | 1 (sequentialthinking) |

## 6. 跨资源决策树

| 想做什么 | 优先选 | 详细 |
|---------|-------|------|
| 写流程图 | `flowgen` 系列 | 8 个 skill 按场景分流 |
| 写 PPT | `anthropic-ppt` skill | FIELDBOOK 风格 |
| 查论文 / 文章 | wiki query + Hub source-summaries | [[../architecture/dual-loop]] § query |
| ingest 长论文 | `wiki-ingester` agent | ADR-002 |
| Code review | `code-review` skill 或 `code-reviewer` agent | 看场景 |
| MATLAB 函数 | `tech-requirements` skill | 项目特化 |
| 写 docx | `docx` 内置 skill | Anthropic 官方 |
| 写 xlsx | `xlsx` 内置 skill | 同上 |
| 跨项目 promote 候选 | [[ecosystem-dashboard]] § Promote 队列 | 手动审查 |

## 7. 加载层次

```
启动 Claude Code
  ↓
SessionStart hook 注入上下文
  ↓
~/.claude/rules/common/* 加载（system prompt）
  ↓
项目/.claude/rules/* 按路径加载（visit wiki/ → wiki.md）
  ↓
Skills/Agents/MCP 按需调用（关键词 / 显式 / 路径）
  ↓
Hooks 按触发时机执行（PreToolUse / PostToolUse / Stop / SessionStart）
```

## 相关页面

- [[../architecture/hub-as-brain]] — 大脑功能定位
- [[../architecture/system-overview]] § Harness 机制 — 三仓 harness 总览
- [[../architecture/conventions]] — Exit Code Strategy 等
- [[ecosystem-dashboard]] § Hub Hooks
