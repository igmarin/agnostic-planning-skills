---
name: work-router
type: orchestrator
description: Route a work request to one skill in the active project profile. Use when the task crosses product, delivery, and engineering roles or the next skill is unclear.
metadata:
  user-invocable: "true"
---

# Work Router

Input: the request and one active profile from `profiles.json`. Read only the selected profile's skills.

Return exactly one next skill in this form:

`Next skill: <profile>/<skill>`

Add a checkpoint only when the work changes production data, security or authorization, deployment, performs an irreversible action, or depends on an unverified external API. Routine work continues without a human handoff.

## Route by intent

| Request | Select |
|---|---|
| Clarify a rough request or acceptance criteria | `requirements-clarifier` |
| Draft or review a product brief | `create-prd` or `review-prd` |
| Rank backlog, size work, plan a sprint, or report delivery | `prioritize-backlog`, `estimate-tasks`, `plan-sprint`, or `generate-status-report` |
| Draft tracker tickets | `plan-tickets` |
| Create or update GitHub issues | `github-issue` |
| Rails feature, review, or routine maintenance | `rails-feature`, `rails-review`, or `rails-maintenance` |
| Elixir/Phoenix implementation | The narrowest matching domain skill; Ecto uses `ecto-essentials` |
| Rust implementation or crate API question | `rust-essentials`; use `ownership-borrowing`, `type-driven-design`, or `error-handling` for a focused question |
| Plain Ruby implementation | The matching Ruby pattern skill or `code-workflow` |

If a task names a specific skill, use it when it belongs to the active profile. Role words such as product owner, project manager, and tech lead refine intent; they do not start a separate workflow.

Do not emit multiple next skills. The selected skill owns the task and can consult a specialist when the request actually needs one.
