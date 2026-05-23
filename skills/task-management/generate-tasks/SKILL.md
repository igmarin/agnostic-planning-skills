---
name: generate-tasks
license: MIT
description: >
  Breaks a feature or PRD into implementation tasks with TDD quadruplets
  (write test → run fail → implement → run pass). Auto-detects test commands,
  source directories, and doc conventions from the project. Saves to
  /tasks/tasks-[name].md. Language-agnostic.
  Trigger words: task list, implementation plan, feature breakdown, generate tasks, TDD.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## Quick Reference

- **Task 0.0:** Always "Create feature branch".
- **TDD:** Write test → Run fail → Implement → Run pass.
- **Paths:** Exact file paths. Never vague.
- **Auto-detect:** Infer test command, source dir, doc tool from project files.

## HARD-GATE

```text
DO NOT skip Task 0.0 (Create feature branch) unless user overrides.
DO NOT use vague references — every task needs exact file paths.
DO NOT combine TDD sub-tasks into a single task. Break out:
  a) Write test   b) Run test (verify fails)   c) Implement   d) Run test (verify passes)
Each c-step is one action in one primary file.
```

## Core Process

1. **Analyze** — extract Functional Requirements and Goals from the PRD or feature description.
2. **Detect project context** — auto-detect test command, source directory, test directory, and doc tool (see [PROJECT_DETECTION.md](./PROJECT_DETECTION.md) for detection rules). Fall back to asking the user if ambiguous.
3. **Determine mode** — phased plan (strategy/sequencing) or detailed checklist (implementation steps).
4. **Draft Relevant Files** — list every file to create/modify, including tests, docs, and diagrams.
5. **Draft Tasks** — build TDD quadruplets (1+ per work area, 3+ for multi-concern features), then documentation, README/docs updates, and code review gate.
6. **Save** to `/tasks/tasks-[feature-name].md`. Use the PRD's slug if one exists.
7. **Verify** — re-read saved file; confirm all Output Style elements are present.
8. **Deliver** — include the full checklist content, not a summary table.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[PROJECT_DETECTION.md](./PROJECT_DETECTION.md)** — How to auto-detect test commands, source directories, test directories, and doc tools from project files.
- **[HEURISTICS.md](./HEURISTICS.md)** — Which test to write first by change type.
- **[TASK_TEMPLATES.md](./TASK_TEMPLATES.md)** — Full template structure for phased plans and detailed checklists.

## Output Style

1. **Full checklist artifact** — include the concrete `tasks-[name].md` content, not a summary.
2. **Task 0.0** — "Create feature branch" with checkout command.
3. **Relevant Files** — all files with concrete paths, listed before Tasks.
4. **TDD quadruplets** — at least 1 per work area, four sub-tasks each (`a` write, `b` run fail, `c` implement, `d` run pass). Every line names the exact file path.
5. **Documentation** — public API docs + README/diagram updates. Name each file.
6. **Code review gate** — self-review before PR.
7. **Save location** — state path in `/tasks/`.
8. **Guidance Used** — section stating which companion files were used and why.
9. **Instructions for Completing Tasks** — work one sub-task at a time; verify RED before implementation, GREEN after.
10. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
| **create-prd** | Generate PRD first, then derive tasks from it |
| **plan-tickets** | When the same initiative also needs ticket drafts |
