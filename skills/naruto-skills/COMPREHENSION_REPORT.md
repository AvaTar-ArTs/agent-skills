# naruto-skills: Comprehension and Use Report

## Executive interpretation

This repository is a Claude Code marketplace plugin that acts as a content-to-visual compiler. It transforms a source article, webpage, tutorial, story, or pasted brief into an intermediate semantic plan, then routes that plan to image generation or publication-oriented output.

It is not a single Naruto-specific generator and it is not yet a fully packaged application. It is primarily an instruction-driven skill catalog with four creative orchestration skills and four executable utilities.

## Actual composition

```text
source URL / article / brief
        ↓
semantic analysis and language detection
        ↓
objectives, narrative structure, layout, style, and character decisions
        ↓
prompt / storyboard / structured-content artifacts
        ↓
image-gen backend or PDF/article output
        ↓
review and publication
```

### Marketplace groups

| Group | Skills | Role |
|---|---|---|
| `content-skills` | `cover-image`, `comic`, `infographic`, `article-illustrator` | Creative planning and media composition instructions |
| `ai-generation-skills` | `image-gen` | Executable OpenAI/Google image-generation backend |
| `utility-skills` | `url-to-markdown` | Executable Chrome-CDP research/content ingestion |
| `dev-skills` | `smart-git-commit` | Executable repository change analysis and commit workflow |

`release-skills` is a local Claude skill and is not registered in the marketplace manifest.

## What each skill actually does

### `url-to-markdown`

The ingestion layer. It launches Chrome through DevTools Protocol, optionally waits for login or user interaction, scrolls lazy-loaded content, extracts metadata and article/main content, converts HTML to Markdown, and writes the result under a domain/slug-based data directory.

Best use: ingest research, product pages, documentation, public articles, or authenticated source material before visual processing.

### `article-illustrator`

The editorial illustration layer. It reads an article, identifies where visuals improve comprehension, proposes illustration positions and styles, creates prompts, generates assets, and inserts Markdown image references and alt text.

Best use: knowledge articles, workflow documentation, product explainers, and long-form posts.

### `infographic`

The information-design layer. It separates information architecture from visual aesthetics: 20 layouts cover relationships such as timelines, systems, metrics, cycles, and taxonomies; 17 styles control visual treatment. It creates analysis, learning objectives, structured content, prompt instructions, and a final infographic.

Best use: agent/MCP architectures, production pipelines, catalog overviews, metrics, ecosystem maps, and educational summaries.

### `comic`

The narrative-visualization layer. It turns biographies, tutorials, technical concepts, and stories into page plans, character references, multiple storyboard variants, sequential image prompts, page images, and an optional PDF assembled by `merge-to-pdf.ts`.

Its distinctive method is visual metaphor: technical concepts become gadgets, action, or explorable spaces rather than static talking heads. The reusable student/mentor/antagonist pattern supports learner confusion, demonstration, and misconception.

Best use: AI tutorials, origin stories, brand lore, music mythology, and approachable technical education.

### `cover-image`

The distribution-thumbnail layer. It analyzes a topic, tone, and symbolic visual metaphor to create a single cover image, with title/no-title and aspect-ratio controls.

Best use: article headers, social cards, product launches, and media entries.

### `image-gen`

The shared execution backend. It supports Google multimodal/Imagen and OpenAI image APIs, prompt files, reference images, aspect ratios, quality presets, retries, and JSON output. API keys and model selection are environment-driven.

### `smart-git-commit`

The repository operations layer. It analyzes changes, suggests Conventional Commit types and splits, optionally runs checks, stages changes, and commits.

### `release-skills`

The release checklist layer. It instructs an agent to update the changelog, marketplace version, README, commit, and tag. It is a workflow specification rather than an executable release program.

## Why this matters for Steven's ecosystem

This package can become a content-intelligence layer for avatararts.org, AI workflow documentation, lore systems, catalog intelligence, and automated publishing:

1. Ingest source material with `url-to-markdown`.
2. Convert the source into article illustrations, infographics, comics, or covers.
3. Preserve the intermediate artifacts as provenance: source, analysis, objectives, storyboard, prompt, asset, and publication target.
4. Route image creation through a provider-neutral `image-gen` adapter.
5. Send approved outputs into the broader media catalog and publishing pipeline.

High-value combinations include:

- AI workflow article → `url-to-markdown` → `article-illustrator` with `blueprint`, `editorial`, or `intuition-machine`.
- Agent/MCP architecture → `infographic` with `structural-breakdown` + `technical-schematic`.
- Content-production lifecycle → `infographic` with `circular-flow` + `craft-handmade` or `subway-map`.
- Technical tutorial → `comic` with `ohmsha` + `webtoon`.
- Personal or brand origin story → `comic` with `warm` + `standard`.
- Product launch → `cover-image` with `bold-editorial`, followed by `article-illustrator` with `editorial` or `flat`.
- Catalog overview → `infographic` with `bento-grid`, `periodic-table`, or `dashboard`.

## Verified engineering reality

- Original repository-authored prose is now English-clean, but generated output may intentionally be `en`, `zh`, `ja`, or another language.
- Only the image generator, URL converter, comic PDF merger, and Git utility contain TypeScript execution code. The four main content skills depend on the host agent following their instructions.
- There is no `package.json`, lockfile, TypeScript configuration, test suite, CI configuration, or declared dependency manifest.
- The documentation claims no external npm packages, but `image-gen` imports `ai` and `@ai-sdk/google`, and the comic PDF merger imports `pdf-lib`. These dependencies are unpinned and undocumented.
- The marketplace manifest is version `1.1.0`, while the old project guidance claimed `v1.0.0`; version metadata should be reconciled before release.

## Material risks and limitations

1. `smart-git-commit` can auto-stage every repository change when nothing is staged; this may include unrelated or sensitive files.
2. Its commit-message shell construction is vulnerable to shell interpolation. Commit using argument arrays rather than `sh -c`.
3. `url-to-markdown` accepts arbitrary URL schemes recognized by `URL`, uses a persistent authenticated Chrome profile, and can write private captured content to disk. Treat it as an SSRF/privacy boundary.
4. URL capture attaches to the first HTTP page target, which can be the wrong tab during concurrent or pre-existing browser use.
5. Extracted page metadata is inserted into YAML with incomplete escaping; newlines or control characters can corrupt front matter.
6. Image-generation retries are unconditional and may double-charge quota, authentication, or validation failures.
7. Image-generation output paths are resolved and overwritten without an overwrite or symlink policy.
8. The documented `--n` batch behavior is not consistently implemented; current paths save only one image.
9. Comic documentation uses both `3:4` and `2:3` as portrait defaults; normalize this before production.
10. Some visual references are culturally specific or IP-adjacent. Replace Ghibli/Disney-style wording with an original house style for commercial work, and override bilingual `intuition-machine` behavior when strict English output is required.

## Recommended evolution

The proprietary opportunity is not the provider call. It is a provider-neutral semantic manifest containing objects such as `Source`, `Analysis`, `Objective`, `StoryBeat`, `Character`, `Layout`, `Prompt`, `Asset`, `Review`, and `Publication`, with explicit states such as proposed, generated, needs_revision, approved, published, and superseded.

Next engineering steps:

- Add a root package manifest and lockfile with pinned `ai`, `@ai-sdk/google`, and `pdf-lib` versions.
- Add fixture tests for argument parsing, HTML conversion, YAML escaping, URL policy, PDF ordering, and commit-message safety.
- Replace shell-interpolated Git commands and remove silent auto-staging of unrelated files.
- Restrict URL capture to HTTP(S), isolate browser profiles per run, add a concurrency lock, and make private-page persistence explicit.
- Validate provider URLs, downloaded image MIME types and sizes, output paths, and overwrite behavior.
- Reconcile version metadata and keep generated artifacts tied to source and prompt manifests.

## Confidence and boundary

Confidence is high for repository structure, documented workflows, imports, configuration paths, and the language audit. Runtime execution was not performed in this environment because Bun and the undeclared external packages are unavailable here. The report therefore distinguishes verified source behavior from runtime behavior that still needs an environment with declared dependencies.
