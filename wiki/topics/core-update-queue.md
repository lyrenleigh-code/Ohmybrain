---
type: topic
created: 2026-05-24
updated: 2026-06-09
tags: [core, queue, 下沉, 候选]
---

# core 更新候选队列

人工维护的"待下沉到 ohmybrain-core/template-* 的候选清单"。机制详见 [[../architecture/core-update-mechanism]]。

## 待下沉候选（pending）

### high priority

| ID | 候选 | 当前位置 | 目标位置 | 验证状态 | ADR |
|----|------|---------|---------|---------|------|
| Q-001 | `check_index_log_sync.py` hook | `Ohmybrain/scripts/` | `core/template-*/scripts/` | ✓ Hub 实战，需 ≥ 2 项目验证 | — |
| Q-002 | `<private>` 标签拦截 hook | `Ohmybrain/scripts/check_private_tags.py` | `core/template-document/scripts/`（必要时同步三模板） | ✓ Hub 实战，DocProcess 项目验证 | — |
| Q-004 | `~/.claude/rules/common/llm-wiki.md` 工作流约定 | `~/.claude/rules/common/` | `core/template-*/.claude/rules/wiki.md` | ✓ 全局已使用 | — |

### medium priority

| ID | 候选 | 备注 |
|----|------|------|
| Q-005 | 三层渐进披露查询约定（index → log → 详 ≤3 页）| 写入 core/template-*/.claude/skills/query.md，启发自 claude-mem |
| Q-006 | `~/.claude/rules/common/code-review.md` 通用部分 | 部分跨项目通用，需筛选 |
| Q-007 | Hook exit code strategy 文档 | 已在 Hub CLAUDE.md 阐述，可下沉到 core/template-*/CLAUDE.md |
| Q-008 | knowledge.review 步骤定义（workflows/knowledge/04-review.md）| 检查 core 当前版本是否完整 |

### low priority / 待评估

| ID | 候选 | 评估 |
|----|------|------|
| Q-009 | engineering.validate 内 RCA 子环节描述 | 项目特化（MATLAB 算法 RCA 不外推）— 暂不下沉，保留项目层 |
| Q-010 | V→V→V 工作流 | 项目特化 UWAcomm — **不下沉**，留项目 wiki |
| Q-011 | PMF 双指标 | 同上 — **不下沉** |
| Q-012 | worktree 三路隔离 约定 | 项目级实践，可下沉为 core README 推荐 setup |

## 已下沉历史（synced）

> 本段记录已成功下沉到 core 的条目。从 pending 移到这里。

| 日期 | ID | 内容 | core commit | 备注 |
|------|---|------|-------------|------|
| 2026-05-24 | Q-003 | wiki-ingester agent 契约 | `ohmybrain-core 4902412` | 3 模板都加（knowledge 闭环跨类型通用）|

## 评估标准（决策时用）

应下沉 iff 同时满足：

- [ ] **跨项目通用**（不是项目特化）
- [ ] **≥ 2 个项目验证**（或明显的通用价值）
- [ ] **不含敏感**（无 secrets / 无 private 内容）
- [ ] **稳定**（不是一次性实验）
- [ ] **value 足够**（值得维护到一个或多个 template-* 中）

## 反例（曾考虑但拒绝下沉）

| 候选 | 拒绝理由 |
|------|---------|
| UWAcomm V→V→V 工作流 | 项目特化，算法 RCA 场景 |
| DocProcess 4 步 pandoc pipeline | 私人项目，含敏感内容 |
| Hub-as-brain 8 类页 | Hub 专属，新项目不需要 |
| FlowGen vsdx 调用模板 | 工具项目特化，归 Tools/FlowGen |

## 维护节奏

- **每次 ADR 产生**：评估是否标 "downstream" → 加 Q-XXX
- **每周末**：扫一次 pending，标 priority
- **每月**：跑 `/sync-to-core` 处理 high priority 队列

## 相关页面

- [[../architecture/core-update-mechanism]] — 同步机制详细规约
- [[../architecture/hub-as-brain]] § 通道 3 | core template
- [[../architecture/decision-log]] — ADR 触发候选
- `Ohmybrain/.claude/commands/sync-to-core.md` — `/sync-to-core` 命令实现
