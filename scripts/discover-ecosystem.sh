#!/bin/bash
# Run this to see what's innately available

echo "🔍 Ecosystem Discovery - What I Know"
echo ""

echo "=== Memory Access ==="
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT COUNT(*) FROM decisions;" 2>/dev/null | xargs echo "Decisions stored:"
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT COUNT(*) FROM patterns;" 2>/dev/null | xargs echo "Patterns tracked:"

echo ""
skill_count=$(find ~/.agent-skills/skills -mindepth 1 -type f -name SKILL.md \
  -not -path '*/.git/*' -not -path '*/backups/*' -not -path '*/deeptutor/*' \
  -not -path '*/tmp-*/*' | wc -l | tr -d ' ')
echo "=== Skills Available (${skill_count} SKILL.md files) ==="
find ~/.agent-skills/skills -mindepth 1 -type f -name SKILL.md \
  -not -path '*/.git/*' -not -path '*/backups/*' -not -path '*/deeptutor/*' \
  -not -path '*/tmp-*/*' -print | sed 's#^.*/skills/##' | head -20
echo "... and $((skill_count > 20 ? skill_count - 20 : 0)) more"

echo ""
agent_count=$(find ~/.agent-skills/agents -type f -name '*.md' \
  -not -name README.md -not -path '*/backups/*' -not -path '*/deeptutor/*' \
  -not -path '*/tmp-*/*' | wc -l | tr -d ' ')
echo "=== Agents Available (${agent_count} Markdown files) ==="
find ~/.agent-skills/agents -type f -name '*.md' -not -name README.md \
  -not -path '*/backups/*' -not -path '*/deeptutor/*' \
  -not -path '*/tmp-*/*' -print | sed 's#^.*/agents/##' | head -10
echo "... and $((agent_count > 10 ? agent_count - 10 : 0)) more"

echo ""
echo "=== Pipeline Scripts ==="
ls ~/.agent-skills/scripts/pipelines/ 2>/dev/null

echo ""
echo "=== Last 5 Decisions (context for this session) ==="
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT topic, choice, timestamp FROM decisions ORDER BY rowid DESC LIMIT 5;" 2>/dev/null
