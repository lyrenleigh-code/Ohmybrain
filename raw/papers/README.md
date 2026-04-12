# papers/ — 学术论文与技术报告

## 存放内容
- 学术论文 PDF 及其 markdown 摘要
- 技术白皮书、研究报告

## 来源工具
- **Zotero**：浏览器插件一键收藏 → 自动抓取 metadata → 导出 PDF 到此目录
- 手动下载：直接放入

## 命名规范
```
YYYY-MM-DD-论文简称.pdf        # PDF 原件
YYYY-MM-DD-论文简称.md         # Zotero 导出的 metadata + 摘要
```

示例：
```
2026-04-12-attention-is-all-you-need.pdf
2026-04-12-attention-is-all-you-need.md
```

## metadata 模板（.md 文件）
```markdown
# 论文标题

- **作者**：
- **年份**：
- **DOI**：
- **Zotero ID**：
- **摘要**：

## 关键内容

（由 Zotero 导出或手动填写）
```

## 注意事项
- PDF 原件较大，已在 .gitignore 中配置 Git LFS 或排除
- markdown 摘要文件必须保留，作为 ingest 的输入
