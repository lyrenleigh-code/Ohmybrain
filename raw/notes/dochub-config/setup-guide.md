# DocHub 首次搭建指南

## 前置要求

- [x] Zotero 桌面端已安装
- [x] Obsidian 已安装，vault 在 `D:\Obsidian\workspace\`
- [ ] Python 3.10+ 已安装

## 搭建步骤

### Step 1: 安装 Python（5 分钟）

1. 访问 https://www.python.org/downloads/
2. 下载 Python 3.12+（Windows installer, 64-bit）
3. 安装时**勾选 "Add Python to PATH"**
4. 验证：打开终端，运行 `python --version`

### Step 2: 安装 Zotero 插件（15 分钟）

按照 `config/zotero-setup.md` 操作：

1. 安装 Better BibTeX
2. 配置 citekey 格式为 `auth.lower + year + shorttitle(1,1)`
3. 刷新所有现有条目的 citekey

### Step 3: 安装 Obsidian 插件（20 分钟）

按照 `config/obsidian-plugins.md` 操作：

1. 安装 Zotero Integration
2. 安装 Dataview
3. 安装 Templater
4. 配置各插件参数

### Step 4: 部署模板（5 分钟）

将本项目的模板复制到 Obsidian vault：

```bash
# 备份现有模板
copy "D:\Obsidian\workspace\Templates\paper-note.md" "D:\Obsidian\workspace\Templates\paper-note.md.bak"

# 部署新模板
copy "D:\Claude\Document\templates\paper-note.md" "D:\Obsidian\workspace\Templates\paper-note.md"
copy "D:\Claude\Document\templates\algorithm-card.md" "D:\Obsidian\workspace\Templates\algorithm-card.md"
```

### Step 5: 验证（10 分钟）

1. 打开 Zotero 桌面端
2. 在 Obsidian 中按 `Ctrl+Shift+Z`
3. 搜索一篇已有论文
4. 确认笔记在 `3-Resources/论文笔记/` 生成
5. 确认 zotero:// 链接可跳转

### Step 6: 整理 Zotero 分类（可选，1-2 小时）

在 Zotero 中建立 Collection 层级：
- 参考 CLAUDE.md 中的 "Zotero Collection 层级" 章节
- 将 `D:\TechReq\UWAcomm\refrence\` 下的 PDF 导入 Zotero

## 搭建完成检查

- [ ] `python --version` 输出 3.10+
- [ ] Zotero Better BibTeX citekey 格式正确
- [ ] Obsidian `Ctrl+Shift+Z` 可生成论文笔记
- [ ] 论文笔记包含 Zotero 链接字段
- [ ] Dataview 查询在预览模式正常渲染
- [ ] algorithm-card 模板出现在 Templater 模板列表中
