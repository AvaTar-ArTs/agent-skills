# agent-skills Index

<<<<<<< HEAD
Generated from commit 15c9bbc0ef13d6d3bf5cdd3c4292fb8e12db7143 on 2026-08-18T03:40:00Z.
=======
Last audited: 2026-08-18. Detailed findings:
`docs/audits/local-agent-skills-review-2026-08-18.md`.
>>>>>>> cdd0010 (Remove nested .git directories and add full project files)

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

<<<<<<< HEAD
## Runtime boundary
=======
| Area | Current count | Notes |
|------|---------------|-------|
| `agents/` root files | 103 | Markdown source files directly under `agents/` |
| `agents/` active Markdown files | 218 | Excludes README and archive/project areas |
| Active skill files | 311 | `SKILL.md` files under `skills/` plus `deep-research/` |
| Skill metadata | 311/311 | All active skills have `name` and `description` frontmatter |
| Skill-name collisions | 22 | Requires explicit primary/alias/reference policy |
| Agent-name collisions | 70 | Includes many categorized copies and exact duplicates |
| Broken repository-local links | 25 | All are under `.claude/skills/`; host-level links are separate |
>>>>>>> cdd0010 (Remove nested .git directories and add full project files)

- Root agent/config files and categorized agent packs coexist under agents/.
- Skill contracts are indexed by each skills/**/SKILL.md entry.
- This repository is the broad authored source ecosystem.
- Curated skills should be projected into superSkills.
- Curated agents should be projected into superAgents.
- Historical, generated, restricted, and vendored material should not be promoted automatically.

## Known issues

<<<<<<< HEAD
- agents/MANIFEST.csv has 75 unresolved agents.archive/ references.
- Prior counts in this file were stale.
- A root CHANGELOG.md now exists; CI workflow remains to be added.
- Red-team jailbreak material requires restricted promotion policy.
- File modes need normalization; many Markdown agents are executable.
=======
```text
/Users/steven/.agents/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.claude/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.claude/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.codex/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers
```
>>>>>>> cdd0010 (Remove nested .git directories and add full project files)

## Generated catalogs

- [Agent catalog](catalog/agents.json)
- [Skill catalog](catalog/skills.json)
- [Full repository index](catalog/repository-index.json)
- [Audit report](docs/audits/2026-08-18-agent-skills-audit.md)
- [Changelog](CHANGELOG.md)

<<<<<<< HEAD
## Source
=======
- Use `/Users/steven/.agent-skills` as the canonical path in new configuration.
- Keep `/Users/steven/.agents` only as a compatibility directory for older tools.
- Treat `skills/.system/` and `skills/skill-porter-examples/` as vendored/reference
  material; their duplicate skill names are intentional unless promoted.
- Treat root `agents/*.md` files as the runtime primary surface when matching by
  filename; categorized `agents/<group>/*.md` copies are retained for organization.
- Treat this repository as the sole active runtime. `~/my-supremepowers` is a
  historical/upstream lab only; do not link runtime skills to it.
- Preserve local history and generated reports unless cleanup is explicitly
  requested.
- Put temporary generated outputs under `tmp/`, `tmp-csv/`, or `tmp-md/`.
- Treat cache, session, credential, and runtime-state paths as non-importable.
>>>>>>> cdd0010 (Remove nested .git directories and add full project files)

- Repository: [AvaTar-ArTs/agent-skills](https://github.com/AvaTar-ArTs/agent-skills)
- Branch: main
- Commit: 15c9bbc0ef13d6d3bf5cdd3c4292fb8e12db7143
