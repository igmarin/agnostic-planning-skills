# Skill Architecture — Agnostic Planning Skills

Conventions and structure for every `SKILL.md` in this library.

- **Overview and catalog:** [README](../README.md)
- **Persona chains:** [persona-guide.md](persona-guide.md)
- **Docs index:** [index.md](index.md)

## Directory Structure

```text
agnostic-planning-skills/
├── docs/                    # Documentation
│   ├── architecture.md
│   ├── persona-guide.md
│   ├── calling-skills.md
│   └── reference/
│       ├── skill-catalog.md
│       └── integration-matrix.md
├── skills/                  # Categorized skills and personas
│   ├── prd/                 # PRD creation skills (atomic)
│   │   └── create-prd/
│   ├── task-management/     # Task and ticket skills (atomic)
│   │   ├── generate-tasks/
│   │   └── plan-tickets/
│   ├── requirements-clarifier/ # Analysis skill (atomic)
│   └── personas/            # Role-based orchestrators (persona)
│       └── product-owner/
│           └── SKILL.md
├── bin/                     # Pre-built rs-guard binaries for local review
│   ├── rs-guard-macos-arm64 # macOS arm64 (v1.6.0)
│   ├── rs-guard-linux-x64   # Linux x86_64 (v1.6.0)
│   └── CHECKSUMS.txt        # SHA-256 checksums and provenance
├── hooks/                   # Git hook scripts
│   ├── pre-commit-rs-guard  # Advisory pre-commit review (rs-guard)
│   └── hooks.json           # Hook wiring for agent runtimes
├── SKILL.md                 # Root orchestrator
└── README.md
```

## SKILL.md Structure

Every skill follows this structure:

### 1. YAML Frontmatter (Required)

```yaml
---
name: skill-name
description: >
  Use when [concrete trigger conditions]. Covers [key topics].
  [Additional trigger words for discovery].
---
```

**Rules:**

- `name`: kebab-case, matches directory name
- `description`: starts with "Use when...", third person
- Include concrete trigger words (error symptoms, tools, scenarios)
- Do NOT summarize the workflow (prevents model from skipping the skill body)
- Max 1024 characters total for frontmatter

### 2. Title and Core Principle

```markdown
# Skill Title

Use this skill when [brief trigger].

**Core principle:** [One sentence philosophy]
```

### 3. Quick Reference (High Priority)

A scannable table at the top for fast lookup:

```markdown
## Quick Reference

| Aspect | Rule |
|--------|------|
| ... | ... |
```

### 4. HARD-GATE (Where Applicable)

Non-negotiable blockers in a code block:

```markdown
## HARD-GATE

\```
DO NOT [forbidden action].
ALWAYS [required action].
\```
```

### 5. Core Rules / Process

The main instructions. Use numbered steps for processes, bullet lists for rules.

### 6. Common Mistakes (High Priority)

Table format with "Mistake" and "Reality" columns:

```markdown
## Common Mistakes

| Mistake | Reality |
|---------|---------|
| "Excuse or bad practice" | Why it's wrong and what to do instead |
```

### 7. Red Flags (High Priority)

Bullet list of signals that the skill is being violated:

```markdown
## Red Flags

- Signal that something is wrong
- Another signal
```

### 8. Integration (Medium Priority)

Table of related skills and when to chain them:

```markdown
## Integration

| Skill | When to chain |
|-------|---------------|
| **other-skill** | When [condition] |
```

## Frontmatter Optimization (CSO)

"Claude Search Optimization" — how the description helps AI agents find the right skill:

1. Start with "Use when..." (activation trigger)
2. Include concrete nouns: "controller", "migration", "factory"
3. Include action verbs: "reviewing", "creating", "fixing"
4. Include symptoms: "N+1", "fat model", "flaky tests"
5. Do NOT summarize the workflow (the model will skip reading the body)

**Good:**

```yaml
description: >
  Use when generating a Product Requirements Document, defining feature scope,
  or writing a product spec. Covers goals, user stories, functional requirements,
  success metrics, and open questions.
```

**Bad:**

```yaml
description: >
  This skill creates PRDs by first writing the introduction, then goals, then
  user stories, then requirements, then non-goals, then success metrics.
```

## Skill Types

### Atomic Skills (`type: atomic`)

Single-purpose capabilities. Do one thing well.

- `create-prd` — Product Requirements Documents
- `generate-tasks` — TDD task checklists from PRDs
- `plan-tickets` — Tracker-ready ticket drafts
- `requirements-clarifier` — Transform vague requests into specifications

### Personas (`type: persona`)

Role-based orchestrators that sequence atomic skills with approval gates.

- `product-owner` — Full planning lifecycle: Discovery → PRD → Tasks → Tickets → Sprint
- `delivery-lead` — End-to-end pipeline: Scope → Plan → Prioritize → Sprint → Execute → Retrospect

## Skill Reference Formats

Skills are referenced by three conventions depending on context:

| Context | Format | Example |
|---------|--------|---------|
| `directory.json` | Full path: `skills/<category>/<name>/SKILL.md` | `skills/prd/create-prd/SKILL.md` |
| Persona body (activate calls) | Category-path: `<category>/<name>` | `prd/create-prd` |
| Integration tables | Short name only | `create-prd` |

The category-path format (`<category>/<name>`) drops the `skills/` prefix and the `/SKILL.md` suffix from the full directory.json path. Integration tables use bare names since the surrounding context (which skill file you're in) plus the category taxonomy in the root `SKILL.md` makes disambiguation straightforward.

## Approval Gates

Planning skills use **hard gates** — explicit user approval checkpoints that block progress until confirmed:

### PRD Approval Gate

Defined in: `create-prd`, `product-owner` persona.

Purpose: The PRD must be explicitly approved before any task generation or implementation. This prevents feature work on unapproved scope.

### Ticket Approval Gate

Defined in: `plan-tickets`, `product-owner` persona.

Purpose: Ticket drafts must be reviewed and approved before creating issues in a tracker. Default mode is draft-only.

### Sprint Confirmation Gate

Defined in: `product-owner` persona.

Purpose: Sprint placement must be confirmed by the user. The persona does not assume sprint IDs, capacity, or team availability.

## Platform Compatibility

All skills use standard Markdown and YAML frontmatter, compatible across major AI coding assistants that support skill/plugin loading.
