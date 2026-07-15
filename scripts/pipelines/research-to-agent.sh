#!/bin/bash
# Research → Agent → Refine Cycle
# Usage: research-to-agent.sh <topic>

topic="$1"
if [ -z "$topic" ]; then
  echo "Usage: research-to-agent.sh <topic>"
  exit 1
fi

# Step 1: Research
echo "🔬 Researching: $topic"
deeptutor run deep_research "$topic" --format json -l en --config-json '{"mode":"report","depth":"standard","sources":["web"]}' 2>/dev/null || echo "deeptutor not installed - using memory pattern"

# Step 2: Check memory for similar research
sqlite3 ~/.memory/memory.sqlite "SELECT topic, choice, outcome FROM decisions WHERE topic LIKE '%$topic%' LIMIT 3;" 2>/dev/null

# Step 3: Suggest agent creation
echo "
📋 Suggested Agent Creation:
Based on research above, create agent with:
- frontmatter: name, description, activation_keywords
- persona: domain expert
- integration: connect to your tools
- memory: store learnings in ~/.memory/
"
