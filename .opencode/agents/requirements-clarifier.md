---
description: >
  Transforms vague or incomplete task descriptions into actionable
  specifications with clear acceptance criteria, user stories, and
  identified edge cases. Read-only — produces requirements, never code.
  Use when a task is ambiguous and needs refinement before implementation.
mode: subagent
prompt: "{file:./skills/requirements-clarifier/SKILL.md}"
permission:
  bash: deny
  edit: deny
  write: deny
  task: deny
---
