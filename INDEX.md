# ~/.agents — Master Index

> Generated 2026-06-14. This is the **Codex/agents runtime surface** (descriptions reference Codex/Qwen),
> a sibling to `~/.claude`. Three top-level areas: **agents/**, **skills/**, **plugins/**.

## At a glance

| Area | Count | Notes |
|------|-------|-------|
| Skill directories (top-level) | 96 | 72 have a root `SKILL.md`; 24 are category folders |
| **Total `SKILL.md` files** | **173** | 72 flat + 101 nested in category folders |
| Agent definitions (`.md`) | 42 | + 3 `.toml`, plus `openai.yaml`, `cleanup-manifest.csv` |
| Plugins | 1 | `plugins/marketplace.json` |
| Total files | 914 | 615 md, 66 py, 39 xsd, 17 json, 13 sty/tex (LaTeX), … |
| Disk | ~15 MB | almost all under `skills/` |

---

## 1. Agents (`agents/`) — 42 definitions

Fresh-context specialists. **Note:** most descriptions are auto-generated boilerplate
(`"Use when working with: X, Y, Z"`); a handful are hand-authored (flagged ★).

**Architecture & engineering**
`backend-architect` · `frontend-architect` · `system-architect` · `api-specialist` ★ · `database-specialist` · `devops-engineer` · `performance-engineer` · `security-engineer` · `javascript-expert` · `python-expert` · `testing-specialist` · `technical-writer` · `code-reviewer`

**Ecosystem & meta**
`ecosystem-analyzer` · `ecosystem-learning` · `ecosystem-synergy` · `integrated-evolution` · `self-evolution` · `capability-atlas` ★ · `system-analyzer` · `tree-explorer` · `filesystem-inventory` · `path-list-analyzer` · `content-consolidator` · `content-organizer` · `context-management` · `context-handoff-compiler` · `workflow-orchestrator` · `documentation-management`

**Product, growth & domain**
`xeo-strategist` · `ai-xeo` · `revenue-optimizer` · `project-launch-manager` · `knowledge-automation-strategist` · `seo-keyword-analyst` · `task-management` · `ai-workflow-manager` · `ai-music-video-creator` ★ · `avatararts-organizer` · `notebooklm-enhancement-advisor` · `ice-tracker-assistant` · `agent-creation-guidance`

**Non-md configs:** `autotag_architect.toml`, `capability_atlas.toml`, `ecosystem_intelligence.toml`, `openai.yaml`, `cleanup-manifest.csv`

---

## 2. Skills (`skills/`)

### 2a. Flat skills — 72 (root `SKILL.md`)

**Skill/agent authoring & meta**
`agent-creation-guidance` · `agent-development` · `skill-creator` · `skill-development` · `skill-installer` · `skill-porter-examples` · `writing-skills` · `writing-rules` · `rule-definition-patterns` · `command-development` · `hook-development` · `capability-atlas` · `automation-recommender`

**MCP & plugins**
`build-mcp-server` · `build-mcp-app` · `build-mcpb` · `mcp-integration` · `mcp-app-development-principles` · `plugin-structure` · `plugin-settings`

**Dev workflow (core loop)**
`brainstorm` · `brainstorming` *(dup)* · `writing-plans` · `executing-plans` · `subagent-driven-development` · `test-driven-development` · `systematic-debugging` · `requesting-code-review` · `receiving-code-review` · `verification-before-completion` · `finishing-a-development-branch` · `using-git-worktrees` · `dispatching-parallel-agents` · `using-superpowers` · `workflow-bootstrap`

**Ecosystem ops**
`ecosystem-clarity` · `ecosystem-navigation` · `managing-ecosystem-cleanup` · `workspace-ecosystem-audit` · `cursor-integration` · `self-assistance` · `self-improvement` · `chat-history-export` · `session-report` · `claude-md-improver` · `eza-nav`

**Messaging channels**
`discord-access` · `discord-configure` · `imessage-access` · `imessage-configure` · `telegram-access` · `telegram-configure`

**Git AI / integrations**
`git-ai-assistant` · `git-ai-cursor-integration` · `ice-tracker-integration` · `hermes-integration` · `composio-cli`

**Frontend & creative**
`frontend-design` · `frontend-ux-modernizer` · `taste-skill` · `playground` · `dogfood` · `narrative-blueprints` · `narrative-documentation` · `sora`

**ToolUniverse / science**
`setup-tooluniverse` · `devtu-fix-tool` · `devtu-optimize-descriptions` · `devtu-optimize-skills` · `tooluniverse-clinical-trial-design` · `tooluniverse-sequence-retrieval`

**Misc**
`notebooklm` · `math-olympiad-solver`

### 2b. Nested skills — 101 (in 23 category folders)

| Category | Skills |
|----------|--------|
| **apple** | apple-reminders, macos-computer-use, imessage, findmy, apple-notes |
| **autonomous-ai-agents** | claude-code, codex, hermes-agent, ecosystem-layering, opencode |
| **creative** (19) | p5js, architecture-diagram, sketch, ascii-art, design-md, baoyu-comic, popular-web-designs, manim-video, pixel-art, pretext, humanizer, creative-ideation, comfyui, baoyu-infographic, songwriting-and-ai-music, ascii-video, touchdesigner-mcp, excalidraw, claude-design |
| **software-development** (11) | node-inspect-debugger, debugging-hermes-tui-commands, subagent-driven-development, test-driven-development, systematic-debugging, plan, hermes-agent-skill-authoring, python-debugpy, writing-plans, spike, requesting-code-review |
| **productivity** (10) | ocr-and-documents, nano-pdf, maps, teams-meeting-pipeline, linear, notion, airtable, powerpoint, google-workspace |
| **github** (6) | github-auth, github-repo-management, github-pr-workflow, github-code-review, github-issues, codebase-inspection |
| **mlops** (9) | huggingface-hub, inference/{llama-cpp,vllm,obliteratus}, evaluation/{lm-evaluation-harness,weights-and-biases}, research/dspy, models/{audiocraft,segment-anything} |
| **media** (5) | youtube-content, heartmula, spotify, songsee, gif-search |
| **research** (5) | blogwatcher, polymarket, llm-wiki, arxiv, research-paper-writing |
| **devops** (3) | kanban-worker, kanban-orchestrator, webhook-subscriptions |
| **gaming** (2) | minecraft-modpack-server, pokemon-player |
| **email** | himalaya | **note-taking** | obsidian | **mcp** | native-mcp |
| **data-science** | jupyter-live-kernel | **smart-home** | openhue | **social-media** | xurl | **red-teaming** | godmode |

**Category folders that are stubs** (only a `DESCRIPTION.md`, no skills yet): `diagramming`, `domain`, `gifs`, `inference-sh`.
**`dist/`** holds one packaged artifact: `frontend-ux-modernizer.skill`.

---

## 3. Plugins (`plugins/`)
- `marketplace.json` — single plugin marketplace manifest.

---

## Observations / cleanup candidates

1. **Duplicates** — `brainstorm` ≈ `brainstorming` (identical descriptions). And 5 dev-loop skills exist **both** flat *and* nested under `software-development/`: `test-driven-development`, `systematic-debugging`, `subagent-driven-development`, `writing-plans`, `requesting-code-review`. Worth consolidating to one canonical location.
2. **Boilerplate agent descriptions** — 38 of 42 agents use auto-generated `"Use when working with: …"` text. These trigger poorly; rewriting frontmatter `description:` fields would materially improve routing.
3. ~~Empty category stubs — `diagramming`, `domain`, `gifs`, `inference-sh` contain only `DESCRIPTION.md`. Either populate or remove.~~ (Stubs removed 2026-06-17)
4. **Cross-surface naming drift** — several skill descriptions reference "Codex"/"Qwen" even where the skill is host-agnostic (e.g. `claude-md-improver` describes itself as editing `AGENTS.md`). Consistent with this being the Codex runtime surface, but flag if parity with `~/.claude` matters.
