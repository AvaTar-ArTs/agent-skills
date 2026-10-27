# .agent-skills

Canonical skill and agent library for this machine.

## Surfaces

- `skills/` — complete library
- `active-skills/` — curated projection used by Claude Code
- `agents/` — canonical agents
- `docs/` — audits, checkpoints, catalogs

Host runtimes (`~/.claude`, `~/.Codex`, `~/.cursor`, `~/.grok`) consume this tree. Edit here first.

## Working rules

- Keep the `~/.agents/skills` → `~/.agent-skills/skills` link.
- Load a non-projected skill by explicit path or the skill index.
- Do not bulk-import third-party packs; stage through quarantine and inspect first.
- Counts drift; check the directory when a total matters.
