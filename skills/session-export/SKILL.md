---
name: session-export
description: AvatarArts Terminal Session Exporter - creates durable project handoffs for agent continuation
---

# Session Export

Creates continuation-ready session exports with workspace state, decisions, and next steps.

## Usage

```bash
python3 ~/.config/poolside/skills/session-export/scripts/export_session.py --focus "integration task"
```

## Output

Creates `.agent-exports/YYYY-MM-DD_HHMMSS-<slug>.md` containing:

- Session goal and acceptance criteria
- Completed work with evidence
- Workspace changes (git status)
- Commands and verification results
- Errors and diagnostics
- Remaining work and blockers
- Continuation prompt for next agent
- Provenance and privacy notes

## Options

| Option | Values | Default |
|--------|--------|---------|
| `--focus` | Emphasize topic | coding session |
| `--format` | md, json | md |
| `--depth` | compact, standard, deep | standard |
| `--path` | Custom output path | .agent-exports/ |

## Output Contract

### Markdown
- YAML frontmatter with metadata
- Sections: Executive Snapshot, Original Goal, Work Completed, Decisions, Workspace Changes, Commands and Verification, Errors and Diagnostics, Current Repository State, Remaining Work, Continuation Prompt, Session Narrative, Provenance

### JSON
- `schema_version`, `exporter`, `exported_at`, `source`, `title`, `project`, `cwd`, `git`, `status`, `focus`, `original_goal`, `work_completed`, `decisions`, `workspace_changes`, `commands_and_verification`, `errors_and_diagnostics`, `remaining_work`, `continuation_prompt`, `session_narrative`, `provenance`, `redactions`

## Safety Rules

- Read-only workspace inspection except for export file
- No network requests, installs, or mutations
- Secrets redacted as `[REDACTED]`
- Never writes outside workspace without explicit path