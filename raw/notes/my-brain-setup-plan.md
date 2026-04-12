# my-brain 系统搭建计划

> 目标：搭建一套 harness + LLM wiki 一体化的个人知识与工程管理系统。
> 执行方式：在 Claude Code 中按阶段逐步完成。

---

## 执行前提

- 已安装 Claude Code
- 已安装 git
- 已安装 Python 3.8+
- 有 GitHub 账号（第三阶段需要）

---

## 第一阶段：搭骨架

**目标：** 建好仓库结构，能把第一份资料 ingest 成 wiki 页。

---

### Step 1-1：建立仓库

```bash
mkdir my-brain && cd my-brain
git init
git branch -M main
```

---

### Step 1-2：建立目录结构

```bash
mkdir -p raw/papers raw/articles raw/notes raw/assets
mkdir -p wiki/concepts wiki/entities wiki/topics wiki/comparisons wiki/source-summaries
mkdir -p workflows scripts .github/workflows
```

---

### Step 1-3：创建 CLAUDE.md

路径：`CLAUDE.md`

内容如下：

```markdown
# CLAUDE.md — my-brain 操作手册

## 仓库地图

| 目录 | 用途 |
|------|------|
| raw/ | 原始资料，只读，不得修改 |
| wiki/ | 知识沉淀层，所有推理从这里读 |
| workflows/ | 操作流程文档 |
| scripts/ | 自动化脚本 |

## 核心规则

1. **raw/ 目录只读**：任何情况下不得修改或删除 raw/ 下的文件。
2. **更新 wiki 必须同步更新 index**：每次新增或修改 wiki/ 下的文件，必须同步更新 wiki/index.md。
3. **所有变更必须记入 log**：每次操作结束前，在 wiki/log.md 末尾追加一条记录，格式为 `- YYYY-MM-DD: [操作描述]`。
4. **优先读 wiki**：回答问题时优先从 wiki/ 读取，不足时才回到 raw/ 补充证据。
5. **高价值回答要 promote**：如果一次对话产生了重要结论，必须将其写回 wiki/，不能只停留在聊天记录里。

## 命名约定

- wiki 页面文件名全部小写，用连字符分隔，例如：`harness-engineering.md`
- source-summaries 用原始文件名命名，例如：`paper-attention-is-all-you-need.md`
- 概念页标题格式：`# 概念名称`
- log 条目格式：`- YYYY-MM-DD: [操作]`

## 禁止行为

- 不得直接修改 raw/ 下任何文件
- 不得在没有更新 index.md 和 log.md 的情况下结束任务
- 不得凭记忆回答可以从 wiki 验证的问题
```

---

### Step 1-4：创建 wiki/index.md

路径：`wiki/index.md`

内容如下：

```markdown
# Wiki Index

> 最后更新：YYYY-MM-DD
> 页面总数：0

## Concepts（概念页）

<!-- 每新增一个概念页，在这里加一行 -->
<!-- 格式：- [概念名](concepts/文件名.md) — 一句话描述 -->

## Entities（实体页）

<!-- 人物、工具、项目、组织 -->

## Topics（专题页）

<!-- 跨概念的综合理解 -->

## Comparisons（比较页）

<!-- A vs B 类分析 -->

## Source Summaries（资料摘要页）

<!-- 每份 raw/ 资料对应一个摘要页 -->
```

---

### Step 1-5：创建 wiki/log.md

路径：`wiki/log.md`

内容如下：

```markdown
# 变更日志

> 记录每次对 wiki 的操作，最新的在最上面。

---

<!-- 格式：- YYYY-MM-DD: [操作描述] -->
```

---

### Step 1-6：创建 ingest 工作流文档

路径：`workflows/ingest.md`

内容如下：

```markdown
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
```

---

### Step 1-7：创建 query 和 promote 工作流文档

路径：`workflows/query.md`

```markdown
# Query 工作流

回答问题时的优先级顺序：

1. **优先读 wiki/**：从 index.md 找相关页面，读取内容后回答。
2. **不足时读 raw/**：如果 wiki 中信息不够，回到 raw/ 找原始证据。
3. **回答后判断是否 promote**：如果这次回答产生了新的重要结论，走 promote 流程。

## 判断是否需要 promote 的标准

- 这个结论 wiki 里没有
- 这个结论将来很可能被反复用到
- 这个结论综合了多个来源，有独立价值
```

路径：`workflows/promote.md`

```markdown
# Promote 工作流

把高价值对话结论写回 wiki。

## 步骤

1. 识别本次对话中值得沉淀的结论
2. 找到对应的概念页（或新建）
3. 追加结论，注明来源（对话日期 + 简短描述）
4. 更新 wiki/index.md 和 wiki/log.md
```

---

### Step 1-8：第一阶段完成验证

在 Claude Code 中执行以下命令，验证第一阶段完成：

```
请把 raw/notes/ 下的对话记录文件执行 ingest 流程，
生成 source-summary 页和相关概念页，并更新 index.md 和 log.md。
```

**完成标准：**

- [ ] `wiki/source-summaries/` 下有对应摘要页
- [ ] `wiki/concepts/harness-engineering.md` 存在
- [ ] `wiki/concepts/llm-wiki.md` 存在
- [ ] `wiki/index.md` 已更新
- [ ] `wiki/log.md` 已更新

---

## 第二阶段：加约束

**目标：** 用 hooks 和 lint 脚本让 agent 无法跳过关键步骤。

---

### Step 2-1：创建 Claude Code hooks 配置

路径：`.claude/settings.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit|Create",
        "hooks": [
          {
            "type": "command",
            "command": "python3 scripts/check_raw_write.py $TOOL_INPUT_PATH"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit|Create",
        "hooks": [
          {
            "type": "command",
            "command": "python3 scripts/lint_wiki.py --quick"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 scripts/check_index_log_sync.py"
          }
        ]
      }
    ]
  }
}
```

---

### Step 2-2：创建 PreToolUse hook 脚本

路径：`scripts/check_raw_write.py`

```python
#!/usr/bin/env python3
"""
PreToolUse hook：禁止 Claude 修改 raw/ 目录下的任何文件。
"""
import sys
import os

path = sys.argv[1] if len(sys.argv) > 1 else ""

if path.startswith("raw/") or "/raw/" in path:
    print(f"[HOOK BLOCKED] 禁止修改 raw/ 目录：{path}")
    print("raw/ 是只读原始资料层，请将内容整理后写入 wiki/ 目录。")
    sys.exit(1)

sys.exit(0)
```

---

### Step 2-3：创建 lint 脚本

路径：`scripts/lint_wiki.py`

```python
#!/usr/bin/env python3
"""
Wiki lint 脚本：检查孤儿页、断链、缺失 index 条目。
用法：
  python3 scripts/lint_wiki.py          # 完整检查
  python3 scripts/lint_wiki.py --quick  # 快速检查（PostToolUse hook 用）
"""
import os
import re
import sys

WIKI_DIR = "wiki"
INDEX_PATH = "wiki/index.md"
LOG_PATH = "wiki/log.md"

def get_all_wiki_pages():
    pages = []
    for root, _, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md") and f not in ("index.md", "log.md"):
                pages.append(os.path.join(root, f))
    return pages

def get_indexed_pages():
    if not os.path.exists(INDEX_PATH):
        return set()
    with open(INDEX_PATH) as f:
        content = f.read()
    links = re.findall(r'\(([^)]+\.md)\)', content)
    return set(os.path.normpath(os.path.join(WIKI_DIR, l)) for l in links)

def check_orphans():
    all_pages = set(get_all_wiki_pages())
    indexed = get_indexed_pages()
    orphans = all_pages - indexed
    return orphans

def check_log_exists():
    return os.path.exists(LOG_PATH)

def main():
    quick = "--quick" in sys.argv
    errors = []

    orphans = check_orphans()
    if orphans:
        for o in orphans:
            errors.append(f"[孤儿页] {o} 未在 index.md 中注册")

    if not check_log_exists():
        errors.append("[缺失] wiki/log.md 不存在")

    if errors:
        print("=== Wiki Lint 发现问题 ===")
        for e in errors:
            print(f"  ✗ {e}")
        if not quick:
            sys.exit(1)
    else:
        print("✓ Wiki lint 通过")

if __name__ == "__main__":
    main()
```

---

### Step 2-4：创建 Stop hook 脚本

路径：`scripts/check_index_log_sync.py`

```python
#!/usr/bin/env python3
"""
Stop hook：检查如果 wiki/ 有变更，index.md 和 log.md 是否也被更新。
通过 git diff 判断。
"""
import subprocess
import sys

def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD"],
        capture_output=True, text=True
    )
    return result.stdout.strip().split("\n")

changed = get_changed_files()
wiki_changed = any(f.startswith("wiki/") and f not in ("wiki/index.md", "wiki/log.md")
                   for f in changed)

if wiki_changed:
    index_updated = "wiki/index.md" in changed
    log_updated = "wiki/log.md" in changed

    missing = []
    if not index_updated:
        missing.append("wiki/index.md")
    if not log_updated:
        missing.append("wiki/log.md")

    if missing:
        print(f"[HOOK BLOCKED] wiki/ 有变更，但以下文件未更新：{', '.join(missing)}")
        print("请先更新这些文件再结束任务。")
        sys.exit(1)

print("✓ index/log 同步检查通过")
sys.exit(0)
```

---

### Step 2-5：创建 slash commands

路径：`.claude/commands/ingest-source.md`

```markdown
# /ingest-source

对指定的原始资料文件执行完整的 ingest 流程。

## 参数
$ARGUMENTS — 文件路径，例如：raw/notes/my-note.md

## 执行步骤
1. 读取 $ARGUMENTS 文件内容
2. 按照 workflows/ingest.md 的步骤逐步执行
3. 生成 source-summary 页
4. 更新或新建相关概念页
5. 更新 wiki/index.md
6. 更新 wiki/log.md
7. 运行 python3 scripts/lint_wiki.py 验证
```

路径：`.claude/commands/lint-wiki.md`

```markdown
# /lint-wiki

对整个 wiki/ 目录执行完整 lint 检查。

## 执行步骤
运行：python3 scripts/lint_wiki.py
输出所有问题并逐一修复。
```

路径：`.claude/commands/promote-answer.md`

```markdown
# /promote-answer

将当前对话中的重要结论写回 wiki。

## 执行步骤
1. 识别本次对话中值得沉淀的结论（参考 workflows/promote.md）
2. 找到对应概念页或新建
3. 追加结论，注明来源
4. 更新 wiki/index.md 和 wiki/log.md
5. 运行 lint 验证
```

---

### Step 2-6：第二阶段完成验证

在 Claude Code 中测试以下场景：

1. **测试 PreToolUse hook**：尝试让 Claude 修改 `raw/` 下的文件，应被拦截。
2. **测试 Stop hook**：修改一个 wiki 页面但不更新 index，尝试结束任务，应被拦截。
3. **测试 `/ingest-source` command**：执行一次完整 ingest，全程不需要手动提醒。

**完成标准：**

- [ ] hook 能正确拦截违规操作
- [ ] `/ingest-source` 可以端到端完成全部步骤
- [ ] `lint_wiki.py` 能识别孤儿页

---

## 第三阶段：让它生长

**目标：** 加入自动化检查和 review 机制，形成持续运转的闭环。

---

### Step 3-1：创建 GitHub Actions workflow

路径：`.github/workflows/wiki-check.yml`

```yaml
name: Wiki Lint

on:
  push:
    paths:
      - 'wiki/**'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Run wiki lint
        run: python3 scripts/lint_wiki.py
```

---

### Step 3-2：建立 wiki review 习惯

在 `workflows/` 下新建 `review.md`：

```markdown
# Wiki Review 流程

建议每月执行一次。

## 检查项

- [ ] 运行 `python3 scripts/lint_wiki.py` 清理孤儿页和断链
- [ ] 检查 log.md，回顾上个月的变更
- [ ] 找出被引用最多的概念页，判断是否需要拆分或扩充
- [ ] 标记超过 3 个月未更新的结论，加 `> ⚠️ 待验证` 注释
- [ ] 检查是否有高价值对话结论尚未 promote
```

---

### Step 3-3：最终结构验证

完成后的仓库结构应如下：

```
my-brain/
├─ CLAUDE.md
├─ .claude/
│  ├─ settings.json
│  └─ commands/
│     ├─ ingest-source.md
│     ├─ lint-wiki.md
│     └─ promote-answer.md
├─ raw/
│  ├─ papers/
│  ├─ articles/
│  ├─ notes/
│  └─ assets/
├─ wiki/
│  ├─ index.md
│  ├─ log.md
│  ├─ concepts/
│  ├─ entities/
│  ├─ topics/
│  ├─ comparisons/
│  └─ source-summaries/
├─ workflows/
│  ├─ ingest.md
│  ├─ query.md
│  ├─ promote.md
│  └─ review.md
├─ scripts/
│  ├─ check_raw_write.py
│  ├─ lint_wiki.py
│  └─ check_index_log_sync.py
└─ .github/
   └─ workflows/
      └─ wiki-check.yml
```

---

## 执行建议

### 在 Claude Code 中的推荐启动方式

打开仓库目录后，直接把这份计划文档发给 Claude Code：

```
请按照 my-brain-setup-plan.md 执行第一阶段的所有步骤，
建立完整的目录结构和所有配置文件，完成后运行验证清单。
```

### 三个阶段的时间预期

| 阶段 | 预计时间 | 关键产出 |
|------|----------|----------|
| 第一阶段 | 30 分钟内 | 能跑起来 |
| 第二阶段 | 1-2 小时 | hooks 和 commands 生效 |
| 第三阶段 | 持续迭代 | 形成习惯闭环 |

---

*本文档版本：v1.0 — 2026-04-12*
