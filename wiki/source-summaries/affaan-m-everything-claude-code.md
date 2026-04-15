---
type: source-summary
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, Agent-Harness, Skill, Command, Hook, MCP, ECC, 黑客松冠军, 生产级配置]
source_type: repo
---

# Everything Claude Code (ECC) — AI 代理 Harness 性能优化系统

## 来源信息

- **仓库**：`github.com/affaan-m/everything-claude-code`
- **本地路径**：`raw/repos/affaan-m-everything-claude-code`
- **作者**：Affaan Mustafa（2025 年 Anthropic × Forum Ventures 黑客松冠军，`zenith.chat` 联合创始人）
- **许可**：MIT
- **最新版本**：v1.10.0（2026-04 发布；读 `VERSION` 文件确认，无 git tag）
- **规模**：仓库深度被限制到 1 commit（本地影子）；上游 **140k+ stars / 21k+ forks / 170+ contributors**、997+ 内置测试
- **npm 包**：`ecc-universal`（核心）+ `ecc-agentshield`（安全扫描）
- **官方插件标识**：`everything-claude-code@everything-claude-code`
- **定位**："**agent harness performance system**"——不只是配置集合，而是围绕 Claude Code 等 harness 的**性能优化完整方案**（skills / instincts / memory / continuous learning / security scanning / research-first）

## 核心价值主张

> "Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development."

与 [[claude-code-best-practice]] 做"教科书式参考清单"的定位不同，ECC 是**经过 10+ 个月日均高强度使用打磨出的可直接部署生产配置包**。Affaan 用它构建真实产品（zenith.chat），然后把沉淀配置 OSS 化。

## 产品线（令人震撼的规模）

| 组件 | 数量（v1.10.0） | 说明 |
|------|---------------|------|
| **Agents** | 48 | 覆盖 planner / architect / tdd-guide / 各语言 reviewer + build-resolver / loop-operator / harness-optimizer / chief-of-staff / security-reviewer 等 |
| **Skills** | 183 | 从 tdd-workflow 到 brand-voice / investor-materials / market-research / continuous-learning-v2 / iterative-retrieval 等横跨工程 + 运营 |
| **Commands**（legacy shims） | 79 | `/plan`、`/tdd`、`/e2e`、`/orchestrate`、`/multi-plan`、`/harness-audit`、`/loop-start`、`/model-route` 等 |
| **Hooks** | 8 种 event + 20+ scripts | hooks.json 配置，Node.js 脚本 ≤200 行 |
| **Rules** | 29 文件 × 12 语言生态（common / typescript / python / golang / swift / php / java / kotlin / rust / cpp / csharp / dart / perl / web / zh） |
| **MCP configs** | 14 服务器（GitHub / Context7 / Exa / Memory / Playwright / Sequential Thinking / Supabase / Vercel / Railway / ...） |
| **跨 Harness 兼容** | Claude Code（原生）+ Codex app+CLI + Cursor + OpenCode + Gemini CLI + Antigravity IDE + 手动适配（Grok 等） |

## 架构哲学（与 ECC 文档直引）

1. **Agent-First**：默认委派给专精代理
2. **Test-Driven**：80%+ coverage 是硬门槛
3. **Security-First**：never compromise
4. **Immutability**：永远创建新对象
5. **Plan Before Execute**：复杂任务先规划
6. **Skills is the canonical workflow surface**：skills 是主工作流表面，commands 是**遗留 slash-entry 兼容层**，新工作流应先进 skills

## 三种扩展机制的工程化取舍

ECC 的目录结构印证 [[skills-vs-commands]] 中的三机制分工：

- `skills/` 是主力（183 个）——自动发现 + 可被 Claude 自动调用 + 可被 Agent 预加载
- `agents/` 做重活（48 个）——每个有专属领域 + 独立上下文 + 可限定 model/tools
- `commands/` 作为兼容层（79 个）——只为用户已习惯的 `/tdd`、`/plan`、`/code-review` 保持入口

> "New workflow contributions should land in `skills/` first" —— AGENTS.md §Workflow Surface Policy

这是对 [[subagents-orchestration]] "Command → Agent → Skill" 模式的**生产级验证**：当需要规模化时，skills 的语义匹配 + 可组合性胜出，commands 只剩"已知入口"的价值。

## 创新机制（ECC 独有）

### 1. Continuous Learning v2（Instinct 系统）

> "Continuous learning v2 — Instinct-based learning with confidence scoring, import/export, evolution"

- `/instinct-status`、`/instinct-import <file>`、`/instinct-export`、`/evolve`（把 instincts 聚类成 skill）、`/prune`（清理 30 天过期 pending instincts）、`/promote`（把项目 instinct 提到全局 scope）
- 核心机制：**PreToolUse 观察者 hook** 在每次工具调用时捕获 tool-use 模式，confidence scoring 跟踪"这个模式出现几次"，置信度达阈值后提示固化成 skill
- 与**传统** `continuous-learning` v1 区别：v1 是 Stop hook 批量提取；v2 是**逐步累积 + 跨会话共享**，支持 team 共享（export / import）

### 2. Memory Persistence（Session Lifecycle Hooks）

- `SessionStart` 钩子 → 加载上次结束的上下文
- `SessionEnd` / `PreCompact` → 压缩前持久化到外部存储
- 与 Claude Code v2.1.33+ 的原生 Agent Memory 形成**双层**：agent memory 是代理级长期记忆，session persistence 是会话级增量快照

### 3. Iterative Retrieval（解决子代理上下文问题）

`skills/iterative-retrieval/` — **渐进式上下文精炼**。问题：一次全塞给子代理过大；分多轮喂食又丢失整体视角。方案：子代理先拿需求摘要 + 索引，自己决定逐步 pull 所需片段。

### 4. Strategic Compact（替代默认 95% 自动压缩）

- 官方默认在 95% 上下文时自动 `/compact`，此时常处于**实现中期**会丢变量名/路径/部分状态
- ECC 通过**逻辑断点检测** hook 在"研究完 → 开始实现前"、"里程碑完成后"等时机**建议**手动 compact
- 配合 `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` 把 auto-compact 阈值提前到 50%，规避后段压缩

### 5. Search-First 开发

`/skills/search-first/` — 写代码前**强制走研究流程**：

```
NEED ANALYSIS → PARALLEL SEARCH (npm / MCP / GitHub) → EVALUATE → DECIDE (Adopt / Extend / Build Custom)
```

对应 development-workflow 第 0 步"Research & Reuse"的工程化固化，通过 `researcher` agent 并行执行。

### 6. Hook Runtime Controls（运行时门控）

```bash
export ECC_HOOK_PROFILE=minimal|standard|strict    # 默认 standard
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"
```

所有 hook 通过 `scripts/hooks/run-with-flags.js` 统一包装。**不需要编辑 hook 文件**即可临时调节严格度——比 claude-code-best-practice 的静态配置更灵活。

### 7. Selective Install（v1.9.0 起）

- Manifest-driven 安装管线（`install-plan.js` + `install-apply.js`）
- 5 个 install profile：`core` / `developer`（推荐）/ `security` / `research` / `full`
- 按语言选择性安装 rules：`./install.sh typescript python golang swift php`
- SQLite state store 跟踪"装了什么"，支持增量更新

### 8. NanoClaw v2（会话管理套件）

- 模型路由（`/model-route` 按复杂度/预算路由任务）
- Skill 热加载
- 会话 branch / search / export / compact / metrics

### 9. AgentShield（随 ECC 发布的安全扫描器）

- `npx ecc-agentshield scan` — 扫 CLAUDE.md / settings.json / MCP configs / hooks / agent / skills
- 5 类：secret 检测（14 模式）+ permission 审计 + hook 注入分析 + MCP 服务器风险 + agent config review
- `--opus` 模式：三个 Opus 4.6 agent 做 red-team / blue-team / auditor 流水线
- 1282 tests / 98% coverage / 102 static rules
- 独立 GitHub Marketplace 上架 `ecc-tools`（free / pro / enterprise 层级）

## 跨 Harness 一致性工程（罕见亮点）

> "ECC is the **first plugin to maximize every major AI coding tool**."

- **AGENTS.md** 作为**跨工具通用根文件**（Cursor / Codex / OpenCode 都原生读）
- **DRY Adapter Pattern**：Cursor 的 20 种 hook event 通过 `.cursor/hooks/adapter.js` 转成 Claude Code 8 种 event 格式，**复用** `scripts/hooks/*.js` 无重复
- Codex 没有 hook 能力 → 用 `AGENTS.md` + sandbox + approval 替代
- `scripts/sync-ecc-to-codex.sh` — add-only 策略合并 MCP 配置到 `~/.codex/config.toml`，**从不删**用户已有
- 跨 harness feature parity 表（README 第 1323 行）量化对比 Agents / Commands / Skills / Hooks / Rules / Custom Tools / MCP

## Token 优化策略（与 Ohmybrain 直接相关）

| 设置 | 默认 | ECC 推荐 | 影响 |
|------|------|---------|------|
| `model` | opus | **sonnet** | ~60% 成本降低（Sonnet 覆盖 80%+ 任务） |
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | ~70% 隐形 thinking 成本降低 |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 95 | **50** | 早期压缩 → 长会话质量更好 |
| `CLAUDE_CODE_SUBAGENT_MODEL` | — | **haiku** | 子代理用 Haiku 再省 |

这与 [[toolchain]]、 `.claude/rules/common/performance.md` 中的模型选择策略**完全一致**，但 ECC 量化到具体数值。

## MCP 精简建议（与 best-practice 相互印证）

> "Have 20-30 MCPs in config, but keep under 10 enabled / under 80 tools active. Your 200k context window might only be 70k with too many tools."

与 [[claude-code-best-practice]] "之前装 15 个，日常只用 4 个"**结论一致**——MCP 不是越多越好。ECC 支持 `disabledMcpServers` 项目级开关，比全局启用更灵活。

## 与 Ohmybrain 的连接点

### 可立即借鉴（低成本高回报）

1. **Instinct 系统 → 喂给 `/learn` 类命令**：本仓 `promote-answer` 是一次性固化，ECC 的**增量 + confidence scoring** 适合长周期积累（论文笔记的反复主题、USBL 算法的反复问题模式）
2. **Search-First 加入 `/ingest`**：当前 wiki-ingester agent 尚无前置搜索步骤；加入后可避免重复摘入（如同一论文不同版本）
3. **Hook Runtime Controls**：本仓可能需要 "严格模式 lint vs 宽松模式写稿" 切换——`OHMYBRAIN_HOOK_PROFILE=strict|draft` 可复用 ECC 模式
4. **Strategic Compact**：处理长时间 USBL 论文摘入会话（如 yumin-2006、huangjian-2019 等 9 篇批量）时用 `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` 避免中期丢上下文
5. **选择性安装 Manifest**：本仓当前 `install.sh` 是全量；借鉴 ECC 按模块 / 按语言 profile 可支持未来分发（若 Ohmybrain 配置包 OSS 化）

### 架构级启发（重大重构）

6. **Agent 级 Memory**：给 wiki-ingester / promote-answer 类自主代理加 `memory: user`（[[subagents-orchestration]] §Agent Memory），跨项目累积 ingest 经验（哪些论文类型需要哪种抽取策略）
7. **Harness-Optimizer Agent**：ECC 独有 `harness-optimizer` 代理专门调 harness 配置（可靠性 / 成本 / 吞吐）。Ohmybrain 本身即是 "harness + 知识库" 双重角色，有空间装一个
8. **OpenCode / Codex 兼容**：若将来希望 Ohmybrain 规则不只跑在 Claude Code 上，ECC 的 AGENTS.md + DRY adapter 是现成参考
9. **AgentShield 扫本仓**：现有 `scripts/lint_wiki.py` 只做结构检查，AgentShield 能扫 settings.json / MCP / hooks 配置里的注入风险和权限失当——可作为 pre-push hook 加入

### 差异点（ECC 不适合 Ohmybrain 的地方）

10. **规模失衡**：ECC 183 skills 覆盖跨行业（包括运营、财务、投资人材料）；Ohmybrain 是个人知识库，不需要这么广。**复制骨架（skills / agents / hooks 三大类），按需添细节**即可
11. **商业化集成**：ECC 有 ecc.tools GitHub App（付费）、sponsorship 层级；Ohmybrain 无此需求
12. **Instinct 投票 UI**：ECC 的 instinct 系统假设有团队场景（import / export / promote），单用户的 Ohmybrain 可简化到"本地置信度累积 + 自动 evolve"

## 派生概念页（已存在）

- [[skills-vs-commands]] — 三机制选择（ECC 的 skills-first 策略印证其 "skill 是最轻量" 的结论）
- [[subagents-orchestration]] — Agent 深入（ECC 的 48 agents + agent memory + harness-optimizer 是该模式的规模化版本）
- [[claude-hooks-architecture]] — Hooks 架构（ECC 的 runtime controls + profile 是该架构的工程化扩展）

## 与其他源的对照

| 对照对象 | 定位差异 | 互补角度 |
|---------|---------|---------|
| [[claude-code-best-practice]] | "参考清单"（文档 + 可运行样板） | ECC 是"生产配置包"（可直接 npm 安装全量部署） |
| [[nousresearch-hermes-agent]] | 自改进 Agent 本体（带模型 + 多平台） | ECC 是 harness 之上的**配置**层，不含模型 |
| [[yizhiyanhua-ai-fireworks-tech-graph]] | 单一 Skill 深度范本（1 SKILL + 10 refs + 10 templates） | ECC 是 skills 生态规模范本（183 skills 横跨多领域） |

> 三者共同指向：AI Agent 的竞争力从"模型能力"向"**harness 工程化**"转移。ECC 是**商业级 Claude Code harness 包**，Hermes 是**全栈独立 Agent**，yizhiyanhua 是**单一 skill 深度工艺**，claude-code-best-practice 是**文档化最佳实践**。

## 来源

- 参考仓库：`raw/repos/affaan-m-everything-claude-code/README.md`（1499 行）
- Agent 清单：`raw/repos/affaan-m-everything-claude-code/AGENTS.md`
- 变更日志：`raw/repos/affaan-m-everything-claude-code/CHANGELOG.md` + README §What's New
- 安全能力：`raw/repos/affaan-m-everything-claude-code/the-security-guide.md`（~30k 字）
- 轻量概览：`raw/repos/affaan-m-everything-claude-code/the-shortform-guide.md`（~16k 字）
- 深度指南：`raw/repos/affaan-m-everything-claude-code/the-longform-guide.md`（~15k 字）
- 仓库评估：`raw/repos/affaan-m-everything-claude-code/REPO-ASSESSMENT.md`（install profile 选择指南）
- 相关实体：[[claude-code]]
- 相关 summary：[[claude-code-best-practice]]、[[nousresearch-hermes-agent]]、[[yizhiyanhua-ai-fireworks-tech-graph]]
- 相关概念：[[skills-vs-commands]]、[[subagents-orchestration]]、[[claude-hooks-architecture]]
