# Agent Skills Backup Comparison — 2026-08-18

## New backup

Created a complete metadata-preserving snapshot:

```text
/Users/steven/.agent-skills-backup-2026-08-18
```

Size: **215 MB**. A final `rsync -aHnrc --delete` verification reports **zero
remaining differences** between the current source and this backup.

The source tree was not modified. The mirror operation only wrote the new
backup destination.

## Compared sources

| Source | Size | Assessment |
|---|---:|---|
| `.agent-skills-backup-2026-08-18` | 215 MB | Current verified snapshot |
| `.agent-skills` | 215 MB | Canonical current source |
| `.agent-skills-backup-2026-08-06` | 74 MB | Older partial directory snapshot; substantial drift |
| `.agent-skills.zip` | 63 MB | Older ZIP snapshot with 1,445 regular entries |
| `.agents` | 4 KB | Compatibility directory, not a content backup |
| `.agents.pre-agent-skills-link-20260713-1420` | 12 KB | Pre-link settings snapshot only |

## Older directory backup delta

Compared with `.agent-skills-backup-2026-08-06`, the current source produces
10,480 rsync dry-run records, including:

- 6,609 current-side file additions/changes
- 159 paths present only in the old backup, including the removed research
  skill bundle and older generated artifacts
- 1,111 file timestamp/content metadata differences
- 96 mode/metadata changes

The old backup should be retained as historical recovery material, not treated
as a current mirror.

## ZIP comparison

The ZIP contains an older `.agent-skills/`-prefixed snapshot with:

- 1,445 regular entries
- 206 `SKILL.md` files
- 216 agent Markdown files

It also contains `.git`, nested archives, and macOS metadata. It is not a
complete current representation of the 215 MB source tree.

## Compatibility paths

`/Users/steven/.agents` contains only:

- `.skill-lock.json`
- `skills -> /Users/steven/.agent-skills/skills`

It is a compatibility projection, not an independent backup.

The pre-link directory contains only `.poolside/settings.local.yaml` and
`.DS_Store`; it does not contain the former skills tree.

## Recommendation

Use `.agent-skills-backup-2026-08-18` as the recovery snapshot. Keep the
2026-08-06 directory and ZIP until the current GitHub/local reconciliation and
worktree cleanup are complete. Do not delete either historical artifact yet;
they contain older material that is no longer present in the canonical tree.

## Superagents / superskills comparison

No literal `superagents/` or `superskills/` directories were found. The
equivalent host surfaces are:

| Surface | Skills | Agents | Relationship |
|---|---:|---:|---|
| `.codex/superpowers` | 1 projected entry | — | Symlink to canonical `skills/using-superpowers` |
| `.claude/skills` | 306 projected contracts | — | Symlink to canonical `skills/` |
| `.claude/agents` | — | canonical projection | Symlink to canonical `agents/` |
| `.agents/skills` | 306 projected contracts | — | Symlink to canonical `skills/` |
| `.qwen/superpowers` | 105 | 2 | Independent copied ecosystem |
| `.gemini/supremepower` | 26 | 15 | Independent copied ecosystem |

The GitHub repository `AvaTar-ArTs/agent-skills` contains no literal
`superagents` or `superskills` paths. Its latest catalog files report 186
indexed skills and 218 agent/config files, generated from source commit
`15c9bbc`; the remote tip is newer, so those catalog provenance fields are
already stale.

The Qwen and Gemini copies should be classified as host-specific projections
or historical forks, not merged blindly into the canonical backup. Their
independent content should be reconciled by skill/agent name and content hash
before promotion.
