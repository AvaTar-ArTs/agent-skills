#!/bin/bash

set -euo pipefail

HOOK_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
HOOK="$HOOK_DIR/pre-tool-autocontext.sh"
TEST_DIR=$(mktemp -d)
trap 'rm -rf "$TEST_DIR"' EXIT
DB="$TEST_DIR/memory.sqlite"

sqlite3 "$DB" <<'SQL'
CREATE TABLE decisions (
  id INTEGER PRIMARY KEY,
  topic TEXT NOT NULL,
  choice TEXT NOT NULL,
  context TEXT,
  outcome TEXT,
  timestamp TEXT DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO decisions(topic, choice, outcome) VALUES
  ('alpha project', 'keep', 'Use the alpha workflow');
SQL

run_hook() {
  AGENT_SKILLS_MEMORY_DB="$DB" bash "$HOOK"
}

output=$(printf '%s\n' \
  '{"tool_name":"Bash","tool_input":{"command":"alpha audit"}}' \
  | run_hook)
printf '%s' "$output" | jq -e '
  .continue == true and
  .suppressOutput == true and
  (.systemMessage | contains("alpha project"))
' >/dev/null

# A malformed command field must not hide a valid file_path fallback.
output=$(printf '%s\n' \
  '{"tool_name":"Write","tool_input":{"command":{},"file_path":"alpha.txt"}}' \
  | run_hook)
printf '%s' "$output" | jq -e '.systemMessage | contains("alpha project")' >/dev/null

# Malformed events fail open and produce no hook output.
if output=$(printf '%s' '{not-json}' | run_hook) && [ -n "$output" ]; then
  echo "malformed input should produce no output" >&2
  exit 1
fi

echo "pre-tool-autocontext: PASS"
