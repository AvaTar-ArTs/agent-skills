# 2026-10-05 Codex / Cursor / Hermes reclaim

Approved execute of the 3.9G staging/cache set. Ruflo tmp clone, sessions, sqlite, extensions, and Hermes `state.db` were held.

- Tool: Grok Build, `rm -rf` / truncate, 2026-10-05T23:15:13Z
- Manifest: `cleanup-manifest.csv`
- Before: `~/.codex` 7.2G, `~/.cursor` 2.4G, `~/.hermes` 2.1G
- After: `~/.codex` 3.6G, `~/.cursor` 2.3G, `~/.hermes` 2.0G
- Live daemon still `0.160.1`. Unpacked `chrome-mac-x64/` kept. `worker.log` truncated to 0 bytes.

Restore is Time Machine or re-download. These were `.tmp` clones, an old daemon release, a duplicate zip, and a log.
