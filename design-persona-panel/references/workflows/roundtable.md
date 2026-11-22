# Workflow: Roundtable

Three or more personas negotiate **one shared, ranked priority list**. Disagreements that remain are
recorded openly instead of being smoothed over.

- **Use when:** the user asks what to fix first, wants the team or personas to agree on priorities, plans a sprint or release from a design, or asks for consensus.
- **Personas:** 3 or more (default 3–4). With no personas named, choose the lenses that match the user's goal. For a general product question, use Stakeholder, Frustrated User, Developer, and A11y Expert.
- **Moderator:** a neutral facilitator that merges proposals and records the outcome.

## Steps

### 1. Agenda

State the scope in one line: what is being prioritized (e.g. "fixes before the v2 launch") and any constraint the user gave (time, team size, release date).

### 2. Proposals

Each persona proposes up to 3 priorities from its own lens. Each one includes the affected area, severity, evidence label, and a one-line reason. Several personas may propose the same fix at this stage. The overlap is a signal, and it is resolved in the merge. Negotiation exchanges in step 4 are short arguments and do not need the full finding fields.

### 3. Merge

The moderator merges overlapping proposals into single items, noting which personas backed each one. Items backed by several lenses gain weight but are not automatically ranked first.

### 4. Negotiation

For each contested item or ranking conflict, run a short exchange: the persona pushing it up, the persona pushing it down, and the trade-off between them. Keep each exchange to 2–4 lines. Use the Developer's effort estimates when the Developer is present. Otherwise label effort as **To verify**.

### 5. Final ranking

Rank in two passes:

1. **Tier first:** task blockers, accessibility barriers, data loss, broken flows, and misleading behavior rank above cosmetic or growth-only items, unless the user's constraint explicitly says otherwise.
2. **Then impact against effort** within each tier.

If a top-tier item does not fit the user's constraint (time, team size), keep it at the top. Then propose the smallest scoped-down or staged version that does fit, and record the remainder as **Next**.

For each item:

```text
Rank: [n]
Item: [what to do]
Affected area: [screen, step, component, or requirement]
Owner lens: [persona whose concern it primarily resolves]
Backed by: [personas, including any who raised it during merge or negotiation]
Severity: Critical | Major | Minor
Effort: S (≤2 dev-days) | M (3–5) | L (>5) | To verify
Urgency: Now | Next | Later
Evidence: Observed | Inferred | To verify
Done when: [validation test or acceptance signal]
```

Use the Developer's estimate for Effort when the Developer is present, and treat it as **Inferred** unless the team supplied estimates. Otherwise use **To verify**.

### 6. Dissent log

List every persona that still disagrees with a ranking or with an item being included or left out:

```text
Persona: [name]
Item: [item or omitted proposal]
Objection: [one line]
Revisit if: [signal that would reopen the decision]
```

Write "No recorded dissent" only if that is genuinely true.

### 7. Next steps

List 3–5 concrete actions to start the plan: who or which lens acts, what they do first, and which **To verify** questions must be answered before work begins.

## Output

```text
# Design Roundtable - [Product or Scope]
## Agenda
## Proposals
## Merge
## Negotiation
## Agreed Priorities
## Dissent Log
## Next Steps
```

## Quality checks

- Every final item traces back to at least one persona, whether it was proposed in step 2 or raised during merge or negotiation.
- The ranking respects the blocker-first rule.
- Dissent is recorded rather than erased.
- The list is short enough to act on (usually 5–8 items).
