# CLAUDE.md — Ohmybrain 知识库 + Hub

## 定位

Ohmybrain 是**个人知识库**和**项目导航中心**，不承载具体项目的代码和工程闭环。

## 三仓架构

```
ohmybrain-core（母仓/模板）
  ├→ 派生 → UWAcomm（自包含项目，H:\UWAcomm）
  └→ 派生 → 未来其他项目...

ohmybrain（本仓库 = 知识库 + Hub）
  ├── raw/          个人知识原料（只读）
  ├── wiki/         跨项目知识沉淀
  └── projects/     项目导航总览
```

## 不可违反的规则

- 不得修改 `raw/` 下的文件，除非用户明确要求
- 优先更新 `wiki/` 而非在对话中重复分析
- 知识变更必须同步更新 `wiki/index.md` 和 `wiki/log.md`
- 所有 wiki 内容用中文撰写

## 目录地图

| 目录 | 职责 |
|------|------|
| `raw/` | 只读原始资料（论文、文章、视频转录、代码仓库参考等） |
| `wiki/` | 跨项目知识层（概念、实体、架构、研究地图、摘要、探索） |
| `projects/` | 项目导航（链接到各项目仓库，状态总览） |
| `scripts/` | 知识库自动化脚本（lint/sync/导入/转录/抓取） |

## 项目仓库映射

| 项目 | 仓库地址 | 本地路径 |
|------|---------|---------|
| UWAcomm | github.com/lyrenleigh-code/UWAcomm | `D:\Claude\TechReq\UWAcomm` |
| UWAnet | github.com/lyrenleigh-code/UWAnet | `D:\Claude\TechReq\UWAnet` |
| USBL | github.com/lyrenleigh-code/USBL | `D:\Claude\TechReq\USBL` |
| UWAcomm_usbl 🔒 | 私人，不公开 | `D:\Claude\TechReq\UWAcomm_usbl` |
| ohmybrain-core | github.com/lyrenleigh-code/ohmybrain-core | `D:\Claude\ohmybrain-core` |
| Pricing 🔒 | 私人，不公开 | `D:\Claude\DocProcess\Pricing` |
| PaperReview 🔒 | 私人，不公开 | `D:\Claude\DocProcess\PaperReview` |
| DigitalTwinGuide 🔒 | 私人，不公开 | `D:\Claude\DocProcess\DigitalTwinGuide` |
| FlowGen | 私人，不公开 | `D:\Claude\Tools\FlowGen` |

## 知识闭环

```
raw/ → ingest → wiki/ → query → promote → wiki/
```

具体项目的实验结论通过 promote 沉淀到本仓库的 wiki。

## 常用命令

| 命令 | 用途 |
|------|------|
| `python scripts/lint_wiki.py` | Wiki 结构检查 |
| `python scripts/sync_index.py` | 同步 index 页面计数 |
| `python scripts/transcribe.py <文件>` | Whisper 音视频转录 |
| `python scripts/scrape.py <URL>` | Firecrawl 网页抓取 |
| `python scripts/import-zotero.py` | Zotero 论文导入 |

## Hook Exit Code Strategy

所有 `scripts/*.py` hook 脚本遵循 Claude Code 的 exit code 契约（借鉴自 claude-mem，see `wiki/source-summaries/thedotmack-claude-mem.md` §5）：

| Exit | 含义 | 触发效果 |
|------|------|---------|
| **0** | 成功 / 优雅放行 | 继续执行，stdout 可见（SessionStart 上下文等） |
| **1** | 非阻断错误 | stderr 显示给用户，继续执行 |
| **2** | 阻断错误 | stderr 喂回 Claude 处理，阻止工具调用 |

**设计原则**：

- **宽松优先**：hook 遇未知输入（JSON 解析失败等）应 `exit 0` 放行，**不要阻断无关场景**
- **阻断谨慎**：只在**安全性 / 一致性**被破坏时 `exit 2`（如：`check_raw_write.py` 拦截 raw/ 写入 / `check_private_tags.py` 拦截 `<private>` 标签外泄 / `check_index_log_sync.py` 拦截 index 未同步）
- **提醒用 1**：非致命的"顺手提示"用 `exit 0` + stdout（如 `raw_ingest_reminder.py`），避免打断工作流
- **Windows Terminal 注意**：Windows 下大量非 0 exit 可能导致 tab 累积；副作用 hook 默认用 exit 0 + stdout 提示

当前 Hub hook 清单（2026-05-12）：

| 类型 | 脚本 | 时机 | 说明 |
|------|------|------|------|
| 🔴 阻断 | `check_raw_write.py` | PreToolUse Edit/Write | raw/ 写入拦截 |
| 🔴 阻断 | `check_private_tags.py` | PreToolUse Edit/Write | `<private>` 标签写入拦截 |
| 🔴 阻断 | `check_index_log_sync.py` | Stop | wiki/ 变更但 index/log 未同步 |
| 🟡 提醒 | `post_wiki_write.py` | PostToolUse Edit/Write | 写入 wiki 后自动 lint |
| 🟡 提醒 | `raw_ingest_reminder.py` | PostToolUse Bash | Bash 触及 raw/ 时提醒 `/ingest` |
| 🟡 提醒 | `commit_reminder.py` | Stop | wiki 未 commit 提醒 |
| 🟡 提醒 | `check_memory_log_gap.py` | Stop | memory 日期 vs wiki/log.md 缺口（2026-05-12 新增） |
| 🟢 注入 | `session_context.py` | SessionStart | 载入会话上下文 |

详见 `wiki/architecture/system-overview.md §Hub hooks`。
