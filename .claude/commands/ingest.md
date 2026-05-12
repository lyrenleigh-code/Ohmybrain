---
description: 摄入 Hub raw/ 中的原始资料到 Hub wiki/。先预判规模并询问用户选路径（inline 主会话内联 / agent 委托 wiki-ingester 子代理），主会话做入口编排 + index/log 同步 + 验证。
---

# Ingest — Hub 知识摄入工作流

将 `raw/` 中的原始资料摄入到 `wiki/` 知识体系。Hub 是跨项目知识终点，不向上回流。

## 架构

```
用户 /ingest <args>
    ↓
主会话（Command）
    ├─ Step 1:   解析/扫描 raw/（入口编排）
    ├─ Step 1.5: 预判资料规模 + 询问用户选路径  ← 新增
    ├─ Step 2-4: 二选一执行
    │    ├─ 路径 A [inline]：主会话内联（依赖 llm-wiki skill）
    │    └─ 路径 B [agent] ：委托 wiki-ingester Agent（独立上下文）
    └─ Step 5-7: 同步 index.md + 追加 log.md + 运行 lint（机械同步 + 验证）
```

为什么这样拆？

- **Step 2-4 是规模敏感的**：长论文/大仓需要独立上下文保护主会话；短笔记/短文重型 agent 划不来，主会话内联更快
- **Step 1.5 的存在理由**：规模阈值不是绝对的（例如篇幅短但数学密集的论文可能仍需 agent；主题冷门的小笔记用户可能想让 agent 多挖一挖）——最终决定权交给用户
- **两条路径产出同构的"摄入报告"**：Step 5-7 与用户选哪条无关，机械消费即可
- **Step 5-7 是机械同步 + 用户可见的审计点**：保留在主会话，便于用户看到 index 增长、log 追加

## 使用方式

```
/ingest <文件或主题>
/ingest                    # 无参数: 扫描 raw/ 列出未摄入
```

## raw/ 子目录速查

| 子目录 | 类型 | 模板 |
|------|------|------|
| `papers/` | 论文 PDF | `paper-note.md` |
| `articles/` `notes/` `threads/` | 文本类 | `source-summary.md` |
| `books/` `courses/` | 章节/讲义 | `source-summary.md` |
| `repos/` | 代码仓 | `source-summary.md`（repo 专项字段） |
| `videos/` `podcasts/` | 先 transcribe | `source-summary.md` |
| `assets/` | 图片 | 不摄入，被其他页引用 |

## 执行流程

### Step 1: 识别待摄入资料（主会话）

从 `$ARGUMENTS` 解析目标：

- **有参数**：直接定位 raw/ 下路径（若用户给了 URL/主题，先映射到路径；不存在则报错）
- **无参数**：扫描 `raw/` 除 `assets/` 外所有子目录，对比 `wiki/index.md` Source Summaries 段，列出未摄入清单，请用户挑选

### Step 1.5: 预判规模 + 询问用户选路径（主会话）

对 Step 1 确定的每份资料，先做**规模预判**：

| 类型 | 短（建议 inline） | 长（建议 agent） | 测量方式 |
|------|------------------|-----------------|---------|
| 文本（md / txt） | < 5k 字 | ≥ 5k 字 | `wc -m <file>` |
| PDF | < 10 页且无公式推导 | ≥ 10 页或数学密集 | `python -c "import pymupdf; print(pymupdf.open('...').page_count)"` |
| 代码仓 | 单文件或纯 README | 多模块/插件架构 | `ls raw/repos/{name}/` 看目录数 |
| 视频/播客转录 | < 15 min | ≥ 15 min | 转录 md 的 `wc -l` |

**然后通过 AskUserQuestion 询问用户**——无论预判倾向如何都要问，规模不是唯一决策因子（"这次想快"或"这次想细"会推翻默认）：

```
问：摄入 {raw_path}，预判为「{短|长}」（依据：{字数/页数/...}）。选路径：
  - [inline] 主会话内联处理（快，但吃主会话上下文）
  - [agent]  委托 wiki-ingester Agent（~300s+，独立上下文、可并行）
默认高亮推荐项，用户回车接受或显式选另一条
```

**批量摄入**时增加"批次统一"选项，见本文末 [批量摄入](#批量摄入)。

### Step 2-4: 二选一执行

用户选择 `inline` 或 `agent` 后分别执行。两条路径的产出都是等价的"摄入报告"结构（见下方**报告契约**），Step 5-7 统一消费。

#### 路径 A — 主会话内联（inline）

`llm-wiki` skill 已因 `paths: wiki/**` 自动激活（协议细则见 `~/.claude/skills/llm-wiki/SKILL.md`）。主会话按以下步骤完成：

1. **读原材料**：一次性 `Read` raw/ 下文件（PDF 用 Read 的 `pages:` 参数或 PyMuPDF 提取前 N 页）
2. **选模板**：按类型取 `.obsidian/templates/source-summary.md` 或 `paper-note.md`
3. **拟 slug**：按 llm-wiki skill 的 slug 规则（论文 `{姓拼音}-{年}-{关键词}`、仓库 `{owner}-{repo}` 等）
4. **写 source-summary 页**：`Write wiki/source-summaries/{slug}.md`
5. **交叉引用**：识别 1–3 个相关 concept / entity，在各自"来源"段追加 `[[{slug}]]`
6. **组装报告**：在主会话内形成与 agent 同构的结构化报告（见下），直接进入 Step 5

#### 路径 B — 委托 wiki-ingester Agent（agent）

**首选调用**（2026-05-12 起 wiki-ingester 已迁至全局 `~/.claude/agents/wiki-ingester.md`）：

```
Agent(
  subagent_type="wiki-ingester",
  description="摄入 {raw_path} 到 wiki",
  prompt="raw_path: {raw_path}\nuser_intent: {可选的用户意图，含扩展关键词}"
)
```

**Fallback — general-purpose 内联契约**（如 subagent_type 列表无 wiki-ingester，或全局 agent 被 harness 屏蔽）：

```
Agent(
  subagent_type="general-purpose",
  description="摄入 {raw_path}（wiki-ingester 契约内联）",
  prompt="""
你扮演 wiki-ingester。**先 Read `~/.claude/agents/wiki-ingester.md`** 作为完整契约（含职责/预算/流程/硬约束/输出契约），然后按其执行。

raw_path: {raw_path}
user_intent: {可选}

注意：若 Write 工具被 harness 拒（subagent 权限受限），把所有应落盘内容**内联到输出报告**——
- 新建页：用 ` ```markdown ... ``` ` 完整给出文件内容 + 目标路径
- 更新页（追加 wikilink）：给出"目标文件 + 要追加的 wikilink 行"
主会话会按此代为落盘（feedback_subagent_write_permission 标准后备）。
"""
)
```

**主会话代写后备**（即便首选路径，subagent Write 仍可能被拒）：

- 当 agent 报告含 `wiki/...` 文件路径但实际未落盘（用 `Glob` 验证）→ 视为 Write 失败
- 从报告中提取内联内容主会话代写
- 2026-04-22 6 篇 doppler 摄入验证：6 个 agent 中 5 个需主会话代写，是默认后备

**user_intent 扩展关键词**（默认不开；超出默认行为的动作必须显式带关键词，否则 agent 会退化为提案——见 `~/.claude/agents/wiki-ingester.md §预算与默认行为`）：

| 关键词 | 放开什么 |
|-------|---------|
| `depth: full` | summary 放宽到 ≤400 行、核心观点 8-12 条、启发 10-15 条 |
| `new_concepts_ok` | 允许自建新 concept 页 |
| `new_entities_ok` | 允许自建新 entity 页 |
| `allow_new_sections` | 允许在已有 concept/entity 里加新"## 小节" |
| `allow_paragraph_edit` | 允许改写已有段落 |
| `wide_cross_ref` | 放开"≤5 个已有页更新"上限 |

默认（不传任何扩展关键词）= summary ≤200 行 / ≤5 页 cross-ref / 仅追加 wikilink 行 / 新概念与小节都走"备注提案"路径。

**等待 Agent 返回结构化报告**。

#### 报告契约（两条路径共用）

```
## 摄入报告
### 元数据
- slug: ...
- source_type: ...
### 新建页面
- wiki/source-summaries/{slug}.md
### 更新页面
- wiki/concepts/{existing}.md
### 一句话摘要（主会话写入 log.md）
> ...
### 备注
...
```

**若报错**（资料损坏、slug 冲突、概念边界不清）：

- 不执行 Step 5-6
- 把报告的"备注"转述给用户，等用户决策后重启或跳过

### Step 5: 同步 wiki/index.md（主会话）

读取 Agent 报告"新建页面"清单：

- 每个 `source-summaries/*.md` → 在 Source Summaries 段落追加 `- [slug](source-summaries/slug.md) — 一句话描述`
- 每个 `concepts/*.md` → 在 Concepts 段落追加同格式行
- 每个 `entities/*.md` → 在 Entities 段落追加同格式行
- 更新页面总数（顶部 "页面总数：N"）

### Step 6: 追加 wiki/log.md（主会话）

在最顶部插入新条目：

```markdown
## [YYYY-MM-DD] ingest | {类型}：{标题}

{一句话摘要（来自 Agent 报告）}

- 新建 source-summary: wiki/source-summaries/{slug}.md
- 更新 concepts: ... (若有)

更新 index.md（页面总数 N → N+k）。

---
```

### Step 7: 验证（主会话）

```bash
python scripts/lint_wiki.py
python scripts/check_index_log_sync.py
```

两项都通过才算完成。PostToolUse hook 每次 wiki/ 写入已自动跑过 `lint_wiki.py`，这里手动再跑一次作最终确认。

## 批量摄入

多份资料时：

1. **Step 1**：列清单让用户全选
2. **Step 1.5（批次模式）**：先问一次"统一策略"——
   - `全部 inline`：所有资料主会话内联处理（适合批次规模小、整体短）
   - `全部 agent`：所有资料并行委托 Agent（适合批次含长资料，可同一消息内起 N 个 Agent 工具块，独立上下文互不干扰）
   - `混合 / 逐个询问`：每份资料各自在 Step 1.5 再问一次
3. **Step 2-4**：按选定策略执行
   - 全部 agent 且并行：主会话在一条消息内发起 N 个 `Agent(subagent_type="wiki-ingester", ...)`，汇总所有报告后再进 Step 5
   - 全部 inline：主会话逐份 Read→Write→交叉引用
   - 混合：按每份的选择分别执行
4. **Step 5-6**：批量处理（一次性更新 index.md + 一条 log.md 条目涵盖全部）
5. **Step 7**：最后统一校验

**并行约束**（agent 路径）：多个 agent 只写自己的 source-summary，**不**编辑 concept/index/log；cross-ref 提案在各自报告中给出，主会话汇总后批量应用——避免 race condition（4/14 USBL 8 篇并行摄入已验证此模式）。

## 硬约束

- **raw/ 只读**（PreToolUse hook `check_raw_write.py` 强制）
- **Hub 是终点**：无 `/promote-answer`；下游项目把结论 promote 到 Hub
- **中文撰写**
- **slug 规则**见 `.claude/agents/wiki-ingester.md`
- **wikilink** `[[slug]]` 不带 `.md`

## 相关

- Agent 定义（全局，首选）：`~/.claude/agents/wiki-ingester.md`
- Agent 定义（项目本地，契约源头/参考）：`.claude/agents/wiki-ingester.md`
- Wiki 操作 skill（自动激活）：`~/.claude/skills/llm-wiki/SKILL.md`
- Hook 配置：`.claude/settings.json`
