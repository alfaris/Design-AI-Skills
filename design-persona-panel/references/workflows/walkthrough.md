# Workflow: Walkthrough

The selected personas move through a multi-step flow **together, one step at a time**. Each persona
comments on each step where it has something real to say.

- **Use when:** the user asks to walk through, step through, or review an onboarding, checkout, signup, setup, or any flow with several screens or steps.
- **Personas:** 2 or more. The default is Frustrated User, A11y Expert, and UI/UX Expert. Add Stakeholder when the flow ends in a conversion, Growth Marketing when it includes sharing or referral, or both (5 personas at most).
- **Requirement:** a flow with at least two identifiable steps. If the evidence shows only one screen, say so and run the Audit workflow instead.

## Steps

### 1. Map the flow

List the steps in order, numbered, each with a short name and the screen or evidence it comes from. Label inferred steps (e.g. a confirmation email that is implied but not shown) as **Inferred**. Note the user's goal and the entry point.

### 2. Step-by-step review

For each step:

- **What the user sees and must do:** one line, from the evidence.
- **Persona notes:** each selected persona adds 0–3 notes. A persona with nothing material to add at a step stays silent. Do not write filler like "looks fine". Each note uses a compact form of the Finding contract:

  ```text
  [Persona] · [Critical | Major | Minor] · [Observed | Inferred | To verify]: [finding] → Fix: [change]
  ```

- **Step verdict:**
  - **Blocker:** a Critical issue whose effect on completing the step is Observed. Either the design leaves no way forward, or supplied metrics show most users fail at this step.
  - **Friction:** any Major issue, or a Critical issue whose blocking effect is Inferred or To verify (for example, an Observed contrast failure whose effect on completion is not measured).
  - **Pass:** only Minor issues, or none.

  When a Friction verdict rests only on Inferred or To verify issues, write it as **Friction (to verify)** and list the question that would confirm it under **To verify**. Severity and evidence stay independent: an unconfirmed Major issue is still Major.

Carry context forward. Personas notice problems that come from earlier steps, such as re-entered data, lost state, or broken promises from a previous screen. Write a cross-step issue once, at the step where users feel it, and name the step where it originates. List it once in Top Fixes.

### 3. Journey summary

After the last step:

- **Journey heatmap:** a compact table with steps as rows and personas as columns. Each cell holds the highest severity that persona found at that step (C / Mj / Mn / –). Keep it narrow. Use a stacked list instead when there are more than 4 personas or the user asks for a compact or mobile layout.
- **Drop-off risk:** the step most likely to lose users, and why.
- **What works:** up to 3 strengths worth preserving, each tied to a step.
- **Top fixes:** up to 5 deduplicated fixes across the whole journey, ranked by impact, each using the full Finding contract.
- **To verify:** open questions the evidence could not answer.

## Output

```text
# Design Walkthrough - [Flow Name]
## Flow Map
## Step 1 - [Name]
...one section per step...
## Journey Summary
### Heatmap
### Drop-off Risk
### What Works
### Top Fixes
### To Verify
```

## Quality checks

- Every step in the map is reviewed, and every review step appears in the map.
- Notes are tied to the specific step, not to the product in general.
- Step verdicts match the notes.
- The top fixes contain no duplicates across steps and personas.
