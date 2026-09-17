# Contributing

This is a focused collection. A useful change should make one of the two skills more accurate, more actionable, easier to install, or easier to evaluate.

## What to contribute

- Report generic, incorrect, or fabricated output with the prompt and a short description of the expected behavior.
- Improve one skill with a sharper decision rule, a missing edge case, a better example, or clearer evidence handling.
- Request a new skill only when the task is distinct from the existing audit and decision-support boundaries.

## Quality bar

- Write decision rules and workflow gates, not a general knowledge essay.
- Keep findings grounded in supplied evidence and label assumptions or verification needs.
- Preserve the existing English and Arabic behavior and keep corresponding README guidance aligned.
- Keep each skill independently installable with its `SKILL.md`, `agents/openai.yaml`, and references.
- Keep `INSTALL.md` bilingual and synchronize its repository URLs, skill names, required-file list, and permission limits with the README.
- Do not add claims, source material, or examples that require attribution without recording the source.

## Validate before opening a change

Run this from the repository root:

```text
python scripts/validate-skills.py
```

Keep changes focused, do not commit generated files, and add a changelog entry when behavior or packaging changes.