# Reference Architecture

Complete system overview.

## Layer diagram

```
┌─────────────────────────────────────────────────────────┐
│                    USER REQUEST                          │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                    HOST RUNTIME                          │
│  Desktop Commander │ Hermes │ Claude Code │ Cursor       │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                  SKILL DISCOVERY                         │
│  Scan: ~/.agents/skills/ or ~/.hermes/skills/            │
│  Match: request → description field                      │
│  Load: SKILL.md into AI context                          │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                  SKILL EXECUTION                         │
│  AI follows skill instructions                           │
│  May load sub-files (progressive disclosure)             │
│  Uses host tools (read_file, write_file, etc.)           │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│               CANONICAL LIBRARY                          │
│  ~/.agent-skills/skills/     (322 top-level with SKILL.md, 608 total)│
│  ~/.agent-skills/agents/     (archive; Claude loads 7)   │
│  ~/.agent-skills/active-skills/ (curated symlinks)       │
│  ~/.agent-skills/tools/      (Python scripts)            │
└─────────────────────────────────────────────────────────┘
```

## Data flow

```
Canonical skills/ → active-skills/ (symlinks) → Host discovery → Context injection
                   ↕
           ~/.agents/skills/ (DC projection)
           ~/.hermes/skills/ (Hermes cache)
           ~/.cursor/skills/ (Cursor copy)
```

## Audit pipeline

```
bash ~/scripts/run-agent-skills-smoke.sh
  ├── audit     → scripts/audit_runtime.py → audit.json
  ├── hooks     → hooks/tests/*.sh
  ├── doors     → symlink target verification
  ├── hosts     → ~/.cursor, ~/.grok health check
  └── catalog   → scripts/export_catalog_csv.py → agents-catalog.csv
```

## Key files

| File | Purpose |
|------|---------|
| `~/.agent-skills/skills/*/SKILL.md` | Skill definitions |
| `~/.agent-skills/agents/*.md` | Agent definitions |
| `~/.agent-skills/active-skills/*` | Curated symlinks |
| `~/scripts/run-agent-skills-smoke.sh` | Audit driver |
| `~/.agent-skills/scripts/audit_runtime.py` | Audit engine |
| `~/.hermes/spawn-ledger.json` | MCP server registry |
| `~/.hermes/cache/mcp_schema_cache.json` | MCP tool schemas |
| `~/.hermes/config.yaml` | Hermes configuration |

## Quick reference

```bash
# Run full audit
cd ~/.agent-skills && bash ~/scripts/run-agent-skills-smoke.sh

# Count everything
echo "Skills: $(find ~/.agent-skills/skills -name SKILL.md | wc -l)"
echo "Agents: $(find ~/.agent-skills/agents -name '*.md' | wc -l)"
echo "Active: $(ls ~/.agent-skills/active-skills/ | wc -l)"

# Find broken links
find ~/.agent-skills -type l ! -exec test -e {} \; -print

# List MCP servers
cat ~/.hermes/spawn-ledger.json | python3 -c "import json,sys; [print(e['argv']) for e in json.load(sys.stdin)]"
```
