# Ohmybrain Hub — 待办事项

> 此文件记录 Hub 尚未完成或需要观察后决策的事项。与 `wiki/log.md`（已完成历史）互补。

## 待观察 / 待提交

### 🟡 记忆系统改造（2026-08-29 立项，2026-09-19 状态重写）

> 取代未合并分支 `memory-system-todo`（`67a238e`，只改本文件）。该分支记录的「第 2 步合流」已被 08-30 撤回决定推翻，原文作废。

**已完成**

- ✅ 止血：`~/.claude/settings.json` `cleanupPeriodDays: 3650`（08-29）；官方文档确认 memory 文件本就不受清理影响
- ✅ 版本控制：`~/.claude/projects/` git 仓只放行 `*/memory/*.md`；09-19 快照 `5f84ed0` → 索引瘦身 `3b0d645` → 补登 `2dc2d07`
- ✅ 读取留痕 I4：`log_wiki_read.py` + `wiki_usage.py`（08-30）；退役冷层 I1：`retire_memory.py`（08-30）
- ✅ 索引瘦身（09-19）：MEMORY.md 26.5KB 超官方 25KB 读取上限（末尾 3 条会话启动时读不到）→ 分组 + 改写 → 21.4KB / 126 条
- ✅ 漏记 feedback 补登（09-19）：扫 101 个会话记录，9 主题 45 条全收；4 处冲突用户改裁（字号看得清 / 保留版本号归档后整理 / 首版从简 / 测试按用户要求）
- ✅ 零散库：AcousticLiteracy 3 条收入主库；`C--Users-zazn`、`D--TechReq-UWAcomm` 按 08-30 决定留作冷层

**待办**

- [ ] **A. 用户执行**：`~/.claude/settings.json` 加 `"autoMemoryDirectory": "~/.claude/projects/D--Claude/memory"`，让所有项目和 worktree 会话共用主库（Claude 自改 settings 被权限 classifier 拦截）；加后在任一子项目新开会话验证
- [ ] **B. 索引容量**：21.4KB / 25KB，余约 3.6KB（约 15 条）。启用 A 后各项目会话都写主库，增长会加快 → 下一步把已完结的 project 状态条目用 `retire_memory.py` 退役（候选：UWAcomm_usbl 05 月 session 簇、已退役项目）
- [ ] **C. 反复违反的机械规则固化进工具**：「文本框/线上标注无填充」「方案文档图切黑白线框」记入 memory 后仍复发 → 改 flowgen 模板默认值
- [ ] **D. feedback 捕获机制**：8 月 65 个会话仅新增 7 条 feedback；考虑 Stop hook 提醒「本会话用户纠正过什么」，或定期重跑本次的会话记录扫描（脚本思路见 09-19 log）
- [ ] **E. 规则坍缩（原第 5 步）**：09-19 已按主题合并新增部分；存量 feedback 的族内合并（覆盖用户产物族 / worktree 归属族 / flowgen 族）待做
- [ ] **F. 设计方案默认六章**同步进 `ohmybrain-core` 的 `template-document`（走 /sync-to-core）
- [x] 旧分支 `memory-system-todo` 及其 worktree 已删除（2026-09-19，用户同意）

### 其他

<!-- 后续新增待办在这里追加 -->

---

## 已关闭 / 归档

### ✅ 2026-04-15 试用期 3 处 Claude Code 配置（2026-05-12 决断闭环）

依据 [[yizhiyanhua-ai-fireworks-tech-graph]] + [[affaan-m-everything-claude-code]] 启发点实施，挂"试用期未 commit"标签 28 天后决断：

- **#1 `~/.claude/skills/llm-wiki/SKILL.md` 触发关键词** — ✅ 保留
  - 全局 skill 不入 git，无需 commit；本次 2026-04-17 + 2026-05-12 会话均验证 `paths: wiki/**` 自动激活有效
  - **结论**：永久保留，不必再观察

- **#2 Hub `.claude/settings.json` `env.CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50`** — ✅ 保留
  - 2026-04-22 6 篇 doppler 并行摄入 + 2026-04-23 双图谱扩展 + 2026-05-12 三层基础设施会话均长 context，**28 天无可见副作用**
  - **结论**：保留配置，纳入 settings.json 正常 commit（不再单独 gate）

- **#3 `.claude/agents/wiki-ingester.md` `memory: user`** — ❌ 已删（2026-04-22）+ 根因已修复（2026-05-12）
  - 2026-04-22 实测确认字段无效（项目本地 agent 不被识别）
  - 2026-05-12 L1 修复：迁全局 + commands/ingest.md 加 fallback + 主会话代写后备
  - **结论**：试用配置 #3 + L1 路径 B 修复一并闭环

### ✅ 2026-04-22 /ingest 路径 B 修复（2026-05-12 关闭）

详见 `wiki/log.md [2026-05-12] fix | /ingest 路径 B 工序修复` entry。

**遗留处理**：项目本地 `.claude/agents/wiki-ingester.md`（契约源头）与全局 `~/.claude/agents/wiki-ingester.md`（invocable handle）的同步漂移已通过 `scripts/sync_agent.py` + Stop hook `--check` 自动化（2026-05-12）。
