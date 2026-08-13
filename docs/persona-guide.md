# Persona Guide

Index of the four orchestrators. Phase steps and gates live in each persona `SKILL.md` — one owner.

| Persona | Use when | Path |
|---------|----------|------|
| `product-owner` | Feature needs discovery → PRD → tasks → tickets → sprint | [SKILL.md](../skills/personas/product-owner/SKILL.md) |
| `project-manager` | Sprint or project needs estimates, risks, and a status report | [SKILL.md](../skills/personas/project-manager/SKILL.md) |
| `tech-lead` | PRD needs a technical go/no-go | [SKILL.md](../skills/personas/tech-lead/SKILL.md) |
| `delivery-lead` | Full cycle from PRD through retrospective | [SKILL.md](../skills/personas/delivery-lead/SKILL.md) |

## product-owner

```mermaid
graph TD
    A[Feature idea] --> B[Discovery]
    B --> C[PRD draft]
    C --> D{PRD approved?}
    D -->|no| C
    D -->|yes| E[Tasks]
    E --> F[Tickets]
    F --> G{Tickets approved?}
    G -->|no| F
    G -->|yes| H[Sprint placement]
    H --> I{Sprint confirmed?}
    I -->|no| H
    I -->|yes| J[Ready for development]
```

## project-manager

```mermaid
graph TD
    A[Task list / PRD] --> B[estimate-tasks]
    B --> C{Estimates reviewed?}
    C -->|no| B
    C -->|yes| D[identify-risks]
    D --> E{Risks accepted?}
    E -->|no| D
    E -->|yes| F[Tracking setup]
    F --> G[generate-status-report]
    G --> H{Report approved?}
    H -->|no| G
    H -->|yes| I[Share]
```

## tech-lead

```mermaid
graph TD
    A[PRD] --> B[review-prd]
    B --> C{Verdict?}
    C -->|Needs revision| D[Back to create-prd]
    C -->|Approved| E[Feasibility]
    E --> F{Feasible?}
    F -->|High blocker| G[Report and stop]
    F -->|yes| H[Estimation quality]
    H --> I{Quality OK?}
    I -->|no| H
    I -->|yes| J[Technical risk report]
    J --> K[Go / No-go / Go with conditions]
```

## delivery-lead

```mermaid
graph TD
    A[Feature idea] --> B[Scope: create-prd + review-prd]
    B --> C{PRD approved?}
    C -->|no| B
    C -->|yes| D[Plan: tasks + estimates + risks]
    D --> E[Prioritize: backlog + tickets]
    E --> F[plan-sprint]
    F --> G{Sprint committed?}
    G -->|no| F
    G -->|yes| H[Execute: status + risks]
    H --> I[create-retrospective]
    I --> J{Retro complete?}
    J -->|no| I
    J -->|yes| K[Delivery complete]
```

## See also

- [Skill catalog](reference/skill-catalog.md)
- [Integration matrix](reference/integration-matrix.md)
