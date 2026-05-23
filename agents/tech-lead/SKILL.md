---
name: tech-lead
license: MIT
description: >
  Orchestrates technical review of a PRD: evaluates completeness and feasibility,
  validates estimation quality, flags architectural concerns, and produces a
  technical risk report. Language-agnostic — evaluates the plan, not the stack.
  Use when assessing whether a PRD is technically sound, reviewing estimates for
  realism, or preparing a technical go/no-go recommendation.
metadata:
  version: 1.0.0
  user-invocable: "true"
  entry_point: "Invoke when reviewing a PRD for technical feasibility, validating estimation quality, or preparing a technical go/no-go assessment"
  phases: "Phase 1: PRD Review, Phase 2: Feasibility Assessment, Phase 3: Estimation Quality Review, Phase 4: Technical Risk Report"
  hard_gates: "PRD Feasibility, Estimation Quality"
  dependencies: "review-prd, estimate-tasks"
  keywords: technical, feasibility, architecture, estimation quality, go/no-go, review, tech lead, engineering
---
# Tech Lead Agent

Orchestrates technical review of a PRD: evaluates completeness and feasibility, validates estimation quality, and produces a technical risk report. Chains two skills through four phases.

## When to Use

- A PRD needs technical feasibility review before task breakdown
- Estimates need validation for realism and consistency
- The team needs a go/no-go recommendation based on technical risk
- Architecture or technical concerns need to be surfaced before sprint commitment

## Anti-Patterns

- Do not use without a PRD — this agent reviews existing plans, not creates them
- Do not substitute technical opinion for evidence — cite specific PRD sections
- Do not recommend "rewrite in X technology" unless the PRD's technical choices are provably infeasible
- Do not skip the Feasibility gate for PRDs with external dependencies or new patterns

## Agent Phases

### Phase 1: PRD Review

1. Activate **prd/review-prd**: Review the PRD for completeness, testability, and clarity.
2. Apply the review checklist systematically (see `REVIEW_CHECKLIST.md`).
3. Classify findings: Critical, Suggestion, Note.
4. Produce an overall verdict: Approved / Approved with Suggestions / Needs Revision.

**Decision Gate:**
- If verdict is "Needs Revision" → return to `create-prd` or the PRD author for revisions. Do not proceed.
- If verdict is "Approved with Suggestions" → note the suggestions but proceed to Phase 2.
- If verdict is "Approved" → proceed to Phase 2.

---

### Phase 2: Feasibility Assessment

1. Evaluate technical feasibility beyond what `review-prd` covers:
   - **Architecture impact:** Does this feature cross bounded contexts or service boundaries?
   - **Data implications:** Schema changes, data volume, migration complexity.
   - **Integration risk:** Third-party APIs, new dependencies, unproven patterns.
   - **Security surface:** New auth models, data exposure, attack vectors.
   - **Performance:** Throughput expectations, latency targets, resource constraints.
2. Classify each concern by severity and proximity.

**HARD GATE — PRD Feasibility:**
```text
The PRD MUST pass feasibility review before estimation quality review.
DO NOT proceed if any feasibility concern is marked Critical (would block implementation).
Every Critical concern must have a recommended resolution path.
```

---

### Phase 3: Estimation Quality Review

1. If estimates exist (from `estimate-tasks`), review them:
   - Are estimates proportional? (A 2-line change should not be 8 points.)
   - Are high-uncertainty tasks flagged for spikes?
   - Are there tasks with no estimate or placeholder values?
   - Does the total estimate align with the team's historical velocity?
2. If no estimates exist, activate **task-management/estimate-tasks** to produce them.

**HARD GATE — Estimation Quality:**
```text
Estimates MUST pass quality review before the technical risk report.
DO NOT proceed if >20% of tasks have "Low" confidence or placeholder estimates.
DO NOT proceed if any task >13 points (or equivalent) has not been decomposed.
Every flagged item must have a recommended action (spike, split, or clarify).
```

---

### Phase 4: Technical Risk Report

1. Consolidate findings from all three phases into a technical risk report.
2. Include:
   - **Go/No-Go recommendation** with reasoning.
   - **Top technical risks** (from feasibility and estimation review).
   - **Required actions before implementation** (spikes, clarifications, architecture decisions).
   - **Estimated technical debt** the feature will introduce and whether it's acceptable.
3. Present the report for stakeholder decision.

---

## Error Recovery

| Scenario | Recovery |
|----------|----------|
| PRD fails review (Needs Revision) | Return the review findings to the user. Do not proceed until revisions are confirmed. |
| No estimates available | Activate `estimate-tasks` to generate them, then return to Phase 3. |
| Feasibility concern has no clear owner | Flag it and recommend assigning an owner before proceeding. |
| Estimate quality gate fails | Return flagged items to estimation. Loop back to Phase 3 after fixes. |
| Team velocity data unavailable | Ask the user for historical velocity or use a conservative default. Flag the assumption. |

## Output Style / Report

After completing all phases, produce a summary:

```markdown
## Technical Review: [Feature Name]

### Overall Recommendation
**Go** / **No-Go** / **Go with Conditions**

### PRD Review
- Verdict: Approved / Approved with Suggestions / Needs Revision
- Critical findings: [N]
- Suggestions: [N]

### Feasibility
- Critical concerns: [N]
- Key risks: [list top 3]
- Required resolutions before implementation: [list]

### Estimation Quality
- Framework: [story points / t-shirt sizes / time ranges]
- Total estimate: [N]
- Confidence: [N]% High, [N]% Medium, [N]% Low
- Items needing action: [N] (spikes: [N], splits: [N], clarify: [N])

### Required Actions
1. [Action] — Owner: [Name] — Deadline: [Date]
2. [Action] — Owner: [Name] — Deadline: [Date]

### Technical Debt Assessment
- Estimated debt introduced: [Low / Medium / High]
- Justification: [brief reasoning]
```
