# my-brain 工具链指南

> 围绕 harness engineering + LLM wiki 系统，建立完整的个人工作流工具链。
> 更新日期：2026-04-12

---

## 总体架构

```
原始资料来源              收集 & 管理              沉淀 & 执行
──────────────           ──────────────           ──────────────
论文 / PDF          →    Zotero               →   raw/papers/
网页文章            →    Readwise Reader      →   raw/articles/
YouTube 视频        →    Firecrawl / Whisper  →   raw/videos/
本地视频 / 录像     →    Whisper              →   raw/videos/
代码 / 项目资料     →    GitHub               →   raw/ 或直接引用
                              │
                              ▼
                         Claude Code
                        （ingest / harness）
                              │
                              ▼
                           wiki/
                              │
                    ┌─────────┴─────────┐
               Obsidian             GitHub
              （可视化）           （同步 / CI）
```

---

## 核心工具

### Claude Code

**角色：** 整个系统的执行引擎

**主要用途：**
- 执行 ingest、promote、lint 工作流
- 编程和项目开发（主力）
- 维护 harness 规则（hooks、commands）

---

### Obsidian

**角色：** wiki/ 的可视化和浏览层

**为什么选它：** wiki/ 全是 markdown 文件，Obsidian 天然适配，没有格式转换成本，同一份文件在 git 仓库和 Obsidian 里完全一致。

**必装插件：**

| 插件 | 用途 |
|------|------|
| Git | 自动定时 commit + push，多设备免手动同步 |
| Dataview | 把 index.md 变成动态查询，自动列出所有页面 |
| Templater | 给概念页、source-summary 页建模板，保持格式统一 |

**配置建议：**
- 将 my-brain 仓库目录直接作为 Obsidian vault 打开
- Git 插件设置为每 10 分钟自动 commit，每次打开时自动 pull
- 用 Dataview 替代手动维护的 index.md 展示层（index.md 仍保留作 Claude Code 导航用）

---

### GitHub

**角色：** 多设备同步 + 自动化检查

**主要用途：**
- 私有仓库存放 my-brain
- GitHub Actions 每次 push 自动跑 `lint_wiki.py`
- 版本历史作为知识变更记录的最终来源

**建议设置：**
- 仓库设为 **Private**
- 开启 branch protection，防止强推覆盖历史
- Actions 只在 `wiki/` 有变更时触发，节省 CI 资源

---

### Zotero

**角色：** 论文和 PDF 的专属管理器

**为什么需要它：** Zotero 自动抓取论文 metadata（标题、作者、DOI、摘要），导出时比手动整理干净得多，直接作为 source-summary 的基础信息。

**工作流：**
1. 浏览器插件一键收藏论文
2. 自动下载 PDF 到本地
3. 定期将 PDF 复制到 `raw/papers/`，触发 ingest 流程

**与 my-brain 的连接：**
- Zotero 管原始 PDF 和 metadata
- `raw/papers/` 只存 PDF 副本
- source-summary 页引用 Zotero 条目 ID，方便反查

---

### Readwise Reader

**角色：** 网页文章的收集和高亮管理

**为什么需要它：** 直接把网页扔进 `raw/` 格式太乱，Readwise 先做清洗，导出的是干净的 markdown，带高亮和注释，ingest 质量更高。

**工作流：**
1. 浏览器扩展一键收藏文章
2. 阅读时打高亮、加注释
3. 定期导出带高亮的 markdown 到 `raw/articles/`
4. 触发 ingest 流程

**导出设置建议：**
- 导出格式选 markdown
- 包含高亮和注释
- 文件名格式：`YYYY-MM-DD-article-title.md`

---

### 视频处理

**角色：** 把视频内容转成可 ingest 的 markdown，放入 `raw/videos/`

视频是线性的，无法检索，必须先转成文字才能进入 wiki 系统。根据视频来源不同，推荐不同工具：

#### YouTube 视频 → Firecrawl

**适用场景：** YouTube 链接，有字幕或自动字幕

**为什么推荐：** Firecrawl 支持 MCP server，可以直接连接 Claude Code，在 ingest 工作流里不需要额外手动操作，是 AI agent 工作流里最灵活的选项。

**工作方式：**

```bash
# 通过 CLI 直接输出 markdown
firecrawl scrape "https://youtube.com/watch?v=xxxx" --format markdown
```

或在 Claude Code 里通过 MCP 调用，直接把转录结果写入 `raw/videos/`。

---

#### 本地视频 / 无字幕视频 → Whisper

**适用场景：** 本地录像、会议录屏、课程视频、无字幕视频、内容敏感不想上云

**为什么推荐：** OpenAI 开源，完全本地运行，不上传内容，支持中文，准确率高。

**安装：**

```bash
pip install openai-whisper
```

**基本用法：**

```bash
# 转录本地视频
whisper video.mp4 --language Chinese --output_format txt --output_dir raw/videos/
```

**转录后处理：** 原始 Whisper 输出是纯文本，建议交给 Claude Code 做结构化，加标题和段落分隔，再存入 `raw/videos/`。

---

#### 快速在线方案 → VOMO AI

**适用场景：** 偶发需求，不想装本地工具，需要直接导出结构化 `.md` 文件

**特点：** 上传视频或粘贴 YouTube 链接，输出带标题和段落的结构化 markdown，而不是原始转录文本块，可以直接导入 Obsidian 或 GitHub。

**限制：** 免费版有时长限制，内容上传到云端，对敏感内容不适合。

**网址：** vomo.ai

---

#### 视频处理方案选择

| 场景 | 推荐工具 |
|------|----------|
| YouTube 视频，接入 Claude Code 工作流 | Firecrawl（MCP）|
| 本地视频，内容敏感，不想上云 | Whisper（本地）|
| 偶发需求，快速处理 | VOMO AI（在线）|
| YouTube 播放列表批量处理 | yt-video-text-md（Python）|

---

#### 视频 ingest 完整流程

```
视频来源
   │
   ├─ YouTube → Firecrawl（MCP）→ raw/videos/xxx.md
   │
   └─ 本地视频 → Whisper → raw/videos/xxx.txt
                              │
                         Claude Code 结构化
                              │
                         raw/videos/xxx.md
                              │
                    /ingest-source raw/videos/xxx.md
                              │
                    wiki/source-summaries/ 更新
                    wiki/concepts/ 更新
                    wiki/index.md 更新
                    wiki/log.md 更新
```

---

## 多设备使用

所有设备的同步都通过 git 完成，不依赖任何云同步服务。

```bash
# 开始工作前
git pull

# 结束工作后
git add .
git commit -m "YYYY-MM-DD: [简述变更]"
git push
```

Obsidian Git 插件可以自动完成以上操作，手动操作只在需要精确 commit 信息时使用。

**大文件处理：**
- `raw/videos/` 只存转录后的 markdown，不存视频原件
- `raw/assets/` 下的图片和大 PDF 建议加入 `.gitignore` 或使用 Git LFS

---

## 最小起步顺序

```
第 1 步（今天）
└─ Obsidian + Git 插件
   验证：换台电脑后 wiki 能自动同步

第 2 步（用一周后）
└─ Readwise Reader
   验证：有文章成功 ingest 进 wiki

第 3 步（按需）
└─ Whisper 或 Firecrawl
   有视频需要处理时再装
   验证：一个视频成功转成 markdown 并 ingest

第 4 步（按需）
└─ Zotero
   论文阅读量上来后再加
   验证：论文 metadata 自动进入 source-summary
```

---

## 一句话总结各工具的边界

| 工具 | 只做这一件事 |
|------|-------------|
| Zotero | 管论文原件和 metadata |
| Readwise | 清洗文章，产出带高亮的 markdown |
| Whisper | 本地视频转录，隐私安全 |
| Firecrawl | YouTube 视频转 markdown，接入 Claude Code |
| VOMO AI | 快速在线视频转结构化 markdown |
| Claude Code | 执行 ingest / harness / 编程 |
| Obsidian | 浏览和可视化 wiki |
| GitHub | 同步和自动化检查 |

**每个工具只做自己最擅长的那一件事，交接点通过 markdown 文件完成。**

---

*本文档版本：v1.1 — 2026-04-12*
