---
type: source-summary
created: 2026-04-14
updated: 2026-04-14
tags: [Claude-Code, Skill, SVG, 技术图, Skill-工程化, 可打包]
source_type: repo
---

# Fireworks Tech Graph — Claude Code Skill 工程化范本

## 来源信息

- **仓库**：`github.com/yizhiyanhua-ai/fireworks-tech-graph`
- **npm 包**：`@yizhiyanhua-ai/fireworks-tech-graph`（v1.0.4）
- **本地路径**：`raw/repos/yizhiyanhua-ai-fireworks-tech-graph`
- **许可**：MIT（2025）
- **维护方**：yizhiyanhua-ai（个人开源作者）
- **规模**：单次快照（commits = 1）、Skill 本体 ~21 KB、总资源约 60+ 文件
- **对标版本**：Claude Code Skill 规范 2026-04
- **定位**：把“用中文描述生成 SVG 技术图”做成**可分发 npm 包**的 Claude Code Skill——同时也是 **Skill 工程化的参考模板**

## 核心观点

本仓对 Ohmybrain 的价值**不在它的画图能力本身**，而在它作为 **Skill 工程化范本** 展示的 7 条可迁移模式。按重要性排序：

### 1. Skill 三层资源分离（最有启发）

主 `SKILL.md` 只保留**入口契约**和**决策树**，细节全部外置到 `references/` + `templates/` + `scripts/`——按需懒加载，不占主上下文。

```
SKILL.md (21 KB)                 入口：frontmatter + 工作流 + 决策树
├── references/*.md (10 个)      细节：每种风格一个文件，需要时才加载
│   ├── style-1-flat-icon.md
│   ├── style-2-dark-terminal.md
│   ├── ... (7 种风格)
│   ├── icons.md                 40+ 产品品牌色
│   ├── style-diagram-matrix.md  风格 × 图类型推荐表
│   └── svg-layout-best-practices.md
├── templates/*.svg (10 个)      起点：每种图类型一个 SVG 模板
│   ├── agent-architecture.svg
│   ├── architecture.svg
│   ├── er-diagram.svg
│   └── ... (10 种图类型)
├── fixtures/*.json (7 个)       回归样例：测试用输入
└── scripts/ (4 个)              辅助：validate-svg.sh / generate-from-template.py
```

**主 SKILL.md 在用户触发时全量进入上下文，但分层文件只在需要时才 `Read`。** `references/style-2-dark-terminal.md` 只在用户要“暗黑极客风”时才读，其他风格的细节不占 token。

这是对 Ohmybrain `~/.claude/skills/llm-wiki/SKILL.md` **当前把所有 wiki 操作协议挤在单文件内**的直接反例——应该拆为：
- `SKILL.md` 只放决策树（什么时候调用 /ingest、什么时候 /promote）
- `references/wiki-conventions.md` 放 frontmatter 规范、slug 命名、wikilink 格式
- `references/slug-patterns.md` 放作者-年份-关键词等具体规则
- `templates/*.md` 保留现有的 `.obsidian/templates/` 作为起点模板

（详见下文“对 Ohmybrain 的启发” §1）

### 2. Frontmatter 触发关键词（细粒度激活）

`description` 字段塞入**大量中英文触发短语**，让模型自动匹配用户意图：

```yaml
description: >-
  Use when the user wants to create any technical diagram - architecture, data
  flow, flowchart, sequence, agent/memory, or concept map - and export as
  SVG+PNG. Trigger on: "画图" "帮我画" "生成图" "做个图" "架构图" "流程图"
  "可视化一下" "出图" "generate diagram" "draw diagram" "visualize" or any
  system/flow description the user wants illustrated.
```

**对比 Ohmybrain 现有 skill**：`llm-wiki` 仅靠 `paths: wiki/**` 触发，是**文件路径匹配**——需要用户先打开 wiki 文件或提及 wiki 路径。fireworks 是**意图匹配**——用户说“画个图”就自动触发，不需要先访问任何文件。

两种触发机制互补：
- `paths:` 适合“操作特定目录”的 skill（wiki 编辑、项目代码规范）
- `description:` 加关键词适合“特定任务模式”的 skill（画图、批处理、翻译）

**Ohmybrain 可以改进**：`llm-wiki` 可以**两者叠加**——`paths: wiki/**` + `description` 加“记个笔记 / 沉淀到 wiki / 写回 Hub / /promote”等触发短语，即使用户没打开 wiki 文件也能识别意图。

### 3. Pre-Tool-Call Checklist + Error Recovery Protocol

**这是最对症 Ohmybrain 痛点的部分。** Skill 显式写了 2 套机制：

**Pre-Tool-Call Checklist**（工具调用前每次都要过）：
```text
1. Can I write out the COMPLETE command/content right now?
2. Do I have ALL required parameters ready?
3. Have I checked for syntax errors in my prepared content?

If ANY answer is NO: STOP. Do NOT call the tool. Prepare the content first.
```

**Error Recovery Protocol**（失败时严格执行）：
```text
First error:  Analyze root cause, apply targeted fix
Second error: Switch method entirely (Python list -> chunked generation)
Third error:  STOP and report to user - do NOT loop endlessly
Never:        Retry the same failing command or call tools with empty parameters
```

**对症**：Ohmybrain 的 `wiki-ingester` agent 之前遇 PDF 乱码会反复重试 PyMuPDF 提取，直到触发主会话 timeout。移植此协议可直接堵住这个坑。

**工程含义**：**把“LLM 常踩的坑”上升为显式硬规约**——不是寄希望于“下次做得更好”，而是把**已知失败模式**写成条款强制约束。这和 [[claude-hooks-architecture]] “确定性替代依从性” 的核心主张完全同构——只是 hook 是外部约束、checklist 是内部自律。

### 4. UML Coverage Map —— 语义映射减少漂移

```markdown
| UML Diagram            | Supported As          | Notes                          |
|------------------------|-----------------------|--------------------------------|
| Class                  | Class Diagram         | Full UML notation              |
| Component              | Architecture Diagram  | Use colored fills per component|
| Deployment             | Architecture Diagram  | Add node/instance labels       |
| Communication          | —                     | Approximate with Sequence      |
| Interaction Overview   | Flowchart             | Combine activity + sequence    |
| ...                    |                       |                                |
```

14 种 UML 图类型 → 实际支持的 10 种图类型的**显式映射表**。好处：
- 用户问“部署图”，Skill 明确映射到“Architecture Diagram + 加实例标签”——**不会漂移**到某个折中方案
- 不支持的类型（Communication）**明示“—”**——不假装支持
- 每行有 Notes 指出差异，用户可预期结果

**迁移到 Ohmybrain**：可在 `llm-wiki` 或 `source-summary` skill 里加类似表：
- “Zotero 条目类型 → wiki source_type” 映射
- “用户口头描述 → wiki 目录” 映射（“笔记” → notes、“论文” → papers、“文章” → articles）

减少每次摄入时的**分类漂移**。

### 5. MANDATORY: Python List Method —— 经验 best practice 硬规约化

```python
# Heredoc style: each line appended separately, then joined
lines = []
lines.append("<svg viewBox=\"0 0 960 700\">")
lines.append("  <defs>")
# ... each line separately
lines.append("</svg>")

with open("/path/to/output.svg", "w") as f:
    f.write("
".join(lines))
```

**Why mandatory**: Prevents character truncation, typos, and syntax errors. Each line is independent and easy to verify.

**工程含义**：把一个具体的**实现风格（列表累加再 join）** 直接写进 SKILL——不是“建议”而是“**MANDATORY**”。加上列出的 **Common Syntax Errors to Avoid**（`yt-anchor` -> `y="60" text-anchor="middle"` 这类真实踩坑），把模型**可能写错**的东西**前置提醒**。

**对比 Ohmybrain**：`llm-wiki` SKILL 提了 frontmatter 字段规范，但没提“写 frontmatter 时常见错误”（如 `source-type` vs `source_type` 下划线/连字符混用——这事确实发生过）。可借鉴加一节 “Common frontmatter errors to avoid”。

### 6. Skill 可打包可发布

```json
{
  "name": "@yizhiyanhua-ai/fireworks-tech-graph",
  "version": "1.0.4",
  "main": "SKILL.md",
  "files": ["SKILL.md", "references/", "scripts/", "fixtures/", "templates/", "assets/"],
  "engines": { "node": ">=14.0.0" }
}
```

```bash
npx skills add yizhiyanhua-ai/fireworks-tech-graph            # 安装
npx skills add yizhiyanhua-ai/fireworks-tech-graph --force -g -y  # 更新
```

**可版本化、可分享、可回滚、可依赖声明**。Ohmybrain 当前的 skill 裸存于 `~/.claude/skills/`，没有版本、没有 changelog、改一次就没历史。

**迁移方向**（非紧急，记在本子里）：
- 如果 Ohmybrain 的 `llm-wiki` skill 未来要给其他用户或项目复用——打包成 `@lyrenleigh/llm-wiki-skill`
- 至少先**加个 `skill.json` 记版本和依赖**，为以后打包留钩子
- 但当下 Ohmybrain 一人用，过早打包 = YAGNI

### 7. agents/openai.yaml —— 多 runtime 兼容

```yaml
interface:
  display_name: "Fireworks Tech Graph"
  short_description: "Generate polished SVG and PNG technical diagrams"
  default_prompt: "Turn the user system or workflow description into a polished SVG diagram and export a PNG."
```

仓内有 `agents/openai.yaml`——说明这个 skill **不仅给 Claude Code 用，也兼容 OpenAI Codex / 其他 agent runtime**。这呼应 [[nousresearch-hermes-agent|Hermes]] “不绑死单一 runtime” 的策略——**Skill 的价值单元应该可跨 runtime 复用**。

**对 Ohmybrain**：如果未来探索 Codex / Cursor / Continue.dev 等其他 runtime——skill 设计时就把 **runtime-specific 配置外置**（像 fireworks 把 OpenAI adapter 放在 `agents/openai.yaml`）。SKILL.md 本体只写规范和流程，不写“给 Claude 的指令”。

## 架构核心

### 工作流（Skill 强制执行顺序）

```
1. Classify      图类型判断（14 类）
2. Extract       从用户描述抽层/节点/边/流
3. Plan layout   套用该图类型的布局规则
4. Load style    按需 Read references/style-N.md
5. Map shapes    套用 Shape Vocabulary（概念 -> 形状）
6. Check icons   按需 Read references/icons.md
7. Write SVG     MANDATORY Python List Method
8. Validate      rsvg-convert file.svg -o /dev/null
9. Export PNG    rsvg-convert -w 1920 file.svg
10. Report       返回生成的文件路径
```

### 语义形状词汇表（跨风格一致）

一套“概念 -> 形状”映射**跨所有 7 种风格复用**：

| 概念 | 形状 |
|------|------|
| User | Circle + body path |
| LLM | Rounded rect + brain/spark icon |
| Agent | Hexagon or rounded rect with double border |
| Memory (short-term) | Dashed border rect (ephemeral) |
| Memory (long-term) | Cylinder (persistent) |
| Vector Store | Cylinder + grid lines |
| Graph DB | Circle cluster (3 overlapping) |
| Tool | Gear-like rect |
| API Gateway | Hexagon (single border) |
| Queue | Horizontal tube |
| Decision | Diamond |
| Data | Parallelogram |

**工程价值**：用户只需描述“系统有个 Vector Store”——Skill 自动知道画**带内环圆柱**。用户**不用学 SVG**，也不用为每种风格单独记形状。

### 语义箭头系统

| Flow Type | Color | Dash | Meaning |
|-----------|-------|------|---------|
| Primary data flow | `#2563eb` | solid | Main path |
| Control / trigger | `#ea580c` | solid | Triggering |
| Memory read | `#059669` | solid | Retrieval |
| Memory write | `#059669` | `5,3` | Write op |
| Async / event | `#6b7280` | `4,2` | Non-blocking |
| Embedding | `#7c3aed` | solid | Transform |
| Feedback loop | `#7c3aed` | curved | Iterative |

**Always include a legend when 2+ arrow types are used**——这也是硬规约，不是建议。

## 对 Ohmybrain 的启发

### 现在就能做

#### 1. `llm-wiki` skill 三层化（对应观点 1）

当前 `~/.claude/skills/llm-wiki/SKILL.md` 一个文件承载所有协议。仿 fireworks 拆为：

```
~/.claude/skills/llm-wiki/
├── SKILL.md                        入口：触发条件 + 决策树 + 流程编号
├── references/
│   ├── frontmatter-spec.md         每种 type 的 frontmatter 字段
│   ├── slug-patterns.md            作者-年份-关键词等规则
│   ├── wikilink-conventions.md     [[slug]] 写法 + 反向链接
│   ├── directory-roles.md          concepts/entities/source-summaries 用途
│   └── common-errors.md            frontmatter 常见错误清单
├── templates/*.md                  可链接到 .obsidian/templates/
└── fixtures/
    └── example-concept.md           典型好 concept 页参考
```

**主 SKILL.md 只写**：何时触发、决策树、流程编号、必要时 Read 哪个 references 文件。

收益：
- 写 concept 页时不加载 slug 规则；写 paper 摘要时不加载 concept 字段规范——**按需加载减少 token 消耗**
- `common-errors.md` 可以累积实际踩的坑（`source-type` vs `source_type` 等）

#### 2. 给 `llm-wiki` skill 加触发关键词（对应观点 2）

现状：
```yaml
paths: wiki/**
```

改为：
```yaml
paths: wiki/**
description: >-
  Use when user writes to wiki/, runs /ingest or /promote-answer,
  or describes knowledge work. Trigger on: "记笔记" "沉淀到 wiki"
  "写回 Hub" "这个值得记" "/promote" "/ingest" "摘要一下"
  "note this" "save to wiki" "promote to hub".
```

**效果**：即使用户没先打开 wiki 文件，说“这个结论值得沉淀”也能触发 skill 激活。

#### 3. 给 `wiki-ingester` agent 加 Pre-Tool-Call + Error Recovery（对应观点 3）—— 最急

当前 `wiki-ingester` 遇 PDF 乱码会反复调 PyMuPDF。在其 agent spec 加：

```markdown
## Pre-Tool-Call Checklist

Before invoking transcribe.py / PyMuPDF / ffmpeg:
1. Have you verified the file exists and is not empty?
2. Have you checked file encoding / MIME type?
3. Do you have the correct parameters ready?

If ANY answer is NO: STOP. Do NOT retry. Report the issue.

## Error Recovery Protocol

First PDF extraction error:  Try PyMuPDF with different text mode
Second error:                Switch to multimodal OCR
Third error:                 STOP. Report failure. Do NOT write any wiki file.
Never:                       Retry the same command with same parameters.
```

预估 30 分钟可移植，解决已知痛点。

### 值得规划

#### 4. UML-style 映射表收敛概念漂移（对应观点 4）

为 Ohmybrain 的**摄入分类**写显式映射表。加到 `~/.claude/skills/llm-wiki/references/ingest-classification.md`：

```markdown
| 用户口头 | wiki 目录 | source_type |
|---------|----------|------------|
| “我读了一篇论文” | source-summaries/ | paper |
| “这篇文章有意思” | source-summaries/ | article |
| “某人的某个观点” | source-summaries/ | thread |
| “理解了一个概念” | concepts/ | (不是 summary) |
| “某个工具/人物” | entities/ | (不是 summary) |
| “实验结论” | source-summaries/ 或 explorations/ | note |
| “架构规划” | explorations/ | note |
```

减少每次摄入时反复思考“这该放哪儿”。

#### 5. 把“常见 frontmatter 错误”写成 references/common-errors.md（对应观点 5）

照抄 fireworks 的 Common Syntax Errors to Avoid 模式：

```markdown
## Common Wiki Frontmatter Errors

- ERR  source-type: paper    -> OK  source_type: paper (underscore)
- ERR  created: 2026/04/14   -> OK  created: 2026-04-14 (dash)
- ERR  tags: Claude-Code, Skill  -> OK  tags: [Claude-Code, Skill] (YAML list)
- ERR  [[slug.md]]           -> OK  [[slug]] (no extension)
- ERR  type: summary         -> OK  type: source-summary (full form)
```

每踩一次坑加一条，skill 自己会变得更健壮。

### 记在本子里

#### 6. Skill 未来打包（对应观点 6）

非紧急。单人使用阶段不需要 npm 打包。但如果以后有同行愿意复用 Ohmybrain 的 `llm-wiki` skill——可参考 fireworks 的 `package.json` + `npx skills add {owner}/{repo}` 模式。

#### 7. Multi-runtime 兼容（对应观点 7）

如果未来探索 OpenAI Codex 或 Continue.dev——skill 设计时把 runtime-specific 配置外置。当下 Claude Code only，无需操心。

## 对标已有 wiki 的交叉引用

本 summary 补充而非替代以下页面：

- [[claude-code-best-practice]]：shanraisshan 参考仓——也展示 skill 工程化，但偏“配置最佳实践总集”，fireworks 偏“单一 skill 的深度范本”
- [[nousresearch-hermes-agent]]：Hermes 用 agentskills.io 开放标准；fireworks 是 Claude Code 私有格式 + npm 打包——两种打包哲学对照
- [[skills-vs-commands]]：三机制对比的概念总表；本 summary 展示具体 Skill 实现范本
- [[skill-layered-resources]]：本次新建——把三层资源模式抽象为可复用概念
- [[subagents-orchestration]]：本 summary 的 Pre-Tool-Call 协议对 wiki-ingester agent 直接可移植
- [[claude-hooks-architecture]]：Pre-Tool-Call checklist 是“**内部自律版 hook**”——和 hook 的“外部确定性约束”哲学同构
- [[ohmybrain-agent-architecture-insights]]：本 summary 的启发条目可并入该规划 doc 作为“现在就能做” §3 的扩充

## 引用摘录

> **MANDATORY: Python List Method** (ALWAYS use this) — Why mandatory: Prevents character truncation, typos, and syntax errors. Each line is independent and easy to verify.

> **Pre-Tool-Call Checklist** (CRITICAL - use EVERY time): If ANY answer is NO: STOP. Do NOT call the tool. Prepare the content first.

> **Error Recovery Protocol** — Third error: STOP and report to user - do NOT loop endlessly. Never: Retry the same failing command or call tools with empty parameters.

## 来源

- 本地路径：`raw/repos/yizhiyanhua-ai-fireworks-tech-graph/SKILL.md`
- npm 包：`@yizhiyanhua-ai/fireworks-tech-graph` v1.0.4
- GitHub：`github.com/yizhiyanhua-ai/fireworks-tech-graph`
- 相关 summary：[[claude-code-best-practice]]、[[nousresearch-hermes-agent]]
- 相关 concept：[[skills-vs-commands]]、[[skill-layered-resources]]、[[subagents-orchestration]]、[[claude-hooks-architecture]]
- 相关实体：[[claude-code]]
- 相关探索：[[ohmybrain-agent-architecture-insights]]
