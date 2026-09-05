# Deep `fzf` + `rg` Capability Search — 2026-08-18

## Search method

This pass used `fd` for structural discovery, `rg` for content/frontmatter
signals, and `fzf --filter` for path partitioning. It included hidden files and
excluded dependency/build internals such as `.git`, `node_modules`, macOS
`Library`, Python caches, package caches, and build directories.

The first broad path search produced 47,962 nested path hits because every file
under a skills tree matched. The focused search reduced that to:

- **7,414** actual `SKILL.md` files
- **3,406** agent-like Markdown files under `agents/` or named `AGENTS.md`
- **1,525** files with capability-style metadata signals in the selected host
  trees

No file bodies or credential values were copied into this report.

## Capability ecosystems found

### Canonical / primary

- `~/.agent-skills/skills`
- `~/.agent-skills/agents`
- `~/.agent-skills/deep-research`

### Host-specific runtime surfaces

- `~/.qwen/skills` and `~/.qwen/agents`
- `~/.cursor/skills` and `~/.cursor/agents`
- `~/.gemini/skills` and `~/.gemini/agents`
- `~/.grok/skills`
- `~/.hermes/skills`
- `~/.opencode/skills`
- `~/.kimi/skills`
- `~/.cline/skills`
- `~/.copilot/skills`
- `~/.codeium/windsurf/skills`
- `~/.codex/skills`

### Project-local / standalone surfaces

- `~/skills`
- `~/agents`
- `~/iterm2/skills` and command-local `SKILL.md` files
- `~/github/*`
- `~/NotebookLM/skill`
- `~/comic/*`
- `~/portfolio-intell/*`
- `~/tmp/*_recovered`

### Backup and generated material

- `.claude/skills.bak` and `.claude/agents.bak`
- `.agent-skills-backup-2026-08-06`
- `.gemini/backups`
- `.cursor/MERGE_BACKUP_*`
- plugin marketplaces and package-managed skill caches

## Important findings

1. The home contains multiple independently writable capability authorities.
   The canonical source is clear, but several host trees contain real copies,
   not only symlinks.
2. Common names such as `comic`, `agmsg`, `ccxt-*`, `find-docs`, `skill-creator`,
   and `writing-plans` occur across multiple hosts and projects.
3. There are many manifest/index files: `skills-lock.json`, `skills-meta.csv`,
   `.skillfish.json`, plugin manifests, and project registries. These should be
   treated as source-specific metadata, not one global truth.
4. Broad manifest searching surfaced NotebookLM `auth_info.json` files. Keep
   credential-bearing manifests excluded from future content indexing.
5. The repository-local `.agent-skills/.claude/skills` compatibility links still
   contain 25 broken links, while the host-level `~/.claude/skills`
   projection resolves correctly.

## Recommended next move

Create one machine-readable identity record per capability:

```yaml
name: writing-plans
canonical_path: ~/.agent-skills/skills/writing-plans/SKILL.md
status: active        # active | alias | reference | backup | cache
runtime_hosts: [codex, claude, qwen]
source: local
content_hash: ...
```

Then generate host projections from that identity map. This will make `fzf`
and `rg` searches useful for discovery without allowing every cached or copied
skill to become an accidental runtime authority.
