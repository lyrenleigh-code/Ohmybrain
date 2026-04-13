# 算法理论

> 核心算法原理与公式推导笔记。每张卡片是知识图谱的核心节点，连接论文、模块实现和调试经验。

---

## 算法卡片

```dataview
TABLE aliases as "别名", tags as "标签"
FROM "3-Resources/算法理论"
WHERE contains(tags, "算法") AND file.name != "README"
SORT file.name ASC
```

## 主题分类

### 稀疏重建
- [[GAMP广义近似消息传递]]
- [[OMP正交匹配追踪]]
- [[SBL稀疏贝叶斯学习]]

### 时变信道
- [[BEM基扩展模型]]

### 均衡
- [[MMSE-IC最小均方误差干扰消除]]
- [[DFE判决反馈均衡]]
- [[MP消息传递OTFS均衡]]

### 编译码
- [[BCJR前向后向MAP译码]]

## 待创建

- 卡尔曼滤波与跟踪
- VAMP/Turbo-VAMP
- EXIT Chart 分析
