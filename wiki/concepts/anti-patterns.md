---
type: concept
created: 2026-05-24
updated: 2026-05-29
tags: [反模式, 经验, 教训, anti-pattern]
---

# 跨项目反模式合集

提炼自 `~/.claude/projects/D--Claude/memory/feedback_*.md`（feedback 类 21 条 / memory 共 77 个：user 1 / feedback 21 / project 52 / reference 3）+ 各项目 wiki/debug-logs/ + 项目复盘。本页是 single source of truth，memory 是触发源。

> **「首次触发事件」列**记录该反模式第一次被踩中并沉淀为 feedback 的 session / 项目 / 日期。无法从对应 memory 确证日期或来源的，标「来源待补」，不臆测。

## 按阶段分类

### Research 阶段反模式

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **confirmation bias** | 问 Claude 找证据支持已相信的，Claude 顺着走 | 反向 pressure-test，找 disconfirming evidence（话术模板见下） | 来源待补（方法论沉淀，非单次 session） |
| **跳过 query 重造轮子** | 不查 Hub wiki / memory 直接动手 | 硬约束 `先查后做`（[[dual-loop]] § knowledge.query） | 来源待补 |
| **3 层渐进披露不用** | 一次 Read 5+ 页 wiki，token 浪费 | `index → log → 详` ≤3 页（[[thedotmack-claude-mem]] 启发） | 来源待补 |

#### confirmation bias 应对话术模板

当用户的提问预设了某个结论、希望我"帮忙找证据"时，先做反向 pressure-test，再给平衡结论。可复用的话术骨架：

- **明确两边假设**："在确认 X 之前，我先列一下支持 X 和反对 X 的证据各自有哪些，再判断哪边更站得住。"
- **主动找 disconfirming evidence**："如果 X 是错的，我们最先会在哪里看到反例？我去查一下这个反例存不存在。"
- **拒绝单边迎合**："我能找到支持 X 的材料，但那不等于 X 成立——我同时检查了反面，结论是 …"
- **量化而非定性**（呼应 [[#Build 阶段反模式|不代下结论]]）："我只陈述观察到的数字（NMSE 从 A 到 B），是否算"验证通过"由你判断。"
- **反例 > 例证的优先级**：plan C 时变证伪（见 RCA 阶段）就是"保守直觉 ≠ 审计结论"的范例——一个反例能推翻一串看似支持的例证。

### Build 阶段反模式

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **代下"完成 / work"结论** | Claude 跑完 test 就说"work 了"，未经用户判定 | `feedback_uwacomm_testing_boundary`：每 checkpoint 停 + 不代下"完美/work/闭环/成功"结论，只陈述观察事实 | 2026-04-22 UWAcomm session（用户："测试函数我自己跑，你不要代替我下结论"） |
| **单元 fix 当集成验证** | 单元层 fix 验证后直接推到 benchmark 就当集成通过 | 单元 ≠ 集成，物理意义不同，分别停 checkpoint 确认 | 2026-04-22 UWAcomm session（同 testing_boundary） |
| **跳过 specs 直接 code** | 不写 spec 直接动手 → 没有 trace 的代码 | `feedback_ohmybrain_workflow`：硬工序 `specs/active → plans → discussion → code → specs/archive` | 2026-04-13 UWAcomm session（用户："是否按照 ohmybrain 的思路去做"） |
| **零摩擦 scope creep** | spec 写完后实施时悄悄加新需求 | `specs/active` 单职责硬约束 + 新 scope 必新 spec | 来源待补（与 ohmybrain_workflow 同源工序约束） |
| **硬编码路径** | 用 `D:\TechReq\UWAcomm` 而非 `D:\Claude\TechReq\UWAcomm` | `feedback_uwacomm_path`：旧副本 2026-04-13 已删，统一用 `D:\Claude\TechReq\` 前缀 | 2026-04-13 UWAcomm（旧 `D:\TechReq\UWAcomm` 副本删除当天） |
| **MATLAB inf 字面量触发隐性错误** | 用 `[inf, …]` 数组字面量 → "double 转 struct"诡异错误 | `feedback_matlab_inf_bug`：用 `0` 代 inf，`Kval==0` 替 `isinf`；[[matlab-pitfalls]] | 2026-04-13 UWAcomm test_sync.m |
| **agentic 技术债 / worktree 漂移** | 多 worktree 独立演化未集成，堆积分歧 | 周期性集成（2026-05-12 一次吸收 codex 175 文件）；归属规则见下「协作边界」 | 2026-05-12 UWAcomm claude+codex 集成 session |

### RCA 阶段反模式

> **RCA 定位**：Root Cause Analysis 是 `engineering.validate` 失败时的子环节（不在 4 步闭环之内），找单一根因 → fix → 重新 validate。详见 [[workflow-glossary]]（§ RCA）。

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **plan C 时变证伪 / 多根因混淆** | 把"信道时变""保守回退"当假根因，绕过单一函数 fix | `feedback_single_root_cause_audit`：D9/D10 toggle + 跨 runner audit；"保守回退是直觉假设，不是审计结论" | 2026-04-24 SC-TDE V5.4 fix（plan C 把 fd=1Hz 0% 打崩到 37%，回滚 plan A） |
| **多 fix 并行** | 同时改 X + Y，无法判断哪个有效 | 一次只动一个因素，跨 runner audit 验证 | 2026-04-23~05-04 UWAcomm RCA 三 case 期 |
| **跨 runner 单 bug 未广播** | 命中根因只修当前 runner，同 pattern 其他 runner 留 bug | 命中后 grep 同 pattern 全套 runner 一次同步（2026-04-24 audit 命中 4 runner） | 2026-04-24 DSSS post-CFO 同 bug（43%→0%，4 runner 同步） |
| **盲信 caller 注释 / 不对照 codex** | P4/14_Streaming BER 异常直接钻 claude 代码盲调；信 caller 旧注释 | `feedback_uwacomm_codex_compare_method`：先 diff codex worktree；callee 头注 > caller 注释 | 2026-05-?? P4 调试（caller 注释说传 -alpha，callee V7+ 头注说传正 alpha） |
| **UI BER 异常直接改算法** | 14_Streaming UI 跑 50% BER 就改 modem_decode / 字段透传 | `feedback_uwacomm_ui_ber_diagnose_order`：先写 diag 绕开 UI 验算法（直接 encode→信道→decode），分清 UI 链路差异 vs 算法 bug | 2026-05-01 V4.0 预设按钮（UI 50% vs diag 0.68%，差 73× 全在 UI 链路） |
| **complex baseband 时间伸缩漏补载波相位** | 对 baseband complex 做 time-scaling 后不补 `exp(-j2πfc·α·t)` → body 整段相位旋转 → BER 50% | `feedback_comp_resample_carrier_phase`：baseband 必手动反载波相位；passband 已隐式包含 | 2026-05-01 P4 UI bypass=ON 路径（dop_hz=10 时 BER 50%，bypass=OFF 同条件 0%） |

### Promote 阶段反模式

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **过度 promote** | 把项目级 commit hash / BER 数字硬塞 Hub | promote 前自审"换到其他项目是否仍有效" | 来源待补（promote 协议沉淀） |
| **忘 promote** | 跨项目可复用结论留在 memory 没回流 | 定期 `knowledge.review` 挑出 reference / feedback 类型 | 来源待补 |
| **私密泄露** | DocProcess 私人项目方法论进了公开 Hub | `<private>` 标签 + `check_private_tags.py` hook | 来源待补（hook 防御性设计） |
| **Hub 索引漂移** | wiki 写但 index/log 未同步 | Stop hook `check_index_log_sync.py` 强制 | 来源待补（hook 防御性设计） |
| **sync queue 不 diff 就 apply** | candidate 标"值得 sync"就直接 cp 到 core，未确认真有差异 | `feedback_sync_to_core_lessons`：加 candidate 时同步做 baseline diff；trivial/already-sync/反向都要标，一次一个 | 2026-05-24 `/sync-to-core` 首次实战（Q-001~Q-004 四个 high priority 实际只 1 个真需 sync） |
| **不接业务前先自检漏做** | 进 Hub 直接接业务，Hub 停滞不演化 | `feedback_ohmybrain_self_improvement`：进 Ohmybrain 第一件事 = 完善自己（P0 log+memory+roadmap 自检） | 2026-05-24 Ohmybrain session（PPT 编制暴露 Hub 散乱根因） |

### 全阶段反模式

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **git commit / push 未授权** | Claude 自作主张 commit 或 push | `feedback_git_confirmation`：破坏性/公开操作必明授权，"你执行吧"不含 git 授权 | 来源待补（对 git-workflow.md 的个人化强化） |
| **凭据反复使用** | PAT 暴露后还继续用，为"诊断/善后"再调一次 | `feedback_pat_after_exposure`：用一次完成必要操作即停，善后优先"用户自己 Web 操作 / 先 revoke" | 2026-04-25 内网 GitLab 迁移（admin token 完成后再用一次诊断被拒） |
| **跳过 review** | 写完代码不审查 | `~/.claude/rules/common/code-review.md` + code-reviewer agent | 来源待补（rules 标准） |

### 协作边界反模式（worktree / 分支）

> UWAcomm 与 UWAcomm_usbl 都用 git worktree 隔离协作。下面三条是边界混淆类反模式，根因都是"在错误的 worktree 写了不归自己管的路径"。

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **擅改主项目工作树** | 直接改 `D:\Claude\TechReq\UWAcomm`（用户 source of truth），未经同意 | `feedback_uwacomm_worktree_ownership`：claude 只读写 `UWAcomm-claude`，改主项目先停下问；合入走 PR | 2026-04-25 worktree 三路隔离建立（claude / codex / 主项目） |
| **跨 worktree 写错路径** | design 窗口改了 V0.4/wiki/STATUS（归 main）；或 main 直接改 design-plan/ | `feedback_uwacomm_usbl_worktree_ownership`：进任务前 `pwd` 确认；越界路径停下回对应 worktree 改 | 2026-05-11 UWAcomm_usbl 双工作树升级（main / design/v1.x） |
| **该放权时仍逐步停 / 该守边界时擅自下结论** | 混淆"可自主迭代"与"代下结论"边界 | `feedback_uwacomm_claude_branch_autonomous`：仅 UWAcomm-claude 可代跑+决策迭代，但仍不代下"成功/闭环"结论、git 仍需授权 | 2026-05-?? UWAcomm-claude 分支放权（加速迭代，避免诊断脚本 ping-pong） |

### 文档类反模式

> 适用 UWAprojDoc / DigitalTwinGuide / CooperativeDetection / UWAcomm_usbl 等方案/方法论文档。

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **统一布局换数据** | 33 个流程图都是横向 6 步线性 + 末步前决策，dashboard 统一布局换 KPI | `feedback_doc_visual_diversification`：按业务真实结构匹配 5 模式（线性/并行/反馈环/扇出/多源汇聚），竖向优于横向，决策文案业务化（"BER 达标"非"通过?"） | 2026-04-28 UWAprojDoc（用户："不同的工作流和页面要体现出差异化"，第一版被否） |
| **matplotlib mock / 手画 SVG 配图** | 用 matplotlib 假图 / 手画 SVG / Word SmartArt 替代正式配图 | `feedback_doc_flowgen_only`：方案文档所有图必走 flowgen* 8 个 skill 之一，按决策树分流；禁手画 vsdx XML / 绕过 templates/ / 调外部 LLM API | 2026-05-03 UWAprojDoc（M4/M5/M6 三模式实战验证，立约源头） |

### agent / 工具链类反模式

| 反模式 | 表现 | 解药 / 触发源 | 首次触发事件 |
|--------|------|---------------|--------------|
| **项目本地 agent 当可调** | `D:\Claude\Ohmybrain\.claude\agents\*.md` 写齐全但 `subagent_type` 调不出（"Agent type not found"） | `feedback_project_local_agent_not_invocable`：迁 `~/.claude/agents/` 全局，或 `general-purpose` 替身 + 内联契约 + 让替身先 Read 项目本地定义 | 2026-04-22 Ohmybrain（wiki-ingester 6 次全报错） |
| **假设后台 subagent 能 Write** | 并行 ingester / writer 模式默认 subagent 能落盘，实际 Write/Bash 被 harness 拒 | `feedback_subagent_write_permission`：默认假设无法 Write，要求 agent 报告里**内联完整目标文件内容**，主会话代写 | 2026-04-22 Ohmybrain（6 并行 agent 摄入 UWA Doppler 论文，5 个 Write 被拒） |

## 与 PPT V4 S35 反模式表的对应

V4 PPT `CC算法开发-v4.pptx` S35 把这里的反模式合并为 8 行 × 3 列展示（反模式 / 出现阶段 / 解药 + memory 条目）。详见 [[../../../Tools/AnthropicPPT/wiki/concepts/slide-layouts]] § Antipattern Table。

## 未来扩展

- TODO 把标「来源待补」的反模式补齐首次触发 session / commit（confirmation bias / 跳过 query / 3 层披露 / scope creep / 过度 promote / 忘 promote / 私密泄露 / Hub 索引漂移 / git 未授权 / 跳过 review）
- TODO 各反模式补一个最小复现片段或 diff 链接（指向项目 wiki/debug-logs/）

## 相关页面

- [[dual-loop]] — 双闭环（反模式分阶段对应）
- [[hub-as-brain]] — 大脑功能定位（本页是其中之一）
- [[workflow-glossary]] — RCA / validate 等术语定义
- [[matlab-pitfalls]] — MATLAB 陷阱清单（inf 字面量等）
- [[thedotmack-claude-mem]] — 3 层渐进披露启发源
- [[memory-index]] — memory 条目索引（feedback 类 21 条 / 共 77 个原始源）
