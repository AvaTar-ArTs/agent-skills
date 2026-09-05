# GitHub Comparison — 2026-08-18

Remote verified:

```text
https://github.com/AvaTar-ArTs/agent-skills.git
```

## Branch state

- Local `HEAD`: `db5edb8` — adds nine deep-learning sub-skills.
- Remote `origin/main`: `af71bdf` — links generated audit and catalogs.
- Local committed branch: **2 commits ahead**, **8 commits behind** GitHub.
- Working tree: **287 dirty entries** before this comparison; these were not
  merged, rebased, reset, or overwritten.

## Remote-only changes

GitHub’s eight newer commits add or refresh:

- `catalog/agents.json`
- `catalog/skills.json`
- `catalog/repository-index.json`
- `docs/audits/2026-08-18-agent-skills-audit.md`
- root `CHANGELOG.md`
- `INDEX.md`, `README.md`, and `.gitignore`

There are no remote-only `SKILL.md` or agent-definition path changes relative
to the local committed `HEAD`; the divergence is primarily indexing,
documentation, and repository hygiene.

## Inventory comparison

| Surface | GitHub `origin/main` | Local committed `HEAD` | Local working tree scan |
|---|---:|---:|---:|
| Skill contracts | 192 | 202 | 306+ under `skills/` plus related roots |
| Agent Markdown under `agents/` | 192 | 212 | 218 active canonical files |

The GitHub `INDEX.md` itself says it was generated from commit `15c9bbc`, while
the remote tip is `af71bdf`; its embedded generation provenance is stale even
though the remote catalog commits are newer. It also records known unresolved
`agents.archive/` references and missing CI normalization.

## Recommendation

Do not merge directly into the current worktree. The safe sequence is:

1. Preserve or commit the current local audit/index work separately.
2. Create a clean comparison worktree from `origin/main`.
3. Reconcile the two local commits with the eight remote commits there.
4. Regenerate catalogs from the reconciled tree and verify runtime projections.
5. Only then decide whether to update the canonical local runtime.

This avoids mixing GitHub’s generated catalog changes with the large set of
local source edits, deletions, generated artifacts, and home-wide audit files.
