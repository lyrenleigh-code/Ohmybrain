---
type: source-summary
created: 2026-04-17
updated: 2026-04-17
tags: [Claude-Code, Skill, SVG, 架构图, 设计系统, 极简-Skill]
source_type: repo
---

# Architecture Diagram Generator — Claude Skill 极简单用途范本

## 来源信息

- **仓库/本地**：`raw/architecture-diagram-generator/`（GitHub 仓未记录 owner，skill 作者为 Cocoon AI）
- **SKILL 元数据**：`name: architecture-diagram`，v1.0，MIT（2025-12-22 最近提交）
- **维护方**：Cocoon AI（`hello@cocoon-ai.com`）
- **规模**：**极简**——整个 skill 仅 2 个核心文件（`SKILL.md` 163 行 + `assets/template.html` 319 行） + `.zip` 分发包 + 3 个 HTML 示例
- **分发形态**：Claude.ai 网页版 `.zip` 上传 / Claude Code CLI `~/.claude/skills/` 解压 / 项目本地 `./.claude/skills/`
- **定位**：**单用途 skill**——只画系统架构图（云/微服务/Web App），输出单文件自包含 HTML（内联 SVG + CSS + Google Fonts）

## 核心观点

本仓对 Ohmybrain 的启发**不在于功能强大**，而在于它是 [[yizhiyanhua-ai-fireworks-tech-graph]] 的 **"极简反例"**——展示了"Skill 不必三层分离"的场景边界。

### 1. 与 fireworks 对照：何时不必分层

| 维度 | [[yizhiyanhua-ai-fireworks-tech-graph]] | Cocoon architecture-diagram |
|------|-----|-----|
| 图类型 | 14 种（架构/ER/时序/流程/网络 等） | **1 种**（架构图） |
| 视觉风格 | 7 种（扁平图标/暗黑终端/霓虹/... ） | **1 种**（深色 slate-950） |
| 主 SKILL.md | 入口 + 决策树 | **入口 + 完整设计系统**（颜色表 + 间距规则 + SVG 片段） |
| references/ | 10 个（每风格一个 + 矩阵 + 最佳实践） | **无** |
| templates/ | 10 个 SVG（每图类型一个） | 1 个 `template.html` |
| fixtures/ | 7 个回归样例 | **无** |
| scripts/ | 4 个辅助脚本 | **无** |
| 总文件数 | 60+ | **~10** |

**结论**：当 skill 只有**一种输出形态 + 一种视觉风格**时，三层分离反而增加决策成本——全部塞进单 SKILL.md 反而更清晰，因为决策树退化为线性流程。[[skill-layered-resources]] 的分层判据应补：**"≥2 个正交维度（风格 × 类型）才值得分层"**。

### 2. 设计系统即 skill 本体

该 skill 的**核心价值是约束**，不是流程：

- **6 类语义颜色**（Frontend 青 / Backend 翠 / Database 紫 / Cloud 琥珀 / Security 玫瑰 / External 板岩）——强制可读性
- **间距规则**（组件高 60px / 垂直间隔 ≥40px / 消息总线放 gap 中心）——防重叠
- **Legend 外置**（必须在所有 boundary 之下 ≥20px）——防遮挡
- **Z-order 规则**（arrows 先画 → 不透明背景遮 → 半透明组件覆盖）——防穿透

用户输入自然语言即可，**约束保证输出不会走样**。这个思路值得迁移到其他"生成式"skill：**用明文硬约束 + 最小模板替代大段指令**。

### 3. 极简分发：.zip + SKILL.md

整个 skill 打包成 `architecture-diagram.zip`（6.5 KB），用户在 Claude.ai 设置页一键上传即可。CLI 用户 `unzip` 到 `~/.claude/skills/` 同样工作。**零依赖、零脚本**——这是 Claude Skill 的"hello world"形态，适合作为**新手参考**。

对比 Ohmybrain `llm-wiki` skill 当前依赖项目脚本（`lint_wiki.py` / `check_index_log_sync.py`）才能闭环，不可便携分发——说明"wiki 协议"本质是**项目级 skill**，不具备通用性。

### 4. Skill 作者标注

frontmatter 写明 `license: MIT` + `metadata.author: Cocoon AI (hello@cocoon-ai.com)`——这是规范的开源 skill 元数据格式，比 fireworks 只有 npm 元数据更完整。[[affaan-m-everything-claude-code]] 的 48 agents / 183 skills 生态里也普遍遵循此格式。

## 相关概念

- [[skill-layered-resources]] — 本仓作为"何时**不**三层分离"的反例
- [[subagents-orchestration]] — skill 作为 agent 原子能力的供给侧

## 相关实体

- [[claude-code]] — 本 skill 通过 `~/.claude/skills/` 加载；也支持 Claude.ai 网页上传
- [[obsidian]] — 生成 HTML 可嵌入 Obsidian 笔记作系统架构图

## 引用摘录

> "Always produce a single self-contained `.html` file with: Embedded CSS (no external stylesheets except Google Fonts) / Inline SVG (no external images) / No JavaScript required (pure CSS animations)." — SKILL.md §Output

> "CRITICAL: Place legends OUTSIDE all boundary boxes (region boundaries, cluster boundaries, security groups)." — SKILL.md §Legend Placement

> "Arrow z-order: Draw connection arrows early in the SVG (after the background grid) so they render behind component boxes." — SKILL.md §Visual Elements
