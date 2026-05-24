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

- **Task 0.0:** Always create feature branch first
- **Test pattern:** Write test → Run fail → Implement → Run pass (TDD quadruplet)
- **Auto-detect:** Test command, source dir, test dir, doc tool (see [REFERENCE.md](REFERENCE.md) for detection rules)
- **Output:** `/tasks/tasks-[feature-name].md`
- **Validation:** Verify test command works before generating full task list

## Workflow

### Step 1: Project Detection

**CRITICAL RULE:** You MUST explicitly detect and list the project's conventions before generating any tasks (see [REFERENCE.md](REFERENCE.md) for patterns):

1. **Test Command Detection** - Check config files (such as `package.json`, `Gemfile`, `Cargo.toml`, `pyproject.toml`, or `go.mod`) for test scripts and identify the exact test command.
2. **Directory Detection** - Identify the source directory (e.g. `src/`, `lib/`, `app/`, `pkg/`) and test directory (e.g. `__tests__/`, `spec/`, `test/`, `tests/` or co-located tests).
3. **Work Type Classification** - Classify the project's work type (Web app, CLI tool, Library/SDK, API service, or other).
4. **Documentation Tool Detection** - Identify the documentation tool in use (e.g. JSDoc/TypeDoc, YARD, rustdoc, godoc, Sphinx) to include documentation tasks.

### Step 2: Validation Checkpoint

**CRITICAL:** Verify the detected test command works:

```bash
# Run the detected test command
<test-command>

# If it fails, ask user to confirm:
# "Detected test command: <command>. Is this correct?"
```

Only proceed if tests run successfully (even if they fail on specific tests).

### Step 3: Requirements Analysis

Break down the feature/PRD into implementation tasks:

1. **Identify User-Visible Behaviors** - User capabilities, APIs, data flows
2. **Apply First-Slice Heuristics** - Choose test boundary (see [REFERENCE.md](REFERENCE.md))
3. **Create Parent Task Groups** - Group related behaviors with TDD quadruplets

### Step 4: Generate Task List

Create `/tasks/tasks-[feature-name].md` using the template in [TASK_TEMPLATES.md](TASK_TEMPLATES.md).

### Step 5: Final Validation

1. **Review Generated Tasks**
   - Are all user behaviors covered?
   - Is the TDD quadruplet pattern consistent?
   - Are file paths correct for detected directories?

2. **Verify Test Integration**
   - Test command references are correct
   - File paths match project structure
   - Dependencies are accounted for

## Reference Materials

See [REFERENCE.md](REFERENCE.md) for auto-detection patterns and [TASK_TEMPLATES.md](TASK_TEMPLATES.md) for output templates. 