# Skill Catalog — Agnostic Planning Skills

Complete catalog of 3 language-agnostic planning skills and 1 orchestration agent.

---

## Quick Navigation

**Skills:** [create-prd](#create-prd) · [generate-tasks](#generate-tasks) · [plan-tickets](#plan-tickets)
**Agents:** [product-owner](#product-owner-agent)

---

## Skills

### create-prd

| Path | `skills/prd/create-prd/SKILL.md` |
| Category | PRD |
| Description | Generate a Product Requirements Document from a feature description |
| Trigger Words | "PRD", "product requirements", "plan a feature", "write a spec", "requirements document" |

**What it does:** Drafts a structured PRD in Markdown following `PRD_TEMPLATE.md`. Covers goals, user stories, functional requirements, non-goals, design and technical considerations, implementation surface, success metrics, and open questions.

**HARD-GATE:** Focus exclusively on WHAT and WHY, not HOW. No code until PRD is approved.

**Next after use:** `generate-tasks` (to break PRD into implementation tasks) or `plan-tickets` (for tracker-ready tickets).

---

### generate-tasks

| Path | `skills/task-management/generate-tasks/SKILL.md` |
| Category | Task Management |
| Description | Break a feature into TDD implementation tasks with exact file paths |
| Trigger Words | "task list", "implementation plan", "feature breakdown", "break down this PRD", "generate tasks" |

**What it does:** Converts a PRD or feature description into a sequential task checklist with TDD quadruplets (write test → run fail → implement → run pass). Auto-detects test commands, source directories, and documentation conventions from the project.

**HARD-GATE:** Do not skip Task 0.0 (Create feature branch). Do not combine the TDD quadruplet sub-tasks into a single task.

**Next after use:** Begin implementation of the first task group, or chain to `plan-tickets` for ticket generation.

---

### plan-tickets

| Path | `skills/task-management/plan-tickets/SKILL.md` |
| Category | Task Management |
| Description | Draft tracker-ready tickets from an initiative plan with classification |
| Trigger Words | "create tickets", "Jira", "Linear", "GitHub Issues", "sprint planning" |

**What it does:** Classifies work items by type, area, execution order, and dependency level. Drafts tickets with title conventions (`BE |`, `FE |`, `Mobile |`) and a standard five-section structure (Summary, Background, Acceptance Criteria, Dependencies, Technical Notes).

**HARD-GATE:** Do not create tracker issues unless the user explicitly asks for creation. Default is draft-only.

**Next after use:** Continue to sprint placement or begin implementation.

---

## Agents

### product-owner Agent

| Path | `agents/product-owner/SKILL.md` |
| Description | Full planning lifecycle with approval gates |

**Phases:**
1. **Discovery & Clarification** — Scope the feature and gather requirements
2. **PRD Draft** — Generate the Product Requirements Document
3. **Review & Revise** — Iterate on feedback until approved
4. **Task Estimation** — Break approved PRD into TDD tasks
5. **Ticket Generation** — Convert tasks into tracker-ready tickets
6. **Sprint Placement** — Order tickets by dependency and sprint readiness

**Hard Gates:** PRD Approval, Ticket Approval, Sprint Confirmation

**Dependencies:** `create-prd`, `generate-tasks`, `plan-tickets`

---

## If You Need...

| You need... | Recommended Skill(s) |
| **Write a PRD** | `create-prd` |
| **Break down a feature** | `create-prd` → `generate-tasks` |
| **Generate tickets** | `plan-tickets` |
| **End-to-end planning** | `product-owner` agent |
| **Sprint-ready backlog** | `product-owner` agent |

---

## See Also

- [Integration Matrix](integration-matrix.md) — How skills chain together
- [Agent Guide](../agent-guide.md) — Agent workflow details with Mermaid diagrams
- [Architecture](../architecture.md) — Repository layout and conventions
