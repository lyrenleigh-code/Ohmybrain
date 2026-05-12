---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, 知识管理, 可视化]
entity_type: tool
---

# Obsidian

基于本地 markdown 文件的知识管理工具，是 my-brain 系统的**可视化和浏览层**。

## 角色定位

wiki/ 全是 markdown 文件，Obsidian 天然适配，没有格式转换成本。同一份文件在 git 仓库和 Obsidian 里完全一致。

## 必装插件

| 插件 | 用途 |
|------|------|
| Git | 自动定时 commit + push，多设备免手动同步 |
| Dataview | 把 index.md 变成动态查询，自动列出所有页面 |
| Templater | 给概念页、source-summary 页建模板，保持格式统一 |

## 配置建议

- 将 my-brain 仓库目录直接作为 Obsidian vault 打开
- Git 插件设置为每 10 分钟自动 commit，每次打开时自动 pull
- 用 Dataview 替代手动维护的 index.md 展示层（index.md 仍保留作 [[claude-code]] 导航用）

## 来源

- [[toolchain.md|工具链指南]] — 描述了 Obsidian 的角色和配置建议
- [[mermaid-js-mermaid]] — Obsidian 内置 Mermaid 预览,本 Hub 架构图(如 `memory-graph.md`)直接用其 DSL
