---
name: Archive Packs
description: Archive policy for numbered historical agent packs and quarantined _incoming/ category packs — explains live discovery set vs. retained provenance packs, plus a filename index with byte status against the archive root.
---

# Agent pack archive policy

Updated: 2026-10-27

## What actually loads
Claude Code loads agent files from `~/.claude/agents/` and from a project's `.claude/agents/`. It does not scan `~/.agent-skills/agents/`. As of 2026-10-26 the user roster is seven files: `code-investigator`, `conversation-analyzer`, `export-knowledge-curator`, `eza-comprehender`, `filesystem-inventory`, `repo-clean`, `review`.

This archive keeps copies. Root `name.md` files are the archive set. A missing `.toml` does not make a markdown file unloadable by Claude; Claude reads the markdown. Do not treat a filename match as proof that two copies are the same file. Compare bytes, and check `readlink` before calling anything a duplicate. `rg` does not follow symlinks unless `-L`.

`eza-comprehender.md` and `repo-clean.md` are copied at the archive root from `~/.claude/agents/`. `export-knowledge-curator.md` is not at the root; the archive copy is `6-automation-workbench/export-knowledge-curator.md`, and it matches the live file.

## Numbered historical packs (do not treat as primaries)
These remain in-tree for provenance. Several names also exist at the root, and the bytes often differ. Do not delete or replace a pack by matching the filename.

- `1-eng-specialist-pack/`
- `2-personal-tooled/`
- `3-contains-studio/`
- `5-misc-personal/`
- `6-automation-workbench/` (its own five agents, including the export-knowledge-curator copy above; it is not a collision with a root file of that name)

Prefer the live file in `~/.claude/agents/` when Claude is the host. Prefer the archive root when a host is reading this tree and a root file exists.

## Skill bundles retained under `agents/`

These directories are not agent packs. They contain skill instructions or conversion examples that were historically stored under this tree. The active skill source is under `skills/`; the copies here are not synchronized and must not be merged or deleted by matching names. A byte comparison on 2026-10-27 found:

- `skill-creator/` vs. `../skills/skill-creator/`: 11 vs. 25 files; 5 of 8 shared paths are identical and 3 differ.
- `skill-installer/` vs. `../skills/skill-installer/`: 10 vs. 9 files; 5 of 9 shared paths are identical and 4 differ.
- `skill-porter/` vs. `../skills/skill-porter-examples/`: 20 vs. 19 files; 6 of 19 shared paths are identical and 13 differ.
- `desktop-commander-chat-formatter/` vs. `../skills/desktop-commander-chat-formatter/`: 3 vs. 1 files; the one shared path differs.

Keep these copies as retained provenance until a separate, file-by-file migration is approved. For current skill behavior, consult `~/.agent-skills/skills/` and the relevant host projection.

## Quarantine (`_incoming/`)
Untracked categorized packs moved here on 2026-10-05T00:13:48 for promote-or-drop triage:

- `analysis/`
- `architecture/`
- `browser/`
- `consensus/`
- `core/`
- `custom/`
- `data/`
- `development/`
- `devops/`
- `flow-nexus/`
- `github/`
- `goal/`
- `optimization/`
- `payments/`
- `sona/`
- `sparc/`
- `specialized/`
- `sublinear/`
- `swarm/`
- `templates/`
- `testing/`
- `v3/`

Restore a pack: `mv agents/_incoming/<name> agents/<name>`

## Pack filename index

Indexed: 2026-10-26. SHA-256 of each pack `*.md` against `agents/<same filename>` at the archive root. 34 same bytes, 41 differs, 5 pack only.

Claude loads `~/.claude/agents/` only. This list is for finding files. When a root file exists, prefer `agents/<name>.md`. A matching filename is not a reason to copy a pack file into `~/.claude/agents/`, and it is not a reason to delete either copy. There is no pack `4`. `_incoming/` is not in this index.

Of the 41 that differ, `1-eng-specialist-pack/api-specialist.md` also has a shorter body on the root. `2-personal-tooled/capability-atlas.md` differs by blank lines in the body. The other 39 differ in frontmatter only. Pack 1 still has `expertise`, `activation_keywords`, and `complexity_threshold`. The root file of the same name does not, so the root is not a full replacement of that pack.

A frontmatter `name` that differs is shown in parentheses as the pack name, then the root name.

### `1-eng-specialist-pack/`

- `api-specialist.md` — differs
- `database-specialist.md` — differs
- `devops-engineer.md` — differs
- `frontend-architect.md` — differs
- `javascript-expert.md` — differs
- `performance-engineer.md` — differs
- `python-expert.md` — differs
- `security-engineer.md` — differs
- `system-architect.md` — differs
- `technical-writer.md` — differs
- `testing-specialist.md` — differs

### `2-personal-tooled/`

`2-personal-tooled/code-review.md`, `agents/code-review.md`, and `agents/code-reviewer.md` stay three files. The pack bytes match neither root file.

- `bots.md` — same bytes
- `capability-atlas.md` — differs
- `code-review.md` — differs (`code-reviewer`, `code-review`)
- `context-handoff-compiler.md` — differs
- `documentation-management.md` — differs
- `notebooklm-enhancement-advisor.md` — differs
- `rule-definition.md` — same bytes
- `system-analysis.md` — same bytes
- `workflow-orchestrator.md` — differs

### `3-contains-studio/`

- `ai-music-video-creator.md` — differs
- `analytics-reporter.md` — same bytes
- `api-tester.md` — same bytes
- `app-store-optimizer.md` — same bytes
- `brand-guardian.md` — same bytes
- `content-creator.md` — same bytes
- `content-organizer.md` — differs
- `experiment-tracker.md` — same bytes
- `feedback-synthesizer.md` — same bytes
- `finance-tracker.md` — same bytes
- `growth-hacker.md` — same bytes
- `infrastructure-maintainer.md` — same bytes
- `instagram-curator.md` — same bytes
- `joker.md` — same bytes
- `knowledge-automation-strategist.md` — differs
- `legal-compliance-checker.md` — same bytes
- `mobile-app-builder.md` — same bytes
- `performance-benchmarker.md` — same bytes
- `project-launch-manager.md` — differs
- `project-shipper.md` — same bytes
- `reddit-community-builder.md` — same bytes
- `sprint-prioritizer.md` — same bytes
- `studio-producer.md` — same bytes
- `support-responder.md` — same bytes
- `system-analyzer.md` — differs
- `test-results-analyzer.md` — same bytes
- `tiktok-strategist.md` — same bytes
- `tool-evaluator.md` — same bytes
- `trend-researcher.md` — same bytes
- `twitter-engager.md` — same bytes
- `ui-designer.md` — same bytes
- `ux-researcher.md` — same bytes
- `visual-storyteller.md` — same bytes
- `whimsy-injector.md` — same bytes
- `workflow-optimizer.md` — same bytes

### `5-misc-personal/`

The live `filesystem-inventory.md` matches the archive root. The pack file differs.

- `agent-creation-guidance.md` — differs
- `ai-workflow-manager.md` — differs
- `ai-xeo.md` — differs
- `avatararts-organizer.md` — differs
- `content-consolidator.md` — differs
- `context-management.md` — differs (`Context Management`, `context-management`)
- `documentation-manager.md` — same bytes
- `ecosystem-analyzer.md` — differs
- `ecosystem-learning.md` — differs (`Ecosystem Learning`, `ecosystem-learning`)
- `ecosystem-synergy.md` — differs (`Ecosystem Synergy`, `ecosystem-synergy`)
- `filesystem-inventory.md` — differs
- `ice-tracker-assistant.md` — differs (`Ice Tracker Assistant`, `ice-tracker-assistant`)
- `integrated-evolution.md` — differs (`Integrated Evolution`, `integrated-evolution`)
- `path-list-analyzer.md` — differs
- `revenue-optimizer.md` — differs
- `self-evolution.md` — differs (`Self Evolution`, `self-evolution`)
- `seo-keyword-analyst.md` — differs
- `task-management.md` — differs (`Task Management`, `task-management`)
- `tree-explorer.md` — differs
- `xeo-strategist.md` — differs

### `6-automation-workbench/`

This pack also has a `README.md`. That file is not an agent. `export-knowledge-curator.md` has no root copy, and its bytes match `~/.claude/agents/export-knowledge-curator.md`.

- `automation-offer-architect.md` — pack only
- `export-knowledge-curator.md` — pack only
- `host-portability-architect.md` — pack only
- `preview-first-operator.md` — pack only
- `proof-asset-strategist.md` — pack only
