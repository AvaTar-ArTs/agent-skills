# ~/.agent-skills — Creative & Technical AI Ecosystem

**Owner:** Steven Chaplinski  
**Last documented:** August 8, 2026  
**Repository:** git-tracked, multi-platform AI agent/skill ecosystem  

---

## What This Is

`~/.agent-skills/` is a production-grade, multi-platform AI agent and skill ecosystem designed for advanced creative automation, multimedia systems design, and agentic workflow orchestration. It serves as the shared intelligence layer across:

- **Claude Code** (primary)
- **Codex / OpenAI**
- **Cursor**
- **Gemini CLI**
- **Qwen**

This is not a collection of scripts. It is a **stateful creative operating system** — with persistent cross-tool memory, pre-tool context injection hooks, a comprehensive skill library, and a multi-specialist agent directory. Every component is designed to preserve continuity across sessions, platforms, and projects.

---

## Quick Stats

| Dimension | Count |
|---|---|
| Skill directories | ~99 |
| Skill files (total) | 936 |
| Agent definitions | 241 |
| Agent subdirectory packs | 11 |
| Memory exports | 5 |
| Scripts | 7 |
| Pipeline scripts | 3 |
| Archived skill ZIPs | 7 |
| Cross-tool memory DB | 1 (SQLite, 33 KB) |

---

## Directory Map

```
~/.agent-skills/
├── ECOSYSTEM.md              ← This file: authoritative ecosystem overview
├── skills/                   ← 99 skill directories, 936 files
│   ├── .system/              ← System skills: imagegen, openai-docs, plugin-creator
│   ├── [skill-name]/         ← Each skill: SKILL.md + assets/ + references/ + scripts/ + agents/
│   ├── creative/             ← 20 creative sub-skills (comic, infographic, manim, p5js, etc.)
│   ├── deep-learning/        ← 9 ML/DL sub-skills
│   ├── mlops/                ← 6 MLOps sub-skills
│   ├── productivity/         ← 9 productivity sub-skills
│   ├── software-development/ ← 10 dev workflow sub-skills
│   ├── github/               ← 6 GitHub operation sub-skills
│   ├── autonomous-ai-agents/ ← 5 agent-pattern sub-skills
│   ├── research/             ← 5 research sub-skills
│   ├── dormant_archives/     ← 7 archived skill ZIPs (preserved, not active)
│   └── dist/                 ← Distribution artifacts
├── agents/                   ← 241 agent files across 11 subdirectory packs
│   ├── 1-eng-specialist-pack/  ← 11 engineering specialists
│   ├── 2-personal-tooled/    ← Personal tooled agents
│   ├── 3-contains-studio/    ← Studio/creative agents
│   ├── 5-misc-personal/      ← Miscellaneous personal agents
│   ├── commands/             ← Command agents: export, hooks-create, hooks-status
│   ├── deep-learning/        ← ML-specialized agents
│   ├── documentation/        ← Documentation agents
│   ├── gemini-roles/         ← Gemini platform role definitions
│   ├── skill-creator/        ← Skill creation agents with full subsystem
│   ├── skill-installer/      ← Skill installation agents
│   └── skill-porter/         ← Skill conversion/porting agents
├── hooks/                    ← Event-driven automation
│   └── pre-tool-autocontext.sh  ← SQLite memory injection before tool use
├── memory/                   ← Cross-tool persistent memory
│   ├── shared.sqlite         ← SQLite DB (33 KB): decisions, patterns, preferences
│   ├── exports/              ← 5 exports: JSON, MD, CSV (July 2026)
│   └── scripts/              ← Memory utility scripts
├── scripts/                  ← Utility and pipeline scripts
│   ├── chatgpt-exporter-userscript.js  ← ChatGPT history export (903 KB)
│   ├── discover-ecosystem.sh  ← Ecosystem discovery
│   ├── export_catalog_csv.py  ← Skills/agents → CSV catalog
│   ├── innate-context.sh     ← Session context injection
│   ├── inspect_md_content.py  ← Markdown content analysis (14 KB)
│   ├── summarize_what_they_do.py  ← Skill/agent summarization (12 KB)
│   └── pipelines/
│       ├── creative-validation.sh   ← Validate creative skill output
│       ├── research-to-agent.sh     ← Convert research output into agents
│       └── version-evolution.sh     ← Track version evolution across skills
├── deep-research/            ← Multi-agent research harness skill
│   └── SKILL.md
├── docs/                     ← Documentation hub
│   ├── README.md             ← Docs index
│   ├── SKILLS-CATALOG.md     ← Full skill-by-skill reference
│   ├── AGENTS-CATALOG.md     ← Full agent-by-agent reference
│   ├── ARCHITECTURE.md       ← System architecture and patterns
│   ├── DIRECTORIES.md        ← Per-directory deep reference
│   ├── CHANGELOG.md          ← Project changelog
│   ├── EVOLUTION_AND_ITEM_HISTORY.md
│   ├── MY_SUPREMEPOWERS_CONSOLIDATION.md
│   └── imports/              ← Knowledge imports (deep-learning docs)
├── README.md                 ← Original repo README (canonical intro, layout summary)
├── INDEX.md                  ← Runtime index: exact counts, symlink map, operating notes (July 2026)
├── PATH_SCANNING_TEMPLATE.md ← Symbolic [ROOT] path convention for scan outputs
├── .claude/                  ← Claude Code local settings
├── .codex-history/           ← Codex session history
└── .git/                     ← Git repository (tracked since Jul 2026)
```

---

## Runtime Symlinks

The canonical path is `~/.agent-skills/`. Several legacy/platform paths are symlinked here:

| Symlink | Target | Purpose |
|---|---|---|
| `/Users/steven/.agents` | `/Users/steven/.agent-skills` | Compatibility alias for older tools |
| `/Users/steven/.claude/agents` | `/Users/steven/.agent-skills/agents` | Claude Code agent resolution |
| `/Users/steven/.claude/skills` | `/Users/steven/.agent-skills/skills` | Claude Code skill resolution |
| `/Users/steven/.codex/agents` | `/Users/steven/.agent-skills/agents` | Codex agent resolution |
| `/Users/steven/.codex/superpowers` | `/Users/steven/.agent-skills/skills/using-superpowers` | Codex entry-skill shortcut |

> Note: `/Users/steven/.codex/skills` is a managed Codex directory (system skills), NOT a symlink to this tree.

**Rule:** Use `~/.agent-skills` as the canonical path in all new configuration. Keep `~/.agents` only as a compatibility alias for older tools.

---

## Skills: Category Overview

Skills are the primary capability units of this ecosystem. Each skill lives in its own directory with a `SKILL.md` (frontmatter + instructions) and optional `assets/`, `references/`, `scripts/`, and `agents/` subdirectories.

**Discovery rule:** Reusable capabilities must live under a host's discoverable `/skills/` tree and include a trigger-relevant `SKILL.md` description. `~/.agent-skills/skills/` is the cross-tool capability library; `~/.codex/skills/` is Codex's directly discovered library. Agent definitions belong under `/agents/`, and cache or temporary paths are never authoritative skill locations. When a skill is mirrored into both trees, validate full-directory parity—not only `SKILL.md` or `agents/openai.yaml`.

### Agent & System Development
| Skill | Purpose |
|---|---|
| `agent-creation-guidance` | Design and structure autonomous agents, system prompts, triggering conditions, and dev best practices |
| `agent-development` | Create agents for Codex plugins with YAML frontmatter, examples, and tool specs |
| `automation-recommender` | Analyze a codebase and recommend hooks, subagents, skills, MCP servers |
| `brainstorm` | Explore requirements and design patterns before any implementation begins |
| `brainstorming` | Mandatory design gateway — no code until design is presented and approved |
| `command-development` | Create slash commands with YAML frontmatter, arguments, and file references |
| `dispatching-parallel-agents` | Orchestrate 2+ independent parallel tasks without shared-state conflicts |
| `skill-creator` | Create, iterate, and eval-test new skills with a TDD approach |
| `skill-development` | Develop skills for Codex plugins with progressive disclosure patterns |
| `skill-installer` | Install curated skills from the openai/skills registry |

### MCP & Plugin Architecture
| Skill | Purpose |
|---|---|
| `build-mcp-app` | Build MCP servers with interactive UI widgets (forms, pickers, dashboards, confirmations) |
| `build-mcp-server` | Design and build MCP servers end-to-end: discovery → recommendation → implementation |
| `build-mcpb` | Package MCP servers as self-contained bundles (.mcpb) with bundled runtime |
| `mcp-app-development-principles` | Architectural principles for MCP apps with interactive UI widgets |
| `mcp-integration` | Integrate MCP servers into plugins: config, auth, security, lifecycle |
| `mcp/native-mcp` | Native MCP protocol patterns |
| `plugin-settings` | Use `.local.md` files for per-project plugin configuration |
| `plugin-structure` | Codex plugin directory layout, manifest-driven config, auto-discovery |
| `hook-development` | Create PreToolUse, PostToolUse, Stop hooks for event-driven automation |

### Code Quality & Review
| Skill | Purpose |
|---|---|
| `code-review` | Review diffs for bugs, efficiency, and simplification opportunities |
| `receiving-code-review` | Process and apply code review feedback with technical rigor |
| `verification-before-completion` | Run fresh verification commands before claiming any task complete |
| `devtu-fix-tool` | Fix failing ToolUniverse tools via systematic diagnosis and validation |
| `devtu-optimize-descriptions` | Optimize ToolUniverse tool descriptions for clarity, completeness, and usability |
| `devtu-optimize-skills` | Improve ToolUniverse skills for better report quality, evidence handling, UX |
| `frontend-ux-modernizer` | Modernize ESO project frontend with traceability and service-ticket logging |
| `git-ai-assistant` | Git AI integration, attribution tracking, checkpoint creation |
| `git-ai-cursor-integration` | Integrate Git AI tracking with Cursor workflows and automatic checkpoints |

### Implementation & Planning
| Skill | Purpose |
|---|---|
| `executing-plans` | Execute written implementation plans with batch checkpoints and review gates |
| `finishing-a-development-branch` | Complete development: test → options → integrate → clean |
| `workflow-bootstrap` | Mandatory workflow definitions for creative work and multi-step implementation |
| `using-git-worktrees` | Create isolated git worktrees with safety verification before destructive ops |
| `innate-workflow` | Session-level rhythm: audit workspace → select skills → execute → update memory |
| `using-superpowers` | Entry skill for any implementation, debugging, or building work |

### Frontend & Design
| Skill | Purpose |
|---|---|
| `design-taste-frontend` | Anti-generic landing pages, portfolios, and redesigns using brief inference |
| `frontend-design` | Create production-grade distinctive interfaces avoiding AI aesthetic defaults |
| `taste-skill` | Sub-skills: brutalist, minimalist, output, redesign — experimental design modes |
| `dogfood` | Exploratory QA of web apps: find bugs, produce evidence, generate reports |

### Documentation & Narrative
| Skill | Purpose |
|---|---|
| `narrative-blueprints` | Persuasive narratives that explain concept + monetization + workflow for non-technical audiences |
| `narrative-documentation` | Descriptive narratives for non-technical audiences explaining purpose and value |
| `claude-md-improver` | Audit and improve AGENTS.md files in repositories against quality templates |

### Ecosystem & Memory
| Skill | Purpose |
|---|---|
| `ecosystem-clarity` | Single reference for how Cursor/Codex/Qwen/Gemini capabilities fit together |
| `ecosystem-intelligence` | Audit, analyze, and evolve the multi-tool AI ecosystem |
| `ecosystem-navigation` | Understand and navigate Qwen capabilities and features |
| `managing-ecosystem-cleanup` | Audit AI tool ecosystems for duplicate plugins, backup skills, context bloat |
| `workspace-ecosystem-audit` | Deep inventory of local AI/agent ecosystem configs, code, dependencies, risks |
| `cross-tool-memory` | Cross-tool memory bridge via `~/.agent-skills/memory/shared.sqlite` |
| `self-evolving-memory` | Persistent memory that learns and improves from usage patterns |
| `self-improvement` | Continuous self-improvement cycles for Qwen capability enhancement |

### Research & Knowledge
| Skill | Purpose |
|---|---|
| `deep-research` | Multi-agent research harness: fan-out searches, fetch, adversarially verify, synthesize |
| `find-docs` | Retrieve up-to-date docs, API refs, and examples for any developer technology via Context7 |
| `research` | Category: arxiv, blogwatcher, polymarket, llm-wiki, research-paper-writing |
| `tooluniverse` | General strategies for 10,000+ scientific tools |
| `tooluniverse-clinical-trial-design` | Clinical trial research via ToolUniverse |
| `tooluniverse-sequence-retrieval` | Sequence retrieval via ToolUniverse |
| `setup-tooluniverse` | Install and configure ToolUniverse with MCP for any AI client |

### Communication & Access Control
| Skill | Purpose |
|---|---|
| `imessage-access` | Manage iMessage channel access: approve pairings, edit allowlists, set DM policy |
| `imessage-configure` | Check iMessage setup and review channel access policy |
| `discord-access` | Manage Discord channel access and approval workflows |
| `discord-configure` | Configure Discord bot token and review policy |
| `telegram-access` | Manage Telegram channel access |
| `telegram-configure` | Configure Telegram channel |

### Apple & macOS Integration
| Skill | Purpose |
|---|---|
| `apple` | Apple ecosystem: Reminders, FindMy, Notes, iMessage, Computer Use |
| `cua-driver` | Drive native macOS apps via AX tree snapshots: click, type, scroll by element_index |
| `eza-nav` | Enhanced filesystem navigation and directory listing using eza |

### Session & Export
| Skill | Purpose |
|---|---|
| `session-export` | Create durable session exports for agent continuation across context windows |
| `session-report` | Generate structured session reports |
| `chat-history-export` | Export, search, and inspect local AI conversation history from session JSON |
| `agmsg` | Cross-agent messaging via SQLite — send messages between Claude Code, Codex, Gemini, Qwen |

### Specialized Tools
| Skill | Purpose |
|---|---|
| `sora` | Sora video generation and remix via OpenAI API |
| `notebooklm` | NotebookLM integration |
| `math-olympiad-solver` | Solve competition math (IMO, Putnam, USAMO, AIME) with adversarial verification |
| `capability-atlas` | Map and translate capabilities across hosts (Gemini, Qwen, Codex, Cursor) |
| `cursor-integration` | Coordinate between Qwen, Cursor, Codex and other AI tools |
| `hermes-integration` | Manage Hermes Agent as an isolated containerized service |
| `ice-tracker-integration` | ICE Tracker project development with Git AI assistance |
| `mythic-atlas` | Generate personalized Soul Blueprint delivery bundles — symbolic poster brief, clean copy, philosophical manuscript, animation prompt, metadata, and ZIP — from customer YAML intake; style-aware across 5 presets; Chaplinski family series in active production | `references/` · `scripts/` |

### Creative Skill Sub-Library (`skills/creative/`)
20 sub-skills for visual and multimedia creation:
`architecture-diagram` · `ascii-art` · `ascii-video` · `baoyu-comic` · `baoyu-infographic` · `claude-design` · `comfyui` · `creative-ideation` · `design-md` · `excalidraw` · `humanizer` · `manim-video` · `p5js` · `pixel-art` · `popular-web-designs` · `pretext` · `sketch` · `songwriting-and-ai-music` · `structured-asset-pipeline` · `touchdesigner-mcp`

### Deep Learning Sub-Library (`skills/deep-learning/`)
9 ML/DL sub-skills:
`dataset-preparation` · `experiment-tracking` · `hyperparameter-optimization` · `model-deployment` · `model-evaluation` · `model-training-workflow` · `pytorch-debugging` · `tensorflow-debugging` · `transfer-learning-design`

### MLOps Sub-Library (`skills/mlops/`)
Sub-skills: `evaluation/lm-evaluation-harness` · `evaluation/weights-and-biases` · `huggingface-hub` · `inference/llama-cpp` · `inference/obliteratus` · `inference/vllm` · `models/audiocraft` · `models/segment-anything` · `research/dspy` · `training/vector-databases`

### Productivity Sub-Library (`skills/productivity/`)
`airtable` · `google-workspace` · `linear` · `maps` · `notion` · `ocr-and-documents` · `powerpoint` · `teams-meeting-pipeline` · `nano-pdf`

### Software Development Sub-Library (`skills/software-development/`)
`debugging-hermes-tui-commands` · `hermes-agent-skill-authoring` · `node-inspect-debugger` · `plan` · `python-debugpy` · `requesting-code-review` · `spike` · `subagent-driven-development` · `systematic-debugging` · `test-driven-development` · `writing-plans`

### GitHub Sub-Library (`skills/github/`)
`codebase-inspection` · `github-auth` · `github-code-review` · `github-issues` · `github-pr-workflow` · `github-repo-management`

### Dormant Archives (`skills/dormant_archives/`)
7 preserved ZIP archives of retired or staged skills:
`communications.zip` · `exploration.zip` · `integrations.zip` · `math.zip` · `media_art.zip` · `niche_automation.zip` + 1 additional

---

## Agents: Category Overview

241 agent definition files across 11 packs and 100 root-level agents.

### Root-Level Agents (100 .md files, key selections)

**Creative & Content**
`ai-music-video-creator` · `ai-xeo` · `brand-guardian` · `bots` · `content-creator` · `content-organizer` · `visual-storyteller` · `whimsy-injector` · `instagram-curator` · `twitter-engager` · `tiktok-strategist` · `reddit-community-builder`

**Engineering & Architecture**
`api-specialist` · `backend-architect` · `database-specialist` · `devops-automator` · `devops-engineer` · `frontend-architect` · `frontend-developer` · `javascript-expert` · `mobile-app-builder` · `performance-benchmarker` · `performance-engineer` · `python-expert` · `security-engineer` · `system-architect` · `system-analyzer` · `technical-writer` · `testing-specialist`

**AI & Ecosystem**
`ai-engineer` · `ai-workflow-manager` · `agent-creation-guidance` · `capability-atlas` · `conversation-analyzer` · `ecosystem-analyzer` · `ecosystem-dev` · `ecosystem-learning` · `ecosystem-synergy` · `integrated-evolution` · `innate-memory-agent` · `self-evolution`

**Product & Business**
`analytics-reporter` · `app-store-optimizer` · `experiment-tracker` · `feedback-synthesizer` · `finance-tracker` · `growth-hacker` · `knowledge-automation-strategist` · `legal-compliance-checker` · `project-launch-manager` · `project-shipper` · `rapid-prototyper` · `revenue-optimizer` · `sprint-prioritizer` · `xeo-strategist`

**Research & Knowledge**
`knowledge-fetcher` · `seo-keyword-analyst` · `trend-researcher` · `tool-evaluator` · `notebooklm-enhancement-advisor`

**Operations & Support**
`context-fetcher` · `context-handoff-compiler` · `date-checker` · `documentation-manager` · `file-creator` · `filesystem-inventory` · `git-workflow` · `infrastructure-maintainer` · `path-list-analyzer` · `support-responder` · `task-management` · `tree-explorer` · `workflow-optimizer` · `workflow-orchestrator`

**Steven-Specific**
`avatararts-organizer` · `iterm2-ecosystem-dev` · `ice-tracker-assistant` · `sorty`

**Studio / Coordination**
`studio-coach` · `studio-producer`

### Agent Packs

| Pack | Contents |
|---|---|
| `1-eng-specialist-pack/` | 11 engineers: api, database, devops, frontend, javascript, performance, python, security, system-architect, technical-writer, testing |
| `2-personal-tooled/` | Tooled variants of personal agents |
| `3-contains-studio/` | Studio and creative coordination agents |
| `5-misc-personal/` | Miscellaneous personal agents |
| `commands/` | Command agents: `export`, `hooks-create`, `hooks-status` |
| `deep-learning/` | ML research and implementation agents |
| `documentation/` | Technical writing and documentation agents |
| `gemini-roles/` | Role definitions for Gemini CLI platform |
| `skill-creator/` | Full skill creation subsystem (agents + assets + references + scripts) |
| `skill-installer/` | Skill installation agents and scripts |
| `skill-porter/` | Skill conversion tools with before/after examples |

---

## Memory System

The cross-tool memory layer provides persistent context that survives across sessions and AI platforms.

**Primary store:** `~/.agent-skills/memory/shared.sqlite` (33 KB)  
**Schema:** `decisions` table with `topic` and `outcome` columns  
**Hook integration:** `hooks/pre-tool-autocontext.sh` queries this DB before every tool use, injecting relevant prior decisions as automatic context  

**Memory exports (July 2026):**
- `decisions-2026-07-13.json` / `.md` — structured decision log
- `preferences-2026-07-13.csv` — user preferences snapshot
- `conversation-export.md` — conversation-level export
- `full-session-export.json` — complete session state

**Cross-tool reach:** All AI clients (Claude Code, Codex, Gemini CLI, Qwen) can read/write to the same SQLite database via the `cross-tool-memory` skill and `agmsg` skill.

---

## Hooks System

Single active hook at `hooks/pre-tool-autocontext.sh`:

```bash
# Pre-tool hook: auto-loads relevant memory context before tool use
# Extracts keywords from tool args, queries shared.sqlite, injects top 3 matching decisions
sqlite3 ~/.agent-skills/memory/shared.sqlite \
  "SELECT topic, outcome FROM decisions WHERE topic LIKE '%$keywords%' LIMIT 3;"
```

This makes memory **innate** — always available without explicit recall commands. Every tool invocation automatically surfaces relevant prior decisions.

---

## Architecture Patterns

**Skill structure (standard):**
```
skill-name/
├── SKILL.md          ← Frontmatter + instructions (always present)
├── assets/           ← Images, icons (optional)
├── references/       ← Supporting documentation (optional)
├── scripts/          ← Executable scripts (optional)
└── agents/           ← Agent definitions for this skill (optional)
```

**Multi-platform design:**  
Skills use Codex tool names internally. Each platform has a translation reference (`references/codex-tools.md`, `references/gemini-tools.md`, `references/copilot-tools.md`).

**Skill invocation flow:**  
`using-superpowers` → check for applicable skills → invoke before any response or action

**Memory flow:**  
pre-tool hook → SQLite query → injected context → tool use → cross-tool-memory skill → append new decisions

**Creative pipeline:**  
`brainstorming` → `writing-plans` → `executing-plans` → `verification-before-completion` → `finishing-a-development-branch`

---

## Navigation

| I want to... | Go to |
|---|---|
| Find a specific skill | [docs/SKILLS-CATALOG.md](docs/SKILLS-CATALOG.md) |
| Find a specific agent | [docs/AGENTS-CATALOG.md](docs/AGENTS-CATALOG.md) |
| Understand the architecture | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Deep-dive a specific directory | [docs/DIRECTORIES.md](docs/DIRECTORIES.md) |
| Work with skills | [skills/README.md](skills/README.md) |
| Work with agents | [agents/README.md](agents/README.md) |
| Understand memory | [memory/README.md](memory/README.md) |
| Run or add scripts | [scripts/README.md](scripts/README.md) |
| Understand hooks | [hooks/README.md](hooks/README.md) |
