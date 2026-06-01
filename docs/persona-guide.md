# Persona Guide — Agnostic Planning Skills

Step-by-step workflows for the orchestrating personas.

---

## Product Owner Persona

Orchestrates the full product planning lifecycle: from a feature idea to sprint-ready tickets. Chains three skills through six phases with explicit approval gates.

### Phase Flow

```mermaid
graph TD
    A[Feature Idea] --> B["Phase 1<br/>Discovery & Clarification"]
    B -->|Scope clear| C["Phase 2<br/>PRD Draft"]
    C --> D{"PRD Approved?"}
    D -->|No| E["Phase 3<br/>Review & Revise"]
    E --> C
    D -->|Yes| F["Phase 4<br/>Task Estimation"]
    F --> G["Phase 5<br/>Ticket Generation"]
    G --> H{"Tickets Approved?"}
    H -->|No| G
    H -->|Yes| I["Phase 6<br/>Sprint Placement"]
    I --> J{"Sprint Confirmed?"}
    J -->|No| I
    J -->|Yes| K[Ready for Development]
```

| Phase | Skill | Gate |
|-------|-------|------|
| 1. Discovery & Clarification | — | Scope clear |
| 2. PRD Draft | `create-prd` | — |
| 3. Review & Revise | — | **PRD Approval** |
| 4. Task Estimation | `generate-tasks` | — |
| 5. Ticket Generation | `plan-tickets` | **Ticket Approval** |
| 6. Sprint Placement | — | **Sprint Confirmation** |

**Dependencies:** `create-prd`, `generate-tasks`, `plan-tickets`

---

## Project Manager Persona

Orchestrates execution tracking: from task estimation through risk assessment to stakeholder status reports. Chains three skills through four phases with approval gates.

### Phase Flow

```mermaid
graph TD
    A[Task List / PRD] --> B["Phase 1<br/>Estimation<br/>estimate-tasks"]
    B --> C{"Estimates Reviewed?"}
    C -->|No| B
    C -->|Yes| D["Phase 2<br/>Risk Assessment<br/>identify-risks"]
    D --> E{"Risks Accepted?"}
    E -->|No| D
    E -->|Yes| F["Phase 3<br/>Tracking Setup"]
    F --> G["Phase 4<br/>Status Reporting<br/>generate-status-report"]
    G --> H{"Report Approved?"}
    H -->|No| G
    H -->|Yes| I[Share with Stakeholders]
```

| Phase | Skill | Gate |
|-------|-------|------|
| 1. Estimation | `estimate-tasks` | **Estimation Review** |
| 2. Risk Assessment | `identify-risks` | **Risk Acceptance** |
| 3. Tracking Setup | — | Quality Check |
| 4. Status Reporting | `generate-status-report` | **Status Report Approval** |

**Dependencies:** `estimate-tasks`, `identify-risks`, `generate-status-report`

---

## Tech Lead Persona

Orchestrates technical review of a PRD: evaluates completeness, feasibility, and estimation quality. Produces a go/no-go recommendation. Chains two skills through four phases.

### Phase Flow

```mermaid
graph TD
    A[PRD] --> B["Phase 1<br/>PRD Review<br/>review-prd"]
    B --> C{Verdict?}
    C -->|Needs Revision| D[Return to create-prd]
    C -->|Approved| E["Phase 2<br/>Feasibility Assessment"]
    E --> F{"Feasible?"}
    F -->|No - Critical| G[Report & Stop]
    F -->|Yes| H["Phase 3<br/>Estimation Quality<br/>estimate-tasks"]
    H --> I{"Quality OK?"}
    I -->|No| H
    I -->|Yes| J["Phase 4<br/>Technical Risk Report"]
    J --> K[Go / No-Go / Go with Conditions]
```

| Phase | Skill | Gate |
|-------|-------|------|
| 1. PRD Review | `review-prd` | Decision: Approved / Needs Revision |
| 2. Feasibility Assessment | — | **PRD Feasibility** |
| 3. Estimation Quality | `estimate-tasks` | **Estimation Quality** |
| 4. Technical Risk Report | — | Go/No-Go recommendation |

**Dependencies:** `review-prd`, `estimate-tasks`

---

## Full Planning + Execution Pipeline

```mermaid
graph LR
    subgraph "Tech Lead"
        T[review-prd] --> U[estimate-tasks]
        U --> V[Technical Risk Report]
    end
    subgraph "Product Owner"
        A[create-prd] -->|approved| B[generate-tasks]
        B --> C[plan-tickets]
    end
    subgraph "Project Manager"
        D[estimate-tasks] --> E[identify-risks]
        E --> F[generate-status-report]
    end
    A --> T
    B --> D
    C --> F
```

---

## Delivery Lead Persona

Meta-persona orchestrating the full delivery pipeline: from feature idea through execution to retrospective. Chains skills through six phases with approval gates.

### Phase Flow

```mermaid
graph TD
    A[Feature Idea] --> B["Phase 1<br/>Scope<br/>create-prd + review-prd"]
    B --> C{"PRD Approved?"}
    C -->|No| B
    C -->|Yes| D["Phase 2<br/>Plan<br/>generate-tasks + estimate + risks"]
    D --> E["Phase 3<br/>Prioritize<br/>prioritize-backlog + plan-tickets"]
    E --> F["Phase 4<br/>Sprint<br/>plan-sprint"]
    F --> G{"Sprint Committed?"}
    G -->|No| F
    G -->|Yes| H["Phase 5<br/>Execute<br/>generate-status-report + risks"]
    H --> I["Phase 6<br/>Retrospect<br/>create-retrospective"]
    I --> J{"Retro Complete?"}
    J -->|No| I
    J -->|Yes| K[Delivery Complete]
```

| Phase | Skills | Gate |
|-------|--------|------|
| 1. Scope | `create-prd`, `review-prd` | **PRD Approval** |
| 2. Plan | `generate-tasks`, `estimate-tasks`, `identify-risks` | Quality Check |
| 3. Prioritize | `prioritize-backlog`, `plan-tickets` | — |
| 4. Sprint | `plan-sprint` | **Sprint Commitment** |
| 5. Execute | `generate-status-report`, `identify-risks` | — |
| 6. Retrospect | `create-retrospective` | **Retrospective Complete** |

**Dependencies:** All 10 skills

---

## Full Pipeline Diagram

```mermaid
graph LR
    subgraph "Delivery Lead"
        DL_Scope[create-prd + review-prd]
        DL_Plan[generate + estimate + risks]
        DL_Prioritize[prioritize + tickets]
        DL_Sprint[plan-sprint]
        DL_Execute[status + risks]
        DL_Retro[retrospective]
        DL_Scope --> DL_Plan --> DL_Prioritize --> DL_Sprint --> DL_Execute --> DL_Retro
    end
    subgraph "Tech Lead"
        T[review-prd] --> U[estimate-tasks]
        U --> V[Technical Risk Report]
    end
    subgraph "Product Owner"
        A[create-prd] -->|approved| B[generate-tasks]
        B --> C[plan-tickets]
    end
    subgraph "Project Manager"
        D[estimate-tasks] --> E[identify-risks]
        E --> F[generate-status-report]
    end
    A --> T
    B --> D
    C --> F
```

---

## See Also

- [Skill Catalog](reference/skill-catalog.md) — All skills and personas
- [Integration Matrix](reference/integration-matrix.md) — Complete chaining reference
