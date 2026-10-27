# Audits Catalog

Durable audit outputs are stored under `~/.agent-skills/docs/audits/` and should include a README, manifest, findings, and continuation export when applicable.

## Entries

- [Home workspace overview — 2026-10-13](audits/2026-10-13-home-workspace-overview/README.md) — Read-only, Eza-guided map of the broader home workspace, project evidence relevant to DEV.to, one-time storage snapshot, and verification/privacy limitations.

- [Workspace ecosystem audit — 2026-10-06](audits/2026-10-06-workspace-ecosystem-audit/README.md) — Structural rescan of 11 agent homes, 130728 entries; tmp manifest gitignored; hotspots Codex sqlite/Hermes state.db/Grok installers; secret-named list; [xlsx workbook](audits/2026-10-06-workspace-ecosystem-audit/workspace-ecosystem-audit-2026-10-06.xlsx); [sanitized Grok export](audits/2026-10-06-workspace-ecosystem-audit/exports/2026-10-06-grok-01a11447-workspace-audit.md); [knowledge pack](audits/2026-10-06-workspace-ecosystem-audit/knowledge/README.md); no deletes.

- [Ruflo leftovers removal — 2026-10-05](audits/ruflo-leftovers-2026-10-05/README.md) — Finished the Ruflo/claude-flow purge: archived then removed live copies in `~/iterm2/.claude`, `~/iterm2/.agents`, `~/scripts/.claude`, agent-skills `.claude/skills` pack, Ruflo `CLAUDE.md`/`AGENTS.md`, Codex `CLAUDE_FLOW_*` env, and `proven-config.json`. Undo: `~/.agent-skills/backups/ruflo-leftovers-2026-10-05/`. Records kept.

- [skillOverrides `off` review — 2026-10-05](audits/skills-off-review-2026-10-05/README.md) — Review of 230 skills set `off` by /doctor: 110 flagged (dependency-named or recently modified), 3 confirmed export-skill prerequisites (capability-atlas, chroma, research-source-intake). Sheet: `off-skills-review.csv`. No overrides changed; limitations stated in the README.

- [Local agent ecosystem deep-dive — 2026-09-12](audits/2026-09-12-agent-ecosystem-deepdive/README.md) — Current topology, canonical skill/agent surfaces, Hermes toolsets/MCP, runtime risks, parity drift, and ranked recommendations.

- [Workspace ecosystem audit — 2026-09-11](audits/2026-09-11-workspace-ecosystem/README.md) — Structural no-follow scan of `~/.agents` through `~/.hermes`. Skill `inventory.py` missing. Only Claude skills/agents symlink to canonical. Codex==.Codex same inode. Hotspots: Codex sqlite, Grok installers, Claude ccassist.db.
- [Agents vs agent-skills topology — 2026-09-11](audits/2026-09-11-agents-vs-agent-skills.md) — `~/.agents` is a real 45M tree, not a symlink to canonical. 199 identical `SKILL.md` hashes, 23 content diffs, 3 agents-only skills. CSV: `index-agents-vs-agent-skills-skills-2026-09-11.csv`.
- [Plugin Creator Deep Audit and Remediation — 2026-08-08](audits/plugin-creator-review-2026-08-08/README.md) — Full source/mirror parity, Codex CLI integration, scaffolding, marketplace paths, validation, rollback, cachebuster behavior, security, seven regression probes, and verified repairs in both `/skills/` trees.
- [QF-PIE Agent-Skills Audit — 2026-08-08](audits/qfpie-agent-skills-2026-08-08/README.md) — 226 project-like units and 33 duplicate candidates from the canonical skill/agent ecosystem.
- [QF-PIE Project Ecosystem Audit — 2026-08-08](audits/qfpie-project-ecosystem-2026-08-08/README.md) — 1,000 capped project-like units and 527 duplicate candidates across selected home projects.
- [Steven Home Eza Audit — 2026-08-08](audits/steven-eza-home-audit-2026-08-08/README.md) — Home trees, size inventory, major-root trees, and Git repository discovery.
