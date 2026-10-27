# Ecosystem Map

Your machine has multiple AI hosts, each with its own skill/agent loading mechanism.

## The landscape

```
~/.agent-skills/          ← CANONICAL LIBRARY (source of truth)
    skills/               ← 322 top-level folders with SKILL.md; 608 SKILL.md total (2026-10-27)
    agents/               ← archive; Claude loads 7 from ~/.claude/agents
    active-skills/        ← curated symlinks
    backups/              ← dated backups
    tools/                ← Python scripts

~/.agents/skills/         ← DESKTOP COMMANDER projection (symlinks into canonical)
~/.hermes/skills/         ← HERMES projection (cached/flattened, 303 dirs)
~/.claude/skills/         ← CLAUDE CODE projection (symlink doors)
~/.cursor/skills/         ← CURSOR projection (real copies — drifts!)
~/.grok/skills/           ← GROK projection (symlinks)

~/.desktop-commander/     ← Desktop Commander's own skills (separate)
    skills/               ← host-specific skills (find-skills, system-connector, etc.)
```

## Host comparison

| Host | Path | Mechanism | Drift risk |
|------|------|-----------|------------|
| Canonical | `~/.agent-skills/skills/` | Source of truth | N/A |
| Desktop Commander | `~/.agents/skills/` | Symlinks | Low |
| Hermes | `~/.hermes/skills/` | Cached projection | Medium |
| Claude Code | `~/.claude/skills/` | Symlink doors | Medium |
| Cursor | `~/.cursor/skills/` | Real copies | **High** |
| Grok | `~/.grok/skills/` | Symlinks | Low |

## MCP servers (separate system)

Skills and agents are NOT MCP servers. MCP servers are external processes:

```
~/.hermes/spawn-ledger.json    ← registered MCP servers
~/.hermes/cache/mcp_schema_cache.json  ← tool schemas

Example MCP servers:
- suno-cdp (Node, stdio) → /Users/steven/ideo-mcp/vendors/unforced-suno-mcp
- suno-recon (Python, stdio) → /Users/steven/ideo-mcp/vendors/sandraschi-suno-mcp
- chrome-devtools-mcp (npx)
```

## Cross-tool memory

Shared state across tools:
```
~/.agent-skills/skills/cross-tool-memory/   ← SQLite-based cross-tool memory
~/.hermes/memories/                          ← Hermes memory files
```

## Try it yourself

```bash
# Compare skill counts across hosts
echo "Canonical: $(ls ~/.agent-skills/skills/ | wc -l)"
echo "Desktop Commander: $(ls ~/.agents/skills/ 2>/dev/null | wc -l)"
echo "Hermes: $(ls ~/.hermes/skills/ 2>/dev/null | wc -l)"
echo "Claude: $(ls ~/.claude/skills/ 2>/dev/null | wc -l)"
echo "Cursor: $(ls ~/.cursor/skills/ 2>/dev/null | wc -l)"

# Check which hosts exist
for p in ~/.agents ~/.hermes ~/.claude ~/.cursor ~/.grok; do
  test -d "$p/skills" && echo "EXISTS: $p/skills" || echo "MISSING: $p/skills"
done
```

## Next

→ [10: Troubleshooting](10-troubleshooting.md)
