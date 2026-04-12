---
type: architecture
created: 2026-04-12
updated: 2026-04-12
tags: [架构, 闭环, harness]
---

# 系统架构总览

## 定位

Ohmybrain 是一个 **LLM Wiki + 开发工程 + Claude Code Harness** 一体化仓库，同时承载知识管理和工程交付两个职能。

## 完整目录结构

```
ohmybrain/
├── .claude/                        # Harness 层
│   ├── settings.json               #   hooks 配置
│   ├── rules/                      #   路径特定规则
│   │   ├── wiki.md                 #     wiki 编写规范
│   │   ├── raw.md                  #     raw 只读规则
│   │   ├── engineering.md          #     代码工程规范
│   │   └── specs.md                #     任务管理规范
│   ├── skills/                     #   可复用工作流
│   │   ├── ingest-source/          #     资料摄入
│   │   ├── plan-task/              #     任务规划
│   │   ├── implement-task/         #     任务实现
│   │   ├── lint-wiki/              #     Wiki 检查
│   │   └── promote-answer/         #     结论沉淀
│   ├── hooks/                      #   行为强制执行
│   │   ├── protect-raw.sh          #     拦截 raw/ 修改
│   │   ├── wiki-post-edit.sh       #     编辑后 lint
│   │   └── check-stop.sh           #     停止前验证
│   └── commands/                   #   slash commands (旧版保留)
│
├── raw/                            # 原始事实层 (只读)
│   ├── papers/                     #   学术论文
│   ├── articles/                   #   网页文章
│   ├── videos/                     #   视频转录
│   ├── podcasts/                   #   播客转录
│   ├── books/                      #   书籍笔记
│   ├── courses/                    #   课程讲义
│   ├── notes/                      #   对话/会议/思考
│   ├── threads/                    #   社交媒体帖子
│   ├── repos/                      #   代码仓库
│   └── assets/                     #   图片/附件
│
├── wiki/                           # 可复用知识层
│   ├── index.md                    #   内容索引
│   ├── log.md                      #   变更日志
│   ├── concepts/                   #   概念和方法
│   ├── entities/                   #   人物/工具/项目/组织
│   ├── architecture/               #   系统架构 (本文件所在)
│   ├── modules/                    #   模块设计和接口
│   ├── decisions/                  #   设计决策记录
│   ├── incidents/                  #   故障和教训
│   ├── topics/                     #   跨概念综合专题
│   ├── comparisons/                #   A vs B 对比分析
│   ├── explorations/               #   深度研究笔记
│   └── source-summaries/           #   原始资料摘要
│
├── specs/                          # 需求入口层
│   ├── active/                     #   当前任务 spec
│   └── archive/                    #   已完成 spec
│
├── plans/                          # 实现计划层
├── tasks/                          # 任务追踪
├── src/                            # 源代码
├── tests/                          # 自动化测试
├── evals/                          # Agent/工作流评测
│
├── workflows/                      # 操作流程文档
│   ├── knowledge/                  #   知识闭环
│   │   ├── 01-ingest.md            #     1. 资料摄入
│   │   ├── 02-query.md             #     2. 知识查询
│   │   ├── 03-promote.md           #     3. 结论沉淀
│   │   └── 04-review.md            #     4. 定期审查
│   └── engineering/                #   开发闭环
│       ├── 01-spec.md              #     1. 需求定义
│       ├── 02-plan.md              #     2. 实现计划
│       ├── 03-implement.md         #     3. 代码实现
│       └── 04-validate.md          #     4. 完成验证
│
├── scripts/                        # 自动化脚本
│   ├── lint_wiki.py                #   Wiki 结构检查
│   ├── sync_index.py               #   同步 index 计数
│   ├── validate_task.py            #   任务完成验证
│   ├── transcribe.py               #   Whisper 音视频转录
│   ├── scrape.py                   #   Firecrawl 网页抓取
│   ├── import-zotero.py            #   Zotero 论文导入
│   ├── import-readwise.py          #   Readwise 文章导入
│   └── zotero_cleanup.py           #   Zotero 重复清理
│
├── .github/workflows/              # CI/CD
│   ├── wiki-check.yml              #   Wiki lint + validate
│   └── ci.yml                      #   测试 + 验证
│
├── .obsidian/                      # Obsidian vault 配置
���   └── templates/                  #   页面模板
│
├── CLAUDE.md                       # 项目级 Claude Code 入口
└── .gitignore
```

## 六层架构

| 层 | 目录 | 职责 | 读写 |
|----|------|------|------|
| **Harness** | `.claude/` | 规则、技能、钩子——让 Claude 按规矩办事 | Claude 读，用户写 |
| **原始事实** | `raw/` | 论文、文章、视频转录、代码仓库 | 只读 |
| **可复用知识** | `wiki/` | 概念、实体、架构、决策、摘要 | 读写 |
| **任务上下文** | `specs/` `plans/` | 需求 spec 和实现计划 | 读写 |
| **交付物** | `src/` `tests/` `evals/` | 源代码、测试、评测 | 读写 |
| **自动化** | `scripts/` `workflows/` `.github/` | 脚本、流程、CI | 读写 |

## 两个闭环

### 知识闭环

```
raw/  -->  ingest  -->  wiki/  -->  query  -->  promote  -->  wiki/
 |                       ^                                    |
 +-----------------------+------------------------------------+
```

| 阶段 | 操作 | 输入 | 输出 |
|------|------|------|------|
| **收集** | 资料放入 `raw/` 对应子目录 | URL / 文件 / 文本 | `raw/{type}/` 文件 |
| **摄入** | `/ingest-source` | `raw/` 文件 | source-summary + 概念/实体页更新 |
| **查询** | 用户提问 | 问题 | 基于 wiki 的回答 |
| **沉淀** | `/promote-answer` | 高价值结论 | wiki 页面更新 |
| **审查** | 定期 review | wiki 全局 | 修复缺口、标记过时 |

详细流程见 `workflows/knowledge/` 下的 4 个文件。

### 开发闭环

```
spec  -->  plan  -->  implement  -->  test  -->  validate  -->  archive
  |                      |                          |
  |                      +----> wiki/ 同步 <--------+
  |
specs/active/  ---------------------------------------->  specs/archive/
```

| 阶段 | 操作 | 输入 | 输出 |
|------|------|------|------|
| **需求** | 在 `specs/active/` 建 spec | 用户需求 | spec 文件 |
| **计划** | `/plan-task` | spec | `plans/` 下的实现计划 |
| **实现** | `/implement-task` | spec + plan | `src/` 代码变更 |
| **测试** | 运行测试 | 代码 | `tests/` 测试通过 |
| **验证** | 自动检查 | 全局 | lint + validate 通过 |
| **归档** | spec 移入 archive | -- | `specs/archive/` |

实现过程中架构、行为或接口发生变化时，必须同步更新 wiki：
- `wiki/architecture/` -- 架构变更
- `wiki/modules/` -- 模块接口变更
- `wiki/decisions/` -- 重要设计决策
- `wiki/incidents/` -- 故障和教训

详细流程见 `workflows/engineering/` 下的 4 个文件。

### 两个闭环的交汇点

**wiki/ 是交汇点**——知识闭环往 wiki 写入知识，开发闭环从 wiki 读取上下文并在变更后写回 wiki。

```
         知识闭环
            |
     raw -> wiki -> query
            |
            v  <-- 交汇点
            |
     spec -> wiki -> implement
            |
         开发闭环
```

## Harness 机制

Claude Code 通过 `.claude/` 下的三层机制确保行为一致：

| 层 | 位置 | 作用 | 执行时机 |
|----|------|------|---------|
| **Rules** | `.claude/rules/*.md` | 路径特定规范 | 读取对应路径时自动加载 |
| **Skills** | `.claude/skills/*/SKILL.md` | 可复用工作流 | 用户调��时 |
| **Hooks** | `.claude/hooks/*.sh` | 强制执行 | PreToolUse / PostToolUse / Stop |

### 当前 Skills

| 技能 | 对应闭环 | 用途 |
|------|---------|------|
| `/ingest-source` | 知识 | 原始资料 -> wiki 知识 |
| `/lint-wiki` | 知识 | Wiki 结构检查和修复 |
| `/promote-answer` | 知识 | 对话结论 -> wiki 沉淀 |
| `/plan-task` | 开发 | spec -> 实现计划 |
| `/implement-task` | 开发 | spec + plan -> 代码交付 |

### Hooks 触发流程

```
用户请求 -> Claude 调用工具
                |
         PreToolUse hook
         protect-raw.sh     <-- 拦截 raw/ 修改
                |
           工具执行
                |
         PostToolUse hook
         wiki-post-edit.sh  <-- lint 检查
                |
         Claude 完成任务
                |
           Stop hook
         check-stop.sh      <-- 验证任务完成
```

## 工具链

```
原始资料来源              收集工具               沉淀
--------------           --------------         --------------
论文              ->     [[zotero]]          ->  raw/papers/
网页文章          ->     [[readwise-reader]]  ->  raw/articles/
YouTube 视频      ->     [[firecrawl]]        ->  raw/videos/
本地视频          ->     [[whisper]]          ->  raw/videos/
代码仓库          ->     [[github]]           ->  raw/repos/
                              |
                              v
                        [[claude-code]]
                       (ingest / harness)
                              |
                              v
                           wiki/
                              |
                    +---------+---------+
               [[obsidian]]         [[github]]
              (可视化浏览)         (同步 / CI)
```

## 当前项目状态

| 指标 | 数值 |
|------|------|
| Wiki 页面数 | 25 |
| 概念页 | 10（覆盖全部研究方向） |
| 实体页 | 8（7 个工具 + 1 个项目） |
| Zotero 论文数 | 3,179（清理后） |
| 工作流文档 | 8（知识 4 + 开发 4） |
| Skills | 5 |
| Rules | 4 |
| 自动化脚本 | 8 |

## 演进历史

| 日期 | 里程碑 |
|------|--------|
| 2026-04-12 | 初始搭建：仓库结构、CLAUDE.md、wiki 骨架 |
| 2026-04-12 | 加入约束：hooks、lint 脚本、slash commands |
| 2026-04-12 | 打通工具链：Obsidian、Whisper、Firecrawl、Zotero |
| 2026-04-12 | Zotero 清理：移除 1634 重复条目，生成研究地图（10 方向） |
| 2026-04-12 | Ingest UWAcomm 水声通信仿真平台 |
| 2026-04-12 | 工程升级：开发闭环、rules/skills/hooks、CI |

## 相关页面

- [[research-map]] -- 研究方向全景地图
- [[toolchain]] -- 工具链详细指南
- [[my-brain-setup-plan]] -- 初始搭建计划（历史参考）
- [[uwacomm]] -- UWAcomm 水声通信仿真平台
