#!/bin/bash
# Skill Version → Agent Version → Memory Evolution
# Usage: version-evolution.sh <skill_or_agent>

target="$1"
if [ -z "$target" ]; then
  echo "Usage: version-evolution.sh <skill_or_agent>"
  echo "Shows version history and suggests improvements"
  exit 1
fi

# Find versions
echo "📦 Versions found for: $target"

# Check skill versions
if [ -d "~/.agent-skills/skills/$target/versions" ]; then
  ls ~/.agent-skills/skills/$target/versions/ 2>/dev/null | while read v; do
    echo "  - $v"
  done
fi

# Check agent versions in memory
sqlite3 ~/.memory/memory.sqlite "SELECT topic, choice, timestamp FROM decisions WHERE topic LIKE '%$target%' ORDER BY timestamp DESC;" 2>/dev/null | head -5

# Suggest next iteration
echo "
🔄 Evolution Suggestion:
- Read latest version
- Combine with brainstorming skill  
- Create next version
- Store in memory for tracking
"
