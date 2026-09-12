# Local agent ecosystem deep-dive audit — 2026-09-12

Read-only audit of `~/.agents`, `~/.agent-skills`, and `~/.hermes`. Secret values, tokens, session contents, and database contents were not read or copied. Runtime-heavy directories were counted structurally but excluded from semantic file sampling.

## Executive finding

`~/.agent-skills` is the canonical authored capability library. `~/.agents/skills` currently points to its `skills/` directory, so the live `~/.agents` path is a compatibility projection. The remaining `~/.agents/skills.bak-2026-09-11-1402-copy` is a historical fork and must not be merged or deleted blindly.

`~/.hermes` is a separate full runtime/control plane: 3.0 GB on disk, local model/provider routing, 26 built-in CLI toolsets, delegation, memory, sessions, skills, and MCP integrations. It is not merely another skill mirror.

## Current topology

| Surface | Verified state | Role |
|---|---|---|
| `~/.agent-skills` | real Git repository, ~380 MB | canonical authored skills, agents, catalogs, memory, audit docs |
| `~/.agents/skills` | symlink → `~/.agent-skills/skills` | compatibility / npx skills projection |
| `~/.agents/skills.bak-*` | real historical copy | migration evidence; not live authority |
| `~/.hermes` | real runtime, ~3.0 GB | Hermes executable, sessions, state, skills, MCP, caches, models |
| `~/.hermes/skills` | mixed symlinked and local skills | Hermes skill surface; some canonical, some Hermes-specific |

## Capability counts

- Canonical direct skill contracts: **254**; all nested `SKILL.md` files: **521**.
- Historical `.agents` backup direct skill contracts: **227**.
- Direct backup/canonical intersection: **226**; identical: **202**; content-different: **24**.
- Canonical agent definition files (`.md`, `.toml`, YAML-like): **315**.
- Hermes direct skill contracts: **69**; all recursive `SKILL.md` files: **159**.
- Hermes skill symlinks discovered: **59**; broken: **1**.

The count difference between direct authority and recursive `SKILL.md` counts is caused by nested skill packs, references, archives, tests, and vendored/project trees. Use direct top-level contracts for active capability counts; use recursive counts for physical footprint only.

## Hermes tools and orchestration

Configured built-in/toolset capabilities include:

```text
bfl, browser, clarify, code_execution, computer_use, context_engine, cronjob,
delegation, discord, discord_admin, file, homeassistant, image_gen, kanban,
memory, session_search, skills, spotify, stt, terminal, todo, tts, video,
video_gen, vision, web, x_search, yuanbao
```

Current MCP configuration includes:

| Server | State | Function |
|---|---|---|
| `ideogram` | disabled | remote Ideogram MCP endpoint |
| `chrome-devtools` | enabled | browser/devtools MCP via npx |
| `suno-cdp` | enabled | local Node Suno browser/CDP bridge |
| `suno-recon` | enabled | local Suno reconstruction MCP with browser/session tools |

Hermes delegation is configured with:

- Maximum spawn depth: `1`
- Maximum concurrent children: `10`
- Automatic child approval: disabled
- MCP toolset inheritance: enabled
- Maximum iterations: `250`
- Gateway timeout: `1800s`

This is bounded but not low-risk: child depth and automatic approval are constrained, while MCP inheritance and a high iteration budget still expand the blast radius.

## Runtime and state footprint

| Area | Observation | Risk |
|---|---|---|
| Hermes `state.db` | ~319 MB plus WAL | persistent runtime state; do not treat as source |
| Hermes sessions | 153 files | private conversations and task evidence |
| Hermes terminal sessions | 14 files | command/runtime evidence |
| Hermes caches | 158 files | derived/cache data |
| Hermes logs | 23 files | potentially sensitive diagnostics |
| Hermes auth/env links | present | credential boundary; values intentionally not inspected |
| Hermes Chrome bundle | large | runtime dependency, not agent capability |
| `.agent-skills` Git packfiles | large | repository history/storage, not active tools |

## Strengths

1. **Clear canonical library exists.** `~/.agent-skills` has catalogs, agents, skills, memory, hooks, scripts, and audit documentation.
2. **Compatibility topology is improving.** `~/.agents/skills` now resolves to canonical instead of remaining a second live copy.
3. **Hermes is a real orchestration runtime.** It provides delegation, toolsets, memory, browser, terminal, media, MCP, and session persistence.
4. **Capability breadth is high.** The ecosystem covers software development, research, media, creative production, productization, agents, MCP, and workstation operations.
5. **Audit history exists.** Previous audits document topology and drift instead of silently changing it.

## Findings requiring attention

### 1. Historical fork remains ambiguous

The backup skill tree has 24 content-different names in the current comparison, plus 1 backup-only name (`video-marketing`). Most differences are host/provider terminology migrations; `create-skill` and `workflow-bootstrap` also contain substantive packaging/workflow changes. It should be treated as migration evidence, not an active authority. See `skill-drift-ledger.json` for hashes, counts, and per-skill disposition.

### 2. Canonical authority must be verified

`~/.agent-skills` is the canonical candidate, not automatically proven authority: it is a dirty Git worktree with untracked and generated material. Treat `~/.agent-skills/skills/` as the strongest current authority candidate until host loader behavior and provenance are verified. `~/.codex/skills/` remains a separate populated host tree.

### 3. Active counts are currently ambiguous

The ecosystem reports several incompatible counts: direct active contracts, recursive contracts, catalog entries, Hermes projections, and backup copies. Future reports should always label the counting scope.

### 4. Hermes has high operational power

Enabled Suno MCP tools include browser authentication/session and cookie save/load operations. Keep these behind explicit approval and never include raw MCP/session artifacts in portable skill sources.

### 5. Runtime storage is mixed with authored capability

Hermes combines skills with a large state database, model caches, browser binaries, sessions, logs, and archives. Use `~/.hermes/skills/` for skill discovery only; do not inventory the whole runtime as if it were a source library.

### 6. Documentation drift persists

Some older ecosystem documents describe previous symlink topology or historical counts. Prefer the current filesystem, current symlink targets, and dated audit artifacts over stale summaries.

## Recommended agent workflow

### Canonical audit route

1. `workspace-ecosystem-audit` — structural and metadata inventory.
2. `ecosystem-intelligence` — topology, drift, and evolution analysis.
3. `capability-atlas` — canonical capability versus host rendering matrix.
4. `automation-recommender` — identify the smallest useful hooks/subagents/MCP additions.
5. `verification-before-completion` — verify links, manifests, and tool availability.

### Best specialist lanes

| Agent | Use |
|---|---|
| `local-ecosystem-auditor` | filesystem/runtime risk and topology |
| `ecosystem-analyzer` | cross-host drift and duplication |
| `tree-explorer` | directory manifests and size hotspots |
| `capability-atlas` | canonical source and host parity |
| `security-engineer` | auth, MCP, credential, and private-state review |
| `tool-evaluator` | decide which tools/MCPs are actually useful |
| `workflow-orchestrator` | turn findings into ordered reversible work |

## Security corrections from independent review

- `~/.hermes/skills/video-marketing` is a broken skill projection and needs either repair or explicit retirement.
- `chrome-devtools` runs mutable `npx -y chrome-devtools-mcp@latest`; pin and verify the package before relying on it.
- Enabled Suno MCPs expose login, cookie save/load, authenticated-session restore, browser capture, generation, and downloads. Treat these as high-risk account-control tools.
- Current safety defaults deserve review: `tirith_fail_open: true`, lazy installs enabled, destructive slash confirmation disabled, `verify_on_stop: false`, and MCP inheritance enabled for children.
- Check permissions at the symlink targets of `~/.hermes/.env` and `~/.hermes/auth.json`; the links alone do not establish credential safety.
- Skill presence, configured toolsets, and MCP enablement do not prove runtime health or successful loading.

## Recommendations ranked

### P0 — maintain the boundary

- Keep `~/.agent-skills` canonical for authored skills and agents.
- Keep `~/.agents/skills` as a compatibility symlink.
- Do not delete or merge `skills.bak-*` until the content differences are reviewed.
- Keep Hermes state, sessions, logs, auth, and model caches out of canonical capability inventories.
- Do not describe the broad built-in tool list as enabled without checking `platform_toolsets.cli`; configured availability and runtime health are separate claims.

### P1 — create one capability parity ledger

Track each capability with:

```text
capability name
canonical source
Claude projection
Codex projection
Hermes projection
other host projections
content hash
trigger
tools/MCP required
parity status
drift risk
last verified
```

### P1 — audit enabled MCPs

- Verify `chrome-devtools`, `suno-cdp`, and `suno-recon` are still required.
- Separate low-risk read tools from browser authentication and cookie operations.
- Add explicit approval gates around login, cookie, download, and generation tools.

### P2 — reduce report ambiguity

Update future audit reports to publish both:

- **Authority count:** direct active contracts only.
- **Physical count:** recursive files including nested references, backups, and vendored material.

### P2 — add a runtime capability probe

A small read-only probe should verify:

- symlink targets
- broken links
- skill frontmatter validity
- agent manifest validity
- MCP server command existence
- toolset configuration
- stale catalog timestamps
- canonical/host content hashes

## Artifacts

- `FINAL-FINDINGS.md` — reflected synthesis with specialist provenance, confidence boundaries, and final decision.
- `README.md` — this audit and recommendations.
- `surface-inventory.json` — machine-readable root metrics.
- `skill-parity.json` — canonical/backup direct skill comparison.
- `skill-drift-ledger.json` — hashed parity ledger and read-only disposition of canonical, backup, and divergent skills.
- `surfaces.csv` — compact surface inventory.

## Limitations

- No session, database, auth, token, or secret contents were inspected.
- The audit is structural and configuration-aware, not a full semantic review of every skill.
- Hermes runtime directories were intentionally excluded from deep content walking where they are cache/session-heavy.
- A skill’s existence does not prove it is loaded by every host.
- Enabled MCP configuration does not prove the external/local server is healthy.

