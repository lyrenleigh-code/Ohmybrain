---
type: source-summary
created: 2026-04-17
updated: 2026-04-17
tags: [水声网络, MAC协议, Aqua-Sim-NG, ns-3, 仿真平台, UWAnet]
source_type: note
---

# 水声通信组网协议仿真笔记

## 来源信息

- **类型**：学习笔记（整理自对话）
- **本地路径**：`raw/notes/uwanet-protocol-sim.md`（282 行）
- **内容范围**：协议栈概览 / 仿真平台对比 / ns-3+Aqua-Sim-NG 环境搭建 / 5 节点 Slotted ALOHA 案例 / 理论要点 / 参考资料 / Claude Code 加速 / 1 月学习路线
- **定位**：UWAnet 项目（`TechReq/UWAnet`）**前期调研的主种子文档**——项目目前处于"前期调研阶段"，尚未产出仿真代码

## 核心观点

### 1. 协议栈分层与入门重点

水声网络沿用经典分层，但每层都有独特约束：

```
应用层 → 传输层 (UWAN-TCP / ALOHA-Q)
      → 网络层 (VBF / DBR / EEDBR)
      → MAC 层 (FAMA / MACA-U / T-LOHI)        ← 入门重点
      → 物理层 (OFDM / DSSS / FSK)              ← 复用 [[uwacomm]]
      → 水声信道 (多径 / 多普勒 / 高延迟)
```

**入门推荐**：MAC 层协议 + Aqua-Sim-NG（基于 ns-3）。**物理层直接复用 UWAcomm 已实现的 6 种通信体制**——这是 UWAnet 与 UWAcomm 的最自然衔接点。

### 2. 仿真平台选择：Aqua-Sim-NG 为首选

| 平台 | 定位 | 适用 |
|------|------|------|
| **ns-3** | 开源模块化，社区活跃 | 网络协议层仿真首选 |
| **Aqua-Sim-NG** | ns-3 水声扩展插件 | **水声网络专用首选** |
| **DESERT Underwater** | ns2/ns3 扩展 | 跨层协议研究 |
| MATLAB/Simulink | 信号处理强 | 物理层 + 信道建模（UWAcomm 当前用途） |
| Python + SimPy | 灵活轻量 | 自定义协议快速验证 |

**推荐组合**：Aqua-Sim-NG（ns-3）承载 MAC/网络层 + MATLAB (UWAcomm) 提供物理层信道模型。

### 3. 环境搭建关键点（Ubuntu 20.04 + ns-3.36）

- ns-3.36 版本与 Aqua-Sim-NG 兼容；高版本需验证
- Aqua-Sim-NG 源：`github.com/rmartin5/aqua-sim-ng`（克隆到 `src/aqua-sim/`）
- 编译 99% 报错源自 Python 版本（需 3.8+）
- 验证命令：`./ns3 run "aqua-sim-simple"`
- 重点入门文件：`src/aqua-sim/model/aqua-sim-mac-aloha.cc`

### 4. Slotted ALOHA 起步案例的改造路径

从 `examples/broadcastMAC.cc` 复制到 `scratch/my-mac-demo.cc`，改：
- 节点数 `nodes.Create(5)`
- MAC 类型 `AquaSimMacAloha` + `SlottedAloha=true`
- 线形拓扑 Z=-50m（水下 50 米）
- 自定义 `SendWithBackoff` 带退避（slot × UniformVariable(1,8)）
- 参数扫描批量 shell + Python matplotlib 绘吞吐量/时延曲线

### 5. Claude Code 加速仿真开发

笔记里给出的时间对比（手动 vs Claude Code 辅助）：

| 阶段 | 手动 | Claude Code |
|------|------|-------------|
| 环境搭建 | 5~7 天 | 1 天 |
| MAC 模块开发 | 7~10 天 | 2 天 |
| 调试排错 | 3~5 天 | 1 天 |
| 实验分析 | 2~3 天 | 1 天 |
| **合计** | **~4 周** | **~1 周** |

工作流：在 `ns-allinone-3.36/ns-3.36/` 下启动 `claude`，自然语言描述 → 自动读代码结构、生成 `.h`/`.cc` + 修改 `CMakeLists.txt` 注册模块。

**边界**：Claude Code 压不了"理解仿真结果背后原因"的时间——节点密度 vs 吞吐量曲线的解释仍依赖排队论/博弈论直觉。

## 相关概念

- [[underwater-acoustic-communication]] — 水声网络是 UWA 通信在组网方向的延伸（MAC 层 / 路由层已列入"关键技术"条目）

## 相关实体

- [[uwacomm]] — UWAnet 物理层直接复用 UWAcomm 的 6 种通信体制（OFDM / DSSS / FH-MFSK / SC-TDE / SC-FDE / OTFS）

## 新建 concept 提案

笔记覆盖面广（7 大节 + 1 学习路线），涉及 **MAC/网络/传输层协议** + **仿真平台生态** + **水声网络理论**——在现有 `underwater-acoustic-communication` concept 中挂靠较勉强。

**提案**：待 UWAnet 项目产出 ≥2 个实测结论后（MAC 协议实验 / 路由协议实验等），新建 concept `uwa-networking` 作为锚点页。当前**单源 defer**，不急于创建。

## 引用摘录

> "入门推荐路线：MAC 层协议 + Aqua-Sim-NG" — §一

> "重点学习文件：`aqua-sim-mac-aloha.cc`" — §四

> "工具加速写代码，理论理解无法跳过。" — §八
