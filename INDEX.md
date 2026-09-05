# agent-skills Index

Last audited: 2026-09-05. Detailed findings: `docs/audits/2026-08-18-agent-skills-audit.md`.

## Verified Inventory

| Area | Current Count | Notes |
| --- | ---: | --- |
| `agents/` root source files | 103 | 100% paired Markdown & TOML agent definitions |
| `agents/` active Markdown files | 218 | Excludes README and archive/project areas |
| Active skill authorities | 325 | `SKILL.md` files under `skills/` |
| Catalog JSON files | 12 | Validated schemas in `catalog/` |
| Python files | 114 | Automation, analyzer, and catalog scripts |
| Markdown files | 815+ | Documentation, guides, and skill authorities |

## Runtime Boundary

```text
/Users/steven/.agents/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.claude/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.claude/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.codex/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers
```

- Root agent/config files and categorized agent packs coexist under `agents/`.
- Skill contracts are indexed by each `skills/**/SKILL.md` entry.
- This repository is the broad authored source ecosystem.
- Curated skills are projected into target agent environments.
- Historical, generated, restricted, and vendored material are retained safely without automatic promotion.

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
