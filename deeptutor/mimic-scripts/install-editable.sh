#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
# shellcheck source=/dev/null
source "${HERE}/set-root.sh"
cd "${DEEPTUTOR_ROOT}"
EXTRA="${DEEP_EXTRAS:-server}"
exec pip install -e ".[${EXTRA}]"
