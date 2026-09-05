# Unified workspace (merged)

**Date:** 2026-05-09

The following were merged into **this** tree (`My-Deep-Proprietary`):

| Former location | What was merged |
|-----------------|-----------------|
| `~/Guides/deeptutor-mimic/` | `mimic-scripts/`, `bundled/`, `flows/`, and hub markdown (`INDEX.md`, `MIMIC_OVERVIEW.md`, `RUNBOOK.md`, `SOURCE_OF_TRUTH.md`, `COMPONENT_INVENTORY.md`, `ENV_KEYS.md`). |
| `~/Guides/MY_SETUP/` (root only) | Hub docs + inventory → [`docs/my-setup-hub/`](./docs/my-setup-hub/). |

**Canonical disk path**

- **`~/PYTHON_MARKETPLACE_MASTER/My-Deep-Proprietary/`** — full tree lives here after rsync from `~/Guides/My-Deep-Proprietary`.

**Compatibility symlinks (still valid)**

- `~/Guides/My-Deep-Proprietary` → **symlink** → this directory.
- `~/Guides/deeptutor-mimic` → `~/Guides/My-Deep-Proprietary` → resolves here.
- `~/Guides/MY_SETUP/deeptutor-mimic` → `~/Guides/My-Deep-Proprietary` → resolves here.

Use **`DEEPTUTOR_ROOT="$PWD"`** from this folder for mimic scripts. Refresh upstream DeepTutor with your usual rsync/git flow; then re-run `mimic-scripts/sync-repo-mirror.sh` if you still mirror from Downloads.

**Canonical proprietary overlay** remains `docs/private/` and `packages/proprietary/` (see `AVA-TAR-OVERLAY.md`).

**Marketplace (`PYTHON_MARKETPLACE_MASTER`)**

- **`MY_SETUP/`** — Ecosystem prose, `home-dot-ecosystem-inventory.json`, and a **separate** full **`deeptutor-mimic/`** checkout (not auto-replaced by this merge). Treat **`My-Deep-Proprietary/`** as the single **product** canonical tree; use **`MY_SETUP/deeptutor-mimic`** only when you want an isolated mimic refresh path, then rsync into proprietary if needed.

**`docs/guides-from-home-Guides/`** — Copy of selected files from **`~/Guides/`** (atlases, hub README, inventory JSON, etc.); see **`README-PROVENANCE.md`** there.
