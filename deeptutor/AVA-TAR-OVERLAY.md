# AvaTar ArTs — proprietary workspace overlay

This directory is a **full file replication** of the DeepTutor codebase (see upstream clone under `~/AvaTar-ArTs/projects/my-deep` or your canonical path), plus **AvaTar-specific folders** that are not symlinks.

**Placement:** The physical tree lives at `~/PYTHON_MARKETPLACE_MASTER/My-Deep-Proprietary/` so it sits beside marketplace packaging and category reviews. The AvaTar hub still exposes it as `~/AvaTar-ArTs/projects/my-deep-proprietary` (symlink).

## Licensing (read this)

- **`LICENSE`** at the repository root is the **Apache License, Version 2.0** as shipped with DeepTutor. The replicated Python, frontend, Docker, and docs files inherit that license unless you replace them entirely with your own work.
- **`docs/private/LICENSE-AvaTar-ArTs-PROPRIETARY.txt`** states **additional proprietary terms** intended to apply only to **your original files** (for example under `docs/private/` and `packages/proprietary/`). It does **not** relicense upstream DeepTutor files.
- **`NOTICE-THIRD-PARTY.md`** summarizes obligations when mixing OSS and your proprietary additions.

If you redistribute binaries or source, keep Apache notices and required attribution for any DeepTutor-derived portions. For legal certainty on a commercial product, consult counsel.

## What AvaTar added (physical folders)

| Path | Purpose |
|------|---------|
| `docs/private/` | Internal notes, proprietary specs — **not** part of upstream DeepTutor. |
| `packages/proprietary/` | Closed-source packages / extensions you add here. |
| `AVA-TAR-OVERLAY.md` | This file — workspace marker and licensing reminder. |

## Maintenance

- To **refresh** from upstream DeepTutor: repeat `rsync` from your canonical `DeepTutor-main` checkout (exclude `.git`, `node_modules`, `.next`, caches). Resolve conflicts with `docs/private/` and `packages/proprietary/` manually.
- Prefer **`git init`** here only after you decide whether this remote stays **private** and how you track upstream updates (subtree, periodic rsync, or fork).

## Replication note

Populated by copying tree contents (not symlinks) so this folder can be archived, zipped, or pushed to a **private** remote independently of `Downloads/Compressed/DeepTutor-main`.
