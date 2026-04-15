---
type: concept
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, Skill, 资源分层, 懒加载, 工程化]
---

# Skill Layered Resources — Skill 三层资源分离模式

## 定义

**Skill 三层资源分离**：一个 Claude Code Skill 不应把所有内容塞进 `SKILL.md` 单文件。应拆为三层——

1. **入口层（SKILL.md 本体）**：frontmatter + 工作流决策树 + 何时调用哪个子资源的路由指示。**主动加载**进上下文。
2. **参考层（references/*.md）**：按场景分割的细节文档（风格定义、错误清单、映射表、领域知识）。**按需懒加载**——只在决策树指示时才 Read。
3. **资产层（templates/ + scripts/ + fixtures/）**：可执行脚本、起点模板、回归测试样例。**仅工具调用时**参与。

核心理念：**SKILL.md 是路由器，不是百科全书**。大部分内容不该在用户触发时默认加载。

## 核心要点

### 为什么要分层

Skill 的 `SKILL.md` 在 skill 被触发时**全量注入上下文**，占 token。把所有协议堆在 SKILL.md：

- 每次触发都加载**全部**细节，哪怕只用到其中 10%
- SKILL.md 长到几 KB 后，模型注意力分散——决策质量下降
- 每改一条协议都会污染所有使用场景的上下文

分层后：

- SKILL.md 保持精简（理想 < 5 KB），只放决策树
- `references/style-2-dark-terminal.md` 只在画暗黑风时才加载
- 细节变更只影响被 Read 的场景，其他流程零污染

### 三层各自职责

| 层 | 何时加载 | 典型内容 | 大小目标 |
|----|---------|---------|---------|
| **入口 SKILL.md** | 触发即加载 | 触发条件、工作流步骤编号、决策树、何时 Read 哪个 references | < 5 KB |
| **参考 references/** | 按需 Read | 每种风格定义、领域知识表、错误清单、映射表 | 每个 1-5 KB |
| **资产 templates/ + scripts/ + fixtures/** | 工具调用 | SVG 起点、JSON 样例、验证/生成脚本 | 按需 |

### 参考范本（来自 [[yizhiyanhua-ai-fireworks-tech-graph]]）

```
fireworks-tech-graph/
├── SKILL.md                        21 KB 主入口（还可以更瘦）
├── references/*.md (10 个)         细节：7 种风格 + icons + matrix + layout
├── templates/*.svg (10 个)         每种图类型一个 SVG 起点模板
├── fixtures/*.json (7 个)          回归测试样例
└── scripts/ (4 个)                 validate-svg.sh / generate-from-template.py
```

### 反例：单文件 SKILL

Ohmybrain 当前 `~/.claude/skills/llm-wiki/SKILL.md` **把所有 wiki 操作协议塞在一个文件内**：frontmatter 规范、slug 命名、wikilink 格式、目录用途、工作流编号、常见错误——全部在同一文件。

后果：

- 写 concept 页时，slug 规则（主要给 paper 用）也在上下文
- 写 paper summary 时，concept 字段规范（paper 用不到）也在上下文
- 调整 frontmatter 规范要重写整个 SKILL.md，风险大

改造建议在 [[yizhiyanhua-ai-fireworks-tech-graph]] 对 Ohmybrain 的启发 §1 展开。

## 判定规则（什么时候该分层）

- **SKILL.md > 10 KB**：几乎一定该分层
- **有多种模式/风格/类别的 skill**（如 fireworks 的 7 种风格）：天然分层
- **Skill 内有按输入走不同路径的分支**：每条路径单独一个 references 文件
- **有可能积累错误清单 / 最佳实践清单**：单独一个 `common-errors.md` / `best-practices.md`，每踩一次坑加一条

## 与其他机制的关系

- **vs Agent 预加载 skill**：Agent 通过 `skills:` 字段预加载 skill 时，**仍只加载 SKILL.md 主体**，不会递归加载 references。这使分层尤其重要——否则 agent 启动成本高。
- **vs Command 的动态注入**：Command 的 `` !`bash cmd` `` 可在触发时注入上下文；references 则是**Skill 自己决策加载哪个**——两种机制互补。
- **vs 主 CLAUDE.md**：CLAUDE.md 是**仓库级**背景（永远加载），SKILL.md 是**技能级**入口（触发时加载），references 是**场景级**细节（按需加载）。三层对应三个粒度。

## 相关概念

- [[skills-vs-commands]] — Skill/Command/Agent 三机制对比（本概念是 Skill 内部的组织模式）
- [[subagents-orchestration]] — Agent 可通过 `skills:` 预加载分层 Skill 的入口层
- [[claude-hooks-architecture]] — Hook 是外部强制约束，references/common-errors.md 是内部知识沉淀，两者互补

## 来源

- 参考范本：[[yizhiyanhua-ai-fireworks-tech-graph]]（21 KB SKILL + 10 references + 10 templates + 7 fixtures + 4 scripts）
- 对照反例：Ohmybrain 当前 `~/.claude/skills/llm-wiki/SKILL.md` 单文件堆砌
- 原始资料：`raw/repos/yizhiyanhua-ai-fireworks-tech-graph/SKILL.md`、`raw/repos/yizhiyanhua-ai-fireworks-tech-graph/references/`
- 相关实体：[[claude-code]]
- 相关探索：[[ohmybrain-agent-architecture-insights]] §2.1（llm-wiki 改 skill 的后续深化）
