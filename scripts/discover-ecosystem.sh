#!/bin/bash
# Run this to see what's innately available

echo "🔍 Ecosystem Discovery - What I Know"
echo ""

echo "=== Memory Access ==="
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT COUNT(*) FROM decisions;" 2>/dev/null | xargs echo "Decisions stored:"
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT COUNT(*) FROM patterns;" 2>/dev/null | xargs echo "Patterns tracked:"

echo ""
echo "=== Skills Available (178 total) ==="
ls ~/.agent-skills/skills/ | head -20
echo "... and $(ls ~/.agent-skills/skills/ | wc -l) more"

echo ""
echo "=== Agents Available (204 total) ==="  
ls ~/.agent-skills/agents/ | head -10
echo "... and $(ls ~/.agent-skills/agents/*.md ~/.agent-skills/agents/*/ 2>/dev/null | wc -l) more"

echo ""
echo "=== Pipeline Scripts ==="
ls ~/.agent-skills/scripts/pipelines/ 2>/dev/null

echo ""
echo "=== Last 5 Decisions (context for this session) ==="
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT topic, choice, timestamp FROM decisions ORDER BY rowid DESC LIMIT 5;" 2>/dev/null
