---
name: judgment-gate
type: atomic
license: MIT
description: >
  Use when a plan, backlog, or design needs a defensible go/no-go or
  ranking and vibes are not enough. Frame narrow independently-answerable
  questions, collect judgments independently, and let the human keep
  policy. Trigger words: judgment, second opinion, independent review,
  rank options, go/no-go, sanity check this plan.
metadata:
  version: 1.0.0
  user-invocable: "true"
  output: Question set, independent verdicts, merged decision or escalation
  constraints: "Judgments inform; the human decides. At most two rounds."
---

# Judgment Gate

Explicit independent judgment for planning decisions — the planning
counterpart of `judgment-day` (which owns adversarial *code* review).
Never run both on the same target.

## HARD-GATE

- Judgments inform; the human decides. A judgment carries no delivery
  authority and satisfies no commit, push, or release gate by itself.
- Frame questions narrow enough to answer independently. "Is this plan
  good?" is not a question; "Does the plan name an owner for every P0
  task?" is.
- At most **two** rounds of fix-and-re-judge. Anything unresolved after
  that escalates to a human; never extend the budget.
- Judges are independent: separate context, identical frozen scope.
  Never accept a partial judgment.

## Process

1. **Freeze the target.** One complete, immutable artifact (plan,
   backlog, design doc) with a stated decision to make.
2. **Frame the questions.** Yes/no with explicit criteria, or ordered
   levels (e.g. risk: low/medium/high with definitions). 3–8 questions;
   each judge sees the same set.
3. **Judge independently.** Run two judges blind, or one judge plus a
   differently-framed pass. Record verdicts and confidence per question.
4. **Merge.** Agreement → act. One judge dissents → record as suspect,
   do not auto-fix. Contradiction → escalate for explicit human decision.
5. **Fix and re-judge (bounded).** Fix only confirmed findings; re-judge
   only the frozen ledger plus the delta. Repeat once at most.

## Question framing guide

| Decision shape | Frame as |
|----------------|----------|
| Include/exclude several items | One independent yes/no per item, rank by confidence |
| Single winner among options | One pick per judge with reasons; disagreement = escalate |
| Graded setting (risk, effort, readiness) | Ordered levels with written definitions per level |

## Decision gates

| Condition | Action |
|-----------|--------|
| Target or decision unclear | Ask one scope question and stop |
| Both judges agree | Proceed or fix, per verdict |
| One dissents | Record suspect; human decides whether to pursue |
| Judges contradict | Escalate; never average away a contradiction |
| Issues remain after round two | Escalate and stop |

## Output contract

Return: target identity, the question set, per-question verdicts with
confidence, confirmed/suspect/contradiction counts, and exactly one
terminal line: `DECISION: PROCEED ✅`, `DECISION: REVISE 🔁`, or
`DECISION: ESCALATE ⚠️`.

## Integration

| Skill | When to chain |
|-------|---------------|
| `review-prd` | Gate a PRD before `generate-tasks` |
| `prioritize-backlog` | Independent judgment on a ranking |
| `llm-judgment-layer` | Same discipline applied inside an app |
