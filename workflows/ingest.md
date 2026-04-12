# Ingest 工作流

每次新增一份原始资料时，按以下步骤执行。

## 步骤

### 1. 放入 raw/

将文件放入对应子目录：

- 论文 → raw/papers/
- 文章 → raw/articles/
- 会议/对话记录 → raw/notes/
- 图片/附件 → raw/assets/

### 2. 生成 source-summary 页

在 wiki/source-summaries/ 下新建一个 markdown 文件，包含：

```markdown
# [资料标题]

- **来源**：[URL 或文件路径]
- **日期**：YYYY-MM-DD
- **类型**：论文 / 文章 / 笔记 / 对话记录

## 核心观点

1. [观点一]
2. [观点二]

## 相关概念

- [概念名](../concepts/概念文件名.md)

## 引用摘录

> [重要原文片段]
```

### 3. 更新或新建相关概念页

检查 wiki/index.md，判断是否需要：

- 新建概念页（wiki/concepts/）
- 更新已有概念页（追加新信息，注明来源）

### 4. 更新 wiki/index.md

在对应分类下追加新页面条目。

### 5. 更新 wiki/log.md

在文件顶部追加：

```
- YYYY-MM-DD: ingest [资料标题]，新增/更新了 N 个概念页
```

## 示例

输入命令：
> `/ingest-source raw/notes/harness-llm-wiki-conversation.md`

预期输出：
- `wiki/source-summaries/harness-llm-wiki-conversation.md`
- `wiki/concepts/harness-engineering.md`（新建）
- `wiki/concepts/llm-wiki.md`（新建）
- `wiki/index.md` 更新
- `wiki/log.md` 更新
