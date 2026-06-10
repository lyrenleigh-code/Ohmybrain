# USBL_hw

> USBL 硬件设计（中文名「USBL硬件设计」）：声学基阵 / 收发电路 / 结构 / 接口的硬件本体设计

- **仓库**：`D:\Claude\TechReq\USBL_hw`
- **类别**：🔒 私人项目（TechReq 工程系 **engineering-hardware 子型首例**，禁止推送公开 GitHub/Gitee / 禁止 promote 未脱敏内容至 Hub 公开 wiki）
- **状态**：🟡 起步；SOP §1+§1.5 派生完成（含 design/bom/datasheets/prototypes/output 硬件目录扩展），待首个 spec；git init main 未 commit、无远程（push 待内网私有库）
- **派生时间**：2026-06-10（ADR-026，见 [[../../wiki/architecture/decision-log]]）
- **派生自**：`D:\Claude\ohmybrain-core\template-engineering\` + 硬件目录扩展
- **依赖**：USBL（算法主项目，**公开仓**——本项目资料不得回流其中）、UWAcomm_usbl 🔒（整机集成与实测经验，引用不复制）
- **启动模式**：手动（探索性长周期：spec → plan → 讨论 → 设计，每 checkpoint 停下确认）

## 为什么独立而非 USBL 分支

① USBL 主仓公开（github.com/lyrenleigh-code/USBL），硬件资料必须私密；② 交付物域不同（图纸/BOM/datasheet vs MATLAB 算法），二进制设计资料不宜混入算法仓历史；③ 沿 2026-06-09 口径走 engineering-hardware 子型——其目录结构经本项目实战验证后可升格 `template-hardware`（触发条件：第 2 个纯硬件项目出现）。

## 项目边界（与 UWAcomm_usbl 分工）

阵元位置 LS 校准算法（calibration/v1.x）、CAGE5 水池实测数据与 DOA 流水线（poolData/）、水听器收发三板架构（SPEC-003）均留 UWAcomm_usbl；**基阵 / 换能器 / 收发电路 / 结构 / 接口的硬件本体设计、BOM、样机验证归本项目**。跨界引用写指针不复制。

## 关联

- 算法主项目导航：`projects/usbl/README.md`
- 整机集成导航：`projects/uwacomm_usbl/README.md`
- 生态总览：[[../../wiki/topics/ecosystem-dashboard]]
