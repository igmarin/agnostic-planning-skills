---
name: generate-tasks
type: atomic
license: MIT
description: Break a feature into implementation tasks — always create a feature branch first, detect test command and directories, write failing test → implement → pass (TDD), and save to /tasks/tasks-[name].md. Use for task list, implementation plan, feature breakdown, TDD tasks.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## Quick Reference
- Task 0.0: create feature branch.
- Output: `/tasks/tasks-[feature-name].md`.
- Auto-detect test command, source dir, test dir, doc tool.
- Validate test command before full generation.

## Workflow

### 1. Project Detection
Detect conventions using config files (see [TEST_COMMANDS.md](./TEST_COMMANDS.md)). Identify source and test directories.

### 2. Validation
Run detected test command; if it fails, confirm with user.

### 3. Requirements Analysis
Break down the feature/PRD:
- Identify user-visible behaviors.
- Choose a smallest slice (first-slice heuristics) for TDD.
- Group behaviors into parent task groups.

### 4. Generate Task List
Create `/tasks/tasks-[feature-name].md` using the template in [TASK_TEMPLATES.md](./TASK_TEMPLATES.md). Each parent group follows TDD quadruplet (write failing test, confirm fail, implement, confirm pass).

### 5. Final Validation
Review tasks for coverage, correctness, and file paths.

## Integration
| Skill | When |
|-------|------|
| **create-prd** | Feeds requirements |
| **estimate-tasks** | After tasks generated |
