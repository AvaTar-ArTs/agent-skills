---
name: run-pythons
description: Run, list, smoke-test, or launch scripts in the ~/pythons collection via its pythons-sort launcher (pythons_sort.py). Use to find a script, run one with its own arguments, dry-run a command, check launcher guards, or run the CLI tests.
---

# Run pythons

`~/pythons` is ~4,200 standalone scripts plus one real CLI: **`pythons_sort.py`** (installed name `pythons-sort`). It does two things: `info` lists scripts and `run` executes one exact repository-relative script with its own arguments passed through unchanged. Drive everything through it. The driver **`~/scripts/run-pythons-smoke.sh`** (shell scripts live in `~/scripts`) exercises listing, a real script run, the safety guards and the tests. Paths below are relative to `~/pythons/`. All output goes to `.tmp/run-skill/<timestamp>/` (git-ignored).

## Prerequisites

System `python3` (3.14.6) with `pytest` already installed. Nothing to build for the agent path.

## Run (agent path)

```bash
cd ~/pythons
bash ~/scripts/run-pythons-smoke.sh          # all checks, ~5s; exit = number of FAILs
bash ~/scripts/run-pythons-smoke.sh run      # one check: list|run|guards|tests
```

Find and run a script yourself:

```bash
python3 pythons_sort.py info --all                       # 1222 scripts in 5 categories (analysis, cleanup, dedup, rename, scanners)
python3 pythons_sort.py info --category rename
python3 pythons_sort.py run --dry-run directory_tree_csv/tree_to_csv.py -- --help    # prints the command, runs nothing
python3 pythons_sort.py run directory_tree_csv/tree_to_csv.py -- --help
python3 pythons_sort.py run directory_tree_csv/tree_to_csv.py -- directory_tree_csv -o .tmp/run-skill/tree.csv --max-depth 1
```

Everything after `--` goes to the script untouched. Each script has its own interface, so check `-- --help` first.

## Test

```bash
python3 -m pytest tests/test_cli.py -q -p no:cacheprovider     # 14 passed
```

## Installed command (human path)

The package needs Python **< 3.13**. Use uv's 3.12 in a project-local venv:

```bash
[ -x .tmp/run-skill/venv312/bin/python ] || uv venv -q -p 3.12 .tmp/run-skill/venv312   # re-running uv venv on an existing dir exits 2
uv pip install -q -p .tmp/run-skill/venv312/bin/python --no-deps -e .
.tmp/run-skill/venv312/bin/pythons-sort info --category rename
```

## Gotchas

- **`info --all` lists only 1,222 of the ~4,200 scripts.** It scans just the top level of 4 folders plus `scan*` files at the repo root (`CATEGORY_PATHS` in `pythons_sort.py`). `run` still accepts **any** `.py` path inside the repo, so for anything else locate it with `rg --files -g '*name*'` and pass the path.
- **The installed `pythons-sort` runs scripts with its own venv's Python.** In the `--no-deps` venv, any script that imports third-party packages fails. `python3 pythons_sort.py` uses the system 3.14 with your global packages, so prefer it.
- **Legacy subcommands (`analyze`, `cleanup`, `dedup`, `organize`, `scan`, `rename`, `pdf`) are retired.** They exit 2 with a pointer to `info`/`run`. Old docs that use them are stale.
- **Exit codes:** launcher errors (retired command, path escaping the repo, missing script, the launcher itself) all exit **2**. A real run returns the script's own code. Piping to `tail` hides this; check `$?` without a pipe.
- **CSV outputs use CRLF** (`\r\n`), the Python `csv` default. Strip `\r` before exact-matching lines.
- **Scripts write wherever you tell them.** Point outputs (`-o`) at `.tmp/…`, never the repo root.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ERROR: Package 'python-automation-framework' requires a different Python: 3.14.6 not in '<3.13,>=3.9'` | Install into a uv 3.12 venv (above). |
| `no such file or directory: /usr/local/opt/python@3.12/libexec/bin/python3` | That's the `run12` helper in `~/.zshrc`; Homebrew 3.12 is gone. Use `uv venv -p 3.12` (uv has cpython-3.12.14) or `/usr/local/bin/python3.11`. |
| `.tmp/review-venv/bin/python: no such file` | That venv is broken (no interpreter). Create a fresh one as above. |
| Header check fails on a CSV that looks right | CRLF line endings; `tr -d '\r'`. |
| `error: Failed to create virtual environment … already exists` (uv) | Venv is already there; skip creation (the guard above). Don't use uv's suggested `--clear`, which deletes it. |

## Changelog (location history; earlier forms kept for reference)

- **v1 (2026-10-05):** lived at `~/pythons/.claude/skills/run-pythons/` with `smoke.sh` beside it. Commands were `bash .claude/skills/run-pythons/smoke.sh [list|run|guards|tests]`; root found via `dirname $0/../../..`. Venv step was an unguarded `uv venv -q -p 3.12 .tmp/run-skill/venv312`, which exits 2 on re-run.
- **v2 (2026-10-05):** moved to canonical `~/.agent-skills/skills/run-pythons/`, projected via `active-skills/run-pythons -> ../skills/run-pythons`; command `bash ~/.agent-skills/skills/run-pythons/smoke.sh`; root = `${PYTHONS_REPOSITORY:-$HOME/pythons}`.
- **v3 (2026-10-05, current):** driver moved to `~/scripts/run-pythons-smoke.sh` (shell scripts live in `~/scripts`); this dir holds only SKILL.md.
