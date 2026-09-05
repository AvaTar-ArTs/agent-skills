# Source of truth — standalone `deeptutor-mimic`

This folder **is** a complete DeepTutor project root (`pyproject.toml`, `deeptutor/`, `web/`, upstream `scripts/`, etc.). You can run **`python scripts/start_web.py`** here without another checkout.

```text
+ STANDALONE_ROOT=/Users/steven/PYTHON_MARKETPLACE_MASTER/MY_SETUP/deeptutor-mimic
+ UPSTREAM_REFERENCE=/Users/steven/Downloads/Compressed/DeepTutor-main
```

| Piece | Location |
|-------|----------|
| Editable app | **This directory** (`STANDALONE_ROOT`) |
| MY_SETUP helpers | `mimic-scripts/*.sh` |
| Extra prose | `MIMIC_OVERVIEW.md`, `RUNBOOK.md`, `flows/`, `COMPONENT_INVENTORY.md`, … |
| Optional file duplicates | `bundled/` (refresh via `mimic-scripts/sync-bundled-from-root.sh`) |

Refresh Python/web trees from another disk copy:

```bash
DEEPTUTOR_MIRROR_SRC=/Users/steven/Downloads/Compressed/DeepTutor-main \
  ./mimic-scripts/sync-repo-mirror.sh
```

Override **`DEEPTUTOR_ROOT`** only when you intentionally want helpers to target **`My-Deep-Proprietary`** or another clone instead of this folder.
