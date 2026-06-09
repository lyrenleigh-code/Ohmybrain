# UWAnet 新建项目闭环 — Prompt 套件

本目录提供"从一行目标到 M1 环境搭建落地"的 **GAN Harness + Verification Loop** 完整闭环驱动文件。

## 文件

| 文件 | 角色 | 使用阶段 |
|------|------|---------|
| [`goal.yaml`](goal.yaml) | 权威驱动（rubric / 预算 / 红线 / 种子 / 模型分配） | Phase 0 写死，全程只读 |
| [`planner.md`](planner.md) | `gan-planner` agent prompt，产出 PRD + 架构 + 里程碑 + 风险 | Phase 3 |
| [`evaluator.md`](evaluator.md) | `gan-evaluator` agent prompt，独立打分 + 反馈 | Phase 4（陪跑 Phase 3） |

## 阶段映射

```
Phase 0 人工准备（写 goal.yaml）
   ↓
Phase 1 scaffold（Haiku，从 template 派生 + git init）
   ↓
Phase 2 ingest（Sonnet，raw/seed → wiki/source-summaries）
   ↓
Phase 3 ─┬─→ planner.md（Opus）────→ specs/active + plans/*.md
         ↑                              │
         └──← evaluator.md（Sonnet）←───┘   rubric 未达 → Planner 再改
   ↓ PASS
Phase 4 gen + eval（setup.sh + smoke test）
   ↓
Phase 5 注册 + 回流到 Hub
   ↓
Phase 6 run-report + 通知
```

## 使用

### 交互式（推荐先跑）

```bash
# 1. 准备 worktree
mkdir -p D:/Claude/worktrees/uwanet-redo
cp goal.yaml D:/Claude/worktrees/uwanet-redo/
cd D:/Claude/worktrees/uwanet-redo

# 2. 在主会话发起（示意）
# "请作为 gan-planner，按本目录 planner.md 的指示完成 Phase 3"
# 完成后：
# "请作为 gan-evaluator，按 evaluator.md 评估并反馈"
```

### 调度式（成熟后）

```bash
/schedule new --cron "0 22 * * *" \
  --cmd "/gan-design goal=D:/Claude/worktrees/uwanet-redo/goal.yaml --autonomous"
```

## 先做什么（最小验证）

1. **别动现有 UWAnet**（它还在调试）
2. `EnterWorktree` 开 `uwanet-redo` 分支
3. 只跑 Phase 1 + Phase 2，看 Hub wiki 是否正确更新
4. 再加 Phase 3（Planner），此时还不涉及代码，风险小
5. 最后加 Phase 4（M1 环境搭建），ns-3 装机有外部副作用，**先在 Docker 里跑**更稳

## 为什么 UWAnet 适合当首个"新建项目闭环"试点

- SOP 已成型（[[new-project-sop]]）
- 领域资料已完整 ingest（6 份 source-summary，见 `UWAnet/wiki/log.md` 2026-04-21 条目）
- 依赖 UWAcomm 的接口清单已有
- 可与主线 UWAnet 调试完全隔离（独立 worktree）

## 关键注意

- 设计主观项（rubric 里"选型理由合理"之类）**必须提前量化**，否则 Evaluator 会漂移
- goal.yaml 的 `red_lines` 比模型参数更重要，先把这条守住
- 预算 300k / $5 是"混搭模型"假设下的估算，全 Opus 会翻倍
- 迭代上限比 token 上限更关键 —— 200k 设得再大，死循环一样烧光

## 相关

- 设计决策过程：见会话沉淀（暂未 promote 到 Hub wiki）
- 母模板：`D:/Claude/ohmybrain-core/template-engineering`
- 新项目 SOP：`D:/Claude/ohmybrain-core/docs/new-project-sop.md`
- UWAnet 当前状态：`D:/Claude/TechReq/UWAnet/wiki/dashboard.md`
