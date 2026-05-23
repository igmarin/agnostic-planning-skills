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

- **Task 0.0:** Always 