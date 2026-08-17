# ~/.agent-skills - Current Runtime Index

Last audited: 2026-08-17.

This tree is the canonical local source for reusable agents and skills. The
legacy `/Users/steven/.agents` path is maintained as a compatibility symlink to
this directory; new runtime configuration should point directly at
`/Users/steven/.agent-skills`.

## At a Glance

| Area | Current count | Notes |
|------|---------------|-------|
| `agents/` root files | 108 | Non-hidden files directly under `agents/` |
| `agents/` all files | 221 | Non-hidden files under all agent subdirectories |
| `skills/` top-level directories | 97 | Non-hidden dirs; hidden `.system/` also present; no top-level skill symlinks |
| Direct/root-visible skills | 79 | `SKILL.md` files within depth 2 |
| Local expanded skills | 186+ | Prior audited baseline was 186; nested creative workflow additions may increase this count |
| Symlink-followed runtime-visible skills | 186+ | Recount after runtime sync; no external skill symlink is required for runtime material |

## Runtime Links

Claude and Codex should resolve through the canonical `.agent-skills` tree:

```text
/Users/steven/.agents -> /Users/steven/.agent-skills
/Users/steven/.claude/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.claude/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.codex/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers
```

Codex note: `/Users/steven/.codex/skills` is an existing managed directory with
system skills, not a symlink to this tree.

## Operating Notes

- Use `/Users/steven/.agent-skills` as the canonical path in new configuration.
- Keep `/Users/steven/.agents` only as a compatibility alias for older tools.
- Treat `skills/.system/` and `skills/skill-porter-examples/` as vendored/reference
  material; their duplicate skill names are intentional unless promoted.
- Treat root `agents/*.md` files as the runtime primary surface when matching by
  filename; categorized `agents/<group>/*.md` copies are retained for organization.
- Treat this repository as the sole active runtime. `~/my-supremepowers` is a
  historical/upstream lab only; do not link runtime skills to it.
- Preserve local history and generated reports unless cleanup is explicitly
  requested.
- Put temporary generated outputs under `tmp/`, `tmp-csv/`, or `tmp-md/`.
- Treat cache, session, credential, and runtime-state paths as non-importable.

## Workflow Architecture

The shared boundary between skills, workflows, MCP/tools, provider backends, and
durable memory is documented in `docs/SKILL_WORKFLOW_CONTRACT.md`.

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

Skill routing and provider routing are deliberately separate. Provider availability
must not bypass process/domain skill selection.

## Useful Entry Points

- `skills/using-superpowers/SKILL.md` - process authority for SupremePower /
  using-superpowers requests and meta-routing across skills.
- `skills/brainstorming/SKILL.md` - ambiguity/design gate with structured handoff
  semantics and recognition of already-approved designs.
- `skills/creative/music-to-video/SKILL.md` - provider-neutral song/cue to visual
  narrative, SceneGraph/ShotManifest planning, render, continuity, edit, evaluation,
  export, publish, and archive workflow.
- `skills/creative/songwriting-and-ai-music/SKILL.md` - upstream songwriting and
  AI-music craft for tracks that are not yet approved/final.
- `skills/creative/structured-asset-pipeline/SKILL.md` - reproducible multi-unit
  asset execution helper suitable for downstream keyframe/clip generation.
- `skills/ecosystem-intelligence/SKILL.md` - ecosystem audit and topology work.
- `skills/cross-tool-memory/SKILL.md` - shared memory bridge workflows.
- `skills/agmsg/SKILL.md` - cross-agent messaging workflows.
- `docs/SKILL_WORKFLOW_CONTRACT.md` - interoperability contract for handoffs,
  semantic capabilities, checkpoints, verification, and provider boundaries.
