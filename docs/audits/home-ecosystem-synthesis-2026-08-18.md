# Home Capability Ecosystem Synthesis — 2026-08-18

## Executive assessment

The local capability ecosystem is usable and the intended canonical design is
sound: `/Users/steven/.agent-skills` is the source tree, while the primary
Claude, Codex, and legacy `.agents` projections resolve to it. The dominant
problem is not missing capability content. It is identity and lifecycle
management: the same skills and agents exist across canonical sources, host
projections, project-local copies, backups, and package caches, without one
machine-readable authority map.

The practical risk is that an update can land in one copy, a runtime can load a
different copy, and an index can report a third view. The next improvement
should therefore be a control plane for provenance, projection health, and
active-versus-archived classification—not another broad content import.

## Evidence consolidated

Sources reviewed:

- `docs/audits/local-agent-skills-review-2026-08-18.md`
- `docs/audits/home-capability-audit-2026-08-18.md`
- `docs/audits/deep-fzf-rg-capability-search-2026-08-18.md`
- `docs/audits/github-agent-skills-comparison-2026-08-18.md`
- `docs/audits/backup-comparison-2026-08-18.md`
- the 2026-08-09 ecosystem audit and 2026-08-08 QF-PIE overlap report
- current filesystem projections, lock files, Git state, and selected runtime
  links

Current evidence:

| Area | Finding |
|---|---|
| Canonical source | 311 active skills and 218 active agent/config files in the runtime audit |
| Home-wide search | 3,459 capability roots; 7,789 skill files; 3,285 agent-like Markdown files |
| Home-wide duplication | 1,806 skill-name groups and 445 agent-name groups; many are cache or archive artifacts |
| Exact duplication | 2,111 exact skill groups and 797 exact agent groups across the home scan |
| Primary projections | `.claude/skills`, `.claude/agents`, `.codex/superpowers`, and `.agents/skills` resolve correctly |
| Secondary broken links | 5 remain: 3 stale marketplace links and 2 `.gemini/skills` links targeting the wrong `.agents` path |
| Lock metadata | canonical `.skill-lock.json` and compatibility `.agents/.skill-lock.json` have different skill selections and agent lists |
| GitHub | local branch is 2 commits ahead and 8 behind `origin/main`; the worktree has 287 dirty entries |
| GitHub catalogs | remote generated catalogs have stale provenance and documented unresolved archive references |
| Backup | new `/Users/steven/.agent-skills-backup-2026-08-18` is a verified content match, excluding volatile `.DS_Store` differences |
| Storage | `.agent-skills` is 215M; the major host runtimes are much larger: `.cursor` 1.8G, `.gemini` 1.2G, `.codex` 824M, `.qwen` 764M, `.claude` 568M |

The duplicate counts must not be interpreted as 1,806 cleanup candidates.
They include package caches, backups, project-local intentionally scoped
skills, and multiple copies of the same content. They demonstrate why path
classification and content hashes are required before consolidation.

## Priority findings

### P0 — establish a single capability authority

The canonical path is documented correctly, but runtime identity is implicit.
The lock files already show divergence: the canonical lock selects
`find-skills`, while `.agents/.skill-lock.json` selects `hyperframes-cli`,
`hyperframes-registry`, and `media-use`. This is a configuration drift signal,
not a content defect.

Recommendation: add a small checked-in registry such as
`catalog/capability-authority.json` with, for every active capability:

- canonical relative path
- type: skill, agent, command, hook, or plugin
- status: active, compatibility, project-local, archive, or cache
- content SHA-256
- supported hosts/projections
- source repository and source commit, when external
- last audit timestamp

Make every index and projection check consume that registry.

### P0 — isolate the dirty Git synchronization problem

The local branch and GitHub have diverged, while the worktree contains 287
dirty entries. A normal pull, merge, or catalog regeneration in this worktree
would mix unrelated local changes with remote generated files and make review
or rollback difficult.

Recommendation: use a clean temporary worktree based on `origin/main` for the
GitHub comparison and reconciliation. Compare three sets independently:

1. local committed commits ahead of GitHub;
2. GitHub commits absent locally;
3. uncommitted local changes.

Only after review should selected changes be applied to the working tree.

### P1 — repair or retire the five secondary broken links

The primary projections are healthy. The remaining failures are:

- three stale links inside the Claude marketplace artifact tree;
- `.gemini/skills/ccxt-python`;
- `.gemini/skills/ccxt-cli`.

The Gemini links point through `../../.agents/skills`, which resolves outside
the user home layout. If Gemini should use the canonical source, recreate them
against `../../.agent-skills/skills/<name>` or replace the whole Gemini skills
surface with a maintained projection. The marketplace links should be repaired
by refreshing that marketplace or removed from the active runtime if the
referenced self-improving-agent package is no longer installed. Do not repair
these by creating a new `/Users/.agents` compatibility tree.

### P1 — split active indexes from discovery indexes

The broad scan found thousands of files because caches, vendored plugins,
backups, project-local repositories, and runtime exports are all meaningful
search results but not active global skills. Maintain separate views:

- `active`: canonical capabilities eligible for global routing;
- `projections`: host links and copies with health/status;
- `project-local`: capabilities intentionally scoped to one repository;
- `archive`: snapshots and historical material;
- `cache`: package-managed or generated copies.

The current reports are useful evidence, but a single undifferentiated count
will keep producing false duplication and stale-total problems.

### P1 — make generated metadata reproducible and trustworthy

GitHub catalogs currently have provenance that does not match the latest remote
tip, and the remote index records unresolved `agents.archive/` references and
missing CI normalization. Local documentation also contains trailing
whitespace in `ECOSYSTEM.md` and `docs/DIRECTORIES.md`, so `git diff --check`
is not clean.

Recommendation: add a deterministic `make audit` or equivalent command that:

- validates frontmatter and required descriptions;
- checks duplicate active names and broken links;
- validates all projections against the authority registry;
- regenerates catalogs with source commit, timestamp, and tool version;
- fails when generated metadata is stale or references nonexistent paths;
- runs `git diff --check` and normalizes file modes.

Generated catalogs should either be regenerated in CI or clearly marked as
release artifacts. They should never silently become a second source of truth.

### P1 — protect indexing from credential-bearing and personal data

The home-wide scan surfaced NotebookLM `auth_info.json` files in earlier
searches, along with histories, session exports, `.env` examples, and runtime
stores. Filename matches such as `token` or `auth` are not proof of a secret,
but they show that capability indexing must use an explicit denylist and never
copy content from those paths into reports.

Recommendation: exclude auth files, histories, session exports, browser data,
`.env*`, keychains, database files, caches, and media from content indexes;
report only redacted path metadata. Run a secret scanner against the canonical
tree and Git diffs, not against every package cache by default.

### P2 — reduce duplication by promotion, not blind deletion

The QF-PIE report identified useful overlap candidates, including duplicate
`skill-creator`/`skill-installer` material and related design, testing, and
platform skills. The home scan shows the larger systemic version of the same
issue. First classify each duplicate as exact mirror, fork, compatibility
adapter, project-local specialization, archive, or cache. Then:

- promote the best maintained variant into the canonical tree;
- add aliases or compatibility metadata for old names;
- leave project-local specializations local;
- retire only verified exact mirrors and stale caches;
- retain historical backups until the canonical hash and runtime behavior are
  verified.

## Best implementation sequence

### Do first

1. Preserve the verified 2026-08-18 backup and the older 2026-08-06 backup;
   treat the ZIP and `.agents.pre-agent-skills-link-*` directory as historical
   references, not active sources.
2. Create the authority registry and a projection-health checker.
3. Inspect the five broken links and decide whether Gemini and the marketplace
   are active; repair only the active surfaces.
4. Generate a clean-worktree GitHub reconciliation report before changing
   `origin/main` or merging catalogs.

### Do next

5. Add active/projection/project-local/archive/cache classifications to the
   home scanner.
6. Reconcile `.skill-lock.json` into one authoritative lock plus generated
   host-specific adapters, or document why a host intentionally differs.
7. Add CI checks for broken links, metadata, duplicate active names, stale
   catalogs, file modes, and secret-path exclusions.

### Do later

8. Review the highest-value overlap candidates from QF-PIE and the exact hash
   groups, starting with canonical-vs-canonical duplicates.
9. Prune or compact caches only after confirming their owning package manager
   can recreate them.
10. Add scheduled audit snapshots and a small trend report: active capability
    count, unhealthy projections, new duplicates, stale indexes, and storage.

## What not to do

- Do not delete the 1,806 duplicate-name groups wholesale.
- Do not merge GitHub into the current dirty worktree.
- Do not copy the entire canonical tree into every host runtime.
- Do not make `/Users/steven/.agents` a second writable source.
- Do not publish broad home-wide indexes containing auth, history, or session
  content.
- Do not treat generated catalogs as authoritative until their provenance is
  reproducible.

## Bottom line

The ecosystem has strong capability coverage and a correct primary projection
architecture. Its next maturity step is operational: provenance, health,
classification, and reproducible indexes. If the authority registry,
projection checker, and clean Git reconciliation are implemented first, later
deduplication and cache cleanup become safe, measurable maintenance instead of
high-risk filesystem surgery.
