# Risk Patterns Reference

Catalog of risk patterns to scan for when analyzing plans and tasks.

---

## Dependency Chain Risk

**Pattern:** Task A blocks Task B blocks Task C. If Task A slips, everything slips.

**Scan for:**
- Tasks with multiple downstream dependents.
- Tasks on the critical path (longest chain of dependencies).
- Tasks where the estimate is "Low confidence" and multiple items depend on it.

**Example:**
> Task 2.0 (API contract definition) blocks Tasks 3.0, 4.0, and 5.0. If the API contract changes, 3 downstream tasks must be reworked. Mitigation: freeze the API contract early; define it with a consumer-driven contract test.

---

## External Dependency Risk

**Pattern:** The plan depends on something outside the team's control.

**Scan for:**
- Third-party API integrations.
- Vendor timelines or procurement.
- Team handoffs (design → dev, dev → QA).
- Infrastructure provisioning by another team.

**Example:**
> Task 4.0 integrates with the payment provider. The provider's sandbox is currently rate-limited. Mitigation: mock the provider in tests; request sandbox limit increase in parallel.

---

## Ambiguous Requirements Risk

**Pattern:** The PRD or task description is vague, leaving implementation open to interpretation.

**Scan for:**
- PRD sections marked "TBD" or "Open Question."
- Acceptance criteria that use subjective language ("fast," "intuitive," "good UX").
- Tasks that say "implement X" without specifying the scope of X.

**Example:**
> Requirement "The system must handle errors gracefully" is ambiguous. Does it mean retry? Fallback UI? Alert the user? Mitigation: clarify the specific error handling behavior before estimating.

---

## Single Point of Failure Risk

**Pattern:** One person, service, or component is the only thing keeping the plan together.

**Scan for:**
- One person owns all tasks in a critical path.
- One service handles all business logic with no fallback.
- No redundancy for a critical integration.

**Example:**
> Only Alice knows the authentication module. She's on 8 of the 12 tasks. Mitigation: pair program on auth tasks; document the module before the sprint starts.

---

## Capacity Risk

**Pattern:** The sprint plan exceeds what the team can realistically deliver.

**Scan for:**
- Total estimated points exceed the team's historical velocity.
- Key person is assigned to too many parallel critical tasks.
- Sprint includes tasks that require external coordination (reducing available capacity).

**Example:**
> Sprint target is 40 points but the team's average velocity is 28. Three tasks depend on the design team who have competing priorities this sprint. Mitigation: reduce scope to 28 points; defer design-dependent tasks.

---

## Technical Uncertainty Risk

**Pattern:** The plan involves something the team has never done before.

**Scan for:**
- New framework, library, or language the team hasn't used.
- Unproven integration pattern.
- Tasks that say "spike" or "investigate" with large estimates.

**Example:**
> Task 3.0 introduces a new real-time WebSocket layer. No one on the team has production WebSocket experience. Mitigation: run a spike first; pair with someone who has WebSocket experience; budget 2x the initial estimate.
