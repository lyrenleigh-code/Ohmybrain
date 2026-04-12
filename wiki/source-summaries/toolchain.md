---
type: source-summary
created: 2026-04-12
updated: 2026-04-12
tags: [工具链, 工作流, harness-engineering, llm-wiki]
source_type: note
---

# my-brain 工具链指南

- **来源**：raw/notes/toolchain.md
- **日期**：2026-04-12
- **类型**：笔记
- **原始文件**：raw/notes/toolchain.md

## 核心观点

1. **总体架构**：三层流水线——原始资料来源（论文、文章、视频）→ 收集与管理工具（Zotero、Readwise Reader、Firecrawl/Whisper）→ 沉淀与执行层（Claude Code ingest → wiki/ → Obsidian 可视化 + GitHub 同步）。
2. **各工具职责明确，交接点统一为 markdown 文件**：
   - [[zotero]] — 管论文原件和 metadata，输出 PDF 到 raw/papers/
   - [[readwise-reader]] — 清洗网页文章，输出带高亮的 markdown 到 raw/articles/
   - [[whisper]] — 本地视频转录，隐私安全，输出文本到 raw/videos/
   - [[firecrawl]] — YouTube 视频转 markdown，支持 MCP 接入 Claude Code
   - VOMO AI — 在线快速视频转结构化 markdown（偶发需求）
   - [[claude-code]] — 执行 ingest / harness / 编程，是整个系统的中枢
   - [[obsidian]] — 浏览和可视化 wiki，Git 插件实现自动同步
   - [[github]] — 私有仓库存放、Actions 自动 lint、版本历史
3. **视频处理方案分层**：YouTube 视频用 Firecrawl（MCP），本地/敏感视频用 Whisper（本地），偶发需求用 VOMO AI（在线）。
4. **最小起步顺序**：Obsidian + Git → Readwise Reader → Whisper/Firecrawl（按需）→ Zotero（按需），渐进式扩展工具链。
5. **多设备同步**：全部通过 git 完成，不依赖云同步服务。Obsidian Git 插件可自动 commit/pull。

## 相关概念

- [[harness-engineering]] — 工具链的架构设计体现了 harness 思想：每个工具只做一件事，通过 markdown 文件标准化交接
- [[llm-wiki]] — 工具链最终服务的知识沉淀层

## 相关实体

- [[claude-code]] — 执行引擎，系统中枢
- [[obsidian]] — wiki 可视化层
- [[zotero]] — 论文管理
- [[readwise-reader]] — 文章收集与清洗
- [[whisper]] — 本地视频转录
- [[firecrawl]] — YouTube 视频转 markdown
- [[github]] — 同步与自动化

## 引用摘录

> 每个工具只做自己最擅长的那一件事，交接点通过 markdown 文件完成。

> Zotero 自动抓取论文 metadata（标题、作者、DOI、摘要），导出时比手动整理干净得多，直接作为 source-summary 的基础信息。

> 直接把网页扔进 raw/ 格式太乱，Readwise 先做清洗，导出的是干净的 markdown，带高亮和注释，ingest 质量更高。
