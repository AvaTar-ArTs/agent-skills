---
name: reanalyze-entire-conversation
description: Use when asked to audit, reanalyze or review a whole past conversation or session from its first message, compare it with earlier sessions or checkpoints ("previous selves"), and save the findings, including requests like "begin at the start of your conversation", "review my previous history and compare", or "save checkpoints for what you missed".
---

# Reanalyze entire conversation

## Overview

A self-audit is only worth reading if every number in it was measured by something independent of the thing being audited. Your own memory of the session, an earlier summary, and a loose text search are the weakest evidence: in two audits of one session they produced a false credential alarm, a self-correction count that matched a folder name, a "question-ending" metric computed from clipped text, and a note written before the number it relied on was read. Measure first, spot-check, then write.

Use this for whole-session reviews. Not for: exporting a transcript (`session-export`, `chat-history-export`), a one-off reasoning gate before an action (`ralph-self-audit`), or code review.

## Procedure

1. **Look before building.** Read the user's feedback notes, the latest checkpoint for this work, and the memory index; check for an existing map of the area you will compare (e.g. a HOOK-MAP, earlier `pass1`/`pass2` checkpoints). Settle the transcript path (`~/.claude/projects/<project>/<session>.jsonl`) from the notes before searching. Reuse beats rebuild: earlier audits of the same session are versions to extend, never to overwrite.
2. **Extract, never read raw.** Run `scripts/extract_transcript.py <session.jsonl> <out_dir>` into a real, visible project folder (not `/tmp`). It writes a masked `timeline.tsv` and `stats.json` (counts, errors, classifier blocks, mid-turn queued user messages, token-shaped hits as counts only). Raw lines hold images and secrets.
3. **Measure, then spot-check.** Every figure in the report comes from a script or a re-run. For any count built from a text pattern, open three hits and three near-misses before trusting it. Known traps: folder or file names that look like a marker (`x20`), words that look like a command (`INSERT`), key-shaped runs inside image payloads, and metrics computed from clipped text (recompute from the raw field). The extractor's `USER` row count is an upper bound, not "typed prompts": it also holds slash-command wrappers, pasted blocks and compaction summaries. Report the split (hand-typed, typed with a paste, slash command, summary) and say how you drew it. If `masked_lines` is above 0, locate each masked line (line number, role) before saying "no secrets".
4. **Walk the chronology in windows** around each user correction and each mid-turn message. List typed prompts, queued corrections, errors, skill and agent calls, classifier blocks, and how your replies ended.
5. **Ledger the changes.** Files created or edited against the changelog; memory and index integrity with `scripts/check_memory_links.py <memory_dir>`; claims you made against what later evidence showed (state each claim, then the superseding evidence).
6. **Compare.** Earlier checkpoints, decision rows, the user's own prompt history on the topic, and other hosts' selves where they exist. Record where they converge and where they diverge, with sources.
7. **Save.** Write a NEW checkpoint note (see `references/report-template.md`), append one index line, add one Engram entry (no secrets), and add a decision row only for something decided. Write notes only after the numbers are in front of you, not in the same command that produced them. A changelog entry is needed only if config changed.
8. **Report.** Lead with corrections to your own earlier claims, then new findings, then what you did not verify. Keep it short; no closing menu of options.

## Secrets

Never print a credential or an unfinished-looking token. Report count, location (line, field, role) and at most a masked fingerprint. Classify by location: a key-shaped run inside an `image` payload is almost certainly base64 noise, a key-shaped value in a tool result or prompt is not. If asked to "paste them so I can rotate them", give locations and counts, and offer to open the exact line for the user.

## Red flags (all mean: stop and re-measure)

| Thought | Reality |
|---|---|
| "The regex count is close enough" | Free-text patterns overmatch; spot-check hits both ways |
| "My earlier summary said so" | A summary is a claim, not evidence; re-derive it |
| "The text I have is the text" | Extractions clip; compute length and endings from raw |
| "I'll write the note while measuring" | The number can contradict the note; read the output first |
| "No existing process for this" | Search skills, agents, maps and earlier checkpoints first |
| "Paste the keys so they can rotate" | Locations and masked fingerprints are enough |

## Quick reference

```bash
python3 -I scripts/extract_transcript.py <session.jsonl> <out_dir>        # timeline.tsv + stats.json
python3 -I scripts/check_memory_links.py <memory_dir> [--glob 'note*.md'] # index/wiki-link integrity
```
