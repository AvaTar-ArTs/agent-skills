#!/usr/bin/env bash
set -euo pipefail
# Refresh this standalone tree from another DeepTutor checkout (default: Downloads).
HERE=$(cd "$(dirname "$0")" && pwd)
DEST="$(cd "${HERE}/.." && pwd)"
SRC="${DEEPTUTOR_MIRROR_SRC:-/Users/steven/Downloads/Compressed/DeepTutor-main}"

if [[ ! -f "${SRC}/pyproject.toml" ]]; then
  echo "sync-repo-mirror: SRC=${SRC} missing pyproject.toml" >&2
  exit 2
fi

rsync -a --delete \
  --exclude 'node_modules' \
  --exclude '.next' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude '.venv' \
  "${SRC}/assets" \
  "${SRC}/deeptutor" \
  "${SRC}/deeptutor_cli" \
  "${SRC}/requirements" \
  "${SRC}/scripts" \
  "${SRC}/tests" \
  "${SRC}/web" \
  "${DEST}/"

for f in \
  .dockerignore \
  .env.example \
  .env.example_CN \
  .gitattributes \
  .gitignore \
  .pre-commit-config.yaml \
  .secrets.baseline \
  AGENTS.md \
  CITATION.cff \
  Communication.md \
  CONTRIBUTING.md \
  DeepTutor.code-workspace \
  docker-compose.dev.yml \
  docker-compose.ghcr.yml \
  docker-compose.yml \
  Dockerfile \
  How-To.md \
  LICENSE \
  pyproject.toml \
  README.md \
  requirements.txt \
  SKILL.md
do
  [[ -e "${SRC}/${f}" ]] && cp -a "${SRC}/${f}" "${DEST}/${f}"
done

echo "Synced standalone root ${DEST} from ${SRC}"
