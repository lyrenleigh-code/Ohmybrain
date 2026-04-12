# CLAUDE.md — my-brain 操作手册

## 仓库地图

| 目录 | 用途 |
|------|------|
| raw/ | 原始资料，只读，不得修改 |
| wiki/ | 知识沉淀层，所有推理从这里读 |
| workflows/ | 操作流程文档 |
| scripts/ | 自动化脚本 |

## 核心规则

1. **raw/ 目录只读**：任何情况下不得修改或删除 raw/ 下的文件。
2. **更新 wiki 必须同步更新 index**：每次新增或修改 wiki/ 下的文件，必须同步更新 wiki/index.md。
3. **所有变更必须记入 log**：每次操作结束前，在 wiki/log.md 末尾追加一条记录，格式为 `- YYYY-MM-DD: [操作描述]`。
4. **优先读 wiki**：回答问题时优先从 wiki/ 读取，不足时才回到 raw/ 补充证据。
5. **高价值回答要 promote**：如果一次对话产生了重要结论，必须将其写回 wiki/，不能只停留在聊天记录里。

## 命名约定

- wiki 页面文件名全部小写，用连字符分隔，例如：`harness-engineering.md`
- source-summaries 用原始文件名命名，例如：`paper-attention-is-all-you-need.md`
- 概念页标题格式：`# 概念名称`
- log 条目格式：`- YYYY-MM-DD: [操作]`

## 禁止行为

- 不得直接修改 raw/ 下任何文件
- 不得在没有更新 index.md 和 log.md 的情况下结束任务
- 不得凭记忆回答可以从 wiki 验证的问题
