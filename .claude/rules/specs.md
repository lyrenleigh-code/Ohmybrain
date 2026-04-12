---
paths:
  - specs/**
  - plans/**
  - tasks/**
---

# 任务管理规则

- spec 是需求入口，必须包含：目标、原因、范围、非目标、验收标准
- plan 是实现路径，必须包含：影响文件、步骤、风险、验证方式
- 完成的 spec 从 `specs/active/` 移到 `specs/archive/`
- 任务完成标准：代码已更新 + 测试通过 + wiki 已同步（如需要）
