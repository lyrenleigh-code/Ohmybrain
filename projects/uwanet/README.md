# UWAnet

> 水声通信组网协议仿真 — Aqua-Sim-NG (ns-3)，物理层复用 UWAcomm

- **仓库**：github.com/lyrenleigh-code/UWAnet
- **本地**：`D:\Claude\TechReq\UWAnet`
- **状态**：前期调研阶段

## 协议栈架构

```
应用层    — 数据采集、任务调度
传输层    — UWAN-TCP / ALOHA-Q
网络层    — VBF / DBR / EEDBR
MAC 层    — FAMA / MACA-U / T-LOHI        ← 入门重点
物理层    — ← UWAcomm (OFDM/DSSS/FSK)
水声信道  — 多径、多普勒、高延迟
```

## 技术路线

| 层级 | 工具 | 重点 |
|------|------|------|
| 物理层 | MATLAB (UWAcomm) | 已有 6 种体制可复用 |
| MAC 层 | Aqua-Sim-NG (ns-3) | Slotted ALOHA → FAMA → MACA-U |
| 网络层 | Aqua-Sim-NG (ns-3) | VBF / DBR 路由 |
| 跨层 | ns-3 + MATLAB | 信道驱动自适应协议 |

## 里程碑

| 阶段 | 内容 | 状态 |
|------|------|------|
| M0 | 前期调研与技术选型 | 进行中 |
| M1 | ns-3 + Aqua-Sim-NG 环境搭建 | 待做 |
| M2 | 读懂 aqua-sim-mac-aloha.cc 源码 | 待做 |
| M3 | 实现自定义 MAC 模块（Slotted ALOHA） | 待做 |
| M4 | 参数扫描 + 性能分析 + 理论对比 | 待做 |

## 与 UWAcomm 的关系

UWAcomm 提供物理层（OFDM/DSSS/FSK + 信道模型 + 多普勒/同步），UWAnet 在其上构建 MAC/网络层。

## 前期调研材料

- `raw/notes/uwanet-moc-v1.md` — 项目地图
- `raw/notes/protocol-sim-brainstorm.md` — 288 行详细调研（环境搭建、代码结构、MAC 协议分类、学习路线）

## Hub wiki 关联

- [underwater-acoustic-communication](../../wiki/concepts/underwater-acoustic-communication.md)
- [mobile-communication](../../wiki/concepts/mobile-communication.md)
