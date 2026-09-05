# Migration 2026-08-10 — invert `.agents/skills` ↔ `.agent-skills/skills`

## What was actually wrong

An earlier audit concluded that `~/.agents/skills` held 34 **duplicate copies** of skills
already present in `~/.agent-skills/skills`, and proposed deleting it.

That was wrong, in a way that would have destroyed data. The real topology was:

```
~/.agent-skills/skills/songsee  ->  SYMLINK ../../.agents/skills/songsee
~/.agents/skills/songsee            REAL DIRECTORY  (the only copy)
```

The canonical library held **symlinks into** `.agents`; the content lived in `.agents`.
`rm -rf ~/.agents/skills` would have deleted the only copy of all 34 skills and left 34
dangling links inside the canonical library.

Two measurement errors produced the false "duplicate" reading:

- `diff -r A B` **follows symlinks**, so it compared each directory against *itself* and
  reported IDENTICAL. Use `diff -r --no-dereference`, or compare inodes of the resolved
  targets.
- `stat -f %i` on a symlink returns the **link's own inode**, which always differs from the
  target's. That test cannot distinguish a copy from a link.

## Where `~/.agents/skills` comes from

The npm package **`skills`** (v1.5.22, run via `npx skills`; lockfile at
`~/.agents/.skill-lock.json`). Inside its bundle:

```js
const AGENTS_DIR = ".agents"; const SKILLS_SUBDIR = "skills";
```

`.agents/skills` is that CLI's hardcoded **universal store** — the shared skills directory
for the ~14 agents that have no directory of their own (Amp, Antigravity, Cline, Codex,
Cursor, Deep Agents, Gemini CLI, GitHub Copilot, Kimi, OpenCode, Warp, Zed, …). Agents that
*do* have their own path (Claude Code, Hermes, Qwen) receive symlinks instead — which is why
the install banner read `universal: … / symlinked: Claude Code, Hermes Agent, Qwen Code`.

It is **not** a legacy Claude Code path, and there is no environment variable to redirect it
(`CLAUDE_CONFIG_DIR`, `CODEX_HOME`, `HERMES_HOME`, `GROK_HOME` exist; nothing for `AGENTS_DIR`).

## What this migration did

Inverted the relationship at the root, so the canonical library owns the content:

```
BEFORE                                  AFTER
.agent-skills/skills/X -> .agents/…/X   .agent-skills/skills/X   [real dir]
.agents/skills/X          [real dir]    .agents/skills -> /Users/steven/.agent-skills/skills
```

- 34 real skill directories moved from `~/.agents/skills` into `~/.agent-skills/skills`,
  replacing the 34 symlinks that pointed at them.
- `~/.agents/skills` replaced by a single symlink to the canonical directory.
- 3 **already-dangling** symlinks removed: `ai-video-generation`, `ccxt-cli`, `ccxt-python`.
  These were broken before the migration. They had to go: their targets
  (`../../.agents/skills/<name>`) would have resolved back through the new root symlink into
  the canonical directory itself, turning each into a self-referential symlink loop.
- `~/.agent-skills/skills/coh-mod` and `coh-mod-narrator` (links into
  `~/CoX-mod-Adventure`) were left untouched.
- `~/.agents/.skill-lock.json` left in place — it sits beside `skills/`, not inside it, and
  the CLI still reads it correctly.

## Why this is the durable fix

The installer resolves `join(home, ".agents", "skills")` at write time and uses ordinary
`readdirSync`/write calls, which follow a directory symlink transparently. So future
`npx skills` runs write **straight into the canonical library** with no wrapper, patch, or
post-install reconciliation step. Universal agents reading `~/.agents/skills` continue to
resolve normally.

## Rollback

```bash
~/.agent-skills/migration-2026-08-10/restore.sh
```

Aborts unless `~/.agents/skills` is currently a symlink (i.e. the migration is in its
applied state). Restores all 34 real directories to `~/.agents/skills`, recreates the 34
canonical symlinks, and recreates the 3 dangling links exactly as they were.

`manifest.json` records the full pre-migration state: every symlink with its raw target,
resolved target, existence, and inode; every legacy entry with inode and recursive child
count.
