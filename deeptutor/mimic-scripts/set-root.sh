#!/usr/bin/env bash
# shellcheck disable=SC2034
# Source me:  source .../mimic-scripts/set-root.sh
_STANDALONE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export DEEPTUTOR_ROOT="${DEEPTUTOR_ROOT:-${_STANDALONE_ROOT}}"

if [[ ! -f "${DEEPTUTOR_ROOT}/pyproject.toml" ]]; then
  echo "deeptutor-mimic: DEEPTUTOR_ROOT=${DEEPTUTOR_ROOT} missing pyproject.toml" >&2
  echo "Default is this standalone folder; override DEEPTUTOR_ROOT for another checkout." >&2
  return 2 2>/dev/null || exit 2
fi
