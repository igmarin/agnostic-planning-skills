---
name: generate-tasks
license: MIT
description: >
  Use when breaking down a feature or generating an implementation task list from a PRD.
  Output MUST follow this exact structure: (1) Task 0.0: Create feature branch with git
  checkout command, (2) Relevant Files section listing all files with concrete paths,
  (3) TDD task groups with four sub-tasks each: X.Xa Write test, X.Xb Run test
  and verify it FAILS, X.Xc Implement, X.Xd Run test and verify it PASSES, (4) Documentation
  task, (5) Documentation update task for README/diagrams, (6) Code review gate,
  (7) Save as tasks-[name].md in /tasks/ folder. Language-agnostic — auto-detects test
  commands, source directories, and documentation conventions from the project.
  Trigger words: task list, implementation plan, feature breakdown, todo list, project
  tasks, work plan, break down this PRD, generate tasks, feature branch, TDD.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## Quick Reference

- **Task 0.0:** Always "Create feature branch".
- **Tasks format:** Each sub-task must be single action (2-5 mins).
- **Paths:** Use exact file paths from the project.
- **TDD:** Write test -> Run fail -> Implement -> Run pass.
- **Auto-detect:** Infer test command, source dir, and doc tool from project files.

## HARD-GATE

```text
DO NOT skip Task 0.0 (Create feature branch) unless the user explicitly overrides.
DO NOT use vague references instead of exact file paths.
DO NOT summarize the task list in a table instead of producing the actual checklist artifact.
DO NOT combine the TDD quadruplet sub-tasks into a single task. They must be broken out:
  a) Write test
  b) Run test (verify fails)
  c) Implement
  d) Run test (verify passes)
Each c-step is one implementation action in one primary file. Split endpoint,
service, data layer, UI component, and integration work into separate
quadruplets or separate follow-up tasks.
```

## Core Process

1. **Analyze:** Extract Functional Requirements and Goals from the PRD, or use the feature description. Identify scope and main work areas.
2. **Detect project context:** Auto-detect the project's conventions by inspecting project files:
   - **Test command:** Inspect project files (e.g., `package.json` scripts, `Gemfile`, `Cargo.toml`, `Makefile`, `pyproject.toml`, `go.mod`). Infer the test command (`npm test`, `bundle exec rspec`, `cargo test`, `pytest`, `go test`, etc.). Fall back to asking the user if ambiguous.
   - **Source directory:** Check for `src/`, `lib/`, `app/`, `pkg/`, or project-specific conventions. Ask the user if unclear.
   - **Test directory:** Check for `__tests__/`, `spec/`, `test/`, `tests/`, or mirror convention. Ask the user if unclear.
   - **Documentation tool:** Detect JSDoc, YARD, Sphinx, rustdoc, godoc, etc. If none detected, default to a generic "document public API" task.
   - **Work type:** Classify as web app, CLI tool, library/SDK, API service, or other. This affects slice ordering.
3. **Determine Output Mode:**
   - If the user asks for strategy, sequencing, phases, or approach, produce a phased plan first.
   - If the user asks for implementation tasks, checklist, or exact steps, produce the detailed mode.
4. **Draft Relevant Files Section:** List all files to create or modify including tests, docs, and diagrams. Include the detected test command.
5. **Draft Tasks:** Construct the sequential task list incorporating TDD task groups (write test, run fail, implement, run pass), followed by documentation, README/docs updates, and a code review gate. Use at least 1 TDD group per distinct work area — 3+ if the feature spans multiple concerns (endpoint, service, UI, data layer). Each TDD implementation sub-task line must name the exact file path using the detected source and test directories.
6. **Save:** Save the output as `tasks-[feature-name].md` in `/tasks/`. Use the same `[feature-name]` as the PRD if one was provided.
7. **Verify Checkpoint:** Re-read the saved file and confirm all required elements from the Output Style are present.
8. **Final Artifact:** Include the full `tasks-[feature-name].md` checklist content in the response; do not only describe the file or summarize it in a table.

## Extended Resources (Progressive Disclosure)

Load these files only when their specific guidance is required:

- **[HEURISTICS.md](./HEURISTICS.md)** — Use when deciding the first test to write for a given change type (endpoint, service, job, library, bug fix).
- **[TASK_TEMPLATES.md](./TASK_TEMPLATES.md)** — Use when you need the full template structure for phased plans or detailed checklists.

## Output Style

When asked to generate tasks, your output MUST include:

0. **Full checklist artifact** — Include the concrete `tasks-[feature-name].md` content, not a summary table about the file.
1. **Task 0.0** — "Create feature branch" with checkout command (e.g., `git checkout -b feature/name`).
2. **Relevant Files section** — All files to create/modify with concrete paths, listed before Tasks.
3. **TDD quadruplets** — At least 1 implementation group per work area (3+ if the feature spans multiple concerns), four sub-tasks each:
   - `X.Xa` Write test for `[behavior]` at `<test-file-path>`
   - `X.Xb` Run `<test-command>` — verify it **fails**
   - `X.Xc` Implement `[behavior]` at `<source-file-path>`
   - `X.Xd` Run `<test-command>` — verify it **passes**
   Every `a/b/c/d` line must include the concrete file path or command path for that slice.
4. **Documentation task** — Add docs to new/changed public API; name each file and the detected documentation tool.
5. **Documentation update task** — Update README, diagrams (Mermaid, ADRs), domain docs; list concrete paths.
6. **Code review gate** — Self-review; fix blockers before opening PR.
7. **Save location** — State that it was saved to `tasks-[feature-name].md` in `/tasks/` folder.
8. **Guidance Used** — Add a section with this exact heading. State whether `HEURISTICS.md` and/or `TASK_TEMPLATES.md` were used, and why.
9. **Instructions for Completing Tasks** — Add a section with this exact heading. Tell the implementer to work one sub-task at a time, verify RED before implementation and GREEN after, and avoid combining actions.
10. **Language** — Must be in English unless explicitly requested otherwise.

For endpoint work, the first TDD quadruplet should normally be the request/API-boundary test slice. Add service or data-layer slices after the boundary is established unless the PRD is explicitly persistence-only.

## Integration

| Skill | When to chain |
| **create-prd** | Generate PRD first, then derive tasks from it |
| **plan-tickets** | When the same initiative also needs ticket drafts |
