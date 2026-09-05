#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
# shellcheck source=/dev/null
source "${HERE}/set-root.sh"
exec python "${DEEPTUTOR_ROOT}/scripts/start_web.py" "$@"
