---
name: devils-advocate-and-convincer
description: Pressure-test an idea by surfacing realistic objections, then turn each objection into an audience-specific response and presentation-ready pitch. Use for pitches, proposals, negotiations, hard conversations, strategic decisions, business ideas, product directions, investor or client preparation, and requests to find risks, poke holes in an idea, overcome objections, or persuade a skeptical audience.
---

# Devil's Advocate + Master Convincer

Stress-test an idea without softening the risks, then build credible responses for the specific audience the user needs to persuade.

This is a **decision-support** skill. Its job is to improve the decision and the user's preparation, not to manufacture certainty or win through manipulation.

## Language

- Write the complete response in the language used by the user unless they explicitly request another language.
- For Arabic, use clear Modern Standard Arabic and preserve established names, measurements, and technical terms where useful.
- Match the audience's likely vocabulary and level of formality.
- Do not ask the user to choose a language when their request already makes it clear.

## Capture the input

Extract five inputs: **Name**, **What**, **Why**, **How**, and **Audience**.

Also establish, when possible: **Decision**, **Stage**, **Reversibility**, **Evidence**, and **Audience authority**. A reversible experiment, an irreversible commitment, and a post-decision defense require different levels of scrutiny.

- Proceed immediately when the user supplies enough context.
- Infer minor gaps from the conversation and disclose the assumptions in one compact section.
- If several audiences are plausible but their objections would differ materially, ask one focused question about who must be convinced and what decision they control.
- If the idea is too vague to assess, ask for one paragraph describing the idea, intended audience, and desired decision. Do not make the user complete a long template.
- Separate **facts**, **assumptions**, **hypotheses**, and **unknowns** before generating objections. Treat user-supplied claims as claims, not verified evidence, unless the user provides supporting material or a connected research capability verifies them.

### Context gate

Before the objection pass, write a compact context profile:

```text
Decision: [what must be decided]
Stage: [exploration | proposal | commitment | retrospective]
Reversibility: [easy | moderate | hard]
Evidence quality: [strong | mixed | weak | absent]
Audience authority: [decider | influencer | approver | affected party]
```

If a missing value changes the level of scrutiny, ask one focused question. Otherwise state the assumption and continue. Match the response pattern to the profile: use experiments for weak evidence and reversible choices, and demand stronger proof and explicit safeguards for hard-to-reverse commitments.

## Phase 1: Devil's Advocate

Surface specific objections across these categories:

1. **Logical weaknesses**: unsupported assumptions, contradictions, market-fit gaps, or weak reasoning.
2. **Practical barriers**: cost, time, execution, technical, resource, legal, or operational constraints.
3. **Social and political risks**: stakeholder resistance, incentives, competition, culture, brand, or reputation.
4. **Psychological pushback**: fear of change, status threats, skepticism, sunk costs, or trust gaps.
5. **Worst-case scenarios**: concrete failure modes, triggers, consequences, and early warning signs.

Aim for two to four substantive objections per relevant category. State briefly when a category does not apply instead of padding it.

Rate each objection as **Critical**, **Major**, or **Minor** using consequence, likelihood, and time to detect. A high-severity objection should identify the decision it could block and the cheapest test or mitigation that would reduce uncertainty.

Use this compact shape for each objection:

```text
Severity: Critical | Major | Minor
Category: [logical | practical | social | psychological | worst-case]
Objection: [specific mechanism]
Evidence status: [fact | assumption | hypothesis | unknown]
Consequence: [what fails and for whom]
Test or safeguard: [cheapest way to reduce the risk]
```

A substantive objection names a mechanism. Replace generic claims such as "this may cost too much" with the specific condition that makes the economics, timing, trust, or execution fail. Never invent facts, market data, regulations, named examples, or financial figures.

## Phase 2: Master Convincer

Respond to every objection with five elements:

- **Reframe**: change the interpretation without denying a legitimate concern.
- **Solution**: give a concrete mitigation, experiment, commitment, threshold, or next step.
- **Technique**: name and apply one fitting persuasion method.
- **Emotional hook**: connect to the audience's real incentives, ambitions, or fears without manipulation.
- **Closing line**: write one confident sentence the user can say aloud.

Choose from anchoring, framing, social proof, authority, scarcity, loss aversion, storytelling, contrast, reciprocity, commitment and consistency, or specificity and numbers. Use social proof or authority only when the user supplied evidence or when a connected research capability can verify the claim. Otherwise recommend the type of proof to gather.

Do not disguise unresolved risk as certainty. The convincing response should become stronger by addressing the objection, not by dismissing it.

When the audience lacks authority to make the decision, adapt the response toward the audience's actual role: influence, evidence gathering, sponsorship, or escalation. When evidence is weak, use a proof-gathering request or reversible pilot instead of social proof, authority, or invented numbers.

## Final narrative

Write a 200-400 word presentation-ready pitch after both phases. Open with the strongest audience-relevant hook, move through the two or three most important objection-response transitions, and close with the strongest defensible line.

Make it sound natural when spoken. Do not repeat the analysis tables or introduce evidence that did not appear earlier.

## Output structure

Use this order:

```text
# [Idea Name] - Devil's Advocate & Convincing Strategy

## Inferred Context
## Executive Summary
## Phase 1: Objections
## Phase 2: Convincing Responses
## Final Narrative
```

Skip **Inferred Context** when the user supplied all essential information.

Use a compact table for Phase 1 when it improves comparison:

```text
| Category | Objection | Why it matters |
```

For Phase 2, use a table only when the cells remain short and readable. Otherwise use one stacked subsection per objection with Reframe, Solution, Technique, Hook, and Closing Line labels. Prefer the stacked layout for Arabic, mobile users, and detailed responses.

Default to inline Markdown. If the user requests a file, use an available platform-native document capability. If that capability is unavailable, return the complete content in Markdown and mention the fallback briefly.

## Quality checks

Before delivering:

- Make every objection specific to the idea and audience.
- Give every major objection a direct response.
- Replace vague solutions with an action, owner, measure, or decision gate when the context supports one.
- Keep the hostile analysis rigorous while keeping the final language professional.
- Flag claims that need research instead of fabricating proof.
- Confirm the final narrative is 200-400 words and matches the user's language.
- Confirm every claim in the final narrative is supported by the earlier analysis, clearly marked as an assumption, or framed as a proposed test.
