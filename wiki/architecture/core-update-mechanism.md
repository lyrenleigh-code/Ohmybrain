---
type: architecture
created: 2026-05-24
updated: 2026-05-24
tags: [core, 同步, 下沉, mechanism]
---

# Hub → core 同步机制

「Hub = 大脑」需要主动维护 ohmybrain-core/template/，让成熟模式下沉。**当前 = 手动同步 + `/sync-to-core` 命令辅助**。

## 三仓数据流回顾

```
project → wiki 反馈 → Hub → [本机制] → 更新 core template/ → 新项目派生
```

本页是 [本机制] 部分的详细规约。

## 什么下沉到 core

✓ **应该下沉**（在 ohmybrain-core/template/ 中维护）：

| 类型 | 例 | 触发条件 |
|------|-----|---------|
| 通用 skill | `lint_wiki.py` / `promote-answer.md` / `ingest.md` | 在 ≥ 2 个项目实战验证有效 |
| 通用 hook | `check_raw_write.py` / `check_index_log_sync.py` | 同上 |
| 通用 rule | 跨项目通用的 review / coding / git 等约定 | ADR 标 "downstream" |
| workflow 改进 | engineering / knowledge 闭环步骤增减 | ADR + review 决议 |
| 目录结构 | `specs/active/` vs `archive/` 等 | 一次性架构决策 |
| CLAUDE.md 模板 | 关键约定（不可违反规则、目录地图等） | 哲学澄清后 |

## 什么不下沉

✗ **不应下沉**：

| 类型 | 例 | 原因 |
|------|-----|------|
| Hub 专属页 | `hub-as-brain.md` / `decision-log.md` / `ecosystem-dashboard.md` | 新项目不需要"大脑功能页" |
| 项目特化 | UWAcomm 的 V→V→V / SC-FDE 工作流 | 业务驱动方决定，留项目 wiki/ |
| 私人项目知识 | DocProcess/* 系全部 | `<private>` 标签拦截 |
| 一次性实验 | dry-run / 临时 patch | 不构成"模式" |
| 含 secrets | API key / token 等 | `.env.example` 模板，不含实值 |

## 触发信号

### Signal 1：实战验证 ≥ 2 项目

新 skill / hook 在 1 个项目用，可能是项目特化。在 **2 个项目** 都验证有效 → 候选下沉。

### Signal 2：ADR 标 "downstream"

`[[decision-log]]` 中的 ADR 在结尾标：
```markdown
### 下沉建议
- core/template/.claude/skills/<name>.md 添加（已在 UWAcomm / USBL 验证）
```

### Signal 3：knowledge.review 阶段决议

定期 `knowledge.review`（周/月）时，user 评估 wiki 中哪些 cross-cutting 模式可下沉。

### Signal 4：哲学澄清后

如 2026-05-24 三仓哲学澄清，可能触发 core/template/CLAUDE.md 中"Hub 大脑"描述更新。

## 候选标记方式

在 wiki 页面中标记 "candidate for core"：

### 方式 A：frontmatter

```yaml
---
type: concept
core_candidate: true
core_target: template/.claude/skills/lint_wiki.md
---
```

### 方式 B：inline 注释

```markdown
本 skill 已在 UWAcomm + USBL 实战。

<!-- candidate-for-core: template/.claude/skills/lint-wiki.md -->
```

### 方式 C：直接进 queue 页

`[[core-update-queue]]` 人工维护清单（最简洁）。

## 同步步骤

### 手动同步

```bash
# 1. 识别候选
查 wiki/topics/core-update-queue.md 或 grep "candidate-for-core" wiki/

# 2. 比对差异
diff D:/Claude/Ohmybrain/<source> D:/Claude/ohmybrain-core/<target>

# 3. 切到 core 仓
cd D:/Claude/ohmybrain-core

# 4. apply 改动
cp / edit template/<target>

# 5. commit + push
git commit -m "feat(template): 下沉 <name> from Hub (ADR-XXX)"
git push
```

### 半自动同步：`/sync-to-core` 命令

详见 `Ohmybrain/.claude/commands/sync-to-core.md`。流程：

1. Claude 读 `wiki/topics/core-update-queue.md`
2. 对每个候选条目：读 Hub wiki 详细页 + 比对 ohmybrain-core/template/
3. 生成 diff 报告 + 推荐 commit message
4. user 审查 → 授权后 apply
5. 同步完更新 queue 页（移到"已下沉历史"段）

## 安全约束

1. **私人项目内容 不进 core**：`<private>` 标签 hook 拦截
2. **包含 secrets 不进 core**：`.env` / API key 等扫描
3. **Hub 专属页 不进 core**：hub-as-brain / decision-log 等
4. **修改 core 必须 git commit**：不要本地修改不 commit（造成新派生项目用错版本）

## 与现有体系的关联

| 关联 | 说明 |
|------|------|
| [[hub-as-brain]] § 通道 3 | 本机制就是通道 3 的实现细节 |
| [[three-tier-architecture]] § 数据流向 | 本机制是"Hub → 更新 → core"那一步 |
| [[decision-log]] | ADR 触发本机制（标 "downstream"） |
| [[core-update-queue]] | 待下沉候选清单（事实源） |

## 演化记录

- **2026-05-24** 本机制首次形式化，加 `/sync-to-core` 命令 + queue 页
- 之前：纯手动同步 + 散在 user 头脑中
