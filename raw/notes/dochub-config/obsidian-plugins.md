# Obsidian 插件配置指南

## 必装插件

### 1. Zotero Integration (mgmeyers)

#### 安装

Obsidian → 设置 → 第三方插件 → 浏览 → 搜索 "Zotero Integration" → 安装 → 启用

#### 配置

设置 → Zotero Integration：

1. **Database**:
   - Database Type: `Zotero`（不是 "Better BibTeX JSON"）

2. **Import Settings**:
   - Note Import Location: `3-Resources/论文笔记`
   - Image Import Location: `Attachments/zotero`

3. **Template**:
   - 配置论文笔记模板路径：`Templates/paper-note.md`

4. **快捷键**（建议）:
   - Obsidian → 设置 → 快捷键 → 搜索 "Zotero"
   - "Zotero Integration: Create Note" → `Ctrl+Shift+Z`
   - "Zotero Integration: Insert Citation" → `Ctrl+Shift+C`

#### 使用

1. 确保 Zotero 桌面端正在运行
2. 在 Obsidian 中按 `Ctrl+Shift+Z`
3. 弹出搜索框 → 输入论文标题或作者
4. 选择论文 → 自动在 `3-Resources/论文笔记/` 生成笔记
5. 笔记文件名为 citekey（如 `rangan2011generalized.md`）

### 2. Dataview

#### 安装

Obsidian → 设置 → 第三方插件 → 浏览 → 搜索 "Dataview" → 安装 → 启用

#### 配置

设置 → Dataview：
- Enable JavaScript Queries: `开启`
- Enable Inline Queries: `开启`

#### 常用查询示例

**列出所有论文笔记（按年份排序）**：
```dataview
TABLE authors, year, journal, status
FROM "3-Resources/论文笔记"
WHERE contains(tags, "论文")
SORT year DESC
```

**列出某方向的论文**：
```dataview
TABLE authors, year
FROM "3-Resources/论文笔记"
WHERE contains(tags, "信道估计")
SORT year DESC
```

**列出待读论文**：
```dataview
LIST
FROM "3-Resources/论文笔记"
WHERE status = "待读"
```

**列出自动生成的函数索引**：
```dataview
TABLE sync-source as "源文件", last-sync as "最后同步"
FROM "1-Projects/UWAcomm"
WHERE contains(tags, "函数索引")
```

### 3. Templater

#### 安装

Obsidian → 设置 → 第三方插件 → 浏览 → 搜索 "Templater" → 安装 → 启用

#### 配置

设置 → Templater：
- Template Folder Location: `Templates`
- Trigger Templater on new file creation: `开启`

### 4. Tag Wrangler（可选）

Obsidian → 设置 → 第三方插件 → 浏览 → 搜索 "Tag Wrangler" → 安装 → 启用

功能：在标签面板右键可批量重命名标签。

## 验证清单

安装配置完成后逐项检查：

- [ ] Zotero 桌面端运行中
- [ ] Better BibTeX 已安装且 citekey 格式正确
- [ ] Obsidian 中 `Ctrl+Shift+Z` 能弹出 Zotero 搜索框
- [ ] 选择论文后在 `3-Resources/论文笔记/` 成功生成笔记
- [ ] 笔记文件名为 citekey 格式
- [ ] 笔记中 zotero:// 链接可跳转回 Zotero
- [ ] Dataview 查询在预览模式下正常渲染
