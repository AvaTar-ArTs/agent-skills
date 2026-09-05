# Changelog

## [Unreleased]

### Fixed — 2026-09-05
- Created `agents/documentation.md` to achieve 100% (103/103) root agent MD/TOML pairing parity.
- Preserved research capabilities (`skills/research/`) and updated `.gitignore` to exclude runtime state (`agent-skills-meta.csv.summary.json`, `agent-skills-meta.duplicates.csv`, `deeptutor/user/logs/deeptutor.jsonl`).

### Added — 2026-08-08
- Bounded `ralph-self-audit` reasoning gate in `~/.agent-skills/skills/ralph-self-audit/` and `~/.codex/skills/ralph-self-audit/`.
- Durable-artifact rule: `/tmp` is scratch-only; reusable audits belong in a canonical, indexed location.
- Session checkpoint and cross-tool memory reference for ecosystem audit decisions.
- Synchronized Codex temporary `plugin-creator` metadata with `~/.codex/skills/.system/plugin-creator/`; the `.system` copy is the source of truth.
- Saved and cataloged the `plugin-creator` review with Markdown and JSON continuation exports.
- Expanded `plugin-creator` into a deep audit with full-directory parity analysis, CLI verification, security review, and seven executable regression probes.
- Repaired and synchronized `plugin-creator` under both Codex and agent-skills `/skills/` trees; added atomic writes, preflight/rollback, contract validation, semver safeguards, corrected references, and a passing seven-test suite.
- Established `/skills/` placement plus trigger-relevant `SKILL.md` metadata as a cross-tool discovery requirement.
- Added a comprehensive sorted chat checkpoint, JSON companion, and checkpoint catalog covering audits, repairs, publication state, memory, risks, and continuation priorities.
- Promoted QF-PIE and Eza audit outputs from `/tmp` into indexed `~/.agent-skills/docs/audits/` bundles and added stable `~/.codex/audits/` references.

### Added
- Pool export configuration (~/.config/poolside/mcp.json)
- Memory integration for nocturneMelodies
- Pipeline scripts (research-to-agent, version-evolution, creative-validation)
- Innate memory agent
- cross-tool-memory skill with query.py

### Changed  
- Moved memory database to ~/.agent-skills/memory/shared.sqlite
- Updated init_memory.py and query_memory.py paths
- Created AGENT_PATTERN_GUIDE.md documenting pack patterns

### Cross-links
- Poolside config, Memory system, Pipeline scripts, NocturneMelodies, ralph-self-audit, checkpoint
