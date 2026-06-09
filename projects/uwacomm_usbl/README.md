# UWAcomm_usbl 🔒

> 水声通信 + USBL 联合定位/通信仿真 — 把 UWAcomm 的通信链路与 USBL 的几何定位耦合，研究通信信号复用为定位探测信号、定位/通信联合优化、跨模块互馈等场景

- **仓库**：内网 GitLab Internal 可见（http://192.168.10.100:8880/lilin/UWAcomm_usbl，**不推 GitHub**）
- **本地**：`D:\Claude\TechReq\UWAcomm_usbl`
- **分类**：TechReq/（算法研究类，与 UWAcomm / USBL / UWAnet 同级）
- **状态**：**SPEC-001 批 0+1 完成**（2026-04-25，M1 8 文件 70k 字 C 档详细级），3 冲突待决，批 2-6 暂停
- **派生自**：历史旧模板（2026-04-25 派生）；当前同类模板为 `D:\Claude\ohmybrain-core\template-engineering\`
- **启动模式**：混合（M0-M1 闭环冷启动 → M2+ 切手动）

## 关联项目

- **依赖**：
  - [[uwacomm]] — 6 体制水声通信仿真平台（SC-FDE / OFDM / SC-TDE / OTFS / DSSS / FH-MFSK），提供链路层与信道模型
  - [[USBL]] — 超短基线自定位算法（D:\Claude\TechReq\USBL），提供阵列几何与时延/方位角解算
- **资料增量**：raw/ 后续会持续追加用户提供的论文 / 数据 / 参考实现

## SPEC-001 技术设计方案进度

把 raw 方案 [[usbl-loadout-v1.0]] 五大模块从"页面级速查"细化为**部件级技术输出报告**（C 档详细级，每部件 1500-2500 字），整体 41 文件输出在 `docs/tech-design/`：

| 批次 | 模块 | 文件数 | 状态 |
|------|------|--------|------|
| 批 0 | overview | 1 | 🟢 完成 |
| **批 1** | M1-waveform（8 部件：唤醒 / LFM 前导 / 同步字 / OFDM 数据 / 尾 LFM / JANUS / 链路预算）| 8 | 🟢 **完成（70k 字）** |
| 批 2 | M2-array-cal（7 部件：几何 / L1-L4 校准 / 多基线）| 7 | ⏸ 暂停 |
| 批 3 | M3-fpga（9 部件：Zynq / ADC / DDC / 匹配滤波 / FFT / CORDIC / 定点 / 水下 MCU）| 9 | ⏸ 暂停 |
| 批 4 | M4-ekf（8 部件：17D 状态向量 / 量测 / 过程 / bias / 创新检验 / 8D 简化）| 8 | ⏸ 暂停 |
| 批 5 | M5-mechanical（6 部件：换能器 / 阵基 / 耐压舱 / 连接器 / 部署）| 6 | ⏸ 暂停 |

**3 冲突待决**：见 spec 文件 `specs/active/SPEC-001-techdesign-master.md`。

## 目标方向

- 通信波形作为定位探测信号的可行性（同步序列复用为 USBL ping）
- 多普勒估计在通信解调与 USBL 距离测量两端的耦合误差
- 阵列几何对低 SNR 通信链路的辅助（空时联合处理）
- 定位 / 通信联合资源分配

## 约束

- **单用户私人项目**：本地保存，不推 GitHub
- **MATLAB 主力**（与 UWAcomm / USBL 一致）
- **不复制 UWAcomm / USBL 代码**：通过路径引用或 wiki 摘要复用，避免双向漂移

## 后续工作

spec / plan / M1 MVP 实施均**在 UWAcomm_usbl 项目自身的 Claude Code 会话内**进行，本 Hub README 只做导航。

## 相关

- 记忆：`project_uwacomm_usbl_init` · `project_uwacomm_usbl_techdesign`
- Hub wiki：[[usbl-positioning]] · [[uwacomm]]
- 三仓架构：[[system-overview]]
