# Task List Templates

## Detailed Checklist

```markdown
# Task List: [Feature Name]

Based on: `prd-[feature-name].md` *(only if PRD was the source)*

## Relevant Files

- `path/to/file1.ext` - Why this file is relevant.
- `path/to/file1.test.ext` (or `.spec.ext`) - Tests for file1.
- `path/to/file2.ext` - Why this file is relevant.

### Notes

- Tests live next to or mirror the code they cover.
- Run tests: `<test-command>` *(auto-detected from project — e.g. `npm test`, `bundle exec rspec`, `cargo test`, `pytest`)*
- After green tests: document public API, update README/diagrams/docs as needed, then self code review before PR.

## Instructions for Completing Tasks

Check off each task when done: change `- [ ]` to `- [x]`. Update the file after each sub-task, not only after a full parent task.

## Tasks

- [ ] 0.0 Create feature branch: `git checkout -b feature/[feature-name]`
- [ ] 1.0 Request/API boundary *(use this first for new endpoints; replace with the correct first boundary for non-endpoint work)*
  - [ ] 1.1a Write test for [user-visible behavior] (`<test-dir>/path/to/test.ext`)
  - [ ] 1.1b Run `<test-command>` — verify it fails (feature does not exist yet)
  - [ ] 1.1c Implement the smallest handler/route/service wiring needed for [behavior] (`<source-dir>/path/to/handler.ext`, `<source-dir>/path/to/service.ext`)
  - [ ] 1.1d Run `<test-command>` — verify it passes
- [ ] 2.0 [Parent task title]
  - [ ] 2.1a Write test for [behavior] (`<test-dir>/path/to/test.ext`)
  - [ ] 2.1b Run `<test-command>` — verify it fails (feature does not exist yet)
  - [ ] 2.1c Implement [behavior] to pass test (`<source-dir>/path/to/file.ext`)
  - [ ] 2.1d Run `<test-command>` — verify it passes and no other tests break
- [ ] 3.0 [Parent task title]
  - [ ] 3.1a Write test for [behavior] (`<test-dir>/path/to/test.ext`)
  - [ ] 3.1b Run `<test-command>` — verify it fails (feature does not exist yet)
  - [ ] 3.1c Implement [behavior] to pass test (`<source-dir>/path/to/file.ext`)
  - [ ] 3.1d Run `<test-command>` — verify it passes
- [ ] 4.0 Public API documentation
  - [ ] 4.1 Add docs to new/changed public classes, functions, and methods (`<source-dir>/path/to/file.ext`) — English only
  - [ ] 4.2 Run project documentation tool if applicable — fix warnings on touched files
- [ ] 5.0 Update documentation artifacts
  - [ ] 5.1 Update README or module README if behavior or setup changed (`README.md` or `docs/...`)
  - [ ] 5.2 Update diagrams or architecture docs if flows or boundaries changed (`docs/...`, ADRs)
- [ ] 6.0 Code review before merge
  - [ ] 6.1 Self-review full diff; fix Critical/Suggestion items
  - [ ] 6.2 Security/architecture pass if scope warrants
  - [ ] 6.3 Open PR or request review — attach summary of doc updates

## Guidance Used

- `HEURISTICS.md`: [used/not used] — [why this work type did or did not need ordering guidance]
- `TASK_TEMPLATES.md`: used — this file provides the required output structure
```

## Phased Plan

```markdown
# Implementation Plan: [Feature Name]

Based on: `prd-[feature-name].md` *(only if PRD was the source)*

## Work Type

- Web app / CLI tool / Library-SDK / API service / Other

## Phases

### Phase 1: [Goal]
- Target behavior:
- First failing test:
- Likely files:
- Dependencies / decisions:

### Phase 2: [Goal]
- Target behavior:
- First failing test:
- Likely files:
- Dependencies / decisions:

## Completion

- Public API documentation
- README / diagrams / docs updates
- Self-review
```
