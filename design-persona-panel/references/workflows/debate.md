# Workflow: Debate

Two or more personas argue one explicit question about the design. A neutral moderator then turns the
debate into a decision the team can act on.

- **Use when:** the user faces a trade-off, compares options, or asks "should we…?", "A or B?", or asks personas to argue or debate.
- **Personas:** 2 or more. With no personas named, pick the 2 who would genuinely take opposite sides of this motion. Start from the natural tensions in `personas.md`, check each candidate's **Fights for**, and say in one line why you chose the pair, in the note block under the workflow line. If the evidence is so one-sided that no persona would honestly defend one option, a persona may argue a specific alternative (such as a lighter version of the option) instead. Use 3 or 4 only when the question has more than two real sides.
- **Moderator:** a neutral voice, not one of the personas. It does not argue. It summarizes, judges evidence quality, and recommends.

## Steps

### 1. Motion

State the motion as one decidable question, e.g. "Should guest checkout replace the mandatory signup step?"

- If the user gave a question, restate it precisely.
- If the user gave only a design and asked for a debate, derive the most consequential open trade-off from the evidence, state it, and label it as the moderator's choice.
- If the options are unclear and would change the debate materially, ask one focused question.

Add a short context line: product, audience, stage, and what the decision affects.

### 2. Opening statements

Each persona, in turn:

- **Position:** one sentence. Positions may be for, against, or a specific alternative.
- **Arguments:** the 2–3 strongest arguments from its own lens. Each one names its mechanism, cites the evidence with an **Observed / Inferred / To verify** label, and states the consequence. Arguments use this compact form, not the full Finding contract. Fixes and guardrails belong in the moderator verdict.

### 3. Rebuttals

Run 1 round by default. Run up to 3 rounds only when the user asks for more or a key point is still contested.

- Each rebuttal must quote or name a specific opposing claim and answer it with evidence, a counter-mechanism, or a narrower scope.
- No strawmen: restate the opponent's point fairly before answering it.
- Do not repeat opening arguments without engaging the opponent's claim.

### 4. Concessions

Each persona states, in one or two lines, what it now accepts from the other side and what it still holds as non-negotiable.

### 5. Moderator verdict

- **Recommendation:** the decision, which may be a hybrid or a staged rollout.
- **Why:** the decisive arguments and the evidence quality behind them.
- **Conditions and guardrails:** what must be true or monitored for the recommendation to hold.
- **Unresolved:** points the evidence cannot settle.
- **Settling test:** the cheapest experiment, metric, or research question that would resolve the disagreement.
- **Confidence:** High, Medium, or Low, with one line explaining why.

If the evidence is too weak to choose, say so and make the settling test the recommendation.

## Output

```text
# Design Debate - [Motion]
## Motion & Context
## Opening Statements
### [Persona]: [one-line position]
## Rebuttals
### Round 1
## Concessions
## Moderator Verdict
```

Use a short side-by-side table only when the arguments fit in short cells. Otherwise use stacked subsections, and always use stacked subsections for Arabic or mobile readers.

## Quality checks

- The motion is one decidable question.
- Every argument is grounded in evidence and labeled.
- Every rebuttal answers a specific opposing claim.
- The verdict follows from the arguments and does not introduce new evidence.
- The verdict is not a forced compromise. A hybrid is legitimate only when it keeps the decisive benefit each side argued for and the evidence supports both. It is a forced compromise when it splits the difference without answering a decisive argument. When one side's decisive argument stands unrebutted, choose that side.
