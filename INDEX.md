# agent-skills Index

Last audited: **2026-10-05**. Deep dive: `docs/audits/2026-09-12-agent-ecosystem-deepdive/README.md`. Topology: `docs/audits/2026-09-11-agents-vs-agent-skills.md`. Session synthesis: `tmp-md/2026-10-05-agents-skills-synthesis.md`.

## Verified Inventory

| Area | Current Count | Notes |
| --- | ---: | --- |
| `agents/` root paired defs | 109 | Paired Markdown & TOML (live set) |
| `agents/_incoming/` packs | 22 | Quarantined untracked category packs (2026-10-05) |
| `skills/` `SKILL.md` | ~599 | Full canonical tree including nested packs |
| `skills/` top-level dirs | ~343 | Includes packs, archives relocated out where noted |
| `active-skills/` projection | ~299 tops / ~338 `SKILL.md` | Symlink projection into `skills/` (rebuilt 2026-10-05) |
| Catalog JSON files | 12 | Validated schemas in `catalog/` |

## Runtime Boundary

```text
/Users/steven/.agents/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.claude/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.claude/skills -> /Users/steven/.agent-skills/active-skills
/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers
```

Notes (2026-10-05):

- `~/.agents/skills` remains the npx `skills` door into the full canonical library.
- Claude uses **`active-skills/`** (symlink projection), not the full `skills/` tree.
- `~/.codex/agents` is a flat mirror, not a directory symlink to `agents/`.
- Numbered agent packs are historical; see `agents/ARCHIVE-PACKS.md`.
- Reclaim backups + restore commands: `backups/cleanup-manifest-2026-10-05.csv`.

## Known Issues & Operating Guidelines

- Use `/Users/steven/.agent-skills` as the canonical path in new configuration.
- Keep `/Users/steven/.agents` as a compatibility directory for older tools.
- Treat `skills/.system/` and `skills/skill-porter-examples/` as vendored/reference material.
- Treat root `agents/*.md` files as the runtime primary surface when matching by filename.
- Preserve local history and generated reports.
- Put temporary generated outputs under `tmp/`, `tmp-csv/`, or `tmp-md/`.

## Generated Catalogs

- [Agent catalog](catalog/agents.json)
- [Skill catalog](catalog/skills.json)
- [Full repository index](catalog/repository-index.json)
- [Audit report](docs/audits/2026-08-18-agent-skills-audit.md)
- [Changelog](docs/CHANGELOG.md)

## Workflow Architecture

The shared boundary between skills, workflows, MCP/tools, provider backends, and durable memory is documented in `docs/SKILL_WORKFLOW_CONTRACT.md`.

Preferred high-level flow:

```text
user intent
  -> skill discovery
  -> process/domain workflow
  -> semantic operation
  -> tool/MCP
  -> provider/local backend
  -> artifacts + provenance
  -> verification
```

Skill routing and provider routing are deliberately separate. Provider availability must not bypass process/domain skill selection.

## Useful Entry Points

- `skills/using-superpowers/SKILL.md` - process authority for SupremePower / using-superpowers requests and meta-routing across skills.
- `skills/brainstorming/SKILL.md` - ambiguity/design gate with structured handoff semantics and recognition of already-approved designs.
- `skills/creative/music-to-video/SKILL.md` - provider-neutral song/cue to visual narrative, SceneGraph/ShotManifest planning, render, continuity, edit, evaluation, export, publish, and archive workflow.
- `skills/creative/songwriting-and-ai-music/SKILL.md` - upstream songwriting and AI-music craft for tracks that are not yet approved/final.
- `skills/creative/structured-asset-pipeline/SKILL.md` - reproducible multi-unit asset execution helper suitable for downstream keyframe/clip generation.
- `skills/ecosystem-intelligence/SKILL.md` - ecosystem audit and topology work.
- `skills/cross-tool-memory/SKILL.md` - shared memory bridge workflows.
- `skills/agmsg/SKILL.md` - cross-agent messaging workflows.
- `docs/SKILL_WORKFLOW_CONTRACT.md` - interoperability contract for handoffs, semantic capabilities, checkpoints, verification, and provider boundaries.
