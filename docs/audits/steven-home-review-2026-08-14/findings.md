# Findings

## 1. The home directory has several operational zones

The top level separates into recognizable zones:

- AI and agent runtime state: `.agent-skills`, `.agents`, `.claude`, `.codex`,
  `.gemini`, `.grok`, `.hermes`, `.kimi`, `.opencode`, `.qwen`, and related
  tool directories.
- Source and project collections: `github`, `Development`, `CoX-mod-Adventure`,
  `ESO`, `PYTHON_MARKETPLACE_MASTER`, `diGiTaLdiVe`, `fiverr`, `AVATARARTS`,
  `portfolio-intell`, and `create-mcp-to-sell`.
- Personal/creative media: `!!FONTS`, `comic`, `my-comic`, `Pictures`,
  `Movies`, `Music`, `NotebookLM`, and `RightFont`.
- Staging and historical material: `audit`, `exports`, `logs`, `tmp`,
  `tmp-csv`, `local-dev-runtime-quarantine`, and
  `system-cleanup-quarantine-20260715-101935`.

This is a useful conceptual map for future targeted reviews.

## 2. Storage concentration is dominated by Downloads and project/media roots

Observed approximate sizes:

| Path | Size |
|---|---:|
| `Downloads` | 24 GB |
| `Documents` | 3.2 GB |
| `CoX-mod-Adventure` | 4.3 GB |
| `.codex` | 668 MB |
| `.claude` | 568 MB |
| `Desktop` | 581 MB |
| `.agent-skills` | 123 MB |
| `portfolio-intell` | 45 MB |
| `create-mcp-to-sell` | 23 MB |

The next storage investigation should focus on `Downloads`, then the large
project/media roots, using age, duplication, and recoverability—not size alone.

## 3. Repository sprawl is broad but organized around recurring themes

The scan found Git repositories in the central `github/` collection and in
many project families, including CoX, ESO, AI tooling, agent skills, media,
marketplace work, and personal sites. There are also nested repositories and
vendor/history repositories, so a raw repository count would overstate active
projects.

Representative roots include:

- `/Users/steven/github`
- `/Users/steven/CoX-mod-Adventure`
- `/Users/steven/ESO`
- `/Users/steven/PYTHON_MARKETPLACE_MASTER`
- `/Users/steven/diGiTaLdiVe`
- `/Users/steven/Development`
- `/Users/steven/iterm2`

The practical next step is classification into active, reference, archive,
vendor, and duplicate/derived repositories.

## 4. Agent-runtime duplication deserves explicit ownership rules

The home directory contains both canonical-looking runtime locations and
backups/legacy or adjacent ecosystems, including `.agent-skills`, `.agents`,
`.agent-skills-backup-2026-08-06`, `.agents.pre-agent-skills-link-20260713-1420`,
`.codex`, `.claude`, `.gemini`, and `.hermes`.

This is not evidence that any directory is safe to delete. It is evidence that
future cleanup should begin with a source-of-truth map and link/consumer check.

## Recommended follow-up sequence

1. Build a storage report for `Downloads` and `Documents` by age, file type,
   duplicate hash, and last-access policy.
2. Build a repository registry that marks each Git root as active, archived,
   nested/vendor, or duplicate/derived.
3. Maintain an agent-runtime ownership table showing canonical source,
   symlink/mirror status, and disposable caches.
4. Review quarantine and staging directories separately; do not merge their
   contents into active project inventories automatically.
5. Re-run this structural snapshot after major migrations so trend changes are
   recorded without replacing prior audits.

## Evidence method

- Used the local `eza-nav` listing script and `eza` for directory metadata.
- Used bounded filesystem scans for Git repository locations.
- Used `du -sh` for selected high-value roots.
- No files were modified, moved, deleted, staged, or committed.
