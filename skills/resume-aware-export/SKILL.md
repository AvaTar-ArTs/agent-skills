---
name: resume-aware-export
description: Create a compact, local, continuation-ready session handoff keyed by a quit/resume ID. Use when a session is ending, the user wants to save progress for later, provides a resume ID, asks to continue from a previous session, or wants export without exporting all history. Escalate to full history only when explicitly requested or when the targeted session cannot be located.
---

# Resume-Aware Export

Create the smallest useful continuity artifact first. A resume handoff is the default;
full-history export is an explicit escalation.

## Route the request

Choose the first matching path:

| Situation | Action |
|---|---|
| A quit/resume ID is available | Create a targeted chat-history export and a compact session handoff. |
| The session ID is known but no separate resume ID is available | Target the session and use the session ID as the continuity reference. |
| Only a broad topic or “save everything” is requested | Inventory first, then offer or perform an explicit full-history export. |
| The target cannot be found | Search/list the relevant source; do not silently export all history. |

## Targeted export

1. Identify the source tool: `claude`, `cline`, `codex`, or `pool`.
2. Identify the source session ID or a unique filename filter.
3. Preserve the quit/resume ID exactly as supplied.
4. Run a dry run before writing when the source or destination is unclear.
5. Export only the selected session.
6. Add `--force` when a previously exported session must be rewritten with a newly
   supplied resume ID.

```bash
python3 /Users/steven/.agent-skills/skills/chat-history-export/scripts/export_chat_history.py \
  export \
  --tool <claude|cline|codex|pool> \
  --session <session-id-or-filter> \
  --resume-id <resume-id> \
  --force \
  --format md \
  --out <named-output-directory>
```

Use `--format json` when another tool will parse the artifact. Use `--dry-run` before
exporting if the session filter or output path has not been confirmed.

## Compact workspace handoff

Create a local continuation artifact for the current workspace:

```bash
python3 /Users/steven/.agent-skills/skills/session-export/scripts/export_session.py \
  --focus "<session focus>" \
  --resume-id <resume-id> \
  --depth compact \
  --format md \
  --path <workspace>/.agent-exports/<stable-name>.md
```

Use JSON when the handoff will be indexed or consumed programmatically:

```bash
python3 /Users/steven/.agent-skills/skills/session-export/scripts/export_session.py \
  --focus "<session focus>" \
  --resume-id <resume-id> \
  --depth compact \
  --format json \
  --path <workspace>/.agent-exports/<stable-name>.json
```

The handoff exposes `export_mode: resume`, `resume_id`, workspace state, and a
continuation prompt. Treat empty decisions, verification, blockers, and remaining-work
arrays as unknown; add those details to the focus or a follow-up note rather than
inventing them.

## Resume later

When a user provides a resume ID:

1. Search `<workspace>/.agent-exports/` and other approved local export directories for
   the literal resume ID.
2. If no handoff matches, search the relevant local session source with `list`, `latest`,
   or `search`, then target the matching session ID.
3. Read the compact handoff first.
4. Read the targeted transcript only when the handoff leaves an unresolved question.
5. Query durable memory before repeating prior decisions.
6. Continue from the handoff; do not regenerate all history by default.

## Full-history escalation

Offer full-history export only when the user explicitly requests history, archival backup,
cross-session research, or a knowledge-system ingestion run that needs broader evidence.
If the target cannot be located, report the miss and ask whether to broaden the scope;
do not broaden automatically.

```bash
python3 /Users/steven/.agent-skills/skills/chat-history-export/scripts/export_chat_history.py \
  export --tool <tool> --format md --dry-run
```

Review the dry-run scope, destination, and exclusions before removing `--dry-run`.
For downstream indexing, route approved exports through `export-to-knowledge-system`.

## Privacy and integrity

- Keep exports local unless the user explicitly approves another destination.
- Preserve the original resume ID, session ID, source path, timestamps, and export time.
- Do not treat the exporters as a redaction boundary: inspect the selected content for
  secrets and sensitive paths before sharing or indexing it.
- Keep credentials, auth stores, provider settings, runtime databases, caches, and raw
  secrets out of the selected source and destination.
- Do not extract browser tokens or call undocumented provider APIs.
- Preserve unknown or unsupported content as an explicit marker rather than silently
  dropping it.
- Keep originals unchanged; derived summaries never authorize deletion.
- Report the exact output path and verification performed.

## Related skills

- `chat-history-export` — locate and export a targeted transcript or explicit history set.
- `session-export` — create the workspace continuation handoff.
- `export-to-knowledge-system` — turn an approved handoff/export into source-linked knowledge.

The exporters may include absolute workspace paths and transcript content. Apply a
human review or a local sanitization step before external sharing.