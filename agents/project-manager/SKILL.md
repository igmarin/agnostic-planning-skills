---
name: project-manager
license: MIT
description: >
  Orchestrates the execution tracking lifecycle: estimates tasks, identifies risks,
  sets up tracking checkpoints, and generates stakeholder status reports. Language-agnostic.
  Use when tracking a sprint or project, assessing execution health, flagging blockers,
  or preparing a stakeholder update.
metadata:
  version: 1.0.0
  user-invocable: "true"
  entry_point: "Invoke when tracking project execution, assessing sprint health, or preparing a stakeholder status report"
  phases: "Phase 1: Estimation, Phase 2: Risk Assessment, Phase 3: Tracking Setup, Phase 4: Status Reporting"
  hard_gates: "Estimation Review, Risk Acceptance, Status Report Approval"
  dependencies: "estimate-tasks, identify-risks, generate-status-report"
  keywords: execution, tracking, status, risks, estimation, sprint, project management, blockers, stakeholder, report
---
# Project Manager Agent

Orchestrates execution tracking: from task estimation through risk assessment to stakeholder status reports. Chains three atomic skills through four phases with approval gates.

## When to Use

- A sprint or project needs estimation and risk assessment before execution begins
- A stakeholder needs a status update with honest progress, blockers, and risks
- The team needs a repeatable execution tracking pipeline
- Existing plans need a health check: "Are we on track? What are the risks?"

## Anti-Patterns

- Do not use before a PRD exists — this agent tracks execution, not scope definition
- Do not fabricate progress or hide blockers to make the report look better
- Do not skip the Risk Acceptance gate — risks the team hasn't acknowledged will surface later
- Do not generate a status report without current data — ask for updates if stale

## Agent Phases

### Phase 1: Estimation

1. Activate **task-management/estimate-tasks**: Estimate effort for the task list or PRD.
2. Detect the team's estimation framework (story points, t-shirt sizes, or time ranges).
3. Assign estimates with confidence levels.
4. Flag tasks needing further breakdown or spikes.

**HARD GATE — Estimation Review:**
```text
The estimation must be reviewed before proceeding to risk assessment.
DO NOT proceed if more than 30% of tasks have "Low" confidence.
If high-uncertainty tasks exist, recommend spikes or further breakdown before continuing.
```

---

### Phase 2: Risk Assessment

1. Activate **execution/identify-risks**: Scan the estimated task list for risks.
2. Classify each risk by likelihood, impact, and proximity.
3. Suggest concrete mitigations for each risk.
4. Identify the top 3 critical risks.

**HARD GATE — Risk Acceptance:**
```text
The risk register MUST be reviewed and acknowledged before tracking setup.
Every High/High risk must have a named owner and a mitigation plan.
DO NOT proceed with unacknowledged critical risks.
```

---

### Phase 3: Tracking Setup

1. Define tracking checkpoints:
   - **Milestones:** Key dates or events (API contract freeze, feature complete, QA start).
   - **Check-in cadence:** Daily standup, weekly sync, or async updates.
   - **Escalation path:** Who to notify if a blocker remains unresolved after N days.
2. Map tasks to milestones — which tasks must complete by which checkpoint.
3. Present the tracking plan for review (informational — no hard gate here).

**Quality Check:**
- Every milestone has at least one associated task.
- Every High-risk item has a checkpoint for reassessment.
- **If quality check fails:** Return to milestone mapping and fill the gaps.

---

### Phase 4: Status Reporting

1. Gather current progress data (from tracker, user input, or task list).
2. Activate **execution/generate-status-report**: Generate the structured status report.
3. Include: accomplishments, in-progress, blocked items, risks, next steps.
4. Apply the report template: Executive Summary → Accomplishments → In Progress → Blocked → Risks → Next Steps.

**HARD GATE — Status Report Approval:**
```text
The status report MUST be explicitly approved before sharing with stakeholders.
Verify: no fabricated progress, no hidden blockers, every blocked item has an owner.
DO NOT distribute the report without approval.
```

---

## Error Recovery

| Scenario | Recovery |
|----------|----------|
| Cannot detect estimation framework | Ask: "What estimation framework does your team use? (story points, t-shirt sizes, or time ranges)" |
| No task list available for estimation | Ask: "Do you have a task list or PRD I can estimate from? If not, I can estimate from the PRD requirements directly." |
| Risk register has no High/High items but plan seems risky | Flag: "The risk scan found no critical risks, but consider: [specific concern based on plan analysis]. Should I add it?" |
| Status data is stale (no updates in N days) | Flag: "Task progress hasn't been updated since [date]. I'll mark unknown items as 'needs update.' Share this report only after confirming status." |
| User rejects status report | Ask: "Which section needs correction? I'll revise the specific items rather than regenerating the whole report." |

## Output Style / Report

After completing all phases, produce a summary:

```markdown
## Execution Tracking Set Up: [Project/Sprint Name]

### Estimation Summary
- Framework: [story points / t-shirt sizes / time ranges]
- Total estimate: [N] points / [N] days
- Confidence: [N]% High, [N]% Medium, [N]% Low
- Items needing breakdown: [N]

### Top Risks
1. [Risk] — [Likelihood/Impact] — Owner: [Name]
2. [Risk] — [Likelihood/Impact] — Owner: [Name]
3. [Risk] — [Likelihood/Impact] — Owner: [Name]

### Tracking Plan
- Milestones: [N] defined
- Check-in cadence: [daily / weekly / async]
- Escalation path: [who to notify for unresolved blockers]

### Latest Status
- Report saved: `/reports/status-[date].md`
- Health: 🟢 On Track / 🟡 At Risk / 🔴 Blocked
```
