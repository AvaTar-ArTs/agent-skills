# active-skills projection

Rebuilt: 2026-10-05T00:13:18

Policy: entries are **symlinks** into `../skills/` (or `../skills/.system/`) whenever a canonical counterpart exists.
Materialized copies are kept only for active-only names without a skills/ peer.

Backup of pre-rebuild tree: `/Users/steven/.agent-skills/backups/active-skills-materialized-20261005-001318`
Cleanup manifest: `/Users/steven/.agent-skills/backups/cleanup-manifest-2026-10-05.csv`

Counts this run:
- newly linked: 282
- already symlink: 16
- kept materialized (no canon): 0
- errors: 0

Recounted 2026-10-27 (directory listing, not a rebuild):
- symlinks: 308
- real directories with no `skills/` peer: 9
  (`github-code-review`, `github-multi-repo`, `github-project-management`,
  `github-release-management`, `github-workflow-automation`, `hooks-automation`,
  `sparc-methodology`, `swarm-advanced`, `verification-quality`)
- other entries: `PROJECTION.md`

The 2026-10-05 policy still holds: link when a canonical peer exists, and keep a real directory only when it does not. The "kept materialized: 0" line is the rebuild result from that night, not the current tree.

Claude Code can expose both a skill directory name and its frontmatter `name` as invocation names. To keep the standard and experimental taste skills distinct in this projection, `design-taste-frontend-experimental` links to `../skills/design-taste-frontend`; the standard skill is `taste-skill`, whose frontmatter alias is `design-taste-frontend`.
