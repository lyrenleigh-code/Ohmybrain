# USBL-S1 Simulation Platform (Autonomous Workflow Dry-Run)

> **方法论 P2 验证** — 第 2 个项目跑完整 autonomous new-project workflow
>
> 本条目记录 **USBL 主项目 S1 仿真平台** 作为 autonomous workflow 第 2 次验证的 dry-run 成果。
> 不是独立项目，**USBL 主项目仍以 `projects/usbl/README.md` 为权威入口**。

- **Worktree**：`D:/Claude/worktrees/usbl-redo/`
- **首例参考**：`D:/Claude/worktrees/uwanet-redo/`（UWAnet 首例 2026-04-21）
- **验证目标**：autonomous-new-project-workflow 方法论对 MATLAB 研究仿真项目的适用性
- **主项目**：`D:/Claude/TechReq/USBL/`（本次全程 `never_touch`，未改动）
- **完成日期**：**2026-04-22**
- **判定**：**✅ Phase 0-4 全 PASS**（Phase 5 Hub 注册即本页）

## 执行成果

| 维度 | UWAnet 首例 | **USBL-S1（本次）** |
|---|---|---|
| Phase 3 v1 判定 | FAIL（需 v2） | **PASS（92/100）** |
| Phase 4 v1 判定 | FAIL（Bash 权限） | **PASS（91→100 修后）** |
| Agent 调用次数 | 5 | **4** |
| 壁钟 / Token / $ | 75 min / 530k / $7 | **55 min / 450k / $6.5** |
| 人工介入 | 2 | **1** |

**方法论新证据**：workflow 不依赖特定技术栈，C++/ns-3 → MATLAB/Monte Carlo 全流程复用。

## 产物

### Phase 3 规划（1032 行）
- `plans/roadmap.md` — 5 里程碑 M1-M5
- `plans/architecture.md` — 6 层分层 + A1-A5 接口表
- `plans/risks.md` — 12 条风险（5T+4X+3M）
- `specs/active/M0-charter.md` — 项目章程

### Phase 4 骨架代码（1324 行）
- `src/setup/init_simulation.m` — 仿真初始化
- `src/mc/run_monte_carlo.m` — parfor + for 双模式 MC 框架
- `src/scenarios/scenario_lib.m` — 6 场景（SC1-SC6 对齐 development-plan）
- `src/channel/channel_multipath.m` — 12kHz 浅海 射线追踪 + 瑞利多径
- `src/config/usbl_config.m` — 全局 cfg（端口自主仓 + 扩展 mc/channel 字段）
- `tests/smoke/test_s1_single_run.m` — matlab -batch smoke 测试
- `workflows/01-simulation-framework.md` — M1 操作手册

### 设计决策
- `loop_strategy: parfor_with_for_fallback` — license 检测 + cfg.mc.use_parallel 双保险
- `channel_model: raytrace_rayleigh_v1` — 浅海等间距抽头 + 各径独立瑞利衰落
- `scenario_ids: [SC1_NEAR_NOMINAL, SC2_MID_TYPICAL, SC3_FAR_LIMIT, SC4_SHALLOW_MULTIPATH, SC5_WIDE_ANGLE, SC6_DYNAMIC]`

## 新发现 Pitfalls（已补到 exploration）

- **#10 Wikilink 根目录路径的歧义** — `[[goal.yaml]]` Obsidian 可解析，fs 层不可达；需 `[[../goal.yaml]]`
- **#11 MATLAB 脚本 `matlab_invoke` 结构限制** — .m 无 shebang，只能注释记录调用命令

## 尚未完成

- **本机 MATLAB smoke 真跑**：worktree 代码 A1-A5 是 stub（because `never_touch: USBL 主仓`），需用户本机 MATLAB 跑一次 `matlab -batch "run('tests/smoke/test_s1_single_run.m')"` 验证骨架
- **主仓 S1 接入**：骨架代码若有采纳价值，可由主仓 S1 spec 工作流（非本 worktree）取舍合并

## 相关

- 方法论：[[Ohmybrain/wiki/explorations/autonomous-new-project-workflow]]
- 完整报告：`D:/Claude/worktrees/usbl-redo/run-report.md`
- 首例对照：`D:/Claude/worktrees/uwanet-redo/run-report.md`
- USBL 主项目导航：[[Ohmybrain/projects/usbl/README]]
