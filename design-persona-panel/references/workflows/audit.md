# Workflow: Audit

Each selected persona reviews the evidence **independently** and writes its own report. The moderator
then combines the reports into one prioritized deliverable.

- **Use when:** the user wants a review, critique, or audit of a design, flow, feature, or concept.
- **Personas:** 1 or more. The default core panel is Frustrated User, A11y Expert, and UI/UX Expert.
- **Independence:** each persona forms its findings from the evidence alone, without adjusting to the other personas' views. Deduplication and comparison happen only after every persona's findings are drafted.

## Steps

1. Run each selected persona against the evidence and draft its findings, using the five-section structure below.
2. Deduplicate across the drafts. Route each issue to its owning lens:
   - usability, flow, and copy friction → Frustrated User
   - WCAG and assistive technology → A11y Expert
   - visual composition, hierarchy, and components → UI/UX Expert
   - conversion, pricing, and business model → Stakeholder
   - feasibility, architecture, and cost → Developer
   - market parity and positioning → Competitor
   - activation, loops, referral, and tracking → Growth Marketing

   When one issue spans lenses, route it by the nature of the problem, not by which metric reveals it. A mandatory signup wall is flow friction, so it belongs to Frustrated User even when the evidence is a business funnel metric. A tiny close button on a referral modal is a target-size problem, so it belongs to A11y Expert, while the modal's interruption of the confirmation goes to Growth Marketing or Frustrated User. Mention its other consequences in the Executive Summary rather than repeating the finding. Repeat an issue under a second persona only when the impact or fix materially differs.
3. Write the synthesis: executive summary, top issues, and consolidated action plan.

## Persona report structure

Every persona report has exactly five sections, always in this order:

1. **Critical Issues**: things that seriously hurt the persona's core concern.
2. **Warnings**: things worth fixing before they grow.
3. **What's Working Well**: real strengths to preserve.
4. **Opportunities**: additions or changes with clear upside.
5. **Plan**: the persona-specific closing plan.

**Critical Issues** holds Critical-severity findings only. **Warnings** holds Major and Minor findings. If a persona has no Critical findings of its own, write one line saying so. If its Critical finding was routed to another persona, point to that report.

Each Critical Issue and Warning uses: Title, Severity, Evidence, Affected Area, the persona-specific impact field, Suggested Fix, and Validation. This is the Finding contract in persona voice: the persona-specific impact field carries the contract's Finding mechanism and Impact, and Suggested Fix is the contract's Fix.
Each Strength uses: Title, Evidence, and the persona-specific value field.
Each Opportunity uses: Title, Evidence, the persona-specific payoff field, and an implementation path. Opportunities do not need severity.

### Persona-specific fields

| Persona | Critical impact field | Warning risk field | Strength field | Opportunity field |
| --- | --- | --- | --- | --- |
| Stakeholder | Business Impact | The Hidden Risk | Positive Value | Growth Potential |
| Frustrated User | Why It Makes Me Quit | Why It Distracts Me | Why I Appreciate It | Delight Factor |
| Developer | Technical Risk | Maintenance Overhead | Engineering Value | Technical Payoff |
| Competitor | Market Deficit | The Competitive Disadvantage | Competitive Edge | Disruptive Potential |
| A11y Expert | Exclusion Impact (include the WCAG criterion) | Compliance/Friction Risk | Accessible Value | Inclusive Innovation |
| UI/UX Expert | Design Failure (name the principle) | Visual Polish Risk | Design Value | Aesthetic Payoff |
| Growth Marketing | Growth Block | Velocity Drag | Growth Value | Viral Scalability |

### Persona-specific plans

- **Stakeholder → Strategic Plan:** top 5 business priorities, quick wins for an immediate conversion lift, final recommendation before production.
- **Frustrated User → Usability Plan:** top 5 workflow bottlenecks to remove, quick wins to cut user effort (fields to drop, steps to skip), final verdict for an impatient audience.
- **Developer → Architecture Plan:** top 5 architecture or data-model fixes, engineering quick wins, final technical-readiness recommendation.
- **Competitor → Competitive Roadmap:** top 3 updates to win market share, low-cost high-perception tweaks, final positioning recommendation.
- **A11y Expert → Accessibility Remediation Plan:** top 5 blockers to fix before coding or deployment, specifications for interactive elements (modals, dropdowns, forms), final compliance verdict.
- **UI/UX Expert → Design System & UI Plan:** top 5 hierarchy and layout corrections, component rules to enforce, final aesthetic-readiness verdict.
- **Growth Marketing → Growth Engine Plan:** top 3 structural changes to raise the viral coefficient (K-factor), tracking and analytics baselines to place before launch, final growth-readiness appraisal.

Use fewer items than the counts above when the evidence does not support them. Never pad.

## Synthesis

Place the synthesis before the persona reports:

1. **Executive Summary:** recurring themes, meaningful disagreements between lenses, and an overall readiness verdict. Omit comparison language when only one persona runs.
2. **Top Issues:** deduplicated findings ranked by user impact, business impact, accessibility severity, and implementation urgency. Each uses the Finding contract. Do not rank cosmetic preferences above task blockers, accessibility barriers, data loss, broken flows, or misleading behavior.
3. **Consolidated Action Plan:** immediate fixes, next-iteration work, and validation steps combined across personas. List unresolved questions under **To verify**.

## Output

```text
# Design Audit - [Product Name]
## Executive Summary
## Top Issues
## Consolidated Action Plan
## [Persona] Report
...one report per selected persona...
```

## Quality checks

- Every critical issue points to supplied evidence.
- The Top Issues list contains no duplicates across personas.
- Each persona report keeps its five sections in order.
