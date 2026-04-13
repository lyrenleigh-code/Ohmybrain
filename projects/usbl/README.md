# USBL

> 超短基线水下自定位系统算法 — MATLAB 仿真原型

- **仓库**：github.com/lyrenleigh-code/USBL
- **本地**：`D:\Claude\TechReq\USBL`
- **状态**：活跃开发中

## 系统参数

| 参数 | 值 |
|------|-----|
| 中心频率 | 10 kHz (λ=15cm) |
| 阵列 | 五元均匀圆阵 (UCA), d=20cm, d/λ=1.33 |
| 最大距离 | ≥ 10 km |
| 精度 | 优于斜距 1% |
| 信号体制 | LFM, BW=4kHz, τ=100ms |

## 算法清单

| 类别 | 算法 | 角色 |
|------|------|------|
| **DOA 主力** | ML 两级搜索 | 单快拍最优, 天然解模糊 |
| **DOA 辅助** | 相位比较法 | 交叉验证 + 残差质量指标 |
| **DOA 粗估** | CBF | 解模糊基底 |
| 分析 | CRB / 误差分配 / 灵敏度 | 性能评估 |

## 代码结构

```
simulation/
├── config/usbl_config.m        # 全局参数
├── core/                       # 基础模块 (阵列/导向向量/信道/坐标变换)
├── doa/                        # DOA 算法 (CBF/MVDR/MUSIC/ML/相位比较)
├── analysis/                   # 误差分析
├── run_doa_comparison.m        # DOA 对比主脚本
├── run_error_budget.m          # 误差分配主脚本
└── run_full_simulation.m       # 全链路仿真
```

## 待办

| 项 | 优先级 |
|----|--------|
| 射线追踪极端声速剖面保护 | 中 |
| 多径效应（海面/海底反射） | 高 |
| C/C++ 产品化移植 | 后续 |

## 参考文献

- `reference/` 下 4 篇中文学位论文（USBL 定位/校准/精度改进）

## Hub wiki 关联

- [mimo-and-array-processing](../../wiki/concepts/mimo-and-array-processing.md)
- [signal-processing-fundamentals](../../wiki/concepts/signal-processing-fundamentals.md)
