# Changelog / سجل التغييرات

All notable changes to this collection are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the collection uses [Semantic Versioning](https://semver.org/).

يحتوي هذا الملف على التغييرات المهمة في المجموعة. نتبع أسلوب Keep a Changelog ونستخدم نظام Semantic Versioning.

## [Unreleased] / غير منشور

- Added a bilingual one-prompt installer that fetches selected skills directly from GitHub without requiring a ZIP or full repository download.
- The installer confirms the target skills directory, requests overwrite permission, and reports when web or file-writing access prevents persistent installation.
- تمت إضافة أمر تثبيت ثنائي اللغة يجلب المهارات المختارة مباشرة من GitHub من دون الحاجة إلى ملف ZIP أو تنزيل المستودع كاملاً.
- يؤكد أمر التثبيت مجلد المهارات المستهدف ويطلب الإذن بالاستبدال، ويبلغ المستخدم عندما يمنع الوصول إلى الويب أو الكتابة التثبيت الدائم.

## [0.9.1] - 2026-09-02

### Added / تمت الإضافة

- Portable installation guidance for generic `SKILL.md` consumers, `npx skills`, Claude-style local plugins, and Figma-connected workflows.
- Repository contribution guidance and a standard-library skill metadata validator with focused regression tests.

### Changed / تم التغيير

- Clarified the evaluative and decision-support roles of the two skills.
- Added evidence labels, severity guidance, context gates, and anti-fabrication rules while preserving English and Arabic behavior.

## [0.9.0] - 2026-08-06

### Added / تمت الإضافة

- Codex UI metadata for both skills.
- English and Arabic installation, examples, compatibility notes, and troubleshooting.
- Collection-level Semantic Versioning through `VERSION` and this changelog.
- Automatic response-language matching for English and Arabic requests.

### Changed / تم التغيير

- Reworked the repository experience for designers and other nontechnical users.
- Made design-audit file delivery portable across Claude, Codex, and tool-limited environments.
- Clarified missing-context, inaccessible-design, mobile-layout, and output fallback behavior.
- Replaced the oversized thumbnail with a lightweight, accessible SVG.

[Unreleased]: https://github.com/alfaris/Design-AI-Skills-by-Faris/compare/v0.9.1...HEAD
[0.9.1]: https://github.com/alfaris/Design-AI-Skills-by-Faris/releases/tag/v0.9.1
[0.9.0]: https://github.com/alfaris/Design-AI-Skills-by-Faris/releases/tag/v0.9.0
