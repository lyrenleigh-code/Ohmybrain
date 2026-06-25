---
type: architecture
created: 2026-04-23
updated: 2026-04-23
tags: [架构, 记忆, memory, CLAUDE.md, auto-memory, MCP, 知识图谱]
---

# 记忆栈架构

## 定位

Claude Code 的"长期记忆"不是单一机制，而是**5 层不同粒度 / 生命周期 / 作用域**的持久层叠加。本页描述当前栈结构、决策树与维护节奏，作为未来新增/清理记忆的事实源。

搭建日期：2026-04-23（本页是记忆栈首次全面文档化，此前以 [[system-overview]] 的 Harness 机制段简略涉及）。

## 五层总览

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 5: Ohmybrain wiki（跨项目人类可读知识，永久）            │
│          D:\Claude\Ohmybrain\wiki\                           │
├─────────────────────────────────────────────────────────────┤
│ Layer 4: MCP memory server（结构化知识图谱，会话间持久）       │
│          mcp__plugin_ecc_memory__* （无对应文件路径，外部服务）│
├─────────────────────────────────────────────────────────────┤
│ Layer 3: auto-memory（Claude 自主沉淀，项目目录级）            │
│          ~/.claude/projects/<proj>/memory/*.md               │
├─────────────────────────────────────────────────────────────┤
│ Layer 2: Project CLAUDE.md（项目级固定指令，每会话加载）       │
│          <项目根>/CLAUDE.md + <项目根>/.claude/...            │
├─────────────────────────────────────────────────────────────┤
│ Layer 1: Global CLAUDE.md + rules/ + skills/（跨项目默认）     │
│          ~/.claude/CLAUDE.md + ~/.claude/rules/*/*.md         │
└─────────────────────────────────────────────────────────────┘
```

## 逐层详解

### Layer 1 — 全局默认（所有会话加载）

| 属性 | 值 |
|------|---|
| 位置 | `~/.claude/CLAUDE.md` + `~/.claude/rules/{common,zh,web}/*.md` + `~/.claude/skills/*/SKILL.md` |
| 加载 | **所有 Claude Code 会话自动加载** |
| 生命周期 | 永久，手动改 |
| 粒度 | 用户画像 / 跨项目偏好 / 工具限制 / 通用编码规则 |
| 容量预算 | 精简为主，rules/ 分领域拆分防单文件过长 |

**适合放什么：**
- 用户身份（研究领域、技术栈、语言偏好）
- 跨项目的交互偏好（简洁、并行 agent、用户主导结论）
- Claude Code 版本相关限制（subagent Write / 本地 agent 不可调）
- 通用编码/测试/安全规范

**反例（不要放）：**
- 具体项目的当前 TODO → 用 auto-memory
- 具体 bug 细节 → 用 auto-memory
- 领域知识（水声多普勒细节）→ 用 Hub wiki

### Layer 2 — 项目级指令

| 属性 | 值 |
|------|---|
| 位置 | `<proj>/CLAUDE.md` + `<proj>/.claude/{rules,skills,agents,settings.json}` |
| 加载 | **在该项目目录打开会话时自动加载** |
| 生命周期 | 永久，手动改；随项目版本化 |
| 粒度 | 项目架构、模块清单、工作流规范、hook 脚本 |

**适合放什么：**
- 项目路径、模块结构、体制清单
- 项目级工作流（specs/plans/commit 流程）
- 项目特有的 hook / skill / agent 定义
- 项目级工具偏好（如 Python 版本、测试框架）

**本仓实例：** `D:\Claude\CLAUDE.md`（D:/Claude 工作区目录，含 6 项目清单 + Obsidian vault 说明）

### Layer 3 — auto-memory（项目目录级自主记忆）

| 属性 | 值 |
|------|---|
| 位置 | `~/.claude/projects/D--Claude/memory/*.md` |
| 加载 | **在对应项目目录打开时自动注入 `MEMORY.md` 索引到上下文** |
| 生命周期 | 持续累积，需定期清理过期/重复条目 |
| 粒度 | user / feedback / project / reference 四类 |
| 写入者 | **Claude 自主判断并写入**（依照 system prompt 的 auto-memory 协议） |

**四类用途：**

| 类型 | 何时写 | 示例 |
|------|--------|------|
| `user_*` | 学到用户角色/偏好/知识时 | 用户是 UWA 算法研究者 |
| `feedback_*` | 用户纠正或确认某种做法时 | "MATLAB 测试我自己跑，不代我下结论" |
| `project_*` | 项目进行中的工作状态 | UWAcomm α 补偿改造进度、6 体制当前 BER 数据 |
| `reference_*` | 外部资源/系统指针 | OTFS pilot tradeoff 参考表 |

**关键规则：**
- MEMORY.md 是**索引**，每条 ≤150 字，内容放独立 `.md` 文件
- 所有记忆都是**时间点快照**（会注入"memory is N days old"提醒）
- 回忆前需用 git/Read 验证代码现状；冲突时信当前代码而非记忆

**本仓实例（2026-04-23 清点后）：** 16 条（详见 `MEMORY.md`），含 1 项目画像、3 活跃工作线、8 feedback 规则、1 reference、1 Hub 生态、1 UWA 论文摄入、1 Obsidian 指针。

### Layer 4 — MCP memory server（结构化知识图谱）

> [!warning] 休眠（2026-06-24 标注）
> 此层自 **2026-05-12** 起 `graph.jsonl` 停止同步、事实休眠（dormant）。当前活跃记忆以 Layer 3 auto-memory + Layer 5 Hub wiki 为主，已覆盖跨会话 + 关系网需求。下方为原设计描述，保留作参考；如需复活另起 spec。见 [[memory-graph]]。

| 属性 | 值 |
|------|---|
| 位置 | 外部 MCP 服务（`mcp__plugin_ecc_memory__*` tool 族） |
| 加载 | **不自动加载**，需显式 `read_graph` / `search_nodes` 查询 |
| 生命周期 | 跨会话持久，存储在 MCP server 后端 |
| 粒度 | entity（节点）+ relation（边）+ observations（属性） |

**适合放什么：**
- 跨维度关系清晰的对象网（scheme ↔ technique ↔ paper）
- 人物 / 项目 / 概念 间的网状关联
- 查询"A 采用什么技术？技术参考什么论文？"这类多跳问题

**与 auto-memory 的分工：**
- auto-memory = **一维叙述**，擅长"我在做什么 / 用户说过什么"
- MCP memory = **多维图谱**，擅长"A 和 B 和 C 之间怎么连"

**首次使用（2026-04-23）：** 构建"UWAcomm α 补偿技术栈"图，17 实体（1 项目 + 1 Hub + 6 体制 + 3 技术 + 6 论文）+ 23 关系。

### Layer 5 — Ohmybrain wiki（跨项目人类可读）

| 属性 | 值 |
|------|---|
| 位置 | `D:\Claude\Ohmybrain\wiki\` |
| 加载 | **不自动加载**，主会话按需 Read；`llm-wiki` skill 路径触发 |
| 生命周期 | 永久，版本化，Obsidian 可视 |
| 粒度 | concepts / entities / source-summaries / architecture / agents / workflows / topics / explorations / comparisons / mcp-entities |

**适合放什么：**
- 领域知识（水声多普勒估计方法学、USBL 定位、Claude Code 机制）
- 资料摘要（论文 / 文章 / 仓库）
- 跨项目架构与方法论
- 可与 Obsidian 双向链接浏览的长文

**与其他层的分工：**
- auto-memory 是"**我在做什么**"（短周期），wiki 是"**领域知识怎么回事**"（长周期）
- auto-memory 写给未来的 Claude 看，wiki 写给未来的用户 + Claude 一起看

## 决策树：新信息放哪里？

```
新信息产生
    │
    ├─ 是"永久的用户画像/规则/限制"？
    │      └→ Layer 1（全局 CLAUDE.md / rules/）
    │
    ├─ 是"某个项目的架构/工作流规范"？
    │      └→ Layer 2（项目 CLAUDE.md / .claude/）
    │
    ├─ 是"当前进行中工作 / 用户纠正反馈 / 具体 bug"？
    │      └→ Layer 3（auto-memory）
    │
    ├─ 是"多对象多跳关系网"？
    │      └→ Layer 4（MCP memory graph）
    │
    └─ 是"领域知识 / 资料摘要 / 跨项目结论"？
           └→ Layer 5（Ohmybrain wiki）
```

**同一信息可能跨层冗余**：如 UWAcomm α 改造进度，在 Layer 3（进度与 TODO）、Layer 4（技术关系图）、Layer 5（方法学 concept + source-summary）各有一份，从不同视角存取。

## 当前栈状态（2026-04-23）

| Layer | 位置 | 当前规模 | 最近更新 |
|-------|------|---------|---------|
| 1 全局 | `~/.claude/CLAUDE.md` | 新建 1 个 | 2026-04-23 |
| 1 规则 | `~/.claude/rules/{common,zh,web}/` | 30+ 文件 | 历史累积 |
| 1 技能 | `~/.claude/skills/{llm-wiki,...}/` | 若干 | 历史累积 |
| 2 项目 | `D:\Claude\CLAUDE.md` | 项目清单 + Hub 导航 | 2026-04-22 |
| 3 auto-memory | `~/.claude/projects/D--Claude/memory/` | 16 条（7 project + 7 feedback + 2 reference） | 2026-04-23 清点 |
| 4 MCP graph | MCP server | 17 实体 + 23 关系 | 2026-04-23 首建 |
| 5 Hub wiki | `D:\Claude\Ohmybrain\wiki\` | 58 页 + 本页 = 59 | 2026-04-22 |

## 新会话 Bootstrap 清单

context 被压缩或新开会话时，按这个顺序快速进入状态：

### 自动加载（不需要主动动作）

- **Layer 1** `~/.claude/CLAUDE.md` — 用户画像 + 偏好
- **Layer 1** `~/.claude/rules/{common,zh,web}/` — 编码 / 测试 / 安全 / Git / Agent 规则
- **Layer 2** `D:\Claude\CLAUDE.md`（如在此目录打开）— 项目清单 + Hub 导航
- **Layer 3** `MEMORY.md` 索引 —— auto-memory 86 条一行描述（`MEMORY.md` 索引 87 行，含 1 行指向全局 skill）

### 按任务类型触发读取

| 任务类型 | 先查 |
|---|---|
| **UWAcomm α 补偿** | memory `project_uwacomm_alpha_refinement` + wiki `concepts/doppler-estimation-methods` + `[[memory-graph]]` |
| **UWAcomm E2E benchmark** | memory `project_uwacomm_e2e_benchmark` |
| **UWAcomm P3 UI** | memory `project_uwacomm_p3_ui` + `D:\Claude\TechReq\UWAcomm\wiki\debug-logs\13_SourceCode\` |
| **Ohmybrain wiki 读写** | `llm-wiki` skill 自动激活（`paths: wiki/**`） |
| **MCP graph 查询** | `read_graph` / `search_nodes` 工具；对比 [[memory-graph]] 快照 |
| **Git 破坏性操作** | memory `feedback_git_confirmation` — 先确认再动作 |
| **Subagent 调用** | memory `feedback_project_local_agent_not_invocable` + `feedback_subagent_write_permission` |

### 启动自检（可选）

- 项目是否在活跃工作线？→ 查 `project_*` memory 对应条目
- 用户最近反馈过什么？→ `feedback_*` 条目扫一遍
- 有无跨项目知识已沉淀？→ 查 Hub wiki 相关 concept / source-summary

## 维护节奏

| 节奏 | 动作 |
|------|------|
| **会话内** | Claude 自主写 auto-memory；用户明确要求时 `/promote-answer` 到 wiki |
| **会话后** | 回顾是否有新 feedback 值得记；wiki 页改动需同步 `index.md` + `log.md` |
| **每周** | 清理 auto-memory 过期 `project_*` 条目（TODO 完结的）；整合重复 feedback |
| **每月** | MCP graph 大扫除：删除失效关系、合并重复实体 |
| **每季度** | 审视 Layer 1（全局 CLAUDE.md）是否漂移出"真正跨项目"边界，把项目专属内容下沉到 Layer 2 |

## 已知权衡

1. **层间冗余 vs 单点失效** — 关键信息（如"OTFS 暂停"）在 Layer 1+3 都有，避免只读一层时遗漏；接受一定维护成本
2. **auto-memory 时间漂移** — 每条都带 "N days old" 提醒，防止用历史快照下当前结论
3. **MCP graph 依赖外部服务** — 若 MCP 后端故障，图谱数据不可达；Layer 3/5 是文件，更稳健
4. **Obsidian vault 可视性** — 仅 Layer 2/5 是 `.md` 文件可在 Obsidian 浏览，Layer 3 在 `~/.claude/` 不在 vault 范围

## 相关页面

- [[system-overview]] — 三仓架构与 Harness 总览（本页是其"记忆"维度切片）
- [[claude-code]] — Claude Code 实体页
- [[claude-hooks-architecture]] — Hook 生命周期（SessionStart 注入 auto-memory 至上下文的入口）
- [[skills-vs-commands]] — Skill/Command/Agent 三机制（llm-wiki skill 属 Layer 1）
- [[subagents-orchestration]] — Subagent 编排（Layer 3 的 feedback "subagent Write 受限"来源）
- [[anthropic-2026-founders-playbook]] — Anthropic 官方 founder 方法论 v3（CLAUDE.md as architectural memory，对 L2 层的独立 validation）

## 修订记录

- 2026-04-23：首次创建。场景：用户问"如何建立长期记忆"，系统清点后识别已有 5 层；同步清理 auto-memory 3 条过期/误分类条目，建全局 CLAUDE.md，首次建 MCP 图谱，此页作第 4 步文档化收口。
