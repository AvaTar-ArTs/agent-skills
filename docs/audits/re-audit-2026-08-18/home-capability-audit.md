# Home Capability Audit — 2026-08-18

## Scope

Discovered `skills/` and `agents/` directories under `/Users/steven`, excluding dependency/build/cache internals listed in the scanner. The JSON/CSV index records paths and metadata counts, not prompt bodies or secrets.

## Summary

- Capability roots: **3668**
- Skill files: **8544**
- Agent Markdown files: **3793**
- Skill duplicate-name groups: **1836**
- Agent duplicate-name groups: **450**
- Exact duplicate skill groups: **2162**
- Exact duplicate agent groups: **810**

The all-home totals include cache/vendored and archive material. The canonical-source subset is the runtime baseline; host-runtime and project-local files are projections or separate workspaces until explicitly promoted.

## Roots by classification

| Classification | Roots |
|---|---:|
| backup/archive | 250 |
| cache/vendored | 2590 |
| canonical-source | 87 |
| host-runtime | 350 |
| project-local | 391 |

## Recommended consolidation order

1. Keep `/Users/steven/.agent-skills` as the canonical source.
2. Treat healthy host links as runtime projections and repair broken links before adding more copies.
3. Mark project-local and host-specific copies as `active`, `alias`, `reference`, `backup`, or `cache`.
4. Exclude dependency/plugin caches from runtime discovery and refresh this index from the script.

Machine-readable index: `home-capability-index-2026-08-18.json`; root CSV: `home-capability-roots-2026-08-18.csv`.
