#!/bin/bash
# Creative Generation → Research Validation → Agent Creation
# Usage: creative-validation.sh <creative_idea>

idea="$1"
if [ -z "$idea" ]; then
  echo "Usage: creative-validation.sh <creative_idea>"
  exit 1
fi

echo "🎨 Creative Idea: $idea"

# Step 1: Generate creatively
echo "
💭 Creative Output Options:
- ascii-art: Text-based art
- comfyui: Image generation  
- architecture-diagram: System diagrams
- baoyu-comic: Comic generation
"

# Step 2: Research validation
echo "🔬 Validation Research:"
sqlite3 ~/.memory/memory.sqlite "SELECT topic, outcome FROM decisions WHERE topic LIKE '%creative%' LIMIT 3;" 2>/dev/null

# Step 3: Agent recommendation
echo "
🤖 Agent Creation Suggestion:
If you want this creative workflow as an agent:
1. Use agent-creation-guidance for structure
2. Focus on the creative skill integration
3. Add memory for learning preferences
"
