# articles/ — 网页文章与博客

## 存放内容
- 网页文章、技术博客、新闻报道
- 带高亮和批注的清洗后 markdown

## 来源工具
- **Readwise Reader**：浏览器扩展收藏 → 阅读时高亮/批注 → 导出 markdown 到此目录
- **Firecrawl**：通过 MCP 或 CLI 抓取网页内容为 markdown
- 手动：复制粘贴整理

## 命名规范
```
YYYY-MM-DD-文章简称.md
```

示例：
```
2026-04-12-karpathy-llm-wiki-pattern.md
2026-04-12-how-to-build-a-second-brain.md
```

## 文件结构建议
```markdown
# 文章标题

- **来源**：URL
- **作者**：
- **日期**：
- **标签**：

---

（正文内容，含高亮和批注）
```

## Readwise 导出设置
- 格式：Markdown
- 包含：高亮 + 注释
- 文件名格式：`YYYY-MM-DD-article-title.md`
