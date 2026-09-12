# naruto-skills

A collection of Claude Code skills shared by Naruto to improve everyday productivity.

## Requirements

- Node.js installed
- Ability to run `npx bun`

## Installation

```bash
# Quick installation (recommended)
npx skills add zlh-428/naruto-skills

# Or register the marketplace in Claude Code
/plugin marketplace add zlh-428/naruto-skills
```

## Available plugins

| Plugin | Description | Included skills |
|---|---|---|
| **content-skills** | Content generation and publishing | `cover-image`, `comic`, `infographic`, `article-illustrator` |
| **ai-generation-skills** | AI image generation | `image-gen` |
| **utility-skills** | Content-processing utilities | `url-to-markdown` |
| **dev-skills** | Development workflows and tools | `smart-git-commit` |

## Skills

### cover-image

Generates hand-drawn article cover images in multiple styles.

```bash
/cover-image path/to/article.md
/cover-image path/to/article.md --style warm
/cover-image path/to/article.md --no-title
```

Available styles: `elegant` (default), `blueprint`, `bold-editorial`, `chalkboard`, `dark-atmospheric`, `editorial-infographic`, `fantasy-animation`, `flat-doodle`, `intuition-machine`, `minimal`, `nature`, `notion`, `pixel-art`, `playful`, `retro`, `sketch-notes`, `vector-illustration`, `vintage`, `warm`, and `watercolor`.

### comic

Creates original educational comics from source material, including storyboards and sequential image generation.

```bash
/comic posts/turing-story/source.md
/comic posts/turing-story/source.md --style dramatic
/comic posts/turing-story/source.md --style "watercolor with soft edges"
/comic posts/turing-story/source.md --layout cinematic --aspect 16:9
/comic posts/turing-story/source.md --lang en
```

| Option | Values |
|---|---|
| `--style` | `classic` (default), `dramatic`, `warm`, `sepia`, `vibrant`, `ohmsha`, `realistic`, `wuxia`, `shoujo`, or a custom description |
| `--layout` | `standard` (default), `cinematic`, `dense`, `splash`, `mixed`, `webtoon` |
| `--aspect` | `3:4` (default portrait), `4:3` (landscape), `16:9` (widescreen) |
| `--lang` | `en` for English, `auto`, or another supported language code |

Styles range from classic ligne claire and realistic digital painting to wuxia, shoujo, and the student-mentor visual-metaphor structure used by Ohmsha guides. Layout definitions are in `skills/comic/references/layouts/`.

### infographic

Analyzes content, recommends combinations from 20 information layouts and 17 visual styles, and generates publication-ready infographics.

```bash
/infographic path/to/content.md
/infographic path/to/content.md --layout hierarchical-layers
/infographic path/to/content.md --style technical-schematic
/infographic path/to/content.md --layout funnel --style corporate-memphis
/infographic path/to/content.md --aspect portrait --lang en
```

| Option | Description |
|---|---|
| `--layout <name>` | Information layout; see `skills/infographic/references/layouts/` |
| `--style <name>` | Visual style; default: `craft-handmade` |
| `--aspect <ratio>` | `landscape` (16:9), `portrait` (9:16), or `square` (1:1) |
| `--lang <code>` | Output language; use `en` for English |

Layouts include `linear-progression`, `binary-comparison`, `comparison-matrix`, `hierarchical-layers`, `tree-branching`, `hub-spoke`, `structural-breakdown`, `bento-grid`, `iceberg`, `bridge`, `funnel`, `isometric-map`, `dashboard`, `periodic-table`, `comic-strip`, `story-mountain`, `jigsaw`, `venn-diagram`, `winding-roadmap`, and `circular-flow`.

Styles include `craft-handmade` (default), `claymation`, `kawaii`, `storybook-watercolor`, `chalkboard`, `cyberpunk-neon`, `bold-graphic`, `aged-academia`, `corporate-memphis`, `technical-schematic`, `origami`, `pixel-art`, `ui-wireframe`, `subway-map`, `ikea-manual`, `knolling`, and `lego-brick`.

### article-illustrator

Analyzes an article and generates illustrations where visuals improve understanding.

```bash
/article-illustrator path/to/article.md
/article-illustrator path/to/article.md --style warm
/article-illustrator path/to/article.md --style watercolor
```

Its styles include `notion` (default), `elegant`, `warm`, `minimal`, `playful`, `nature`, `sketch`, `watercolor`, `vintage`, `scientific`, `chalkboard`, `editorial`, `flat`, `flat-doodle`, `retro`, `blueprint`, `vector-illustration`, `sketch-notes`, `pixel-art`, `intuition-machine`, and `fantasy-animation`.

### image-gen

Generates images through the official OpenAI and Google APIs. It supports text-to-image generation, reference images, aspect ratios, and quality presets.

```bash
/image-gen --prompt "a cute cat" --image cat.png
/image-gen --prompt "a landscape" --image landscape.png --ar 16:9
/image-gen --prompt "a banner" --image banner.png --quality 2k
/image-gen --prompt "a cat" --image cat.png --provider openai
/image-gen --prompt "turn it blue" --image out.png --ref source.png
```

| Option | Description |
|---|---|
| `--prompt`, `-p` | Prompt text |
| `--promptfiles` | Read and concatenate prompts from files |
| `--image` | Required output image path |
| `--provider` | `google` or `openai`; default: `google` |
| `--model`, `-m` | Model ID |
| `--ar` | Aspect ratio, such as `16:9`, `1:1`, or `4:3` |
| `--size` | Dimensions, such as `1024x1024` |
| `--quality` | `normal` or `2k`; default: `normal` |
| `--ref` | Reference image for Google multimodal generation |

Required keys are supplied through `OPENAI_API_KEY` or `GOOGLE_API_KEY`. Optional variables include `OPENAI_IMAGE_MODEL`, `GOOGLE_IMAGE_MODEL`, `OPENAI_BASE_URL`, and `GOOGLE_BASE_URL`.

### url-to-markdown

Captures a URL through Chrome DevTools Protocol and converts it to clean Markdown.

```bash
/url-to-markdown https://example.com/article
/url-to-markdown https://example.com/private --wait
/url-to-markdown https://example.com/article -o output.md
```

Use `--wait` for authenticated or dynamic pages and `--timeout <ms>` to change the default 30-second page-load timeout.

### smart-git-commit

Analyzes changes and creates Conventional Commit messages with emoji. It supports pre-commit checks, staged-change analysis, and intelligent split suggestions.

```bash
/smart-git-commit
/smart-git-commit "add user authentication"
/smart-git-commit --no-verify
/smart-git-commit --amend
```

## Configuration

Skills read environment variables in descending priority: CLI environment, `process.env`, `<cwd>/.content-gen-skills/.env`, then `~/.content-gen-skills/.env`. Never commit API keys.

## Customization

All skills support `EXTEND.md` overrides. Project settings at `.content-gen-skills/<skill-name>/EXTEND.md` take precedence over personal settings at `~/.content-gen-skills/<skill-name>/EXTEND.md`.
