# Findings

## 1. Inventory documentation is stale

The repository documentation says it was last audited on 2026-07-15 and
reports:

- 108 root agent/config files
- 221 agent files total
- 97 top-level skill directories
- 186 local `SKILL.md` files

The current filesystem reports:

- 110 root agent files
- 245 agent files total
- 212 top-level skill directories, excluding hidden `.system`
- 292 active `SKILL.md` files, excluding `.system` and
  `skill-porter-examples`

The July counts should not be treated as the current runtime inventory.

## 2. Runtime links are mostly aligned

These paths resolve to `/Users/steven/.agent-skills`:

- `/Users/steven/.claude/agents`
- `/Users/steven/.claude/skills`
- `/Users/steven/.codex/agents`
- `/Users/steven/.codex/superpowers` resolves to the local
  `using-superpowers` skill

However, `/Users/steven/.agents` is a real directory, not a symlink. This
contradicts the compatibility-link statements in `README.md` and `INDEX.md`.
The directory should be inspected before any migration or cleanup decision.

## 3. The worktree is intentionally or incidentally in transition

At review time, Git reported many pre-existing modifications, deletions, and
untracked additions. The changes include agent definitions, plugin-creator
material, a large research-skill deletion set, new skills, audits, checkpoints,
and generated inventory files.

No attempt was made to normalize, revert, stage, or delete these changes.

## 4. Multiple inventory/lock artifacts exist

The root contains both hidden and visible metadata files, including:

- `.skill-lock.json` and `skills-lock.json`
- `.agent-skills-meta.csv` and `agent-skills-meta.csv`
- `inventory-agent-skills.json`

These may be purposeful exports, but their authority and refresh process are
not obvious from the short README. A future maintenance pass should label each
as canonical, generated, or historical.

## Recommended follow-up

1. Run the inventory scripts and promote a reviewed current count into
   `README.md`, `INDEX.md`, and the relevant catalog files.
2. Document whether `/Users/steven/.agents` is intentionally a directory or
   should become the stated compatibility symlink; do not change it without
   inspecting its contents and ownership.
3. Define the source-of-truth relationship among the lock files and CSV/JSON
   inventories.
4. Review the current Git diff as a separate change-management task before
   committing or cleaning the workspace.

## Method note

This is an evidence snapshot from 2026-08-14. Counts can change as skills are
added or removed; later reviews should preserve this snapshot and record new
observations additively.
