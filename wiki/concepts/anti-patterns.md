---
type: concept
created: 2026-05-24
updated: 2026-05-24
tags: [反模式, 经验, 教训, anti-pattern]
---

# 跨项目反模式合集

提炼自 `~/.claude/projects/D--Claude/memory/feedback_*.md` 60+ 条 + 各项目 wiki/debug-logs/ + 项目复盘。本页是 single source of truth，memory 是触发源。

## 按阶段分类

### Research 阶段反模式

| 反模式 | 表现 | 解药 / 触发源 |
|--------|------|---------------|
| **confirmation bias** | 问 Claude 找证据支持已相信的，Claude 顺着走 | 反向 pressure-test，找 disconfirming evidence |
| **跳过 query 重造轮子** | 不查 Hub wiki / memory 直接动手 | 硬约束 `先查后做`（[[../architecture/dual-loop]] § knowledge.query） |
| **3 层渐进披露不用** | 一次 Read 5+ 页 wiki，token 浪费 | `index → log → 详` ≤3 页（[[../source-summaries/thedotmack-claude-mem]] 启发） |

### Build 阶段反模式

| 反模式 | 表现 | 解药 / 触发源 |
|--------|------|---------------|
| **代下"完成 / work"结论** | Claude 跑完 test 就说"work 了"，未经用户判定 | `feedback_uwacomm_testing_boundary`：每 checkpoint 停 + 不代下结论 |
| **agentic 技术债 / worktree 漂移** | 多 worktree 独立演化未集成，堆积分歧 | 周期性集成（2026-05-12 一次吸收 codex 175 文件）+ [[worktree 三路隔离]] |
| **零摩擦 scope creep** | spec 写完后实施时悄悄加新需求 | `specs/active` 单职责硬约束 + 新 scope 必新 spec |
| **跳过 specs 直接 code** | 不写 spec 直接动手 → 没有 trace 的代码 | `feedback_ohmybrain_workflow`：硬工序 `specs → plans → discussion → code` |
| **硬编码路径** | 用 `D:\TechReq\UWAcomm` 而非 `D:\Claude\TechReq\UWAcomm` | `feedback_uwacomm_path` |

### RCA 阶段反模式

> **RCA 定位**：Root Cause Analysis 是 `engineering.validate` 失败时的子环节（不在 4 步闭环之内），找单一根因 → fix → 重新 validate。详见 [[workflow-glossary#RCA]]。

| 反模式 | 表现 | 解药 / 触发源 |
|--------|------|---------------|
| **plan C 时变证伪 / 多根因混淆** | 把"信道时变"作为假根因，绕过单一函数 fix | `feedback_single_root_cause_audit`：D9/D10 toggle + 跨 runner audit |
| **多 fix 并行** | 同时改 X + Y，无法判断哪个有效 | 单一 fix 一次，跨 runner audit 验证 |

### Promote 阶段反模式

| 反模式 | 表现 | 解药 / 触发源 |
|--------|------|---------------|
| **过度 promote** | 把项目级 commit hash / BER 数字硬塞 Hub | promote 前自审"换到其他项目是否仍有效" |
| **忘 promote** | 跨项目可复用结论留在 memory 没回流 | 定期 `knowledge.review` 挑出 reference / feedback 类型 |
| **私密泄露** | DocProcess 私人项目方法论进了公开 Hub | `<private>` 标签 + `check_private_tags.py` hook |
| **Hub 索引漂移** | wiki 写但 index/log 未同步 | Stop hook `check_index_log_sync.py` 强制 |

### 全阶段反模式

| 反模式 | 表现 | 解药 / 触发源 |
|--------|------|---------------|
| **git commit / push 未授权** | Claude 自作主张 commit 或 push | `feedback_git_confirmation`：破坏性操作必明授权 |
| **凭据反复使用** | PAT 暴露后还继续用 | `feedback_pat_after_exposure`：用一次即停 |
| **跳过 review** | 写完代码不审查 | `~/.claude/rules/common/code-review.md` + code-reviewer agent |

## 与 PPT V4 S35 反模式表的对应

V4 PPT `CC算法开发-v4.pptx` S35 把这里的反模式合并为 8 行 × 3 列展示（反模式 / 出现阶段 / 解药 + memory 条目）。详见 [[../../../Tools/AnthropicPPT/wiki/concepts/slide-layouts]] § Antipattern Table。

## 未来扩展

- TODO 把每个反模式的"首次触发事件"标注（哪次 session / commit）
- TODO 补 Research 阶段 confirmation bias 的具体应对话术模板

## 相关页面

- [[../architecture/dual-loop]] — 双闭环（反模式分阶段对应）
- [[../architecture/hub-as-brain]] — 大脑功能定位（本页是其中之一）
- [[../topics/memory-index]] — memory 条目索引（feedback_* 60+ 条原始源）
