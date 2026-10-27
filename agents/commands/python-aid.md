---
description: Give evidence-first help across Steven's Python ecosystems
argument-hint: [request]
name: Python Aid
---

# /python-aid

Help with the user's Python work using the three approved source surfaces:

- `/Users/steven/pythons` — broad Python/tooling workspace; inspect the relevant subproject before editing.
- `/Users/steven/Music/nocturneMelodies/python` — primary nocturneMelodies automation layer and historical utilities; read its `README.md`, inspect `Development/pyproject.toml`, and run only scoped tests before editing. Preserve lineage and do not bulk-refactor.
- `/Users/steven/Music/nocturneMelodies/story-lyric-pythons` — lyric, story, timing, caption, beat-grid, and creative workflow packages; read `ATLAS.md`, `INDEX.md`, or `PROVENANCE.json` when the request touches those workflows.
- `/Users/steven/Music/nocturneMelodies/other/Discography/enriched-disco.csv` — optional historical inventory index; use it for discovery and lineage clues, not as proof that an old path still exists.

## Known nocturneMelodies aid surfaces

Prefer these existing tools before creating another matcher:

- `tools/build_mp3_match_report.py` — technical MP3 inventory, SHA-256, ffprobe metadata, and catalog-match report.
- `tools/reconcile_suno_catalog.py` — conservative catalog↔active-library reconciliation; UUID is confirmed evidence, title+duration is only probable/ambiguous evidence.
- `tools/build_mp3_duplicate_csv.py` — duplicate relationship report from existing inventory/match TSVs; it does not identify song generations.
- `tools/build_simple_catalog_map.py` — legacy map tied to `reports/reconciliation_suno1466`; inspect its inputs before reuse.
- `tools/inventory_mp3_covers.py` — embedded-cover inspection, currently input/output-path configured; inspect constants before running.
- `tools/quarantine_exact_duplicates.py` — moves exact-byte duplicates; treat as a destructive state change despite its reversible quarantine design. Require explicit authorization, preserve its manifest, and verify afterward.

## Story/lyric routing order

Use the `story-lyric-pythons/ATLAS.md` model rather than filename order:

1. `collection-identity` — establish the authoritative audio, lyric, cover, tags, and UUID family.
2. `lyric-timing-story`, `whisper-timing`, or `whisperx-align` — establish the clock.
3. `lyric-analyze`, `content-awareness`, or `emotion-audio` — interpret meaning and emotional movement.
4. `lyric-storyboard`, `transcript-prompts`, `suno-nanobanana-prompts`, or `sora-storyboard` — design the picture plan.
5. `captions-subtitles`, `instagram-story-surface`, or delivery tools — package the verified result.

Treat `agent-skills-story` as a working clone of methods whose canonical skills live under `~/.agent-skills`. Read `ATLAS.md`, `INDEX.md`, and `PROVENANCE.json` when selecting among same-named scripts. Do not merge variants by filename, shared lyrics, or title alone.

Request: $ARGUMENTS

## Operating rules

1. Interpret the request as a Python-aid task, not permission to reorganize the repositories.
2. Start with read-only discovery. Use exact filename/content search and inspect the smallest relevant source files, manifests, tests, and nested `AGENTS.md` files.
3. Use `rg` plus `fzf` when shortlisting existing scripts is useful. Prefer an existing script over creating a duplicate.
4. Trace symbols to their definitions and usages before changing code. Treat similarly named scripts as separate until lineage is verified.
5. Classify findings as observed, inherited, inferred, or unverified. Preserve provenance and report canonical paths.
6. For `nocturneMelodies`, keep UUID/Suno/catalog identity separate from title, duration, lyric family, or filename similarity. Never merge song generations based only on shared lyrics or title.
7. For story/lyric workflows, preserve the distinction between source meaning, timing data, visual vocabulary, generated outputs, and previews. Do not infer canon from filenames alone.
8. Before implementation, state the smallest proposed change, files to touch, and verification command. If the user has already specified the change, do not ask for redundant approval.
9. Make only scoped, reversible edits. Do not delete, move, rename, archive, install packages, commit, push, or alter secrets unless explicitly requested.
10. Verify with the narrowest relevant test, lint, CLI help, parser check, or dry run. If a check cannot run, say why.

## Routing guide

- Debugging: inspect traceback, reproduce minimally, trace call paths, then patch the root cause.
- Catalog/audio/MP3 linking: use UUID-first evidence and produce a versioned report; leave ambiguous files unmatched.
- Lyric/story/video preparation: inspect the relevant workflow package and its provenance/timing references before touching prompts or media.
- Script selection or cleanup: inventory candidates, compare hashes/lineage, and recommend a canonical source before modifying copies.
- New reusable tooling: search all three surfaces first, then place the smallest tool in the owning ecosystem with a test or dry-run mode.

## Response contract

Report:

- scope and source paths inspected
- evidence-backed finding
- files changed, if any
- verification result
- unresolved ambiguity or next safe step

Never claim a script was run, a file was changed, or a mapping was verified without tool output.