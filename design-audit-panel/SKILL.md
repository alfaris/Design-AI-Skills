---
name: design-audit-panel
description: Audit a design, product concept, feature, user flow, or UI through expert business, usability, engineering, competitive, accessibility, UI/UX, and growth perspectives. Use for design reviews, UX critiques, accessibility audits, product critiques, red-team reviews, screenshots, Figma designs, prototypes, or written specifications when the user wants prioritized findings and an action plan.
---

# Design Audit Panel

Audit the provided design through selected expert perspectives, then combine the findings into one prioritized deliverable.

Read `references/personas.md` before writing a report. Use only the persona blocks selected for the audit and preserve each persona's five-section sequence.

## Perspectives

| Perspective | Primary lens |
| --- | --- |
| Stakeholder | Business viability, monetization, and conversion |
| Frustrated User | Real-world friction, clarity, and effort |
| Developer | Feasibility, architecture, and maintainability |
| Competitor | Positioning, parity, and defensibility |
| Accessibility Expert | WCAG 2.2 and inclusive design |
| UI/UX Expert | Hierarchy, interaction, design systems, and information architecture |
| Growth Marketing | Acquisition, activation, retention, referral, and revenue |

## Language

- Write the complete deliverable in the language used by the user unless they explicitly request another language.
- Keep product names, technical terms, and standards in their established form when translation would reduce clarity.
- For Arabic output, use clear Modern Standard Arabic and translate report headings consistently while preserving the required section order and meaning.
- Do not ask the user to choose a language when their request already makes it clear.

## Workflow

### 1. Select the perspectives

Use the perspectives named by the user. If none are named:

- For a general UI or flow review, use the Frustrated User, Accessibility Expert, and UI/UX Expert as the default core panel.
- For a business, growth, engineering, or competitive request, select the perspectives that directly match the stated goal.
- Run all seven only when the user requests a comprehensive review or explicitly asks for every perspective.

State the selected perspectives in one short line. Ask a selection question only when two plausible panels would produce materially different results and the user's goal does not resolve the choice.

### 2. Inspect the evidence

Review every supplied screenshot, design file, link, flow, and written requirement before auditing.

- Use a connected Figma tool when one is available and authorized.
- If a Figma or external link cannot be opened, say so and request screenshots or a concise description. Never imply that an inaccessible design was inspected.
- View attached images directly when the environment supports them.
- Distinguish observed evidence from inferred context. Label important assumptions.

Infer product type, audience, and stage when the evidence makes them reasonably clear. If a missing detail would change the audit materially, ask one compact question covering the product, audience, and stage. Do not request information that can be derived from the supplied material.

### 3. Run each persona

Read the relevant blocks in `references/personas.md`, adopt each lens, and produce one report per selected perspective.

- Preserve the five-section sequence: Critical Issues, Warnings, What's Working Well, Opportunities, and the persona-specific Plan.
- Ground every finding in visible or described evidence.
- Identify the affected screen, step, component, or requirement whenever possible.
- Separate confirmed accessibility failures from risks that require implementation or contrast inspection to verify.
- Keep persona voices distinct without using insults, stereotypes, or theatrical filler.
- Prefer a short, specific report over invented or repetitive findings.

### 4. Synthesize the audit

Place an executive summary before the persona reports. Include:

1. **Cross-perspective synthesis**: recurring themes, meaningful disagreements, and the overall readiness verdict. Omit comparison language when only one perspective runs.
2. **Top issues**: deduplicated findings ranked by user impact, business impact, accessibility severity, and implementation urgency.
3. **Consolidated action plan**: immediate fixes, next iteration work, and validation steps combined across the selected perspectives.

Do not rank cosmetic preferences above task blockers, accessibility barriers, data loss, broken flows, or misleading behavior.

### 5. Deliver in an available format

Default to readable inline Markdown when the user does not request a file type.

- For Markdown, respond inline or create a `.md` file when the user asks for a downloadable artifact.
- For Word or PDF, use an available platform-native document tool or skill.
- If the requested file capability is unavailable, provide the complete report in Markdown and add one brief note explaining the fallback.
- When creating a file, use the writable output location and file-sharing mechanism provided by the current platform. Never assume a fixed filesystem path or tool name.
- Avoid wide tables for long findings. Use stacked sections when the user is on mobile or when table cells would become difficult to scan.

Use this document order:

```text
# Design Audit - [Product Name]
## Executive Summary
## Top Issues
## Consolidated Action Plan
## [Perspective] Report
...one report per selected perspective...
```

## Quality checks

Before delivering:

- Confirm every critical issue points to supplied evidence.
- Remove duplicate findings across perspectives from the executive summary.
- Make recommendations concrete enough to assign and verify.
- Preserve useful strengths, not only faults.
- Check that the result matches the user's language and requested format.
- Clearly disclose inaccessible sources, unsupported tools, and material assumptions.
