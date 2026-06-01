---
description: >
  Orchestrates the full delivery pipeline from feature idea through execution
  to retrospective. Chains all 10 planning skills through six phases with
  approval gates. Use when a feature needs the complete end-to-end workflow.
mode: subagent
prompt: "{file:./skills/personas/delivery-lead/SKILL.md}"
permission:
  # Orchestrates skills as a subagent: allows file writes (PRDs, tasks, reports)
  # but denies arbitrary shell execution. Task delegation to other subagents allowed.
  bash: deny
  edit: allow
  write: allow
  task: allow
---
