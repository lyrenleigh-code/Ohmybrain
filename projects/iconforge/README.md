# IconForge

> 自然语言 → 图标（SVG）生成工具：用一句话描述，由 Claude 直出矢量图标，可选导出 PNG/ICO 多尺寸。

- **仓库**：`D:\Claude\Tools\IconForge`
- **类型**：工具类（tool）— 主交付物 = 可复用 skill + 模板套件
- **状态**：🌱 已派生，待 spec（2026-05-29）
- **核心路线**：LLM 本会话即引擎生成 SVG（与 `flowgen-vsdx` skill 同构，零外部 API）
- **依赖**：无（独立工具）

## 里程碑

| 里程碑 | 内容 | 状态 |
|--------|------|------|
| M0 | 从 ohmybrain-core/template-tool 派生 + 注册 Hub | ✅ 2026-05-29 |
| M1 | spec：SVG 图标规格（风格枚举 / 画板 / 命名 / 输出形态）+ 首个 demo 图标 | ⏳ |
| M2 | 导出管线：SVG → PNG/ICO 多尺寸（cairosvg / rsvg） | ⏳ |
| M3 | 注册全局 skill `iconforge`（关键词触发：图标 / icon / SVG 图标） | ⏳ |
