---
name: design-persona-panel
description: Review a design, product concept, feature, user flow, or UI with a panel of expert personas (business, frustrated user, engineering, competitive, accessibility, UI/UX, growth) using one of four workflows - Audit (independent reports and a prioritized action plan), Debate (personas argue a trade-off and a moderator decides), Roundtable (personas agree on one ranked priority list), or Walkthrough (personas step through a flow screen by screen). Use for design reviews, UX critiques, accessibility audits, red-team reviews, design trade-offs, "should we A or B", prioritizing fixes, and walking through screenshots, Figma designs, prototypes, or written specifications.
---

# Design Persona Panel

Run selected expert personas against the supplied design through one workflow, then deliver one
structured result.

- [`references/personas.md`](references/personas.md) defines **who** each persona is and the shared quality rules.
- [`references/workflows/`](references/workflows/) defines **how** the personas interact and what the output looks like:
  - [`audit.md`](references/workflows/audit.md)
  - [`debate.md`](references/workflows/debate.md)
  - [`roundtable.md`](references/workflows/roundtable.md)
  - [`walkthrough.md`](references/workflows/walkthrough.md)

This is an **evaluative** skill. Every workflow reviews supplied evidence through the selected lenses. Do not generate a redesign or fill missing evidence with plausible assumptions.

## Personas

| Persona | Primary lens |
| --- | --- |
| Stakeholder | Business viability, monetization, and conversion |
| Frustrated User | Real-world friction, clarity, and effort |
| Developer | Feasibility, architecture, and maintainability |
| Competitor | Positioning, parity, and defensibility |
| A11y Expert | WCAG 2.2 and inclusive design |
| UI/UX Expert | Hierarchy, interaction, design systems, and information architecture |
| Growth Marketing | Acquisition, activation, retention, referral, and revenue |

## Workflows

| Workflow | Use when | Personas | Delivers |
| --- | --- | --- | --- |
| Audit | Review or critique a design | 1+ | Persona reports, top issues, action plan |
| Debate | A trade-off, an "A or B", or a "should we…?" question | 2+ | Arguments, rebuttals, moderator verdict, settling test |
| Roundtable | Decide what to fix first or agree on priorities | 3+ | One ranked priority list and a dissent log |
| Walkthrough | Step through a multi-step flow | 2+ | Per-step persona notes, step verdicts, journey heatmap |

## Finding contract

This is the full shape of a finding. Use it for every top-level ranked item: Audit **Top Issues** and Walkthrough **Top Fixes**. The item templates inside each workflow (persona report items, debate arguments, roundtable priorities, walkthrough notes) are compact forms of this contract. When a workflow template differs from this contract, follow the workflow template. Every finding, in any form, still needs an evidence label, the affected area, and a concrete fix or consequence.

```text
Severity: Critical | Major | Minor
Evidence: Observed | Inferred | To verify
Affected area: [screen, step, component, or requirement]
Finding: [specific problem and its mechanism]
Impact: [user, business, accessibility, or delivery consequence]
Fix: [concrete change]
Validation: [test, question, or evidence needed]
```

Do not force a field to sound certain. Use `To verify` when the supplied material cannot support a confirmed finding, and omit an impact category that does not apply.

## Language

- Write the complete deliverable in the language used by the user unless they explicitly request another language.
- Keep product names, technical terms, and standards in their established form when translation would reduce clarity.
- For Arabic output, use clear Modern Standard Arabic and translate headings consistently while preserving the required section order and meaning.
- For non-English output, also translate persona names, field labels, and the severity, evidence, urgency, and verdict values. Pick one translation for each term and use it everywhere, including short codes in tables. Add the English term in parentheses on first use when it helps recognition. Keep WCAG criterion numbers and product names unchanged.
- Do not ask the user to choose a language when their request already makes it clear.

## Process

### 1. Pick the workflow

- A workflow the user names always wins.
- A question with options, a trade-off, or a request to argue or debate → **Debate**.
- "What should we fix first?", prioritization, consensus, or sprint or release planning → **Roundtable**.
- A multi-step flow plus "walk through", "step through", or a request for screen-by-screen review → **Walkthrough**.
- Anything else → **Audit**.

Ask a workflow question only when two workflows would produce materially different deliverables and the request does not resolve the choice.

### 2. Pick the personas

Use the personas named by the user. Otherwise apply the default from the selected workflow file:

- **Audit:** Frustrated User, A11y Expert, and UI/UX Expert for a general UI or flow review. When the request or evidence also has a business, growth, engineering, or competitive goal, add the matching persona(s) to the core panel. Replace the core panel only when the request is purely business, engineering, or competitive and there is no UI evidence. Run all seven only on request.
- **Debate:** the 2 personas who would genuinely take opposite sides of the motion. Use the natural tensions in `personas.md` as a starting point, then check each candidate's **Fights for** against the specific motion. If both would argue the same side, choose a different pairing.
- **Roundtable:** 3–4 lenses that match the goal.
- **Walkthrough:** the Audit core panel. Add Stakeholder when the flow ends in a conversion, Growth Marketing when it includes sharing or referral, or both. Keep the panel at 5 personas or fewer.

If the user asks for fewer personas than the workflow's minimum, explain the minimum in one line and suggest the closest valid panel or workflow.

State the workflow and personas in one short line, e.g. "Debate · Growth Marketing vs Frustrated User". Put it on the first line of the response, above the document heading. When delivering a file, put it on the file's first line instead. Put assumptions and inaccessible-source notes in a short block directly under that line, then start the workflow's document heading once.

### 3. Establish context and inspect the evidence

Establish the smallest useful context profile: product or feature, target audience, platform, lifecycle stage, and goal. Infer what the evidence makes reasonably clear. Ask one compact question only when a missing detail would change the workflow, the panel, or severity.

Review every supplied screenshot, design file, link, flow, and written requirement before starting.

- Use a connected Figma tool when one is available and authorized.
- If a Figma or external link cannot be opened, say so and request screenshots or a concise description. Never imply that an inaccessible design was inspected.
- View attached images directly when the environment supports them.
- Tag material claims as **Observed**, **Inferred**, or **To verify**. A finding based only on an inference cannot be presented as a confirmed failure.

### 4. Run the workflow

Read the selected persona blocks in `references/personas.md` and the selected workflow file, then follow the workflow's steps and output structure exactly.

**Optional isolated execution:** when the environment can run subagents and the user has not asked for a single quick pass, the independent phases (Audit reports, Debate opening statements, Roundtable proposals) may run as one isolated subagent per persona, given only that persona's block, the shared rules, and the evidence. This keeps the lenses from converging. Then merge the results in the main response. Without subagents, simulate each persona in turn within one response. Never require subagents.

### 5. Deliver in an available format

Default to readable inline Markdown when the user does not request a file type.

- For Markdown, respond inline or create a `.md` file when the user asks for a downloadable artifact.
- For Word or PDF, use an available platform-native document tool or skill.
- If the requested file capability is unavailable, provide the complete result in Markdown and add one brief note explaining the fallback.
- When creating a file, use the writable output location and file-sharing mechanism provided by the current platform. Never assume a fixed filesystem path or tool name.
- Avoid wide tables for long content. Use stacked sections for mobile readers or when table cells would become difficult to scan.

## Quality checks

Before delivering:

- Confirm the workflow's own quality checks pass.
- Confirm every critical claim points to supplied evidence.
- Remove duplicate findings across personas from any summary or ranked list.
- Make recommendations concrete enough to assign and verify.
- Preserve useful strengths, not only faults.
- Check that the result matches the user's language and requested format.
- Clearly disclose inaccessible sources, unsupported tools, and material assumptions.
