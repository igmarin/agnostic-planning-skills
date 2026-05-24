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

Orchestrates execution tracking: from task estimation through risk assessment to stakeholder status reports, across four phases with hard approval gates.

## When to Use

- A sprint or project needs estimation and risk assessment before execution begins
- A stakeholder needs a status update with honest progress, blockers, and risks
- The team needs a repeatable execution tracking pipeline
- Existing plans need a health check: "Are we on track? What are the risks?"

## Anti-Patterns

- Do not use before a PRD exists — this agent tracks execution, not scope definition
- Do not fabricate progress or hide blockers to make the report look better
- Do not skip the Risk Acceptance gate — unacknowledged risks will surface later
- Do not generate a status report without current data — ask for updates if stale

## Atomic Sub-Skill Contracts

This skill chains three atomic sub-skills. These contracts are the single source of truth for each sub-skill's interface. Each phase references these contracts — do not restate them in the phase steps.

**estimate-tasks** — Input: task list or PRD requirements. Output: each task annotated with effort estimate, estimation unit (story points / t-shirt size / time range), and confidence level (High / Medium / Low). Flag tasks needing spikes.

**identify-risks** — Input: estimated task list. Output: risk register where each entry has: risk description, likelihood (High/Med/Low), impact (High/Med/Low), proximity (near/mid/far), mitigation suggestion, and named owner field.

**generate-status-report** — Input: task progress snapshot, risk register, milestone plan. Output: structured Markdown report with sections: Executive Summary, Accomplishments, In Progress, Blocked, Risks, Next Steps.

---

## Agent Phases

### Phase 1: Estimation

1. Activate **task-management/estimate-tasks** per the contract above.
2. Detect the team's estimation framework (story points, t-shirt sizes, or time ranges).
3. Assign estimates with confidence levels; flag tasks needing further breakdown or spikes.

**HARD GATE — Estimation Review:**
```text
The estimation must be reviewed before proceeding to risk assessment.
DO NOT proceed if more than 30% of tasks have "Low" confidence.
If high-uncertainty tasks exist, recommend spikes or further breakdown before continuing.
```

**Example Output (story points, 1 SP ≈ half a day):**

```
| Task                          | Estimate | Confidence | Notes                          |
|-------------------------------|----------|------------|--------------------------------|
| Design database schema        | 3 SP     | High       |                                |
| Implement user authentication | 5 SP     | Medium     | OAuth flow needs spike         |
| Build REST API endpoints      | 8 SP     | Medium     | Scope depends on auth design   |
| Write integration tests       | 3 SP     | High       |                                |
| Deploy to staging             | 2 SP     | High       |                                |

Total: 21 SP | Confidence: 60% High, 40% Medium, 0% Low
Spike recommended: OAuth provider selection (1 SP) before auth implementation.
```

Gate result: 0% Low confidence — gate passes. Proceed after user review.

---

### Phase 2: Risk Assessment

1. Activate **execution/identify-risks** per the contract above.
2. Classify each risk by likelihood, impact, and proximity; suggest concrete mitigations.
3. Identify the top 3 critical risks.

**HARD GATE — Risk Acceptance:**
```text
The risk register MUST be reviewed and acknowledged before tracking setup.
Every High/High risk must have a named owner and a mitigation plan.
DO NOT proceed with unacknowledged critical risks.
```

**Example Risk Register:**
```
| Risk                              | Likelihood | Impact | Proximity | Mitigation                              | Owner |
|-----------------------------------|------------|--------|-----------|-----------------------------------------|-------|
| OAuth spike reveals scope creep   | High       | High   | Near      | Timebox spike to 1 SP; decide by Day 2 | Alice |
| Staging environment unavailable   | Med        | High   | Mid       | Reserve env slot; confirm with DevOps  | Bob   |
| Integration tests flaky on CI     | Med        | Med    | Far       | Add retry logic; dedicate 0.5 SP buffer| Alice |
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
2. Activate **execution/generate-status-report** per the contract above.
3. Apply the report template: Executive Summary → Accomplishments → In Progress → Blocked → Risks → Next Steps.

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

After completing all phases, produce a summary. Example with realistic sample data:

```markdown
## Execution Tracking Set Up: Auth Service Sprint 4

### Estimation Summary
- Framework: Story points (1 SP ≈ half a day)
- Total estimate: 21 points
- Confidence: 60% High, 40% Medium, 0% Low
- Items needing breakdown: 1 (OAuth spike — timebox to 1 SP)

### Top Risks
1. OAuth spike reveals scope creep — High/High — Owner: Alice
2. Staging environment unavailable — Med/High — Owner: Bob
3. Integration tests flaky on CI — Med/Med — Owner: Alice

### Tracking Plan
- Milestones: 3 defined (OAuth spike complete Day 2, API contract freeze Day 5, Feature complete Day 8)
- Check-in cadence: Daily async update in #sprint-4 Slack channel
- Escalation path: Notify Tech Lead if any blocker unresolved after 2 days

### Latest Status
- Report saved: `/reports/status-2024-11-15.md`
- Health: 🟡 At Risk — OAuth spike outcome pending; all other tasks on track
```
