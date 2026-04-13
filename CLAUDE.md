# CLAUDE.md — Ohmybrain 知识库 + Hub

## 定位

Ohmybrain 是**个人知识库**和**项目导航中心**，不承载具体项目的代码和工程闭环。

## 三仓架构

```
ohmybrain-core（母仓/模板）
  ├→ 派生 → UWAcomm（自包含项目，H:\UWAcomm）
  └→ 派生 → 未来其他项目...

ohmybrain（本仓库 = 知识库 + Hub）
  ├── raw/          个人知识原料（只读）
  ├── wiki/         跨项目知识沉淀
  └── projects/     项目导航总览
```

## 不可违反的规则

- 不得修改 `raw/` 下的文件，除非用户明确要求
- 优先更新 `wiki/` 而非在对话中重复分析
- 知识变更必须同步更新 `wiki/index.md` 和 `wiki/log.md`
- 所有 wiki 内容用中文撰写

## 目录地图

| 目录 | 职责 |
|------|------|
| `raw/` | 只读原始资料（论文、文章、视频转录、代码仓库参考等） |
| `wiki/` | 跨项目知识层（概念、实体、架构、研究地图、摘要、探索） |
| `projects/` | 项目导航（链接到各项目仓库，状态总览） |
| `scripts/` | 知识库自动化脚本（lint/sync/导入/转录/抓取） |

## 项目仓库映射

| 项目 | 仓库地址 | 本地路径 |
|------|---------|---------|
| UWAcomm | github.com/lyrenleigh-code/UWAcomm | `D:\Claude\TechReq\UWAcomm` |
| UWAnet | github.com/lyrenleigh-code/UWAnet | `D:\Claude\TechReq\UWAnet` |
| USBL | github.com/lyrenleigh-code/USBL | `D:\Claude\TechReq\USBL` |
| ohmybrain-core | github.com/lyrenleigh-code/ohmybrain-core | `D:\Claude\ohmybrain-core` |

## 知识闭环

```
raw/ → ingest → wiki/ → query → promote → wiki/
```

具体项目的实验结论通过 promote 沉淀到本仓库的 wiki。

## 常用命令

| 命令 | 用途 |
|------|------|
| `python scripts/lint_wiki.py` | Wiki 结构检查 |
| `python scripts/sync_index.py` | 同步 index 页面计数 |
| `python scripts/transcribe.py <文件>` | Whisper 音视频转录 |
| `python scripts/scrape.py <URL>` | Firecrawl 网页抓取 |
| `python scripts/import-zotero.py` | Zotero 论文导入 |
