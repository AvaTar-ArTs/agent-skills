# Plugin Creator Repair Verification

Date: 2026-08-08

## Repaired locations

- `~/.codex/skills/.system/plugin-creator/` — authoritative Codex copy.
- `~/.agent-skills/skills/.system/plugin-creator/` — synchronized cross-tool mirror.

Both locations remain under discoverable `/skills/` trees. No third copy was created at `~/.agent-skills/skills/plugin-creator`.

## Fixes applied

- Made trigger metadata accurately describe marketplace generation as optional.
- Made `skills: "./skills/"` conditional on creating the `skills/` directory.
- Added marketplace preflight before scaffold writes.
- Added cleanup of newly created plugin roots when a later write fails.
- Added atomic JSON replacement for manifests, companions, marketplaces, and cachebusters.
- Required non-empty marketplace names and categories.
- Enforced plugin folder/name and nested skill folder/frontmatter-name identity.
- Required declared `skills/` paths to exist.
- Rejected non-semver version bases before cachebuster mutation.
- Removed the unsupported `hooks` field from the canonical sample and clarified hook-directory behavior.
- Clarified configured marketplace-root path resolution.
- Added a seven-test regression suite to the skill itself.
- Made script file modes consistent with their shebangs.
- Removed the full-directory drift between Codex and `.agent-skills` copies.

## Verification

- Full-directory `diff`: clean.
- Codex skill validation: passed.
- Agent-skills mirror validation: passed.
- Codex regression suite: 7 passed.
- Agent-skills regression suite: 7 passed.
- Ruff across both complete skill directories: passed with zero findings.
- Python compilation: passed.

## Remaining operational caveat

These are `.system` skills and may be replaced by a future host update. The full-directory parity check and cross-tool memory rule should be rerun after Codex upgrades.
