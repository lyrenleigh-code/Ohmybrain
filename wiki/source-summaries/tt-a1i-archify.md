---
type: source-summary
created: 2026-08-29
updated: 2026-08-29
tags: [Claude-Code, Skill, 架构图, JSON-IR, 校验门禁, 跨引擎, 出图]
source_type: repo
---

# tt-a1i/archify — JSON IR + 校验门禁的出图 skill

- **来源**：<https://github.com/tt-a1i/archify>（MIT，2026-04-15 创建，本次核验 @2026-08-29 时 27,569 star / 1,747 fork，v2.16，506 文件）
- **日期**：2026-08-29 ingest（README_ZH + `SKILL.md` + `references/delivery-contract.md` + `schemas/` + `renderers/shared/diagnostics.mjs` 细读 + **本机装入实测**）
- **一句话**：把「自然语言/Mermaid → 图」重做成 **typed JSON IR → schema 校验 → 确定性渲染 → 原子交付**的工序，产出自包含可交互 HTML（5 图型 × 4 视觉预设）。
- **本工作区状态**：**已装** `~/.claude/skills/archify`（6.8 MB，从 main tarball 抽 `archify/` 子目录，未用 `npx skills add` 以免引入第三方 CLI）；同日**取代退役** [[cocoon-ai-architecture-diagram]]。

## 血统：Hub 悬案的答案

`SKILL.md` frontmatter 自证 `based_on: Cocoon-AI/architecture-diagram-generator (MIT, v1.0)`——即 Hub 2026-04-17 摄入的 [[cocoon-ai-architecture-diagram]]。那页当时把 cocoon 记为「**极简反例**：单图型单风格时不必三层分离」，并留下判据「**≥2 个正交维度（风格 × 类型）才值得分层**」待验。

archify = 同一血统 4 个月后的续作，维度长到 **5 图型 × 4 预设**，结构随之分裂为 `SKILL.md` + `references/` + `schemas/` + `renderers/` 四层。**同作者血统、同功能域的前后对照**比跨项目对照更强——判据成立，已一行 promote 至 [[../concepts/skill-layered-resources]]。

## 值得移植的四个机制

| 机制 | 做法 | 对上本工作区什么 |
|---|---|---|
| **schema-first IR + 结构化诊断** | JSON Schema（`ajv` 预编译成 `generated-validators.mjs`）+ 诊断对象 `{code, severity, subject, evidence, supportedFixes}` | flowgen 家族现为「Claude 手改 Python 模板 → pywin32 渲染」，**渲染失败无机器可读回执**，agent 只能瞎试——最大可移植项 |
| **原子交付 + 双 SHA-256 收据** | `deliver` 冻结 spec 字节 → 渲染私有快照 → 全门禁过才原子替换目标 → 回执含 spec/artifact 各自 sha256 与字节数 | 直接对上红线 `feedback_never_overwrite_user_edits`：**产物 hash 与上次收据不符即可判定被外部改动**，比 mtime 目检可靠 |
| **视觉检查只给证据** | `visual-check` 量四视口容纳性 + 明暗截图，回执**恒报 `visualReview: "pending"`**；契约明写「自动化证据不能宣称感知审查」 | 与 `feedback_uwacomm_testing_boundary`「不代下结论」同构，可移植到 flowgen/FieldKit 出图收尾 |
| **修复终止准则** | 「最多 2 轮聚焦修复；两轮不改善即停止并如实报告未解诊断」写进 SKILL.md | 防 agent 在渲染失败上无限打转 |

另有 `repository-evidence`：节点可挂 git 校验过的文件+行号（`SRC n`），拒绝绝对路径/`..`/`.git` 逃逸——对 UWAcomm/USBL 做「带出处的代码地图」有用，也呼应 Hub 一行 promote 的「结论+来源+日期」纪律。

**SKILL.md 自身的读取预算纪律**也值得抄：明写「产出首个候选前**不得**读 `geometry.mjs`/渲染器/校验器/测试」「仅在诊断指向内部或两次修复失败后才看实现」——对 8 个 flowgen SKILL.md 的瘦身是现成范本（[[../concepts/skill-layered-resources]]）。

## 本机实测（2026-08-29）

`doctor` 15 项全绿（Node v24 + Chrome 就位，渲染零运行时依赖）。中文实例（UWAcomm 收发链路 10 节点 9 连线）：`validate --quality showcase` **9/9、0 error 0 warning**（交叉 0 / 走廊歧义 0 / 标签净距 91.6 px）→ `deliver` 原子交付 695 KB → `visual-check` 1440×900 / 1600×1000 / 1920×1080 / 2048×1320 **四视口零溢出** + 明暗 4 截图。**中文渲染正常**，`meta.locale: "zh-CN"` 使 Viewer UI 全本地化。留白偏多系作者坐标问题，非工具缺陷——机检只管容纳性不管疏密，正合「不代下结论」口径。

## 定位边界（与既有出图族不重叠）

- **flowgen-\*** 8 skill → 可编辑 `.vsdx`（进 docx / 汇报，Visio COM）：**不可替代**。
- **calibration-field / FieldKit** → 风格化位图 + PPT 幻灯片（氛围层）。
- **archify** → 可交互 HTML（网页/演示交付），产物不可编辑；进 docx 需导 PNG/SVG。

## 跨引擎意义

archify 同时声明支持 Claude Code / Cursor / Codex CLI / OpenCode，是 **agentskills.io 开放标准可跨引擎复用的活证据**——见 [[openai-codex-harness]]。

## 相关页面

- [[cocoon-ai-architecture-diagram]] — 上游 v1.0（已退役，本页为其继任）
- [[openai-codex-harness]] — 跨引擎 skill 标准的另一半
- [[../concepts/skill-layered-resources]] — 分层判据（本页提供实证）
- [[../concepts/vsdx-reverse-engineering-workflow]] — flowgen 侧的对照工序
- [[../entities/claude-code]]
