# GitHub Clean-Worktree Reconciliation — 2026-08-18

## Execution

The reconciliation was performed in a temporary detached worktree at
`origin/main` (`af71bdf`). The temporary worktree was clean and removed after
the comparison. The canonical working tree was not reset, merged, or altered
by the reconciliation.

A fresh `git fetch origin main` was attempted but GitHub DNS was unavailable in
this session. The locally cached `origin/main` ref was therefore used; it was
the previously verified remote tip `af71bdf`.

## Branch relationship

- Local `HEAD`: `db5edb8`
- Cached `origin/main`: `af71bdf`
- Local committed history: **2 commits ahead**, **8 commits behind**
- Local working tree: **287 dirty entries** at the start of this operation
- Clean detached worktree: passed status and `git diff --check`

## Source-level delta

The committed delta is broader than generated catalogs. GitHub removes the
deep-learning agent/skill set and other historical/project material, while the
local branch adds the deep-learning capabilities and retains local ecosystem
content. This should be reconciled as an explicit product decision, not an
automatic merge.

There were no remote-only changes to the primary source files that justify an
immediate replacement of the local canonical tree. Remote-only additions are
primarily catalogs, the generated audit, and root documentation.

## Remote metadata findings

The remote `INDEX.md` and audit identify:

- catalog provenance generated from commit `15c9bbc`, not the current remote tip;
- 75 unresolved `agents.archive/` references in `agents/MANIFEST.csv`;
- CI still missing;
- Markdown files with executable modes needing normalization;
- restricted red-team material requiring deliberate promotion policy.

## Reconciliation decision

Keep the local canonical source and its current backup intact. Before any
future push or merge:

1. review the local two commits independently from the 287 uncommitted files;
2. decide whether the deep-learning removals on GitHub are intentional;
3. regenerate catalogs from the reconciled source commit;
4. add CI checks for manifest paths, file modes, projections, locks, and
   sensitive-path exclusions;
5. push only a reviewed, coherent branch.
