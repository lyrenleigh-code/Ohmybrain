# LLM Wiki + 开发工程 + Claude Code Harness 一体化仓库模板

这个模板适合把 **LLM wiki**、**开发工程流程** 和 **Claude Code 的 harness 思路** 放到同一个仓库里。

核心思路：

- 用 `raw/` 保存原始资料
- 用 `wiki/` 保存沉淀后的知识层
- 用 `specs/`、`plans/`、`src/`、`tests/` 承载开发任务
- 用 `.claude/` 放规则、skills、hooks、settings

---

## 仓库结构

```text
agent-knowledge-repo/
├─ CLAUDE.md
├─ README.md
├─ .gitignore
│
├─ .claude/
│  ├─ settings.json
│  ├─ rules/
│  │  ├─ wiki.md
│  │  └─ src.md
│  ├─ skills/
│  │  ├─ ingest-source/
│  │  │  └─ SKILL.md
│  │  ├─ plan-task/
│  │  │  └─ SKILL.md
│  │  ├─ implement-task/
│  │  │  └─ SKILL.md
│  │  ├─ lint-wiki/
│  │  │  └─ SKILL.md
│  │  └─ promote-answer/
│  │     └─ SKILL.md
│  └─ hooks/
│     ├─ protect-raw.sh
│     ├─ wiki-post-edit.sh
│     └─ check-stop.sh
│
├─ raw/
│  ├─ papers/
│  ├─ docs/
│  ├─ notes/
│  └─ imports/
│
├─ wiki/
│  ├─ index.md
│  ├─ log.md
│  ├─ concepts/
│  ├─ architecture/
│  ├─ modules/
│  ├─ decisions/
│  ├─ incidents/
│  ├─ source-summaries/
│  └─ comparisons/
│
├─ specs/
│  ├─ active/
│  └─ archive/
│
├─ plans/
├─ tasks/
├─ src/
├─ tests/
├─ evals/
│
├─ scripts/
│  ├─ lint_wiki.py
│  ├─ sync_index.py
│  ├─ validate_task.py
│  └─ promote_answer.py
│
└─ .github/
   └─ workflows/
      ├─ ci.yml
      └─ wiki-check.yml
```

---

## 每一层的职责

### `raw/`
原始资料层，只读。
论文、会议记录、设计文档、网页摘录、导入的 markdown 都放这里。

### `wiki/`
知识沉淀层。
这里不是原文复制，而是 Claude 维护后的“中间知识层”。

### `specs/`
需求入口层。
每个要开发的功能、修复的 bug、研究任务，都先落成一个 spec。

### `plans/`
实现计划层。
先拆解，再动手改代码。

### `src/ tests/ evals/`
交付层。
代码、测试、agent 流程评测都放这里。

### `.claude/`
harness 层。
规则、skills、hooks、项目设置都在这里。

---

## `CLAUDE.md` 示例

这个文件要短，放“总入口”和“永远有效的规则”，不要把长文档全塞进去。

```md
# CLAUDE.md

## Repo purpose
This repository combines:
1. a persistent LLM wiki under `wiki/`
2. raw source material under `raw/`
3. software delivery workflows under `specs/`, `plans/`, `src/`, `tests/`, and `evals/`

## Non-negotiable rules
- Never edit files under `raw/` unless the user explicitly asks.
- Prefer updating `wiki/` instead of repeating analysis in chat.
- Every code task starts from a spec in `specs/active/`.
- Every non-trivial implementation requires a plan in `plans/`.
- When code changes, update tests or explain why no test is needed.
- When knowledge changes, update `wiki/index.md` and `wiki/log.md`.
- Do not stop if requested deliverables are incomplete.

## Directory map
- `raw/`: immutable source material
- `wiki/`: curated knowledge layer
- `specs/active/`: current task specs
- `plans/`: implementation plans
- `src/`: source code
- `tests/`: automated tests
- `evals/`: agent and workflow evaluations
- `.claude/skills/`: reusable workflows
- `.claude/rules/`: path-specific rules
- `.claude/hooks/`: deterministic enforcement

## Standard workflows

### For new source material
1. Read the source from `raw/`
2. Create or update `wiki/source-summaries/...`
3. Update related pages in `wiki/concepts/`, `wiki/architecture/`, `wiki/modules/`, etc.
4. Refresh `wiki/index.md`
5. Append a short note to `wiki/log.md`

### For a new engineering task
1. Read the relevant spec from `specs/active/`
2. Create a plan in `plans/`
3. Inspect impacted files
4. Implement in `src/`
5. Add or update tests in `tests/`
6. Run checks
7. Update wiki pages if architecture or behavior changed

## Preferred commands
- lint wiki: `python3 scripts/lint_wiki.py`
- sync wiki index: `python3 scripts/sync_index.py`
- validate task: `python3 scripts/validate_task.py`
- run tests: `pytest -q`

## Completion criteria
A task is complete only when:
- requested files are updated
- relevant tests pass
- wiki updates are made when needed
- the final response states exactly what changed
```

---

## `.claude/settings.json` 示例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-raw.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/wiki-post-edit.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-stop.sh"
          }
        ]
      }
    ]
  }
}
```

---

## hooks 示例

### `.claude/hooks/protect-raw.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

INPUT="$(cat)"
FILE_PATH="$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // ""')"

if [[ "$FILE_PATH" == *"/raw/"* ]] || [[ "$FILE_PATH" == raw/* ]]; then
  echo "Editing raw/ is blocked. Put derived knowledge in wiki/ instead." >&2
  exit 2
fi

exit 0
```

### `.claude/hooks/wiki-post-edit.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"

python3 "$PROJECT_DIR/scripts/lint_wiki.py" || {
  echo "Wiki lint failed. Fix broken links / missing index updates before continuing." >&2
  exit 2
}
```

### `.claude/hooks/check-stop.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

INPUT="$(cat)"

if [[ "$(echo "$INPUT" | jq -r '.stop_hook_active // false')" == "true" ]]; then
  exit 0
fi

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"

python3 "$PROJECT_DIR/scripts/validate_task.py" >/dev/null 2>&1 || {
  echo "Task is not complete yet: required files, tests, or wiki updates are still missing." >&2
  exit 2
}

exit 0
```

---

## `.claude/rules/` 示例

### `.claude/rules/wiki.md`

```md
---
paths:
  - wiki/**
---

# Wiki rules
- Prefer concise, linked markdown pages.
- Each new page should link back to at least one parent page.
- Every source-derived statement should reference the source summary page.
- Avoid dumping raw text from `raw/`; summarize and structure it.
```

### `.claude/rules/src.md`

```md
---
paths:
  - src/**
  - tests/**
---

# Source code rules
- Keep functions small and testable.
- When behavior changes, update or add tests.
- Prefer explicit names over terse abbreviations.
- Update architecture wiki pages when module boundaries change.
```

---

## skills 示例

### `.claude/skills/ingest-source/SKILL.md`

```md
---
name: ingest-source
description: Read new material from raw/ and update the wiki knowledge layer.
---

# Purpose
Turn raw source material into structured wiki knowledge.

# Steps
1. Read the target file under `raw/`.
2. Create or update a summary page under `wiki/source-summaries/`.
3. Update the most relevant knowledge pages:
   - `wiki/concepts/`
   - `wiki/architecture/`
   - `wiki/modules/`
   - `wiki/decisions/`
   - `wiki/comparisons/`
4. Update `wiki/index.md`.
5. Append one entry to `wiki/log.md`.

# Output requirements
- Do not modify the raw file.
- Prefer linked pages over one giant summary.
- Mention which wiki pages were created or changed.
```

### `.claude/skills/plan-task/SKILL.md`

```md
---
name: plan-task
description: Create an implementation plan from a spec before coding.
---

# Purpose
Convert a spec into an actionable engineering plan.

# Steps
1. Read the spec in `specs/active/`.
2. Identify scope, constraints, dependencies, and affected files.
3. Write a plan in `plans/`.
4. Include:
   - goal
   - non-goals
   - touched modules
   - test strategy
   - rollback/risk notes
```

### `.claude/skills/implement-task/SKILL.md`

```md
---
name: implement-task
description: Implement a planned task with tests and wiki updates.
---

# Purpose
Execute a spec + plan safely.

# Steps
1. Read the spec and plan.
2. Inspect impacted files.
3. Implement changes in `src/`.
4. Update or add tests in `tests/`.
5. Run the relevant checks.
6. If architecture, behavior, or interfaces changed, update `wiki/`.
7. Summarize changed files and validation results.
```

### `.claude/skills/lint-wiki/SKILL.md`

```md
---
name: lint-wiki
description: Check wiki structure, links, orphan pages, and missing index entries.
---

# Steps
1. Run `python3 scripts/lint_wiki.py`
2. Fix broken links
3. Fix orphan pages
4. Refresh `wiki/index.md` if needed
5. Add a short entry to `wiki/log.md` if substantial cleanup was done
```

### `.claude/skills/promote-answer/SKILL.md`

```md
---
name: promote-answer
description: Turn a useful analysis or implementation result into a durable wiki page.
---

# Steps
1. Identify whether the answer belongs in concepts, architecture, modules, decisions, incidents, or comparisons.
2. Create or update the target wiki page.
3. Add backlinks from `wiki/index.md`.
4. Add a short change note in `wiki/log.md`.
```

---

## `wiki/` 的最小骨架

### `wiki/index.md`

```md
# Wiki Index

## Start here
- [Architecture overview](architecture/system-overview.md)
- [Core concepts](concepts/core-concepts.md)
- [Module map](modules/module-map.md)
- [Decision log](decisions/index.md)
- [Incident patterns](incidents/index.md)

## Active topics
- [Knowledge ingestion workflow](concepts/knowledge-ingestion.md)
- [Agent delivery workflow](concepts/agent-delivery.md)

## Recent changes
See [log.md](log.md)
```

### `wiki/log.md`

```md
# Wiki Change Log

## 2026-04-12
- Initialized repository structure
- Added baseline CLAUDE.md
- Added initial skills for ingest, planning, implementation, wiki lint, and answer promotion
```

### `wiki/architecture/system-overview.md`

```md
# System Overview

## Layers
1. Raw sources in `raw/`
2. Curated knowledge in `wiki/`
3. Task specs in `specs/`
4. Plans in `plans/`
5. Delivery in `src/`, `tests/`, `evals/`
6. Harness in `.claude/`

## Principle
Use wiki to preserve knowledge.
Use harness to enforce behavior.
```

---

## `specs/` 模板

### `specs/active/2026-04-12-add-ingest-validator.md`

```md
# Task Spec: Add ingest validator

## Goal
Add a validator that checks whether every new source summary links back to at least one parent wiki page.

## Why
To avoid isolated summaries that never become part of the navigable knowledge graph.

## Scope
- Add validation logic in `scripts/lint_wiki.py`
- Add tests
- Update wiki rules if needed

## Non-goals
- Full semantic deduplication
- Embedding-based retrieval

## Acceptance criteria
- Lint fails when a source summary has no backlinks
- Tests cover pass/fail cases
- Relevant wiki rules are updated
```

---

## `plans/` 模板

### `plans/2026-04-12-add-ingest-validator.md`

```md
# Plan: Add ingest validator

## Summary
Implement backlink validation for source summary pages.

## Impacted files
- scripts/lint_wiki.py
- tests/test_lint_wiki.py
- .claude/rules/wiki.md

## Steps
1. Inspect current lint behavior
2. Add backlink validation
3. Write tests
4. Run tests
5. Update wiki rule text if needed

## Risks
- False positives for newly created pages before index sync

## Validation
- pytest -q
```

---

## `scripts/` 最小占位

### `scripts/lint_wiki.py`

```python
from pathlib import Path
import re
import sys

WIKI = Path("wiki")

def md_files():
    return [p for p in WIKI.rglob("*.md") if p.is_file()]

def links_in(path: Path):
    text = path.read_text(encoding="utf-8")
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)

def main():
    files = md_files()
    errors = []

    for f in files:
        for link in links_in(f):
            if link.startswith("http://") or link.startswith("https://") or link.startswith("#"):
                continue
            target = (f.parent / link).resolve()
            if not target.exists():
                errors.append(f"{f}: broken link -> {link}")

    if errors:
        print("\n".join(errors))
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### `scripts/validate_task.py`

```python
from pathlib import Path
import sys

def main():
    checks = [
        Path("CLAUDE.md").exists(),
        Path("wiki/index.md").exists(),
        Path("wiki/log.md").exists(),
        Path(".claude/settings.json").exists(),
    ]
    if not all(checks):
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## GitHub Actions 示例

### `.github/workflows/wiki-check.yml`

```yaml
name: wiki-check

on:
  pull_request:
  push:
    branches: [main]

jobs:
  wiki:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run wiki lint
        run: python3 scripts/lint_wiki.py

      - name: Validate task baseline
        run: python3 scripts/validate_task.py
```

### `.github/workflows/ci.yml`

```yaml
name: ci

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Run tests
        run: pytest -q
```

---

## 实际使用顺序

### 新资料进入时
1. 把资料放进 `raw/`
2. 调 `/ingest-source`
3. Claude 更新 `wiki/source-summaries/...`
4. 同步更新 `wiki/index.md` 和 `wiki/log.md`

### 新开发任务进入时
1. 在 `specs/active/` 建 spec
2. 调 `/plan-task`
3. 生成 `plans/...`
4. 调 `/implement-task`
5. Claude 改 `src/`、`tests/`，必要时更新 `wiki/`

### 收尾时
1. `PostToolUse` 自动跑 wiki 检查
2. `Stop` hook 检查这轮任务是不是能结束
3. CI 再做一次仓库级验证

---

## 简化版理解

这个模板里：

- `raw/` 是**原始事实**
- `wiki/` 是**可复用知识**
- `specs/` 和 `plans/` 是**任务上下文**
- `src/ tests/ evals/` 是**交付物**
- `.claude/` 是**让 Claude 按你的方式干活的 harness**

你要的其实是两个闭环同时存在：

**知识闭环**：`raw → wiki → query → promote back to wiki`

**开发闭环**：`spec → plan → implement → test → validate → merge → write lessons back`
