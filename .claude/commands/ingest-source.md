# /ingest-source

对指定的原始资料文件执行完整的 ingest 流程。

## 参数
$ARGUMENTS — 文件路径，例如：raw/notes/my-note.md

## 执行步骤
1. 读取 $ARGUMENTS 文件内容
2. 按照 workflows/ingest.md 的步骤逐步执行
3. 生成 source-summary 页
4. 更新或新建相关概念页
5. 更新 wiki/index.md
6. 更新 wiki/log.md
7. 运行 python3 scripts/lint_wiki.py 验证
