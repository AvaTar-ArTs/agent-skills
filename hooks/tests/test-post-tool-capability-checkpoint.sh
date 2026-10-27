#!/bin/bash

set -euo pipefail

HOOK_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
HOOK="$HOOK_DIR/post-tool-capability-checkpoint.sh"

output=$(printf '%s\n' \
  '{"hook_event_name":"PostToolUse","tool_name":"Bash","tool_response":"zsh: command not found: eza"}' \
  | bash "$HOOK")
printf '%s' "$output" | jq -e '
  .hookSpecificOutput.hookEventName == "PostToolUse"
  and (.hookSpecificOutput.additionalContext | contains("Resolve checkpoint"))
  and (.hookSpecificOutput.additionalContext | contains("eza"))
' >/dev/null

pipe=$(printf '%s\n' \
  '{"hook_event_name":"PostToolUse","tool_name":"run_terminal_command","tool_response":"exit: 141\ndrwxr-xr-x tree"}' \
  | bash "$HOOK")
printf '%s' "$pipe" | jq -e '
  .hookSpecificOutput.hookEventName == "PostToolUse"
  and (.hookSpecificOutput.additionalContext | contains("Fix checkpoint"))
  and (.hookSpecificOutput.additionalContext | contains("141"))
' >/dev/null

if output=$(printf '%s\n' \
  '{"hook_event_name":"PostToolUse","tool_name":"Bash","tool_response":"completed file141.mp4"}' \
  | bash "$HOOK") && [ -n "$output" ]; then
  echo "non-failure output must not trigger the checkpoint" >&2
  exit 1
fi

if output=$(printf '%s' '{not-json}' | bash "$HOOK") && [ -n "$output" ]; then
  echo "malformed input must fail open" >&2
  exit 1
fi

start=$(printf '%s\n' '{"hook_event_name":"SessionStart","source":"startup"}' | bash "$HOOK")
printf '%s' "$start" | /usr/bin/grep -Fq 'Deduce the current goal' || {
  echo "SessionStart must tell the agent to deduce" >&2
  exit 1
}
if printf '%s' "$start" | /usr/bin/grep -Fq 'EXTREMELY-IMPORTANT'; then
  echo "SessionStart must not dump using-superpowers SKILL.md" >&2
  exit 1
fi

submit=$(printf '%s\n' '{"hook_event_name":"UserPromptSubmit","prompt":"continue"}' | bash "$HOOK")
printf '%s' "$submit" | /usr/bin/grep -Fq 'Deduce the current goal' || {
  echo "UserPromptSubmit must tell the agent to deduce" >&2
  exit 1
}
printf '%s' "$submit" | /usr/bin/grep -Fq 'Classify once against' || {
  echo "UserPromptSubmit must classify, not dump continuity" >&2
  exit 1
}
if printf '%s' "$submit" | /usr/bin/grep -Fq 'Available investigation surfaces'; then
  echo "UserPromptSubmit must not cat capability-continuity.md" >&2
  exit 1
fi
if printf '%s' "$submit" | /usr/bin/grep -Eqi 'Bang-use|Deduce-now|!deduce'; then
  echo "UserPromptSubmit must not use a fixed bang token" >&2
  exit 1
fi

ask_snake=$(printf '%s\n' \
  '{"hook_event_name":"PreToolUse","tool_name":"run_terminal_command","tool_input":{"command":"python3 scripts/export_chat_history.py export --tool pool"}}' \
  | bash "$HOOK")
printf '%s' "$ask_snake" | jq -e '
  .decision == "ask"
  and (.reason | contains("eza"))
  and (.reason | contains("existing dumps"))
' >/dev/null || {
  echo "PreToolUse export must ask before writing dumps" >&2
  exit 1
}

ask_camel=$(printf '%s\n' \
  '{"hook_event_name":"PreToolUse","toolName":"run_terminal_command","toolInput":{"command":"python3 scripts/export_chat_history.py export"}}' \
  | bash "$HOOK")
printf '%s' "$ask_camel" | jq -e '.decision == "ask"' >/dev/null || {
  echo "PreToolUse camelCase Grok payload must ask" >&2
  exit 1
}

if output=$(printf '%s\n' \
  '{"hook_event_name":"PreToolUse","tool_name":"run_terminal_command","tool_input":{"command":"python3 scripts/export_chat_history.py export --dry-run"}}' \
  | bash "$HOOK") && [ -n "$output" ]; then
  echo "PreToolUse --dry-run must not ask" >&2
  exit 1
fi

if output=$(printf '%s\n' \
  '{"hook_event_name":"PreToolUse","tool_name":"run_terminal_command","tool_input":{"command":"python3 scripts/export_chat_history.py list --limit 20"}}' \
  | bash "$HOOK") && [ -n "$output" ]; then
  echo "PreToolUse list must not ask" >&2
  exit 1
fi

if output=$(printf '%s\n' \
  '{"hook_event_name":"PreToolUse","tool_name":"run_terminal_command","tool_input":{"command":"eza -la ~/.claude/chat-history"}}' \
  | bash "$HOOK") && [ -n "$output" ]; then
  echo "PreToolUse unrelated shell must fail open with empty stdout" >&2
  exit 1
fi

echo "post-tool-capability-checkpoint: PASS"
