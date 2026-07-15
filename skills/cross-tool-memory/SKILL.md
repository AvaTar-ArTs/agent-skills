---
name: cross-tool-memory
description: Cross-tool memory bridge using ~/.agent-skills/memory/shared.sqlite for ALL AI tools
---

# Cross-Tool Memory Bridge

## Database Location
`~/.agent-skills/memory/shared.sqlite` (symlinked to ~/.memory for backward compatibility)

## Memory Tables
- **decisions**: topic, choice, context, outcome, timestamp
- **patterns**: pattern, frequency, confidence, first_seen, last_seen  
- **preferences**: key, value, source, timestamp

## Operations
```bash
# Record
sqlite3 ~/.agent-skills/memory/shared.sqlite "INSERT INTO decisions (topic, choice, context, outcome) VALUES ('topic', 'choice', 'context', 'outcome');"

# Query
python3 ~/.agent-skills/skills/self-evolving-memory/scripts/query_memory.py <term>

# Export
python3 ~/.agent-skills/skills/cross-tool-memory/scripts/export_decisions.py decisions json
python3 ~/.agent-skills/skills/cross-tool-memory/scripts/export_decisions.py decisions md --topic <term>
python3 ~/.agent-skills/skills/cross-tool-memory/scripts/export_decisions.py preferences csv
```

## Export Formats

The `export_decisions.py` script supports:
- **json** - Machine-readable JSON array for programmatic use
- **md** - Markdown report with timestamps for human review
- **csv** - Spreadsheet-friendly CSV for analysis

## Symlinks
Skills are symlinked from `~/.agent-skills/` to `~/.config/poolside/skills/` for centralized access.
