---
type: source-summary
created: 2026-04-17
updated: 2026-04-17
tags: [Claude-Code, 插件, 持久记忆, MCP, 渐进披露, Hook生命周期, 子代理编排, 多语言]
source_type: repo
---

# Claude-Mem — Claude Code 跨会话持久记忆插件

## 来源信息

- **仓库**：`github.com/thedotmack/claude-mem`
- **npm**：`claude-mem` v12.1.6（package.json 版本；README 仍标 v6.5.0 未更新）
- **本地路径**：`raw/repos/claude-mem`
- **许可**：AGPL-3.0（`ragtime/` 子目录单独 PolyForm Noncommercial）
- **维护方**：Alex Newman（`@thedotmack`），Awesome Claude Code 收录，Trendshift 推荐
- **规模**：211 MB / TypeScript + Bun + SQLite + Chroma + React UI + 36 个本地化 mode + 7 plugin skills + 5 lifecycle hooks
- **定位**：Claude Code 插件，通过 hook 自动捕获 tool 使用轨迹 → AI 压缩 → SQLite+Chroma 存储 → 下次会话自动注入上下文

## 核心观点

对 Ohmybrain 的启发**不在持久记忆本身**（Ohmybrain 已有 `~/.claude/projects/.../memory/` 自动记忆），而在 **5 条可迁移的工程模式**。

### 1. 三层渐进披露检索模式（最有启发）

MCP 工具暴露 3 个层级的 search，Claude 必须**按层级递进**：

```
Step 1: search()          → 压缩索引（ID+title，~50-100 tokens/条）
Step 2: timeline()        → 时序上下文（anchor 前后 N 条）
Step 3: get_observations()→ 完整详情（仅过滤后的 ID，~500-1k tokens/条）
```

约束由 `mem-search` skill 硬编码：**"NEVER fetch full details without filtering first. 10x token savings."**

**对 Ohmybrain 的价值**：当前 `llm-wiki` 查询是 "grep → 直接 Read 全文"，wiki 页数扩大后必然低效。`wiki-index` (当前 index.md 已近似) → `wiki-log-timeline` (log.md 按日期切) → `wiki-read` 三层协议可直接移植。

### 2. `make-plan` + `do` 的强约束编排模式

- **`make-plan` Phase 0 = Documentation Discovery**：强制子代理先取 API 签名 / examples / 反模式，主代理只做 synthesis
- **Subagent Reporting Contract（MANDATORY）**：子代理每次必须返回 {sources consulted, concrete findings (exact API/paths), copy-ready snippet locations, confidence + known gaps}——"Reject and redeploy the subagent if it reports conclusions without sources."
- **"COPY from docs, don't invent"** 写入硬约束：Good="Copy the V2 session pattern from docs/examples.ts:45-60" / Bad="Migrate the existing code to V2"
- **`do` 每阶段并行子代理**：Verification / Anti-pattern / Code Quality / Commit——**commit only if verified**

**对 Ohmybrain 的价值**：下游 `plan-task` / `implement-task` skill 可吸收 Phase 0 + Subagent Contract。比当前 spec→plan 单流程强约束。对应 [[subagents-orchestration]]。

### 3. 36 个本地化 mode 系统（语言层与功能层分离）

`plugin/modes/code--{lang}.json` 定义每语言的 XML 占位符 + 指令片段，统一由 `CLAUDE_MEM_MODE=code--zh` 环境变量切换。主骨架 prompt 是稳定的，**语言只是叠加层**。

示例（`code--zh.json`）：
```json
{
  "name": "Code Development (Chinese)",
  "prompts": {
    "xml_title_placeholder": "[**title**: 捕捉核心行动或主题的简短标题]",
    "xml_fact_placeholder": "[简洁、独立的陈述]",
    "continuation_instruction": "IMPORTANT: ... LANGUAGE REQUIREMENTS: Please write the observation data in 中文"
  }
}
```

**对 Ohmybrain 的价值**：未来 wiki 出英文版（开源分享）时，避免 skill 内容分叉；也可用于 UWAcomm "中文注释 + 英文函数名" 规则的系统化表达。

### 4. `<private>` 标签 + hook 层剥除

`<private>content</private>` 在 hook 边界（数据出主会话前）就被 `src/utils/tag-stripping.ts` 移除，**私密内容永不进 SQLite / worker / DB**。

**对 Ohmybrain 的价值**：Hub `Pricing` 🔒 项目当前靠人记"不 promote"。一个 PreToolUse Python hook 扫描 `<private>` 片段 + 自动过滤，可**自动隔离私密内容避免泄漏**。成本极低（正则 + hook）。

### 5. 5-lifecycle hooks 的职责分工 + Exit Code Strategy

**hook 生命周期**：`Setup → SessionStart → UserPromptSubmit → PostToolUse → Stop → SessionEnd`

- `Setup` hook（plugin 特有）：`smart-install.js` 检查依赖并按需自动安装 Bun/uv
- `SessionStart`（matcher: `startup|clear|compact`）：拉 context + 等 worker healthcheck（curl loop 20×）
- `PostToolUse`（matcher: `*`）：每个 tool 调用写一条 observation，120s timeout

**CLAUDE.md §Exit Code Strategy** 明文契约：
- `Exit 0`：success OR 优雅关闭（Windows Terminal 不累积 tab）
- `Exit 1`：non-blocking error（stderr 给用户看，继续）
- `Exit 2`：blocking error（stderr 喂回 Claude）
- **哲学**："Worker/hook errors exit with code 0 to prevent Windows Terminal tab accumulation. The wrapper/plugin layer handles restart logic."

**对 Ohmybrain 的价值**：Hub / 下游 CLAUDE.md 可补一段"hook 行为契约"段，让 hook exit code 选择可追溯。对应 [[claude-hooks-architecture]]。

## 不建议借鉴

| 特性 | 原因 |
|------|------|
| Chroma 向量搜索 | 49 页规模 grep 足够；+uv+Python 运维负担大；阈值 ~200 页 |
| Worker service (localhost:37777) + React UI | 过度工程；Obsidian + dataview 已提供可视化 |
| 全局 SQLite observation DB | 与 Ohmybrain "主动 ingest + 结构化 wiki" 哲学正交 |
| AGPL-3.0 | 当前私人项目不涉及许可；未来需慎选（AGPL 对商用不友好） |

## 与已有范本的对照

| 维度 | claude-mem | [[affaan-m-everything-claude-code|ECC]] | [[yizhiyanhua-ai-fireworks-tech-graph|fireworks]] | [[cocoon-ai-architecture-diagram|cocoon]] |
|------|-----------|-----|-----|-----|
| 定位 | 持久记忆插件（单功能纵深） | 生产级配置包（183 skills 广度） | Skill 工程化范本（分层） | 极简单用途 Skill |
| 规模 | 211 MB | ~60 files plugin | ~60 files repo | ~10 files |
| 核心价值 | 运行时 + hook 协同 | 配置 + Instinct 学习 | Skill 分层懒加载 | 设计系统即 Skill |
| 对 Ohmybrain 独家贡献 | **3-layer progressive disclosure + Subagent Contract + `<private>` tag** | Instinct 系统 + ECC_HOOK_PROFILE | 三层资源分离 | 单用途不分层反例 |

## 新建 concept 提案

**候选**：`progressive-disclosure-retrieval`——"索引→时序上下文→详情"三层渐进检索模式。

**论据**：
- 跨多处适用（wiki 查询 / MCP 设计 / agent 工具调用）
- [[skill-layered-resources]] 是 Skill 侧的分层；此概念是 **查询侧的分层**，正交互补
- claude-mem + smart-explore skill 两处已显式实现此模式（多源）

**当前 defer**：单源（仅 claude-mem 显式命名此模式），待再找 1 个独立源（Anthropic 官方 Context Engineering 文档？）再创建。暂以本 summary 的 §1 承载。

## 推荐落地（按优先级）

| 优先级 | 行动 | 改动范围 |
|------|------|---------|
| P0 | `<private>` tag PreToolUse hook | 1 个 Python 脚本 + Hub/下游 settings.json |
| P1 | `llm-wiki` skill 加三层检索协议 | 改写 `~/.claude/skills/llm-wiki/SKILL.md` §Query |
| P1 | 下游 `plan-task` / `implement-task` 吸收 Phase 0 + Subagent Contract | 改 `ohmybrain-core/template/.claude/skills/` |
| P2 | Hub + 下游 CLAUDE.md 补"Exit Code Strategy"段 | 文档补充 |
| P3 | mode 系统试点 | 新目录 `modes/` |

## 相关概念

- [[claude-hooks-architecture]] — 5 lifecycle hooks 活例（含 Setup + Summary 等 Claude-mem 扩展点）
- [[subagents-orchestration]] — make-plan/do 的 Phase 0 + Subagent Reporting Contract
- [[skill-layered-resources]] — plugin/skills/ 7 skills 的分层实践对照

## 相关实体

- [[claude-code]] — 本仓是 Claude Code 插件生态中的"持久记忆"代表

## 引用摘录

> "NEVER fetch full details without filtering first. 10x token savings." — `plugin/skills/mem-search/SKILL.md`

> "Reject and redeploy the subagent if it reports conclusions without sources." — `plugin/skills/make-plan/SKILL.md`

> "COPY patterns from documentation, don't invent. If an API seems missing, STOP and verify — don't assume it exists." — `plugin/skills/do/SKILL.md`

> "Worker/hook errors exit with code 0 to prevent Windows Terminal tab accumulation. The wrapper/plugin layer handles restart logic." — `CLAUDE.md §Exit Code Strategy`
