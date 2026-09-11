# Audit: `~/.agents` vs `~/.agent-skills` — 2026-09-11

Phase 1 of a home (`~/`) ecosystem index. Read-only. No files deleted.

Companion CSV: `../index-agents-vs-agent-skills-skills-2026-09-11.csv`

## Identity (lstat, no follow)

| Path | Kind | Inode | Physical size | Top-level |
|---|---|---:|---|---|
| `~/.agents` | **real directory** (not a symlink) | 216692106 | 45M | `.skill-lock.json`, `skills/` |
| `~/.agent-skills` | **real directory**, canonical git repo | 203166630 | 271M | `skills/`, `agents/`, docs, zips, catalogs |

`INDEX.md` (last audited 2026-09-05) still says:

```text
~/.agents/skills -> ~/.agent-skills/skills
```

**That link is gone.** `~/.agents/skills` is a real tree (247 children, 333 `SKILL.md`). Canonical `skills/` is a separate tree (252 children, 338 `SKILL.md`). Zero shared inodes. Zero child-level symlinks between the two skill roots.

The 2026-08-10 migration (`migration-2026-08-10/`) inverted links so `npx skills` could use `~/.agents/skills` as the universal store. That topology has since split into two copies.

## Runtime map (this machine, now)

| Surface | Kind |
|---|---|
| `~/.claude/skills` | symlink → `~/.agent-skills/skills` |
| `~/.claude/agents` | symlink → `~/.agent-skills/agents` |
| `~/.codex/superpowers` | symlink → `~/.agent-skills/skills/using-superpowers` |
| `~/.codex/skills`, `~/.codex/agents` | **real** (not the canonical tree) |
| `~/.cursor/skills`, `~/.gemini/skills`, `~/.qwen/skills`, `~/.hermes/skills`, `~/.grok/skills` | **real** |
| `~/.agents/agents` | missing |
| `~/.agent-skills/.agents/skills` | nested extra skills dir (not the live `~/.agents`) |

Claude Code is correctly pointed at canonical. The `skills` npm universal store (`~/.agents/skills`) is a **second copy**, not a link.

## Skill-name comparison

| Relation | Count |
|---|---:|
| Name intersection | 244 |
| Identical `SKILL.md` content (sha256) | 199 |
| Different `SKILL.md` content | 23 |
| Name match but no `SKILL.md` pair | 22 |
| Only in `~/.agents/skills` | 3: `ci-cd-and-automation`, `mcp-builder`, `webapp-testing` |
| Only in canonical `skills/` | 8 including `coh-mod`, `coh-mod-narrator`, `naruto-skills`, plus index/csv files |

Content diffs (do not merge blindly):

`agmsg`, `belt`, `blackbox`, `ccassist`, `chat-history-export`, `claude-code`, `claude-handoff`, `codex`, `content-strategy`, `create-agents`, `create-skill`, `cua-driver`, `dspy`, `find-skills`, `git-guardrails-claude-code`, `hermes-agent-spawning`, `instructor`, `mcporter`, `ml-paper-writing`, `setup-matt-pocock-skills`, `setup-ts-deep-modules`, `statusline`, `writing-for-agents`

Mtimes: 196 agents-side files are newer, 22 canonical-side newer. Newer mtime ≠ newer meaning; 199 hashes still match (copy/touch drift).

## Canonical root composition (271M)

Live:

- `skills/` ~46M (authority)
- `agents/` ~3.7M (authority)
- `catalog/`, `docs/`, `scripts/`, `hooks/`, `memory/`, `plugins/`

Heavy / generated / archive (do not treat as runtime):

- `skills.zip` 15M
- `enriched-.agents.csv` 8.2M
- `agent-skills-meta.csv` 4.4M
- `inventory-agent-skills.json` 2.6M
- `agents.zip`, other csv/zip snapshots
- `backups/`, `tmp/`, `tmp-csv/`, `tmp-md/`
- sibling `~/.agent-skills-backup-2026-08-06` 74M (outside this repo)

`SKILL.md` count walking the **entire** canonical repo (no follow) is 687 because nested copies exist under docs/tmp/nested trees. Authority count is the 338 under `skills/`.

## Measurement rules (re-confirmed)

- Do not use `diff -r` without `--no-dereference`.
- Do not use `stat -f %i` on a symlink as proof of a duplicate.
- This audit used `lstat` / `readlink` / sha256 of `SKILL.md` only.

## Do not do yet

- Do not `rm -rf ~/.agents/skills`. It is the `npx skills` universal store and holds 3 skills canonical does not.
- Do not relink until the 23 content diffs are triaged file-by-file.
- Do not treat `~/.codex/skills` or `~/.grok/skills` as the same tree; they are next audit slices.

## Next slices (home index)

1. Triage the 23 content-diff skills (canonical vs `~/.agents`).
2. Index `~/.claude`, `~/.codex`, `~/.cursor`, `~/.gemini`, `~/.qwen`, `~/.hermes`, `~/.grok` the same way (link vs copy).
3. Refresh `INDEX.md` runtime-boundary block after a decision, not before.
