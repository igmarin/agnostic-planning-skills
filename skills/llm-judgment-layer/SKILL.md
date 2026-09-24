---
name: llm-judgment-layer
type: atomic
license: MIT
description: >
  Use when adding an LLM judgment or recommendation layer to an
  application — adaptive difficulty, content ranking, daily mixes,
  personalization. The model ranks and scores; code decides. Every
  failure path degrades silently to a deterministic fallback.
  Trigger words: llm judgment, ai difficulty, recommendation model,
  model-in-the-loop, adaptive content, ai personalization.
metadata:
  version: 1.0.0
  user-invocable: "true"
  output: Integration design — question set, state shape, gates, fallback
  constraints: "Model never holds policy; fallback must work with zero network."
---

# LLM Judgment Layer

Seasoning, not the meal. The app is 100% deterministic and works offline;
the model answers a few narrow questions per time-bucket and code keeps
control of everything else.

## HARD-GATE

- The model **never** decides policy. It ranks, scores, or answers yes/no;
  code sorts, clamps, thresholds, and chooses.
- The UI **never** waits on the network. Render the cached/default plan
  first; update in place if the model answers.
- Every failure path lands **silently** on the deterministic fallback.
  No error copy, no retry storms, no dead UI.
- The API key **never** ships in the client. Server-side proxy adds it;
  unset proxy URL means the layer is inert by design.

## Core loop

1. **State** — aggregate statistics only, composed in the model's primary
   language. No names, dates, identifiers, or free text.
2. **One batched request per time-bucket** (usually per local day), fired
   lazily on first need, cached by bucket stamp. All questions ride in one
   call against the same state.
3. **Parse per question** — a half-good response still contributes its
   good answers; failed questions fall back individually.
4. **Gate on confidence** — apply a model answer only above a threshold
   set by the stakes of being wrong. Below threshold: keep previous value.
5. **Decide in code** — sort, clamp, threshold. Guarantee a valid result
   even when every probability is low.

## Question primitives

| Primitive | Returns | Use for |
|-----------|---------|---------|
| Choice | one winner + probabilities | exactly-one selection |
| Noul (P(yes) per item) | independent probabilities | multi-select mixes — rank in code, take top N |
| Score (ordered levels) | float over a legend | graded settings like difficulty — round, clamp, gate |

Multi-select is the classic trap: a single Choice forces one winner;
independent Nouls give a per-item probability you can rank yourself.

## Timing

Batch per time-bucket, not per event. Difficulty that shifts mid-session
feels erratic; per-event calls multiply cost for no benefit at fine
granularity. New users start at a safe default, never at a model guess.

## Failure taxonomy (all → silent fallback)

No network or timeout · non-2xx · malformed or missing answers ·
low confidence · no proxy configured. The fallback is a first-class
feature: deterministic rotation, keep-yesterday's value, safe defaults.
Test the fallback path as heavily as the happy path.

## Privacy

The state object is the entire data contract: counts, ratios, recency.
If a field could identify a person, it does not belong. The proxy adds
the key server-side and forwards verbatim — no rewriting, no logging.

## Anti-patterns

- Letting the model's raw answer reach the UI ungated
- Error copy when the model fails (the user did nothing wrong)
- Per-event requests where a daily cache suffices
- PII or locale leaking into the state object
- Ignoring `confidence` — it's a separate axis from the answer itself

## Integration

| Skill | When to chain |
|-------|---------------|
| `judgment-gate` | Apply the same discipline to planning decisions |
| `tech-lead` | Feasibility review of the proposed integration |
