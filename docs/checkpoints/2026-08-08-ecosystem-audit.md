# Checkpoint — Ecosystem Audit and Self-Audit Rule

Date: 2026-08-08

## Mission

Review the local project, skill, and agent ecosystem; make its capabilities discoverable; and prevent unsupported assumptions or misplaced durable artifacts.

## Completed

- Audited requested home-directory ecosystems with QF-PIE.
- Repaired and validated QF-PIE in an isolated virtual environment (`2 passed`).
- Created `ralph-self-audit` in both the agent-skills and Codex skill trees.
- Wired the rule into `innate-workflow`.
- Established `/tmp` as scratch-only for reusable reports.

## Durable artifact rule

Reusable reports belong under `~/.agent-skills/docs/audits/<audit-name>/`, with a manifest and an index entry. If the destination is ambiguous, ask before generating the final artifact.

## Memory references

- Session anchor: [`~/.session-checkpoint.md`](../../../.session-checkpoint.md)
- Cross-tool decision store: `~/.agent-skills/memory/shared.sqlite`
- Decision topic: `ecosystem-durable-artifacts-and-ralph-self-audit`
- Changelog: [`../CHANGELOG.md`](../CHANGELOG.md)
- Agent-skills rule: [`../../skills/ralph-self-audit/SKILL.md`](../../skills/ralph-self-audit/SKILL.md)
- Codex rule: `~/.codex/skills/ralph-self-audit/SKILL.md`

## Known limitations

The broad QF-PIE scan was capped at 1,000 project units and over-counted nested/cloned copies. Its rankings are triage signals, not proof of ownership, uniqueness, readiness, or market value.
