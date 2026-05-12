---
type: source-summary
created: 2026-04-23
updated: 2026-04-23
tags: [mermaid, 图表, flowchart, JavaScript, diagram-dsl, 可视化]
source_type: repo
---

# mermaid-js/mermaid — 文本到图表的 JS 渲染器

## 定位

**Mermaid** 是 Knut Sveidqvist 自 2014 年起维护的 JavaScript 图表生成库,通过 Markdown 风格的文本 DSL 声明 → 前端渲染 SVG,已成为 **"diagram-as-code"** 事实标准(GitHub、GitLab、Obsidian、VS Code 原生支持)。

- **仓库**: https://github.com/mermaid-js/mermaid
- **许可**: MIT(Copyright 2014-2022 Knut Sveidqvist)
- **包版本**: monorepo 根 `mermaid-monorepo@10.2.4`; 核心包 `mermaid@11.14.0`
- **近期动态**: 最新提交为 mindmap tidy-tree root edges 修复(PR #7639);本地 clone 为浅克隆(commits=1,无 tag)
- **规模**: 单体 monorepo(pnpm workspace) × 8 个 package × **27 种内置图表类型**

## 核心观点(6 条)

1. **DSL > GUI**:"图随代码"(doc-rot Catch-22 的解法)—— 文档和代码一起 diff、review、版本控制
2. **分层架构**:`Parser(Langium/Jison) → AST → Diagram-API(detectType/loadDiagram)→ rendering-util + 主题 → SVG`,每种图类型都是一个 plug-in
3. **统一配置协议**: `frontmatter.ts` + `defaultConfig.ts` + JSON schema 生成 TS 类型(`create-types-from-json-schema.mts`)—— 配置即代码
4. **可插拔布局引擎**: 独立子包 `mermaid-layout-elk`(ELK)、`mermaid-layout-tidy-tree`(D3 tree)、`mermaid-zenuml`(序列图 ZenUML 后端)
5. **安全 DSL**: 支持 sandbox iframe 渲染级别,对抗嵌入式 XSS(因图表语法 ≈ HTML 特殊字符,标准 sanitize 会破图)
6. **视觉回归优先**: Argos + Applitools 为每个 PR 跑截图对比,渲染器开发的关键基建

## 架构模块(简图)

```
packages/
├── mermaid/               核心渲染器(11.14.0)
│   └── src/
│       ├── diagrams/      27 种图 × 每个一目录(flowchart/sequence/gantt/c4/mindmap/er/state/...)
│       ├── diagram-api/   detectType / loadDiagram / frontmatter / comments
│       ├── rendering-util/ dagre-wrapper / viewbox 设置
│       ├── themes/        base / dark / forest / neutral
│       └── schemas/       JSON schema → TS 类型
├── parser/                Langium-based 新解析器(sequenceDiagram 等迁移中)
├── mermaid-layout-elk/    ELK 布局
├── mermaid-layout-tidy-tree/ tidy-tree 布局
├── mermaid-zenuml/        ZenUML 序列图集成
├── mermaid-example-diagram/ 第三方图类型样板
└── tiny/                  精简发行版
```

## 支持的图表类型(27)

flowchart / sequence / class / state / gantt / pie / gitGraph / userJourney / c4 / er / mindmap / timeline / quadrant-chart / sankey / xychart / packet / requirement / architecture / block / kanban / radar / treemap / treeView / venn / wardley / ishikawa / eventmodeling — 覆盖**流程、时序、数据、战略、UX** 五大类,已超出早期"流程图工具"定位。

## 对 FlowGen 项目的启发(8 条)

1. **DSL 设计优先 LLM 友好**:Mermaid 语法故意**像 markdown**(`-->`、`[...]`、`A --> B`),LLM zero-shot 生成准确率高 —— FlowGen 若要做"LLM 生成流程图",直接复用 Mermaid DSL 比自造 JSON 更省 prompt token、更易 round-trip
2. **图类型插件化**:每个图独立目录 + 注册到 `diagram-orchestration.ts`—— FlowGen 支持多图类型时可参考同构
3. **Langium 替代 Jison**:`packages/parser` 新一代基于 Langium(TypeScript-first、IDE/LSP 友好)—— FlowGen 若要做语法扩展或 IDE 补全,Langium 是当前业界首选
4. **frontmatter + JSON schema 驱动配置**:用户侧写 YAML,内部用 JSON schema 校验 + 生成 TS 类型,FlowGen 处理"用户自定义配置"可照搬
5. **ELK / tidy-tree 布局解耦**:布局算法做外置包,核心只管渲染 —— FlowGen 输出到不同引擎(d3、reactflow、graphviz)时值得借鉴
6. **视觉回归 > 单元测试**:渲染器的正确性难以断言,Argos(Cypress + S3 截图对比)是核心验证方式 —— FlowGen 若要做生产级渲染,应尽早接入
7. **Safe DSL 与沙箱渲染**:用户输入 + 浏览器渲染必上 CSP/sandbox iframe,mermaid 的 `securityLevel` 分档模式可复用
8. **monorepo + changesets**:pnpm workspace + `@changesets/cli` 管理 8 个联动 package 的版本 —— FlowGen 若扩展到多子包同理

## 与 Ohmybrain 的连接点

- **Hub 已直接使用**: `wiki/architecture/memory-graph.md` 就是纯 Mermaid `flowchart LR` 渲染的 MCP 知识图谱快照(23 实体 + 34 关系),通过 [[obsidian]] 预览
- **执行引擎渲染**: [[claude-code]] 在对话中输出的流程/时序图、本 Hub 里的跨项目架构图(`system-overview.md`),终态都是 Mermaid 源文
- **潜在 concept 空缺**: Hub 目前无 `diagram-as-code` / `diagram-dsl-family` concept 页,Mermaid 是这一领域最成熟的样板;若 FlowGen 后续深化,值得建立该 concept 并把 Mermaid 作为首条

## 提案(未执行,等主会话决策)

- **建 concept `diagram-as-code`**(或 `diagram-dsl-family`)—— 归纳 Mermaid / PlantUML / D2 / Structurizr / Graphviz 这一族工具的通性(DSL、版本控制友好、渲染器分离),再挂本 source-summary + 未来 PlantUML/D2 摄入
- **建 concept `visual-regression-testing`** —— 提炼 Argos / Applitools / Percy 这类"截图 diff"模式,记录何时该用、替代 jest snapshot 的边界(mermaid 是典型案例)
- **本 source 有可能派生一篇 concept `diagram-orchestration-pattern`** —— 提炼 Mermaid "detectType + loadDiagram + 插件注册" 这套**通用图类型调度器模式**,可迁移到 FlowGen

## 备注

- 本次摄入为**浅克隆**(`git log` 仅 1 条 commit、无 tag),版本号采自 `package.json`(`11.14.0`)
- 只读:`README.md` 前 200 + 50 行、`LICENSE`、`package.json`、`packages/` 目录树、`packages/parser/README.md` 前 50 行、`packages/mermaid/src/diagrams/` 目录列表
- **未读**:`cypress/`、`demos/`、`docs/` 正文、`scripts/`、`themes/` 具体样式 —— 遵守阅读预算
