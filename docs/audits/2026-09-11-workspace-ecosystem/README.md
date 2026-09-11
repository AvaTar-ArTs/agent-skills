# Workspace ecosystem audit — 2026-09-11

Skill: `workspace-ecosystem-audit`. `scripts/inventory.py` is **not present** in either `~/.agent-skills` or `~/.agents` copies of the skill (only reference CSVs pointing at old `~/my-supremepowers/agents/workspace-ecosystem-audit-data`). This run used a structural walk: **no symlink follow**, no content hash, no preview.

Walks skipped `.git`, `node_modules`, `__pycache__`, `.cache`, `sessions`, `projects`, `logs`, `tmp`. File cap 8000/root (`.codex`, `.cursor`, `.hermes` hit the cap).

Artifacts: `identities.json`, `surfaces.json`, `walk-summaries.json`, `largest-files.csv`.

Companion: `../2026-09-11-agents-vs-agent-skills.md`.

## Identities

| Path | Kind | Notes |
|---|---|---|
| `~/.agents` | real | npm `skills` store, 45M, 333 `SKILL.md` |
| `~/.agent-skills` | real | git library, 271M physical, 687 `SKILL.md` in whole repo walk |
| `~/.claude` | real | skills/agents **symlinks** to canonical |
| `~/.codex` and `~/.Codex` | **same inode** | macOS case-insensitive; one tree, 2.0G physical |
| `~/.cursor` `.gemini` `.grok` `.qwen` `.hermes` `.qodo` | real | |
| `~/.Codex-server-commander` | missing | listed in the skill quick-start, not on disk |
| `~/.supremepower` | missing | still named in `ecosystem-clarity` |

## Who loads skills from where

| Host | `skills/` | `agents/` |
|---|---|---|
| Claude | **link →** `~/.agent-skills/skills` | **link →** `~/.agent-skills/agents` |
| `npx skills` / `~/.agents` | **real copy** | none |
| Codex | real | real |
| Cursor | real (some child links into canonical) | real |
| Gemini, Qwen, Hermes, Grok | real | real where present |
| Codex `superpowers` | **link →** canonical `using-superpowers` | |

Only Claude (and that one Codex superpowers link) honors the agnostic library. Everyone else is a fork.

## Walk slice (excluded caches/sessions; bytes = seen files only)

| Root | Files seen | `SKILL.md` | Seen MB | Capped | Broken links |
|---|---:|---:|---:|---|---:|
| `.agents` | 2382 | 333 | 42 | no | 0 |
| `.agent-skills` | 7851 | 687 | 202 | no | 0 |
| `.claude` | 5849 | 878 | 289 | no | 3 |
| `.codex` | 8001 | 831 | 997 | **yes** | 0 |
| `.cursor` | 8001 | 14 | 417 | **yes** | 0 |
| `.gemini` | 4017 | 446 | 242 | no | 0 |
| `.grok` | 5779 | 937 | 525 | no | 1 |
| `.qwen` | 1232 | 188 | 379 | no | 0 |
| `.hermes` | 8001 | 155 | 702 | **yes** | 0 |
| `.qodo` | 18 | 0 | 0.1 | no | 0 |

`.claude` `SKILL.md` 878 is **plugin marketplace copies**, not the linked library (`os.walk` does not enter the skills symlink). Grok 937 is marketplace-cache + bundled skills.

## Hotspots (do not delete without a manifest)

- **Codex DBs:** `thread_history_1.sqlite` 262MB, `logs_2.sqlite` 151MB, plugin host binaries ~227MB + 63MB.
- **Grok installers:** three `downloads/grok-macos-*` binaries ~148MB each (≈450MB).
- **Claude:** `.ccassist/ccassist.db` 124MB, `plugins.zip` 54MB, `skills.bak/` old inventories 16MB+.
- **Gemini:** `extensions_backup/mcp-toolbox/toolbox` 148MB.
- **Cursor:** SpecStory + Cline extension binaries, not skills.
- **Canonical git:** `skills.zip` 14MB, enriched CSVs, nested audit JSON — librarian weight, not runtime.

Broken links are marketplace-relative (Claude plugin `.gemini`/`.hermes` shims; one Grok marketplace cache). Not the Aug-10 skill-store trap.

## Skill gaps

- `workspace-ecosystem-audit` has no `inventory.py` and no `references/targets.md`.
- Bundled CSV index still points at `~/my-supremepowers/agents/workspace-ecosystem-audit-data` (legacy).
- `INDEX.md` still claims `~/.agents/skills` is a symlink; it is not.

## Risks (ranked)

1. **Two live skill authorities** (`~/.agents/skills` vs `~/.agent-skills/skills`) — `npx` vs git. Highest operational risk.
2. **Per-CLI real `skills/` trees** — Codex/Cursor/Gemini/Qwen/Hermes/Grok will drift from the library.
3. **Cache/history mass** — Codex sqlite, Grok duplicate installers, Claude ccassist + plugins.zip. Cleanup candidates *after* a propose+manifest pass.
4. **Stale docs** naming missing roots (`.supremepower`, `.Codex-server-commander`).

## Not done this run

No deletions. No relinks. No full hash inventory. No `~/` walk outside these roots.

Next useful slices: (1) restore `npx` door symlink after copying the three agents-only skills, or (2) size-propose Codex sqlite / Grok downloads only.
