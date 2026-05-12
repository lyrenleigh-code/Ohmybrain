# Ohmybrain Hub — 待办事项

> 此文件记录 Hub 尚未完成或需要观察后决策的事项。与 `wiki/log.md`（已完成历史）互补。

## 待观察 / 待提交

<!-- 当前无活跃待办（2026-05-12 全部决断 / 关闭） -->

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
