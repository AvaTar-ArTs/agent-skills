#!/bin/bash
# Pre-tool hook: auto-loads relevant memory context before tool use
# This makes memory INNATE - always available

TOOL_NAME="$1"
shift
ARGS="$*"

# Get keywords from tool args
keywords=$(echo "$ARGS" | tr ' ' '\n' | head -3 | tr '\n' ',')

# Fetch relevant memory
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT topic, outcome FROM decisions WHERE topic LIKE '%$keywords%' LIMIT 3;" 2>/dev/null
