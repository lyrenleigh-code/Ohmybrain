# Zotero 插件配置指南

## 1. Better BibTeX

### 安装

1. 下载：https://retorque.re/zotero-better-bibtex/installation/
2. Zotero → 工具 → 附加组件 → 齿轮图标 → Install Add-on From File → 选择 .xpi 文件
3. 重启 Zotero

### 配置 citekey

1. Zotero → 编辑 → 设置 → Better BibTeX
2. Citation key format 设为：

```
auth.lower + year + shorttitle(1,1)
```

示例输出：
- `rangan2011generalized`
- `raviteja2018interference`
- `tuchler2002minimum`

3. 勾选 "On item change" → "within pandoc/LaTeX citation key characters"
4. 点击 "Refresh BibTeX key" 刷新所有现有条目

### 自动导出 .bib（可选）

1. 右键点击 "我的文库" → Export Library
2. 格式选 "Better BibTeX"
3. 勾选 "Keep updated"
4. 导出路径：`D:\Obsidian\workspace\Attachments\library.bib`

## 2. Zotero PDF Translate（可选）

### 安装

1. 下载：https://github.com/windingwind/zotero-pdf-translate/releases
2. 同上方式安装 .xpi
3. 设置 → Translate → 翻译引擎选择（推荐：Google 或 DeepL）

## 验证

安装完成后检查：
- [ ] 每篇论文条目右侧面板显示 "Citation Key" 字段
- [ ] citekey 格式符合 `author+year+word` 规范
- [ ] 新添加的论文自动生成 citekey
