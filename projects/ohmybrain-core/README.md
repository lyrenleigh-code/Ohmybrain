# ohmybrain-core

> 母仓 / 三模板 / 通用 harness — 所有项目按类型从此派生

- **仓库**：github.com/lyrenleigh-code/ohmybrain-core（GitLab 内网镜像 http://192.168.10.100:8880/lilin/ohmybrain-core）
- **本地**：`D:\Claude\ohmybrain-core`
- **角色**：core 层（template + harness 复用）

## 三仓架构定位

```
ohmybrain-core（本项目 / 三模板）
  ├── template-engineering/ ──派生──► TechReq/*（算法 / 仿真 / 硬件设计）
  ├── template-document/    ──派生──► DocProcess/*（文档 / 方案 / 报告）
  └── template-tool/        ──派生──► Tools/*（工具 / skill / template）

ohmybrain（Hub）  ← 跨项目知识沉淀
project（具体项目）  ← 工程闭环 / 算法实现
```

## 模板内容

| 目录 | 内容 |
|------|------|
| `template-*/.claude/rules/` | 路径规则（wiki / raw / engineering / specs 等） |
| `template-*/.claude/skills/` | 通用技能（ingest / plan / implement / lint / promote） |
| `template-*/.claude/commands/` | Slash commands（`/ingest`, `/promote`） |
| `template-*/.claude/settings.json` | 跨平台 hooks（Pre / Post / Stop） |
| `template-*/.obsidian/` | Obsidian vault 配置 + wiki 模板 |
| `template-*/raw/` · `wiki/` · `specs/active/` · `plans/active/` · `handoff/active/` | 项目协作骨架 |
| `template-*/scripts/` | 自动化脚本 |
| `template-*/.github/workflows/` | CI + wiki-check |
| `template-*/prompts/` | 自主新建项目闭环驱动套件 |

## 派生项目状态（2026-04-26）

| 项目 | 派生时间 | 路径 | 状态 |
|------|----------|------|------|
| UWAcomm | 早期 | `D:\Claude\TechReq\UWAcomm` | 🟢 活跃（14 模块 / 6 体制 / 365 文件） |
| USBL | 早期 | `D:\Claude\TechReq\USBL` | 🟢 活跃（19 模块 4 线，CAGE5 立体阵） |
| UWAnet | 早期 | `D:\Claude\TechReq\UWAnet` | 🟡 调研（M1 dry-run 通过） |
| UWAcomm_usbl 🔒 | 2026-04-25 | `D:\Claude\TechReq\UWAcomm_usbl` | 🟢 SPEC-001 批 0+1 完成 |
| FlowGen 🔒 | 2026-04-23 | `D:\Claude\Tools\FlowGen` | 🟡 SOP 派生未实装 |
| Pricing 🔒 | 早期 | `D:\Claude\DocProcess\Pricing` | 🟢 私人 |

🔒 = 内网 / 私人，不公开。

## 新项目派生

完整 SOP：`D:\Claude\ohmybrain-core\docs\new-project-sop.md`

```
1. 在 Hub 的 projects/<slug>/ 下建占位
2. 按项目类型拷贝 `template-engineering/`、`template-document/` 或 `template-tool/` 到目标路径
3. 填 CLAUDE.md（slug / 路径 / 关联项目 / 启动模式）
4. （可选）填 prompts/goal.yaml 启用自主闭环
5. git init + 双远端（GitHub + GitLab）
6. 第一次 commit + push 双推
```

## 经验回流

```
项目实战 → 发现可复用模式 → Hub 评估 → 写到 ohmybrain-core/template-*/
       └→ 跨项目知识     → 写到 ohmybrain/wiki/
```

新建项目派生时自动获得最新模板。

## 相关

- 母仓 README：`D:\Claude\ohmybrain-core\README.md`
- Hub wiki：[[system-overview]]（三仓架构权威页）
- 自主新建项目方法论：[[autonomous-new-project-workflow]]
