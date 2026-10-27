# CLAUDE.md

Canonical config for the `~/.agent-skills` library. Behavior-only; kept lean on purpose.
Deeper layer: `PRINCIPLES.md`, `RULES.md` on the host runtimes (`~/.claude`, `~/.Codex`).

## Surfaces & drift

- `~/.agent-skills/skills` and `~/.agent-skills/agents` are the **canonical library**.
  Host runtimes project or link *skills* from this tree. Claude's `~/.claude/agents/`
  is a separate runtime roster of seven copied agent files (measured 2026-10-27); it is
  not a symlink to this archive, and Claude does not auto-load `~/.agent-skills/agents/`.
  When updating an agent, edit the canonical archive source when one exists, then update
  the Claude copy only when that agent belongs in Claude's active roster. Check each
  runtime's own instructions before assuming it uses the same roster.
- **Edit this library first.** Inventories, docs, snapshots, and caches are generated downstream.
- Active Claude skills are the curated projection at `~/.agent-skills/active-skills`.
  Load a non-projected skill by explicit path or by routing through the skill index.
- **`~/.agents/skills` is a symlink to `~/.agent-skills/skills` (since 2026-08-10).**
  Keep the link; do not "clean up" `~/.agents`.
- **Never conclude "duplicate" from `diff -r` or `stat -f %i` alone.** Check `-L`/`readlink` first.

## Agent & skill delegation

- Delegate to an agent only when the work genuinely benefits: large fan-out, parallel
  independent subtasks, or a long task that would otherwise bloat the main thread.
- Do not route routine work through agents.

## Working rules

- File safety: read before write/edit. Absolute paths. Never silently suppress errors.
- Codebase-wide changes: discover all references first, then change in one coordinated pass.
- Commits: clear, descriptive messages; do not self-reference the assistant in them.
- Scratch/temp work: use a project-local `.tmp/` (gitignored), not `/tmp`, unless that is the fallback.
