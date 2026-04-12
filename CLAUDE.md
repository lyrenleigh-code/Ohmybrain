# CLAUDE.md

## 仓库定位

本仓库同时承载三个职能：
1. **LLM Wiki** — `wiki/` 下的持久知识层
2. **原始资料库** — `raw/` 下的只读资料
3. **工程交付** — `specs/` → `plans/` → `src/` → `tests/` → `evals/` 的开发闭环

## 不可违反的规则

- 不得修改 `raw/` 下的文件，除非用户明确要求
- 优先更新 `wiki/` 而非在对话中重复分析
- 每个代码任务从 `specs/active/` 的 spec 开始
- 非平凡实现必须先有 `plans/` 下的计划
- 代码变更必须附带测试，或说明为何不需要测试
- 知识变更必须同步更新 `wiki/index.md` 和 `wiki/log.md`
- 交付物不完整时不要停止

## 目录地图

| 目录 | 职责 |
|------|------|
| `raw/` | 只读原始资料（论文、文章、视频转录、代码仓库等） |
| `wiki/` | 策展后的知识层（概念、实体、架构、模块、决策、摘要） |
| `specs/active/` | 当前任务的需求 spec |
| `specs/archive/` | 已完成的 spec |
| `plans/` | 实现计划 |
| `tasks/` | 任务追踪 |
| `src/` | 源代码 |
| `tests/` | 自动化测试 |
| `evals/` | Agent 和工作流评测 |
| `scripts/` | 自动化脚本 |
| `workflows/` | 操作流程文档 |
| `.claude/skills/` | 可复用工作流定义 |
| `.claude/rules/` | 路径特定规则 |
| `.claude/hooks/` | 确定性行为强制执行 |

## 两个闭环

### 知识闭环

```
raw/ → ingest → wiki/ → query → promote → wiki/
```

1. 新资料放入 `raw/`
2. 执行 `/ingest-source` 生成 wiki 页面
3. 查询时优先读 `wiki/`，不足时回 `raw/`
4. 高价值结论通过 `/promote-answer` 写回 `wiki/`

### 开发闭环

```
spec → plan → implement → test → validate → archive
```

1. 在 `specs/active/` 建 spec（目标、范围、验收标准）
2. 执行 `/plan-task` 生成 `plans/` 下的实现计划
3. 执行 `/implement-task` 修改 `src/`、`tests/`
4. 运行测试验证
5. 如架构或行为变更，同步更新 `wiki/`
6. spec 移入 `specs/archive/`

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
- 请求的文件已更新
- 相关测试通过
- wiki 已同步更新（如需要）
- 最终回复明确说明了变更内容
