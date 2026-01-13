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
├── metadata/
│   ├── metadata-en.md            # English metadata
│   ├── metadata-da.md            # Danish metadata
│   └── ... (other languages)
└── scripts/
    └── export-translation.py     # Export script for publishing
```

## Translation Files

- **Manuscript files**: `manuscript/manuscript-<lang>.md` - The main book content
- **Metadata files**: `metadata/metadata-<lang>.md` - Title, subtitle, author info, etc.

## Translated Images (Optional)

If a translator wants to translate images containing text:

1. Create a folder `manuscript/resources-<lang>/` (e.g., `manuscript/resources-da/` for Danish)
2. Add translated images with the **same name** as the original (e.g., `020-roles.jpg`) or with a language suffix (e.g., `020-roles-da.jpg`) - both work
3. Update the manuscript to reference `resources-<lang>/` for translated images
4. Images that are NOT translated should continue to reference `resources/` (the English version)

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
3. Run the export script to push translations to the [ainutshell](https://github.com/hkniberg/ainutshell) repo

### Exporting a translation

To export a translation to the ainutshell publishing repo:

```bash
python scripts/export-translation.py <lang>
```

For example, to export the Danish translation:

```bash
python scripts/export-translation.py da
```

This will:
1. Checkout the `preview-da` branch in the ainutshell repo (assumes sibling directory)
2. Copy `manuscript-da.md` → `manuscript/manuscript.md`
3. Copy `metadata-da.md` → `manuscript/metadata.md`
4. Update the `LEANPUB_METADATA.*` files with content from the metadata file
5. If translated images exist in `resources-da/`, copy them to `resources/` with corrected names and update image references
6. Offer to commit the changes

After committing, the user should push to trigger Leanpub preview generation. Once verified, the user should create a PR from `preview-<lang>` to `publish-<lang>`.

## ainutshell Publishing Repo

The [ainutshell](https://github.com/hkniberg/ainutshell) repo is the publishing repo, optimized for Leanpub. It uses branches to manage different language versions.

### Branch structure

- `preview`: English version of the book, pushing here will cause a new preview version to be generated on Leanpub
- `publish`: English version of the book, pushing here will cause the published version to be updated on Leanpub
- `preview-<lang>`: Version of the book in `<lang>`, pushing here will cause a new preview version to be generated on Leanpub
- `publish-<lang>`: Version of the book in `<lang>`, pushing here will cause the published version to be updated on Leanpub

## For AI Agents

When helping with this repository:

- **Translator assistance**: Help review and improve translations by comparing with the English source (`manuscript-en.md`)
- **Keep it simple**: This repo avoids branches - everything is on main
- **Follow translator guidelines**: See README.md for detailed guidelines on style, terminology, and special tags
