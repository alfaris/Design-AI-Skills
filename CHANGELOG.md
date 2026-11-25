# Changelog / سجل التغييرات

All notable changes to this collection are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the collection uses [Semantic Versioning](https://semver.org/).

يحتوي هذا الملف على التغييرات المهمة في المجموعة. نتبع أسلوب Keep a Changelog ونستخدم نظام Semantic Versioning.

## [Unreleased] / غير منشور

## [0.10.0] - 2026-11-25

### Changed / تم التغيير

- **Breaking:** renamed `design-audit-panel` to `design-persona-panel`. Remove the old folder and reinstall; `$design-audit-panel` no longer exists.
- Split the persona definitions from the output formats: `references/personas.md` now describes each persona's lens, biases, what they fight for, and natural tensions, and each workflow's structure lives in `references/workflows/`.
- **تغيير جذري:** أُعيدت تسمية `design-audit-panel` إلى `design-persona-panel`. احذف المجلد القديم وأعد التثبيت، فالأمر `$design-audit-panel` لم يعد موجوداً.
- تم فصل تعريف الشخصيات عن صيغ المخرجات: يصف `references/personas.md` الآن منظور كل شخصية وتحيزاتها وما تدافع عنه ونقاط التوتر الطبيعية بينها، بينما توجد بنية كل نمط عمل في `references/workflows/`.
- Updated the installer, validator, and changelog links to the repository's current name, `alfaris/Design-AI-Skills`. The old `Design-AI-Skills-by-Faris` URLs still redirect, but the installer no longer depends on that redirect.
- تم تحديث روابط أمر التثبيت وأداة التحقق وسجل التغييرات إلى الاسم الحالي للمستودع `alfaris/Design-AI-Skills`. ما زالت روابط `Design-AI-Skills-by-Faris` القديمة تُحوَّل تلقائياً، لكن أمر التثبيت لم يعد يعتمد على هذا التحويل.

### Added / تمت الإضافة

- Added four persona workflows: **Audit** (the previous behavior), **Debate** (personas argue a trade-off and a neutral moderator decides), **Roundtable** (personas agree on one ranked priority list with a dissent log), and **Walkthrough** (personas step through a flow screen by screen).
- تمت إضافة أربعة أنماط عمل للشخصيات: **التدقيق** (السلوك السابق)، و**المناظرة** (تتجادل الشخصيات حول مفاضلة ويحكم وسيط محايد)، و**الطاولة المستديرة** (تتفق الشخصيات على قائمة أولويات واحدة مع سجل للاعتراضات)، و**الجولة خطوة بخطوة** (تمر الشخصيات على الرحلة شاشة بشاشة).
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

[Unreleased]: https://github.com/alfaris/Design-AI-Skills/compare/v0.10.0...HEAD
[0.10.0]: https://github.com/alfaris/Design-AI-Skills/releases/tag/v0.10.0
[0.9.1]: https://github.com/alfaris/Design-AI-Skills/releases/tag/v0.9.1
[0.9.0]: https://github.com/alfaris/Design-AI-Skills/releases/tag/v0.9.0
