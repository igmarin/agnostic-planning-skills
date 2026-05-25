---
name: generate-tasks
license: MIT
description: >
  Breaks a feature into implementation tasks — always create a feature branch
  first (Task 0.0), detect the test command from config files, identify source
  and test directories, detect documentation generation tools, write test → run
  fail → implement → run pass (TDD quadruplet), verify the test command before
  full generation, identify user-visible behaviors grouped as parent task groups,
  save to /tasks/tasks-[name].md, and review the generated tasks.
  Language-agnostic.
  Trigger words: task list, implementation plan, feature breakdown, generate tasks, TDD.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## Quick Reference

- **Task 0.0:** Always create feature branch first
- **Test pattern:** Write test → Run fail → Implement → Run pass (TDD quadruplet)
- **Output:** `/tasks/tasks-[feature-name].md`
- **Auto-detect:** Test command, source directory, test directory, and doc tool.
- **Gate:** Test command must pass before full generation

## Workflow

### Step 1: Project Detection

**CRITICAL RULE:** Explicitly detect and list the project's conventions before generating tasks:

1. **Test Command Detection** — Use the lookup table in Step 2 with the concrete commands below.
2. **Directory Detection** — Identify source and test directories:
   ```bash
   # Source dir candidates
   ls -d src/ lib/ app/ 2>/dev/null | head -1
   # Test dir candidates
   ls -d tests/ test/ spec/ __tests__/ 2>/dev/null | head -1
   ```
3. **Documentation Tool Detection** — Identify the documentation tool in use:
   ```bash
   # Check for common doc tools
   grep -q 'typedoc\|jsdoc' package.json 2>/dev/null && echo typedoc
   grep -q 'sphinx\|mkdocs' pyproject.toml requirements.txt 2>/dev/null && echo sphinx/mkdocs
   ls Doxyfile rustdoc 2>/dev/null
   ```

### Step 2: Validation Checkpoint

**CRITICAL:** Verify the detected test command works before proceeding. Use the [TEST_COMMANDS.md](./TEST_COMMANDS.md) lookup table.

Run the detected command. If it fails, ask the user to confirm:
_"Detected test command: [command]. Is this correct?"_
Only proceed if tests execute successfully.

### Step 3: Requirements Analysis

Break down the feature/PRD into implementation tasks:

1. **Identify User-Visible Behaviors**
2. **Apply First-Slice Heuristics** — Choose the smallest slice that proves behavior:

   | Project Type | First Slice |
   |---|---|
   | Web App / API Service | Request/integration test |
   | Service / Domain logic | Service or unit test |
   | Background Job | Job/worker test |
   | External Integration | Client/fetcher layer test |
   | Library / SDK | Public API test |
3. **Create Parent Task Groups** — Group related behaviors with TDD quadruplets.

### Step 4: Generate Task List

Create `/tasks/tasks-[feature-name].md` using the [TASK_TEMPLATES.md](./TASK_TEMPLATES.md) template.

### Step 5: Final Validation

1. **Review Generated Tasks**
   - Are all user behaviors covered?
   - Is the TDD quadruplet pattern consistent?
   - Are file paths correct for detected directories?

2. **Verify Test Integration**
   - Test command references are correct.
   - File paths match project structure.
