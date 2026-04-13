# Citekey 命名规范

## 格式

Better BibTeX citation key format:

```
auth.lower + year + shorttitle(1,1)
```

**规则**：第一作者姓（小写） + 年份 + 标题第一个实词（小写）

## 示例

| 论文 | Citekey |
|------|---------|
| Rangan (2011) "Generalized approximate message passing..." | `rangan2011generalized` |
| Raviteja (2018) "Interference cancellation and iterative detection for OTFS" | `raviteja2018interference` |
| Tuchler (2002) "Minimum mean squared error equalization using..." | `tuchler2002minimum` |
| Bahl (1974) "Optimal decoding of linear codes for minimizing..." | `bahl1974optimal` |
| Wipf (2004) "Sparse Bayesian learning for basis selection" | `wipf2004sparse` |
| Hadani (2017) "Orthogonal time frequency space modulation" | `hadani2017orthogonal` |

## 中文论文/学位论文

中文作者使用拼音：

| 论文 | Citekey |
|------|---------|
| 朱广军 (2020) 硕士学位论文 | `zhu2020shuosheng` 或手动设为 `zhu2020thesis` |
| 杜鹏宇 (2019) 博士学位论文 | `du2019boshi` 或手动设为 `du2019thesis` |

**建议**：中文学位论文 citekey 手动设为 `姓拼音 + 年份 + thesis`，避免中文短标题带来的混乱。

## 冲突处理

同一作者同年多篇论文，Better BibTeX 自动在末尾加字母：
- `rangan2011generalized`
- `rangan2011estimation` （同年第二篇自动消歧）

## 在 Obsidian 中的使用

- 论文笔记文件名 = citekey + `.md`
- frontmatter 中 `aliases` 包含 citekey，支持 `[[citekey]]` 快速链接
- 在任何笔记中引用论文：`[[rangan2011generalized]]`
