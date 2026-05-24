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
- **Auto-detect:** Test command, source directory, test directory, and doc tool.
- **Output:** `/tasks/tasks-[feature-name].md`
- **Validation:** Verify test command works before generating full task list.

## Workflow

### Step 1: Project Detection

**CRITICAL RULE:** Explicitly detect and list the project's conventions before generating tasks:

1. **Test Command Detection** - Check config files to identify the exact test command.
2. **Directory Detection** - Identify the source directory and test directory.
3. **Work Type Classification** - Classify the project (Web app, CLI, library, API, etc.).
4. **Documentation Tool Detection** - Identify the documentation tool in use.

### Step 2: Validation Checkpoint

**CRITICAL:** Verify the detected test command works before proceeding:
- If `package.json` exists with a `test` script, run `npm test` (or `yarn test`/`pnpm test`).
- If `Cargo.toml` exists, run `cargo test`.
- If `Gemfile` exists with `rspec`, run `bundle exec rspec`.
- If `go.mod` exists, run `go test ./...`.
- If `pyproject.toml` exists with `pytest`, run `pytest`.
- If `Makefile` exists with a `test` target, run `make test`.
- Otherwise, run the default test suite command for the detected language/framework.

If the command fails, ask the user to confirm:
_"Detected test command: [command]. Is this correct?"_
Only proceed if tests execute successfully.

### Step 3: Requirements Analysis

Break down the feature/PRD into implementation tasks:

1. **Identify User-Visible Behaviors** - Capabilities, APIs, and data flows.
2. **Apply First-Slice Heuristics** - Choose the smallest slice that proves behavior at the correct boundary:
   - **Web App / API Service**: Start with a request/integration test.
   - **Service / Domain logic**: Start with a service or unit test.
   - **Background Job**: Start with a job/worker test.
   - **External Integration**: Start with a client/fetcher layer test.
   - **Library / SDK**: Start with a public API test.
3. **Create Parent Task Groups** - Group related behaviors with TDD quadruplets.

### Step 4: Generate Task List

Create `/tasks/tasks-[feature-name].md` using the template below.

### Step 5: Final Validation

1. **Review Generated Tasks**
   - Are all user behaviors covered?
   - Is the TDD quadruplet pattern consistent?
   - Are file paths correct for detected directories?

2. **Verify Test Integration**
   - Test command references are correct.
   - File paths match project structure.

### Task List Template Example

Create `/tasks/tasks-[feature-name].md` following this structure:

```markdown
# Task List: [Feature Name]

Based on: `prd-[feature-name].md`

## Relevant Files

- `path/to/file.ext` - Description of relevance.
- `path/to/file.test.ext` - Test coverage.

## Tasks

- [ ] 0.0 Create feature branch: `git checkout -b feature/[feature-name]`
- [ ] 1.0 Core Behavior (TDD Quadruplet)
  - [ ] 1.1a Write failing test for [behavior] (`<test-dir>/path/to/test.ext`)
  - [ ] 1.1b Run test command — verify failure
  - [ ] 1.1c Implement behavior to pass test (`<source-dir>/path/to/file.ext`)
  - [ ] 1.1d Run test command — verify success
- [ ] 2.0 API Documentation & Code Review
  - [ ] 2.1 Document public API methods
  - [ ] 2.2 Self-review diff before PR
``` 