# Host doors

Canonical behavior lives in `post-tool-capability-checkpoint.sh`. Hosts register a trigger only.

Why: the situation is the trigger. Deduce the goal and invoke one match, including skills the prompt did not name. Indexes are clues. No bang token, no `/use`, no skill whitelist. SessionStart is the shared-tree door. Grok PreToolUse lives in `~/.grok/hooks` as regular files (`export-dumps.json` + `export-dumps.sh`); it does not symlink this directory. PostToolUse fires on evidence (command-not-found, exit 141) when a host registers it. The shared script still handles other events if a host registers them (Codex does).

| Host | Trigger | Command target |
|------|---------|----------------|
| Shared | `capability-checkpoint.json` | `/Users/steven/.agent-skills/hooks/post-tool-capability-checkpoint.sh` |
| Grok | `~/.grok/hooks/export-dumps.json` (regular file) calling `~/.grok/hooks/export-dumps.sh` | Grok-local; inspect source=`user` path=`~/.grok/hooks` |
| Codex | `~/.codex/hooks.json` plus `~/.codex/hooks` → this directory | same script |
| Project test | `~/test-hooks/.grok/hooks/capability-checkpoint.json` (symlink) | same script |

Grok global `~/.grok/hooks/*.json` is always trusted. A symlink JSON in that directory did not show up in `grok inspect`; a regular file does (`source=user path=~/.grok/hooks`). Project `.grok/hooks/*.json` needs folder trust (`~/test-hooks` in `~/.grok/trusted_folders.toml`). Do not put `[[hooks.*]]` in `config.toml` for this host: inspect treated `hooks` as an unknown field. `PreToolUse` `ask` is the visible path; `permission_mode` always-approve may auto-answer it. Reload with `r` in the Hooks tab.
