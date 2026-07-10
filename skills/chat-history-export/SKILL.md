---
name: chat-history-export
description: Export, search, list, or inspect local AI conversation history from Cline session JSON. Use when asked what was worked on before, to preserve substantial sessions, to search past Cline/Gemini-style sessions, or before major workspace changes that need a durable markdown record.
---

# Chat History Export

Use this skill to work with local Cline session history. The live source data is under `~/.cline/data/sessions`, where each session has metadata JSON and a companion `*.messages.json` file.

## Workflow

1. Prefer the bundled script over undocumented shell aliases.
2. Run with `--dry-run` before a broad export if the user only asked for review or inventory.
3. Export markdown into `~/.cline/chat-history` unless the user gives a different output directory.
4. Treat `~/.cline/data/secrets.json` and provider settings as sensitive runtime state; never export or quote those files.

## Commands

From the skill folder:

```bash
python3 scripts/export_cline_history.py export --dry-run
python3 scripts/export_cline_history.py export
python3 scripts/export_cline_history.py list --limit 20
python3 scripts/export_cline_history.py search "workspace cleanup"
python3 scripts/export_cline_history.py latest
```

Useful options:

```bash
--source ~/.cline/data/sessions
--out ~/.cline/chat-history
--limit 50
```

## Output

Markdown exports include session metadata, prompt/title when present, message timestamps, roles, text content, tool/result JSON summaries when present, model/provider info, and token/cost metrics when available.

The script writes a tracking file at `~/.cline/chat-history/.exported_sessions.json` so repeated exports skip unchanged sessions. Use `--force` to regenerate.

## Host Mirrors

Mirrors may exist under `.qwen`, `.gemini`, `my-supremepowers`, or CloudDocs. Use the active skill folder first, then update mirrors deliberately only when the user asks for cross-host synchronization.
