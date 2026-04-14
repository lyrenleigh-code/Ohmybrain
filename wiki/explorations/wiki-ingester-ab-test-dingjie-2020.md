---
type: exploration
created: 2026-04-14
updated: 2026-04-14
tags: [架构验证, wiki-ingester, Agent, A/B-test, USBL]
---

# wiki-ingester Agent 新架构首次实测 — 丁杰 2020 论文 A/B

首次用新架构（`/ingest` Command 编排 + `wiki-ingester` Agent 做自治多步决策）摄入真实博士论文。测试目标是验证：

1. Agent 独立上下文能否产出达到/超过老流程的 source-summary 质量
2. 结构化输出契约是否稳定、主会话 Step 5-7 是否能机械解析
3. Prompt Caching 策略是否保住——主会话上下文不被 PDF 原文填满

## 测试条件

| 项 | 值 |
|---|---|
| 论文 | 丁杰 (2020)《复杂紧凑型超短基线定位及校准技术研究》博士论文，哈工程，133 页 |
| PDF 路径 | `D:\Claude\TechReq\USBL\raw\papers\复杂紧凑型超短基线定位及校准技术研究_丁杰.pdf` |
| slug | `dingjie-2020-compact-usbl` |
| 新产出 | `D:\Claude\Ohmybrain\wiki\source-summaries\dingjie-2020-compact-usbl.md` |
| 老产出（对照） | `D:\Claude\TechReq\USBL\wiki\source-summaries\dingjie-2020-compact-usbl.md`（USBL 项目 wiki，2026-04-13 无 agent 产出） |
| Agent 消耗 | ~350 秒 / ~124k tokens / 25 tool uses |

**测试的一个已知局限**：本会话 Claude Code agent 清单在启动时已快照，刚建的 `wiki-ingester` 未注册——改用 `general-purpose` agent 内联 spec 模拟。行为等效，但不是原生 agent 调度。次会话启动后可原生调用。

## A/B 对比

### 定量

| 指标 | 老（项目 wiki） | 新（Hub + agent） | 差异 |
|------|----------------|-------------------|------|
| 行数 | 45 | 127 | +182% |
| 核心章节数 | 5（贡献/方法/结果/关联/链接） | 9（信息/观点/贡献/方法 3 子项/数据/启发/相关概念/相关资料） | +80% |
| 商用设备参数表 | ❌ | ✅ 9 行完整（HPT 7000L / HiPAP 102 / Posidonia / GAPS / iTrack 等） | N/A |
| 数学公式保留 | ❌ | ✅ 观测方程 2-29 | N/A |
| 方法粒度 | 高层 bullet | 坐标变换/观测方程/斜距推导级 | 深 2 级 |
| 跨项目启发条数 | 3（USBL 项目内） | 8（4 项目 + 4 Hub） | +167% |
| 更新 concept 数 | 0 | 2（usbl-positioning、mimo-and-array-processing） | +2 |

### 定性

**新产出的独到之处**：

1. **"核心观点"段（5 条）+"核心贡献"表**双层结构——老版只有单一"核心贡献"。观点层是"论文在教你什么"，贡献层是"论文做了什么新东西"。
2. **"主要方法"分三个子方法，每个有 6-8 个要点**——坐标系转换公式、观测方程矩阵形式、正定 vs 超定组合、斜距用 R 还是 Rₙ 的细节。老版是 3 个一行 bullet。
3. **"对 Ohmybrain / USBL 项目的启发"分两块**：前 4 条项目视角（可直接抄到 USBL 代码的实现指引），后 4 条 Hub 层视角（可迁移到 UWAcomm 信道估计、声纳其它变种）。老版只有项目视角。
4. **"相关资料"把同仓其它 USBL 博/硕士论文列为阅读地图**——跨资源导航，老版没有。
5. **诚实报告处理问题**：返回报告里说 "pdftoppm 没装, 改 PyMuPDF; Windows GBK 编码在 PUA 字符 `\ue5ce` 上崩溃, 改直接写 UTF-8 再读规避"——透明度高，对下次优化有帮助。

**老产出的留白**：

1. 没有商用设备表——该表的全部数据都只出现在 Hub 的 concept 页 `usbl-positioning.md`，溯源断裂（"数据来自丁杰(2020)博士论文"但未直接引链）
2. 方法描述太高层——看完后还要再读 PDF 才能动手实现
3. "与项目的关联"是纯项目视角——对未来其他项目（如 UWAnet）参考价值低

### 审美 / 风格

- 新产出贴近 Hub 已有 summary 风格（如 [[claude-code-best-practice]]、[[nousresearch-hermes-agent]]），章节命名一致
- 老产出的"相关页面"链到 `[[array-design]]`、`[[calibration]]`——这些 concept 在 USBL 项目 wiki 有、Hub 没有，体现出项目 wiki 和 Hub wiki 关注点不同（项目：实现导向；Hub：知识通用性导向）
- 新产出未发明不存在的 concept——在"相关概念"段只链 3 个 Hub 已有 concept（usbl-positioning、mimo-and-array-processing、signal-processing-fundamentals）

## 架构效果验证

| 验证点 | 结果 | 证据 |
|--------|------|------|
| Agent 独立上下文不污染主会话 | ✅ | Agent 内部 25 tool uses / 124k tokens 全在其自己的 context；主会话只看到最终的结构化报告 |
| 结构化输出契约稳定 | ✅ | Agent 严格返回了"元数据 / 新建页面 / 更新页面 / 一句话摘要 / 备注"5 段。主会话直接按此机械执行 Step 5-6 |
| 主会话 Step 5-7 机械性 | ✅ | 仅 2 次 Edit（index.md + log.md）+ 2 次 Bash（lint + sync），无需再读原 PDF |
| Hook 兜底有效 | ✅ | Agent 试 Read raw/papers 下 PDF 被 Read 放行（只读）；未尝试 Write 到 raw/（否则 PreToolUse hook 会拦） |
| 交叉引用判断力 | ✅ | Agent 正确识别出 usbl-positioning 是主 concept、mimo-and-array-processing 是次 concept；拒绝创建 `baseline-decomposition` 独立 concept 并给出理由（"与 usbl-positioning 强耦合，避免孤岛页"） |

## 代价 vs 收益

**代价**：
- Agent 消耗 ~124k tokens / 350 秒——比人工快速 ingest 重
- 需维护 `.claude/agents/wiki-ingester.md` spec，spec 漂移会影响输出质量
- 首次调用需要 session 重启（agent 注册问题）——已知一次性成本

**收益**：
- 质量层面：产出显著更细（+182%）、保留数学、保留原表、双层视角
- 主会话层面：不再被 133 页 PDF 填满——可连续摄入多篇不触发 context compaction
- 可复用：同一 spec 可处理论文 / 代码仓 / 长文章 / 视频转录

**净评价**：对**非平凡资料**（长论文、大仓库、视频）强烈推荐新架构。对简短笔记 / 小文章，重型 agent 可能划不来——Command 内联处理更快。

## 后续动作

1. **等次会话原生 agent**：下次启动 Claude Code 时 `wiki-ingester` 会被注册，原生 `Agent(subagent_type="wiki-ingester", ...)` 即可，无需内联 spec
2. **批量 ingest 剩余 8 篇 USBL 论文**——如果用户确认本次质量 OK，可自动跑一轮（串行或并行）
3. **提炼 spec 改进点**——把本次 agent 产出中的好风格（"核心观点"分条、"启发分项目/Hub 双层"）写回 `.claude/agents/wiki-ingester.md` 作为参考示例
4. **评估是否需要 `baseline-decomposition-positioning` concept**——agent 选择不建，合理；若未来其他紧凑型声纳项目（成像声纳、合成孔径）来 Hub，再提炼

## 对 [[ohmybrain-agent-architecture-insights]] 的反馈

- P1-2（`/ingest` 抽 Agent）**已验证**：架构可行、质量提升、主会话负担降低
- 发现待改进：spec 应在"输出契约"中明确"核心观点 3-5 条 + 启发分项目/Hub 两段"——agent 这次自己做对了，但不明文规定就是运气
- **新 P1-3 候选**：让 Hub index.md 的 Source Summaries 条目按"领域"再分组——目前是平铺，有 34 条后再增会变难导航

## 相关

- [[ohmybrain-agent-architecture-insights]] — 架构启发录（P1-2 对应实现）
- [[claude-code-best-practice]] — 三机制对比参考
- [[nousresearch-hermes-agent]] — 对标代理
- [[dingjie-2020-compact-usbl]] — 本次新产出
- [[usbl-positioning]] — 新产出所更新的 concept
- [[mimo-and-array-processing]] — 次级 concept 更新
