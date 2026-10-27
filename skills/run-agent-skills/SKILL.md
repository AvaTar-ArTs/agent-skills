---
name: run-agent-skills
description: Run, test, smoke-check, audit, or health-check the ~/.agent-skills library and the hosts that load it (~/.claude, ~/.cursor, ~/.grok). Use to verify skill/agent frontmatter, duplicates, broken links, runtime symlink doors, host drift, or to regenerate the agents catalog CSV.
---

# Run agent-skills

`~/.agent-skills` is a library, not an app: the "running" surface is its Python inspection scripts, a hook test, and the symlink doors that let hosts discover it. The driver is **`~/scripts/run-agent-skills-smoke.sh`** (shell scripts live in `~/scripts`). It runs every check and writes all artifacts to `$OUT`, which defaults to `tmp/smoke/<timestamp>/` inside the repo (git-ignored). It **never writes tracked files**, and never uses `/tmp` or `/private/tmp`, because scratch work stays project-local. Paths below are relative to `~/.agent-skills/`.

## Prerequisites

macOS, `python3` (verified with 3.14.6, stdlib only), `bash`. Nothing to install or build.

## Run (agent path)

```bash
cd ~/.agent-skills
bash ~/scripts/run-agent-skills-smoke.sh            # all checks, ~9s
bash ~/scripts/run-agent-skills-smoke.sh audit      # one check: audit|hooks|doors|hosts|catalog
OUT=tmp/smoke/hosts-check bash ~/scripts/run-agent-skills-smoke.sh hosts   # choose the artifact dir
```

Exit code = number of FAILed checks (0 = healthy; 64 = bad argument). `WARN` lines never fail the run.

| Check | What it does | FAILs when |
|---|---|---|
| `audit` | `scripts/audit_runtime.py`, summarized canonical skill/root-agent counts (dup names, exact dupes, missing frontmatter) | any dangling filesystem symlink |
| `hooks` | every `hooks/tests/*.sh` | a test exits non-zero |
| `doors` | `~/.claude/agents`, `~/.claude/skills`, `~/.agents/skills` symlink targets; dangling links in `active-skills/` | wrong target, not a link, or dangling |
| `hosts` | `~/.cursor/{skills,agents}`, `~/.grok/skills`: entry/link counts, dangling links, entries absent from canonical `skills/` | never (report-only; WARN on dangling) |
| `catalog` | `scripts/export_catalog_csv.py --out $OUT/agents-catalog.csv` (+ sibling CHANGELOG) | script errors |

Artifacts in `$OUT`: `audit.json` (full audit; the source when you need the actual duplicate paths), `audit.err`, `test-*.sh.out`, `agents-catalog.csv`, `agents-catalog-CHANGELOG.md`, `catalog.log`.

## Direct invocation

The scripts all take `--help`, and every one uses argparse, so `--help` is safe:

```bash
cd ~/.agent-skills
mkdir -p tmp/smoke/direct
python3 scripts/audit_runtime.py --pretty > tmp/smoke/direct/audit.json        # read-only JSON to stdout, ~2s
python3 scripts/export_catalog_csv.py --root ~/.agent-skills --out tmp/smoke/direct/agents-catalog.csv   # ~5s, 897 rows
bash hooks/tests/test-pre-tool-autocontext.sh                         # prints "pre-tool-autocontext: PASS"
```

## Gotchas

- **No `timeout` on macOS** (no coreutils `gtimeout` either). Don't wrap commands in `timeout`; the slowest check is ~5s.
- **Default output paths write into the repo.** `export_catalog_csv.py` with no `--out` writes `./tmp-csv/agents-catalog.csv` **relative to the CWD** and appends a CHANGELOG beside it. Always pass `--out` (the driver does).
- **`export_catalog_csv.py --root` defaults to `~/.agents`**, not this repo (per its help text). `~/.agents/skills` is a symlink here, but pass `--root ~/.agent-skills` to be explicit.
- **Audit fields change type:** `missing_frontmatter` / `missing_name` / `missing_description` are `0` when empty and a **list of paths** when not. Count with `len()` on lists; printing raw dumps every path.
- **`audit.json` is large** (~32 KB; duplicate maps list every path). Summarize it; don't paste it into a conversation.
- **Audit scope:** `audit_runtime.py` counts canonical `SKILL.md` files recursively and root-level agent definitions only. Numbered packs, `_incoming/`, policy files, and skill documentation nested under `agents/` are outside the agent count.
- **Markdown links:** this audit reports filesystem symlinks only; it does not validate relative links inside Markdown.
- **Hosts are copies, not links.** `~/.cursor/skills` is ~261 real directories with only 1 link into this library, so Cursor drifts from canonical silently. `~/.grok/skills` links into `../../.agents/skills/…`, so a skill removed here dangles there.

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `WARN dangling: ~/.grok/skills/video-marketing -> ../../.agents/skills/video-marketing` (seen 2026-10-05) | No `video-marketing` skill exists in canonical `skills/`. Restore it here or remove the Grok link. |
| `command not found: timeout` | macOS; drop the wrapper. |
| Summary prints a long list of paths instead of a number | You read a non-empty `missing_*` list raw; use `len()`. |

## Changelog (location history; earlier forms kept for reference)

- **v1 (2026-10-05):** lived at `~/.agent-skills/.claude/skills/run-agent-skills/` with `smoke.sh` beside it. Commands were `bash .claude/skills/run-agent-skills/smoke.sh [audit|…]`; output defaulted to `mktemp -d "${TMPDIR:-/tmp}/agent-skills-smoke.XXXXXX"`; root found via `dirname $0/../../..`. Direct-invocation examples used `/path/to/audit.json` and `/path/to/agents-catalog.csv`; the hosts example used `OUT=/path/to/dir`.
- **v2 (2026-10-05):** moved to canonical `~/.agent-skills/skills/run-agent-skills/` and projected via `active-skills/run-agent-skills -> ../skills/run-agent-skills`; command `bash ~/.agent-skills/skills/run-agent-skills/smoke.sh`; output → `<repo>/tmp/smoke/<ts>/`; root = `${AGENT_SKILLS_ROOT:-$HOME/.agent-skills}`.
- **v3 (2026-10-05, current):** driver moved to `~/scripts/run-agent-skills-smoke.sh` (shell scripts live in `~/scripts`); this dir holds only SKILL.md.
