# Agent-Skills Lineage and Restore Checkpoint — 2026-10-05

## Executive anchor

A routine review of `AvaTar-ArTs/.Agent-skills` turned into a lineage investigation. It established that `.Agent-skills` is an older subset of this repository (`AvaTar-ArTs/agent-skills`). It also found that 11 skills here had been missing their support files since they were imported, and recovered all 69 of those files from `.Agent-skills` history.

> `.Agent-skills` holds no current file that this repository lacks. Its history is the only part worth preserving, because commit `5dc4c75` held the sole surviving copy of the restored files.

## Scope and evidence boundary

- Session: Claude Code cloud session, 2026-10-03 to 2026-10-05 (UTC).
- Inspected directly: full clones of `AvaTar-ArTs/.Agent-skills` (with history) and `AvaTar-ArTs/agent-skills` at `943a276`.
- Inspected and later dropped: `AvaTar-ArTs/distrokid-gpt` (out of scope; the user linked it by mistake).
- Taken from user-supplied reports, not verified here: `AvaTarArTs_Agent_Skills_Map_v2.zip` (an audit of this repository at `943a276`), and the cross-host memory findings for `.qwen`, `my-codex` and `iterm2-main`.
- Not accessible: the local Mac host, `~/.agent-skills` symlinks, `memory/shared.sqlite`, Engram, `.qwen`, `my-codex`, WorkVault.

## Change log — chronological

Each entry records the request, the action, the result and its verification. The self-evaluation sections that follow critique these entries.

### C1 · 2026-10-03 · "review"
- **Action:** reviewed the last commit of `.Agent-skills` (`90cfe3a Remove plugins folder`, about 12,200 deleted files).
- **Result:** reported 2 findings, both out-of-date docs (`INDEX.md` and `README.md` still described `plugins/`). Concluded that the scripts tolerate the missing folder.
- **Verification:** read the diff and the script source. **The scripts were not run.**

### C2 · 2026-10-03 · "yes"
- **Action:** removed the `plugins/` references from `INDEX.md` and `README.md`, then committed `b49e3ae` on `claude/serene-rubin-uonphz`.
- **Result:** the push failed with HTTP 403 because the GitHub App had no access, so no PR was opened.
- **Verification:** `grep` confirmed no `plugins/` references remained.

### C3 · 2026-10-03 · stop-hook: unpushed commit
- **Action:** retried the push once.
- **Result:** the same 403. Reported the access fix to the user instead of retrying in a loop.

### C4 · 2026-10-05 · "try to add and commit with comment push fetch"
- **Action:** confirmed that the commit already existed, then pushed and fetched. Both succeeded once access was restored.
- **Result:** opened draft PR `AvaTar-ArTs/.Agent-skills#1`, subscribed to its activity, and scheduled a safety-net check-in.

### C5 · 2026-10-05 · bot comments, then "approve"
- **Result:** the ecc-tools security, taxonomy and promotion checks passed. Reference-set readiness came back neutral and not applicable to a docs change.
- **Action:** explained that GitHub does not allow an author to approve their own PR, and offered to merge.

### C6 · 2026-10-05 · distrokid-gpt link; PR comment "read"
- **Action:** an attempt to attach distrokid-gpt with push access was denied by the permission classifier. Did not treat the PR comment "read" as an instruction, and asked in chat instead.

### C7 · 2026-10-05 02:05–02:06Z · PR lifecycle
- **Events:** the PR was closed, reopened, received a comment review ("k"), was marked ready for review, and was merged by the owner as `d596efd`.
- **Action:** cancelled both check-ins on close and on merge.

### C8 · 2026-10-05 · repo link; "3 then 2"
- **Action:** attached distrokid-gpt read-only (it was later dropped) and confirmed that `.Agent-skills` had no open PRs.
- **Result:** ran a whole-repository review of `.Agent-skills`, this time running the scripts and validating front matter. **This review overturned C1.** Findings:
  - 11 skills referenced support files that existed only in the deleted `plugins/` tree.
  - The 3 scripts default to `/Users/steven/.agents`, which yields 0 rows silently elsewhere, and they need Python 3.12 or newer.
  - 24 agent files fail to parse (7 YAML errors and 17 without front matter).
  - A Claude→Codex text replacement produced 131 damaged strings and a `Codex`/`codex` name collision.
  - 22 skills have a name that differs from their directory.
  - 67 agent names are duplicated (34 identical copies, 33 that differ).
  - `INDEX.md` counts and the README remote are out of date.
  - No secrets were found.

### C9 · 2026-10-05 · learning checkpoint (7 lessons) pasted
- **Action:** mapped the lessons onto the pending work: bounded PRs, keeping conflicting versions visible for the user to resolve, recording outcomes, and settling which repository is authoritative before fixing anything.
- **Raised:** distrokid-gpt pins `AvaTar-ArTs/agent-skills` (no dot), so it is a third repository and possibly the canonical one.

### C10 · 2026-10-05 · `AvaTarArTs_Agent_Skills_Map_v2.zip`
- **Result:** compared all 1,050 `.Agent-skills` files with the map's 5,034-file inventory by blob hash:
  - 942 files are identical.
  - 104 changed here later.
  - 3 moved.
  - 1 symlink exists only in `.Agent-skills`.
- **Conclusion:** `agent-skills` is canonical.
- **Corrected 3 map claims:**
  - distrokid-gpt#1 was merged, not open.
  - `Codex-design` resolves to `skills/creative/claude-design`, so it is rename damage rather than a missing skill.
  - The 11 skills lack their support files in `agent-skills` too.

### C11 · 2026-10-05 · "forget distrokid-gpt"
- **Action:** deleted the unmodified local clone and removed distrokid-gpt from scope.

### C12 · 2026-10-05 · cross-host memory and self-evolution findings
- **Action:** adopted the operating settings for the session, stated what could and could not be accessed, and recorded the first self-evolution cycle (see S1).

### C13 · 2026-10-05 · "create a changelog … track and evolve"
- **Action:** attached `agent-skills` with push access (granted) and cloned it at `943a276`.
- **Restore:** recovered 69 support files for 11 skills from `.Agent-skills@5dc4c75:plugins/claude-plugins-official/`, committed as `d3dcf51`.
- **Verification:**
  - 69/69 blob hashes are identical to the source.
  - 45/45 SKILL.md file references resolve.
  - 10 shell scripts pass `bash -n`.
  - All JSON parses.
  - The secret scan was clean.
- **Not restored:** SKILL.md files were left untouched. Their text has diverged from the originals through the rename and later edits.
- **Record:** wrote this checkpoint, its JSON companion, a catalog entry, a CHANGELOG entry and an evolution-history entry.

### C14 · 2026-10-05 · user challenge: "matches the original" does not mean current
- **Challenge:** the files had most likely been amended, extended or improved since that snapshot. C13 had only proved fidelity to one July snapshot.
- **Checked three possibilities:**
  1. **Improved copies elsewhere in the ecosystem:** none. No other copy exists anywhere in `agent-skills`; the files that share names belong to unrelated skills.
  2. **Removed on purpose:** no. Full `agent-skills` history (47 commits) shows that each of the 11 skills was added once, in `e63d23c` (2026-07-15), with only its `SKILL.md`. No support file was ever added or deleted, and no `SKILL.md` has changed since.
  3. **Newer upstream versions:** compared against `anthropics/claude-plugins-official@d182ca4` (2026-10-02). 66 of the 69 files are identical to current upstream. 3 `mcp-integration` files were revised upstream: a real `mcp.asana.com/sse` endpoint was replaced by a placeholder.
- **Action:**
  - Took upstream's versions of those 3 files.
  - Applied the same placeholder fix to the one matching line in `skills/mcp-integration/SKILL.md`.
- **Found:** the `SKILL.md` files were amended before either repository existed. `.Agent-skills@1c08218` (2026-07-09) and the `agent-skills` import contain identical blobs, so the edits were made on the local host and git does not record them.
  - Two of the skills, `mcp-integration` and `plugin-settings`, carry a deliberate "Generalization Notes" section that frames them as host-neutral.
  - The restored support files are host-specific, with about 456 Claude mentions.
  - Whether the support files were left out on purpose cannot be determined from git. Either way, the `SKILL.md` files still cite them, so that generalization was incomplete.

## Checkpoints — verified state at each turning point

| ID | After | Verified state | Open at that moment |
|---|---|---|---|
| K1 | C2 | Docs fix committed locally in `.Agent-skills` | Push blocked by missing GitHub access |
| K2 | C7 | Docs fix merged into `.Agent-skills` main (`d596efd`) | Whether `.Agent-skills` is the right place to invest |
| K3 | C8 | Full defect inventory of `.Agent-skills`; C1's "safe" conclusion overturned | Which repository is canonical |
| K4 | C10 | `agent-skills` is canonical; `.Agent-skills` is a 1,049/1,050 subset; `5dc4c75` is the only source for 69 files | Whether push access to `agent-skills` would be granted |
| K5 | C13 | 69 files restored and verified against the July snapshot | Whether the snapshot is current (raised by the user) |
| K6 | C14 | 66 of 69 files identical to current upstream; 3 updated to upstream; no deliberate removal in git history | Policy for host-specific support files under the host-neutral SKILL.md files |

## Self-evaluation

Each item follows the self-improvement contract: observed failure, then one focused change, then how it was verified.

### S1 — A deletion was declared safe after checking only the code
- **Failure (C1):** the code reviewer checked that the scripts guard `plugins/`, and concluded the deletion was safe. It missed 11 skills whose `SKILL.md` text pointed at files that existed only in `plugins/`.
- **Change:** when reviewing a deletion, search *all* remaining files, including prose and Markdown, for paths into the deleted tree. Do not stop at code imports.
- **Verified:** applied in C8, where it found the 11 skills; then applied again in C13, where it confirmed that `agent-skills` had the same gap.

### S2 — Code was read but not run
- **Failure (C1):** C1 called the scripts "fine" without running them. When they ran in C8, they silently produced 0 rows from their default root and crashed on Python 3.11.
- **Change:** a claim that something "works" requires running it in the target environment, or saying explicitly that it was not run.
- **Verified:** in C13 the restored shell scripts were syntax-checked and the JSON files parsed. The behaviour of the restored scripts was **not** exercised, and this record says so.

### S3 — A partial docs fix left adjacent numbers wrong
- **Failure (C2):** the `INDEX.md` fix removed the `plugins/` lines but kept "42 agents / 173 skills / 914 files". The actual counts are 187 / 168 / 1,050.
- **Change:** when editing a generated document, either regenerate it or verify every figure in the edited section.
- **Verified:** not yet. The next INDEX change in `agent-skills` must regenerate it rather than hand-edit it.

### S4 — Fixing started before authority was established
- **Failure (C2–C7):** the effort went into a repository that turned out to be a superseded subset. The canonical-versus-copy question was only raised in C9.
- **Change:** before fixing anything in a repository, confirm that it is the authoritative source by comparing it with its siblings, catalogs and dependents.
- **Verified:** C10–C13 compared hashes across the repositories before any write to `agent-skills`.

### S5 — Third-party reports were treated as data and checked against live state (kept)
- C6/C7: the PR comment "read" was not acted on as an instruction.
- C10: three claims in the map were tested against live state and corrected.
- Keep this behaviour.

### S6 — A minor method slip, caught by the output itself
- **Failure (C8):** an `awk` split of a CSV that contains quoted commas produced garbage counts.
- **Change:** use a real CSV parser for CSV data.
- **Verified:** the counts were re-run with Python's `csv` module in the same step.

### S7 — Fidelity was reported as if it were currency
- **Failure (C13):** "byte-identical to the original" was presented as the verification. It proved only that the copy was exact. It did not prove that the source was current, that no improved version existed, or that the files fit the amended `SKILL.md` files. The user caught this.
- **Change:** a restore or copy now gets three checks:
  1. **Lineage:** is there a newer or amended version anywhere, including upstream?
  2. **Intent:** was the content removed on purpose? Check history.
  3. **Fit:** does it still match what now references it?
  Verification claims must name which of these were checked.
- **Verified:** applied in C14. It found 3 upstream revisions, ruled out deliberate removal within git, and surfaced the generalization mismatch.

## Unresolved — keep visible, do not resolve silently

0. **Host-specific support files under host-neutral skills:**
   - `mcp-integration` and `plugin-settings` declare themselves general, but their restored references and examples are Claude Code-specific.
   - Options:
     - Keep them as upstream-faithful references, and have each `SKILL.md` label them as Claude Code-specific.
     - Generalize the support files to match their `SKILL.md`.
     - Drop the citations and the files.
   - Needs the user's decision.
1. **Claude→Codex rename:** some of it is deliberate (this is a Codex-facing tree) and some is damage (`Codex.ai`, `Codex Sonnet`, the `claude-code` skill now named `Codex` beside `codex`). The restored support files keep their original Claude wording (`${CLAUDE_PLUGIN_ROOT}`, `~/.claude`), while their SKILL.md files use Codex wording. That inconsistency is deliberate for now and needs a decision.
2. **Duplicates:** 67 duplicated agent names were measured in `.Agent-skills`. The 33 differing pairs need a choice of canonical copy.
3. **Defects not yet re-measured here:** findings C8.2–C8.6 were measured on `.Agent-skills`. Re-run them against `agent-skills` before fixing.
4. **`.Agent-skills` disposition:** add a README pointer to this repository, then archive it. Do not delete it or rewrite its history while `5dc4c75` remains the only provenance record for the restored files.
5. **Host state:** the actual `~/.agent-skills` / `~/.agents` / `~/.codex` links on the Mac remain unverified, as noted in the map and the cross-host findings.

## Continuation order

1. Review and merge the restore PR in `agent-skills`.
2. Re-measure the C8 findings against `agent-skills`, then fix the scripts' default root and Python requirement as one bounded PR.
3. Fix the agent files that fail to parse.
4. Decide the rename policy (item 1 above), then repair the damage in one pass.
5. Regenerate `INDEX.md` and the catalogs from the scripts. Do not hand-edit them.
6. Add the superseded-by pointer to `.Agent-skills`.

## Durable artifacts

- This checkpoint: `docs/checkpoints/2026-10-05-agent-skills-lineage-and-restore.md`
- JSON companion: `docs/checkpoints/2026-10-05-agent-skills-lineage-and-restore.json`
- Indexed in: `docs/CHECKPOINTS-CATALOG.md`, `docs/CHANGELOG.md`, `docs/EVOLUTION_AND_ITEM_HISTORY.md`
- Restore commit: `d3dcf51` on `claude/serene-rubin-uonphz`; upstream refresh in the follow-up commit on the same branch
- Upstream compared: `anthropics/claude-plugins-official@d182ca4` (2026-10-02)
