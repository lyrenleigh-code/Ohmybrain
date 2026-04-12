# CLAUDE.md

## 仓库定位

本仓库同时承载三个职能：
1. **LLM Wiki** — `wiki/` 下的持久知识层
2. **原始资料库** — `raw/` 下的只读资料
3. **工程管理** — `projects/` 下按项目组织的任务管理 + 各项目仓库中的代码交付

## 不可违反的规则

- 不得修改 `raw/` 下的文件，除非用户明确要求
- 优先更新 `wiki/` 而非在对话中重复分析
- 每个代码任务先在 `projects/{项目名}/active/` 写任务文件
- 代码变更在对应项目仓库中执行，不在 Ohmybrain 的 src/ 中
- 知识变更必须同步更新 `wiki/index.md` 和 `wiki/log.md`
- 交付物不完整时不要停止

## 目录地图

| 目录 | 职责 |
|------|------|
| `raw/` | 只读原始资料（论文、文章、视频转录、代码仓库等） |
| `wiki/` | 策展后的知识层（概念、实体、架构、模块、决策、摘要） |
| `projects/{项目}/active/` | 当前进行中的任务（spec + plan + log + result 合一） |
| `projects/{项目}/archive/` | 已完成的任务 |
| `src/` | Ohmybrain 自身的源代码（脚本、工具） |
| `tests/` | Ohmybrain 自身的测试 |
| `evals/` | Agent 和工作流评测 |
| `scripts/` | 自动化脚本 |
| `workflows/` | 操作流程文档 |
| `.claude/skills/` | 可复用工作流定义 |
| `.claude/rules/` | 路径特定规则 |
| `.claude/hooks/` | 确定性行为强制执行 |

## 项目与仓库映射

| 项目 | 任务管理 | 代码仓库 |
|------|---------|---------|
| UWAcomm | `projects/uwacomm/` | `H:\UWAcomm` |
| Ohmybrain | `projects/ohmybrain/` | 本仓库 `src/` |

## 两个闭环

### 知识闭环

```
raw/ → ingest → wiki/ → query → promote → wiki/
```

详细流程见 `workflows/knowledge/`

### 开发闭环

```
projects/active/ 写任务 → 项目仓库改代码 → 测试 → wiki/ 沉淀 → projects/archive/
```

详细流程见 `workflows/engineering/`

### 任务文件结构

每个任务一个文件，包含四个阶段：

```markdown
## Spec     ← 需求（先写）
## Plan     ← 计划（确认后写）
## Log      ← 执行记录（过程中写）
## Result   ← 结论（完成后写，promote 到 wiki）
```

## 常用命令

| 命令 | 用途 |
|------|------|
| `python3 scripts/lint_wiki.py` | Wiki 结构检查 |
| `python3 scripts/sync_index.py` | 同步 index 页面计数 |
| `python3 scripts/validate_task.py` | 任务完成验证 |
| `python3 scripts/transcribe.py <文件>` | Whisper 音视频转录 |
| `python3 scripts/scrape.py <URL>` | Firecrawl 网页抓取 |

## 完成标准

一个任务只有满足以下全部条件才算完成：
- 代码变更已完成（在对应项目仓库中）
- 相关测试通过
- wiki 已同步更新（如需要）
- 任务文件的 Result 部分已填写
- 任务文件从 `active/` 移到 `archive/`
