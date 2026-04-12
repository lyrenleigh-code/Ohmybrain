# raw/ — 原始资料层

> **核心规则：raw/ 下所有文件只读，入库后不得修改或删除。**

本目录存放所有原始资料，按来源类型分目录。每份资料入库后，由 Claude Code 执行 ingest 流程生成对应的 wiki 页面。

## 目录总览

| 目录 | 存放内容 | 主要来源工具 | 文件格式 |
|------|----------|-------------|---------|
| `papers/` | 学术论文、技术报告 | Zotero | `.pdf`, `.md` |
| `articles/` | 网页文章、博客 | Readwise Reader | `.md` |
| `videos/` | 视频转录文本 | Firecrawl / Whisper / VOMO AI | `.md` |
| `podcasts/` | 播客转录文本 | Whisper / VOMO AI | `.md` |
| `books/` | 书籍笔记、章节摘要 | 手动 / Readwise | `.md` |
| `courses/` | 课程讲义、学习笔记 | 手动 | `.md` |
| `notes/` | 对话记录、会议笔记、个人思考 | 手动 | `.md` |
| `threads/` | 社交媒体长帖、推文串 | 手动 / Firecrawl | `.md` |
| `repos/` | 代码仓库、项目资料 | GitHub / 本地 | 项目目录 |
| `assets/` | 图片、图表、附件 | 手动 | `.png`, `.jpg`, `.svg`, `.pdf` |

## 通用命名规范

```
YYYY-MM-DD-简短标题.md
```

示例：
- `2026-04-12-attention-is-all-you-need.md`
- `2026-04-12-andrej-karpathy-llm-os.md`

## 入库流程

1. 将文件放入对应子目录
2. 执行 `/ingest-source raw/{type}/{filename}`
3. Claude Code 自动生成 source-summary、概念页，并更新 index 和 log
