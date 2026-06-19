---
name: generate-tasks
type: atomic
license: MIT
description: >
  Breaks a feature into implementation tasks — always create a feature branch
  first (Task 0.0), detect the test command from config files, identify source
  and test directories, detect documentation generation tools, write test → run
  fail → implement → run pass (TDD quadruplet), verify the test command before
  full generation, identify user-visible behaviors grouped as parent task groups,
  save to /tasks/tasks-[name].md, and review the generated tasks.
  Language-agnostic. Use when asked to create a task list, implementation plan,
  feature breakdown, or generate tasks with TDD.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Task List from Requirements

## Quick Reference

- **Task 0.0:** Always create feature branch first
- **Output:** `/tasks/tasks-[feature-name].md`
- **Auto-detect:** Test command, source directory, test directory, and doc tool.
- **Gate:** Test command must pass before full generation

## Workflow

### Step 1: Project Detection

**CRITICAL RULE:** Explicitly detect and list the project's conventions before generating tasks:

1. **Test Command Detection** — Use the lookup table below to resolve the concrete command.
2. **Directory Detection** — Check for common source dirs (`src/`, `lib/`, `app/`) and test dirs (`tests/`, `test/`, `spec/`, `__tests__/`).
3. **Documentation Tool Detection** — Identify the documentation tool by checking `package.json`, `pyproject.toml`, `requirements.txt`, or a `Doxyfile` for references to tools such as `typedoc`, `jsdoc`, `sphinx`, `mkdocs`, or `doxygen`.

### Test Command Lookup Table

| Config File Present | Detected Test Command |
|---|---|
| `package.json` (jest/vitest) | `npm test` or `npx vitest run` |
| `package.json` (mocha) | `npx mocha` |
| `pyproject.toml` / `pytest.ini` | `pytest` |
| `Cargo.toml` | `cargo test` |
| `go.mod` | `go test ./...` |
| `Gemfile` (rspec) | `bundle exec rspec` |
| `build.gradle` / `pom.xml` | `./gradlew test` / `mvn test` |
| `.phpunit.xml` | `vendor/bin/phpunit` |

### Step 2: Validation Checkpoint

**CRITICAL:** Verify the detected test command works before proceeding.

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

Create `/tasks/tasks-[feature-name].md` using the structure below.

#### Task File Template

Each parent group follows the TDD quadruplet: write failing test → confirm fail → implement → confirm pass.

```markdown
# Tasks: [Feature Name]

## Relevant Files
- `src/[module]/[file].[ext]` — [brief description]
- `tests/[module]/[file].test.[ext]` — [brief description]

## Tasks

- [ ] 0.0 Create feature branch `feat/[feature-name]`

- [ ] 1.0 [Parent behavior group]  e.g. `UserService can create a new user`
  - [ ] 1.1 Write failing test for [smallest behavior slice]
         e.g. `def test_create_user_returns_user_with_id()` in `tests/services/test_user_service.py`
  - [ ] 1.2 Run `[test command]` — confirm test 1.1 fails
         e.g. `pytest tests/services/test_user_service.py` → FAILED (AttributeError)
  - [ ] 1.3 Implement [feature code] to make test 1.1 pass
         e.g. `UserService.create()` in `src/services/user_service.py`
  - [ ] 1.4 Run `[test command]` — confirm all tests pass
         e.g. `pytest tests/services/test_user_service.py` → 1 passed

- [ ] 2.0 [Next parent behavior group]
  - [ ] 2.1 Write failing test for ...
  - [ ] 2.2 Run — confirm fail
  - [ ] 2.3 Implement ...
  - [ ] 2.4 Run — confirm pass
```

### Step 5: Final Validation

1. **Review Generated Tasks**
   - Are all user behaviors covered?
   - Is the TDD quadruplet pattern consistent?
   - Are file paths correct for detected directories?

2. **Verify Test Integration**
   - Test command references are correct.
   - File paths match project structure.
