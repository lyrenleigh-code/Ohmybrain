---
type: architecture
created: 2026-05-24
updated: 2026-05-31
tags: [roadmap, 演化, 里程碑]
---

# Ohmybrain 演化 Roadmap

里程碑 (过去) + Roadmap (未来)。粗粒度版本，详细 ADR 见 [[decision-log]]。

## 过去里程碑（最近 6 个月）

| 日期 | 里程碑 | 类型 |
|------|--------|------|
| **2026-05-29** | IconForge 项目派生 + 入会自检 B 阶段（8 dedicated 页实质填充 + decision-log ADR 连续重排） | Tools + Hub (ADR-020) |
| **2026-05-25** | DigitalTwin1plusN 项目派生（首例采用 template-document） | DocProcess (ADR-019) |
| **2026-05-24** | Hub 大脑哲学澄清 + 8 dedicated 页框架 | 架构 (ADR-018) |
| **2026-05-23** | AnthropicPPT 项目派生（PPT 模板沉淀） | 工具 (ADR-017) |
| **2026-05-16** | rx_stream_p4 接口移植 + 双回归 RCA | UWAcomm (ADR-016) |
| **2026-05-13** | DigitalTwinGuide 项目初始化 | DocProcess (ADR-015) |
| **2026-05-12** | claude+codex worktree 175 文件吸收 + memory→Hub log 工具链 | UWAcomm + Hub (ADR-014) |
| **2026-05-09** | PaperReview 项目派生 | DocProcess (ADR-013) |
| **2026-05-08** | CooperativeDetection 项目派生 | DocProcess (ADR-012) |
| **2026-05-06** | OTFS 4-27 漏登补登 + Phase 4 BER FAIL 归档 | UWAcomm (ADR-011) |
| **2026-05-04** | simple UI v2.0 + jakes V2.0 + SC-FDE V4.1 (117× 改善) | UWAcomm (ADR-010) |
| **2026-05-01** | P4 UI 稳定性 + V3.0 解耦 | UWAcomm (ADR-009) |
| **2026-04-28** | UWAprojDoc 项目派生 + P4 UI ↔ codex 对齐 | DocProcess + UWAcomm (ADR-008) |
| **2026-04-26** | SC-FDE Phase 4+5 协议层突破 (14× 改善) | UWAcomm (ADR-007) |
| **2026-04-25** | UWAcomm_usbl 项目派生 + V5.5/V5.6 HFM calibration | UWAcomm (ADR-006) |
| **2026-04-23** | FlowGen 项目派生 + 单根因审计法形成 | Tools + UWAcomm (ADR-005) |
| **2026-04-21** | autonomous-new-project-workflow 落地 | Hub (ADR-004) |
| **2026-04-17** | 架构页重写 (三仓架构定型) | Hub (ADR-003) |
| **2026-04-14** | wiki-ingester agent 引入 | Hub (ADR-002) |
| **2026-04-12** | Ohmybrain 体系初版（单仓原型） | Hub (ADR-001) |

## 未来 Roadmap

### P0 - 立即（下 2 周）

**Hub 8 dedicated 页详细填充** ✅ 已于 2026-05-29 自检批次全部实质填充完成（2026-05-24 建骨架 → 2026-05-29 实填 → 2026-05-31 自检校正残留 stale）：
- [x] [[../concepts/workflow-glossary]] 补齐所有术语
- [x] [[../concepts/anti-patterns]] 把每个反模式标"首次触发事件"
- [x] [[../topics/harness-resources]] 完整 skill 分类（本地 31 / 注入 90+）
- [x] [[../topics/memory-index]] 加 cross-cutting topic 索引
- [x] [[decision-log]] 补齐历史 ADR（ADR-001~020 连续，追溯到 2026-04-12）
- [x] [[conventions]] 补 Worktree / 私人项目细化约定
- [x] [[../topics/ecosystem-dashboard]] 实现 `scripts/dashboard_snapshot.py` 自动同步
- [x] [[hub-as-brain]] 维护本页持续更新

> P0 全部完成。下一阶段焦点转 P1（见下）。本批 = ✅ 8 页实质填充（2026-05-29）+ 2026-05-31 入会自检发现并修正 **50 处** 2026-05-29 并行填充残留 stale（计数 / 日期 / ADR 引用 / IconForge 缺失 / 已做未勾选），详见 [[../log]] [2026-05-31] 段。

### P1 - 短期（下 1-2 月）

**UWAcomm**:
- [ ] V→V→V 继续：SC-FDE Phase 4+5 jakes fd=1Hz 50% 回归 RCA
- [ ] OTFS algo B 待 RCA
- [ ] 5 项回归 test 1+2 algo A FAIL 修复

**Hub 工具**:
- [ ] AnthropicPPT templates/layouts/ 9 layout builder 完整封装
- [ ] FlowGen 实装（流程图自动化）
- [ ] Hub `scripts/dashboard_snapshot.py` 自动状态汇总

**UWAcomm_usbl 整机原型**:
- [ ] 5 月水池 PoC
- [ ] 6 月海试

**DocProcess**:
- [ ] CooperativeDetection 4 专题 12 课题文档 + emf 矢量图
- [ ] UWAprojDoc v18 (如有新章节扩展)

### P2 - 中期（下 3-6 月）

**生态扩展**:
- [ ] UWAcomm + UWAcomm_usbl + USBL 联合仿真贯通
- [ ] 12 月国产化 100% 自有算法（脱离厦大借用）

**Hub 智能化**:
- [ ] memory ↔ Hub wiki 自动双向同步（feedback / project 自动 mirror 到 wiki/topics/）
- [ ] promote queue 自动扫描（脚本识别下游项目 wiki 中跨项目可复用条目）
- [ ] Hub wiki Graph view（基于 Obsidian 关系图）

**knowledge 闭环升级**:
- [ ] 多模型协作 ingest（不只 Claude，加 Codex / GPT-4 等并行 ingest 对比）
- [ ] wiki + memory + git history 三层合一查询

### P3 - 长期（6-12 月+）

**对外**:
- [ ] AnthropicPPT 开源（去敏后发 GitHub）
- [ ] FlowGen 开源
- [ ] 部分 wiki / 方法论开源（脱敏 Ohmybrain 框架）

**演化方向**:
- [ ] Hub 成为持续运行的 agent，主动 review + 触发 promote
- [ ] 三仓哲学下沉到 ohmybrain-core 模板（让新 user 派生时即继承本套哲学）

## 决策依据

详见 [[decision-log]]。每个 milestone 对应一条 ADR。

## 复盘节奏

- **每会话**：sub-takeaway 写入对应 memory（auto-memory 4 类）
- **每周末**：review wiki/log.md + memory，更新 ecosystem-dashboard
- **每季度**：复盘 roadmap，调整 P0/P1/P2/P3 优先级，写新 ADR
- **每年度**：架构级总结（如三仓哲学）

## 相关页面

- [[hub-as-brain]] — 大脑功能定位
- [[decision-log]] — 详细 ADR
- [[../topics/ecosystem-dashboard]] — 当前生态状态
- [[../topics/memory-index]] — memory 时序事实源
