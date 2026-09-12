#!/bin/bash
# Read a Codex hook event and add a small, relevant memory context message.
# This hook is intentionally fail-open: memory must never block tool use.

set -u

DB_PATH="${AGENT_SKILLS_MEMORY_DB:-$HOME/.agent-skills/memory/shared.sqlite}"
MAX_INPUT_CHARS=2000
MAX_KEYWORDS=8

command -v jq >/dev/null 2>&1 || exit 0
command -v sqlite3 >/dev/null 2>&1 || exit 0
[ -r "$DB_PATH" ] || exit 0

input=$(dd bs=1 count="$MAX_INPUT_CHARS" 2>/dev/null || true)
[ -n "$input" ] || exit 0

context=$(printf '%s' "$input" | jq -r '
  ([.tool_input.command, .tool_input.file_path, .user_prompt]
    | map(select(type == "string" and length > 0))
    | .[0] // "")
' 2>/dev/null) || exit 0
[ -n "$context" ] || exit 0

# Keep only bounded, distinct words. They are escaped again before entering SQL.
keywords=$(printf '%s' "$context" \
  | tr -cs '[:alnum:]_-' '\n' \
  | awk 'length($0) >= 4 && length($0) <= 80 { print tolower($0) }' \
  | awk '!seen[$0]++' \
  | head -n "$MAX_KEYWORDS")
[ -n "$keywords" ] || exit 0

where_clause=""
while IFS= read -r keyword; do
  [ -n "$keyword" ] || continue
  # SQLite string literals escape apostrophes by doubling them.
  escaped=${keyword//\'/\'\'}
  condition="instr(lower(topic), lower('$escaped')) > 0 OR instr(lower(outcome), lower('$escaped')) > 0"
  if [ -n "$where_clause" ]; then
    where_clause="$where_clause OR $condition"
  else
    where_clause="$condition"
  fi
done <<< "$keywords"
[ -n "$where_clause" ] || exit 0

rows=$(sqlite3 -readonly -batch -noheader -separator $'\t' "$DB_PATH" \
  "SELECT topic, COALESCE(NULLIF(outcome, ''), choice) FROM decisions WHERE $where_clause ORDER BY timestamp DESC LIMIT 3;" \
  2>/dev/null) || exit 0
[ -n "$rows" ] || exit 0

message=$(printf '%s\n' "$rows" | awk -F '\t' '{ print "- " $1 ": " $2 }')
printf '%s' "$message" | jq -Rs '{continue:true, suppressOutput:true, systemMessage:("Relevant prior decisions:\n" + .)}'
