---
name: generate-tasks
license: MIT
description: >
  Breaks a feature into implementation tasks using TDD-based workflow.
  Use when the user wants to break down a feature into implementation tasks,
  create a TDD-based task list, or plan feature implementation steps.
  Always creates a feature branch first (Task 0.0), detects the test command
  from config files, identifies source and test directories, detects
  documentation generation tools, writes test → run fail → implement → run pass
  (TDD quadruplet), verifies the test command before full generation, groups
  user-visible behaviors as parent task groups, saves to /tasks/tasks-[name].md,
  and reviews the generated tasks. Language-agnostic.
  Trigger words: task list, implementation plan, feature breakdown, generate tasks, TDD.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## Quick Reference (Cheat Sheet)

| What | Detail |
|---|---|
| **Branch** | Task 0.0: `git checkout -b feature/[name]` |
| **TDD pattern** | Write test → Run (fail) → Implement → Run (pass) |
| **Output path** | `/tasks/tasks-[feature-name].md` |
| **Auto-detect** | Test command, source dir, test dir, doc tool |
| **Gate** | Test command must pass before full generation |

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

**CRITICAL:** Verify the detected test command works before proceeding. Use this lookup table:

| Config File / Indicator | Detection Command | Test Command |
|---|---|---|
| `package.json` with `test` script | `jq '.scripts.test' package.json` | `npm test` (or `yarn test` / `pnpm test`) |
| `Cargo.toml` | `test -f Cargo.toml` | `cargo test` |
| `Gemfile` + rspec | `grep -q rspec Gemfile` | `bundle exec rspec` |
| `go.mod` | `test -f go.mod` | `go test ./...` |
| `pyproject.toml` + pytest | `grep -q pytest pyproject.toml` | `pytest` |
| `Makefile` with test target | `grep -q '^test:' Makefile` | `make test` |
| Fallback | — | Default test suite for detected language |

Run the detected command. If it fails, ask the user to confirm:
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
