---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, 文章收集, 阅读]
entity_type: tool
---

# Readwise Reader

网页文章的收集和高亮管理工具，是 my-brain 系统中**文章资料的清洗入口**。

## 角色定位

直接把网页扔进 raw/ 格式太乱，Readwise Reader 先做清洗，导出干净的 markdown，带高亮和注释，ingest 质量更高。

## 工作流

1. 浏览器扩展一键收藏文章
2. 阅读时打高亮、加注释
3. 定期导出带高亮的 markdown 到 `raw/articles/`
4. 触发 ingest 流程

## 导出设置建议

- 导出格式选 markdown
- 包含高亮和注释
- 文件名格式：`YYYY-MM-DD-article-title.md`

## 来源

- [[toolchain.md|工具链指南]] — 描述了 Readwise Reader 的角色和配置建议
