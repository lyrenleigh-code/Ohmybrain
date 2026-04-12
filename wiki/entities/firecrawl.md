---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, 视频转录, MCP]
entity_type: tool
---

# Firecrawl

网页抓取和转换工具，支持 MCP server，是 my-brain 系统中 **YouTube 视频转 markdown 的首选方案**。

## 角色定位

Firecrawl 可直接连接 [[claude-code]]，在 ingest 工作流里不需要额外手动操作，是 AI agent 工作流中最灵活的选项。

## 工作方式

```bash
# 通过 CLI 直接输出 markdown
firecrawl scrape "https://youtube.com/watch?v=xxxx" --format markdown
```

或在 Claude Code 里通过 MCP 调用，直接把转录结果写入 `raw/videos/`。

## 适用场景

- YouTube 视频（有字幕或自动字幕）
- 需要接入 Claude Code 自动化工作流的场景

## 来源

- [[toolchain.md|工具链指南]] — 描述了 Firecrawl 的角色和 MCP 集成方式
