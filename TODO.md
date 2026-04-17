# Ohmybrain Hub — 待办事项

> 此文件记录 Hub 尚未完成或需要观察后决策的事项。与 `wiki/log.md`（已完成历史）互补。

## 待观察 / 待提交

### 🟡 试用期未 commit：3 处 Claude Code 配置优化（2026-04-15 发起 / 2026-04-17 复盘）

依据 [[yizhiyanhua-ai-fireworks-tech-graph]] + [[affaan-m-everything-claude-code]] 两仓启发点实施，**已落地但未 commit**，等经验验证再合入。

**2026-04-17 现状核查**：3 项配置都仍在位。观察周期仅 2 天，以下为本次核查证据。

- [x] ✅ **`~/.claude/skills/llm-wiki/SKILL.md` 触发关键词**（生效证据明确）
  - 动作：frontmatter `description` 加 15 中 + 7 英文触发短语 + `paths: wiki/**`
  - **2026-04-17 证据**：本次会话写入 `wiki/comparisons/e2e-test-matrix.md` 时，llm-wiki skill 自动激活（system-reminder 出现）。`paths: wiki/**` 路径触发+触发短语均有效。
  - **无需 commit**（全局 skill 不在 git）。保留配置。

- [ ] 🔶 **Hub `.claude/settings.json` 加 `env.CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50`**（证据不足）
  - 动作：auto-compact 阈值 95% → 50%
  - **2026-04-17 现状**：env 仍在位。2 天内未出现明显长会话到达此阈值的场景，无法判断是否"更稳"或"过于激进"。
  - **建议**：继续观察 1 次长会话（例如一次完整的多模块 /ingest 或大规模测试）再决策。

- [ ] 🔶 **`.claude/agents/wiki-ingester.md` 加 `memory: user`**（证据不足）
  - 动作：agent 开启用户级跨会话记忆
  - **2026-04-17 现状**：`memory: user` 仍在 frontmatter。2 天内 wiki 有活跃写入（P3.1/3.2/3.3 进度）但未见显式 `/ingest` agent 调用记录。
  - **建议**：下次真正触发 `/ingest` 时特别观察 agent 是否引用过往摄入经验；达到 2-3 次再决策。

**何时 commit**：
- #1 已确认生效（但全局 skill 不入 git，无需 commit）
- #2 #3 继续观察；下次长会话/ingest 后再复盘
- 如果 #2/#3 发现副作用 → 删除配置并在 `wiki/log.md` 记录

### 其他

<!-- 后续新增待办在这里追加 -->

---

## 已关闭 / 归档

<!-- 已决策但有价值保留的条目移到这里 -->
