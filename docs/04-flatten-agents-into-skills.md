# Plan 4: Flatten Agents into Skills — agnostic-planning-skills

**Status:** In progress
**Scope:** igmarin/agnostic-planning-skills only (Phase 1 of 3 repos)

## Core Decisions (from grill session)

| Decision | Outcome |
|----------|---------|
| Target directory | `skills/personas/` — not `skills/workflows/` |
| Type field | Explicit `type: atomic` and `type: persona` in frontmatter |
| Requirements-clarifier | New atomic skill at `skills/requirements-clarifier/` (not a persona) |
| Repo-agnostic | requirements-clarifier feeds into product-owner and tech-lead personas |
| OpenCode support | `.opencode/agents/` wrappers with `mode: subagent` + tool restrictions |
| Cross-LLM | Canonical source is `SKILL.md` — `.opencode/agents/` is opencode-specific |
| Persona tooling | Orchestrator personas: allow edit/write, deny bash |
| Persona tooling | Read-only personas: deny edit, write, bash (requirements-clarifier) |
| Future repos | rails-agent-skills → `skills/workflows/`; hanakai-yaku → TBD |
| New roles (future) | architect-designer → ruby-core-skills; test-automation-engineer → ruby-core-skills |

## Vocabulary

| Old Term | New Term | Definition |
|----------|----------|------------|
| Agent | Persona | A role-based workflow (orchestrates atomic skills) |
| Agent directory | `skills/personas/` | Location for persona SKILL.md files |
| Skill | Atomic Skill | Single capability with `type: atomic` |
| Orchestrator | Orchestrating Persona | A persona that chains atomic skills |
| agents.json | (deleted) | Merged into directory.json |
| AGENTS.md | (deleted) | Content merged into CLAUDE.md / GEMINI.md |

---

## PHASE 1 — Add `type: atomic` to existing skills (11 files)

Add `type: atomic` to the YAML frontmatter of every existing atomic skill.

- [x] `SKILL.md` (root) — add `type: catalog`
- [x] `skills/prd/create-prd/SKILL.md` — add `type: atomic`
- [x] `skills/prd/review-prd/SKILL.md` — add `type: atomic`
- [x] `skills/task-management/generate-tasks/SKILL.md` — add `type: atomic`
- [x] `skills/task-management/plan-tickets/SKILL.md` — add `type: atomic`
- [x] `skills/task-management/estimate-tasks/SKILL.md` — add `type: atomic`
- [x] `skills/backlog/prioritize-backlog/SKILL.md` — add `type: atomic`
- [x] `skills/ceremony/plan-sprint/SKILL.md` — add `type: atomic`
- [x] `skills/ceremony/create-retrospective/SKILL.md` — add `type: atomic`
- [x] `skills/execution/generate-status-report/SKILL.md` — add `type: atomic`
- [x] `skills/execution/identify-risks/SKILL.md` — add `type: atomic`

---

## PHASE 2 — Move agents to skills/personas/ (4 files)

- [x] Move `agents/delivery-lead/SKILL.md` → `skills/personas/delivery-lead/SKILL.md`
  - [x] Add `type: persona` to frontmatter
  - [x] Change title from `# Delivery Lead Agent` → `# Delivery Lead Persona`
- [x] Move `agents/product-owner/SKILL.md` → `skills/personas/product-owner/SKILL.md`
  - [x] Add `type: persona` to frontmatter
  - [x] Change title from `# Product Owner Agent` → `# Product Owner Persona`
- [x] Move `agents/project-manager/SKILL.md` → `skills/personas/project-manager/SKILL.md`
  - [x] Add `type: persona` to frontmatter
  - [x] Change title from `# Project Manager Agent` → `# Project Manager Persona`
- [x] Move `agents/tech-lead/SKILL.md` → `skills/personas/tech-lead/SKILL.md`
  - [x] Add `type: persona` to frontmatter
  - [x] Change title from `# Tech Lead Agent` → `# Tech Lead Persona`

---

## PHASE 3 — Create skills/requirements-clarifier/SKILL.md (1 new file)

- [x] Create `skills/requirements-clarifier/SKILL.md`

---

## PHASE 4 — Create `.opencode/agents/` wrappers (5 new files)

- [x] Create `.opencode/agents/delivery-lead.md`
- [x] Create `.opencode/agents/product-owner.md`
- [x] Create `.opencode/agents/project-manager.md`
- [x] Create `.opencode/agents/tech-lead.md`
- [x] Create `.opencode/agents/requirements-clarifier.md`

---

## PHASE 5 — Delete obsolete files (1 dir + 2 files)

- [x] Delete `agents/` directory
- [x] Delete `agents.json`
- [x] Delete `AGENTS.md`

---

## PHASE 6 — Update directory.json (1 file)

- [x] Update `directory.json`

---

## PHASE 7 — Update root SKILL.md (1 file)

- [x] Add `type: catalog` to root SKILL.md frontmatter
- [x] Rename "Agents" section to "Personas"
- [x] Update title references from "Agent" to "Persona"
- [x] Add requirements-clarifier to Quick Reference table
- [x] Update pipeline reference ("4 orchestration agents" → "4 personas")
- [x] Remove references to `agents.json` (now fully in `directory.json`)

---

## PHASE 8 — Update documentation (8 files)

### README.md
- [x] "10 language-agnostic planning skills and 4 orchestration agents" → "11 language-agnostic planning skills and 4 personas"
- [x] "10 planning skills + 4 agents" → "11 planning skills + 4 personas"
- [x] Update "What Is In The Repository" table
- [x] Rename "Agent" sub-table to "Persona"
- [x] Update agent references in body text
- [x] General: replace "agent" with "persona" where appropriate

### CLAUDE.md
- [x] "4 callable agents" → "4 personas"
- [x] Rename agent references
- [x] Update skill table to include requirements-clarifier

### GEMINI.md
- [x] Same changes as CLAUDE.md

### docs/architecture.md
- [x] `agents/` → `skills/personas/`
- [x] Add `type: atomic` and `type: persona` to "Skill Types" section
- [x] Rename "Orchestration Agents" → "Personas"
- [x] Update directory tree

### docs/agent-guide.md
- [x] Rename to `docs/persona-guide.md`
- [x] Replace "Agent" → "Persona" in headers and body
- [x] Update file path references

### docs/calling-skills.md
- [x] "Using Agents" → "Using Personas"
- [x] Add requirements-clarifier to invocation examples

### docs/reference/skill-catalog.md
- [x] "4 orchestration agents" → "4 personas"
- [x] Add requirements-clarifier entry
- [x] Rename "Agents" section to "Personas"
- [x] Update "If You Need..." table
- [x] Update path references from `agents/` → `skills/personas/`

### CHANGELOG.md
- [x] Add version 4.0.0 entry

---

## Summary of Operations

| Action | Files |
|--------|-------|
| Add `type:` field | 11 existing SKILL.md files |
| Move agents → personas (with field updates) | 4 SKILL.md files |
| Create new atomic skill | 1 file |
| Create .opencode/agents wrappers | 5 files |
| Delete obsolete | 1 directory + 2 files |
| Update directory.json | 1 file |
| Update documentation | 8 files |
| **Total** | **~33 file operations** |

## Future Phases (separate battles)

| Repo | When | Target |
|------|------|--------|
| igmarin/rails-agent-skills | After this repo | `skills/workflows/` |
| igmarin/hanakai-yaku | After rails-agent-skills | TBD |
| igmarin/ruby-core-skills | When needed | architect-designer + test-automation-engineer personas |
