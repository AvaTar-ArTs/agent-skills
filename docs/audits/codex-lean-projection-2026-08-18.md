# Codex Lean Capability Projection — 2026-08-18

## Change

Codex now uses a curated default agent surface instead of exposing the full
canonical agent tree:

- before: 221 visible agent Markdown files;
- after: 15 curated agent symlinks;
- before: 81 duplicate agent-name groups;
- after: 0 duplicate agent-name groups;
- before: 16 enabled plugins;
- after: 11 enabled plugins.

The full agent projection was preserved at
`/Users/steven/.codex/agents-full-canonical-2026-08-18`. The original Codex
configuration was preserved at
`/Users/steven/.codex/config.toml.pre-lean-20260818`.

Selected canonical skills are available under
`/Users/steven/.codex/skills/curated/`:

- `agent-development`
- `codebase-inspection`
- `diagnosing-bugs`
- `using-superpowers`
- `verification-before-completion`

The complete library remains at `/Users/steven/.agent-skills` for explicit,
on-demand use.

## Disabled optional plugins

Only these five were disabled:

- `zig-lsp@agentsys`
- `coderabbit@claude-plugins-official`
- `desktop-commander@claude-plugins-official`
- `learning-output-style@claude-plugins-official`
- `typescript-lsp@claude-plugins-official`

Core OpenAI, browser, document, spreadsheet, presentation, template, and
Context7 plugins remain enabled.

## Validation

- All 15 agent symlinks resolve to canonical files.
- All curated skill symlinks resolve to canonical directories.
- No broken links in the Codex home audit.
- No duplicate agent names in the active projection.
- Codex configuration parses successfully.
- Existing project/plugin tests remain passing: 38 tests.
- Codex Doctor no longer reports the duplicate `code-reviewer` role.

## Independent Codex findings

Codex Doctor reports a separate warning for the `memories_1.sqlite` runtime
database. A read-only immutable SQLite integrity check returned `ok`, so no
database was moved or rebuilt. The issue should be rechecked after restarting
Codex; it is unrelated to the capability projection change.

The Codex configuration also contains a credential-bearing HTTP header. Its
value was not copied into any report. Rotate that credential and move it to a
proper environment/secret mechanism before treating the configuration as
shareable.

## Rollback

To restore the prior agent surface, replace the curated `agents/` directory
with the preserved `agents-full-canonical-2026-08-18` symlink and restore the
configuration from `config.toml.pre-lean-20260818`. Re-enable the five plugins
only if they are needed.
