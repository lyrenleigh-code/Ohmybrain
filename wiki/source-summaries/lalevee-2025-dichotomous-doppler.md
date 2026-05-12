---
type: source-summary
created: 2026-04-22
updated: 2026-04-22
tags: [水声通信, 多普勒估计, FPGA, 二分法, 滤波器组, 实时处理, OCEANS, 会议论文]
source_type: paper
source_path: D:/Claude/TechReq/UWAcomm/raw/papers/New_Dichotomous_Implementation_Approach_for_Doppler-Shift_Estimation_and_Compensation_in_an_Underwater_Acoustic_Modem.pdf
source_project: UWAcomm
---

# New Dichotomous Implementation Approach for Doppler-Shift Estimation and Compensation in an Underwater Acoustic Modem

> **引用**：A. Lalevée, P. Forjonel, P.-J. Bouvet, L.P. Pelletier (2025). *New dichotomous implementation approach for Doppler-shift estimation and compensation in an underwater acoustic modem*. OCEANS 2025 Brest. DOI: 10.1109/OCEANS58557.2025.11104300
>
> **作者单位**：L@bISEN, ISEN Yncréa Ouest, Brest, France
>
> **通讯作者**：andre.lalevee@isen-ouest.yncrea.fr

## 来源信息

| 项 | 值 |
|-----|-----|
| 作者 | A. Lalevée, P. Forjonel, P.-J. Bouvet, L.P. Pelletier |
| 机构 | L@bISEN / ISEN Yncréa Ouest（法国布雷斯特） |
| 发表 | OCEANS 2025 Brest 会议 |
| 页数 | 5 页（4 正文 + 1 参考） |
| 类型 | 工程实现论文（算法结构 + FPGA 实现） |
| 关键词 | Doppler, FPGA, Underwater communications |
| PDF 路径 | `D:\Claude\TechReq\UWAcomm\raw\papers\New_Dichotomous_Implementation_Approach_for_Doppler-Shift_Estimation_and_Compensation_in_an_Underwater_Acoustic_Modem.pdf`（IEEE Xplore 原始 PDF） |

## 核心观点

1. **滤波器组法的精度优势不可否认，但算力开销是实时嵌入式的致命瓶颈** —— 水声调制解调器需要估计多普勒频移才能解均衡与译码。SOTA 三大类方法（WSSC+CW 双信号、首尾 preamble 时延伸缩、dopplerized 滤波器组）中，**滤波器组在精度上最优**，代价是穷举 N 个多普勒假设的相关运算。论文正是要把这个"精度最高但最贵"的方法搬上 FPGA。
2. **二分法搜索把穷举 N 降到 log₂N** —— 论文把 dopplerized 模板按多普勒值排列成**二叉树**，每层只测两个节点（当前最佳的左右子节点），若该层无相关峰则继续探索全层，若有则剔除另一分支。最优情形下 N 级二叉树可以区分 2^(N+1)−2 个多普勒假设，**只要 2N 次相关运算**。
3. **FPGA 并行化让"每层两次运算"压成"每层一次时钟"** —— 作者把相关支路复制一份，最佳情形下"下一层"与"上一层计算"在同一时钟周期重叠，即每下一级只消耗 1 次 FFT 时间。加上解调/滤波/下采样与相关并行，整体吞吐量在 100 MHz 时钟下跑到 **122.88 μs / iFFT**，每个 81.7 ms 数据块能算 634 次 iFFT，极限可区分 2^635−2 个多普勒假设。
4. **滑窗 FIFO 解决"模板跨数据块"的漏检问题** —— 若已知序列横跨两个数据块，相关峰会被切断。论文用 FIFO 滑窗（读指针后退 226 样本/帧）保证模板永远完整落在一个窗内。工程实现细节用双端口 RAM + 读写计数器。
5. **二分法精度优于滤波器组法，且浮点>定点（符合预期）** —— 6 级二叉树在 −3 ~ 3 m/s 速度范围（−53.89 ~ 53.89 Hz @ 27 kHz）下的分辨率 0.09375 m/s（1.69 Hz）。仿真在 SNR = 20 dB 与 5 dB 下显示：**dichotomy 平均误差 < 滤波器组**；浮点略优于定点。
6. **资源占用可观但可接受（Xilinx Zynq xc7z020 数量级）** —— 17244 LUT / 2167 FF / 21 BRAM / 22 DSP，FFT 与 iFFT×2 占据大头。这是 26k 门级 FPGA 的适中占用，适合嵌入式声学调制解调器板卡。
7. **适用场景不仅是通信也是 LBL/USBL 定位** —— 同一二分法骨架可同时服务通信（PSK 星座解旋）和定位（插值最合规的多普勒以获取最准到达时间）。配合正交信号，可对 10 信标并行跟踪，20-30 信标是市售系统上限。
8. **方法不确定但有趣的未来工作** —— 作者明确承认：(a) 平台 IROMI-LMAIR 尚未海试验证；(b) 下降速度取决于"第一层检到峰"的概率，非确定性；(c) 用"先扫视线内信标"的 dichotomic controller 可进一步优化。

## 研究问题

嵌入式水声调制解调器如何在**不牺牲滤波器组精度**的前提下，**把多普勒估计的算力塞进 FPGA 的实时预算**？
具体要回答：
- 能否避免对 N 个多普勒假设做全穷举相关？
- 能否用并行硬件把"每层两次测试"消化为恒定延迟？
- 能否处理"模板跨数据块"的边界条件？
- 资源占用能否控制在 Zynq 7020 级 FPGA 可承受范围？

## 方法 / 算法

### 方法 1：二叉树搜索（§III-A, B）

**数据组织**：把 dopplerized 模板按多普勒值从小到大排列成**平衡二叉树**，根节点是 0 Hz，左右子树分别代表负/正多普勒。

**搜索流程**：
1. 第 1 级：测试根的两个直接子节点（如 −71.8 Hz 与 +71.8 Hz），若**均无相关峰**，则进入第 2 级全展开
2. 第 2 级：测试所有"尚未被剔除的子节点"，若某节点检出相关峰，记录该分支
3. 若单层出现 ≥2 个相关峰，只保留**最大值**所属分支，其他分支整体剔除
4. 继续向下逐级收敛，直到树底
5. 最终输出：**所有未剔除节点中相关峰最大者**的多普勒值

**复杂度**：
- 最优情形（第 1 级即检到峰）：N 级树只需 2N 次相关运算，可判别 2^(N+1)−2 个假设
- 最差情形（逐层全展开）：退化到穷举，但仍不劣于原滤波器组

### 方法 2：FPGA 并行相关（§IV-A）

**关键观察**：FPGA 可以把"解调 + 滤波 + 下采样"与"相关计算"做成流水线并行。进一步，把相关支路**复制一份**（×2 相关器）即可单时钟内完成左右子节点比较，即**每下一级只等一次 FFT 时间**。

**时序预算**（100 MHz 时钟）：
- 1024 点 FFT 需 N(2 + log₂N) = 1024 × 12 = 12288 周期 ≈ 122.88 μs
- 数据块间隔 81.7 ms（下采样到 9.766 kHz，每块 798 新样本）
- 每数据块可跑 81.7 ms / 122.88 μs ≈ **634 次 iFFT**
- 极限多普勒假设分辨能力：2^635 −2（远超任何实际需要）

### 方法 3：滑窗 FIFO（§IV-B）

**问题**：模板长度 226 样本，数据块 1024 样本。若模板跨两个数据块，相关峰被腰斩。

**方案**：每次新块不从上一块末尾开始，而是**回退 226 样本**（即读指针跳 −226）。实现上用**双端口 RAM + 读/写计数器 + shift control signal**，每完成一次 FFT 触发一次 shift。

### 方法 4：信号模型（§II）

- **波形**：BPSK 头（19.9 ms）+ QPSK 数据（209.7 ms）的复合单载波信号
- **中心频率**：27 kHz；**带宽**：4 kHz；**SRRC 滚降**：0.4
- **阈值准则**：相关峰 > 阈值（窗内信号能量的镜像）；**主峰下 9 dB 为阈值**，次瓣距主瓣 **12 dB** 以避免误检

## 关键数据 / 结果

### 多普勒假设区分能力对比

| 方案 | 操作次数 | 可判别假设数 |
|------|---------|-----------|
| 非优化滤波器组（穷举） | 1268 次相关 | 1268 |
| 本文最优情形（每级都检到峰） | 634 次 iFFT 时间 | 2^635 − 2 |
| 本文 6 级二分（实测） | 12 次相关（8 次实际计算） | 14 |

### 精度参数（§III-C）

- **速度范围**：−3 ~ +3 m/s（对应 −53.89 ~ +53.89 Hz @ 27 kHz）
- **6 级二分树分辨率**：**0.09375 m/s（1.69 Hz）**
- **仿真 SNR**：20 dB 和 5 dB 两点
- **精度排序**（按平均误差从小到大）：dichotomy 浮点 < dichotomy 定点 < 传统滤波器组

### FPGA 资源（Xilinx Zynq xc7z020clg400，16-bit 定点）

| 组件 | LUT | FF | BRAM | DSP |
|------|-----|-----|------|-----|
| Demodulation | 71 | 36 | 0 | 2 |
| FIR | 381 | 1060 | 0 | 2 |
| FIFO shift | 108 | 40 | 1 | 0 |
| FFT | 5558 | 316 | 6 | 4 |
| iFFT (×2) | 5525 | 296 | 6 | 4 |
| Others | 76 | 123 | 2 | 6 |
| **总计** | **17244** | **2167** | **21** | **22** |

## 对 UWAcomm 项目的启发（与 α 补偿迭代 refinement 对比）

### 横向对比：dichotomy vs iterative refinement（深度比较）

| 维度 | 本文 dichotomy | UWAcomm α 补偿 refinement |
|------|----------------|---------------------------|
| 目标 | 多普勒频移 f_d（Hz） | 多普勒伸缩系数 α（= 1 + v/c） |
| 搜索空间 | 离散 dopplerized 模板集合 | 连续 α 标量 |
| 搜索策略 | 二叉树分层剪枝 | 迭代 refinement（双 LFM + 互相关峰） |
| 运算主体 | N 次相关（FFT/iFFT） | 一次 Resample + 一次互相关 + 迭代 2-3 次 |
| 复杂度 | O(log₂N) 最优 / O(N) 最差 | O(迭代次数 × resample) |
| 精度 | 由二分分辨率决定（本文 1.69 Hz） | 由互相关峰插值精度决定（亚采样级） |
| 确定性 | 非确定（与首层检峰概率相关） | 确定性（固定迭代次数） |
| 硬件友好度 | 强（本文专为 FPGA 设计） | 一般（MATLAB 端到端仿真，未考虑实时） |
| 带外泛化性 | 需要预先离散化多普勒网格 | 连续域搜索无网格限制 |

### 对 UWAcomm 的具体借鉴

1. **窄多普勒范围 + 高精度场景可改用二分法替代穷举** —— 若未来 UWAcomm 的实时嵌入式版本（如 FPGA 板卡）需要多普勒估计，且能接受离散网格，dichotomy 比穷举滤波器组快 log₂N 倍，是强力候选。
2. **27 kHz 中频、4 kHz 带宽是水声嵌入式调制解调器的典型参数锚点** —— UWAcomm 现用 8-12 kHz 左右的仿真参数，与该工程参考相比对有意义，可作为系统级参数选型的参考。
3. **滑窗 FIFO 是处理"模板跨块"边界条件的标准工程解法** —— UWAcomm 的帧同步模块若扩展到流式接收，可借鉴该 FIFO + shift pointer 结构。
4. **相关峰阈值准则（主峰 −9 dB，旁瓣 −12 dB）是工程化经验值** —— 可直接借入 UWAcomm 的同步检测单元，作为"是否承认检到相关峰"的判定依据，替代主观阈值。
5. **二叉树思想对 UWAcomm α 补偿 refinement 有另一种角度的启发** —— 当前 UWAcomm α refinement 是"以上次估计为锚做局部搜索"的**爬山**思路；dichotomy 则是"离散化假设空间后做全局分层剪枝"的**树搜索**思路。若 α 的先验范围无法收窄（如新场景冷启动），二分法比迭代 refinement 更安全。
6. **精度优势论断值得项目引用** —— 论文明确宣称 dichotomy 平均误差 < 滤波器组，是对"精度 vs 算力"长期权衡的一个反直觉结论（算力降低但精度不降反升），可作为 UWAcomm 选型决策的参考文献。
7. **非确定性延迟是硬实时系统的警示** —— 论文作者自己承认"下降速度取决于第一层检峰概率"。UWAcomm 若要做硬实时系统，必须配置"最差情形预算"，不能只看最优情形。
8. **资源占用参考（17k LUT/22 DSP@100 MHz）** —— Zynq 7020 中低端 FPGA 能承载完整多普勒估计链，是对国产化嵌入式声学调制解调器"算力够不够"的直接回答。

## 相关概念

- [[underwater-acoustic-communication]] — 多普勒估计是水声通信接收端的核心前置步骤
- [[signal-processing-fundamentals]] — 滤波器组、相关检测、阈值准则、FIFO 滑窗都是信号处理基础的硬件化实例
- [[time-varying-channel]] — 多普勒频移是时变信道的显式表现，直接驱动本文方法的存在意义
- [[mobile-communication]] — AUV 运动是多普勒效应的主要物理来源，本文研究对象本质上是 mobile scenario
- [[usbl-positioning]] — 论文应用段明确 LBL/USBL 是同构应用场景（多信标同时跟踪）
- [[mimo-and-array-processing]] — 多信标正交信号跟踪是并行相关的典型应用（10 beacons 常见、20-30 beacons 为上限）

## 相关资料

- UWAcomm 当前 α 补偿方案：详见 MEMORY.md `[UWAcomm α 补偿改造]`（双 LFM + 迭代 refinement + pipeline 诊断，2026-04-22 已进入 4 体制）
- 同组作者前作参考：Bouvet 团队 [7] MIMO 水声实验（OCEANS 2017）、[8] 通信基础的 AUV 定位（JMSE 2024）、[9] 移动水声传感网时间同步（IEEE JOE 2016）
- 方法溯源：
  - [3] Garin 2023 OCEANS Limerick — 单信标同时定位与通信
  - [5] Sharif 2000 IEEE JOE — preamble/postamble 伸缩比多普勒估计（经典方法 2）
  - [6] van Walree 2011 FFI — 信道探测用滤波器组（经典方法 3 的源头）
- 相关 UWAcomm 论文对照：
  - [[wei-2020-dual-hfm-speed-spectrum]] —— 双 HFM + 速度谱扫描，另一条非二分的多普勒估计路径
