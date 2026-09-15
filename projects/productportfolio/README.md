# ProductPortfolio 🔒

> 公司产品体系梳理文档工作区——把海星100（环境数据）/ 海涛100（声学仿真）/ 小鲸100（海洋无人平台智控 · 声学 · 能源三核产品族）/ 海若10（开发运维底座）/ 大模型及智能应用平台统一到**一张体系架构图 + 一套产品谱系表 + 一致口径**。主交付物《公司产品体系梳理》docx。

- **仓库**：`D:\Claude\DocProcess\ProductPortfolio`
- **类型**：document（`template-document` 派生，2026-09-15，ADR-049）
- **状态**：🟡 待裁 D1~D6（SPEC-001 大纲已立，撰写未启动）
- **依赖**：[[../xiaojinglaunch/README|XiaojingLaunch]]（产品架构 deck V3 + 2026-09-08「三核独立 · 一体协同」口径决策 + 公司总体介绍 PPT，均为直接输入）；查询复用不构成依赖：[[../auvnetcoop/README|AUVNetCoop]] / [[../uwaprojdoc/README|UWAprojDoc]]（素样式 docx + Visio OLE 构建管线）
- **git**：本地 `main` `2a0a591`，无远程（🔒 私人，禁 push 公开仓）

## 当前焦点

派生当日（2026-09-15）：种子 4 份入 `raw/materials/`（产品架构 deck V3 202 MB / 修改意见 docx / 公司总体介绍 17 MB / 大模型平台介绍 424 MB，pptx 不入库）+ 口径基线抄录 `wiki/topics/product-system-baseline.md`（四产品线 + 小鲸三核固定口径表 + 沿革）+ `specs/active/2026-09-15-SPEC-001-product-portfolio-doc.md`（6 章 + 附 A 谱系总表 / 图件 F1~F3 / 验收点 / D1~D6）+ `plans/active/PLAN-001`（M0~M6）。待办：

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
