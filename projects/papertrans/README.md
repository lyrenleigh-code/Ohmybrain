# PaperTrans

> 外文论文英译中翻译工作区（英文学术论文 → 术语一致的中文译稿）

- **仓库**：`D:\Claude\DocProcess\PaperTrans`
- **类别**：🔒 私人项目（DocProcess 系，禁止公开发布 / 禁止 promote 至 Hub 公开 wiki）
- **状态**：脚手架就绪，待首篇论文
- **派生时间**：2026-06-15
- **派生自**：`D:\Claude\ohmybrain-core\template-document`
- **启动模式**：手动

## 项目目标

- **翻译对象**：外文学术论文（英文为主，水声 / 通信 / 信号处理等领域优先）
- **方向**：英 → 中（EN → ZH）
- **输入材料**：源论文 PDF / 文本（放 `raw/papers/`，只读）
- **期望产出**：术语统一、语体规范、公式与图表标号保形的中文译稿（`output/<slug>-zh.docx`）

## 工作约定

- **一篇论文 = 一份 spec = 一份译稿**：源文进 `raw/papers/`，spec 进 `specs/active/`，译稿进 `output/`
- **术语单一可信源**：`wiki/glossary.md`（中英对照），新术语初译时回写
- **风格规范**：`wiki/concepts/translation-conventions.md`（语体 / 保形 / 一致性 / 自查清单）
- **专家主导**：译法分歧停下问用户，不擅自定稿

## 关联

- 同目录兄弟：`PaperReview`（学位论文外审）、`papers`（论文写作）、`Pricing` / `UWAprojDoc` 等
- 详见 `D:\Claude\DocProcess\CLAUDE.md`

## 注意

DocProcess 私人项目惯例：不推送公开远程；不 `/promote` 回流 Hub 公开 wiki；跨项目结论走 `<private>` 标签或私人区域。
