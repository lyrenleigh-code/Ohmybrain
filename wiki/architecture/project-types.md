---
type: architecture
created: 2026-05-24
updated: 2026-06-09
tags: [项目类型, 模板, 派生, project-types]
---

# 三类项目模板

ohmybrain 体系下的项目实际分 3 类，`ohmybrain-core` 已落地三套模板：`template-engineering/`、`template-document/`、`template-tool/`。新项目先判断主交付物，再按类型派生；硬件设计项目归入 engineering 的硬件子型。

## 三类项目识别

### Type 1: Engineering / 实际开发 (TechReq/*)

**主交付物**：算法代码（MATLAB / Python / C++ 等）

**例**：UWAcomm / USBL / UWAnet / UWAcomm_usbl

**特征**：
- src/ 或 modules/ 是主战场
- V→V→V 工作流 + RCA 子环节
- engineering.validate 失败 → RCA → fix → 下一 V
- 重 `wiki/debug-logs/` + `wiki/modules/`
- 重 `tests/` + `evals/`

#### Engineering-hardware / 硬件设计子型

**主交付物**：硬件需求、阵列/电路/结构设计、接口定义、BOM、datasheet、原理图/PCB/机械资料、样机验证记录。

**派生方式**：仍从 `template-engineering/` 派生到 `D:\Claude\TechReq\<name>/`，再补硬件目录：

```
design/requirements/
design/schematics/
design/pcb/
design/mechanical/
design/interfaces/
design/reviews/
bom/
datasheets/
output/
prototypes/
tests/
```

`src/` 保留给仿真脚本、固件小样、设计计算或自动化校验；不要为了硬套软件项目而把设计资料塞进 `src/`。

### Type 2: Document / 文档撰写 (DocProcess/*)

**主交付物**：docx / pdf 报告 / 方案

**例**：UWAprojDoc / Pricing / CooperativeDetection / PaperReview / DigitalTwinGuide

**特征**：
- specs/active/ 写章节大纲
- output/ 是主战场（docx / pdf 输出）
- 文档撰写闭环 (spec → draft → validate → archive) 代替 engineering 闭环
- 重 wiki/topics/（专题文档）+ wiki/source-summaries/（资料源）
- 走 `flowgen-*` 8 skill 套件出图
- **几乎全是私人项目** 🔒（不进公开 Hub）
- `src/` `tests/` `evals/` 闲置

### Type 3: Tool / 工具 (Tools/*)

**主交付物**：可复用 skill / template

**例**：FlowGen / IconForge / AnthropicPPT

**特征**：
- templates/ 是主战场（模板源码）
- output/sample/ 是演示输出
- skill 注册到 `~/.claude/skills/<name>/SKILL.md`
- 工具开发闭环 (design → implement → test → register-skill → docs)
- engineering 闭环 4 步只用部分
- 通常**开放**（无 🔒）

## 三模板对比

| 维度 | template-engineering | template-document | template-tool |
|------|---------------------|-------------------|---------------|
| **核心目录** | src/ modules/ tests/ evals/ specs/ plans/ handoff/ wiki/ raw/ scripts/ | specs/ plans/ handoff/ wiki/ raw/ output/ scripts/ | templates/ specs/ plans/ handoff/ wiki/ scripts/ output/sample/ |
| **硬件子型扩展** | design/ bom/ datasheets/ prototypes/ output/ | — | — |
| **主战场** | 代码 / 仿真 / 测试 / 硬件设计资料 | 文档输出与资料提炼 | 模板源码、skill、样例输出 |
| **wiki 子目录重点** | concepts / modules / debug-logs / conclusions.md | concepts / topics / source-summaries | concepts / architecture |
| **workflows/** | knowledge + engineering (4+4) | knowledge + document (4+4) | knowledge + tool (4+5) |
| **主 skill** | tech-requirements / ingest / promote-answer | flowgen-* / docx / pdf / 项目特化 | skill-creator + 自身产出 skill |
| **私人标记** | 部分 🔒 (UWAcomm_usbl) | 全 🔒 | 通常开放 |
| **commit 风格** | feat(algorithm): / fix(rca): | docs(spec): / docs(draft): | feat(skill): / feat(template): |
| **典型 hooks** | check_raw_write / check_index_log_sync | check_raw_write + **check_private_tags** + check_index_log_sync | 较少 |

## 文档撰写闭环（Type 2 特有）

替代 engineering 闭环：

```
01 spec   → 02 draft → 03 validate → 04 archive
   ↑                                    ↓
   └──── 弱触发新章节（archive 后触发新 spec）
```

| 步骤 | 动词 | 触发 | 产出 |
|------|------|------|------|
| **01** | `spec` | 新文档 / 新章节启动 | `specs/active/<slug>.md` (章节大纲 + 验收点) |
| **02** | `draft` | spec 完成 | `output/` docx / pdf 初稿 |
| **03** | `validate` | draft 完成 | 用户审查 + 自查清单 |
| **04** | `archive` | 用户终审通过 | spec → specs/archive/，output 标 final |

## 工具开发闭环（Type 3 特有）

```
01 design → 02 implement → 03 test → 04 register-skill → 05 docs
                                            ↓
                                    skill 注册到 ~/.claude/skills/
```

| 步骤 | 动词 | 触发 | 产出 |
|------|------|------|------|
| **01** | `design` | 新工具想法 | `specs/active/<slug>.md` (接口 / 参数 / 输出形态) |
| **02** | `implement` | design 完成 | `templates/` 模板源码 + helpers |
| **03** | `test` | implement 完成 | `output/sample/` demo + 真实 case 验证 |
| **04** | `register-skill` | test 通过 | `~/.claude/skills/<name>/SKILL.md` 关键词触发 |
| **05** | `docs` | skill 注册 | CLAUDE.md + wiki/architecture/design-system.md |

## 派生工作流（当前）

```bash
# 按类型选模板
cp -r D:/Claude/ohmybrain-core/template-engineering/  → D:/Claude/TechReq/<name>/
cp -r D:/Claude/ohmybrain-core/template-document/     → D:/Claude/DocProcess/<name>/
cp -r D:/Claude/ohmybrain-core/template-tool/         → D:/Claude/Tools/<name>/
```

派生时根据项目类型直接选对的模板，常规项目可直接开始；硬件等子型只补少量类型化目录。

硬件设计项目使用第一条 engineering 路径，派生后按上文补 `design/`、`bom/`、`datasheets/` 等硬件资料目录。

## 实施记录（已完成 2026-05-24）

✓ **已落地**（ohmybrain-core commit `247986a`，已 push gitlab/main）：

1. ✓ `template/` → `template-engineering/`（git mv 保留 history）
2. ✓ 新建 `template-document/`（含 `workflows/document/` 4 步 + output/ 占位 + 改 CLAUDE.md）
3. ✓ 新建 `template-tool/`（含 `workflows/tool/` 5 步 + templates/ + output/sample/ + 改 CLAUDE.md）
4. ✓ `docs/new-project-sop.md` 加 §0 三模板决策树 + 派生命令
5. ✓ ohmybrain-core 仓 commit + push

✓ **2026-06-09 追加同步**：
6. 三模板补齐 `AGENTS.md`、`specs/active/`、`plans/active/`、`handoff/active/` 协作目录
7. `docs/new-project-sop.md`、Hub 入口、架构页统一为三模板 + Agent 协作协议口径
8. 新增 engineering-hardware 子型，用于单独硬件设计项目

## 与现有体系的关联

- [[three-tier-architecture]] § core = 被动模板 → 现在是**三种**被动模板
- [[hub-as-brain]] § 通道 3 update template → 三 template 都可能被 update
- [[core-update-queue]] → 候选标记应说明"属于哪个 template"
- [[core-update-mechanism]] § 安全约束 → 加"不要把 engineering 模板的 src/ 强加给 document/tool 模板"

## 演化记录

- **2026-05-24** 三模板设计与 ohmybrain-core 拆分落地
- **2026-06-09** 文档口径同步，补充 Agent 协作目录与硬件设计子型
