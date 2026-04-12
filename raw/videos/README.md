# videos/ — 视频转录文本

## 存放内容
- YouTube 视频转录
- 本地视频/录像转录
- 课程视频转录

> **只存转录后的 markdown/txt，不存视频原件。**

## 来源工具

| 场景 | 工具 | 命令 |
|------|------|------|
| YouTube 视频 | Firecrawl (MCP) | `firecrawl scrape "URL" --format markdown` |
| 本地视频 / 隐私敏感 | Whisper (本地) | `whisper video.mp4 --language Chinese --output_format txt` |
| 快速在线处理 | VOMO AI | vomo.ai 上传处理 |

## 命名规范
```
YYYY-MM-DD-视频简称.md
```

示例：
```
2026-04-12-karpathy-intro-to-llms.md
2026-04-12-3b1b-neural-networks-01.md
```

## 文件结构建议
```markdown
# 视频标题

- **来源**：URL 或本地路径
- **时长**：
- **语言**：
- **转录工具**：Firecrawl / Whisper / VOMO AI

---

（转录正文，建议由 Claude Code 结构化处理后再存入）
```

## 处理流程
```
视频来源 → 转录工具 → raw/videos/xxx.md → /ingest-source → wiki/
```
