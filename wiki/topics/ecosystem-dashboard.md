---
type: topic
created: 2026-05-24
updated: 2026-05-24
tags: [dashboard, 生态, 状态, 实时]
---

# Ohmybrain 生态 Dashboard

跨仓状态快照。**非实时**（需手动同步），但比"散在各处看"快。

> 来源：本页是聚合视图。各项目仓有独立 wiki/log.md，本页 link 而不复制。

## 仓 / 项目状态总览

### TechReq / 水声通信算法仿真

| 项目 | 状态 | 当前焦点 | 路径 |
|------|------|---------|------|
| **UWAcomm** | 🟢 活跃开发 | 6 通信体制 V→V→V 持续迭代 | `D:\Claude\TechReq\UWAcomm` |
| **USBL** | 🟢 活跃开发 | 超短基线自定位 | `D:\Claude\TechReq\USBL` |
| **UWAnet** | 🟡 前期调研 | 水声组网协议 (Aqua-Sim-NG / ns-3) | `D:\Claude\TechReq\UWAnet` |
| **UWAcomm_usbl** 🔒 | 🟢 活跃 | 整机原型样机 + 总集成（2026-04-25 派生） | `D:\Claude\TechReq\UWAcomm_usbl` |

### DocProcess / 文档工作区（全私人）

| 项目 | 状态 | 当前焦点 | 路径 |
|------|------|---------|------|
| **Pricing** 🔒 | 🟢 活跃 | 军用软件四号文报价 | `D:\Claude\DocProcess\Pricing` |
| **UWAprojDoc** 🔒 | 🟢 活跃 | 水声专项方案 v17 (33.2 MB) | `D:\Claude\DocProcess\UWAprojDoc` |
| **CooperativeDetection** 🔒 | 🟢 活跃 | 4 专题 12 课题（≈ 2400 万元） | `D:\Claude\DocProcess\CooperativeDetection` |
| **PaperReview** 🔒 | 🟢 活跃 | 学位论文外审 | `D:\Claude\DocProcess\PaperReview` |
| **DigitalTwinGuide** 🔒 | 🟢 活跃 | 数字孪生实施指南方法论 | `D:\Claude\DocProcess\DigitalTwinGuide` |

### Tools / 跨项目工具

| 项目 | 状态 | 当前焦点 | 路径 |
|------|------|---------|------|
| **FlowGen** | 🟡 未实装 | 需求→Mermaid 流程图工具 | `D:\Claude\Tools\FlowGen` |
| **AnthropicPPT** | 🟢 活跃 | FIELDBOOK PPT 模板（2026-05-23 派生） | `D:\Claude\Tools\AnthropicPPT` |

### 母仓 / Hub

| 仓 | 状态 | 路径 |
|---|------|------|
| **Ohmybrain** (本仓 = Hub) | 🟢 活跃 | `D:\Claude\Ohmybrain` |
| **ohmybrain-core** (母仓) | 🟢 活跃 | `D:\Claude\ohmybrain-core` |

## Hub 内部规模快照（2026-05-25）

| 指标 | 数值 | 说明 |
|------|------|------|
| wiki 页数 | **104** | 20 concepts + 8 entities + 11 architecture + 5 topics + 4 explorations + 31 source-summaries + 25 mcp-entities |
| 自动化脚本 | **19** | `scripts/` 全量 |
| Hooks | **8** | 3 阻断 + 5 提醒/注入 |
| 全局 skill | **90+** | `~/.claude/skills/` 见 [[harness-resources]] |
| Memory 条目 | **60+** | 4 类（user / feedback / project / reference）见 [[memory-index]] |
| MCP servers | **6** | context7 / exa / github / memory / playwright / sequential-thinking |

## Hub Hooks 当前状态

| Hook | 脚本 | 类型 | 触发 |
|------|------|------|------|
| 🔴 阻断 | `check_raw_write.py` | PreToolUse Edit/Write | raw/ 写入拦截 |
| 🔴 阻断 | `check_private_tags.py` | PreToolUse Edit/Write | `<private>` 标签拦截 |
| 🔴 阻断 | `check_index_log_sync.py` | Stop | wiki 改动但 index/log 未同步 |
| 🟡 提醒 | `post_wiki_write.py` | PostToolUse | 写入 wiki 后自动 lint |
| 🟡 提醒 | `raw_ingest_reminder.py` | PostToolUse Bash | Bash 触及 raw/ 提醒 |
| 🟡 提醒 | `commit_reminder.py` | Stop | wiki 未 commit 提醒 |
| 🟡 提醒 | `check_memory_log_gap.py` | Stop | memory 与 wiki/log 缺口提醒 |
| 🟢 注入 | `session_context.py` | SessionStart | 载入会话上下文 |

详细见 [[../architecture/system-overview]] § Harness 机制。

## Promote 队列（候选回流到 Hub）

下游项目中 wiki/* 含"跨项目可复用"标注但未 promote 的条目（截至 2026-05-24）：

> TODO 用脚本扫描 `D:\Claude\TechReq\*\wiki\` 和 `D:\Claude\DocProcess\*\wiki\`（除 🔒 标识）

候选示例（人工识别）：

- UWAcomm `wiki/conclusions.md` 中"高 SNR clamp 算法适用边界"
- USBL `wiki/concepts/cage5-3d-doa.md` 中"立体阵 3D 几何"算法描述
- DocProcess/UWAprojDoc 中"4 步 pandoc pipeline"（文档自动化方法论，可去敏后 promote）

## 待办（人工维护）

- TODO 每周末扫一次本页，标记状态变化
- TODO 实现 `scripts/dashboard_snapshot.py` 自动从各项目 log.md 抽取 latest 状态
- TODO 加 "stale" 标记（30 天无更新的项目）

## 相关页面

- [[../architecture/system-overview]] — 系统架构总览（含规模表）
- [[../architecture/hub-as-brain]] — 大脑功能定位
- [[harness-resources]] — Hooks / Skills / Rules 全景
