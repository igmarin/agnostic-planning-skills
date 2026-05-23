# Project Detection Rules

How to auto-detect a project's test command, source directory, test directory, documentation tool, and work type.

## Test Command

Inspect project files and infer the test command:

| File | Test command |
|------|-------------|
| `package.json` with `"scripts": {"test": "..."}` | `npm test` (or `yarn test`, `pnpm test`) |
| `package.json` with `vitest` | `npx vitest` |
| `package.json` with `jest` | `npx jest` |
| `Gemfile` with `rspec` | `bundle exec rspec` |
| `Cargo.toml` | `cargo test` |
| `Makefile` with `test` target | `make test` |
| `pyproject.toml` with `pytest` | `pytest` |
| `go.mod` | `go test ./...` |

Fall back to asking the user if ambiguous.

## Source Directory

Check for the first directory that exists:

1. `src/` — most common (JS/TS, Rust, Go, Python)
2. `lib/` — Ruby gems, some JS
3. `app/` — Rails, some Python frameworks
4. `pkg/` — Go libraries

Ask the user if none of these match.

## Test Directory

Check for the first directory that exists:

1. `__tests__/` — Jest, some JS/TS conventions (mirror or co-located)
2. `spec/` — RSpec, some JS
3. `test/` — Go, Python unittest
4. `tests/` — pytest, Rust integration tests

Also check for mirror convention (test files next to source, e.g., `src/foo.test.ts`).

Ask the user if unclear.

## Documentation Tool

Detect by project type or config:

| Signal | Doc tool |
|--------|----------|
| `package.json` with `jsdoc` or `typedoc` | JSDoc / TypeDoc |
| `Gemfile` with `yard` | YARD |
| `Cargo.toml` | rustdoc |
| `go.mod` | godoc |
| `pyproject.toml` with `sphinx` | Sphinx |

If none detected, default to a generic "document public API" task.

## Work Type

Classify the project:

| Type | Indicators |
|------|------------|
| Web app | Routes, controllers, views, HTML templates |
| CLI tool | `bin/`, CLI argument parsing, no web server |
| Library/SDK | `lib/` or `pkg/` without a server entry point, `exports` in `package.json` |
| API service | REST/GraphQL endpoints, no UI, server entry point |
| Other | None of the above match |

The work type affects which test slice is written first. For web apps and API services, start with the request/API boundary. For libraries and CLI tools, start with the public API boundary.
