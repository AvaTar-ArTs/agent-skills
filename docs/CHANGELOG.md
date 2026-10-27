# Changelog

## [Unreleased]

### Fixed — 2026-10-05
- Restored 69 missing support files (`references/`, `examples/`, `templates/`, `scripts/`) for 11 skills: build-mcp-server, hook-development, playground, agent-development, automation-recommender, build-mcp-app, mcp-integration, build-mcpb, claude-md-improver, command-development, plugin-settings. Source: `AvaTar-ArTs/.Agent-skills@5dc4c75` (`plugins/claude-plugins-official/`); 66 of 69 identical to current upstream `anthropics/claude-plugins-official@d182ca4`, and the 3 revised upstream `mcp-integration` files (plus the matching `SKILL.md` line) were taken from upstream. All 45 SKILL.md references resolve.

### Added — 2026-10-05
- Local reclaim + projection rebuild (see `backups/cleanup-manifest-2026-10-05.csv`): ComfyUI package `assets` symlinked to skill-root assets; `skills/dormant_archives/` relocated to `backups/`; `active-skills/` rebuilt as symlink projection (~67MB → ~4.4MB); 22 untracked agent category packs quarantined under `agents/_incoming/`; root agent md/toml pairing raised to 109.
- Lineage and restore checkpoint with chronological change log, checkpoints, and self-evaluation: `docs/checkpoints/2026-10-05-agent-skills-lineage-and-restore.md` (+ JSON). Records that `.Agent-skills` is a superseded subset of this repository and that its history must be kept as provenance.

### Added / Enhanced — 2026-09-12
- Saved a detailed continuation handoff at `/tmp/skill-wanderer-handoff-2026-09-12.md`, covering ecosystem findings, marketplace research, reviewer conclusions, privacy boundaries, and the proposed Skill Wanderer project.
- Added marketplace research artifacts under `docs/research/`: skills.sh/GitHub/npx/npm/Claude marketplace brief, sources table, evidence ledger, and candidate-skill review.
- Identified Skill Wanderer as the next project direction: a provenance-first, quarantine-before-promotion explorer for local and public agent skills; design approval is still required before implementation.
- Ran independent read-only code-reviewer, security-engineer, ecosystem-analyzer, and Superpowers workflow reviews; no external skills, plugins, projections, or canonical sources were modified.
- Completed and indexed local agent ecosystem deep-dive audit (`docs/audits/2026-09-12-agent-ecosystem-deepdive/`) with drift ledger, surface inventory, and Hermes control-plane risk analysis.
- Staged and verified ~34 media & AI generative skills including `seedance-2-5-*`, `kling-studio`, `eachlabs-*`, `audiomind`, `video-overlay`, `video-upscaler`, and `wan-2-7`.
- Enhanced `hooks/pre-tool-autocontext.sh` with fail-open guardrails, bounded input parsing, and safe SQLite query escaping.
- Updated `skills/workflow-bootstrap/SKILL.md` and `skills/create-skill/SKILL.md` to document current canonical topology (`~/.agent-skills`) and npx door symlink (`~/.agents/skills`).
- Synchronized design tokens in `skills/canvas/sdk/canvas-tokens.d.ts` and `skills/canvas/sdk/ui-primitives.d.ts`.
- Restructured repository root layout: moved 24 loose audit CSV/JSON dumps and static ZIP snapshots into dedicated `snapshots/historical-audits/` and `snapshots/archives/`.
- Promoted `deep-research` into canonical `skills/deep-research/SKILL.md` for immediate discovery and workspace projection via `~/.agents/skills/deep-research/`.

### Fixed — 2026-09-12
- Repaired `skills/video-breakdown/SKILL.md` frontmatter by adding missing `description` property for progressive disclosure discovery.

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
