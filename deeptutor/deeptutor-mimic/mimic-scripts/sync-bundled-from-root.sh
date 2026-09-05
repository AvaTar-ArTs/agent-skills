#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
MIMIC=$(cd "${HERE}/.." && pwd)
B="${MIMIC}/bundled"
# shellcheck source=/dev/null
source "${HERE}/set-root.sh"

cp "${DEEPTUTOR_ROOT}/AGENTS.md" "${B}/AGENTS.md"
cp "${DEEPTUTOR_ROOT}/SKILL.md" "${B}/SKILL.md"
cp "${DEEPTUTOR_ROOT}/.env.example" "${B}/env.example"
cp "${DEEPTUTOR_ROOT}/pyproject.toml" "${B}/pyproject.toml"
cp "${DEEPTUTOR_ROOT}/docker-compose.yml" "${B}/docker-compose.yml"
cp "${DEEPTUTOR_ROOT}/Dockerfile" "${B}/Dockerfile"
echo "Synced bundled mirrors from ${DEEPTUTOR_ROOT} → ${B}"
