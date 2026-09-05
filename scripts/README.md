# Scripts — ~/.agent-skills/scripts/

**7 utility scripts · 3 pipeline scripts · Audited August 18, 2026**

Utility scripts for ecosystem analysis, catalog generation, context injection, and automated pipelines. These scripts generate the large catalog files in `../tmp-csv/` and `../tmp-md/`.

---

## Root Scripts

### `chatgpt-exporter-userscript.js`

**Size:** 903 KB  
**Language:** JavaScript (browser userscript)  
**Purpose:** Export complete ChatGPT conversation history from the ChatGPT web interface. Install in a userscript manager (Tampermonkey, Greasemonkey) and run while on the ChatGPT site.

---

### `discover-ecosystem.sh`

**Size:** 582 bytes  
**Language:** Bash  
**Purpose:** Scans and summarizes the local AI ecosystem structure. Quick inventory of what exists where across `skills/`, `agents/`, `hooks/`, `memory/`, and `scripts/`.

**Usage:**
```bash
bash ~/.agent-skills/scripts/discover-ecosystem.sh
```

---

### `export_catalog_csv.py`

**Size:** 9.9 KB  
**Language:** Python 3  
**Purpose:** Exports all skills and agents metadata to structured CSV catalogs. Reads SKILL.md frontmatter and agent .md frontmatter, produces catalog files in `../tmp-csv/`.

**Outputs:**
- `../tmp-csv/agents-catalog.csv` (170 KB) — all agents with metadata
- `../tmp-csv/what-they-do.csv` (477 KB) — skill/agent purpose descriptions
- Associated CHANGELOG files

**Usage:**
```bash
python3 ~/.agent-skills/scripts/export_catalog_csv.py
```

---

### `innate-context.sh`

**Size:** 582 bytes  
**Language:** Bash  
**Purpose:** Injects session context at conversation start. Companion to the pre-tool hook — this handles session-level context (as opposed to the per-tool memory injection in `../hooks/pre-tool-autocontext.sh`).

**Usage:** Typically triggered at session start by hook configuration, not manually.

---

### `inspect_md_content.py`

**Size:** 14 KB  
**Language:** Python 3  
**Purpose:** Analyzes and indexes the full Markdown content of all files in the ecosystem. Produces a searchable content index for discovery and analysis.

**Outputs:**
- `../tmp-csv/md-content-index.csv` (6.4 MB) — complete content index with file path, content, size
- `../tmp-md/md-content-report.md` (380 KB) — Markdown report of content analysis

**Usage:**
```bash
python3 ~/.agent-skills/scripts/inspect_md_content.py
```

### `audit_runtime.py`

**Purpose:** Audits the active runtime surface separately from backups,
generated catalogs, memory exports, and the Deeptutor project. Checks skill and
agent frontmatter, duplicate names, exact duplicate content, and broken links.

**Usage:**
```bash
python3 ~/.agent-skills/scripts/audit_runtime.py --pretty
```

This is the focused freshness check for `README.md` and `INDEX.md`; it emits
JSON so CI or a later manifest generator can consume the same facts.

### `audit_home_capabilities.py`

**Purpose:** Discover `skills/` and `agents/` roots across the home directory,
classify them as canonical, host-runtime, project-local, backup/archive, or
cache/vendored, and write a path-only inventory without copying prompt bodies.

**Usage:**
```bash
python3 ~/.agent-skills/scripts/audit_home_capabilities.py --home /Users/steven
```

Outputs are written to `docs/audits/home-capability-*` with JSON, CSV, and a
human-readable Markdown summary.

### `capability_control_plane.py`

Builds the machine-readable authority layer for the ecosystem. It records
canonical capability metadata and SHA-256 hashes, checks primary projections
and broken links, treats `.agent-skills/.skill-lock.json` as authoritative,
and emits separated `active`, `projected`, `project-local`, `archived`, and
`cached` indexes. Sensitive/auth/history/session paths are excluded.

```bash
python3 ~/.agent-skills/scripts/capability_control_plane.py \
  --home /Users/steven \
  --home-audit ~/.agent-skills/docs/audits/home-capability-index-2026-08-18.json
```

Outputs are written to `../catalog/`. The optional `--full-home` mode rescans
all capability roots; it is intentionally opt-in because package caches can be
large. The normal mode uses the canonical tree plus a prior path-only home
audit for classified root evidence.

---

### `summarize_what_they_do.py`

**Size:** 12 KB  
**Language:** Python 3  
**Purpose:** Reads SKILL.md and agent .md files, generates natural-language summaries of what each skill and agent does, and produces both CSV and Markdown output files.

**Outputs:**
- `../tmp-csv/what-they-do.csv` (477 KB) — machine-readable summary table
- `../tmp-md/what-they-do.md` (272 KB) — human-readable summary document

**Usage:**
```bash
python3 ~/.agent-skills/scripts/summarize_what_they_do.py
```

---

## Pipeline Scripts (`pipelines/`)

Three executable shell scripts implementing end-to-end automated workflows:

---

### `pipelines/creative-validation.sh`

**Purpose:** Validates output from creative skill invocations. Checks for:
- Expected artifacts (files created, formats correct)
- Format compliance (SKILL.md frontmatter, asset naming)
- Quality markers before accepting creative output as complete

**Usage:**
```bash
bash ~/.agent-skills/scripts/pipelines/creative-validation.sh [output-path]
```

---

### `pipelines/research-to-agent.sh`

**Purpose:** Converts structured research output (from the `deep-research` skill or `research/` sub-skills) into a new agent definition file. Automates the path:

```
research output → extract knowledge → scaffold agent .md → save to agents/
```

**Usage:**
```bash
bash ~/.agent-skills/scripts/pipelines/research-to-agent.sh [research-output.md] [agent-name]
```

---

### `pipelines/version-evolution.sh`

**Purpose:** Tracks version history across skills by comparing SKILL.md frontmatter content across git history. Useful for understanding when skills were created, significantly modified, or effectively deprecated.

**Usage:**
```bash
bash ~/.agent-skills/scripts/pipelines/version-evolution.sh [skill-name]
```

---

## Generated Output Directories

Scripts write to these directories (not in `scripts/` itself):

| Directory | Contents | Generated by |
|---|---|---|
| `../tmp-csv/` | Catalog CSVs (6.9 MB total) | `export_catalog_csv.py`, `summarize_what_they_do.py`, `inspect_md_content.py` |
| `../tmp-md/` | Catalog Markdown (652 KB total) | `summarize_what_they_do.py`, `inspect_md_content.py` |

**Note:** Contents of `tmp-csv/` and `tmp-md/` are generated outputs. Do not hand-edit them — re-run the generating script instead.

---

## Running All Catalogs at Once

```bash
cd ~/.agent-skills
python3 scripts/export_catalog_csv.py && \
python3 scripts/summarize_what_they_do.py && \
python3 scripts/inspect_md_content.py
echo "All catalogs regenerated."
```
