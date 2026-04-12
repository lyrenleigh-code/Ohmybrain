---
type: source-summary
created: 2026-04-12
updated: 2026-04-12
tags: [搭建计划, harness-engineering, llm-wiki, 系统架构]
source_type: note
---

# my-brain 系统搭建计划

- **来源**：raw/notes/my-brain-setup-plan.md
- **日期**：2026-04-12
- **类型**：笔记
- **原始文件**：raw/notes/my-brain-setup-plan.md

## 核心观点

1. **目标**：搭建一套 harness + LLM wiki 一体化的个人知识与工程管理系统，以 Claude Code 作为执行引擎，在仓库内按阶段逐步完成。
2. **三阶段搭建方案**：
   - **第一阶段（搭骨架）**：建立仓库目录结构（raw/ + wiki/ + workflows/ + scripts/），创建 CLAUDE.md 操作手册、index.md、log.md，定义 ingest / query / promote 三大工作流，完成第一份资料的 ingest 验证。
   - **第二阶段（加约束）**：通过 Claude Code hooks（PreToolUse / PostToolUse / Stop）和 lint 脚本强制执行核心规则——禁止修改 raw/、每次变更必须同步 index 和 log、wiki 页面不得成为孤儿页。同时创建 slash commands（/ingest-source、/lint-wiki、/promote-answer）实现端到端自动化。
   - **第三阶段（让它生长）**：加入 GitHub Actions 自动化 lint 检查，建立月度 review 习惯，形成持续运转的知识闭环。
3. **核心设计原则**：raw/ 只读不可修改；所有变更必须记入 log；优先读 wiki 回答问题；高价值回答必须 promote 回 wiki。
4. **harness engineering 思想贯穿全文**：通过 hooks 和 lint 脚本将规则编码为自动化约束，让 agent 无法跳过关键步骤，而非依赖提示词提醒。

## 相关概念

- [[harness-engineering]] — 本文档的核心方法论，通过自动化约束（hooks、lint、CI）驯服 LLM agent
- [[llm-wiki]] — 本文档要搭建的知识沉淀层，LLM 维护的结构化 wiki 系统
- [[underwater-acoustic-communication]] — 研究主方向，wiki 系统服务的核心知识领域

## 相关实体

- [[claude-code]] — 整个系统的执行引擎
- [[obsidian]] — wiki/ 的可视化和浏览层
- [[github]] — 多设备同步与自动化检查

## 引用摘录

> 目标：搭建一套 harness + LLM wiki 一体化的个人知识与工程管理系统。执行方式：在 Claude Code 中按阶段逐步完成。

> raw/ 目录只读：任何情况下不得修改或删除 raw/ 下的文件。更新 wiki 必须同步更新 index。所有变更必须记入 log。优先读 wiki。高价值回答要 promote。
