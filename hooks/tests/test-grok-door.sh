#!/bin/bash
# Grok runtime hooks live in ~/.grok/hooks as regular files.
# This shared tree is Codex/checkpoint only.

set -euo pipefail

GROK_HOME="${GROK_HOME:-$HOME/.grok}"
DOOR="$GROK_HOME/hooks/capability-checkpoint.json"
GROK_TEST="$GROK_HOME/hooks/tests/test-export-dumps.sh"

[ ! -e "$DOOR" ] || {
  echo "Grok must not keep capability-checkpoint.json (symlink or copy)" >&2
  exit 1
}

[ -x "$GROK_TEST" ] || {
  echo "missing Grok-local test $GROK_TEST" >&2
  exit 1
}
bash "$GROK_TEST"

echo "grok-door: PASS"
