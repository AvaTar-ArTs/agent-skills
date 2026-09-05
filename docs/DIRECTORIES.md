# Directory Reference — Deep Reference

**~/.agent-skills/**  
**Documented:** August 8, 2026  

Per-directory deep reference. For the architecture that connects these directories, see `ARCHITECTURE.md`. For skill and agent inventories, see `SKILLS-CATALOG.md` and `AGENTS-CATALOG.md`.

---

## `skills/` — Skill Library Root

**Purpose:** The primary capability library. Each subdirectory is one skill — a self-contained unit of AI capability with instructions, references, and optional tooling.

**File count:** 936 files across ~99 subdirectories  
**README:** [skills/README.md](../skills/README.md)

**Discovery and triggering rule:** A reusable capability is not considered installed merely because its files exist somewhere. It must be placed under the relevant host's `/skills/` tree, have valid `SKILL.md` frontmatter, and use a description that states both capability and trigger context. Keep agents under `/agents/`; do not use `/tmp`, cache directories, exports, or documentation folders as runtime skill sources.

### Contents

```
skills/
├── .system/               ← Platform-managed system skills (5 skills)
├── [99 skill directories] ← User-installed and platform skills
├── checkpoint.skill       ← Ecosystem checkpoint marker
├── VERSIONING_NOTES.md    ← Skill versioning conventions
├── docs-06-21-12:37.csv   ← Catalog snapshot, June 21
├── docs.txt               ← Text index of skill documentation
└── enriched-skills.csv    ← Enriched skills catalog with descriptions
```

### Subdirectory Categories

| Category | Count | Examples |
|---|---|---|
| Agent & system dev | 10 | `brainstorming`, `skill-creator`, `agent-development` |
| MCP & plugin | 8 | `build-mcp-server`, `build-mcp-app`, `hook-development` |
| Code quality | 9 | `code-review`, `verification-before-completion`, `git-ai-assistant` |
| Implementation | 6 | `executing-plans`, `innate-workflow`, `using-superpowers` |
| Frontend & design | 4 | `frontend-design`, `taste-skill`, `dogfood` |
| Ecosystem & memory | 9 | `cross-tool-memory`, `agmsg`, `ecosystem-intelligence` |
| Research | 7 | `deep-research`, `find-docs`, `tooluniverse` |
| Communication | 6 | `imessage-access`, `discord-configure`, `telegram-access` |
| Apple & macOS | 3 | `apple`, `cua-driver`, `eza-nav` |
| Session & export | 3 | `session-export`, `chat-history-export`, `session-report` |
| Specialized tools | 7 | `sora`, `math-olympiad-solver`, `hermes-integration` |
| Creative (sub-library) | 20 | `songwriting-and-ai-music`, `comfyui`, `baoyu-comic` |
| Deep learning (sub-library) | 9 | `model-training-workflow`, `pytorch-debugging` |
| MLOps (sub-library) | 10 | `inference/vllm`, `models/audiocraft`, `research/dspy` |
| Productivity (sub-library) | 9 | `notion`, `airtable`, `google-workspace` |
| Software dev (sub-library) | 11 | `test-driven-development`, `systematic-debugging` |
| GitHub (sub-library) | 6 | `github-pr-workflow`, `github-issues` |
| Other | 8 | `gaming`, `red-teaming`, `smart-home`, `social-media`, `email`, `devops`, `data-science`, `mcp` |

### System Skills (`.system/`)

Platform-managed and potentially replaced by host updates. Local changes require explicit user authorization, regression validation, and synchronization with any intentional cross-tool mirror.

| Skill | Notable Files |
|---|---|
| `imagegen` | `scripts/image_gen.py`, `scripts/remove_chroma_key.py`, `references/image-api.md` |
| `openai-docs` | `scripts/resolve-latest-model-info.js`, `references/upgrade-guide.md` |
| `plugin-creator` | Full plugin scaffolding system |
| `skill-creator` | Platform-level skill creation system |
| `skill-installer` | Platform-level skill installer |

### Dormant Archives (`dormant_archives/`)

7 ZIP files of archived skills. Preserved but not active:
- `communications.zip` — retired communication skills
- `exploration.zip` — retired exploration/discovery skills
- `integrations.zip` — retired third-party integration skills
- `math.zip` — retired mathematics skills
- `media_art.zip` — retired media and art skills
- `niche_automation.zip` — retired niche automation skills
- *(1 additional unlabeled)*

**To restore a skill:** unzip into `skills/`, verify SKILL.md frontmatter, test invocation.

---

## `agents/` — Agent Library Root

**Purpose:** Agent definition files. Each `.md` file defines a specialist agent with a system prompt, tool list, and triggering description.

**File count:** 241 files across 11 subdirectory packs + ~100 root-level agents  
**README:** [agents/README.md](../agents/README.md)

### Root-Level Files

~100 agent `.md` files (alphabetically organized) plus:

| File | Type | Purpose |
|---|---|---|
| `AGENT_PATTERN_GUIDE.md` | Reference | Guide for agent patterns within pack structure |
| `cleanup-manifest.csv` | Catalog | Agent cleanup operations manifest |
| `docs-06-21-12:39.csv` | Catalog | Agent snapshot from June 21 |
| `docs.txt` | Index | Agent documentation text index |
| `enriched-agents.csv` | Catalog | Enriched agent catalog with AI-generated descriptions |
| `MANIFEST.csv` | Master catalog | Master agent manifest |
| `openai.yaml` | Config | OpenAI agent configuration |

### Subdirectory Packs

| Pack | Files | Purpose |
|---|---|---|
| `1-eng-specialist-pack/` | 11 | Curated engineering specialists |
| `2-personal-tooled/` | varies | Personal agents with tool specialization |
| `3-contains-studio/` | varies | Studio and creative coordination agents |
| `5-misc-personal/` | varies | Miscellaneous personal agents |
| `commands/` | 3 | Slash-command-style agents: export, hooks-create, hooks-status |
| `deep-learning/` | varies | ML/DL specialist agents |
| `documentation/` | varies | Documentation specialist agents |
| `gemini-roles/` | varies | Gemini CLI role definitions |
| `skill-creator/` | full subsystem | Skill creation with agents + assets + references + scripts |
| `skill-installer/` | full subsystem | Skill installation with agents + scripts |
| `skill-porter/` | conversion tools | Skill format conversion with before/after examples |

---

## `hooks/` — Event-Driven Automation

**Purpose:** Shell scripts that execute automatically in response to tool invocation events, injecting context without explicit user commands.

**README:** [hooks/README.md](../hooks/README.md)

### Files

| File | Size | Purpose |
|---|---|---|
| `pre-tool-autocontext.sh` | 413 bytes | Queries `shared.sqlite` before every tool use, injects top 3 matching prior decisions |

### Hook Behavior (pre-tool-autocontext.sh)

```bash
#!/bin/bash
TOOL_NAME="$1"
shift
ARGS="$*"
keywords=$(echo "$ARGS" | tr ' ' '\n' | head -3 | tr '\n' ',')
sqlite3 ~/.agent-skills/memory/shared.sqlite \
  "SELECT topic, outcome FROM decisions WHERE topic LIKE '%$keywords%' LIMIT 3;" 2>/dev/null
```

**Trigger:** Runs before every tool invocation  
**Effect:** Extracts keywords from tool arguments, queries the shared memory database, returns up to 3 relevant prior decisions as injected context  
**Dependency:** Requires `sqlite3` in PATH and `~/.agent-skills/memory/shared.sqlite` to exist

---

## `memory/` — Cross-Tool Persistent Memory

**Purpose:** Shared memory layer accessible by all AI clients (Claude Code, Codex, Gemini CLI, Qwen). Enables decisions made in one tool to inform future sessions in any tool.

**README:** [memory/README.md](../memory/README.md)

### Files

| File | Size | Purpose |
|---|---|---|
| `shared.sqlite` | 33 KB | Primary memory store: `decisions(topic, outcome)` table |
| `exports/` | dir | 5 point-in-time exports from July 2026 |
| `scripts/` | symlink | Utility scripts (note: `scripts/scripts` is a circular symlink — benign) |

### Exports

| Export File | Size | Contents |
|---|---|---|
| `conversation-export.md` | 859 bytes | Markdown conversation-level export |
| `decisions-2026-07-13.json` | 3.3 KB | Structured decision log in JSON |
| `decisions-2026-07-13.md` | 2.9 KB | Structured decision log in Markdown |
| `full-session-export.json` | 802 bytes | Complete session state export |
| `preferences-2026-07-13.csv` | 110 bytes | User preferences snapshot |

### SQLite Schema

```sql
-- Primary table (inferred from hook query pattern)
CREATE TABLE decisions (
  topic   TEXT,   -- What the decision is about (keyword-searchable)
  outcome TEXT    -- The decision made and its reasoning
);
```

### Cross-Tool Access

| Tool | Access Method |
|---|---|
| Claude Code | `cross-tool-memory` skill or `agmsg` skill |
| Codex | `cross-tool-memory` skill or `agmsg` skill |
| Gemini CLI | `cross-tool-memory` skill (via Gemini tool translation) |
| Qwen | `cross-tool-memory` skill |
| Direct | `sqlite3 ~/.agent-skills/memory/shared.sqlite` |

---

## `scripts/` — Utility & Pipeline Scripts

**Purpose:** Standalone scripts for ecosystem analysis, catalog generation, session export, and automated pipelines.

**README:** [scripts/README.md](../scripts/README.md)

### Root Scripts

| File | Size | Purpose |
|---|---|---|
| `chatgpt-exporter-userscript.js` | 903 KB | Browser userscript for exporting ChatGPT conversation history |
| `discover-ecosystem.sh` | 582 bytes | Scans and summarizes the local AI ecosystem structure |
| `export_catalog_csv.py` | 9.9 KB | Exports all skills/agents metadata to CSV catalogs |
| `innate-context.sh` | 582 bytes | Injects session context at conversation start |
| `inspect_md_content.py` | 14 KB | Analyzes and indexes all Markdown content in the ecosystem |
| `summarize_what_they_do.py` | 12 KB | Generates natural-language summaries of all skills and agents |

### Pipeline Scripts (`scripts/pipelines/`)

| File | Purpose |
|---|---|
| `creative-validation.sh` | Validates creative skill output: checks for expected artifacts, format compliance, quality markers |
| `research-to-agent.sh` | Converts structured research output from `deep-research` skill into new agent definitions |
| `version-evolution.sh` | Tracks version history across skills by comparing git history of SKILL.md files |

### Generated Outputs (in `tmp-csv/` and `tmp-md/`)

Running the catalog scripts produces:

| Output | Size | Source Script |
|---|---|---|
| `tmp-csv/agents-catalog.csv` | 170 KB | `export_catalog_csv.py` |
| `tmp-csv/md-content-index.csv` | 6.4 MB | `inspect_md_content.py` |
| `tmp-csv/what-they-do.csv` | 477 KB | `summarize_what_they_do.py` |
| `tmp-md/what-they-do.md` | 272 KB | `summarize_what_they_do.py` |
| `tmp-md/md-content-report.md` | 380 KB | `inspect_md_content.py` |

---

## `deep-research/` — Research Harness Skill

**Purpose:** A standalone skill directory at the top level for the multi-agent deep research harness. Unusual placement (most skills are inside `skills/`) — may be a promoted/featured skill.

**README:** [deep-research/README.md](../deep-research/README.md)

### Files

| File | Size | Purpose |
|---|---|---|
| `SKILL.md` | 2.2 KB | Multi-agent research harness instructions |

### Capability (from SKILL.md)

Invokes a deep research loop:
1. Fan-out parallel web searches
2. Fetch and read primary sources
3. Adversarially verify claims
4. Synthesize a cited, structured report

**Modes:** `notes` · `report` · `comparison` · `learning_path`  
**Depth levels:** `quick` · `standard` · `deep`

---

## `docs/` — Documentation Hub

**Purpose:** Central documentation for the entire ecosystem. Contains the four major reference documents, historical files, and the imports subdirectory.

**README:** [docs/README.md](docs/README.md)

### Files

| File | Size | Purpose |
|---|---|---|
| `README.md` | — | Docs directory index |
| `SKILLS-CATALOG.md` | — | Complete skill-by-skill reference |
| `AGENTS-CATALOG.md` | — | Complete agent-by-agent reference |
| `ARCHITECTURE.md` | — | System architecture and patterns |
| `DIRECTORIES.md` | — | This file — per-directory deep reference |
| `CHANGELOG.md` | 556 bytes | Project changelog (pre-documentation) |
| `EVOLUTION_AND_ITEM_HISTORY.md` | 603 bytes | Evolution and item history tracking |
| `MY_SUPREMEPOWERS_CONSOLIDATION.md` | 1.1 KB | Supremepowers consolidation notes |
| `imports/` | dir | Knowledge imports |

### `docs/imports/`

| Path | Purpose |
|---|---|
| `imports/deep-learning/agents-inventory.md` | Inventory of deep-learning agents |
| `imports/deep-learning/CLAUDE.md` | Claude configuration for deep-learning context |

---

## `tmp-csv/` — Generated CSV Catalogs

**Purpose:** Output directory for catalog generation scripts. Contents are generated and should not be hand-edited.

| File | Size | Generated By |
|---|---|---|
| `agents-catalog.csv` | 170 KB | `scripts/export_catalog_csv.py` |
| `md-content-index.csv` | 6.4 MB | `scripts/inspect_md_content.py` |
| `what-they-do.csv` | 477 KB | `scripts/summarize_what_they_do.py` |
| `agents-catalog-CHANGELOG.txt` | varies | Auto-generated changelog |
| `what-they-do-CHANGELOG.txt` | varies | Auto-generated changelog |
| *(1 additional)* | — | — |

**Regenerating catalogs:**
```bash
cd ~/.agent-skills
python3 scripts/export_catalog_csv.py
python3 scripts/summarize_what_they_do.py
python3 scripts/inspect_md_content.py
```

---

## `tmp-md/` — Generated Markdown Reports

**Purpose:** Output directory for Markdown report generation. Contents are generated.

| File | Size | Generated By |
|---|---|---|
| `md-content-report.md` | 380 KB | `scripts/inspect_md_content.py` |
| `what-they-do.md` | 272 KB | `scripts/summarize_what_they_do.py` |

---

## Root-Level Documents (Pre-existing)

Three files existed at the root before the August 2026 documentation pass:

| File | Size | Purpose |
|---|---|---|
| `README.md` | ~800 bytes | Original repo README: canonical intro, layout summary, working principles ("prefer additive changes, staged outputs, changelogs over destructive cleanup") |
| `INDEX.md` | ~1.5 KB | Runtime index: exact July 2026 counts (108 agent root files, 221 total agent files, 97 skill dirs, 186 expanded skills), symlink map for Claude/Codex resolution |
| `PATH_SCANNING_TEMPLATE.md` | ~600 bytes | Symbolic `[ROOT]` path convention — defines `[ROOT]` and `[ROOT]/tmp` for scan output staging within any target directory |

**Runtime symlinks documented in `INDEX.md`:**

| Symlink | Target |
|---|---|
| `/Users/steven/.agents` | `/Users/steven/.agent-skills` (compatibility) |
| `/Users/steven/.claude/agents` | `/Users/steven/.agent-skills/agents` |
| `/Users/steven/.claude/skills` | `/Users/steven/.agent-skills/skills` |
| `/Users/steven/.codex/agents` | `/Users/steven/.agent-skills/agents` |
| `/Users/steven/.codex/superpowers` | `/Users/steven/.agent-skills/skills/using-superpowers` |

---

## `.claude/` — Claude Code Configuration

**Purpose:** Claude Code local settings for this directory.

| File | Purpose |
|---|---|
| `settings.local.json` | Local Claude Code settings overrides (56 bytes) |

---

## `.codex-history/` — Codex Session History

**Purpose:** Directory for Codex session history tracking. Currently contains only `.DS_Store` — either Codex history is stored elsewhere or this directory is a placeholder.

**Status:** Appears empty / metadata only.

---

## `.git/` — Git Repository

**Purpose:** Full git repository tracking all ecosystem changes since July 2026.

The entire `~/.agent-skills/` directory is version-controlled. This enables:
- `scripts/pipelines/version-evolution.sh` to compare SKILL.md across history
- Rollback of any skill or agent definition
- Audit trail for ecosystem decisions
- Diff-based review of skill changes

**Tracked since:** July 13, 2026 (based on export timestamps)  
**Objects:** 4 object directories with significant history
