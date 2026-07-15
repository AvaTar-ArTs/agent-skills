---
name: chat-history-export
description: Export, search, list, or inspect local AI conversation history from session JSON. Use when asked what was worked on before, to preserve substantial sessions, to search past Poolside/Claude/Codex sessions, or before major workspace changes that need a durable markdown/JSON record.
---

# Chat History Export

Use this skill to work with local AI session history. Supports multiple tool formats:

- **Poolside**: `~/Library/Application Support/poolside/trajectories` (NDJSON format)
- **Cline**: `~/.cline/data/sessions`
- **Claude Code**: `~/.claude/projects` (JSONL format)
- **Codex**: `~/.Codex/projects`
- **Generic**: Any directory structure with `*.json` metadata and `*.messages.json` files

Poolside trajectories store `session.start`, `session.input`, and `turn.output` events.

## Workflow

1. Prefer the bundled script over undocumented shell aliases.
2. Run with `--dry-run` before a broad export if the user only asked for review or inventory.
3. Export into `~/.config/poolside/chat-history` (or tool-specific directory) unless the user gives a different output directory.
4. Treat `secrets.json` and provider settings as sensitive runtime state; never export or quote those files.

## Commands

From the skill folder:

```bash
# List recent sessions
python3 scripts/export_chat_history.py list --limit 20

# Get the latest session
python3 scripts/export_chat_history.py latest

# Export all sessions to markdown
python3 scripts/export_chat_history.py export

# Dry-run to preview exports
python3 scripts/export_chat_history.py export --dry-run

# Search sessions for a term
python3 scripts/export_chat_history.py search "workspace cleanup"
```

## Options

### Tool Selection

```bash
--tool pool     # Use Poolside trajectories (default)
--tool claude   # Use ~/.claude/projects (JSONL format)
--tool cline    # Use ~/.cline/data/sessions
--tool codex    # Use ~/.Codex/projects
```

### Source and Output

```bash
--source ~/Library/Application\ Support/poolside/trajectories  # Override source directory
--out ~/.config/poolside/chat-history        # Override output directory
--limit 50                                   # Limit number of sessions in list
```

### Export Options

```bash
--force                 # Force re-export even if already exported
--dry-run               # Preview exports without writing files
--format md|json|auto    # Output format (default: auto → markdown)
--session <filter>      # Target specific session by session_id or filename substring
```

## Examples

### List Poolside sessions

```bash
python3 scripts/export_chat_history.py list --tool pool
```

### Export a specific Poolside session

```bash
python3 scripts/export_chat_history.py export --tool pool --session 019f5b57
```

### Work with Claude Code history

```bash
# List Claude sessions
python3 scripts/export_chat_history.py list --tool claude

# Export a specific Claude session
python3 scripts/export_chat_history.py export --tool claude --session 91d0b07f-fae1-4a42-affe-d080b14531fa
```

### Work with Cline history

```bash
# List Cline sessions
python3 scripts/export_chat_history.py list --tool cline

# Export specific session
python3 scripts/export_chat_history.py export --session 1n8r8 --format json
```

### Work with Codex history

```bash
python3 scripts/export_chat_history.py export --tool codex
```

## Output

**Markdown exports** include session metadata, prompt/title when present, message timestamps, roles, text content, tool/result JSON summaries when present, model/provider info, and token/cost metrics when available.

**JSON exports** produce structured data with a `metadata` object and `messages` array.

The script writes a tracking file at `~/.config/poolside/chat-history/.exported_sessions.json` so repeated exports skip unchanged sessions. Use `--force` to regenerate.

## Host Mirrors

Mirrors may exist under `.qwen`, `.gemini`, `my-supremepowers`, or CloudDocs. Use the active skill folder first, then update mirrors deliberately only when the user asks for cross-host synchronization.