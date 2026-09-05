# Bundled mirrors (optional)

Small copies of a few root files for quick diffing. The **canonical** copies live at the **parent** standalone root (`../AGENTS.md`, `../.env.example`, …).

Refresh from whatever **`DEEPTUTOR_ROOT`** points to (defaults to the standalone root):

```bash
source ../mimic-scripts/set-root.sh
../mimic-scripts/sync-bundled-from-root.sh
```
