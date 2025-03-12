# AI in a Nutshell - Translation guide

<img src="manuscript/resources/title_page.png" width="300" alt="Book Cover">

This is the source code for the book "Generative AI in a Nutshell - How to Survive and Thrive in the Age of AI", by Henrik Kniberg. The book is based on the [video with the same title](https://www.youtube.com/watch?v=2IK3DFHRFfw).

This repository is public to enable community-submitted improvements to the AI-translated versions. See below for more details.

## Guide for Translators

If you are interested in helping to improve the translations, then you have come to the right place!

### Important Note

**AI-generated translations already exist** for several languages. Your role as a translator is to **review and improve** these existing translations rather than creating new ones from scratch. This makes the process much faster and allows you to focus on refining the language, correcting errors, and ensuring the technical content is accurately conveyed.

### Getting Started

1. **Find your language**: Check if your target language already exists in the repository. Each language has two key files:

   - `manuscript/manuscript-xx.md` (where `xx` is the language code)
   - `metadata/metadata-xx.md` (where `xx` is the language code)

2. **Language codes**: We use standard language codes (e.g., `sv` for Swedish, `fr` for French). For languages with script variants, we use extended codes (e.g., `zh-Hans` for Simplified Chinese, `sr-Latn` for Serbian in Latin script).

3. **Reference materials**: Use the English files (`manuscript-en.md` and `metadata-en.md`) as reference to ensure accuracy of the translation.

### Translation Process

#### Option 1: Using GitHub (Preferred)

If you're familiar with GitHub:

1. Fork this repository
2. Create a new branch for your translation improvements
3. Download the existing AI-translated files for your language:
   - `manuscript/manuscript-xx.md`
   - `metadata/metadata-xx.md`
4. Also download the English files for reference:
   - `manuscript/manuscript-en.md`
   - `metadata/metadata-en.md`
5. Review and improve the existing translation, keeping the Markdown formatting intact
6. In the metadata file, update the "Translator credits" section with your name
7. Submit a Pull Request with your improved translation

#### Option 2: Direct File Submission

If you're not familiar with GitHub:

1. Download the existing AI-translated files for your language:
   - `manuscript/manuscript-xx.md`
   - `metadata/metadata-xx.md`
2. Also download the English files for reference:
   - `manuscript/manuscript-en.md`
   - `metadata/metadata-en.md`
3. Review and improve the existing translation, keeping the Markdown formatting intact
4. In the metadata file, update the "Translator credits" section with your name
5. Email your improved files to ainutshell@ymnig.com with the subject "Translation Improvement: [Your Language]"

### Translation Guidelines

1. **Maintain formatting**: Keep all Markdown formatting (headings, lists, code blocks, etc.) intact.
2. **Preserve code examples**: Do not translate code examples unless they contain comments.
3. **Keep image references**: Don't modify image references or paths.
4. **Consistent terminology**: Try to be consistent with technical terms throughout the translation.
5. **Cultural adaptation**: You may adapt examples to be more relevant to your language's cultural context, as long as the technical meaning remains the same.
6. **Focus on quality**: Pay special attention to areas where the AI translation might be awkward, overly literal, or technically inaccurate.

### Metadata File Structure

The metadata file (`metadata-xx.md`) contains important information about the book in your language. It has the following sections:

```
# Title
[Translated title]

# Subtitle
[Translated subtitle]

# Tagline
[Translated tagline]

# About the book
[Translated book description]

# Author blurb
[Translated author information]

# Meta description
[Translated meta description]

# Translator credits
This translation was originally done by AI, and then reviewed and improved by [Your Name].
```

### Questions or Issues?

If you have any questions or encounter issues during the translation process, please open an issue in this repository or email ainutshell@ymnig.com.

Thank you for contributing to making "Generative AI in a Nutshell" accessible to more readers around the world!

## Translations

Here is a link to each translation.

- ![](https://img.shields.io/badge/done-green) = The translation is already finished and reviewed.
- ![](https://img.shields.io/badge/todo-red) = AI translation is done, but human review & improvement is needed

| Language                                                         | Manuscript                                                | Metadata                                            | Amazon link                                                                                 | Leanpub link                                      |
| ---------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| English ![](https://img.shields.io/badge/done-green)             | [manuscript-en.md](manuscript/manuscript-en.md)           | [metadata-en.md](metadata/metadata-en.md)           | [Amazon](https://www.amazon.com/Generative-AI-Nutshell-Survive-Thrive-ebook/dp/B0DSBFN12W/) | [Leanpub](https://leanpub.com/ainutshell)         |
| Arabic ![](https://img.shields.io/badge/todo-red)                | [manuscript-ar.md](manuscript/manuscript-ar.md)           | [metadata-ar.md](metadata/metadata-ar.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-ar)      |
| Bosnian ![](https://img.shields.io/badge/todo-red)               | [manuscript-bs.md](manuscript/manuscript-bs.md)           | [metadata-bs.md](metadata/metadata-bs.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-bs)      |
| Chinese (Simplified) ![](https://img.shields.io/badge/todo-red)  | [manuscript-zh-Hans.md](manuscript/manuscript-zh-Hans.md) | [metadata-zh-Hans.md](metadata/metadata-zh-Hans.md) |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-zh-Hans) |
| Chinese (Traditional) ![](https://img.shields.io/badge/todo-red) | [manuscript-zh-Hant.md](manuscript/manuscript-zh-Hant.md) | [metadata-zh-Hant.md](metadata/metadata-zh-Hant.md) |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-zh-Hant) |
| Czech ![](https://img.shields.io/badge/todo-red)                 | [manuscript-cs.md](manuscript/manuscript-cs.md)           | [metadata-cs.md](metadata/metadata-cs.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-cs)      |
| Danish ![](https://img.shields.io/badge/todo-red)                | [manuscript-da.md](manuscript/manuscript-da.md)           | [metadata-da.md](metadata/metadata-da.md)           | [Amazon](https://www.amazon.de/dp/B0DWWVP5FM)                                               | [Leanpub](https://leanpub.com/ainutshell-da)      |
| German ![](https://img.shields.io/badge/todo-red)                | [manuscript-de.md](manuscript/manuscript-de.md)           | [metadata-de.md](metadata/metadata-de.md)           | [Amazon](https://www.amazon.de/dp/B0DW4G7D6V)                                               | [Leanpub](https://leanpub.com/ainutshell-de)      |
| Greek ![](https://img.shields.io/badge/todo-red)                 | [manuscript-el.md](manuscript/manuscript-el.md)           | [metadata-el.md](metadata/metadata-el.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-el)      |
| Spanish ![](https://img.shields.io/badge/todo-red)               | [manuscript-es.md](manuscript/manuscript-es.md)           | [metadata-es.md](metadata/metadata-es.md)           | [Amazon](https://www.amazon.es/dp/B0DWLL4G7J)                                               | [Leanpub](https://leanpub.com/ainutshell-es)      |
| French ![](https://img.shields.io/badge/todo-red)                | [manuscript-fr.md](manuscript/manuscript-fr.md)           | [metadata-fr.md](metadata/metadata-fr.md)           | [Amazon](https://www.amazon.fr/dp/B0DWN1D7LD)                                               | [Leanpub](https://leanpub.com/ainutshell-fr)      |
| Hebrew ![](https://img.shields.io/badge/todo-red)                | [manuscript-he.md](manuscript/manuscript-he.md)           | [metadata-he.md](metadata/metadata-he.md)           | [Amazon](https://www.amazon.com/dp/B0DX681CTT)                                              | [Leanpub](https://leanpub.com/ainutshell-he)      |
| Hindi ![](https://img.shields.io/badge/todo-red)                 | [manuscript-hi.md](manuscript/manuscript-hi.md)           | [metadata-hi.md](metadata/metadata-hi.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-hi)      |
| Croatian ![](https://img.shields.io/badge/todo-red)              | [manuscript-hr.md](manuscript/manuscript-hr.md)           | [metadata-hr.md](metadata/metadata-hr.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-hr)      |
| Hungarian ![](https://img.shields.io/badge/todo-red)             | [manuscript-hu.md](manuscript/manuscript-hu.md)           | [metadata-hu.md](metadata/metadata-hu.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-hu)      |
| Indonesian ![](https://img.shields.io/badge/todo-red)            | [manuscript-id.md](manuscript/manuscript-id.md)           | [metadata-id.md](metadata/metadata-id.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-id)      |
| Italian ![](https://img.shields.io/badge/todo-red)               | [manuscript-it.md](manuscript/manuscript-it.md)           | [metadata-it.md](metadata/metadata-it.md)           | [Amazon](https://www.amazon.it/dp/B0DWZZ1WP7)                                               | [Leanpub](https://leanpub.com/ainutshell-it)      |
| Japanese ![](https://img.shields.io/badge/todo-red)              | [manuscript-ja.md](manuscript/manuscript-ja.md)           | [metadata-ja.md](metadata/metadata-ja.md)           | [Amazon](https://www.amazon.co.jp/dp/B0DX5FZKNX)                                            | [Leanpub](https://leanpub.com/ainutshell-ja)      |
| Korean ![](https://img.shields.io/badge/todo-red)                | [manuscript-ko.md](manuscript/manuscript-ko.md)           | [metadata-ko.md](metadata/metadata-ko.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-ko)      |
| Norwegian Bokmål ![](https://img.shields.io/badge/todo-red)      | [manuscript-nb.md](manuscript/manuscript-nb.md)           | [metadata-nb.md](metadata/metadata-nb.md)           | [Amazon](https://www.amazon.de/dp/B0DXBG3DMF)                                               | [Leanpub](https://leanpub.com/ainutshell-nb)      |
| Dutch ![](https://img.shields.io/badge/todo-red)                 | [manuscript-nl.md](manuscript/manuscript-nl.md)           | [metadata-nl.md](metadata/metadata-nl.md)           | [Amazon](https://www.amazon.nl/dp/B0DWXRZH65)                                               | [Leanpub](https://leanpub.com/ainutshell-nl)      |
| Punjabi ![](https://img.shields.io/badge/todo-red)               | [manuscript-pa.md](manuscript/manuscript-pa.md)           | [metadata-pa.md](metadata/metadata-pa.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-pa)      |
| Polish ![](https://img.shields.io/badge/todo-red)                | [manuscript-pl.md](manuscript/manuscript-pl.md)           | [metadata-pl.md](metadata/metadata-pl.md)           | [Amazon](https://www.amazon.pl/dp/B0DX2B4PVS)                                               | [Leanpub](https://leanpub.com/ainutshell-pl)      |
| Portuguese (Brazil) ![](https://img.shields.io/badge/todo-red)   | [manuscript-pt-BR.md](manuscript/manuscript-pt-BR.md)     | [metadata-pt-BR.md](metadata/metadata-pt-BR.md)     | [Amazon](https://www.amazon.com/dp/B0DWLMVHZ3)                                              | [Leanpub](https://leanpub.com/ainutshell-pt-BR)   |
| Portuguese (Portugal) ![](https://img.shields.io/badge/todo-red) | [manuscript-pt-PT.md](manuscript/manuscript-pt-PT.md)     | [metadata-pt-PT.md](metadata/metadata-pt-PT.md)     | [Amazon](https://www.amazon.es/dp/B0DWLQSS3R)                                               | [Leanpub](https://leanpub.com/ainutshell-pt-PT)   |
| Romanian ![](https://img.shields.io/badge/todo-red)              | [manuscript-ro.md](manuscript/manuscript-ro.md)           | [metadata-ro.md](metadata/metadata-ro.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-ro)      |
| Serbian (Latin) ![](https://img.shields.io/badge/todo-red)       | [manuscript-sr-Latn.md](manuscript/manuscript-sr-Latn.md) | [metadata-sr-Latn.md](metadata/metadata-sr-Latn.md) |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-sr-Latn) |
| Swedish ![](https://img.shields.io/badge/todo-red)               | [manuscript-sv.md](manuscript/manuscript-sv.md)           | [metadata-sv.md](metadata/metadata-sv.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-sv)      |
| Thai ![](https://img.shields.io/badge/todo-red)                  | [manuscript-th.md](manuscript/manuscript-th.md)           | [metadata-th.md](metadata/metadata-th.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-th)      |
| Turkish ![](https://img.shields.io/badge/todo-red)               | [manuscript-tr.md](manuscript/manuscript-tr.md)           | [metadata-tr.md](metadata/metadata-tr.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-tr)      |
| Ukrainian ![](https://img.shields.io/badge/todo-red)             | [manuscript-uk.md](manuscript/manuscript-uk.md)           | [metadata-uk.md](metadata/metadata-uk.md)           | [Amazon](https://www.amazon.de/dp/B0DX2K51SS)                                               | [Leanpub](https://leanpub.com/ainutshell-uk)      |
| Vietnamese ![](https://img.shields.io/badge/todo-red)            | [manuscript-vi.md](manuscript/manuscript-vi.md)           | [metadata-vi.md](metadata/metadata-vi.md)           |                                                                                             | [Leanpub](https://leanpub.com/ainutshell-vi)      |
