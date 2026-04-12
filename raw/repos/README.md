# repos/ — 代码仓库与项目资料

## 存放内容
- 完整的 git 项目（作为 git submodule 或目录副本）
- 项目文档、架构说明
- 配置文件快照

## 来源
- **GitHub**：clone 或 submodule
- 本地项目：直接复制

## 目录结构
```
repos/
├── project-name/             # 每个项目一个子目录
│   ├── README.md             # 项目说明（可直接使用项目自带的）
│   └── ...                   # 项目文件
```

## 命名规范
```
项目名/                        # 与仓库名保持一致，小写连字符
```

示例：
```
repos/ohmybrain/
repos/uwacomm/
repos/dochub/
```

## 注意事项
- 大型仓库建议用 git submodule 引用，避免重复存储
- 如果只需要分析项目的部分内容，可以只存关键文件的快照
- node_modules/、build 产物等应通过 .gitignore 排除
