# .agent-skills

Local agent and skill workspace for reusable AI workflows.

This is the canonical local source for reusable agents and skills. New
configuration should point directly at `/Users/steven/.agent-skills`.
`/Users/steven/.agents` is currently a compatibility directory whose
`skills` entry points here; it is not itself a symlink.

This repository is a living working set. Prefer additive changes, staged outputs,
and changelogs over destructive cleanup. CSVs are treated as living tables: rows
may be added, removed, or corrected, but generation scripts should append a
changelog beside the CSV.

## Layout

- `agents/` - Markdown, TOML, YAML, CSV, and text agent/persona definitions. Live set = root paired `.md`+`.toml`. Numbered packs are historical; untracked category packs sit in `agents/_incoming/`.
- `skills/` - Canonical skill directories and nested skill libraries.
- `active-skills/` - Curated **symlink projection** into `skills/` for hosts that want a trimmed discovery set (see `active-skills/PROJECTION.md`).
- `scripts/` - Local inspection and catalog tooling for this workspace.
- `backups/` - Local reclaim/quarantine backups and cleanup manifests (gitignored).
- `tmp-csv/` - Local staged CSV outputs, ignored by Git.
- `tmp-md/` - Local staged Markdown reports, ignored by Git.
- `tmp/` - Local scratch/history folder, ignored by Git.

## Current Runtime Surface

Last audited: **2026-10-27** (local runtime and repository reconcile). Prior deep dives:
`docs/audits/local-agent-skills-review-2026-08-18.md`,
`docs/audits/2026-09-12-agent-ecosystem-deepdive/`,
`tmp-md/2026-10-05-agents-skills-synthesis.md`.

Measured inventory (2026-10-27):

- `agents/` root: **110** paired `.md`+`.toml` definitions (plus archive packs and `agents/_incoming/`).
- `skills/`: **347** top-level directories; **608** `SKILL.md` files (includes nested packs such as calesthio).
- `active-skills/`: **317** entries: **308** symlinks and **9** materialized skill directories.
- Claude discovery uses the **active-skills** projection, not the full `skills/` tree.
- Claude's `~/.claude/agents/` is a separate roster of **7 copied agent files**; it does not load this repository's agent archive automatically.
- Leaf-name collisions and pack copies still exist; treat root / projected entries as primaries.

Runtime doors (verified 2026-10-27):

- `/Users/steven/.agents/skills -> /Users/steven/.agent-skills/skills`
- `/Users/steven/.claude/agents/` is a runtime directory with 7 copied agent files, not a symlink to this repository.
- `/Users/steven/.claude/skills -> /Users/steven/.agent-skills/active-skills`
- `/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers`

Codex note: `/Users/steven/.codex/agents` is a flat mirror (not a directory symlink). `/Users/steven/.codex/skills` remains a managed directory with system skills, not a symlink to this tree.

`INDEX.md` is the broader generated overview. This README is the short entry
point for the repository.

The home-wide capability inventory is in
`docs/audits/home-capability-audit-2026-08-18.md` and its companion JSON/CSV
files. It is intentionally broader than the canonical runtime index and
includes host projections, project-local copies, backups, and caches.

## Inspection Scripts

Run scripts from the repository root:

```bash
python scripts/export_catalog_csv.py
python scripts/summarize_what_they_do.py
python scripts/inspect_md_content.py
python scripts/audit_runtime.py --pretty
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


## Current index

The generated [INDEX.md](INDEX.md), [agent catalog](catalog/agents.json), [skill catalog](catalog/skills.json), and [audit report](docs/audits/2026-08-18-agent-skills-audit.md) are the current repository inventory. See [CHANGELOG.md](CHANGELOG.md) for audit history.
