---
name: github-issue
type: atomic
license: MIT
description: >
  Use when the user wants to create, track, or manage GitHub issues with
  automatic project board integration (Projects V2 and Classic), milestone
  tracking, and stage lifecycle management (todo → in-progress → in-review
  → done). Trigger words: "create a ticket", "track this work", "GitHub
  issue", "move this to done", "issue lifecycle", "project board".
metadata:
  version: 1.0.0
  user-invocable: "true"
---

# GitHub Issue Management

Use this skill when you need to create, track, or manage GitHub issues with project board integration and milestone tracking.

**Core principle:** Always validate issue drafts with the user before creating. Never create tracker issues without explicit approval.

## HARD-GATE

```text
DO NOT create any GitHub issue unless the user explicitly responds
with "yes", "approve", "create it", or an equivalent confirmation.
The issue body, title, labels, milestone, and project board placement
MUST all be presented to the user and confirmed before creation.

For issue updates: DO NOT change stage labels or close issues without
user confirmation. User must explicitly state the desired stage change.
```

## Quick Reference

| Aspect | Rule |
|--------|------|
| **Input** | Approved ticket drafts (from `plan-tickets`), feature description, or bug report |
| **Output** | GitHub issues with labels, project board placement, and milestone assignment |
| **Stage flow** | `todo` → `in-progress` → `in-review` → `done` (closed) |
| **Type labels** | `bug`, `new-feature`, `improvement`, `refactor`, `security` |

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth status`)
- Working in a git repository with a GitHub remote
- Have approved ticket drafts ready (ideally from `plan-tickets`), or a clear feature/bug description

---

## Label Conventions
**Type** (required, one): `bug`, `new-feature`, `improvement`, `refactor`, `security`

**Stage** (lifecycle): `todo`, `in-progress`, `in-review`, `done`

**Phase** (optional): `phase-1`, `phase-2`, etc.

**Priority** (optional): `priority:high`, `priority:medium`, `priority:low`

All labels use kebab-case. New issues always start with stage label `todo`.

---

## Stage Lifecycle

```text
todo → in-progress → in-review → done (closed)
```

Any stage can revert to `todo` if work is blocked or deprioritized.

---

## Creating a New Issue

### Step 1: Gather Context

Extract or ask for: the problem or feature, why it matters, what "done" looks like, and any examples, links, or error messages.

### Step 2: Detect Repository Setup

```bash
# Get owner and repo
OWNER_REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner')
OWNER=$(echo $OWNER_REPO | cut -d'/' -f1)
REPO=$(echo $OWNER_REPO | cut -d'/' -f2)

# Check for issue templates
ls -la .github/ISSUE_TEMPLATE/ 2>/dev/null || echo "No templates found"

# Check for Projects V2
gh project list --limit 10 --json number,title,url 2>/dev/null

# Check for Classic projects
gh api graphql -f query="query { repository(owner: \"$OWNER\", name: \"$REPO\") { projects(first: 10) { nodes { name url } } } }" 2>/dev/null

# Check for open milestones
gh api repos/$OWNER/$REPO/milestones?state=open --jq '.[].title'
```

### Step 3: Draft the Issue

If templates exist in `.github/ISSUE_TEMPLATE/`, adapt to that format. Otherwise use:

**Title:** Clear, action-oriented (e.g. "Add password reset email flow with SendGrid integration")

**Body template:**
```markdown
## Problem / Motivation
[Describe the problem and its impact — who is affected and why it matters.]

## Expected Outcome / Goal
[Describe the desired end state or user-facing result.]

## Proposed Solution (if known)
[Outline the approach, key components, or implementation notes.]

## Acceptance Criteria
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
```

### Step 4: Validate with User

Present the draft before creating:

```text
Here's the issue I'm about to create:

**Title:** [title]
**Type:** [type label]
**Stage:** todo
**Phase/Milestone:** [if applicable]
**Project Board:** [if detected]

**Description:**
[formatted body]

Does this look good, or would you like to adjust anything?
```

Wait for explicit approval before proceeding.

### Step 5: Create the Issue

```bash
# Create the issue and capture URL
ISSUE_URL=$(gh issue create \
  --title "Your title here" \
  --body "Your body here" \
  --label "todo,bug" \
  --json url --jq '.url')

# Extract issue number from URL (e.g. https://github.com/owner/repo/issues/42)
ISSUE_NUMBER=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')
```

**Add to Projects V2:**

```bash
# Add issue to a Projects V2 board
gh project item-add PROJECT_NUMBER --owner $OWNER --url $ISSUE_URL

# Query field IDs and status option IDs
gh api graphql -f query='
  query($owner: String!, $number: Int!) {
    organization(login: $owner) {
      projectV2(number: $number) {
        fields(first: 20) {
          nodes {
            ... on ProjectV2SingleSelectField {
              id name
              options { id name }
            }
          }
        }
      }
    }
  }' -F owner=$OWNER -F number=PROJECT_NUMBER

# Set status column via mutation (use field/option IDs from query above)
gh api graphql -f query='
  mutation($project: ID!, $item: ID!, $field: ID!, $option: String!) {
    updateProjectV2ItemFieldValue(
      input: { projectId: $project, itemId: $item,
               fieldId: $field, value: { singleSelectOptionId: $option } }
    ) { projectV2Item { id } }
  }' -F project=PROJECT_ID -F item=ITEM_ID -F field=FIELD_ID -F option=OPTION_ID
```

**Add to Classic project board:**

```bash
# Query column IDs
gh api graphql -f query='
  query($owner: String!, $repo: String!) {
    repository(owner: $owner, name: $repo) {
      projects(first: 10) {
        nodes { name columns(first: 10) { nodes { id name } } }
      }
    }
  }' -F owner=$OWNER -F repo=$REPO

# Create card in target column
gh api repos/$OWNER/$REPO/projects/columns/COLUMN_ID/cards \
  -f content_id=$ISSUE_NUMBER -f content_type=Issue
```

**Add to milestone:**
```bash
gh issue edit $ISSUE_NUMBER --milestone "Sprint 6 — Notifications"
```

### Step 6: Confirm Creation

Report the created issue number, URL, applied labels, project board column, and milestone assignment.

### Validate: Issue Creation

Before moving on, confirm:
- [ ] Issue title is clear, action-oriented, and specific
- [ ] Body includes Problem/Motivation, Expected Outcome, and Acceptance Criteria
- [ ] Correct type label applied (`bug`, `new-feature`, `improvement`, etc.)
- [ ] Stage label set to `todo`
- [ ] Project board column is correct (if applicable)
- [ ] Milestone assigned (if applicable)
- [ ] Issue URL is accessible and shows the expected content

## Output Style

A successfully created GitHub issue must conform to this shape:

```text
GitHub Issue #<number>
  Title: "<action-oriented, specific title>"
  URL:   https://github.com/<owner>/<repo>/issues/<number>
  State:  open
  Labels: todo, <type-label>
  Project: <board-name> → <column-name>
  Milestone: <milestone-title> (if assigned)

Body:
  ## Problem / Motivation
  <concrete description of the current problem>

  ## Expected Outcome / Goal
  <measurable definition of "done">

  ## Acceptance Criteria
  - [ ] Given <context> when <action> then <expected result>
```

**Validation before reporting "done":**
- Title is specific and action-oriented, not generic
- Body sections are filled with concrete content (no placeholders)
- Correct type label is assigned
- Stage label is `todo` for new issues
- Project board column matches the current stage
- Milestone is set when relevant

---

## Updating an Existing Issue

### Step 1: Find the Issue

```bash
# By number
gh issue view 42 --json title,body,labels,milestone

# By search
gh issue list --search "password reset email flow" --json number,title,labels,state
```

Present results to confirm the right issue.

### Step 2: Detect Stage Change

**User must explicitly state the desired stage change.** Examples: "Move #42 to in-progress", "Mark #42 as done", "Close #42".

### Step 3: Update Labels

```bash
# Remove old stage label, add new one
gh issue edit 42 --remove-label "todo" --add-label "in-progress"

# If done, also close
gh issue close 42 --reason completed
```

### Step 4: Update Project Board

For Projects V2, use the `QueryProjectV2Fields` query (see Creating §Step 5) to look up field/option IDs, then run the `updateProjectV2ItemFieldValue` mutation to move the item to the new status column. For Classic projects, use `QueryClassicProjectColumns` and create a card in the target column.

### Step 5: Confirm Update

```text
✓ Issue #42 updated
  Status: todo → in-progress
  Project: Moved to "In Progress" column
  URL: https://github.com/owner/repo/issues/42
```

### Validate: Issue Updates

Before confirming the update is complete, verify:
- [ ] Old stage label removed, new stage label added
- [ ] Project board card moved to the correct column (if applicable)
- [ ] If closing: issue is closed with the correct reason (`completed` or `not planned`)
- [ ] Issue URL is accessible and reflects the updated state
- [ ] No duplicate or contradictory labels (e.g., `todo` + `in-progress` simultaneously)
