# .agents

Local agent, skill, and plugin workspace for reusable AI workflows.

This repository is a living working set. Prefer additive changes, staged outputs,
and changelogs over destructive cleanup. CSVs are treated as living tables: rows
may be added, removed, or corrected, but generation scripts should append a
changelog beside the CSV.

## Layout

- `agents/` - Markdown and TOML agent/persona definitions.
- `skills/` - Skill directories and nested skill libraries.
- `plugins/` - Plugin source/reference material and marketplace metadata.
- `deep-research/` - Research-oriented skill material.
- `scripts/` - Local inspection and catalog tooling for this workspace.
- `tmp-csv/` - Local staged CSV outputs, ignored by Git.
- `tmp-md/` - Local staged Markdown reports, ignored by Git.
- `tmp/` - Local scratch/history folder, ignored by Git.

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

## Git Notes

The repository intentionally ignores local archives, generated inventory dumps,
temporary staging outputs, `.DS_Store`, and the local virtual environment.

Remote:

```text
https://github.com/AvaTar-ArTs/.agents.git
```
