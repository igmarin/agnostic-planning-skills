# Skill Catalog — Agnostic Planning Skills

Complete catalog of 12 language-agnostic planning skills and 4 personas.

---

## Quick Navigation

**Skills:** [create-prd](#create-prd) · [review-prd](#review-prd) · [requirements-clarifier](#requirements-clarifier) · [generate-tasks](#generate-tasks) · [plan-tickets](#plan-tickets) · [estimate-tasks](#estimate-tasks) · [prioritize-backlog](#prioritize-backlog) · [plan-sprint](#plan-sprint) · [create-retrospective](#create-retrospective) · [identify-risks](#identify-risks) · [generate-status-report](#generate-status-report) · [github-issue](#github-issue)
**Personas:** [product-owner](#product-owner-persona) · [project-manager](#project-manager-persona) · [tech-lead](#tech-lead-persona) · [delivery-lead](#delivery-lead-persona)

---

## Skills

### create-prd

| Path | `skills/prd/create-prd/SKILL.md` |
| Category | PRD |
| Description | Generate a Product Requirements Document from a feature description |
| Trigger Words | "PRD", "product requirements", "plan a feature", "write a spec", "requirements document" |

**What it does:** Drafts a structured PRD in Markdown following `PRD_TEMPLATE.md`. Covers goals, user stories, functional requirements, non-goals, design and technical considerations, implementation surface, success metrics, and open questions.

**HARD-GATE:** Focus exclusively on WHAT and WHY, not HOW. No code until PRD is approved.

**Next after use:** `review-prd` (to validate quality), `generate-tasks` (to break PRD into implementation tasks) or `plan-tickets` (for tracker-ready tickets).

---

### review-prd

| Path | `skills/prd/review-prd/SKILL.md` |
| Category | PRD |
| Description | Review a PRD for completeness, testability, clarity, and feasibility |
| Trigger Words | "review PRD", "PRD review", "check requirements", "validate PRD", "feasibility check" |

**What it does:** Systematically evaluates a PRD against a quality checklist. Produces findings categorized as Critical, Suggestion, or Note. Checks completeness, testability, ambiguity, feasibility, edge cases, and dependency clarity.

**HARD-GATE:** Every finding must cite specific PRD evidence. Do not review the idea — review the document's quality.

**Next after use:** `generate-tasks` (if approved), or return to `create-prd` for revisions.

---

### generate-tasks

| Path | `skills/task-management/generate-tasks/SKILL.md` |
| Category | Task Management |
| Description | Break a feature into TDD implementation tasks with exact file paths |
| Trigger Words | "task list", "implementation plan", "feature breakdown", "break down this PRD", "generate tasks" |

**What it does:** Converts a PRD or feature description into a sequential task checklist with TDD quadruplets. Auto-detects test commands, source directories, and documentation conventions.

**HARD-GATE:** Do not skip Task 0.0 (Create feature branch). Do not combine TDD sub-tasks into a single task.

**Next after use:** `estimate-tasks` (to assign effort), `plan-tickets` (for ticket generation), or begin implementation.

---

### requirements-clarifier

| Path | `skills/analysis/requirements-clarifier/SKILL.md` |
| Category | Analysis |
| Description | Transform vague requests into actionable specifications |
| Trigger Words | "clarify", "requirements", "spec", "define", "scope this", "refine", "unclear task" |

**What it does:** Takes an ambiguous or incomplete task description and produces clarified requirements with user stories, acceptance criteria, identified edge cases, and open questions. Never produces code.

**HARD-GATE:** Output requirements only. No implementation code, configuration, or test cases.

**Next after use:** `create-prd` (to draft a PRD from clarified requirements), or use `generate-tasks` to break into implementation tasks.

---

### plan-tickets

| Path | `skills/task-management/plan-tickets/SKILL.md` |
| Category | Task Management |
| Description | Draft tracker-ready tickets from an initiative plan with classification |
| Trigger Words | "create tickets", "Jira", "Linear", "GitHub Issues", "sprint planning" |

**What it does:** Classifies work items by type, area, execution order, and dependency level. Drafts tickets with title conventions and a standard five-section structure.

**HARD-GATE:** Do not create tracker issues unless the user explicitly asks. Default is draft-only.

**Next after use:** Sprint placement or begin implementation.

---

### estimate-tasks

| Path | `skills/task-management/estimate-tasks/SKILL.md` |
| Category | Task Management |
| Description | Assign effort estimates with confidence levels |
| Trigger Words | "estimate", "story points", "t-shirt size", "effort", "how long", "sizing" |

**What it does:** Assigns effort estimates using story points (Fibonacci), t-shirt sizes, or time ranges. Flags high-uncertainty items and recommends spikes or further breakdown.

**HARD-GATE:** Do not assign estimates to tasks you do not understand. State confidence for every estimate.

**Next after use:** `identify-risks` (to assess dependency and uncertainty risks) or `plan-sprint` (to select tickets based on capacity).

---

### prioritize-backlog

| Path | `skills/backlog/prioritize-backlog/SKILL.md` |
| Category | Backlog |
| Description | Rank backlog items using a prioritization framework |
| Trigger Words | "prioritize", "backlog", "RICE", "MoSCoW", "value vs effort", "ranking", "WSJF" |

**What it does:** Ranks tickets, tasks, or features using RICE, MoSCoW, value-vs-effort, or WSJF. Produces an ordered backlog with scores and rationale.

**HARD-GATE:** Do not prioritize without understanding each item. State criteria for every score.

**Next after use:** `plan-sprint` (use ordered backlog to select sprint candidates).

---

### plan-sprint

| Path | `skills/ceremony/plan-sprint/SKILL.md` |
| Category | Ceremony |
| Description | Plan a sprint: select tickets, define goal, allocate capacity |
| Trigger Words | "plan sprint", "sprint planning", "sprint goal", "sprint capacity", "sprint backlog" |

**What it does:** Selects tickets from a prioritized backlog based on team capacity and velocity. Defines a sprint goal and produces a sprint plan with capacity allocation.

**HARD-GATE:** Do not commit more than the team's historical velocity. Define a single clear sprint goal.

**Next after use:** Begin sprint execution. Use `identify-risks` to scan the sprint plan for risks.

---

### create-retrospective

| Path | `skills/ceremony/create-retrospective/SKILL.md` |
| Category | Ceremony |
| Description | Generate sprint retrospectives with action items |
| Trigger Words | "retrospective", "retro", "sprint review", "what went well", "lessons learned" |

**What it does:** Generates a structured retrospective from sprint data and team feedback. Covers what went well, what didn't, action items, metrics, and kudos.

**HARD-GATE:** Every "what didn't" must have an action item with owner and timeline.

**Next after use:** Feed action items into execution tracking or the next sprint plan.

---

### identify-risks

| Path | `skills/execution/identify-risks/SKILL.md` |
| Category | Execution |
| Description | Scan plans for risks, dependencies, and blockers |
| Trigger Words | "risks", "risk assessment", "blockers", "what could go wrong", "risk register" |

**What it does:** Scans task lists and PRDs for dependency chains, external dependencies, ambiguous requirements, single points of failure, capacity concerns, and technical uncertainty. Produces a risk register with likelihood, impact, and mitigation.

**HARD-GATE:** Every risk must reference specific evidence. Do not fabricate risks.

**Next after use:** `generate-status-report` (include risks in status update).

---

### generate-status-report

| Path | `skills/execution/generate-status-report/SKILL.md` |
| Category | Execution |
| Description | Generate structured stakeholder status reports |
| Trigger Words | "status report", "sprint update", "stakeholder update", "progress report", "project status" |

**What it does:** Produces a structured status report following a standard template: Executive Summary, Accomplishments, In Progress, Blocked, Risks, Next Steps.

**HARD-GATE:** Do not fabricate progress. Mark unknown items as "needs update." Do not hide blockers.

**Next after use:** Continue tracking or begin next sprint planning cycle.

---

### github-issue

| Path | `skills/infrastructure/github-issue/SKILL.md` |
| Category | Infrastructure |
| Description | Create, track, and manage GitHub issues with project board integration |
| Trigger Words | "create a ticket", "track this work", "GitHub issue", "move this to done", "create an issue" |

**What it does:** Creates well-structured GitHub issues with proper labels, descriptions, and acceptance criteria. Manages issue lifecycle through stages (todo → in-progress → in-review → done) with automatic project board integration and milestone tracking.

**HARD-GATE:** Always validate issue drafts with the user before creating. Never create tracker issues without explicit approval.

**Next after use:** Continue tracking or use `generate-status-report` for stakeholder updates.

---

## Personas

### product-owner Persona

| Path | `skills/personas/product-owner/SKILL.md` |
| Description | Full planning lifecycle with approval gates |

**Phases:** Discovery → PRD Draft → Review & Revise → Task Estimation → Ticket Generation → Sprint Placement

**Hard Gates:** PRD Approval, Ticket Approval, Sprint Confirmation

**Dependencies:** `requirements-clarifier`, `create-prd`, `generate-tasks`, `plan-tickets`

---

### project-manager Persona

| Path | `skills/personas/project-manager/SKILL.md` |
| Description | Execution tracking lifecycle with approval gates |

**Phases:** Estimation → Risk Assessment → Tracking Setup → Status Reporting

**Hard Gates:** Estimation Review, Risk Acceptance, Status Report Approval

**Dependencies:** `estimate-tasks`, `identify-risks`, `generate-status-report`

---

### tech-lead Persona

| Path | `skills/personas/tech-lead/SKILL.md` |
| Description | Technical review lifecycle with go/no-go recommendation |

**Phases:** PRD Review → Feasibility Assessment → Estimation Quality Review → Technical Risk Report

**Hard Gates:** PRD Feasibility, Estimation Quality

**Dependencies:** `review-prd`, `estimate-tasks`

---

### delivery-lead Persona

| Path | `skills/personas/delivery-lead/SKILL.md` |
| Description | End-to-end delivery pipeline |

**Phases:** Scope → Plan → Prioritize → Sprint → Execute → Retrospect

**Hard Gates:** PRD Approval, Sprint Commitment, Retrospective Complete

**Dependencies:** All 12 skills

---

## If You Need...

| You need... | Recommended Skill(s) |
| **Clarify requirements** | `requirements-clarifier` |
| **Write a PRD** | `create-prd` |
| **Review a PRD** | `review-prd` |
| **Break down a feature** | `create-prd` → `generate-tasks` |
| **Estimate effort** | `generate-tasks` → `estimate-tasks` |
| **Assess risks** | `estimate-tasks` → `identify-risks` |
| **Generate tickets** | `plan-tickets` |
| **Prioritize backlog** | `prioritize-backlog` |
| **Plan a sprint** | `plan-sprint` |
| **Retrospective** | `create-retrospective` |
| **Status report** | `generate-status-report` |
| **Create GitHub issues** | `github-issue` |
| **End-to-end planning** | `product-owner` persona |
| **Execution tracking** | `project-manager` persona |
| **Technical feasibility** | `tech-lead` persona |
| **Full delivery cycle** | `delivery-lead` persona |

---

## See Also

- [Integration Matrix](integration-matrix.md) — How skills chain together
- [Persona Guide](../persona-guide.md) — Persona workflow details with Mermaid diagrams
- [Architecture](../architecture.md) — Repository layout and conventions
