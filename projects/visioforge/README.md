# VisioForge

> 通用 Visio 出图工作区——为所有项目按需生产 `.vsdx` 图件的"图件工厂"

- **仓库**：`D:\Claude\DocProcess\VisioForge`
- **类别**：🔒 私人项目（DocProcess 系，禁止公开发布 / 禁止 promote 至 Hub 公开 wiki）
- **状态**：初始化完成，0 图件（待首张出图 spec）
- **派生时间**：2026-06-02
- **派生自**：`D:\Claude\ohmybrain-core\template-document\`
- **启动模式**：手动（文档/图件型）

## 项目目标

- **主交付物**：Visio `.vsdx` 图件（架构图 / 流程图 / 组成图 / 时序图 / 路线图 / 复刻图）+ 同名 PNG 自检截图
- **定位**：不绑定单一来源项目，为各项目集中出图；产出 `.vsdx` 按需复制/导出到目标项目
- **出图引擎**：复用全局 `~/.claude/skills/flowgen-*`（8 个 skill），本仓不复制引擎，只存需求 / 产物 / 经验
- **输入**：图设计稿（HTML/文字）→ `raw/designs/`；待复刻参考图（PNG）→ `raw/references/`
- **闭环**：01-spec（图类型 + skill 选型）→ 02-draft（生成 .vsdx）→ 03-validate（截图自检 + 终审）→ 04-archive

## 出图 skill 决策树（8 选 1）

| 图结构 | Skill |
|--------|-------|
| 流程/算法/调用链（Mermaid 文本 / .vsdx） | `flowgen` / `flowgen-vsdx` |
| 自上而下分层架构 | `flowgen-layered` |
| N 分系统 × M 模块纯嵌套 | `flowgen-composition` |
| 多参与者消息时序 | `flowgen-sequence` |
| 项目立项/课题论证三段式 | `flowgen-roadmap` |
| 四化五层体系挂图 | `flowgen-archposter` |
| 已有图片转可编辑 Visio | `flowgen-replica` |

> 自由硬件框图等 flowgen 无法表达的结构 → 例外：手写 HTML/SVG + Playwright 截图（需说明原因）。

## 关联

- 同目录其他子项目：`Pricing` / `UWAprojDoc` / `CooperativeDetection` / `PaperReview` / `DigitalTwinGuide` / `DigitalTwin1plusN`
- 下游消费方：任何需要 Visio 图件的项目（UWAcomm_usbl / UWAprojDoc / DigitalTwin* 等）
- 详见：`D:\Claude\DocProcess\CLAUDE.md`

## 注意

本项目走 DocProcess 私人项目惯例：

- 不推送公开远程仓库
- 不通过 `/promote` 回流 Ohmybrain Hub 公开 wiki
- 跨项目方法论结论走 `<private>` 标签或 Hub 的私人区域
