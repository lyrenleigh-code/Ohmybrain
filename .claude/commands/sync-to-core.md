---
description: Hub → ohmybrain-core 同步辅助命令。扫描 wiki/topics/core-update-queue.md 待下沉候选，比对 core/template/ 差异，生成 diff 报告 + 推荐 commit message。User 审查后授权 apply。
---

# /sync-to-core

把 Hub 决策下沉到 ohmybrain-core/template/ 的辅助命令。

## 何时调用

- 月度 `knowledge.review` 后处理 high priority 队列
- 单条 candidate 验证 ≥ 2 项目后想立即下沉
- ADR 标 "downstream" 后跟进

## 工作流

### Step 1 - 读 queue

读 `wiki/topics/core-update-queue.md`，列出 pending 段所有 candidate（含 ID / 当前位置 / 目标位置 / 验证状态）。

按 priority (high / medium / low) 输出清单。

### Step 2 - 选 candidate

询问 user 哪个 ID 要同步。默认建议从 high priority 第一个开始。

也支持："同步全部 high priority" 或 "ID Q-001 Q-002"。

### Step 3 - 比对差异

对选中的每个 candidate：

1. 读 Hub 当前内容：`<当前位置>` 路径
2. 读 core 当前内容：`D:\Claude\ohmybrain-core\<目标位置>`
   - 如果 core 中文件不存在 → 标 "新增 (CREATE)"
   - 如果存在 → 生成 diff
3. 输出 diff 摘要：
   - 行数变化
   - 关键差异点
   - 是否包含敏感内容（扫 secrets / private）

### Step 4 - 安全检查

每个 diff 必须过：
- [ ] 不含 secrets（API key / token / .env）
- [ ] 不含 `<private>` 标签
- [ ] 不含 Hub 专属内容（hub-as-brain 等术语）
- [ ] 不含项目特化内容（UWAcomm / DocProcess 等具体项目名）

任一不过 → STOP + 报告。

### Step 5 - 生成 commit message

按 conventional commits 格式：

```
feat(template): 下沉 <名称> from Hub (Q-XXX)

来源：[[Hub wiki 页]]
触发：ADR-XXX（如有）
验证：UWAcomm + USBL 实战

[skill/hook/rule/workflow/structure] 类型说明
```

### Step 6 - 等用户授权

输出完整 plan：
- diff 摘要
- 拟变更的文件
- 拟用的 commit message
- 警告（如有）

**等用户明确说 "apply" / "授权" / "go" 才执行**。

破坏性操作（`git commit` / `git push`）必须明确授权（feedback_git_confirmation）。

### Step 7 - Apply

授权后：

1. 切到 core 仓：`cd D:\Claude\ohmybrain-core`
2. Apply 改动（cp / edit）
3. `git add` specific files
4. `git commit -m <message>`
5. **不自动 push**（user 单独授权）

### Step 8 - 更新 queue

把刚同步的 candidate 从 pending 段移到 "已下沉历史" 段：

```markdown
| 2026-MM-DD | Q-XXX | <名称> | <core commit hash> |
```

更新 `wiki/topics/core-update-queue.md` + 同步 `wiki/log.md`。

## 安全约束

1. **不私自 commit**：每个 diff 必须用户审查
2. **不私自 push**：push 必须额外授权
3. **不并行同步**：一次一个 candidate（避免误合并）
4. **失败回滚**：如果 commit 后发现问题，用 `git revert` 而非 `git reset --hard`

## 与其他命令的关系

| 命令 | 角色 | 边界 |
|------|------|------|
| `/ingest` | raw/ → wiki/ | knowledge 闭环 step 01 |
| `/promote-answer` | 项目 wiki → Hub wiki | 仅下游项目有 |
| **`/sync-to-core`** | **Hub wiki → core/template/** | **仅 Hub 有，本文件** |

三者构成"知识三段流"：项目内 ingest → Hub 沉淀 (promote) → 模板下沉 (sync-to-core) → 下次派生新项目继承。

## 相关页面

- [[../../wiki/architecture/core-update-mechanism]] — 机制详细规约
- [[../../wiki/topics/core-update-queue]] — pending 候选清单
- [[../../wiki/architecture/decision-log]] — ADR 标 "downstream" 触发本命令
