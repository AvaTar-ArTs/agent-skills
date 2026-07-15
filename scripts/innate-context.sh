#!/bin/bash
# Innate context loader - automatically provides relevant context
# Usage: innate-context.sh <current_task>

task="$1"

# Auto-query memory for similar topics
echo "🔍 Auto-fetched context for: $task"
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT topic, outcome FROM decisions WHERE topic LIKE '%$task%' OR outcome LIKE '%$task%' LIMIT 5;" 2>/dev/null

# Auto-list relevant skills
echo ""
echo "🛠️ Relevant skills:"
echo "  - $task (if exists as skill)"
echo "  - ecosystem-intelligence (always relevant)"
echo "  - agent-creation-guidance (for new work)"
