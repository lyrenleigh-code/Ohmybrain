# SonarSim

> 主动声呐界面仿真：active sonar 操作显控台 / 探测链路的 MATLAB App Designer 仿真

- **仓库**：`D:\Claude\TechReq\SonarSim`
- **类别**：🔒 私人项目（TechReq 工程系，禁止推送公开 GitHub/Gitee / 禁止 promote 至 Hub 公开 wiki）
- **状态**：初始化完成（ohmybrain-core 派生 + Hub 注册 + git init main），待首个 spec
- **派生时间**：2026-06-03
- **派生自**：`D:\Claude\ohmybrain-core\template-engineering\`
- **依赖**：无（全新独立项目）

## 项目定位

主动声呐的**界面（显控台）仿真**：把发射波形 → 水声传播·目标回波·混响·噪声 → 接收处理（波束形成 + 匹配滤波 + 检测）→ 操作员显控界面（A 显 / PPI / 瀑布等）整链路做成可参数化、可交互的 MATLAB 仿真。

- **交付物**：MATLAB App Designer 应用（`.mlapp` 视图 + 算法 `.m` 模型层）
- **架构原则**：model/view 解耦——算法层 headless 可单测，界面层只做可视化与交互
- **启动模式**：手动（探索性研究：spec → plan → 讨论 → code，每 checkpoint 停下确认）

## 关联

- 同目录其他 TechReq 工程项目见 `D:\Claude\CLAUDE.md`
- 领域知识 query / 跨项目结论 promote 走 Hub `wiki/`（🔒 内容用 `<private>` 标签隔离）

## 注意

TechReq 🔒 私人项目惯例：不推送公开远程仓库 / 不 `/promote` 回流 Hub 公开 wiki / 含密结论走 `<private>` 标签。
