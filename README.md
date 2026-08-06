# Design AI Skills by Faris

Two [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) — reusable instruction sets that give Claude a structured expert framework for a specific kind of work. Drop a folder into Claude and it knows how to run the process below.

## What's inside

### 🎨 `design-audit-panel/`
Audits a design, product concept, feature set, or UI from up to seven expert perspectives — Stakeholder, Frustrated User, Developer, Competitor, A11y Expert, UI/UX Expert, and Growth Marketing. Each persona returns Critical Issues, Warnings, What's Working, Opportunities, and a Plan — assembled into one report with an executive summary.

**Use it for:** design reviews, UX audits, "tear apart my design," red-teaming a product before you build or ship it.

### 🥊 `devils-advocate-and-convincer/`
A two-phase framework: first attacks an idea with every realistic objection a skeptical panel would raise, then converts each objection into a persuasive, audience-calibrated response — capped with a presentation-ready pitch.

**Use it for:** pitches, negotiations, stress-testing a business idea, prepping for a hard conversation with investors, clients, or your boss.

## How to use these

**Claude.ai / Claude apps (Skills feature):**
1. Download this repo (or just the folder you want) as a zip.
2. In Claude, go to Settings → Capabilities → Skills, and upload the folder.
3. Ask Claude to do the thing the skill covers (e.g. "review this UI" or "poke holes in this pitch") — Claude will pick up the skill automatically.

**Claude Code / Cowork:**
Drop the folder into your skills directory (typically `/mnt/skills/user/` or your project's `.claude/skills/`), and Claude will surface it the same way.

## Structure

```
claude-skills/
├── design-audit-panel/
│   ├── SKILL.md
│   └── references/
│       └── personas.md
└── devils-advocate-and-convincer/
    └── SKILL.md
```

## License

CC BY 4.0 — use these, remix them, teach with them, just credit Ahmed Faris (فارس المجرة) as the original source. See [LICENSE](./LICENSE) for the full text.

---
Built and shared by **Ahmed Faris** — فارس المجرة
🌐 [afaris.me](https://afaris.me)
📷 Instagram: [ADD_HANDLE]
🎥 [ADD_OTHER_PLATFORM]
