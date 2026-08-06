# Design AI Skills by Faris

![Design AI Skills by Faris: two bilingual skills for design critique and persuasive thinking](assets/cover.svg)
![Design AI Skills by Faris Thumbnail](assets/thumbnail.svg)

Two ready-to-use AI skills for people who design, present, and defend ideas. Use them with **Claude** or **Codex** in English or Arabic, with no coding required.

[English](#english) | [العربية](#العربية) | [Version 0.9.0](CHANGELOG.md#090---2026-08-06)

---

## English

### Choose a skill

| Skill | Best for | What you receive |
| --- | --- | --- |
| [`design-audit-panel`](design-audit-panel/) | Reviewing a screen, flow, product concept, or feature before building or shipping | An executive summary and prioritized reports from up to seven expert perspectives |
| [`devils-advocate-and-convincer`](devils-advocate-and-convincer/) | Pressure-testing an idea before a pitch, proposal, negotiation, or difficult conversation | Specific objections, persuasive responses, and a presentation-ready narrative |

### Install

Download this repository, then install only the skill folder you want or install both.

#### Claude

1. In **Settings > Capabilities**, enable **Code execution and file creation**. Team or Enterprise owners may need to enable Skills in the organization settings.
2. Compress the complete skill folder as a ZIP file. Keep `SKILL.md` and any `references` folder together.
3. Open **Customize > Skills**, select **+ > Create skill > Upload a skill**, and upload the ZIP file.
4. Make sure the skill is enabled, then name it in your request or describe the task naturally.

See Anthropic's current [custom skill instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude) for plan and organization details.

#### Codex

1. Copy each complete skill folder into `.agents/skills/` inside a repository for project use, or into `$HOME/.agents/skills/` for personal use everywhere.
2. Start or restart Codex if the new skill does not appear automatically.
3. Type `$design-audit-panel` or `$devils-advocate-and-convincer` in your prompt. You can also run `/skills` in Codex CLI or the IDE extension to find installed skills.

The Codex paths and invocation syntax follow the current [official OpenAI skill guidance](https://developers.openai.com/codex/skills/).

### Try it

**Design audit**

```text
$design-audit-panel
Audit this checkout flow for first-time mobile shoppers: [attach screenshots or add a Figma link].
Use the Frustrated User, Accessibility, and UI/UX perspectives.
Return the result in Markdown.
```

Expected output: a cross-perspective summary, ranked issues, a consolidated action plan, and one structured report per selected perspective.

**Devil's Advocate + Convincer**

```text
$devils-advocate-and-convincer
Name: Four-day design sprint
What: Replace our current five-day workshop with a focused four-day format.
Why: Reduce stakeholder fatigue while preserving decision quality.
Audience: A skeptical product director.
```

Expected output: realistic objections grouped by risk, a direct response to each objection, and a 200-400 word pitch ready to present.

### Compatibility and behavior

- Both skills follow the language of your request unless you ask for another language.
- Markdown works everywhere and is the default when file-generation tools are unavailable.
- Word, PDF, Figma, and image handling depend on the tools connected to your Claude or Codex environment.
- When a linked design cannot be opened, the skill asks for screenshots or a short description instead of pretending it saw the design.
- The collection uses one shared version number. The current release is **v0.9.0**.

### Troubleshooting

| Problem | What to do |
| --- | --- |
| The skill is not listed | Confirm the complete folder was installed and that `SKILL.md` is directly inside it, then restart the app. |
| A Figma link cannot be read | Connect a Figma tool if your environment supports one, or attach exported screenshots. |
| Word or PDF is unavailable | Ask for Markdown; the report content remains the same. |
| The result is too long on mobile | Ask for a compact layout or fewer expert perspectives. |
| The skill responds in the wrong language | Say `Answer in English` or `أجب بالعربية` in the request. |

---

## العربية

مهارتان جاهزتان للاستخدام مع أدوات الذكاء الاصطناعي للمصممين وكل من يراجع الأفكار أو يقدمها أو يدافع عنها. تعملان مع **Claude** و**Codex** بالعربية أو الإنجليزية، ولا تحتاجان إلى خبرة برمجية.

### اختر المهارة المناسبة

| المهارة | مناسبة لـ | النتيجة التي تحصل عليها |
| --- | --- | --- |
| [`design-audit-panel`](design-audit-panel/) | مراجعة شاشة أو رحلة مستخدم أو فكرة منتج أو ميزة قبل تنفيذها أو إطلاقها | ملخص تنفيذي وتقارير مرتبة حسب الأولوية من سبع وجهات نظر متخصصة كحد أقصى |
| [`devils-advocate-and-convincer`](devils-advocate-and-convincer/) | اختبار الفكرة قبل عرض أو اقتراح أو تفاوض أو محادثة صعبة | اعتراضات واقعية وردود مقنعة وخطاب جاهز للتقديم |

### التثبيت

نزّل المستودع، ثم ثبّت مجلد المهارة التي تريدها أو ثبّت المجلدين معاً.

#### Claude

1. فعّل **Code execution and file creation** من **Settings > Capabilities**. قد يحتاج مالك حساب Team أو Enterprise إلى تفعيل Skills من إعدادات المؤسسة.
2. اضغط مجلد المهارة كاملاً في ملف ZIP، مع إبقاء `SKILL.md` ومجلد `references` إن وجد معاً.
3. افتح **Customize > Skills**، ثم اختر **+ > Create skill > Upload a skill** وارفع ملف ZIP.
4. تأكد من تفعيل المهارة، ثم اذكر اسمها في طلبك أو اشرح المهمة بطريقة طبيعية.

راجع [تعليمات Anthropic الرسمية](https://support.claude.com/en/articles/12512180-use-skills-in-claude) لمعرفة تفاصيل الخطط وحسابات المؤسسات.

#### Codex

1. انسخ مجلد كل مهارة كاملاً إلى `.agents/skills/` داخل المستودع لاستخدامها في مشروع محدد، أو إلى `$HOME/.agents/skills/` لاستخدامها في كل مشاريعك.
2. أعد تشغيل Codex إذا لم تظهر المهارة تلقائياً.
3. اكتب `$design-audit-panel` أو `$devils-advocate-and-convincer` في طلبك. ويمكنك استخدام `/skills` في Codex CLI أو إضافة IDE للعثور على المهارات المثبتة.

### جرّب المهارات

**تدقيق التصميم**

```text
$design-audit-panel
راجع رحلة الدفع هذه لمستخدم يشتري من الهاتف لأول مرة: [أرفق الصور أو رابط Figma].
استخدم وجهات نظر المستخدم المحبط وخبير الوصول وخبير UI/UX.
أعد النتيجة بصيغة Markdown.
```

النتيجة المتوقعة: ملخص مشترك، مشكلات مرتبة حسب الأولوية، خطة عمل موحدة، وتقرير منظم لكل وجهة نظر اخترتها.

**محامي الشيطان + الإقناع**

```text
$devils-advocate-and-convincer
الاسم: ورشة تصميم من أربعة أيام
الفكرة: استبدال ورشة الأيام الخمسة الحالية بصيغة مركزة من أربعة أيام.
السبب: تقليل إرهاق أصحاب المصلحة مع الحفاظ على جودة القرارات.
الجمهور: مدير منتج متشكك.
```

النتيجة المتوقعة: اعتراضات واقعية مصنفة حسب المخاطر، رد مباشر على كل اعتراض، وخطاب من 200 إلى 400 كلمة جاهز للتقديم.

### التوافق والسلوك

- تتبع المهارتان لغة طلبك ما لم تطلب لغة أخرى.
- تعمل صيغة Markdown في كل البيئات، وهي البديل الافتراضي عندما لا تتوفر أدوات إنشاء الملفات.
- يعتمد إنشاء Word أو PDF وفتح Figma والصور على الأدوات المتصلة ببيئة Claude أو Codex لديك.
- إذا تعذر فتح رابط التصميم، تطلب المهارة صوراً أو وصفاً مختصراً بدلاً من ادعاء أنها شاهدت التصميم.
- تستخدم المجموعة رقم إصدار واحداً مشتركاً. الإصدار الحالي هو **v0.9.0**.

### حل المشكلات

| المشكلة | الحل |
| --- | --- |
| المهارة لا تظهر | تأكد من تثبيت المجلد كاملاً ومن وجود `SKILL.md` داخله مباشرة، ثم أعد تشغيل التطبيق. |
| لا يمكن قراءة رابط Figma | اربط أداة Figma إذا كانت بيئتك تدعمها، أو أرفق صوراً مصدرة. |
| Word أو PDF غير متاح | اطلب Markdown؛ سيبقى محتوى التقرير نفسه. |
| النتيجة طويلة على الهاتف | اطلب تنسيقاً مختصراً أو عدداً أقل من وجهات النظر. |
| لغة الإجابة غير صحيحة | أضف `أجب بالعربية` أو `Answer in English` إلى طلبك. |

---

## Versioning / الإصدارات

This repository follows [Semantic Versioning](https://semver.org/):

- **Patch / تصحيح** (`0.9.1`): fixes and wording improvements that preserve behavior.
- **Minor / فرعي** (`0.10.0`): new compatible capabilities or skills.
- **Major / رئيسي** (`1.0.0`, then `2.0.0`): stable milestones or breaking behavior changes.

Release notes live in [`CHANGELOG.md`](CHANGELOG.md), and the current machine-readable version lives in [`VERSION`](VERSION).

## License / الترخيص

[CC BY 4.0](LICENSE) - use, remix, and share with credit to Ahmed Faris (فارس المجرة).

Built and shared by [Ahmed Faris](https://afaris.me) - فارس المجرة.
