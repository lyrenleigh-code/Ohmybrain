---
project: uwacomm
type: task
status: active
created: 2026-04-12
updated: 2026-04-12
tags: [模块07, 多普勒, 测试]
---

# 模块07 doppler_rate=0 修正

## Spec

### 目标

修正模块 07 统一测试中 doppler_rate=0 的问题，使时变均衡测试包含真实多普勒频偏。

### 原因

当前 `test_channel_est_eq.m` 第 701 行 doppler_rate=0，时变均衡测试仅测了 Jakes 衰落下的估计+均衡能力，未包含真实多普勒频偏。模块级测试结果不能直接反映端到端场景性能。

### 范围

- 代码仓库：`H:\UWAcomm`
- 主要文件：
  - `07_ChannelEstEq/src/Matlab/test_channel_est_eq.m`（约第 701 行）
  - `07_ChannelEstEq/src/Matlab/gen_test_channel.m`（可能需适配）
  - `07_ChannelEstEq/src/Matlab/README.md`（更新测试结果表）

### 非目标

- 不改动估计/均衡算法本身
- 不改动端到端测试（13_SourceCode）

### 验收标准

- [ ] test_channel_est_eq.m 时变测试使用非零 doppler_rate（如 1e-4）
- [ ] 重新运行 24 项测试，更新结果表
- [ ] README.md 测试结果同步更新
- [ ] 新旧结果对比写回 wiki

---

## Plan

（确认 spec 后填写）

### 影响文件

| 文件 | 变更类型 | 说明 |
|------|---------|------|
| `test_channel_est_eq.m` | 修改 | doppler_rate 改为非零值 |
| `gen_test_channel.m` | 可能修改 | 确认支持 doppler_rate 参数 |
| `README.md` | 更新 | 重新填写测试结果表 |

### 实现步骤

1. 确认 gen_test_channel / gen_uwa_channel 对 doppler_rate 的支持
2. 将 doppler_rate=0 改为合理值（如 1e-4，对应 ~1Hz@10kHz fc）
3. 运行全部 24 项测试
4. 记录新基线结果
5. 更新 README.md 中的测试结果表
6. 新旧结果对比分析

### 测试策略

- 运行 `test_channel_est_eq.m` 全部测试项
- 对比：doppler_rate=0 vs doppler_rate=1e-4 的结果差异
- 关注：时变估计 NMSE 和时变均衡 SER 的变化幅度

### 风险

| 风险 | 概率 | 应对 |
|------|------|------|
| 加入真实 Doppler 后部分方法性能大幅下降 | 高 | 这是预期的，记录为新基线 |
| gen_test_channel 不支持 doppler_rate | 低 | 检查接口，必要时适配 |

---

## Log

（执行过程中记录）

---

## Result

（完成后填写结论，promote 到 wiki）
