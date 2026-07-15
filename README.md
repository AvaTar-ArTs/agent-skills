# .agent-skills

Local agent and skill workspace for reusable AI workflows.

This is the canonical local source for reusable agents and skills. The legacy
`/Users/steven/.agents` path is kept as a compatibility symlink only; new
configuration should point directly at `/Users/steven/.agent-skills`.

This repository is a living working set. Prefer additive changes, staged outputs,
and changelogs over destructive cleanup. CSVs are treated as living tables: rows
may be added, removed, or corrected, but generation scripts should append a
changelog beside the CSV.

## Layout

- `agents/` - Markdown, TOML, YAML, CSV, and text agent/persona definitions.
- `skills/` - Skill directories and nested skill libraries.
- `deep-research/` - Research-oriented skill material.
- `scripts/` - Local inspection and catalog tooling for this workspace.
- `tmp-csv/` - Local staged CSV outputs, ignored by Git.
- `tmp-md/` - Local staged Markdown reports, ignored by Git.
- `tmp/` - Local scratch/history folder, ignored by Git.

## Current Runtime Surface

Last audited: 2026-07-15.

- `agents/`: 108 non-hidden root agent/config files; 221 non-hidden files total.
- `skills/`: 97 non-hidden top-level directories plus hidden `.system/`; no top-level skill symlinks.
- Direct/root-visible skills: 79 `SKILL.md` files within depth 2.
- Local expanded skills: 186 `SKILL.md` files.
- Symlink-followed runtime-visible skills: 186 `SKILL.md` files.

Claude and Codex should consume this tree directly:

- `/Users/steven/.claude/agents -> /Users/steven/.agent-skills/agents`
- `/Users/steven/.claude/skills -> /Users/steven/.agent-skills/skills`
- `/Users/steven/.codex/agents -> /Users/steven/.agent-skills/agents`
- `/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers`

Codex note: `/Users/steven/.codex/skills` is an existing managed directory with
system skills, not a symlink to this tree.

`INDEX.md` is the broader generated overview. This README is the short entry
point for the repository.

## Inspection Scripts

Run scripts from the repository root:

```bash
python scripts/export_catalog_csv.py
python scripts/summarize_what_they_do.py
python scripts/inspect_md_content.py
```

Outputs are staged locally:

- `tmp-csv/agents-catalog.csv`
- `tmp-csv/what-they-do.csv`
- `tmp-csv/md-content-index.csv`
- `tmp-md/what-they-do.md`
- `tmp-md/md-content-report.md`

Each CSV script also appends a sibling changelog:

- `tmp-csv/agents-catalog-CHANGELOG.md`
- `tmp-csv/what-they-do-CHANGELOG.md`
- `tmp-csv/md-content-index-CHANGELOG.md`

## Working Convention

1. Inspect current contents before changing them.
2. Add new material next to existing material when practical.
3. Preserve older artifacts unless cleanup is explicitly requested.
4. Stage generated outputs under purpose-specific local folders like `tmp-csv/`
   or `tmp-md/`.
5. Promote reviewed outputs into durable docs, inventory, or report locations
   only after they are useful.
6. Treat `skills/.system/` and `skills/skill-porter-examples/` as vendored or
   reference material; duplicate names there should not be considered active
   runtime conflicts unless those folders are promoted.
7. Treat root `agents/*.md` files as the runtime primary surface when matching by
   filename; categorized `agents/<group>/*.md` copies are retained for
   organization.
8. Treat this repository as the sole active runtime. `~/my-supremepowers` is a
   historical/upstream lab only; do not link runtime skills to it.

## Git Notes

The repository intentionally ignores local archives, generated inventory dumps,
temporary staging outputs, `.DS_Store`, and the local virtual environment.

Remote:

```text
https://github.com/AvaTar-ArTs/agent-skills.git
```
