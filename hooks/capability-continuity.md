# Capability continuity

## Begin from understanding

At startup or after compaction, recover the actual requested outcome, prior approvals,
corrections, verified results, and next unresolved step from available conversation and
the relevant existing checkpoint. If context is absent, say what is unknown rather than
inventing continuity. Read and apply the shared using-superpowers skill at
`/Users/steven/.agent-skills/skills/using-superpowers/SKILL.md` once per loaded context.
Select the relevant process before choosing tools. A named plugin invocation may select
a different version: identify that source explicitly instead of silently equating it with
the shared copy. Current host tool definitions take precedence over stale mappings.

Judge progress by a completed action or a resolved uncertainty. When corrected, revisit
the premise and its dependent conclusions before proposing another artifact. Carry this
reasoning into the next action without asking the user to repeat established intent.

## Discover and apply

Before declaring a capability missing or creating a hook, agent, skill, or memory mechanism, consult existing sources and the current conversation's corrections. Inspect your preceding actions for causes of apparent failure (including zsh's special `path` variable changing PATH).

Use eza for structure and symlinks, rg for filenames and content, and fzf to narrow candidates. If coverage is uncertain, cross-check with find using equivalent roots, path matching, ignore rules and symlink policy. Follow aliases and registry references; search related meanings rather than stopping at matching names. File presence does not prove runtime activation.

**Session dumps and exports (2026-10-05).** Before writing a new chat-history or conversation export, inventory existing dumps with those same tools. Bounded roots: dest dirs `~/.claude/chat-history`, `~/.cline/chat-history`, `~/.config/poolside/chat-history`; live sources `~/.claude/projects`, `~/.cline/data/sessions`, `~/Library/Application Support/poolside/trajectories`, `~/.grok/sessions`; `~/Downloads` (`chat-export*`, `GPT-Export*`, `chatgpt-export*`, `grok-export*`, `chat_output/`); `~/pythons` exporters that default to Downloads. Empty dest dirs and skill copies are unused destinations. `~/.gemini/docs/CHAT_HISTORY_EXPORT.md` launchd/cron/alias auto-export is stale. A slash-command inventory or `--dry-run` is enough until the user names a session or dest. Warn, then wait. Grok PreToolUse lives in `~/.grok/hooks/export-dumps.json` + `export-dumps.sh` (regular files, not an agent-skills symlink). It asks on `export_chat_history.py export` without `--dry-run`. Reload with `r` in the Hooks tab.

Hookify `hookify.{name}.local.md` files belong in a named project's `.Codex/` directory. Shared Grok behavior stays in this file. Grok runtime hooks are regular files in `~/.grok/hooks/`. Codex/Claude still use `~/.agent-skills/hooks`. Home (`~/`) as workspace is an unused destination for hookify files.

Existing starting points: /Users/steven/.agent-skills/agents/sage.md, /Users/steven/.agent-skills/agents/self-evolution.md, /Users/steven/.agent-skills/agents/integrated-evolution.md, and /Users/steven/.agent-skills/skills/agent-workflow-catalog/SKILL.md. Read relevant definitions before reuse. Prefer one verified incremental improvement; delegate only when authorized and useful. Do not recursively spawn agents or rescan home by default.

Available investigation surfaces include /Users/steven/.codex/plugins, /Users/steven/.codex/skills, /Users/steven/.agent-skills/ (especially packages/supremepowers, skills, agents, hooks, and workflows), /Users/steven/.qwen, and /Users/steven/.gemini. Inspect relevant manifests, configuration, scripts, references, and exposed management tools across these sources before declaring a capability unavailable or handing investigation back to the user. Resolve symlinks and distinguish installed plugin versions from shared authoring sources. Read access does not establish activation, write permission, or authority to bypass hook trust; identify the exact remaining boundary from evidence. This rule incorporates the user's 2026-10-05 correction that these sources are already accessible.

Do not treat the current host's prompt as the whole ecosystem. Sibling runtimes keep their own intent files; read those before mapping a Codex or Grok corner onto them.

- `~/.qwen`: QWEN.md and QWEN_SYSTEM_DEFINITION.md. Intent is AVATARARTS as a business-automation stack (marketplace, clients, `~/pythons`, `~/AVATARARTS`), not a generic coding CLI. Superpowers there were copied from `~/iterm2/superpowers`, not from `~/.agent-skills`. User `settings.json` has no `hooks` key. Nested `~/.qwen/.claude/settings.json` is a Claude plugin enablement file, not Qwen policy. `.env` links into `~/.env.d`. Full self-evolution lives in `~/.qwen/agents/self-evolution/`. Logs are claimed at `~/.qwen/logs/`.
- `~/.gemini`: GEMINI.md. Append-only; canonical skills are `~/.agent-skills/skills/`; generate in the target, do not overwrite canonical. Cursor-imported lifecycle (changelog, git-ai, supremepowers). User `settings.json` has Before/After Agent and Tool hooks to Orca and git-ai. Nested `.claude/`, `backups/`, `supremepower/`, and a root `SKILL.md` are host-local, not the shared library. `GIT_AI.md` points at `~/.git-ai`.

Resolve `settings.json` as this host's user file, then this project's file. Do not glob `~/` or nested `~/.<otherhost>/settings.json`.

Shared Grok workflows belong in `~/.agent-skills/workflows/`; `~/.grok/workflows/` is a runtime door (symlink), not the authoring copy.

When evidence changes a premise, revisit dependent conclusions and remedies. Apply durable improvements at their existing shared source, preserving rationale and marking obsolete claims superseded. Runtime memory may point to that source but must not be the only home for shared behavior. Resume verified work instead of repeating it. Demonstrate learning in the next action; distinguish saved guidance, configured hooks, and observed runtime execution.

## Checkpoint hook — intent, evidence, runtime reach

**Intent.** `post-tool-capability-checkpoint.sh` (canonical at `~/.agent-skills/hooks/post-tool-capability-checkpoint.sh`) is the continuity *mechanism* behind this file. On SessionStart and UserPromptSubmit it injects a route-once instruction (deduce the goal, invoke one matching skill or flow, classify once against the trigger indexes). On PostToolUse it acts only on shell-failure signals ("command not found", exit 141/SIGPIPE) and returns eza/fzf/rg candidates. It is a nudge toward selecting the right capability and recovering from a missing one — it is not a recall store and not a task executor.

**Evidence (2026-10-11).** Registered in `~/.codex/hooks.json` on SessionStart, UserPromptSubmit and PostToolUse. `~/.codex/hooks` is a symlink to `~/.agent-skills/hooks`, so the running script and the canonical script are the same file (`-ef`, one inode). Claude Code does **not** register this script: `~/.claude/settings.json` runs `cc-status`, `discover-first.sh` and `route-once.sh` instead. The PreToolUse export branch that exists in the script is registered by no host and is inert.

**Runtime reach — configuration is not execution.** The script fires in the Codex runtime. It does **not** fire in the OpenCode runtime: there is no OpenCode hook registration and `~/.config/opencode/plugins` is empty. In OpenCode these continuity rules arrive a different way — the user-level `AGENTS.md`, loaded as an instruction file, points at this document. So "the hook is configured" and "the hook ran in front of me" are different claims; say which one you are making.

**Lesson (2026-10-11).** A continuity mechanism is a means, not the deliverable. Before opening a new artifact or wiring a new hook, finish or explicitly park the open review and say which one you did. Record, per change, its intent, its evidence, and whether it actually influences the runtime in front of you — those three are not interchangeable.

## Preserve the next starting point

At a meaningful handoff, update the existing task checkpoint with the result, supporting
source, superseded assumption, and next unresolved action. Keep general lessons here and
task-specific evidence in the task's established record. Avoid a new dated file for each
correction. Revalidate volatile state when needed; saved counts, links and activation
claims are observations from a time, not permanent facts.

Known discovery routes: `~/skills.sh` contains browsable website material; the `skills`
CLI may already be available in npm's execution cache; `~/.agents/skills` was verified
linked to `~/.agent-skills/skills` on 2026-10-05. Inspect existing local sources before
downloading another copy. Distribution and installation do not establish runtime use.
