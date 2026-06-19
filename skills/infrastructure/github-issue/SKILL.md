---
name: github-issue
type: atomic
license: MIT
description: >
  Use when the user wants to create, track, or manage GitHub issues with
  automatic project board integration (Projects V2 and Classic), milestone
  tracking, and stage lifecycle management (todo → in-progress → in-review
  → done). Covers issue creation with labels/templates, status updates,
  project board moves, and completion workflows. Also covers "create a
  ticket", "track this work", "what's the status of issue #42", "move this
  to done", or any variation of GitHub issue lifecycle management.
---

# GitHub Issue Management

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth status`)
- Working in a git repository with a GitHub remote

---

## Label Conventions

**Type** (required, one): `bug`, `new-feature`, `improvement`, `refactor`, `security`

**Stage** (lifecycle): `todo`, `in-progress`, `in-review`, `done`

**Phase** (optional): `phase-1`, `phase-2`, etc.

**Priority** (optional): `priority:high`, `priority:medium`, `priority:low`

All labels use kebab-case. New issues always start with stage label `todo`.

---

## Stage Lifecycle

```
todo → in-progress → in-review → done (closed)
```

Any stage can revert to `todo` if work is blocked or deprioritized.

---

## Creating a New Issue

### Step 1: Gather Context

Extract or ask for:
- What's the problem or feature?
- Why does it matter?
- What does "done" look like?
- Any examples, links, or error messages?

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

**Title:** Clear, action-oriented (e.g. "Add retry logic to API client for transient failures")

**Body:**
```markdown
## Problem / Motivation
[What's the current situation and why is it a problem?]

## Expected Outcome / Goal
[What does "done" look like?]

## Proposed Solution (if known)
[Optional — how might this be solved?]

## Examples / References
[Links, error messages, screenshots, or code snippets]

## Acceptance Criteria
- [ ] [Specific, testable condition 1]
- [ ] [Specific, testable condition 2]
- [ ] [Specific, testable condition 3]
```

### Step 4: Validate with User

Present the draft before creating:

```
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
# Create the issue
ISSUE_URL=$(gh issue create \
  --title "Your title here" \
  --body "Your body here" \
  --label "todo,bug" \
  --json url --jq '.url')

ISSUE_NUMBER=$(echo $ISSUE_URL | grep -o '[0-9]*$')
```

**Add to Projects V2:**
```bash
# Add issue to project
gh project item-add PROJECT_NUMBER --owner $OWNER --url $ISSUE_URL
```

For Projects V2 status field updates or Classic project card placement, query the relevant field/column IDs first using the GraphQL API, then mutate. See PROJECTS_REFERENCE.md for full queries.

**Add to milestone:**
```bash
gh issue edit $ISSUE_NUMBER --milestone "Milestone Title"
```

### Step 6: Confirm Creation

```
✓ Issue created: #42 — "Add retry logic to API client"
  URL: https://github.com/owner/repo/issues/42
  Labels: todo, bug
  Project: Added to "Sprint Board" (To do column)
  Milestone: v1.2.0
```

---

## Updating an Existing Issue

### Step 1: Find the Issue

```bash
# By number
gh issue view 42 --json title,body,labels,milestone

# By search
gh issue list --search "retry logic API client" --json number,title,labels,state
```

Present results to confirm the right issue.

### Step 2: Detect Stage Change

**Explicit:** "Move #42 to in-progress", "Mark #42 as done", "Close #42"

**Inferred:**
- "I'm working on #42" → `in-progress`
- "#42 is ready for review" → `in-review`
- "#42 is finished/deployed" → `done`

If ambiguous, ask: "What stage is #42 in now?"

### Step 3: Update Labels

```bash
# Remove old stage label, add new one
gh issue edit 42 --remove-label "todo" --add-label "in-progress"

# If done, also close
gh issue close 42 --reason completed
```

### Step 4: Update Project Board

For Projects V2 status field updates and Classic project card moves, use the GraphQL API — see PROJECTS_REFERENCE.md for full query and mutation examples.

### Step 5: Confirm Update

```
✓ Issue #42 updated
  Status: todo → in-progress
  Project: Moved to "In Progress" column
  URL: https://github.com/owner/repo/issues/42
```
