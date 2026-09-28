---
name: work-router
type: catalog
license: MIT
description: Route a work request to one skill in the active project profile. Use when the task crosses product, delivery, and engineering roles or the next skill is unclear.
metadata:
  user-invocable: "true"
---

# Work Router

Input: the request and one active profile from `profiles.json`. Select only from that profile's expanded skill set. `directory.json` registers skills owned by this repository; stack skills are registered by their own repositories in `profiles.json`.

Output exactly one next-skill line:

`Next skill: <repository>/<skill>`

For behavior changes, add `Proof: <focused test or check>`. Add `Block: <risk>` only for migrations, security or authorization, deployment, destructive actions, or an unverified external API. Omit unused lines; routine work does not need a human handoff.

## Route by intent

| Request | Select |
|---|---|
| Clarify a rough request or acceptance criteria | `requirements-clarifier` |
| Draft a product brief | `create-prd` |
| Review a product brief | `review-prd` |
| Rank a backlog | `prioritize-backlog` |
| Estimate work | `estimate-tasks` |
| Plan a sprint | `plan-sprint` |
| Report delivery status | `generate-status-report` |
| Draft tracker tickets | `plan-tickets` |
| Create or update GitHub issues | `github-issue` |
| Implement a Rails feature | `rails-feature` |
| Review Rails code | `rails-review` |
| Perform routine Rails maintenance | `rails-maintenance` |
| Implement Ecto/database work | `ecto-essentials` |
| Implement other Elixir/Phoenix work | The narrowest matching domain skill; use `elixir-essentials` for general Elixir work |
| Implement Rust work or verify a crate API | `rust-essentials` |
| Diagnose an ownership or borrowing issue | `ownership-borrowing` |
| Design Rust types for domain constraints | `type-driven-design` |
| Handle Rust errors | `error-handling` |
| Implement plain Ruby work | `code-workflow` |

If the request names a skill, use it when it belongs to the active profile. Role words such as product owner, project manager, and tech lead refine intent; they do not start a separate workflow. Do not emit alternatives or multiple next skills. The selected skill owns the task and can consult a specialist when needed.
