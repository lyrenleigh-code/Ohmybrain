# CLAUDE.md — my-brain 操作手册

## 仓库地图

| 目录 | 用途 |
|------|------|
| `raw/` | 原始资料，只读，不得修改 |
| `wiki/` | 知识沉淀层，所有推理从这里读 |
| `workflows/` | 操作流程文档 |
| `scripts/` | 自动化脚本 |

## 工具链架构

```
原始资料来源              收集 & 管理              沉淀 & 执行
──────────────           ──────────────           ──────────────
论文 / PDF          →    Zotero               →   raw/papers/
网页文章            →    Readwise Reader      →   raw/articles/
YouTube 视频        →    Firecrawl (MCP)      →   raw/videos/
本地视频 / 录像     →    Whisper (本地)       →   raw/videos/
播客 / 音频         →    Whisper / VOMO AI    →   raw/podcasts/
书籍笔记            →    Readwise / 手动      →   raw/books/
课程讲义            →    手动                 →   raw/courses/
社交媒体长帖        →    Firecrawl / 手动     →   raw/threads/
代码仓库 / 项目     →    GitHub               →   raw/repos/
对话 / 会议 / 思考  →    手动                 →   raw/notes/
图片 / 附件         →    手动                 →   raw/assets/
                              │
                              ▼
                         Claude Code
                        (ingest / harness)
                              │
                              ▼
                           wiki/
                              │
                    ┌─────────┴─────────┐
               Obsidian             GitHub
              (可视化)             (同步 / CI)
```

## 各工具职责边界

| 工具 | 只做这一件事 |
|------|-------------|
| Zotero | 管论文原件和 metadata |
| Readwise Reader | 清洗文章/书籍，产出带高亮的 markdown |
| Whisper | 本地音视频转录，隐私安全 |
| Firecrawl | YouTube / 网页转 markdown，接入 Claude Code (MCP) |
| VOMO AI | 快速在线音视频转结构化 markdown |
| Claude Code | 执行 ingest / promote / lint / 编程 |
| Obsidian | 浏览和可视化 wiki |
| GitHub | 多设备同步和 CI 自动化检查 |

**交接点统一为 markdown 文件，所有工具通过 raw/ 目录交接。**

## raw/ 目录结构

| 目录 | 内容 | 来源工具 | 文件格式 |
|------|------|---------|---------|
| `raw/papers/` | 学术论文、技术报告 | Zotero | `.pdf`, `.md` |
| `raw/articles/` | 网页文章、博客 | Readwise Reader | `.md` |
| `raw/videos/` | 视频转录文本（不存原件） | Firecrawl / Whisper / VOMO AI | `.md` |
| `raw/podcasts/` | 播客转录文本（不存原件） | Whisper / VOMO AI | `.md` |
| `raw/books/` | 书籍笔记、章节摘要 | Readwise / 手动 | `.md` |
| `raw/courses/` | 课程讲义、学习笔记 | 手动 | `.md` |
| `raw/notes/` | 对话记录、会议笔记、个人思考 | 手动 | `.md` |
| `raw/threads/` | 社交媒体长帖、推文串 | Firecrawl / 手动 | `.md` |
| `raw/repos/` | 代码仓库、项目资料 | GitHub / 本地 | 项目目录 |
| `raw/assets/` | 图片、图表、附件 | 手动 | `.png`, `.jpg`, `.csv` |

**通用命名规范：** `YYYY-MM-DD-简短标题.md`

## 核心规则

1. **raw/ 目录只读**：任何情况下不得修改或删除 raw/ 下的文件。
2. **更新 wiki 必须同步更新 index**：每次新增或修改 wiki/ 下的文件，必须同步更新 wiki/index.md。
3. **所有变更必须记入 log**：每次操作结束前，在 wiki/log.md 末尾追加一条记录，格式为 `- YYYY-MM-DD: [操作描述]`。
4. **优先读 wiki**：回答问题时优先从 wiki/ 读取，不足时才回到 raw/ 补充证据。
5. **高价值回答要 promote**：如果一次对话产生了重要结论，必须将其写回 wiki/，不能只停留在聊天记录里。

## 命名约定

- raw 资料文件名：`YYYY-MM-DD-简短标题.md`
- wiki 页面文件名：全部小写，用连字符分隔，例如 `harness-engineering.md`
- source-summaries：与 raw 文件名对应，例如 `paper-attention-is-all-you-need.md`
- 概念页标题格式：`# 概念名称`
- log 条目格式：`- YYYY-MM-DD: [操作]`

## 禁止行为

- 不得直接修改 raw/ 下任何文件
- 不得在没有更新 index.md 和 log.md 的情况下结束任务
- 不得凭记忆回答可以从 wiki 验证的问题
