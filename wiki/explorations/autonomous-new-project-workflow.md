---
type: exploration
created: 2026-04-21
updated: 2026-04-21
tags: [agent-harness, 闭环, 自动化, GAN-harness, verification-loop, 新建项目, 无人值守]
---

# 自主新建项目工作流方法论

> **背景**：2026-04-21 对话中从"非工作时段让 agent 无人值守地推进项目，早上看结果"这一诉求出发，针对 UWAnet 重建场景设计了一套"从一行目标到 M1 落地"的自主闭环。本页沉淀跨项目可复用的方法论。

## 动机

- 新建项目前期 SOP（派生模板 → ingest → PRD → 脚手架 → 注册）**高度重复**，跨项目机械相同
- 想利用非工作时段让 agent 跑完，早上只看报告
- 但"agent 跑一夜 = 烧钱 + 一片废墟"是真实坑，**必须有收敛机制和升级路径**

## 核心概念

### 开环 vs 闭环

- **开环**：人指令 → agent 做 → 人审 → 人再指令（离不开人）
- **闭环**：agent 做 → 自评 → 不合格则改 → 合格即停（不需要人）

缺了**自评**或**收敛条件**的"闭环"就是死循环/乱跑。

### 三种闭环模式

| 模式 | 判据 | 适用 |
|------|------|------|
| **Verification Loop** | 二进制机器判：build 过？测试绿？lint 通过？ | 工程类兜底门 |
| **Santa Loop** | 两 agent 互审 → Reviewer 连续 N 轮无意见 | 质量 / 文档严谨度 |
| **GAN Harness** | Generator 做 + Evaluator 按 rubric 打分 → 分数收敛 | 目标导向任务 |

**三者可叠加**：Santa/GAN 管"好不好"，Verification 管"对不对"。

## 新建项目闭环 DAG

```
Phase 0 人工准备（写 goal.yaml，5 分钟，一次性）
   ↓
Phase 1 脚手架 ─── Verification（目录完整 + lint-wiki --quick）
   ↓
Phase 2 ingest seed ─── check_index_log_sync
   ↓
Phase 3 Planner ⇄ Evaluator（GAN 迭代，≤3 轮收敛）
   ↓
Phase 4 Generator ⇄ Evaluator + Verification（代码闭环）
   ↓
Phase 5 Hub 注册（ projects/ + CLAUDE.md 映射 + log.md ）
   ↓
Phase 6 收尾（run-report + PushNotification）
```

任一阶段失败/超迭代/卡住 → `PushNotification` + `.checkpoint/` 快照 + 等人工。

## Agent / 模型混搭策略（降本）

| 阶段 | 模型 | 理由 |
|------|------|------|
| scaffold / registrar | **Haiku 4.5** | 简单逻辑，便宜 |
| ingest | **Sonnet 4.6** | 摘要任务稳，性价比高 |
| planner | **Opus 4.7** | 架构决策需深推理 |
| generator / evaluator | **Sonnet 4.6** | 代码生成 Sonnet 已够 |

全 Opus 会翻倍（$10-25/次），混搭约 **$5/次**。

## Rubric 设计原则

- **机器可判**（grep / wc / exit code 能验证）
- **权重加起来 = 100**
- **每项 pass_threshold 独立**
- **Evaluator 不信 Planner 自评**，独立 grep 重打分
- 关键条款在 rubric 里**显式列出必存章节名**（用于 `grep -c`）

## 预算设计：四层约束

| 层 | 作用 |
|---|------|
| Token 上限（技术） | 防 context 爆炸 |
| USD 上限（经济，更直观） | 防账单失控，推荐 $5/次 |
| **迭代上限**（防死循环） | **最关键** —— token 设再大，死循环一样烧光 |
| 收敛 delta（stale 检测） | 连续 N 轮无进展 → 升级 |

**经验值**：200k token 偏紧，推荐 **300k + 混搭模型** + `max_iterations_per_phase: 3`。

## 红线 + 升级机制

### 三类红线

- `never_touch`：绝对路径（现有项目主目录、Hub raw/）
- `never_execute`：命令（`git push`, `rm -rf`, `sudo`, `git reset --hard`）
- `confirm_before`：共享状态动作（commit 到 main、写 Hub 导航、改 Hub CLAUDE.md）

### 升级策略

- `stop_on_uncertainty`: rubric 歧义 → `AskUserQuestion`；seed 不全 → halt
- `checkpoint_path`: 保存失败现场供人工续跑
- `PushNotification`: 告知人工 + 带上失败阶段 + 建议操作

## 调试期 vs 闭环期共存

核心冲突：**调试期代码在变、成功标准还没定死；闭环需要稳定标准**。

对在调项目（如 UWAnet SC-FDE）的分层策略：

1. **已完成模块** → 可挂闭环（6-scheme benchmark 夜跑等）
2. **正在调的模块** → 半自动：agent 收集失败 + 日志 + 诊断，早上人审
3. **基础设施层**（日志、checkpoint、告警 hook）→ 任何时候都该有
4. **独立 worktree 隔离** → 不动主分支，失败可撤

判据：**"能一句话说清什么叫跑对了吗？" 说不清，别上闭环。**

## 对 UWAnet 的具体应用

本次沉淀的可用资产：

| 资产 | 路径 |
|------|------|
| 权威驱动 | `Ohmybrain/projects/uwanet/prompts/goal.yaml` |
| Planner prompt | `Ohmybrain/projects/uwanet/prompts/planner.md` |
| Evaluator prompt | `Ohmybrain/projects/uwanet/prompts/evaluator.md` |
| 套件说明 | `Ohmybrain/projects/uwanet/prompts/README.md` |
| PDF 提取工具 | `Ohmybrain/scripts/extract_pdf.py` |

预处理已完成（见 `TechReq/UWAnet/wiki/log.md` 2026-04-21）：
- 17 份 raw 资料 ingest → 5 份 source-summary
- goal.yaml `pre_ingested_summaries` 字段让新 worktree 可跳过 Phase 2

## Pitfalls（本轮讨论踩过的坑）

1. **Token 预算偏紧** — 200k 只够 1 次过零迭代，推荐 300k 起
2. **Rubric 模糊** — Evaluator 漂移，必须提前量化（grep/wc 可验）
3. **不在 worktree 跑** — 污染主工作区，隔离必须
4. **PDF 读不动** — 本机没 `pdftoppm`，Read 工具直接失败；补 PyMuPDF 自建工具
5. **Evaluator 过早 PASS** — 迭代 < 3 次不得提前过，首轮也要跑满 grep
6. **不记 Changelog** — 多轮迭代失去追溯，每文档末尾追加 `## Changelog v<N>`

## 跨项目可复用清单

| 资产 | 跨项目适用？ | 备注 |
|------|------------|------|
| `extract_pdf.py` | ✓ | PyMuPDF 通用，任何项目 ingest PDF 可用 |
| `goal.yaml` schema | ✓ | 只需改 project / seed / rubric 三段 |
| Planner prompt 框架 | ✓ | 输入/产出/自检/迭代接口模板化 |
| Evaluator rubric 验证法 | ✓ | grep + wc 验证模式通用 |
| 分层自动化（调试+闭环并存） | ✓ | 任何在调项目都适用 |

## 实测数据（2026-04-21 完整 dry-run，UWAnet 为例）

从 Phase 1 到 Phase 5 走完整一遍。以下是逐阶段实测数据，覆盖本页 §预算设计 / §Pitfalls 的预判准确度。

### 阶段实测

| 阶段 | 模型 | 时间 | Token | 结果 |
|---|---|---|---|---|
| P1 scaffold | 人工 dry-run | 2 min | ~5k | 5/5 机器硬门过 |
| P2 ingest | reuse 模式 | <1 min | <1k | 7 页 wiki（复用 UWAnet 已有摘要）|
| P3 Planner v1 | Opus 4.7 | 6.75 min | 97k | 自评 93 |
| P3 Eval v1 | Sonnet 4.6 | 5.7 min | 78k | 独立 83（-10 虚报）|
| P3 Rubric v2 升级 | Edit | 1 min | ~3k | +4 约束 |
| P3 Planner v2 | Opus 4.7 | 10.8 min | 124k | 自评 95 |
| P3 Eval v2 | Sonnet 4.6 | 4.2 min | 88k | **独立 92 PASS，Δ+9** |
| P4 Generator | Sonnet 4.6 | 4.3 min | 76k | stub 自检 PASS |
| P4 Evaluator | Sonnet 4.6 | 3.6 min | 61k | 82 FAIL（Bash 权限问题，非产物）|
| P4 真装机（WSL） | bash（人工确认）| ~45 min | - | 2015/2015 编过（2 轮，1 次 patch）|
| P4 demo 验证 | WSL | <1 min | - | hello / Jmac / VBF / broadcastMAC 全过 |
| P5 Hub diff 准备 | 主会话 | 2 min | ~5k | 等人工确认 |
| **合计** | - | **~75 min** | **~530k** | **~$7** |

### 核心发现

1. **GAN harness 机制有效**：Planner 自评虚报从 v1 的 +10 降到 v2 的 +3，单单两轮就校准 70%。这是"闭环真的能自我收敛"的首次实测证据。
2. **Δ+9 > `convergence_delta_min: 5`**：收敛判据可用，没有假阳性。
3. **预算 300k / $5 单阶段刚好，全闭环 $7 略超 40%**：因为 Planner v2 实际不是"只修"，而是**触发 v2 rubric 的全量扫查**（eval-1 4 处明点 → v2 主动扫查 16 处同类问题一并修）。**教训**：rubric 升级后首轮 Planner 预算要加 50%。
4. **真装机才暴露 upstream 兼容问题**：Phase 3/4 的 agent 都看不出来 `-Werror=parentheses` 会让 Aqua-Sim-NG 挂掉。只有真 bash build 才能捕捉。**这界定了闭环的能力边界**——dry-run 能验证"脚本结构对"，不能验证"装得上"。

## 实测新发现的坑（补充 §Pitfalls）

### 坑位 #7：Subagent Bash 是运行时隐式拦截

- **症状**：subagent 的 `Tools` 列了 Bash，但实际执行被 deny
- **根因**：主会话 permission mode 下 subagent 无法弹权限对话框 + 命令不在 allowlist → auto-deny
- **对闭环的影响**：Verification Loop 的"真执行验证"退化为"静态 code review"。Phase 4 Evaluator 82 FAIL 正是此因（产物本身 100 分）
- **修复**：worktree 的 `.claude/settings.local.json` 显式 `permissions.allow`：

```json
{
  "permissions": {
    "allow": [
      "Bash(bash -n *)", "Bash(python -m py_compile *)",
      "Bash(python tests/**)", "Bash(grep *)", "Bash(wc *)", "Bash(ls *)"
    ]
  }
}
```

- **防御**：Generator 自检必须报告"我没真跑"而非静默成功（本次 Generator 做对了）
- **长期**：模板化到 `ohmybrain-core/template/.claude/settings.local.json.example`，一劳永逸

### 坑位 #8：Upstream 代码与新 GCC 不兼容

- **症状**：`./ns3 build` 因 `-Werror=parentheses` 在 107/2015 处失败；Aqua-Sim-NG 代码 `MacHeader(mach);` 写法触发 GCC 严格 warning
- **根因**：Aqua-Sim-NG 代码较老，GCC 9+ 的 `-Wparentheses` 更严；ns-3 默认 `-Werror` 升级 warning 为 error
- **对闭环的影响**：Phase 3 / 4 的 agent 都看不出来；仅真 build 才暴露
- **修复组合**：
  1. `sed` patch 2 处明确错误（`MacHeader(x);` → `MacHeader x;`）
  2. `CXXFLAGS="-Wno-error" ./ns3 configure --force-refresh`
- **长期**：Phase 4 rubric 目前只看"脚本写了什么"（`must_contain: apt-get...`），不看"装得上"。应加 **Phase 4b：最小装机验证**（Docker/CI 里 30 min build）才能真拦 upstream 兼容问题

### 坑位 #9：ns-3.41 API 变更（Planner 训练数据过时）

- **症状**：`./ns3 show examples` 在 ns-3.41 已废弃（只支持 `show profile/version/config/targets/all`）；target 命名 `jmac_test` 实际是 `JmacTest`（CamelCase）
- **根因**：Planner/Generator 训练数据混杂不同 ns-3 版本，没锁 ns-3.41 的确切 API
- **修复**：
  - `goal.yaml.rubric.m1_environment` 加 `version_lock: ns-3.41` 元约束
  - `install.sh` 已加 `--branch ns-3.41 --depth 1` 锁定版本
  - target 命名规则应记入 `wiki/source-summaries/ns3-documentation-index.md`
- **长期教训**：所有 upstream 依赖在 `goal.yaml` 应**版本锁定**到具体 tag，避免 Planner 假设

### 坑位 #10：Wikilink 根目录路径的歧义（2026-04-22 USBL-S1 P2 发现）

- **症状**：Generator 在 `workflows/01-simulation-framework.md` 写 `[[goal.yaml]]`，Obsidian 可解析（vault 根匹配），但 v2 rubric "fs 可解析" 判定为裸 wikilink
- **根因**：worktree 结构下 `workflows/` 是子目录，`goal.yaml` 在根；`[[goal.yaml]]` 在 fs 层相对当前文件不可达，需 `[[../goal.yaml]]`
- **对闭环的影响**：Phase 4 Evaluator 抓到 2 处，扣 documentation 7/15 → 总分 91（边缘过）；人工 Edit 后升到 100
- **修复**：`Edit` 2 处替换 `[[goal.yaml]]` → `[[../goal.yaml]]`，成本 <1k token
- **长期**：v2.1 rubric 加"相对路径必须从当前文件可解析"的判定；Planner prompt 显式警告"wikilink 是 fs 相对路径，不是 Obsidian vault 根"

### 坑位 #11：MATLAB 脚本 `matlab_invoke` 结构限制（2026-04-22 USBL-S1 P2 发现）

- **症状**：rubric `matlab_invoke` 期望"可执行调用"，但 .m 脚本无法嵌入 bash 命令，只能在注释中记录
- **根因**：MATLAB 语言无 shebang / 无 `#!` 头；`.m` 只能靠 `% USAGE:` 注释记录调用方式
- **对闭环的影响**：Phase 4 Evaluator 扣 smoke_test 1/20；人工 Edit 加醒目 `USAGE:` 块后接受
- **修复**：顶部前 20 行加 `%   USAGE:\n%     $ matlab -batch "run('...')"` 块
- **长期**：rubric 改为 "matlab_invoke 出现在 first 20 lines of comment block"；或外包装 `tests/smoke/run_smoke.sh` 作真可执行

## 后续路径（实测后更新）

- **P0（立即可做）** → ✅ **已完成**（2026-04-21 UWAnet 首例）
- **P1（首次完整闭环后）** → ✅ **已完成**（2026-04-21 下午抽模板）
- **P2（2 个以上项目验证后）** → ✅ **已完成**（2026-04-22 USBL-S1 MATLAB 项目 dry-run，见 [[projects/usbl-s1/README]] 与 `D:/Claude/worktrees/usbl-redo/run-report.md`）
- **P2-matlab-branch（新）** → 待做：抽 `template/prompts/goal.yaml.matlab-sim.tpl` + `template/.claude/settings.local.matlab.json.example`，下次 MATLAB 项目开箱可用（基于 USBL-S1 Phase 4 实测经验）
- **P3（远期）** → 不变：独立 agent 文件 + `/new-project` command

## 相关页面

- [[harness-engineering]] — Harness 工程通用原则
- [[subagents-orchestration]] — 子代理编排，本方案的底层机制
- [[claude-hooks-architecture]] — Hooks 在闭环里作为 red line 强制器
- [[ohmybrain-agent-architecture-insights]] — Ohmybrain 整体架构启发（本页是其具体应用）
- [[system-overview]] — 三仓架构，本方案在 Hub 层沉淀为可复用资产
- [[skills-vs-commands]] — 后续 P2 做成 skill 时参考
