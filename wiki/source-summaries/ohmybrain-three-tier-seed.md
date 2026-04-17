---
type: source-summary
created: 2026-04-17
updated: 2026-04-17
tags: [架构, 三仓, 模板, Hub, Ohmybrain, 设计种子]
source_type: note
---

# Ohmybrain 三仓架构设计笔记（core / project / hub）

## 来源信息

- **类型**：架构设计说明文档
- **本地路径**：`raw/notes/ohmybrain_core_hub_projects_diagram.md`（206 行）
- **定位**：**当前三仓架构的权威事实源**——该笔记准确描述了 `ohmybrain-core → project-* → ohmybrain(hub)` 的职责分工、数据流与使用顺序

## 为什么重要

Ohmybrain 已经**从单仓一体化演化为三仓架构**。早期 [[my-brain-setup-plan]] 中的"LLM Wiki + 开发工程 + Claude Code Harness 一体化仓库"愿景（后来落到 `raw/notes/agent_knowledge_repo_template.md` 的单仓模板设计）经过一次架构拆分，现已成为：

```
ohmybrain-core（母仓/模板）
  └→ 派生 → project-*（自包含子项目仓）
              └→ 索引/导航 ← ohmybrain（Hub，知识库 + 项目导航中心）
                                     ↑
                              promote 回流跨项目结论
```

这个演化的**实际落地证据**：
- 本笔记（2026-04-?）
- `D:\Claude\ohmybrain-core\` 实际存在且已被 UWAcomm / USBL / UWAnet 使用
- Hub 根 `CLAUDE.md` 第 7-18 行定义三仓关系
- `ohmybrain-core/docs/new-project-sop.md` 正是"从模板派生新项目"的操作手册

## 三仓职责（按笔记归纳）

### 1. `ohmybrain-core`（母仓 / 模板）

> 负责"默认应该长什么样"

内容：
- `template/CLAUDE.md` + `template/.claude/{rules,skills,hooks,settings.json}`
- `template/wiki/` + `template/raw/` 骨架
- `template/scripts/` 自动化脚本
- `template/workflows/{knowledge,engineering}/` 闭环流程
- `docs/new-project-sop.md` 新项目启动 SOP

职责：
```
定义模板 / 沉淀通用方法 / 维护可复用 harness
```

### 2. `project-*`（子项目仓，自包含）

> 负责"这次具体做什么、交付什么"

每个项目有自己完整的 `.claude/` + `wiki/` + `specs/` + `src/` + `scripts/`，**从 core 派生但独立演化**。

职责：
```
承载具体业务 / 维护项目知识 / 完成开发闭环 / 把经验再反哺母仓
```

### 3. `ohmybrain`（本仓 = Hub + 知识库）

> 负责"把所有项目串起来看"

内容：
- `raw/` + `wiki/`（跨项目知识沉淀）
- `projects/` 项目导航（链接到下游仓）
- **无 src/、无 specs/**——不承载业务逻辑

职责：
```
统一导航 / 总览所有项目 / 汇总跨项目经验
```

## 核心数据流

```
1. ohmybrain-core 提供模板和规则
2. 新项目 project-* 从 core 派生
3. project-* 在项目内做知识闭环 + 开发闭环
4. 成熟经验回写到 ohmybrain-core（template 演进）
5. 跨项目结论 /promote-answer 到 ohmybrain Hub
6. Hub 提供统一入口（projects/ 导航 + wiki/ 跨项目知识）
```

## 推荐使用顺序

```
第一步：先建 ohmybrain-core
第二步：每个新项目从 core 创建 project-*
第三步：项目多了以后，再补 ohmybrain-hub
```

**理由**：Hub 是总控台，不是最开始必须有的。单项目阶段项目仓自足；多项目后才需要聚合视图。

## 相关概念

（无新建；此笔记的内容直接映射到架构页重写，见下方"相关架构页"）

## 相关实体

- [[claude-code]] — 三仓共用的 harness 引擎
- [[uwacomm]] — 首个从 core 派生的项目仓

## 相关架构页

- `wiki/architecture/system-overview.md` — **本笔记是该架构页 2026-04-17 重写的事实源**（原页描述的是单仓一体化架构，已过时）

## 引用摘录

> "ohmybrain-core = 母仓，负责'默认应该长什么样'" — §你可以这样理解

> "ohmybrain-hub 更像'总控台'，不是最开始必须有的。" — §最推荐的使用顺序
