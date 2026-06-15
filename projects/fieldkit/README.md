# FieldKit

> Calibration Field/校准场 出图样式系统：共享 design kit（tokens + kit.css + sonar 主题 + 氛围层 baker）喂多个消费者。

- **仓库**：`D:\Claude\Tools\FieldKit`（当前无远程，HEAD aa93de0）
- **类型**：工具类（tool）— 按 template-tool SOP 脚手架（产品 fieldkit/ 包 + kit.css + examples + tests + 协作层 specs/plans/handoff/wiki/.claude/raw + SPEC-001 retroactive）
- **状态**：🟢 活跃（2026-06-15 派生）
- **核心**：共享 kit（design tokens + kit.css + sonar motif + bake_atmosphere.py 分辨率无关氛围层）；消费者①=HTML→PNG/PDF 生成器（flow + composition，dark Lacquer Instrument + light Paper Field 双调色板）SHIPPED v1；消费者②=AnthropicPPT templates/styled_diagram.py SHIPPED v2
- **来源**：借鉴 pbakaus/impeccable 的校准场图风
- **关联**：未来全局 skill `calibration-field`（待建）；ADR-027（派生）/ ADR-028（flowgen styled-figure carve-out）；与 AnthropicPPT 互补

## 里程碑

| 里程碑 | 内容 | 状态 |
|--------|------|------|
| M0 | 派生 + 共享 kit（tokens + kit.css + sonar motif）+ HTML→PNG/PDF 生成器 v1（flow + composition）| ✅ 2026-06-15 |
| M1 | 氛围层 baker（bake_atmosphere.py）+ AnthropicPPT styled_diagram v2 | ✅ 2026-06-15 |
| M2 | 注册全局 skill `calibration-field` | ⏳ |
