# Audits Catalog

Durable audit outputs are stored under `~/.agent-skills/docs/audits/` and should include a README, manifest, findings, and continuation export when applicable.

## Entries

- [Workspace ecosystem audit — 2026-09-11](audits/2026-09-11-workspace-ecosystem/README.md) — Structural no-follow scan of `~/.agents` through `~/.hermes`. Skill `inventory.py` missing. Only Claude skills/agents symlink to canonical. Codex==.Codex same inode. Hotspots: Codex sqlite, Grok installers, Claude ccassist.db.
- [Agents vs agent-skills topology — 2026-09-11](audits/2026-09-11-agents-vs-agent-skills.md) — `~/.agents` is a real 45M tree, not a symlink to canonical. 199 identical `SKILL.md` hashes, 23 content diffs, 3 agents-only skills. CSV: `index-agents-vs-agent-skills-skills-2026-09-11.csv`.
- [Plugin Creator Deep Audit and Remediation — 2026-08-08](audits/plugin-creator-review-2026-08-08/README.md) — Full source/mirror parity, Codex CLI integration, scaffolding, marketplace paths, validation, rollback, cachebuster behavior, security, seven regression probes, and verified repairs in both `/skills/` trees.
- [QF-PIE Agent-Skills Audit — 2026-08-08](audits/qfpie-agent-skills-2026-08-08/README.md) — 226 project-like units and 33 duplicate candidates from the canonical skill/agent ecosystem.
- [QF-PIE Project Ecosystem Audit — 2026-08-08](audits/qfpie-project-ecosystem-2026-08-08/README.md) — 1,000 capped project-like units and 527 duplicate candidates across selected home projects.
- [Steven Home Eza Audit — 2026-08-08](audits/steven-eza-home-audit-2026-08-08/README.md) — Home trees, size inventory, major-root trees, and Git repository discovery.
