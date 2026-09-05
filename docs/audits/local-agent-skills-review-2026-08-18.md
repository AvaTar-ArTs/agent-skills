# Local Agent Skills Re-audit — 2026-08-18

## Outcome

The indexing pipeline is healthy, but the checked-in index was stale and the
runtime taxonomy is ambiguous. The active source scan contains 311 skill files
and 218 agent Markdown files. All 311 active skills have usable `name` and
`description` frontmatter.

This audit is additive and does not delete or rewrite backups, exports, the
Deeptutor project, generated catalogs, or pre-existing user changes.

## Scope

The active scan includes `skills/**/SKILL.md` and `deep-research/**/SKILL.md`,
excluding `.git`, caches, backups, generated staging directories, docs,
memory exports, and the Deeptutor project. Agent counts include Markdown files
under `agents/`, excluding README files and the same non-source areas.

Commands run:

```bash
python3 scripts/export_catalog_csv.py
python3 scripts/summarize_what_they_do.py
python3 scripts/inspect_md_content.py
python3 scripts/audit_runtime.py --pretty
bash scripts/discover-ecosystem.sh
```

The generated catalogs are staged under ignored `tmp-csv/` and `tmp-md/`.

## Findings

### P0 — repair repository-local Claude links

There are 25 broken links under `.claude/skills/`. Their relative target is
`../../.agents/skills`, which resolves inside `.agent-skills/.agents/` rather
than to `/Users/steven/.agents/skills`. The host-level
`/Users/steven/.claude/skills` link is separate and currently resolves to the
canonical tree.

Recommended change: either remove the repository-local compatibility links or
replace them with absolute links to `/Users/steven/.agent-skills/skills`.

### P1 — make runtime identity explicit

There are 22 duplicate skill names and 70 duplicate agent names. Some are
intentional (categorized copies, vendor examples, or compatibility variants),
but the runtime currently relies on convention rather than machine-readable
identity. There is also one exact duplicate skill and 35 exact duplicate agent
pairs.

Recommended schema additions: `status: active|alias|reference|archived`,
`canonical_path`, `runtime_hosts`, and `source`. Make catalog generation
exclude `reference` and `archived` entries by default while retaining an
explicit `--include-all` mode.

### P1 — finish the agent metadata boundary

Thirty-four agent Markdown files lack frontmatter because they are reference,
Gemini, example, or legacy material. That is acceptable only if the catalog
explicitly excludes those files. `agents/test-agent.md` is the one runtime-like
agent with a missing description and should be repaired first.

### P1 — replace hard-coded discovery totals

`scripts/discover-ecosystem.sh` previously printed obsolete fixed totals and
counted directory entries inconsistently. It now computes counts from active
`SKILL.md` and agent Markdown files and excludes known non-runtime areas.

### P2 — reduce catalog noise and repository weight

The tree contains large archives and generated artifacts, including
`skills.zip`, `skills/dormant_archives/*.zip`, multi-megabyte inventory CSV/JSON
files, and the 903 KB ChatGPT exporter. Preserve them if needed, but keep
runtime indexes path-oriented and make generated large inventories opt-in.

## Recommended next sequence

1. Repair or remove the 25 repository-local `.claude/skills` links.
2. Add canonical/alias/reference status to the 22 skill and 70 agent collision
   groups; promote only one runtime primary per name.
3. Add a description to `agents/test-agent.md` and classify the 34 reference
   Markdown files.
4. Add CI or a pre-commit check for frontmatter, duplicate active names,
   broken links, and stale index date/counts.
5. Keep the generated CSV/content indexes ignored; publish a small current
   JSON manifest for runtime discovery rather than committing full content
   dumps.

## Repeatability

Run the focused audit with:

```bash
cd /Users/steven/.agent-skills
python3 scripts/audit_runtime.py --pretty
```
