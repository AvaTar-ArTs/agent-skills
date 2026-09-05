# agent-skills Repository Audit

- Repository: [AvaTar-ArTs/agent-skills](https://github.com/AvaTar-ArTs/agent-skills)
- Branch: main
- Audited commit: 15c9bbc0ef13d6d3bf5cdd3c4292fb8e12db7143
- Generated: 2026-08-18T03:40:00Z
- Scope: tree, README, existing indexes/manifests, representative contracts, scripts, references, and security-sensitive paths
- Runtime content changed by this audit: none

## Verified inventory

| Area | Count |
| --- | ---: |
| Total files | 1161 |
| Agent/config files under agents/ | 218 |
| Indexed agent entries | 217 |
| Root agent/config files | 102 |
| Skill contracts | 186 |
| Skill directories | 97 |
| Python files | 114 |
| Markdown files | 815 |
| Root scripts/ files | 9 |

## Findings

### Correctness

1. The prior INDEX.md reported 108 root agent files and 221 total agent files. The current tree contains 102 root agent/config files and 218 files under agents/, of which 101 root and 217 are indexed as entries after excluding the manifest CSV.
2. agents/MANIFEST.csv contains 75 archived paths under agents.archive/, but no agents.archive/ tree exists. All 75 references are unresolved.
3. There is no root CHANGELOG.md.
4. There is no GitHub Actions workflow.
5. The repository has no declared license or repository topics.

### Architecture

agent-skills is a broad authored ecosystem rather than a clean runtime package. It contains agent definitions, skill contracts, references, fixtures, scripts, vendored documents, reports, history, and memory material.

The correct boundary is:

- agent-skills: broad authored source ecosystem
- superSkills: curated skill layer
- superAgents: curated agent/runtime layer

### Strong content

- using-superpowers
- verification-before-completion
- skill-creator
- skill-development
- creative/structured-asset-pipeline
- workspace-ecosystem-audit
- engineering and studio agent packs

### Consolidation candidates

- research/research-paper-writing/SKILL.md is approximately 102 KB.
- taste-skill and design-taste-frontend are approximately 87 KB each.
- skill-creator, skill-development, writing-skills, skill-porter, and Hermes-specific authoring overlap and need explicit boundaries.

### Security and provenance

- red-teaming/godmode contains explicit jailbreak and safety-bypass material and should be restricted from default promotion.
- github/github-auth handles authentication concepts and should receive secret-scanning and shell-safety checks.
- .codex-history and memory exports are historical/session material and should be separated from runtime-importable content.
- 138 files carry executable mode, including many Markdown agent files.
- Large vendored assets and references increase review and supply-chain surface.

## Recommended edits

### P0 — correctness

1. Repair or replace agents/MANIFEST.csv.
2. Generate all counts and paths from the repository tree.
3. Add stable IDs, canonical paths, status, versions, source commits, and hashes.

### P1 — governance

1. Add CHANGELOG.md.
2. Add a license.
3. Add GitHub Actions for JSON/YAML/frontmatter validation, duplicate detection, broken references, and secret scanning.
4. Normalize file permissions.
5. Add explicit restricted-content policy.

### P2 — architecture

1. Generate superSkills projections from the skill catalog.
2. Generate superAgents projections from the agent catalog.
3. Add agent-to-skill dependency references.
4. Add lifecycle status: active, experimental, deprecated, archived.
5. Add pinned source commits and lockfiles.

### P3 — advancement

1. Add trigger-collision analysis.
2. Add fixture-based evaluations.
3. Add capability and dependency graphs.
4. Add generated searchable HTML documentation.
5. Add promotion gates between the three repositories.

## Generated artifacts

- [catalog/agents.json](../../catalog/agents.json)
- [catalog/skills.json](../../catalog/skills.json)
- [catalog/repository-index.json](../../catalog/repository-index.json)
- [INDEX.md](../../INDEX.md)
