# Home Capability Audit — 2026-08-18

## Scope

Discovered `skills/` and `agents/` directories under `/Users/steven`, excluding dependency/build/cache internals listed in the scanner. The JSON/CSV index records paths and metadata counts, not prompt bodies or secrets.

## Summary

- Capability roots: **3459**
- Skill files: **7789**
- Agent Markdown files: **3285**
- Skill duplicate-name groups: **1806**
- Agent duplicate-name groups: **445**
- Exact duplicate skill groups: **2111**
- Exact duplicate agent groups: **797**

The all-home totals include cache/vendored and archive material. The canonical-source subset is the runtime baseline; host-runtime and project-local files are projections or separate workspaces until explicitly promoted.

## Roots by classification

| Classification | Roots |
|---|---:|
| backup/archive | 99 |
| cache/vendored | 2539 |
| canonical-source | 87 |
| host-runtime | 343 |
| project-local | 391 |

## Recommended consolidation order

1. Keep `/Users/steven/.agent-skills` as the canonical source.
2. Treat healthy host links as runtime projections and repair broken links before adding more copies.
3. Mark project-local and host-specific copies as `active`, `alias`, `reference`, `backup`, or `cache`.
4. Exclude dependency/plugin caches from runtime discovery and refresh this index from the script.

Machine-readable index: `home-capability-index-2026-08-18.json`; root CSV: `home-capability-roots-2026-08-18.csv`.
