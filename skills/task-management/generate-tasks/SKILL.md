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
- **Auto-detect:** Test command, source dir, test dir, doc tool
- **Output:** `/tasks/tasks-[feature-name].md`
- **Validation:** Verify test command works before generating full task list

## Workflow

### Step 1: Project Detection

Auto-detect project conventions by examining project files:

1. **Test Command Detection**
   - Check `package.json` for npm/yarn/pnpm scripts
   - Look for `vitest`, `jest`, `pytest`, `rspec`, `cargo test`, `go test`
   - Fall back to `Makefile` or ask user

2. **Directory Detection**
   - Source: `src/` → `lib/` → `app/` → `pkg/`
   - Test: `__tests__/` → `spec/` → `test/` → `tests/` or mirror convention

3. **Work Type Classification**
   - Web app, CLI tool, Library/SDK, API service, or Other
   - Determines which test boundary to start with

4. **Documentation Tool Detection**
   - JSDoc/TypeDoc, YARD, rustdoc, godoc, Sphinx, or generic

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

1. **Identify User-Visible Behaviors**
   - What should users be able to do?
   - What APIs/endpoints are exposed?
   - What data flows exist?

2. **Apply First-Slice Heuristics**
   - New endpoints: Start with request/integration test
   - Services: Start with service/unit test
   - Background work: Start with job/worker test
   - External integrations: Start with client/fetcher test
   - UI components: Start with component/render test
   - Libraries: Start with public API test
   - Bug fixes: Start with reproducing test at user boundary

3. **Create Parent Task Groups**
   - Group related behaviors (e.g., "User authentication", "Data processing")
   - Each parent task contains 1+ TDD quadruplets

### Step 4: Generate Task List

Create `/tasks/tasks-[feature-name].md` using the detailed checklist template:

```markdown
# Task List: [Feature Name]

## Relevant Files
- List key files that will be modified
- Include test file paths

### Notes
- Tests live next to or mirror the code they cover
- Run tests: <detected-test-command>
- After green tests: document public API, update README/diagrams/docs

## Tasks
- [ ] 0.0 Create feature branch
- [ ] 1.0 [First boundary task]
  - [ ] 1.1a Write test for [behavior]
  - [ ] 1.1b Run <test-command> — verify it fails
  - [ ] 1.1c Implement [behavior]
  - [ ] 1.1d Run <test-command> — verify it passes
- [ ] 2.0 [Next parent task]
  - [ ] 2.1a Write test for [behavior]
  - [ ] 2.1b Run <test-command> — verify it fails
  - [ ] 2.1c Implement [behavior]
  - [ ] 2.1d Run <test-command> — verify it passes
- [ ] 3.0 Public API documentation
- [ ] 4.0 Update documentation artifacts
- [ ] 5.0 Code review before merge
```

### Step 5: Final Validation

1. **Review Generated Tasks**
   - Are all user behaviors covered?
   - Is the TDD quadruplet pattern consistent?
   - Are file paths correct for detected directories?

2. **Verify Test Integration**
   - Test command references are correct
   - File paths match project structure
   - Dependencies are accounted for

## Auto-Detection Quick Reference

### Test Commands by Project Type

| Project File | Test Command | Detection Pattern |
|--------------|--------------|-------------------|
| `package.json` | `npm test` | `"scripts": {"test": "..."}` |
| `package.json` | `npx vitest` | `vitest` in devDependencies |
| `package.json` | `npx jest` | `jest` in devDependencies |
| `Gemfile` | `bundle exec rspec` | `rspec` gem present |
| `Cargo.toml` | `cargo test` | Rust project detected |
| `pyproject.toml` | `pytest` | `pytest` in dependencies |
| `go.mod` | `go test ./...` | Go module detected |
| `Makefile` | `make test` | `test:` target exists |

### Directory Patterns

| Purpose | Priority | Pattern |
|---------|----------|---------|
| Source | 1 | `src/` |
| Source | 2 | `lib/` |
| Source | 3 | `app/` |
| Source | 4 | `pkg/` |
| Tests | 1 | `__tests__/` |
| Tests | 2 | `spec/` |
| Tests | 3 | `test/` |
| Tests | 4 | `tests/` |
| Tests | 5 | Mirror (`.test.ts`, `.spec.rb`, etc.) |

### Work Type Indicators

| Type | Key Indicators |
|------|----------------|
| Web app | Routes, controllers, views, HTML templates |
| CLI tool | `bin/`, CLI argument parsing, no web server |
| Library/SDK | `lib/`/`pkg/` without server entry point, `exports` |
| API service | REST/GraphQL endpoints, no UI, server entry point |

## Example Output

See `TASK_TEMPLATES.md` for complete template examples. A typical task list for a "user authentication" feature in a Node.js web app would generate:

```markdown
# Task List: user-authentication

## Relevant Files
- `src/routes/auth.js` - Authentication routes
- `src/services/auth.js` - Authentication business logic
- `src/middleware/auth.js` - Auth middleware
- `__tests__/routes/auth.test.js` - Route tests
- `__tests__/services/auth.test.js` - Service tests

### Notes
- Tests live next to or mirror the code they cover
- Run tests: `npm test`
- After green tests: document public API, update README/diagrams/docs

## Tasks
- [ ] 0.0 Create feature branch: `git checkout -b feature/user-authentication`
- [ ] 1.0 Login endpoint
  - [ ] 1.1a Write test for POST /auth/login with valid credentials
  - [ ] 1.1b Run `npm test` — verify it fails
  - [ ] 1.1c Implement login route and service
  - [ ] 1.1d Run `npm test` — verify it passes
- [ ] 2.0 Token validation
  - [ ] 2.1a Write test for JWT token validation middleware
  - [ ] 2.1b Run `npm test` — verify it fails
  - [ ] 2.1c Implement token validation middleware
  - [ ] 2.1d Run `npm test` — verify it passes
- [ ] 3.0 Public API documentation
- [ ] 4.0 Update documentation artifacts
- [ ] 5.0 Code review before merge
``` 