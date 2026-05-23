# Generate Tasks Reference

Auto-detection patterns and reference materials for the generate-tasks skill. See SKILL.md for main workflow.

## Test Command Detection

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

### Directory Detection Patterns

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

### Work Type Classification

| Type | Key Indicators |
|------|----------------|
| Web app | Routes, controllers, views, HTML templates |
| CLI tool | `bin/`, CLI argument parsing, no web server |
| Library/SDK | `lib/`/`pkg/` without server entry point, `exports` |
| API service | REST/GraphQL endpoints, no UI, server entry point |

### Documentation Tool Detection

| Signal | Doc tool |
|--------|----------|
| `package.json` with `jsdoc` or `typedoc` | JSDoc / TypeDoc |
| `Gemfile` with `yard` | YARD |
| `Cargo.toml` | rustdoc |
| `go.mod` | godoc |
| `pyproject.toml` with `sphinx` | Sphinx |

## First-Slice Heuristics

Use the smallest slice that proves behavior at the right boundary:

| Change type | Default first slice |
|-------------|---------------------|
| New endpoint or API behavior | Request/integration test -> handler/service wiring -> persistence/docs |
| New service or domain rule | Service or unit test -> implementation -> callers/docs |
| Background work | Job/worker test -> service/domain test if logic is substantial |
| External integration | Client/fetcher layer test -> builder/domain mapping -> callers |
| UI component or page | Component/render test -> component implementation -> integration |
| Library / SDK | Public API test -> implementation -> docs/examples |
| Bug fix | Highest-value reproducing test at the boundary where users feel the bug |

When in doubt, prefer the highest-value failing test that proves the user-visible behavior before descending into lower-level units.
