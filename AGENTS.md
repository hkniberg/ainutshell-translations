# AI in a Nutshell - Translations Repository

This repository contains translations for the book "Generative AI in a Nutshell - How to Survive and Thrive in the Age of AI". It is designed to be translator-friendly, so non-technical contributors can easily review and improve translations without dealing with branches or complex git workflows.

## Repository Structure

```
ainutshell-translations/
├── manuscript/
│   ├── manuscript-en.md          # English (source)
│   ├── manuscript-da.md          # Danish translation
│   ├── manuscript-es.md          # Spanish translation
│   ├── ... (other languages)
│   ├── resources/                # Default images (English)
│   └── resources-da/             # Danish translated images (optional)
└── metadata/
    ├── metadata-en.md            # English metadata
    ├── metadata-da.md            # Danish metadata
    └── ... (other languages)
```

## Translation Files

- **Manuscript files**: `manuscript/manuscript-<lang>.md` - The main book content
- **Metadata files**: `metadata/metadata-<lang>.md` - Title, subtitle, author info, etc.

## Translated Images (Optional)

If a translator wants to translate images containing text:

1. Create a folder `manuscript/resources-<lang>/` (e.g., `manuscript/resources-da/` for Danish)
2. Add translated images with the language suffix: `020-roles-da.jpg` instead of `020-roles.jpg`
3. Only include images that have been translated - missing images will fall back to the English version

## Available Languages

| Code | Language |
|------|----------|
| ar | Arabic |
| bs | Bosnian |
| cs | Czech |
| da | Danish |
| de | German |
| el | Greek |
| es | Spanish |
| fr | French |
| he | Hebrew |
| hi | Hindi |
| hr | Croatian |
| hu | Hungarian |
| id | Indonesian |
| it | Italian |
| ja | Japanese |
| ko | Korean |
| nb | Norwegian Bokmål |
| nl | Dutch |
| pa | Punjabi |
| pl | Polish |
| pt-BR | Portuguese (Brazil) |
| pt-PT | Portuguese (Portugal) |
| ro | Romanian |
| sr-Latn | Serbian (Latin) |
| sv | Swedish |
| th | Thai |
| tr | Turkish |
| uk | Ukrainian |
| vi | Vietnamese |
| zh-Hans | Chinese (Simplified) |
| zh-Hant | Chinese (Traditional) |

## Publishing Workflow

This repo is the **source of truth for translations**. The publishing workflow is:

1. Translators submit improvements via PR or email
2. Changes are merged into this repository
3. An import script in the [ainutshell](https://github.com/hkniberg/ainutshell) repo pulls translations and pushes to the appropriate publishing branches

The ainutshell repo handles all publishing complexity (branch management, image path updates, Leanpub integration).

## For AI Agents

When helping with this repository:

- **Translator assistance**: Help review and improve translations by comparing with the English source (`manuscript-en.md`)
- **Keep it simple**: This repo avoids branches - everything is on main
- **Follow translator guidelines**: See README.md for detailed guidelines on style, terminology, and special tags
