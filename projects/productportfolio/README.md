# ProductPortfolio 🔒

> 公司产品体系梳理文档工作区——把海星100（环境数据）/ 海涛100（声学仿真）/ 小鲸100（海洋无人平台智控 · 声学 · 能源三核产品族）/ 海若10（开发运维底座）/ 大模型及智能应用平台统一到**一张体系架构图 + 一套产品谱系表 + 一致口径**。主交付物《公司产品体系梳理》docx。

- **仓库**：`D:\Claude\DocProcess\ProductPortfolio`
- **类型**：document（`template-document` 派生，2026-09-15，ADR-049）
- **状态**：🟢 收尾修订版待用户终审（2026-09-16：Codex 两轮审阅清单 A~D + R1~R6 全部实施；三版并存：原 20 页 / 审阅修订版 / 收尾修订版，Codex 16 页版另存）
- **依赖**：[[../xiaojinglaunch/README|XiaojingLaunch]]（产品架构 deck V3 + 2026-09-08「三核独立 · 一体协同」口径决策 + 公司总体介绍 PPT，均为直接输入）；查询复用不构成依赖：[[../auvnetcoop/README|AUVNetCoop]] / [[../uwaprojdoc/README|UWAprojDoc]]（素样式 docx + Visio OLE 构建管线）
- **git**：本地 `main` `a4696f9`（12 commit），无远程（🔒 私人，禁 push 公开仓）

## 当前焦点

**2026-09-16**：完整版两版并存（Codex 16 页 .mjs 生成 / Claude 20 页 v15.3 原模板）→ Codex 审阅清单 A~D（P11 换「某水声通信原理验证」案例 + V3 P14 原图、P9 原生表格、P13 二期设计示意、P7/P17 闭环返回线、P15「准快全通评」、P19 删未确认联系方式）→ 第二轮 R1~R6（P11 越边与题签、P12 接口职责、P17 考核（新增科目※）、P7/P19 短句）→ **`output/海涛100_产品发布会_完整版_claude_收尾修订版.pptx`** 待用户终审；as-built 文案 v3；待用户给：海涛线联系人 / 二期截图 / 封面措辞。

**2026-09-15 同日续（派生后 9 轮）**：raw/slides 用户新放 5 份（09-14 简化版 = 现行主口径源 / 谱系单页 v3 / 小鲸发布会 v15.3 = 老板认可骨架 / 海星新稿 ×2）抽文字 → F-1 海涛定位讨论 → **decision-001**（主线 A 论证研制 / 海涛出引擎、小鲸仿真试验 = 海涛引擎 + 小鲸接口 / 删「声学载荷支撑」/ 训练参照 AcousticLiteracy sxsy 二期、删红蓝对抗 / sxsy 作海涛应用实例 / 定位「一套引擎 · 三级仿真 · 两条闭环」+ 价值「效果先算清 · 方案再选定 · 训练有数据」）→ F-2 → **decision-002**（小鲸两级口径：族级三核 + 智控级 v15.3 原样，能力开发留智控）→ 用户收窄「只做海涛，小鲸版式 PPT」→ SPEC-002（6 页：需求 / 定位 / 特性×3 / 应用与交付）+ PLAN-002 + **M1 文案 v1**（`specs/active/haitao-copy-v1.md`）待审。海星边界 Q5 暂缓。

**派生当日原计划（已挂起）**：派生当日（2026-09-15）：种子 4 份入 `raw/materials/`（产品架构 deck V3 202 MB / 修改意见 docx / 公司总体介绍 17 MB / 大模型平台介绍 424 MB，pptx 不入库）+ 口径基线抄录 `wiki/topics/product-system-baseline.md`（四产品线 + 小鲸三核固定口径表 + 沿革）+ `specs/active/2026-09-15-SPEC-001-product-portfolio-doc.md`（6 章 + 附 A 谱系总表 / 图件 F1~F3 / 验收点 / D1~D6）+ `plans/active/PLAN-001`（M0~M6）。待办：

1. 用户裁 D1~D6（受众 / 产品线范围含大模型平台与在研 / 口径基准 / 成熟度分级 / 图件形态 / PPT 汇报版）
2. M0 `/ingest` 4 种子（大 pptx 先 python-pptx 抽文字到 .tmp/）→ 修订基线页
3. M2 谱系总表先行 → M3 章节 draft（2→3→1→4→5→6）→ M4 图件 → M5 build docx

## 硬规则

- 口径以 XiaojingLaunch **2026-09-08 三核决策**为准，deck V3 冲突处以决策为准；V1/V2 仅作沿革
- 引用不改源：XiaojingLaunch 只读；本项目结论回流由用户手动裁决
- 图件素样式 flowgen；docx 管线复制入本项目 scripts/，不跨项目 import

## 相关

- Hub 登记：ADR-049（[[../../wiki/architecture/decision-log]]）· [[../../wiki/topics/ecosystem-dashboard]]
- auto-memory：`project_productportfolio_init`
