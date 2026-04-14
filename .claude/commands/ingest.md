---
description: 摄入 Hub raw/ 中的原始资料到 Hub wiki/。自治多步决策（提取/写页/交叉引用）委托给 wiki-ingester 子代理，主会话做入口编排 + index/log 同步 + 验证。
---

# Ingest — Hub 知识摄入工作流

将 `raw/` 中的原始资料摄入到 `wiki/` 知识体系。Hub 是跨项目知识终点，不向上回流。

## 架构

```
用户 /ingest <args>
    ↓
主会话（Command）
    ├─ Step 1: 解析/扫描 raw/（入口编排）
    ├─ Step 2-4: 委托 wiki-ingester Agent（独立上下文，读-判-写-交叉引用）
    └─ Step 5-7: 同步 index.md + 追加 log.md + 运行 lint（机械同步 + 验证）
```

为什么这样拆？

- **Step 2-4 需要"自治多步决策"**（探索 raw/ 结构、挑模板、判定 slug、识别相关 concept 做交叉引用）——代码仓/长论文/视频会把主会话上下文打满，应在独立上下文执行
- **Step 5-7 是机械同步 + 用户可见的审计点**——保留在主会话，便于用户看到 index 增长、log 追加

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

### Step 2-4: 委托 wiki-ingester Agent（主会话调 Agent tool）

```
Agent(
  subagent_type="wiki-ingester",
  description="摄入 {raw_path} 到 wiki",
  prompt="raw_path: {raw_path}\nuser_intent: {可选的用户意图}"
)
```

**等待 Agent 返回结构化报告**，内容形如：

```
## wiki-ingester 摄入报告
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

**若 Agent 报错**（资料损坏、slug 冲突、概念边界不清）：

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
1. Step 1 列清单让用户全选
2. 对每份逐一调 `wiki-ingester` Agent（串行；若追求速度可并行，但主会话要汇总所有 Agent 报告后再一次性 Step 5-6）
3. Step 5-6 批量处理（一次性更新 index.md + 单条 log.md 条目涵盖所有）
4. Step 7 最后统一校验

## 硬约束

- **raw/ 只读**（PreToolUse hook `check_raw_write.py` 强制）
- **Hub 是终点**：无 `/promote-answer`；下游项目把结论 promote 到 Hub
- **中文撰写**
- **slug 规则**见 `.claude/agents/wiki-ingester.md`
- **wikilink** `[[slug]]` 不带 `.md`

## 相关

- Agent 定义：`.claude/agents/wiki-ingester.md`
- Wiki 操作 skill（自动激活）：`~/.claude/skills/llm-wiki/SKILL.md`
- Hook 配置：`.claude/settings.json`
