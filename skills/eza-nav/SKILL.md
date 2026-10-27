---
name: eza-nav
description: Enhanced file system navigation and directory listing using eza. Use for detailed views, tree structures, and git-aware navigation of your workspace.
creator: AvaTarArTs.org / github.com/AvaTar-ArTs / Steven
---

# eza-nav

Use this skill for all directory and file listing needs. Resolve `eza` with `command -v eza` (do not hardcode `/usr/local/bin/eza`). On this machine that is MacPorts `/opt/local/bin/eza`.

## Usage

### Default (Long Listing)
```bash
./scripts/list_all_files.sh /path/to/directory
```

### Tree View
```bash
./scripts/list_all_files.sh /path/to/directory -t -d 2
```

## Advanced Reference

For detailed command options and advanced filtering, refer to the [EZA_USAGE_GUIDE](references/EZA_USAGE_GUIDE.md).
