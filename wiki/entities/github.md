---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, 同步, CI/CD]
entity_type: tool
---

# GitHub

代码托管和协作平台，是 my-brain 系统中**多设备同步和自动化检查的基础设施**。

## 角色定位

- 私有仓库存放 my-brain
- GitHub Actions 每次 push 自动跑 `lint_wiki.py`
- 版本历史作为知识变更记录的最终来源

## 建议设置

- 仓库设为 **Private**
- 开启 branch protection，防止强推覆盖历史
- Actions 只在 `wiki/` 有变更时触发，节省 CI 资源

## 多设备同步

所有设备通过 git 完成同步，不依赖云同步服务。[[obsidian]] Git 插件可自动完成 commit/pull 操作。

## 来源

- [[toolchain.md|工具链指南]] — 描述了 GitHub 的角色和配置建议
- [[my-brain-setup-plan.md|搭建计划]] — 第三阶段 GitHub Actions 自动化
