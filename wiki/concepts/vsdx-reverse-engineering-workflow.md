---
type: concepts
created: 2026-05-10
updated: 2026-05-10
tags: [vsdx, visio, python, pywin32, reverse-engineering, template, skill, flowgen]
source_project: Tools/FlowGen
source_commits: [22c409f, 8c1e4bf, 8c8013d]
---

# Visio .vsdx 反演 + 模板渲染工作流

跨项目通用的"用户参考文件 → Python 模板"反演工作流。在 FlowGen 项目
2026-05-08~09 的 M7-roadmap + M7-archposter skill 实装中**重复 2 次**
得出固定模板,适用未来类似"参考一份 .vsdx / 一组 HTML → 自动生成同风格批量
.vsdx"的任务。

## 适用场景

用户提供 1-N 份**参考视觉文件**(.vsdx / HTML / PPT),希望:
1. 提炼参考的**视觉 DNA**(配色 / 字体 / 字号 / 间距 / 线型)
2. 让 Claude 用 Python + pywin32 **批量产出同风格** .vsdx
3. 跨项目复用(`flowgen-*` skill 模式)

## 五步固定流程

```
┌─ 1. ingest 参考文件 ───────────────────────────────┐
│  raw/{assets,references}/* → wiki/source-summaries/│
│  • 文本提取(unzip + ElementTree 解析 page1.xml)     │
│  • 颜色 / 字体 / 字号统计                            │
│  • 关键 ShapeSheet cell 探测(如 BevelTopType 等)     │
└────────────────────────────────────────────────────┘
                    ↓
┌─ 2. 提炼风格规范 ──────────────────────────────────┐
│  wiki/concepts/<style-name>.md                      │
│  • 配色 token 表(palette key → RGB)                 │
│  • 字体降级链 (Visio 中文版默认装的字体优先)         │
│  • 三线型规范 (LinePattern 1/2/3 = solid/dash/dot)   │
│  • 布局骨架 ASCII 图                                 │
│  • Pydantic schema 草图(为 Phase 1 模板奠基)        │
└────────────────────────────────────────────────────┘
                    ↓
┌─ 3. 反演脚本(关键!)─────────────────────────────┐
│  scripts/probe_<name>_vsdx.py                       │
│  • Python ElementTree 递归提取所有 Shape            │
│  • 转 page 绝对坐标(group_origin + sub_pin)         │
│  • 输出 wiki/concepts/<name>-shapes.raw.{json,txt}  │
│  • 作为模板硬依赖(精确几何参数源)                    │
└────────────────────────────────────────────────────┘
                    ↓
┌─ 4. 写模板(.claude/skills/<skill>/templates/) ─────┐
│  • Python 全局变量 SPEC(无 LLM,Claude 直接改数据)   │
│  • palette 字典 + N 色位强校验                       │
│  • CLI: --from-json fixture + --palette切配色       │
│  • 1 个 fixture 复刻 raw 完整数据(打包到 templates/) │
│  • render() 主流程 + 多个 draw_*() 分模块函数         │
└────────────────────────────────────────────────────┘
                    ↓
┌─ 5. 多轮用户目检迭代 ──────────────────────────────┐
│  每画完一个区(header/body/quad/audit) 让用户跑     │
│  Visio 打开对比 raw,描述偏差(字小/挤/位置错/对齐)   │
│  → 改 → 再跑 → 重复(典型 3-5 轮收敛到"可接受")      │
└────────────────────────────────────────────────────┘
```

## 关键工具与方法

### 反演脚本(Phase 0)模板

```python
# scripts/probe_<name>_vsdx.py 核心逻辑
import xml.etree.ElementTree as ET
import zipfile

NS = "{http://schemas.microsoft.com/office/visio/2012/main}"

def collect_shapes(parent, depth=0):
    """递归收集所有 Shape(包括嵌套 Group 内部)"""
    out = []
    for child in parent:
        if child.tag == NS + "Shape":
            out.append(child)
            inner = child.find(NS + "Shapes")
            if inner is not None:
                out.extend(collect_shapes(inner, depth+1))
        elif child.tag == NS + "Shapes":
            out.extend(collect_shapes(child, depth+1))
    return out

def get_cell(shape_el, name):
    """直接子级 Cell 取值(不递归 sub-shape)"""
    for cell in shape_el.findall(NS + "Cell"):
        if cell.get("N") == name:
            return cell.get("V")
    return None

def get_char_cell(shape_el, name):
    """字符样式 Cell(Section[Character] 内)"""
    cs = next((s for s in shape_el.findall(NS+"Section")
               if s.get("N")=="Character"), None)
    if cs is None: return None
    row = cs.find(NS+"Row")
    if row is None: return None
    for cell in row.findall(NS+"Cell"):
        if cell.get("N") == name:
            return cell.get("V")
    return None

# 使用:解 vsdx + 提 page1.xml + 转绝对坐标 + 输出 JSON
```

### 模板渲染辅助函数

```python
def draw_rect(page, x1, y1, x2, y2, *,
              fill=None, line=None, line_pattern=1,
              rounding_in=0.0, text="",
              font="SimSun", size_pt=12, color="RGB(10,10,10)",
              bold=False, align="center", valign="middle",
              letterspace_pt=0.0):
    """统一矩形 + 填充 + 边框 + 圆角 + 文本 + letter-spacing"""
    s = page.DrawRectangle(x1, y1, x2, y2)
    if fill is None:
        s.Cells("FillPattern").Formula = "0"  # 透明
    else:
        s.Cells("FillForegnd").Formula = fill  # "RGB(r,g,b)"
    if line is None:
        s.Cells("LinePattern").Formula = "0"
    else:
        s.Cells("LineColor").Formula = line
        s.Cells("LinePattern").Formula = str(line_pattern)
    if rounding_in > 0:
        s.Cells("Rounding").Formula = f"{rounding_in} in"
    if text:
        s.Text = text
        s.Cells("Char.Font").Formula = f'"{font}"'
        s.Cells("Char.Size").Formula = f"{size_pt} pt"
        s.Cells("Char.Color").Formula = color
        if bold:
            s.Cells("Char.Style").Formula = "17"
        if letterspace_pt:
            s.Cells("Char.Letterspace").Formula = f"{letterspace_pt} pt"
    return s
```

## 经验教训(踩坑表)

| 问题 | 现象 | 修法 |
|---|---|---|
| **Visio fallback 到 Calibri** | 用 Noto Serif SC / JetBrains Mono 等非默认字体 → Visio 自动退到 Calibri,中文挂图风格全失 | 直接用 SimSun + Microsoft YaHei + Consolas(中文版默认装,100% 可用) |
| **letter-spacing 撑出文字框** | 中文文本加 1.5-2pt letterspace,字间距过大,文字超出盒子被裁切 | **中文 letter-spacing 设 0**,mono 英文 0.3-0.8pt(保留工业风但不撑) |
| **Bevel + Shadow 视觉过强** | 默认开启 BevelTopType + ShapeShdwShow,所有矩形看起来"塑料感"过重 | 默认 `bevel_shadow=False`,需要时显式启用单个 shape |
| **chip 估宽偏大导致换行错乱** | chip flex-wrap 一行只装 3 个,期望装 4 个 → 字符宽估算公式偏大 | 按字号实测调:8pt 中文 ~0.13/字 + 小 padding(0.05)+ 小 gap(0.04) |
| **page1.xml regex 解析嵌套 Group 失败** | 用 regex 拆 Shape 块,内嵌 `<Shapes>` 子节点搞砸边界 | 用 ElementTree 递归遍历,不要 regex |
| **PinX/Y 是中心点不是 y_lower** | shape bbox 计算错误,几何全乱 | `y1 = pin_y - height/2`,要做绝对坐标转换 |
| **DrawRectangle 默认主题** | 落 shape 后 fill 颜色被主题覆盖 | 渲染后立即 `Cells("FillForegnd").Formula = "RGB(...)"` |
| **direction 与 page 不一致** | `DIRECTION="horizontal"` + `PAGE="A3-portrait"` → 布局错乱 | validate_spec 强校验 |

## 模板结构(标准化)

```
.claude/skills/<skill-name>/
├── SKILL.md                     # 触发词 + 决策树 + few-shot 3 例 + 反馈格式
└── templates/
    ├── <name>.py                # ~600-800 行 渲染模板
    └── fixtures/
        └── <complete-data>.json # 复刻 raw 的完整数据(供 --from-json 测试)

scripts/
└── probe_<name>_vsdx.py         # 一次性反演脚本(Phase 0,产物入 wiki/concepts/)

wiki/concepts/
├── poster-<name>-style.md       # 风格规范(palette / 字体 / 字号 / 布局)
└── <name>-shapes.raw.{json,txt} # 反演数据(作模板硬依赖)

wiki/source-summaries/
└── <name>-html-references.md    # 来源参考摘要(raw 文件 5W1H)

wiki/decisions/
└── YYYY-MM-DD-<skill-name>.md   # 设计决策(含 N 项关键选择 + 实施期反馈修正)

specs/active/ → archive/         # spec 起草 → plan → 实装 → 归档
```

## 复用建议

下次接到"参考 X 文件做同风格 Y"类任务,直接走五步:

1. **ingest** raw → wiki/source-summaries
2. **提炼** wiki/concepts/<style>.md(palette + 字体 + schema 草图)
3. **反演** scripts/probe_*.py → wiki/concepts/*.raw.json(精确几何源)
4. **写模板** + fixture(复刻原图作 regression baseline)
5. **多轮目检**(默认接受 3-5 轮迭代,每轮聚焦一个区)

## 项目实例

- **flowgen-roadmap**(M7,2026-05-08):反演 `raw/assets/系统.vsdx`(51 shape)
  → A4 portrait 5 段版式模板 → fixture system-uwacomm.json
  - 关键修正:版式从"三栏纵向"修正为"5 段竖向 + 左栏头"(不看 raw 凭直觉
    会错)
  - commit: 8c1e4bf
- **flowgen-archposter**(M7-archposter,2026-05-09):反演
  `raw/references/{横版,竖版}.html`(372 shape baseline)→ A3 双形态挂图模板
  → fixture wuhua-wuceng.json
  - 关键修正:letter-spacing 全局减小 / EN 副标位置调整 / chip 估宽算法
  - commit: 8c8013d

## 派生

- 下次有 Visio / OOXML 反演任务,可直接引用本工作流而不必从零总结
- 反演脚本模板(probe_*.py)可作为 wiki/concepts/templates/ 提供
