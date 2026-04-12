---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, 文献管理, 论文]
entity_type: tool
---

# Zotero

开源的文献管理工具，是 my-brain 系统中**论文和 PDF 的专属管理器**。

## 角色定位

Zotero 自动抓取论文 metadata（标题、作者、DOI、摘要），导出时比手动整理干净得多，直接作为 source-summary 的基础信息。

## 工作流

1. 浏览器插件一键收藏论文
2. 自动下载 PDF 到本地
3. 定期将 PDF 复制到 `raw/papers/`，触发 ingest 流程

## 与 my-brain 的连接

- Zotero 管原始 PDF 和 metadata
- `raw/papers/` 只存 PDF 副本
- source-summary 页引用 Zotero 条目 ID，方便反查

## 当前论文库规模

根据 [[zotero-library-catalog.md|Zotero 论文库清单]]：总条目 5660 篇，64 个文件夹，覆盖 [[underwater-acoustic-communication]]、[[channel-estimation-and-equalization]]、[[signal-processing-fundamentals]] 等核心研究方向。

## 来源

- [[toolchain.md|工具链指南]] — 描述了 Zotero 的角色和工作流
- [[zotero-library-catalog.md|论文库清单]] — Zotero 库的完整结构化目录
