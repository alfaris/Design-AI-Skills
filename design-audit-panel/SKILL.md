---
name: design-audit-panel
description: Audit a design, product concept, feature set, user flow, or UI from up to seven expert perspectives — Stakeholder (business/CRO), Frustrated User (UX friction), Developer (technical feasibility), Competitor (market positioning), A11y Expert (WCAG), UI/UX Expert (visual/IA), and Growth Marketing (AARRR/virality). Each persona returns a five-section report (Critical Issues, Warnings, What's Working Well, Opportunities, Plan), assembled into one combined deliverable with an executive summary. Use whenever the user wants a design review, design critique, UX audit, accessibility audit, product critique, "tear apart my design", "poke holes in this UI", "review this flow", "audit this feature", "what's wrong with this screen", red-team a product, or expert feedback on screenshots, Figma files, or written specs — even if they don't name the personas. Trigger any time someone hands over a design, mockup, prototype, flow, or concept and wants critical multi-angle feedback before building or shipping.
---

# Design Audit Panel

Audit a design or product concept through up to seven expert lenses, then assemble the reports into a
single deliverable with an executive summary on top.

The full persona prompts live in `references/personas.md`. Read that file before producing any report —
each persona has a deliberate attitude and a fixed five-section output structure that must be preserved
exactly.

## The seven personas

| # | Persona | Lens |
|---|---------|------|
| 1 | 📊 Stakeholder | Business viability, monetization, conversion (CRO) |
| 2 | 😤 Frustrated User | Real-world UX friction, impatience, rage-quit moments |
| 3 | 🛠 Developer | Technical feasibility, architecture, maintainability |
| 4 | 🦊 Competitor | Market positioning, parity gaps, defensibility |
| 5 | ♿ A11y Expert | Accessibility, WCAG 2.2 compliance, inclusive design |
| 6 | 😍 UI/UX Expert | Visual hierarchy, design systems, information architecture |
| 7 | 🚀 Growth Marketing | AARRR funnel, virality, activation, data loops |

## Workflow

### Step 1 — Confirm which personas to run

The default is **user picks per run**. If the user already named the personas (e.g. "run the developer
and a11y lenses"), proceed with those. If they just said something like "audit this design," present the
seven options and ask which they want — offer "all seven" as an easy choice. Don't run all seven silently
unless asked.

### Step 2 — Gather the design context

Look at what was provided: screenshots/images, a Figma link or file, a written spec, or a mix. Read or
view the material thoroughly before auditing.

The personas reference business stage, product type, and target audience. **If those are unclear from the
input, ask before auditing** — a one-line clarification ("What's the product, who's it for, and what
stage is it at?") sharpens every persona's output. If the context is obvious from the material, infer it
and state your assumption rather than stalling.

- For **Figma links**, use the Figma tools if connected; otherwise ask the user to export screenshots.
- For **images**, view them directly.
- For **written specs**, read the full text.

### Step 3 — Run each selected persona

For each persona the user chose, read its block in `references/personas.md`, fully adopt that persona, and
produce its report in the exact five-section structure. Do not soften the persona's attitude — the
Frustrated User should be genuinely impatient, the Competitor genuinely cutthroat, the Developer genuinely
conservative. Ground every finding in the actual design provided; never invent screens or features that
aren't there. If a persona has little to say about the given material, a shorter honest report beats
padding.

### Step 4 — Build the executive summary

After all selected reports exist, write an executive summary that contains all three of:

1. **Cross-persona synthesis** — your own read of the themes that recur across lenses (e.g. "three of the
   four personas flagged the signup flow"). This is the highest-value part.
2. **Top issues ranked across all personas** — a single prioritized list of the most severe findings
   pulled from every persona's Critical Issues, deduplicated and ordered by impact.
3. **Consolidated action plan** — the section-5 plans from each persona, stitched together so the user has
   one place to see every recommended next step.

Place the executive summary at the **top** of the combined deliverable, before the individual reports.

### Step 5 — Deliver in the chosen format

Format is **decided per run**. If the user hasn't said, ask: Markdown, Word (.docx), or PDF. Then:

- **Markdown** → create a `.md` file (use the `md`/`docx` skill conventions only if relevant; a clean
  markdown file is usually enough).
- **Word (.docx)** → use the **docx skill** (`/mnt/skills/public/docx/SKILL.md`).
- **PDF** → use the **pdf skill** (`/mnt/skills/public/pdf/SKILL.md`).

Structure of the combined document:

```
# Design Audit — [Product Name]
## Executive Summary
   - Cross-persona synthesis
   - Top issues ranked across all personas
   - Consolidated action plan
## 📊 Stakeholder Report          (if selected)
## 😤 Frustrated User Report       (if selected)
... one section per selected persona ...
```

Save the final file to `/mnt/user-data/outputs/` and present it with `present_files`.

## Notes

- Keep each persona's voice distinct; the value of the panel is the contrast between lenses.
- When only one persona is selected, skip the cross-persona synthesis (nothing to compare) but still
  provide the ranked issues and action plan, and inline delivery is fine unless a file is requested.
- The personas can disagree with each other — that's expected and useful. Surface the tension in the
  synthesis rather than papering over it.
