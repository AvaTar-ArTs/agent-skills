# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project overview

`naruto-skills` v1.0.0 is a Claude Code marketplace plugin containing AI-assisted content-generation tools.

- Runtime: Bun executes TypeScript through `npx -y bun`; no build step is required.
- Dependencies: the TypeScript utilities are self-contained and use no external npm packages.
- Browser automation: Chrome DevTools Protocol is used for page capture and automation.
- AI APIs: OpenAI image models and Google Imagen/Gemini.

## Skill architecture

Each skill is a self-contained module:

```text
skills/<skill-name>/
├── SKILL.md           # YAML front matter and instructions
├── scripts/           # TypeScript implementation
│   └── main.ts        # Entry point
└── prompts/           # Optional AI prompt templates
    └── system.md
```

| Group | Purpose | Skills |
|---|---|---|
| `content-skills` | Content generation and publishing | `cover-image`, `comic`, `infographic`, `article-illustrator` |
| `ai-generation-skills` | AI generation backend | `image-gen` |
| `utility-skills` | Content-processing tools | `url-to-markdown` |
| `dev-skills` | Development workflows | `smart-git-commit` |

## Running skills

```bash
npx -y bun skills/<skill>/scripts/main.ts [options]
npx -y bun skills/image-gen/scripts/main.ts --prompt "a cat" --image cat.png
npx -y bun skills/image-gen/scripts/main.ts --prompt "a landscape" --image img.png --ar 16:9 --quality 2k
npx -y bun skills/url-to-markdown/scripts/main.ts <url>
npx -y bun skills/url-to-markdown/scripts/main.ts <url> --wait
```

## Script path resolution

1. Treat the directory containing `SKILL.md` as `SKILL_DIR`.
2. Resolve script paths as `${SKILL_DIR}/scripts/<script-name>.ts`.
3. Replace `${SKILL_DIR}` in documentation with the actual path before execution.

The comic PDF utility is `${SKILL_DIR}/scripts/merge-to-pdf.ts`.

## Image-generation requirements

Skills that need generated images must delegate image creation to the `image-gen` skill. Check the available image-generation skills, read the selected skill's instructions, and ask the user to choose only when multiple suitable providers create a meaningful choice.

Each session creates an independent output directory:

```text
<skill-suffix>/<topic-slug>/
```

- Use a two-to-four-word kebab-case topic slug.
- On collision, append `-YYYYMMDD-HHMMSS`.
- Copy source material as `source-{slug}.{ext}`.
- Name generated images `NN-{type}-[slug].png` with a two-digit sequence.

## Environment variables

| Variable | Purpose |
|---|---|
| `OPENAI_API_KEY` | OpenAI API key |
| `GOOGLE_API_KEY` | Google API key |
| `URL_CHROME_PATH` | Custom Chrome executable path |
| `URL_DATA_DIR` | Data directory for `url-to-markdown` |

Precedence: CLI arguments, `process.env`, project `.env`, then user `.env`.

## Release process

When the user requests a release, use `/release-skills`.

1. Update `CHANGELOG.md`.
2. Increment versions in `.claude-plugin/marketplace.json`.
3. Update `README.md`.
4. Commit all release changes together, then create the tag.

This English-only distribution does not maintain separate translated documentation.

## Adding a skill

1. Create `skills/<name>/SKILL.md` with YAML front matter containing `name` and `description`.
2. Add TypeScript implementation under `skills/<name>/scripts/` when needed.
3. Register the skill in `.claude-plugin/marketplace.json`.
4. Add English documentation and examples to `README.md`.
5. Keep prompts, comments, examples, and user-facing strings in English.

## Code conventions

- Use TypeScript executed by Bun.
- Prefer Node-compatible built-in APIs and avoid unnecessary dependencies.
- Preserve documented CLI contracts.
- Keep secrets in runtime environment variables, never in source.
- Validate user-provided paths before writing output.
- Keep all repository documentation and user-facing output in English.

## Extension support

Skills may load project-level overrides from `.content-gen-skills/<skill-name>/EXTEND.md` and user-level overrides from `~/.content-gen-skills/<skill-name>/EXTEND.md`. Project settings take precedence.
