# File index — `deeptutor-mimic` standalone

This directory mirrors a **full DeepTutor repo root** plus MY_SETUP helpers.

| Path | Purpose |
|------|---------|
| [`README.md`](./README.md) | Upstream project readme (start here for features/releases). |
| [`How-To.md`](./How-To.md) | Short local setup (also in Downloads clone). |
| [`MIMIC_OVERVIEW.md`](./MIMIC_OVERVIEW.md) | How this standalone tree + `mimic-scripts/` fit together. |
| [`SOURCE_OF_TRUTH.md`](./SOURCE_OF_TRUTH.md) | Defaults, refresh commands. |
| [`COMPONENT_INVENTORY.md`](./COMPONENT_INVENTORY.md) | Package / subsystem map. |
| [`ENV_KEYS.md`](./ENV_KEYS.md) | `.env` keys vs `env_store.py`. |
| [`RUNBOOK.md`](./RUNBOOK.md) | §0–§7 phased walkthrough + `mimic-scripts` shortcuts. |
| [`flows/FLOWS_LOGIC.md`](./flows/FLOWS_LOGIC.md) | Orchestration logic notes. |
| [`bundled/`](./bundled/) | Optional mirrored copies of a few root files. |
| [`mimic-scripts/set-root.sh`](./mimic-scripts/set-root.sh) | `DEEPTUTOR_ROOT` → this folder by default. |
| [`mimic-scripts/install-editable.sh`](./mimic-scripts/install-editable.sh) | `pip install -e ".[server]"` (extra via `DEEP_EXTRAS`). |
| [`mimic-scripts/start-full-stack.sh`](./mimic-scripts/start-full-stack.sh) | Runs `scripts/start_web.py`. |
| [`mimic-scripts/sync-bundled-from-root.sh`](./mimic-scripts/sync-bundled-from-root.sh) | Refreshes `bundled/` from `$DEEPTUTOR_ROOT`. |
| [`mimic-scripts/sync-repo-mirror.sh`](./mimic-scripts/sync-repo-mirror.sh) | Re-syncs this tree from `DEEPTUTOR_MIRROR_SRC`. |

Upstream code: `deeptutor/`, `deeptutor_cli/`, `web/`, `scripts/`, `tests/`, `assets/`, `requirements/`.
