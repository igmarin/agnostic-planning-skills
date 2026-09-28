---
name: plan-tickets
type: atomic
description: Draft tracker-ready work items from a plan or PRD. Use for ticket decomposition, sequencing, and acceptance criteria; use github-issue separately for requested GitHub mutations.
metadata:
  user-invocable: "true"
---

# Plan Tickets

Turn approved scope into concise, independently verifiable ticket drafts.

1. Read the source plan and identify outcomes, dependencies, and constraints.
2. Split only where work can be implemented and verified independently.
3. Give each draft a title, context, acceptance criteria, dependencies, and technical notes.
4. Suggest estimates or labels only when the project defines that policy; never invent sprint buckets, title prefixes, owners, or status transitions.
5. Return the drafts in Markdown, in dependency order. Leave tracker records unchanged.

For GitHub issue creation or edits, use `github-issue` with the user's explicit request.
