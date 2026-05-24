---
type: architecture
created: 2026-05-24
updated: 2026-05-24
tags: [约定, conventions, 跨项目]
---

# 跨项目约定

命名 / 目录 / commit / PR / 工作流 等跨项目共享约定。**事实源 = `~/.claude/rules/common/*.md`**（全局规则），本页是 Hub wiki 的索引 + 项目级扩展。

## 1. 命名约定

| 类别 | 约定 | 例 |
|------|------|---|
| **项目目录** | 见 `D:\Claude\CLAUDE.md` 项目清单 | `TechReq/UWAcomm` / `DocProcess/Pricing` / `Tools/FlowGen` |
| **wiki 文件名** | kebab-case，无空格无 `.md` 后缀（在 wikilink 中） | `single-root-cause-audit.md` → `[[single-root-cause-audit]]` |
| **spec 文件名** | `YYYY-MM-DD-<slug>.md` | `2026-05-24-hub-brain-clarify.md` |
| **commit message** | conventional commits | `feat: xxx` / `fix: xxx` / `docs: xxx` / `chore: xxx` / `refactor: xxx` |

## 2. 目录约定

| 目录 | 用途 | 规则 |
|------|------|------|
| `raw/` | 原始资料 | **只读**（PreToolUse hook 拦截） |
| `wiki/` | 知识层 | 改动必同步 `index.md` + `log.md`（Stop hook） |
| `specs/active/` | 进行中任务 | 单职责，验收后转 archive |
| `specs/archive/` | 已归档任务 | 不删除，按 date sort |
| `plans/` | 实现计划 | 非平凡任务才需要 |
| `scripts/` | 自动化 | hooks + utilities |
| `output/` | 交付物（如适用） | 通常不 commit binary（除 demo） |
| `.claude/` | harness | rules / skills / hooks / agents / settings.json |

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

## 4. 反模式约定（don't do）

详见 [[../concepts/anti-patterns]]。摘要：

- ❌ 跳过 specs 直接 code
- ❌ 代下"完成 / work"结论（用户主导）
- ❌ git commit / push 未授权
- ❌ 硬编码路径 `D:\TechReq\UWAcomm`（应 `D:\Claude\TechReq\UWAcomm`）
- ❌ `<private>` 内容进公开 wiki
- ❌ wiki 改动不同步 index / log

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
- 硬工序：`specs/active/<slug>.md` → `plans/<slug>.md`（如复杂）→ code → archive

## 7. 跨项目反向工程约定

- 新项目派生：`cp -r ohmybrain-core/template/ → D:\Claude\<area>/<name>/`
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

DocProcess/* 全 🔒 私人项目：
- ❌ 禁止 push 任何公开远程仓库
- ❌ 禁止 `/promote-answer` 回流到 Hub 公开 wiki
- ✓ 可走"脱敏 + 用户手动 promote" 路径
- ✓ `<private>` 标签强制拦截

## 10. Worktree 约定

详见 V4 PPT S36 worktree 三路。摘要：

- **main**: 用户主导，授权才改
- **exp** (UWAcomm-claude 类): Claude 自主迭代，不修主 main
- **dev** (UWAcomm-codex 类): Codex 并行实验，不修主 main
- 集成：周期性 merge / cherry-pick

## 相关页面

- [[hub-as-brain]] — 大脑功能定位（本页是其中之一）
- [[dual-loop]] — 双闭环工作流约定的源头
- [[../concepts/anti-patterns]] — 反模式约定（don't do）
- `~/.claude/rules/common/*` — 全局规则（事实源）
