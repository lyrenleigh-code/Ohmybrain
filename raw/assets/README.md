# assets/ — 图片、图表与附件

## 存放内容
- 截图、示意图、架构图
- PDF 附件（非论文类）
- 数据文件（CSV、JSON）

## 来源
- 手动截图 / 下载
- 其他资料的附属文件

## 命名规范
```
YYYY-MM-DD-描述.扩展名
```

示例：
```
2026-04-12-transformer-architecture.png
2026-04-12-benchmark-results.csv
```

## 注意事项
- 大文件（>10MB）已在 .gitignore 中配置排除或使用 Git LFS
- 图片在 wiki 页面中通过相对路径引用：`![说明](../../raw/assets/文件名)`
- 数据文件建议附带同名 .md 说明文件
