# `deeptutor-mimic` — standalone layout + MY_SETUP extras

This directory is a **full runnable DeepTutor tree** (same layout as upstream): `deeptutor/`, `deeptutor_cli/`, `web/`, `scripts/`, `tests/`, `assets/`, `requirements/`, Docker/pyproject/README, etc.

**Default:** treat **`DEEPTUTOR_ROOT`** as **this folder** — no separate Downloads or proprietary path required.

## Bundled MY_SETUP additions

| Path | Role |
|------|------|
| `mimic-scripts/` | Helpers: `set-root.sh` (defaults `DEEPTUTOR_ROOT` here), `install-editable.sh`, `start-full-stack.sh`, `sync-bundled-from-root.sh`, `sync-repo-mirror.sh` (re-sync from Downloads or `DEEPTUTOR_MIRROR_SRC`). |
| `bundled/` | Optional smaller copies of key files; refresh from any root via `sync-bundled-from-root.sh`. |
| `flows/` | `FLOWS_LOGIC.md` — orchestration contract notes. |
| `COMPONENT_INVENTORY.md`, `ENV_KEYS.md`, `RUNBOOK.md`, `SOURCE_OF_TRUTH.md`, `INDEX.md` | Hub docs (safe to keep alongside upstream files). |

Upstream entry remains **[README.md](./README.md)**; quick setup: **[How-To.md](./How-To.md)**.

## Typical commands

```bash
cd ~/PYTHON_MARKETPLACE_MASTER/MY_SETUP/deeptutor-mimic
source mimic-scripts/set-root.sh
./mimic-scripts/install-editable.sh
cp .env.example .env   # edit keys
python scripts/start_web.py
```

Refresh code from another checkout:

```bash
DEEPTUTOR_MIRROR_SRC=/Users/steven/Downloads/Compressed/DeepTutor-main \
  ./mimic-scripts/sync-repo-mirror.sh
```
