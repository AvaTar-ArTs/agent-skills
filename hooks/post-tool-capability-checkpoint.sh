#!/bin/bash
# Treat "command not found" as a PATH/capability-resolution checkpoint,
# not proof that a capability is absent. Deliberately fail-open.

set -u

PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:${PATH:-}"
MAX_INPUT_CHARS=65536

command -v jq >/dev/null 2>&1 || exit 0
input=$(dd bs=1 count="$MAX_INPUT_CHARS" 2>/dev/null || true)
[ -n "$input" ] || exit 0

event=$(printf '%s' "$input" | jq -r '.hook_event_name // empty' 2>/dev/null) || exit 0
ROUTE='Deduce the current goal from the request. Invoke exactly one matching skill or flow for that scenario, including skills the prompt did not name. Indexes are clues, not walls. User instructions win.'
SESSION_ROUTE="$ROUTE Begin /innate-workflow: audit the workspace, select the task skill, perform the work, verify it, then update durable memory when appropriate."
if [ "$event" = "PreToolUse" ]; then
  cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // .toolInput.command // empty' 2>/dev/null) || exit 0
  case "$cmd" in
    *export_chat_history.py*)
      case "$cmd" in
        *--dry-run*) exit 0 ;;
      esac
      case "$cmd" in
        *' export '*|*' export')
          jq -cn --arg reason 'Search existing dumps with eza, rg, and fzf before writing a new chat-history export. Empty dest dirs are unused. Wait until a session or dest is named. See /Users/steven/.agent-skills/hooks/capability-continuity.md.' '{decision:"ask",reason:$reason}'
          exit 0
          ;;
      esac
      ;;
  esac
  exit 0
fi
if [ "$event" = "SessionStart" ]; then
  jq -cn --arg msg "$SESSION_ROUTE" '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$msg}}'
  exit 0
fi
if [ "$event" = "UserPromptSubmit" ]; then
  printf '%s\n' "$ROUTE Classify once against /Users/steven/.cursor/docs/USE_CASES_AND_TRIGGERS.md then /Users/steven/.qwen/Logic_Flows.md when they fit. If they do not fit, still deduce from the request. Preserve stage and approvals."
  exit 0
fi
tool=$(printf '%s' "$input" | jq -r '.tool_name // empty' 2>/dev/null) || exit 0
[ "$event" = "PostToolUse" ] || exit 0
case "$tool" in
  Bash|Shell|exec_command|run_terminal_command|*__exec_command|functions.exec|functions.exec_command) ;;
  *) exit 0 ;;
esac

response=$(printf '%s' "$input" | jq -cr '
  .tool_response // ""
  | if type == "string" then . else tostring end
' 2>/dev/null) || exit 0

exit_code=$(printf '%s' "$input" | jq -r '
  if .exit_code != null then .exit_code
  elif (.tool_response | type) == "object" then (.tool_response.exit_code // empty)
  else empty end
' 2>/dev/null) || exit_code=""

not_found=0
sigpipe=0
printf '%s' "$response" | /usr/bin/grep -Eqi \
  '(^|\\n)(zsh|bash|sh):.*:[[:space:]]*[^:[:space:]]+:[[:space:]]*command not found|command not found:[[:space:]]*[^[:space:]]+' \
  && not_found=1
if [ "$exit_code" = "141" ] || printf '%s' "$response" | /usr/bin/grep -Eqi \
  'exit:[[:space:]]*141([^0-9]|$)|SIGPIPE|Broken pipe'; then
  sigpipe=1
fi
[ "$not_found" -eq 1 ] || [ "$sigpipe" -eq 1 ] || exit 0

candidates=()
if command -v eza >/dev/null 2>&1; then
  candidates+=("eza: $(command -v eza)")
else
  for _eza in /opt/local/bin/eza /usr/local/bin/eza; do
    [ -x "$_eza" ] && candidates+=("eza: $_eza") && break
  done
fi
unset _eza
[ -x /usr/local/bin/fzf ] && candidates+=("fzf: /usr/local/bin/fzf")
[ -x /usr/local/bin/rg ] && candidates+=("rg: /usr/local/bin/rg")

if [ "${#candidates[@]}" -gt 0 ]; then
  known="Verified local candidates: $(IFS='; '; printf '%s' "${candidates[*]}")."
else
  known="No predefined candidate is currently present; resolve from the environment."
fi

if [ "$sigpipe" -eq 1 ]; then
  message=$(cat <<EOF
Fix checkpoint: the listing was truncated (exit 141 / SIGPIPE). Under pipefail, the pipeline status is the rightmost non-zero command: eza/rg gets SIGPIPE when head closes the pipe, so the script dies even though head exited 0. That is a broken recipe, not a missing tool and not a reason to skip the rest of the scan.

Fix then re-run: do not pipe eza or rg to head under pipefail. eza --level bounds depth, not file count; use eza --only-dirs for structure, a python walk for counts, rg --max-count/-m for search. Complete the original count. Do not treat partial output as the full result.
Apply the shared reasoning in /Users/steven/.agent-skills/hooks/capability-continuity.md before proposing a new mechanism.
$known
EOF
)
else
  message=$(cat <<EOF
Resolve checkpoint: a shell could not resolve an executable. Inspect the preceding command first, including assignments to zsh's special path variable. Treat this shell's PATH as local evidence.

Resolve before fallback: identify the capability; check command -v and which -a; inspect conventional locations and shell startup; then classify it as PATH-only, elsewhere, unavailable, or inaccessible. Use an absolute path for a verified candidate. If two or more plausible active sources remain, compare provenance, runtime use, and meaning before choosing.

For directory navigation, prefer eza; use fzf after the candidate set is bounded.
Apply the shared reasoning in /Users/steven/.agent-skills/hooks/capability-continuity.md before proposing a new mechanism.
$known
EOF
)
fi

jq -cn --arg message "$message" '{
  hookSpecificOutput: {
    hookEventName: "PostToolUse",
    additionalContext: $message
  }
}'
