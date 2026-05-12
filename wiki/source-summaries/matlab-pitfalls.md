---
type: source-summary
created: 2026-05-12
updated: 2026-05-12
tags: [MATLAB, pitfalls, 调试]
source_type: note
---

# MATLAB 跨项目 Pitfalls 集合

## 主题

跨项目积累的 MATLAB 实战陷阱，便于 MATLAB 主力项目（UWAcomm / USBL / UWAcomm_usbl 等）参考。本页生长性收录——每个 pitfall 含**症状 / 根因假设 / 解法 / 来源**。

## Pitfalls

### #1 — `inf` 字面量触发"从 double 转换为 struct"错误

**症状**：
- MATLAB 测试脚本中使用 `[inf, 20, 10, 5, 2]` 这类数组字面量时，触发"从 double 转换为 struct"错误
- 重命名变量、清除缓存均无法解决

**根因假设**：
- MATLAB 路径上某个用户 `.m` 文件覆盖了 `inf` 内置函数（创建了同名 struct 或自定义函数）
- 字面量解析时 MATLAB 优先用 path 上的"自定义 `inf`"，导致类型不匹配

**解法**：
- 在源代码中**避免使用 `inf` 字面量**
- 用 `0` 表示"无穷大 / 无多径"等特殊值
- 配合 `Kval == 0` 判断替代 `isinf(Kval)`

**适用范围**：所有可能在 path 上有用户自定义 `.m` 的 MATLAB 项目（UWAcomm 已验证）

**来源**：UWAcomm 2026-04-13 test_sync.m 实测（memory `feedback_matlab_inf_bug`）

---

## 跨项目启发

- **MATLAB path 污染**是隐性常见陷阱——内置函数被同名 `.m` 静默覆盖时，错误信息极具误导性（指向 type conversion 而非 path）
- **诊断顺序**：遇到莫名 type conversion 错误时先 `which -all <function_name>` 查 path

## 相关概念

- 暂无（本页是单 pitfall 起点，后续累积时建立 cross-ref）

## 来源

- UWAcomm 2026-04-13 实测（memory `feedback_matlab_inf_bug`）
