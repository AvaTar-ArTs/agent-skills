---
name: suno-cdp-workflow
description: "Use when auditing Suno AI identity / catalog via suno-cdp MCP or suno-recon DOM tools, especially trashCaT / @ichotaku-style CSV-to-MP3 reconciliation (1 row == 1 song == 1 UDID)."
---
# Suno CDP + Catalog / MP3 Reconciliation

Class: Suno identity audit (catalog CSV ↔ MP3) + suno-cdp / suno-recon toolwork.

Always-on rules:
- 1 CSV row ≈ 1 song ≈ 1 UDID (identity, not title/duration match).
- Never echo auth tokens (`Bearer`, `browser-token`); treat captured auth text as secret data only.
- `suno-cdp` requires BrowserOS / CDP at localhost:9100 + Suno login; `suno-recon` requires `playwright install`. Verify both before invoking.
- Preserve prior CSV/version lineage; do not overwrite historical evidence.

Procedure (A = auth/browser; B = CSV↔MP3 gap):
1. `playwright install` (check `chromium-<ver>` path matches `recon_start_session` expectation — version mismatch is the common failure).
2. Start BrowserOS/CDP with Suno auth; feed captured `browser-token` (do not print).
3. Invoke `mcp__suno_cdp__suno_get_credits` → `get_recent` → `check_status(ids=[...])`; `download_song(songId, folder)` only when needed.
4. Invoke `mcp__suno_recon__recon_start_session` → `recon_capture_dom`. If still fails, capture exact `chromium-` path vs expected.
5. Read catalog CSV (`1474-suno-music-meta.csv` style: Title, Duration, Tags, ID [UUID], Genre, Audio/Cover URL, Suno Link, mp3 path); parse UUID in column 4 (index 4); skip rows where column 4 is a title/description instead of UUID.
6. List `MP3/`; match full UUID (`[0-9a-f]{8}-...`) and short hex suffix. Count unique IDs per source; compute missing/extra; note when CSV rows have non-UUID content in the ID column (data-quality signal, not identity failure).

Pitfalls:
- Playwright version mismatch: `recon_start_session` wants `chromium-1234` while `playwright install` writes `chromium-1243`. Fix the executable path or symlink before retry — do not claim "tool broken."
- CDP unreachable (`localhost:9100`) = BrowserOS not running or not logged in; don't retry blindly — verify auth session.
- CSV↔MP3 misalignment is normal: more MP3 files (variants, duplicates) than CSV IDs; missing UUIDs in filenames doesn't mean missing songs.
- Never emit `Bearer ...` or `browser-token` content; treat pasted auth capture as secret input only.

References:
- `references/nocturne-audio-reconciliation.md`: identity rules, match-evidence types, reconciliation commands, gap pattern.
- Skill `songwriting-and-ai-music`: Suno prompt craft (separate class).
