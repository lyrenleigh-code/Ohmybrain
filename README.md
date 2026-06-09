# Ohmybrain — 个人知识库 + 项目导航 Hub

> Personal Knowledge Base & Project Navigation Hub
>
> 跨项目知识沉淀与导航中心，承载论文摘要、概念实体、架构页、研究地图、探索笔记等所有"非项目代码"层的知识资产。

---

## 定位

**Ohmybrain 不是项目仓库，而是知识中心**。具体算法和工程闭环放在各 TechReq/Tools 子项目里，跨项目可复用的结论、领域知识、工具经验、论文笔记一律沉淀到这里。

```
ohmybrain-core（母仓 / 模板，三模板拆分：engineering / document / tool）
  ├→ 派生 → UWAcomm                  (TechReq, engineering)
  ├→ 派生 → USBL                     (TechReq, engineering)
  ├→ 派生 → UWAnet                   (TechReq, engineering)
  ├→ 派生 → UWAcomm_usbl 🔒          (TechReq, engineering)
  ├→ 派生 → SonarSim 🔒              (TechReq, engineering, 2026-06-03)
  ├→ 派生 → FlowGen                  (Tools, tool)
  ├→ 派生 → AnthropicPPT             (Tools, tool, 2026-05-23)
  ├→ 派生 → IconForge                (Tools, tool, 2026-05-29)
  ├→ 派生 → Pricing 🔒               (DocProcess, document)
  └→ 派生 → UWAprojDoc 🔒 等 7 个文档项目 (DocProcess, document)

ohmybrain（本仓库 = 知识库 + Hub）
  ├── raw/        只读原始资料（论文 / 文章 / 视频 / 仓库参考）
  ├── wiki/       跨项目知识沉淀（107 页内容页 + index/log）
  ├── projects/   项目导航总览
  └── scripts/    知识库自动化脚本
```

---

## 知识规模（2026-06-09）

| 类别 | 数量 | 路径 |
|------|------|------|
| Wiki 内容页 | **107** | `wiki/`（不含根 `index.md` / `log.md`） |
| Concepts（概念页） | 20 | `wiki/concepts/` |
| Entities（实体页） | 8 | `wiki/entities/` |
| Architecture（架构页） | **12** | `wiki/architecture/`（含 system-overview / three-tier-architecture / project-types / document-protocol 等） |
| Agents（Agent 协作页） | **1** | `wiki/agents/` |
| Workflows（流程页） | **1** | `wiki/workflows/` |
| MCP Entities（MCP 图谱投影） | 25 | `wiki/mcp-entities/` |
| Topics（专题页） | **5** | `wiki/topics/`（含 ecosystem-dashboard / harness-resources / memory-index / core-update-queue / research-map） |
| Explorations（探索页） | 4 | `wiki/explorations/` |
| Source Summaries（资料摘要） | 31 | `wiki/source-summaries/` |
| 自动化脚本 | 22 | `scripts/` |

---

## 目录地图

| 目录 | 职责 | 写入约束 |
|------|------|----------|
| `raw/` | 只读原始资料（论文 PDF / 文章 / 视频转录 / 代码仓库参考 / 笔记） | ⛔ Hook 拦截写入 |
| `wiki/` | 跨项目知识层（中文，frontmatter 必备） | 必须同步 `index.md` + `log.md` |
| `wiki/concepts/` | 概念页（如 OFDM/OTFS、信道估计、多普勒估计） | 知识入口 |
| `wiki/entities/` | 实体页（工具：Claude Code / Obsidian / Zotero / Whisper） | 工具卡片 |
| `wiki/architecture/` | 跨项目架构（system-overview / memory-stack / memory-graph） | 顶层视图 |
| `wiki/agents/` | Claude Code / Codex 等 Agent 协作协议 | 协作边界 |
| `wiki/workflows/` | 跨 Agent / 跨会话流程协议 | 交接流程 |
| `wiki/mcp-entities/` | MCP 知识图谱在 wiki 的 Obsidian 投影（Juggl 可视化） | 自动生成 |
| `wiki/source-summaries/` | 论文/仓库/书籍摘要（每篇一页） | `/ingest` 产出 |
| `wiki/explorations/` | 探索笔记 / 方法论 | `/promote` 沉淀 |
| `projects/` | 项目导航卡片（每个子项目一目录） | 项目入口 |
| `scripts/` | 自动化脚本（lint / sync / ingest / scrape / transcribe） | 开放 |
| `.claude/` | harness（rules / skills / commands / hooks） | 开放 |
| `.obsidian/` | Obsidian vault 配置 | 开放 |

---

## 项目仓库映射

| 项目 | GitHub | GitLab 内网 | 本地路径 | 状态 |
|------|--------|-------------|----------|------|
| **UWAcomm** | [lyrenleigh-code/UWAcomm](https://github.com/lyrenleigh-code/UWAcomm) | [lilin/UWAcomm](http://192.168.10.100:8880/lilin/UWAcomm) | `D:\Claude\TechReq\UWAcomm` | 🟢 活跃 |
| **USBL** | [lyrenleigh-code/USBL](https://github.com/lyrenleigh-code/USBL) | [lilin/USBL](http://192.168.10.100:8880/lilin/USBL) | `D:\Claude\TechReq\USBL` | 🟢 活跃 |
| **UWAnet** | [lyrenleigh-code/UWAnet](https://github.com/lyrenleigh-code/UWAnet) | [lilin/UWAnet](http://192.168.10.100:8880/lilin/UWAnet) | `D:\Claude\TechReq\UWAnet` | 🟡 调研 |
| **UWAcomm_usbl** 🔒 | — | [lilin/UWAcomm_usbl](http://192.168.10.100:8880/lilin/UWAcomm_usbl) | `D:\Claude\TechReq\UWAcomm_usbl` | 🟢 活跃（整机原型 / V0.8 大纲） |
| **SonarSim** 🔒 | — | [lilin/SonarSim](http://192.168.10.100:8880/lilin/SonarSim) | `D:\Claude\TechReq\SonarSim` | 🟢 私人（已 commit+push 内网） |
| **ohmybrain-core** | [lyrenleigh-code/ohmybrain-core](https://github.com/lyrenleigh-code/ohmybrain-core) | [lilin/ohmybrain-core](http://192.168.10.100:8880/lilin/ohmybrain-core) | `D:\Claude\ohmybrain-core` | 🟢 母仓（三模板：engineering / document / tool） |
| **Ohmybrain** | [lyrenleigh-code/Ohmybrain](https://github.com/lyrenleigh-code/Ohmybrain) | [lilin/Ohmybrain](http://192.168.10.100:8880/lilin/Ohmybrain) | `D:\Claude\Ohmybrain` | 🟢 Hub |
| **FlowGen** 🔒 | — | [lilin/FlowGen](http://192.168.10.100:8880/lilin/FlowGen) | `D:\Claude\Tools\FlowGen` | 🟢 活跃（7 skill 实装） |
| **IconForge** 🔒 | — | [lilin/IconForge](http://192.168.10.100:8880/lilin/IconForge) | `D:\Claude\Tools\IconForge` | 🟡 起步（自然语言→SVG 图标） |
| **AnthropicPPT** 🔒 | — | [lilin/AnthropicPPT](http://192.168.10.100:8880/lilin/AnthropicPPT) | `D:\Claude\Tools\AnthropicPPT` | 🟡 起步（2026-05-23 派生） |
| **Pricing** 🔒 | — | [lilin/Pricing](http://192.168.10.100:8880/lilin/Pricing) | `D:\Claude\DocProcess\Pricing` | 🟢 私人 |
| **Patents** 🔒 | — | — | `D:\Claude\Patents` | 🟡 私密专利交底书（无 git） |

### DocProcess 私人文档项目（非 git 仓库）

托管于本地 `D:\Claude\DocProcess\`，不入 git/远端：

| 项目 | 派生 | 焦点 |
|------|------|------|
| **UWAprojDoc** 🔒 | 2026-04-28 | 水声专项方案技术文档 v17（33.2 MB / 17 章 / 146 图）|
| **CooperativeDetection** 🔒 | 2026-05-08 | 水下分布式协同探测 4 专题 12 课题（≈ 2400 万元）|
| **PaperReview** 🔒 | 2026-05-09 | 学位论文外审（中文论文中文评审意见）|
| **DigitalTwinGuide** 🔒 | 2026-05-13 | 数字孪生实施指南方法论（首份种子=20 吨级 AUV 课题指南）|
| **DigitalTwin1plusN** 🔒 | 2026-05-25 | 「1+N」水下集群数字孪生体系方案（1 百吨大 U + 24 一吨小 U，双层孪生）|
| **VisioForge** 🔒 | 2026-06-02 | 通用 Visio 出图工作区（为各项目按需产 .vsdx，复用 flowgen-* 8 skill）|
| **CooperativeASW** 🔒 | 2026-06-03 | UWAprojDoc「编队协同探潜配置仿真与效能评估分系统」单列细化 docx（17 章 223k 字 / 24 图 / 969KB，DEPENDS_ON=UWAprojDoc）|

🔒 内网 GitLab Internal 可见或本地私人，**禁止推送至公开 GitHub/Gitee**。所有 GitLab 远端项目统一使用 `main` 主分支（2026-05-25 起，UWAcomm 同步迁移）。

---

## 知识闭环

```
                               【ingest】
   raw/  ────────────────────────────────────────────►  wiki/source-summaries/
   论文/视频/网页/代码仓库                                    每篇一页摘要 + 5 条结论
                                                                  │
                                                                  │【promote】
                                                                  ▼
                                          wiki/concepts/  ◄──  跨项目沉淀
                                          wiki/entities/      （从 source-summaries
                                          wiki/architecture/   抽取共性）
                                                  │
                                                  │【query】
                                                  ▼
   各子项目  ◄────────────────────  跨项目领域问题先查 Hub
   (UWAcomm/USBL/...)                              │
                                                  │【promote】
                                                  ▼
                                          wiki/concepts/  ◄──  项目结论回流
                                          wiki/explorations/    （新算法卡 / 工具经验 /
                                                                  方法论）
```

**四个动词**：

- `/ingest <资料>` → 摄入 raw/ 资料到 wiki/source-summaries/（7 步流程）
- `query` → 子项目启动新任务前先查 wiki/index.md 和 concepts/
- `/promote <结论>` → 子项目结论回流到 Hub（5 步流程）
- `review` → 周期性整理 wiki/log.md 和 wiki/index.md

---

## 常用命令

| 命令 | 用途 | 备注 |
|------|------|------|
| `python scripts/lint_wiki.py` | Wiki 结构检查（frontmatter / 链接 / 死链） | 含 `--quick` 模式 |
| `python scripts/sync_index.py` | 同步 wiki/index.md 页面计数 | log.md 配套 |
| `python scripts/transcribe.py <文件>` | Whisper 音视频转录 → raw/ | 需 whisper + ffmpeg |
| `python scripts/scrape.py <URL>` | Firecrawl 网页抓取 → raw/ | 需 FIRECRAWL_API_KEY |
| `python scripts/import-zotero.py` | Zotero 论文批量导入 → raw/papers/ | |
| `python scripts/import-readwise.py` | Readwise 高亮批量导入 → raw/articles/ | |
| `python scripts/extract_pdf.py <文件>` | PDF 文本抽取（论文摘要预处理） | |
| `python scripts/import_theses.py` | 学位论文批量导入 | |
| `python scripts/generate_mcp_entities.py` | MCP 图谱 → wiki/mcp-entities/ Obsidian 投影 | 自动化 |
| `python scripts/zotero_cleanup.py` | Zotero 库清理 | 一次性脚本 |
| `/ingest` | 摄入命令（slash command） | `.claude/commands/` |
| `/promote` | 回流命令 | `.claude/commands/` |

---

## Hook Exit Code 策略

所有 `scripts/*.py` hook 脚本遵循 Claude Code 的 exit code 契约（借鉴自 [thedotmack-claude-mem](wiki/source-summaries/thedotmack-claude-mem.md)）：

| Exit | 含义 | 触发效果 |
|------|------|----------|
| **0** | 成功 / 优雅放行 | 继续执行，stdout 可见（SessionStart 上下文等） |
| **1** | 非阻断错误 | stderr 显示给用户，继续执行 |
| **2** | 阻断错误 | stderr 喂回 Claude 处理，阻止工具调用 |

**设计原则**：

- **宽松优先**：hook 遇未知输入（JSON 解析失败等）应 `exit 0` 放行，**不阻断无关场景**
- **阻断谨慎**：只在**安全性 / 一致性**被破坏时 `exit 2`：
  - `check_raw_write.py` — 拦截 raw/ 写入
  - `check_private_tags.py` — 拦截 `<private>` 标签外泄到公开 wiki
  - `check_index_log_sync.py` — 拦截 wiki 写入未同步 index/log
- **提醒用 0**：非致命的"顺手提示"用 `exit 0` + stdout（如 `raw_ingest_reminder.py`）
- **Windows Terminal 注意**：大量非 0 exit 可能导致 tab 累积；副作用 hook 默认用 exit 0 + stdout

---

## Wiki 写作约定

- **语言**：所有 wiki 内容用**中文**撰写（技术术语保留英文）
- **Frontmatter 必备**：`title` / `tags` / `date` / `source`（如有）/ `concept`（如有）
- **同步要求**：每次新增/重命名/删除 wiki 页面后，必须更新 `wiki/index.md` 和 `wiki/log.md`
  - Stop hook `check_index_log_sync.py` 会拦截未同步的 commit
- **双向链接**：用 `[[wikilink]]` 链接相关概念/实体（Obsidian 可视化）
- **摘要 5 条结论**：source-summaries 必须含"5 条可迁移结论"章节，便于 promote
- **页面规模**：单页 200-800 行；超过 800 行考虑拆分到 sub-pages

---

## Obsidian 集成

Obsidian vault 注册在 `D:\Claude`（顶层），Ohmybrain 是其中一棵子树。

- **Juggl 可视化**：`wiki/mcp-entities/_index.md` 提供 MCP 知识图谱样式建议
- **MOC 入口**：`wiki/index.md` 是知识地图主入口
- **回链**：所有 source-summaries 用 `[[concept-page]]` 链回 concepts，形成 graph

---

## 三仓架构详解

详见 [`wiki/architecture/system-overview.md`](wiki/architecture/system-overview.md)（2026-04-17 重写）：

- **core 层** = `ohmybrain-core`（母仓模板，新项目派生源）
- **project 层** = TechReq/*、DocProcess/*、Tools/*、Patents/* 等子项目/工作区（自包含业务闭环）
- **hub 层** = `Ohmybrain`（本仓库，跨项目知识中心）

三层职责清晰：core 复用模板、project 闭环算法、hub 沉淀知识。

---

## 自主新建项目工作流

`wiki/explorations/autonomous-new-project-workflow.md` 给出**一行目标 → Phase 0-6 → M1 真装机**的方法论：

- GAN harness（Generator + Evaluator）
- Verification loop（多轮自检）
- 混搭模型（Opus 规划 + Sonnet 实现 + Haiku 评估）
- 红线/升级机制

**首例参考**：UWAnet 重建（2026-04-21），prompts 套件落盘 `projects/uwanet/prompts/`。

---

## 已完成的关键探索

- [system-overview](wiki/architecture/system-overview.md) — 三仓架构总览
- [memory-stack](wiki/architecture/memory-stack.md) — Claude Code 长期记忆 5 层栈
- [memory-graph](wiki/architecture/memory-graph.md) — MCP 知识图谱 Mermaid 快照
- [research-map](wiki/topics/research-map.md) — 10 大研究方向层次结构
- [doppler-estimation-methods](wiki/concepts/doppler-estimation-methods.md) — 6 篇 UWA 多普勒论文跨论文方法学（2026-04-22）
- [usbl-positioning](wiki/concepts/usbl-positioning.md) — USBL 技术链路 + 商用设备参数
- [skill-layered-resources](wiki/concepts/skill-layered-resources.md) — Skill 三层资源分离模式
- [autonomous-new-project-workflow](wiki/explorations/autonomous-new-project-workflow.md) — 自主新建项目方法论

---

## 远端

- **GitHub**：https://github.com/lyrenleigh-code/Ohmybrain（双推 origin）
- **GitLab 内网**：http://192.168.10.100:8880/lilin/Ohmybrain（gitlab）

两端保持同步，`git push origin main` + `git push gitlab main`。

---

## 许可

内部项目，仅供本人 + 授权内部协作者使用。
