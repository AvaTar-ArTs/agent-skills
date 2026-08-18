# agent-skills Index

Generated from commit 15c9bbc0ef13d6d3bf5cdd3c4292fb8e12db7143 on 2026-08-18T03:40:00Z.

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

## Runtime boundary

- Root agent/config files and categorized agent packs coexist under agents/.
- Skill contracts are indexed by each skills/**/SKILL.md entry.
- This repository is the broad authored source ecosystem.
- Curated skills should be projected into superSkills.
- Curated agents should be projected into superAgents.
- Historical, generated, restricted, and vendored material should not be promoted automatically.

## Known issues

- agents/MANIFEST.csv has 75 unresolved agents.archive/ references.
- Prior counts in this file were stale.
- A root CHANGELOG.md now exists; CI workflow remains to be added.
- Red-team jailbreak material requires restricted promotion policy.
- File modes need normalization; many Markdown agents are executable.

## Generated catalogs

- [Agent catalog](catalog/agents.json)
- [Skill catalog](catalog/skills.json)
- [Full repository index](catalog/repository-index.json)
- [Audit report](docs/audits/2026-08-18-agent-skills-audit.md)
- [Changelog](CHANGELOG.md)

## Source

- Repository: [AvaTar-ArTs/agent-skills](https://github.com/AvaTar-ArTs/agent-skills)
- Branch: main
- Commit: 15c9bbc0ef13d6d3bf5cdd3c4292fb8e12db7143
