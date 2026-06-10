---
type: architecture
created: 2026-05-24
updated: 2026-06-09
tags: [约定, conventions, 跨项目]
---

# 跨项目约定

命名 / 目录 / commit / PR / 工作流 / worktree / 私人项目 等跨项目共享约定。**事实源 = `~/.claude/rules/common/*.md`**（全局规则），本页是 Hub wiki 的索引 + 项目级扩展。

> [!note] 全局资源规模（@2026-06-09）
> `~/.claude/` 当前承载：**auto-memory 78 个**（user 1 / feedback 21 / project 53 / reference 3，`MEMORY.md` 索引 78 行）、**rules 15 个目录**（common / zh / web + 12 语言：cpp / csharp / dart / golang / java / kotlin / perl / php / python / rust / swift / typescript）、**agents 55 个 .md**、**skills 本地 31 个**（33 个目录、其中 31 含 `SKILL.md`；叠加 `ecc:*` plugin / marketplace 注入后约 90+，**两层须区分**，不可裸写 90+）。详见 [[../topics/harness-resources]]。

## 1. 命名约定

| 类别 | 约定 | 例 |
|------|------|---|
| **项目目录** | 见 `D:\Claude\CLAUDE.md` 项目清单 | `TechReq/UWAcomm` / `DocProcess/Pricing` / `Tools/FlowGen` |
| **wiki 文件名** | kebab-case，无空格无 `.md` 后缀（在 wikilink 中） | `decision-log.md` → `[[decision-log]]` |
| **spec 文件名** | `YYYY-MM-DD-<slug>.md` | `2026-05-24-hub-brain-clarify.md` |
| **commit message** | conventional commits | `feat: xxx` / `fix: xxx` / `docs: xxx` / `chore: xxx` / `refactor: xxx` |
| **memory 文件名** | `<type>_<slug>.md`（type ∈ user / feedback / project / reference） | `feedback_uwacomm_worktree_ownership.md` |

## 2. 目录约定

| 目录 | 用途 | 规则 |
|------|------|------|
| `raw/` | 原始资料 | **只读**（PreToolUse hook 拦截） |
| `wiki/` | 知识层 | 改动必同步 `index.md` + `log.md`（Stop hook） |
| `specs/active/` | 进行中任务 | 单职责，验收后转 archive |
| `specs/archive/` | 已归档任务 | 不删除，按 date sort |
| `plans/active/` | 进行中实现计划 | 非平凡任务才需要 |
| `plans/archive/` | 已归档计划 | 与 spec 归档节奏保持一致 |
| `handoff/active/` | Agent / 跨会话交接单 | Claude Code 与 Codex 串行或并行交接时使用 |
| `handoff/archive/` | 已关闭交接单 | 交接完成后归档 |
| `scripts/` | 自动化 | hooks + utilities（Hub 当前 22 个 .py） |
| `output/` | 交付物（如适用） | 通常不 commit binary（除 demo） |
| `.claude/` | harness | rules / skills / hooks / agents / settings.json |

> Hub wiki 当前共 **109 个 .md**：根 `index.md` + `log.md` 2 个 + 107 个内容页（architecture 12 / agents 1 / workflows 1 / concepts 20 / entities 8 / explorations 4 / mcp-entities 25 / source-summaries 31 / topics 5 / comparisons 0）。计数随写入变化，以 `index.md` 同步值为准。

## 3. Wiki 写作约定

来源：`~/.claude/rules/common/*` + Hub wiki 规则。

| 项 | 约定 |
|---|------|
| 语言 | **中文为主**（专业术语保留英文） |
| frontmatter | 必含 `type` / `created` / `updated` / `tags` |
| wikilink | `[[slug]]` 不带 `.md` 后缀 |
| 至少一个 link | 每个新页面至少 1 个 `[[wikilink]]` 到相关页 |
| 矛盾标注 | 用 `> [!warning]` 不静默覆盖 |
| 摘要密度 | source-summary ≤ 200 行；详情页可更长但用层级分割 |
| 提炼 vs 搬运 | wiki 是**提炼**，不是 raw/ 的复制 |
| ADR 引用 | ADR 以章节形式（ADR-001 ~ ADR-026）存放在 [[decision-log]] 内，**引用一律写 `[[decision-log]]`**，不要写 `[[ADR-002]]` 这种悬空链接 |

## 4. 反模式约定（don't do）

详见 [[../concepts/anti-patterns]]。摘要：

- ❌ 跳过 specs 直接 code
- ❌ 代下"完成 / work"结论（用户主导）
- ❌ git commit / push 未授权
- ❌ 硬编码路径 `D:\TechReq\UWAcomm`（应 `D:\Claude\TechReq\UWAcomm`）
- ❌ `<private>` 内容进公开 wiki
- ❌ wiki 改动不同步 index / log
- ❌ 裸写 skills "90+"（须区分本地 31 vs 注入 90+）
- ❌ 引用悬空 ADR 链接 `[[ADR-002]]`（应 `[[decision-log]]`）

## 5. Commit / PR 风格

来源：`~/.claude/rules/common/git-workflow.md`。

### Commit message

```
<type>: <description>

<optional body>
```

Type: `feat` / `fix` / `refactor` / `docs` / `test` / `chore` / `perf` / `ci`

### PR

- 分析全 commit 历史不只 latest
- 用 `git diff [base]...HEAD` 看完整变化
- 包含 test plan TODOs
- 新 branch push 用 `-u`

### 破坏性操作

> commit / push / delete / force 必须明确授权
> "你执行吧"不自动含 git 操作

来源：memory `feedback_git_confirmation`。

## 6. 工作流约定

详见 [[dual-loop]]。摘要：

- **knowledge 闭环**: ingest → query → promote → review
- **engineering 闭环**: spec → plan → implement → validate
- 硬工序：`specs/active/<slug>.md` → `plans/active/<slug>.md`（如复杂）→ code → archive；跨 Agent / 跨会话时补 `handoff/active/<slug>.md`

## 7. 跨项目反向工程约定

- 新项目派生：按项目类型复制 `ohmybrain-core/template-engineering|template-document|template-tool/ → D:\Claude\<area>\<name>/`
- 项目内 wiki 与 Hub 不互相替代：项目 wiki = 项目级具体，Hub wiki = 跨项目可复用
- `/promote-answer` 只在下游项目，Hub 不向上回流

## 8. Hooks 约定

详见 [[../topics/harness-resources]] § Hooks。摘要：

| Exit Code | 含义 | 用法 |
|-----------|------|------|
| **0** | 成功 / 优雅放行 | 默认 |
| **1** | 非阻断错误 | 显示给用户，继续 |
| **2** | 阻断错误 | 喂回 Claude 处理，阻止工具调用 |

设计原则：宽松优先，阻断谨慎，提醒用 0 + stdout，Windows Terminal 慎用非 0。

## 9. 私人项目约定

🔒 标记的项目均为**私人 / 内网项目**，不公开。范围（见 `D:\Claude\CLAUDE.md` 项目清单）：

| 项目 | 性质 | git 状态 |
|------|------|---------|
| `DocProcess/Pricing` 🔒 | 私人（四号文报价） | 私有 |
| `DocProcess/UWAprojDoc` 🔒 | 私人（方案技术文档） | 私有 |
| `DocProcess/CooperativeDetection` 🔒 | 私人（协同探测方案） | 私有 |
| `DocProcess/PaperReview` 🔒 | 私人（学位论文外审） | 私有 |
| `DocProcess/DigitalTwinGuide` 🔒 | 私人（数字孪生指南） | 私有 |
| `DocProcess/DigitalTwin1plusN` 🔒 | 私人（「1+N」集群孪生体系） | 私有 |
| `DocProcess/VisioForge` 🔒 | 私人（通用 Visio 出图工作区） | 私有 |
| `DocProcess/CooperativeASW` 🔒 | 私人（编队协同探潜分系统方案） | 私有 |
| `TechReq/UWAcomm_usbl` 🔒 | **内网 Internal**（UWAcomm+USBL 联合仿真） | 私有，不公开 |
| `TechReq/SonarSim` 🔒 | 私人（主动声呐界面仿真） | 私有 |
| `Patents` 🔒 | 私密专利交底书 | **无 git** |

### 红线

- ❌ 禁止 push 到任何公开远程仓库
- ❌ 禁止 `/promote-answer` 把原文回流到 Hub 公开 wiki
- ❌ `Patents/` 无 git：禁止 `git init` / 引入版本追踪（避免泄露草稿历史）
- ✓ `<private>` 标签强制拦截（`check_private_tags.py`）

### 脱敏 promote 的具体步骤

私人项目的**通用方法论 / 算法卡片 / 工具经验**仍可沉淀到 Hub，但必须走脱敏路径，且**用户手动确认后**才落 Hub：

1. **抽象**：剥离项目名、客户名、密级标识、具体参数表、内网路径，只留可复用的结论 / 方法 / 模式。
2. **改写**：用通用占位（如"某 N 吨级 AUV 课题"代替真实型号），数值改为量级 / 趋势（如"NMSE 降一个量级"而非具体值）。
3. **自检 `<private>`**：确认产出文本无 `<private>` 标签、无密级词、无可反推真实工程的细节；`check_private_tags.py` 是兜底，不是替代人工。
4. **用户确认**：把脱敏后的 wiki 草稿交用户审，**用户点头**才写入 `wiki/`。
5. **落盘 + 同步**：写入对应 `wiki/<分类>/`，同步 `index.md` + `log.md`，**不携带任何指向私有仓库的反链**。

> [!warning] 数值簇 = 可反推指纹（2026-06-09 DOA promote 实践）
> 步骤 2「数值改量级」要看**数值簇整体**而非逐个：单个数值看似量级（如 ~37° / ~7° / 1.5°），但一组高辨识度精确值 + 实验结构（如「两距离 / 距离翻倍」「方位 4–8° 密采」）成簇出现，仍能把读者收敛到**唯一一次真实试验**。脱敏须连数据集结构指纹（距离档数 / 倍率关系 / 精确角栅格度数）一并抹掉，并整体再降一档到趋势 / 量级。**leak-safety 优先于 credibility**——可反推性的风险高于 Hub 页数值可信度的收益，精确值留项目归档。对抗验证时单设「脱敏泄漏」lens 专扫此类数值簇。

## 10. Worktree 约定

UWAcomm 与 UWAcomm_usbl 采用 git worktree 隔离协作。来源：memory `feedback_uwacomm_worktree_ownership`（UWAcomm 三路，跨 Agent 隔离）+ `feedback_uwacomm_usbl_worktree_ownership`（UWAcomm_usbl 双轨，同 claude 跨会话分工）。

### 归属映射表

| 工作目录 | 分支 | 归属 | 写权限 |
|---------|------|------|--------|
| `TechReq/UWAcomm` | 用户决定 | **用户主仓** | 仅用户；claude / codex 改动须先征同意 |
| `worktrees/UWAcomm-codex` | `codex-uwacomm-work-*` | codex 工作树（**并行实验**） | codex 自由读写自己分支 |
| `worktrees/UWAcomm-claude` | `claude-uwacomm-work-*` | claude 工作树（**自主迭代，允许代跑 MATLAB + 决策迭代**，保留"不代下结论"边界） | claude 自由读写自己分支 |
| `TechReq/UWAcomm_usbl` | `main` | **原窗口**：V0.x 大纲 / wiki / STATUS / _extracted / raw / git push | 仅原窗口改 |
| `worktrees/UWAcomm_usbl-design` | `design/v1.x` | **design 修订窗口**：仅 `docs/design-plan/` 13 章 | 仅 design 窗口改该目录 |
| `worktrees/UWAcomm_usbl-calibration` | `calibration/v1.x` | **calibration 窗口**：CAGE5 阵元位置 LS 校准算法（留分支瞄 12 月国产化，HEAD `eae7080` 未 push） | 仅 calibration 窗口改该算法 |

UWAcomm_usbl-design baseline：`dd0f7af`（落地 5/8–5/11 设计方案 V1.1 + V0.4 水池大纲）。

### 规则

- **主仓修改须经用户同意**：`TechReq/UWAcomm` 是用户的 source of truth，不是 claude / codex 的工作区；任何写主仓的操作（切分支 / commit / merge / 改文件）都先停下询问。
- **进任务先确认所在 worktree**：`pwd` 确认在哪个工作目录，再动手。
- **UWAcomm 三路（跨 Agent）**：claude / codex 各自分支隔离，互不写对方与主仓；集成走 PR / merge / cherry-pick，由用户审。
- **UWAcomm_usbl 双轨（同 claude 跨会话）**：design 窗口只读不写 V0.4 / wiki / STATUS / _extracted / raw / 其他 `docs/` 子目录；原窗口不直接改 `docs/design-plan/`，等 design 收敛后合流。
- **边界冲突守则**：frontmatter `status` / `updated` 这类两边都想改的字段，一律守"design 改 design-plan/ 内 frontmatter，main 改外部状态文档"边界。

## 相关页面

- [[hub-as-brain]] — 大脑功能定位（本页是其中之一）
- [[dual-loop]] — 双闭环工作流约定的源头
- [[decision-log]] — 架构决策记录（ADR-001 ~ ADR-026 章节）
- [[../concepts/anti-patterns]] — 反模式约定（don't do）
- [[../topics/harness-resources]] — harness 资源规模 + Hooks 约定来源
- [[document-protocol]] — 项目文档结构协议（骨架 / 状态归属 / 迁移级别）
- [[../agents/claude-codex-collaboration]] — Claude+Codex 协作协议（worktree 规则 / 审查 / 完成契约）
- `~/.claude/rules/common/*` — 全局规则（事实源）
