# One-Prompt Installation / التثبيت بأمر واحد

Copy one of the prompts below into an AI agent that can access the web and create or update files. The prompt installs the selected skill without downloading a ZIP or cloning the full repository.

A prompt cannot bypass an agent's security permissions. If the agent cannot browse the web or write files, it must explain that persistent installation is unavailable instead of claiming success.

## English prompt

```text
Install skills from the Design AI Skills by Faris collection.

Repository: https://github.com/alfaris/Design-AI-Skills-by-Faris
Raw file base: https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main

First, ask me to choose one option:
1. design-audit-panel
2. devils-advocate-and-convincer
3. both skills

Before changing anything:
- Check that you can access the web and create or update files in this environment.
- Detect the skills directory supported by this agent. Prefer the current project's documented skills directory; otherwise use the agent's standard user-level skills directory. Do not invent a path silently.
- Show me the selected skills and the exact target directory, then ask for confirmation.
- If web access or file-writing permission is unavailable, stop and say that you cannot persist the installation. Do not claim that the skill is installed. Offer to use the skill in this conversation if you can retrieve its content, or tell me that I must paste the files into the agent's skills directory.

After confirmation, fetch only the complete folder(s) selected above from the repository's raw files. Preserve each skill folder name and these files:
- SKILL.md
- agents/openai.yaml
- every file in references/, when that directory exists

Use these raw URLs:
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/design-audit-panel/SKILL.md
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/design-audit-panel/agents/openai.yaml
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/design-audit-panel/references/personas.md
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/devils-advocate-and-convincer/SKILL.md
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/devils-advocate-and-convincer/agents/openai.yaml

Before replacing any existing file, show the path and ask for permission. Never overwrite an existing skill silently. Create missing directories as needed, while preserving unrelated files.

When finished, report:
- whether installation completed or was blocked;
- every file created, updated, or skipped;
- the skills directory used;
- how to invoke each installed skill in this agent, including $design-audit-panel and $devils-advocate-and-convincer when supported;
- whether the agent needs to be restarted or reloaded.

Do not download a ZIP, clone the full repository, or report success until the files are actually present at the confirmed target path.
```

## Arabic prompt / الأمر العربي

```text
ثبّت مهارات Design AI Skills by Faris في هذا الوكيل.

المستودع: https://github.com/alfaris/Design-AI-Skills-by-Faris
قاعدة الملفات الخام: https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main

ابدأ بسؤالي عن الخيار المطلوب:
1. design-audit-panel
2. devils-advocate-and-convincer
3. المهارتان معاً

قبل تغيير أي شيء:
- تحقق من قدرتك على الوصول إلى الويب وإنشاء الملفات أو تحديثها في هذه البيئة.
- اكتشف مجلد المهارات الذي يدعمه هذا الوكيل. فضّل مجلد المهارات الموثق للمشروع الحالي، وإلا استخدم مجلد المهارات القياسي للمستخدم في هذا الوكيل. لا تخترع مساراً بصمت.
- اعرض المهارات المختارة والمسار المستهدف الكامل، ثم اطلب تأكيدي.
- إذا لم يتوفر الوصول إلى الويب أو إذن الكتابة، فتوقف واذكر أن التثبيت الدائم غير متاح. لا تدّعِ نجاح التثبيت. اعرض استخدام المهارة في هذه المحادثة إذا استطعت جلب محتواها، أو أخبرني أنني أحتاج إلى لصق الملفات في مجلد مهارات الوكيل.

بعد التأكيد، اجلب المجلد أو المجلدات المختارة كاملة من الملفات الخام في المستودع. حافظ على اسم كل مجلد مهارة وعلى هذه الملفات:
- SKILL.md
- agents/openai.yaml
- كل ملف داخل references/ عندما يكون هذا المجلد موجوداً

استخدم هذه الروابط الخام:
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/design-audit-panel/SKILL.md
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/design-audit-panel/agents/openai.yaml
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/design-audit-panel/references/personas.md
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/devils-advocate-and-convincer/SKILL.md
- https://raw.githubusercontent.com/alfaris/Design-AI-Skills-by-Faris/main/devils-advocate-and-convincer/agents/openai.yaml

قبل استبدال أي ملف موجود، اعرض مساره واطلب الإذن. لا تستبدل مهارة موجودة بصمت. أنشئ المجلدات الناقصة عند الحاجة مع الحفاظ على الملفات الأخرى غير المرتبطة.

عند الانتهاء، أبلغني بما يلي:
- هل اكتمل التثبيت أم تعذر؛
- كل ملف تم إنشاؤه أو تحديثه أو تخطيه؛
- مجلد المهارات المستخدم؛
- طريقة تشغيل كل مهارة مثبتة في هذا الوكيل، بما في ذلك $design-audit-panel و$devils-advocate-and-convincer عندما يدعمهما الوكيل؛
- هل يحتاج الوكيل إلى إعادة تشغيل أو إعادة تحميل.

لا تنزّل ملف ZIP ولا تستنسخ المستودع كاملاً، ولا تبلغ عن نجاح التثبيت قبل التأكد من وجود الملفات في المسار المستهدف المؤكد.
```

## Capability boundary / حدود القدرة

This installer prompt is designed for agents with web access and permission to write files. Chat-only agents may be able to use the skill for the current conversation, but no prompt can create a persistent installation without file access.

صُمم أمر التثبيت هذا للوكلاء الذين يملكون وصولاً إلى الويب وإذناً لكتابة الملفات. قد تتمكن الوكلاء النصية فقط من استخدام المهارة في المحادثة الحالية، لكن لا يمكن لأي أمر إنشاء تثبيت دائم من دون الوصول إلى الملفات.
