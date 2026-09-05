# Priority Group Provenance Review — 2026-08-18

This report compares selected high-volume same-name groups by path, lifecycle classification, SHA-256 hash, and file size. Same-name does not imply same behavior.

## Decision rules

- Exact same hash plus projection/archive provenance: consolidation candidate after runtime verification.
- Different hash: retain as separate variants until a human selects the canonical behavior.
- Project-local or plugin-owned: do not merge into the global source automatically.
- Canonical-source files: treat as authoritative candidates, not disposable duplicates.

## `code-reviewer` (agent)

- Members: **74**
- Distinct hashes: **11**
- Classifications: canonical-source=3, backup/archive=17, cache/vendored=22, host-runtime=9, project-local=23

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills-backup-2026-08-06/agents/2-personal-tooled/code-review.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills-backup-2026-08-06/agents/code-review.md` |
| backup/archive | `697bf01df85207d6…` | 2243 | `~/.agent-skills-backup-2026-08-06/agents/code-reviewer.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills-backup-2026-08-18/agents/2-personal-tooled/code-review.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills-backup-2026-08-18/agents/code-review.md` |
| backup/archive | `6eccc59686422e13…` | 2458 | `~/.agent-skills-backup-2026-08-18/agents/code-reviewer.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/agents/2-personal-tooled/code-review.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/agents/code-review.md` |
| backup/archive | `6eccc59686422e13…` | 2458 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/agents/code-reviewer.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills/backups/agent-skills-20260815-024526/agents/2-personal-tooled/code-review.md` |
| backup/archive | `86834916d903ad21…` | 2848 | `~/.agent-skills/backups/agent-skills-20260815-024526/agents/code-review.md` |
| backup/archive | `6eccc59686422e13…` | 2458 | `~/.agent-skills/backups/agent-skills-20260815-024526/agents/code-reviewer.md` |
| backup/archive | `638802c7718ba46b…` | 3212 | `~/.cursor/MERGE_BACKUP_20260411_025502/MERGE_BACKUP_20260411_025502/agents/code-reviewer.md` |
| backup/archive | `638802c7718ba46b…` | 3212 | `~/.cursor/MERGE_BACKUP_20260411_025502/agents/code-reviewer.md` |
| backup/archive | `638802c7718ba46b…` | 3212 | `~/.gemini/backups/re-ole-20260415/.qwen/agents/code-reviewer.md` |
| backup/archive | `b17be291994b798c…` | 3888 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/agents/code-reviewer.md` |
| backup/archive | `b17be291994b798c…` | 3888 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/agents/code-reviewer.md` |
| cache/vendored | `5677b371344cdc44…` | 3115 | `~/.claude/plugins/cache/claude-plugins-official/coderabbit/1.1.1/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/.claude/plugins/cache/claude-plugins-official/feature-dev/unknown/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/.claude/plugins/cache/claude-plugins-official/pr-review-toolkit/unknown/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/feature-dev/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/.codex/.tmp/marketplaces/claude-plugins-official/plugins/feature-dev/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/.codex/.tmp/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/code-reviewer.md` |
| cache/vendored | `1530b99e77fe785f…` | 2762 | `~/.codex/plugins/cache/claude-plugins-official/coderabbit/1.1.1/agents/code-reviewer.md` |
| cache/vendored | `b17be291994b798c…` | 3888 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/agents/code-reviewer.md` |
| cache/vendored | `6ca110005ba1f2a8…` | 2528 | `~/.gemini/antigravity-cli/plugins/supremepower/core/agents/code-reviewer.md` |
| cache/vendored | `5677b371344cdc44…` | 3115 | `~/.gemini/config/plugins/coderabbit/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/.gemini/config/plugins/feature-dev/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/.grok/marketplace-cache/783232b622f8182e/plugins/feature-dev/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/.grok/marketplace-cache/783232b622f8182e/plugins/pr-review-toolkit/agents/code-reviewer.md` |
| cache/vendored | `1530b99e77fe785f…` | 2762 | `~/.langcli/plugins/cache/claude-plugins-official/coderabbit/aa49953c4cb2/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/.langcli/plugins/marketplaces/claude-plugins-official/plugins/feature-dev/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/.langcli/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/Pictures/ideoGram/Sora-aLt/plugins/claude-plugins-official/plugins/feature-dev/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/Pictures/ideoGram/Sora-aLt/plugins/claude-plugins-official/plugins/pr-review-toolkit/agents/code-reviewer.md` |
| cache/vendored | `5677b371344cdc44…` | 3115 | `~/iterm2/.claude/plugins/claude-plugins-official/coderabbit/1.1.1/agents/code-reviewer.md` |
| cache/vendored | `a7df173bf77a00da…` | 2994 | `~/iterm2/.claude/plugins/claude-plugins-official/feature-dev/unknown/agents/code-reviewer.md` |
| cache/vendored | `019395c3ce457460…` | 3635 | `~/iterm2/.claude/plugins/claude-plugins-official/pr-review-toolkit/unknown/agents/code-reviewer.md` |
| canonical-source | `86834916d903ad21…` | 2848 | `~/.agent-skills/agents/2-personal-tooled/code-review.md` |
| canonical-source | `86834916d903ad21…` | 2848 | `~/.agent-skills/agents/code-review.md` |
| canonical-source | `6eccc59686422e13…` | 2458 | `~/.agent-skills/agents/code-reviewer.md` |
| host-runtime | `6eccc59686422e13…` | 2458 | `~/.codex/agents/code-reviewer.md` |
| host-runtime | `638802c7718ba46b…` | 3212 | `~/.cursor/agents/code-reviewer.md` |
| host-runtime | `b17be291994b798c…` | 3888 | `~/.gemini/supremepower/agents/code-reviewer.md` |
| host-runtime | `6ca110005ba1f2a8…` | 2528 | `~/.gemini/supremepower/core/agents/code-reviewer.md` |
| host-runtime | `638802c7718ba46b…` | 3212 | `~/.qwen/agents/code-reviewer.md` |
| host-runtime | `b17be291994b798c…` | 3888 | `~/.qwen/superpowers/4.2.0/agents/code-reviewer.md` |
| host-runtime | `b17be291994b798c…` | 3888 | `~/.qwen/superpowers/agents/code-reviewer.md` |
| host-runtime | `b17be291994b798c…` | 3888 | `~/iterm2/.qwen/superpowers/4.2.0/agents/code-reviewer.md` |
| host-runtime | `b17be291994b798c…` | 3888 | `~/iterm2/.qwen/superpowers/agents/code-reviewer.md` |
| project-local | `86834916d903ad21…` | 2848 | `~/.config/poolside/agents/code-review.md` |
| project-local | `6eccc59686422e13…` | 2458 | `~/.config/poolside/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/ESO/EsoMystic/extensions/supremepower/core/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/Pictures/ideoGram/Sora-aLt/agents/agents/code-review.md` |
| project-local | `300712e5429c19b6…` | 2576 | `~/Pictures/ideoGram/Sora-aLt/agents/agents/code-reviewer.md` |
| project-local | `86834916d903ad21…` | 2848 | `~/agents/2-personal-tooled/code-review.md` |
| project-local | `86834916d903ad21…` | 2848 | `~/agents/code-review.md` |
| project-local | `697bf01df85207d6…` | 2243 | `~/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/diGiTaLdiVe/my-supremepowers/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/github/my-powers/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/github/my-powers/core/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/github/my-powers/superpowers/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/github/my-powers/superpowers/core/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/iterm2/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/iterm2/superpowers/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/tmp/zij3oup9_recovered/my-supremepowers/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/agents/code-reviewer.md` |
| project-local | `b17be291994b798c…` | 3888 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/agents/code-reviewer.md` |
| project-local | `6ca110005ba1f2a8…` | 2528 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/agents/code-reviewer.md` |

## `brainstorming` (skill)

- Members: **47**
- Distinct hashes: **9**
- Classifications: backup/archive=8, canonical-source=1, cache/vendored=6, host-runtime=10, project-local=22

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `7468ecd929d4585d…` | 4899 | `~/.agent-skills-backup-2026-08-06/skills/brainstorming/SKILL.md` |
| backup/archive | `32723a5847d02bea…` | 5561 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/brainstorming/SKILL.md` |
| backup/archive | `32723a5847d02bea…` | 5561 | `~/.agent-skills-backup-2026-08-18/skills/brainstorming/SKILL.md` |
| backup/archive | `32723a5847d02bea…` | 5561 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/brainstorming/SKILL.md` |
| backup/archive | `f0992e48eb8229e5…` | 2657 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/brainstorming/SKILL.md` |
| backup/archive | `f0992e48eb8229e5…` | 2657 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-brainstorming/SKILL.md` |
| backup/archive | `206c63e80d38c57e…` | 2505 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/brainstorming/SKILL.md` |
| backup/archive | `f0992e48eb8229e5…` | 2657 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/brainstorming/SKILL.md` |
| cache/vendored | `bba47904a7f6bbee…` | 10634 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/brainstorming/SKILL.md` |
| cache/vendored | `74edf03ea6d24ef5…` | 15456 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/brainstorming/SKILL.md` |
| cache/vendored | `bba47904a7f6bbee…` | 10634 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/brainstorming/SKILL.md` |
| cache/vendored | `4f563bda15db0660…` | 285 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/brainstorming/SKILL.md` |
| cache/vendored | `bba47904a7f6bbee…` | 10634 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/brainstorming/SKILL.md` |
| cache/vendored | `bba47904a7f6bbee…` | 10634 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/brainstorming/SKILL.md` |
| canonical-source | `32723a5847d02bea…` | 5561 | `~/.agent-skills/skills/brainstorming/SKILL.md` |
| host-runtime | `f0992e48eb8229e5…` | 2657 | `~/.qwen/integrations/supremepower/skills/brainstorming/SKILL.md` |
| host-runtime | `f0992e48eb8229e5…` | 2657 | `~/.qwen/skills/superpowers-brainstorming/SKILL.md` |
| host-runtime | `206c63e80d38c57e…` | 2505 | `~/.qwen/superpowers/4.2.0/skills/brainstorming/SKILL.md` |
| host-runtime | `206c63e80d38c57e…` | 2505 | `~/.qwen/superpowers/a98c5dfc9de0/skills/brainstorming/SKILL.md` |
| host-runtime | `206c63e80d38c57e…` | 2505 | `~/.qwen/superpowers/skills/brainstorming/SKILL.md` |
| host-runtime | `3752febf1a7e6ff1…` | 4842 | `~/.qwen/superpowers/skills/disabled/brainstorming/SKILL.md` |
| host-runtime | `32723a5847d02bea…` | 5561 | `~/Music/nocturneMelodies/.agents/skills/brainstorming/SKILL.md` |
| host-runtime | `206c63e80d38c57e…` | 2505 | `~/iterm2/.qwen/superpowers/4.2.0/skills/brainstorming/SKILL.md` |
| host-runtime | `206c63e80d38c57e…` | 2505 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/brainstorming/SKILL.md` |
| host-runtime | `206c63e80d38c57e…` | 2505 | `~/iterm2/.qwen/superpowers/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/brainstorming/SKILL.md` |
| project-local | `f0992e48eb8229e5…` | 2657 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/integrations/supremepower/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/brainstorming/SKILL.md` |
| project-local | `3752febf1a7e6ff1…` | 4842 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/disabled/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/Pictures/ideoGram/Sora-aLt/skills/brainstorming/SKILL.md` |
| project-local | `f0992e48eb8229e5…` | 2657 | `~/diGiTaLdiVe/my-supremepowers/integrations/supremepower/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/diGiTaLdiVe/my-supremepowers/skills/brainstorming/SKILL.md` |
| project-local | `3752febf1a7e6ff1…` | 4842 | `~/diGiTaLdiVe/my-supremepowers/skills/disabled/brainstorming/SKILL.md` |
| project-local | `f0992e48eb8229e5…` | 2657 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/github/my-powers/core/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/github/my-powers/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/github/my-powers/superpowers/core/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/github/my-powers/superpowers/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/iterm2/Codex/superpowers/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/iterm2/skills/brainstorming/SKILL.md` |
| project-local | `7a238df1ebf0656c…` | 4690 | `~/iterm2/superpowers/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/brainstorming/SKILL.md` |
| project-local | `206c63e80d38c57e…` | 2505 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/brainstorming/SKILL.md` |
| project-local | `f0992e48eb8229e5…` | 2657 | `~/tmp/zij3oup9_recovered/my-supremepowers/integrations/supremepower/skills/brainstorming/SKILL.md` |

## `executing-plans` (skill)

- Members: **48**
- Distinct hashes: **8**
- Classifications: backup/archive=8, canonical-source=1, cache/vendored=7, host-runtime=10, project-local=22

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `582937183ad9bec6…` | 2171 | `~/.agent-skills-backup-2026-08-06/skills/executing-plans/SKILL.md` |
| backup/archive | `115e5dac2828191a…` | 2391 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/executing-plans/SKILL.md` |
| backup/archive | `115e5dac2828191a…` | 2391 | `~/.agent-skills-backup-2026-08-18/skills/executing-plans/SKILL.md` |
| backup/archive | `115e5dac2828191a…` | 2391 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/executing-plans/SKILL.md` |
| backup/archive | `48cd880cea6a7a97…` | 2323 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/executing-plans/SKILL.md` |
| backup/archive | `48cd880cea6a7a97…` | 2323 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-executing-plans/SKILL.md` |
| backup/archive | `d099fa42fd7518f4…` | 2550 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/executing-plans/SKILL.md` |
| backup/archive | `48cd880cea6a7a97…` | 2323 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/executing-plans/SKILL.md` |
| cache/vendored | `e2102f1163143393…` | 2469 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/executing-plans/SKILL.md` |
| cache/vendored | `c4c3d8b628c51114…` | 2305 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/executing-plans/SKILL.md` |
| cache/vendored | `a711f83fb762e2ea…` | 2459 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/executing-plans/SKILL.md` |
| cache/vendored | `582937183ad9bec6…` | 2171 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/executing-plans/SKILL.md` |
| cache/vendored | `7379b6f734dbe3fb…` | 195 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/executing-plans/SKILL.md` |
| cache/vendored | `e2102f1163143393…` | 2469 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/executing-plans/SKILL.md` |
| cache/vendored | `e2102f1163143393…` | 2469 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/executing-plans/SKILL.md` |
| canonical-source | `115e5dac2828191a…` | 2391 | `~/.agent-skills/skills/executing-plans/SKILL.md` |
| host-runtime | `582937183ad9bec6…` | 2171 | `~/.gemini/supremepower/core/skills/executing-plans/SKILL.md` |
| host-runtime | `582937183ad9bec6…` | 2171 | `~/.gemini/supremepower/skills/executing-plans/SKILL.md` |
| host-runtime | `48cd880cea6a7a97…` | 2323 | `~/.qwen/integrations/supremepower/skills/executing-plans/SKILL.md` |
| host-runtime | `48cd880cea6a7a97…` | 2323 | `~/.qwen/skills/superpowers-executing-plans/SKILL.md` |
| host-runtime | `d099fa42fd7518f4…` | 2550 | `~/.qwen/superpowers/4.2.0/skills/executing-plans/SKILL.md` |
| host-runtime | `d099fa42fd7518f4…` | 2550 | `~/.qwen/superpowers/a98c5dfc9de0/skills/executing-plans/SKILL.md` |
| host-runtime | `582937183ad9bec6…` | 2171 | `~/.qwen/superpowers/skills/executing-plans/SKILL.md` |
| host-runtime | `d099fa42fd7518f4…` | 2550 | `~/iterm2/.qwen/superpowers/4.2.0/skills/executing-plans/SKILL.md` |
| host-runtime | `d099fa42fd7518f4…` | 2550 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/executing-plans/SKILL.md` |
| host-runtime | `582937183ad9bec6…` | 2171 | `~/iterm2/.qwen/superpowers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/ESO/EsoMystic/extensions/supremepower/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/executing-plans/SKILL.md` |
| project-local | `48cd880cea6a7a97…` | 2323 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/integrations/supremepower/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/Pictures/ideoGram/Sora-aLt/skills/executing-plans/SKILL.md` |
| project-local | `48cd880cea6a7a97…` | 2323 | `~/diGiTaLdiVe/my-supremepowers/integrations/supremepower/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/diGiTaLdiVe/my-supremepowers/skills/executing-plans/SKILL.md` |
| project-local | `48cd880cea6a7a97…` | 2323 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/github/my-powers/core/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/github/my-powers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/github/my-powers/superpowers/core/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/github/my-powers/superpowers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/iterm2/Codex/superpowers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/iterm2/skills/executing-plans/SKILL.md` |
| project-local | `d099fa42fd7518f4…` | 2550 | `~/iterm2/superpowers/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/executing-plans/SKILL.md` |
| project-local | `582937183ad9bec6…` | 2171 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/executing-plans/SKILL.md` |
| project-local | `48cd880cea6a7a97…` | 2323 | `~/tmp/zij3oup9_recovered/my-supremepowers/integrations/supremepower/skills/executing-plans/SKILL.md` |

## `finishing-a-development-branch` (skill)

- Members: **49**
- Distinct hashes: **6**
- Classifications: backup/archive=8, canonical-source=1, cache/vendored=8, host-runtime=11, project-local=21

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `dd2f82c6dc8582b6…` | 4250 | `~/.agent-skills-backup-2026-08-06/skills/finishing-a-development-branch/SKILL.md` |
| backup/archive | `ced29061c571106b…` | 4366 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/finishing-a-development-branch/SKILL.md` |
| backup/archive | `ced29061c571106b…` | 4366 | `~/.agent-skills-backup-2026-08-18/skills/finishing-a-development-branch/SKILL.md` |
| backup/archive | `ced29061c571106b…` | 4366 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/finishing-a-development-branch/SKILL.md` |
| backup/archive | `6e65323e67d4d52b…` | 4402 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/finishing-a-development-branch/SKILL.md` |
| backup/archive | `6e65323e67d4d52b…` | 4402 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-finishing-a-development-branch/SKILL.md` |
| backup/archive | `dd2f82c6dc8582b6…` | 4250 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/finishing-a-development-branch/SKILL.md` |
| backup/archive | `6e65323e67d4d52b…` | 4402 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `5c8d4b59aedb14c9…` | 7061 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `8db5a922b242dd4e…` | 7781 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `dd2f82c6dc8582b6…` | 4250 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `dd2f82c6dc8582b6…` | 4250 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `6e65323e67d4d52b…` | 4402 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/disabled/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `60d4e78a2e9e3590…` | 321 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `5c8d4b59aedb14c9…` | 7061 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/finishing-a-development-branch/SKILL.md` |
| cache/vendored | `5c8d4b59aedb14c9…` | 7061 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| canonical-source | `ced29061c571106b…` | 4366 | `~/.agent-skills/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/.gemini/supremepower/core/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/.gemini/supremepower/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `6e65323e67d4d52b…` | 4402 | `~/.qwen/integrations/supremepower/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `6e65323e67d4d52b…` | 4402 | `~/.qwen/skills/superpowers-finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/.qwen/superpowers/4.2.0/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/.qwen/superpowers/a98c5dfc9de0/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `6e65323e67d4d52b…` | 4402 | `~/.qwen/superpowers/skills/disabled/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/.qwen/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/iterm2/.qwen/superpowers/4.2.0/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/finishing-a-development-branch/SKILL.md` |
| host-runtime | `dd2f82c6dc8582b6…` | 4250 | `~/iterm2/.qwen/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `6e65323e67d4d52b…` | 4402 | `~/ESO/EsoMystic/extensions/supremepower/skills/disabled/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/ESO/EsoMystic/extensions/supremepower/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `6e65323e67d4d52b…` | 4402 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/disabled/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `6e65323e67d4d52b…` | 4402 | `~/diGiTaLdiVe/my-supremepowers/skills/disabled/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/diGiTaLdiVe/my-supremepowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `6e65323e67d4d52b…` | 4402 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/github/my-powers/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/github/my-powers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/github/my-powers/superpowers/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/github/my-powers/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/iterm2/Codex/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/iterm2/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/iterm2/superpowers/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/finishing-a-development-branch/SKILL.md` |
| project-local | `dd2f82c6dc8582b6…` | 4250 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/finishing-a-development-branch/SKILL.md` |

## `requesting-code-review` (skill)

- Members: **55**
- Distinct hashes: **11**
- Classifications: backup/archive=11, canonical-source=2, cache/vendored=8, host-runtime=11, project-local=23

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `3c37a6dd18a08d1b…` | 11578 | `~/.agent-skills-backup-2026-08-06/skills/software-development/requesting-code-review/SKILL.md` |
| backup/archive | `8a0a4e2f699dffaa…` | 6337 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/requesting-code-review/SKILL.md` |
| backup/archive | `45d7a5bf53eedb3a…` | 11819 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/software-development/requesting-code-review/SKILL.md` |
| backup/archive | `8a0a4e2f699dffaa…` | 6337 | `~/.agent-skills-backup-2026-08-18/skills/requesting-code-review/SKILL.md` |
| backup/archive | `45d7a5bf53eedb3a…` | 11819 | `~/.agent-skills-backup-2026-08-18/skills/software-development/requesting-code-review/SKILL.md` |
| backup/archive | `8a0a4e2f699dffaa…` | 6337 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/requesting-code-review/SKILL.md` |
| backup/archive | `45d7a5bf53eedb3a…` | 11819 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/software-development/requesting-code-review/SKILL.md` |
| backup/archive | `5d35685977295966…` | 2852 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/requesting-code-review/SKILL.md` |
| backup/archive | `5d35685977295966…` | 2852 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-requesting-code-review/SKILL.md` |
| backup/archive | `2da31af22a58938a…` | 2700 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/requesting-code-review/SKILL.md` |
| backup/archive | `5d35685977295966…` | 2852 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `5a3a44a3667800e2…` | 2808 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `d71cc01ba56d2325…` | 2956 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `a5ff68586ccf62d1…` | 2935 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `2da31af22a58938a…` | 2700 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `5d35685977295966…` | 2852 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/disabled/requesting-code-review/SKILL.md` |
| cache/vendored | `5ba1d1f27e769ec3…` | 212 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `5a3a44a3667800e2…` | 2808 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/requesting-code-review/SKILL.md` |
| cache/vendored | `5a3a44a3667800e2…` | 2808 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/requesting-code-review/SKILL.md` |
| canonical-source | `8a0a4e2f699dffaa…` | 6337 | `~/.agent-skills/skills/requesting-code-review/SKILL.md` |
| canonical-source | `45d7a5bf53eedb3a…` | 11819 | `~/.agent-skills/skills/software-development/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/.gemini/supremepower/core/skills/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/.gemini/supremepower/skills/requesting-code-review/SKILL.md` |
| host-runtime | `5d35685977295966…` | 2852 | `~/.qwen/integrations/supremepower/skills/requesting-code-review/SKILL.md` |
| host-runtime | `5d35685977295966…` | 2852 | `~/.qwen/skills/superpowers-requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/.qwen/superpowers/4.2.0/skills/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/.qwen/superpowers/a98c5dfc9de0/skills/requesting-code-review/SKILL.md` |
| host-runtime | `5d35685977295966…` | 2852 | `~/.qwen/superpowers/skills/disabled/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/.qwen/superpowers/skills/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/iterm2/.qwen/superpowers/4.2.0/skills/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/requesting-code-review/SKILL.md` |
| host-runtime | `2da31af22a58938a…` | 2700 | `~/iterm2/.qwen/superpowers/skills/requesting-code-review/SKILL.md` |
| project-local | `1126afb626b38f5b…` | 8465 | `~/.hermes/hermes-agent/skills/software-development/requesting-code-review/SKILL.md` |
| project-local | `2559f1e7763599b2…` | 12803 | `~/.hermes/skills/software-development/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/requesting-code-review/SKILL.md` |
| project-local | `5d35685977295966…` | 2852 | `~/ESO/EsoMystic/extensions/supremepower/skills/disabled/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/ESO/EsoMystic/extensions/supremepower/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/requesting-code-review/SKILL.md` |
| project-local | `5d35685977295966…` | 2852 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/disabled/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/requesting-code-review/SKILL.md` |
| project-local | `5d35685977295966…` | 2852 | `~/diGiTaLdiVe/my-supremepowers/skills/disabled/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/diGiTaLdiVe/my-supremepowers/skills/requesting-code-review/SKILL.md` |
| project-local | `5d35685977295966…` | 2852 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/github/my-powers/core/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/github/my-powers/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/github/my-powers/superpowers/core/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/github/my-powers/superpowers/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/iterm2/Codex/superpowers/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/iterm2/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/iterm2/superpowers/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/requesting-code-review/SKILL.md` |
| project-local | `2da31af22a58938a…` | 2700 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/requesting-code-review/SKILL.md` |

## `skill-creator` (skill)

- Members: **37**
- Distinct hashes: **9**
- Classifications: backup/archive=11, canonical-source=4, cache/vendored=6, host-runtime=3, project-local=13

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `da44c88f6b3845a8…` | 22047 | `~/.agent-skills-backup-2026-08-06/skills/.system/skill-creator/SKILL.md` |
| backup/archive | `18daa04e9fb75efa…` | 32328 | `~/.agent-skills-backup-2026-08-06/skills/skill-creator/SKILL.md` |
| backup/archive | `da44c88f6b3845a8…` | 22047 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/.system/skill-creator/SKILL.md` |
| backup/archive | `18daa04e9fb75efa…` | 32328 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/skill-creator/SKILL.md` |
| backup/archive | `6ee940a78fe22e60…` | 18874 | `~/.agent-skills-backup-2026-08-18/deeptutor/deeptutor-mimic/deeptutor/tutorbot/skills/skill-creator/SKILL.md` |
| backup/archive | `6ee940a78fe22e60…` | 18874 | `~/.agent-skills-backup-2026-08-18/deeptutor/deeptutor/tutorbot/skills/skill-creator/SKILL.md` |
| backup/archive | `da44c88f6b3845a8…` | 22047 | `~/.agent-skills-backup-2026-08-18/skills/.system/skill-creator/SKILL.md` |
| backup/archive | `18daa04e9fb75efa…` | 32328 | `~/.agent-skills-backup-2026-08-18/skills/skill-creator/SKILL.md` |
| backup/archive | `da44c88f6b3845a8…` | 22047 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/.system/skill-creator/SKILL.md` |
| backup/archive | `18daa04e9fb75efa…` | 32328 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/skill-creator/SKILL.md` |
| backup/archive | `ba8bebb2c0854441…` | 32370 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/skill-creator/SKILL.md` |
| cache/vendored | `dcd4803e61e913e6…` | 33168 | `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md` |
| cache/vendored | `dcd4803e61e913e6…` | 33168 | `~/.codex/.tmp/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md` |
| cache/vendored | `ba8bebb2c0854441…` | 32370 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/skill-creator/SKILL.md` |
| cache/vendored | `dcd4803e61e913e6…` | 33168 | `~/.grok/marketplace-cache/783232b622f8182e/plugins/skill-creator/skills/skill-creator/SKILL.md` |
| cache/vendored | `dcd4803e61e913e6…` | 33168 | `~/.langcli/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md` |
| cache/vendored | `dcd4803e61e913e6…` | 33168 | `~/Pictures/ideoGram/Sora-aLt/plugins/claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md` |
| canonical-source | `6ee940a78fe22e60…` | 18874 | `~/.agent-skills/deeptutor/deeptutor-mimic/deeptutor/tutorbot/skills/skill-creator/SKILL.md` |
| canonical-source | `6ee940a78fe22e60…` | 18874 | `~/.agent-skills/deeptutor/deeptutor/tutorbot/skills/skill-creator/SKILL.md` |
| canonical-source | `da44c88f6b3845a8…` | 22047 | `~/.agent-skills/skills/.system/skill-creator/SKILL.md` |
| canonical-source | `18daa04e9fb75efa…` | 32328 | `~/.agent-skills/skills/skill-creator/SKILL.md` |
| host-runtime | `da44c88f6b3845a8…` | 22047 | `~/.codex/skills/.system/skill-creator/SKILL.md` |
| host-runtime | `ba8bebb2c0854441…` | 32370 | `~/.qwen/skills/skill-creator/SKILL.md` |
| host-runtime | `ba8bebb2c0854441…` | 32370 | `~/.qwen/superpowers/skills/skill-creator/SKILL.md` |
| project-local | `c6cf2838b100ea22…` | 8642 | `~/.config/poolside/skills/skill-creator/SKILL.md` |
| project-local | `e1b848b050004d6f…` | 23383 | `~/.desktop-commander/skills/skill-creator/SKILL.md` |
| project-local | `ba8bebb2c0854441…` | 32370 | `~/ESO/EsoMystic/extensions/supremepower/skills/skill-creator/SKILL.md` |
| project-local | `6ee940a78fe22e60…` | 18874 | `~/PYTHON_MARKETPLACE_MASTER/My-Deep-Proprietary/deeptutor-mimic/deeptutor/tutorbot/skills/skill-creator/SKILL.md` |
| project-local | `6ee940a78fe22e60…` | 18874 | `~/PYTHON_MARKETPLACE_MASTER/My-Deep-Proprietary/deeptutor/tutorbot/skills/skill-creator/SKILL.md` |
| project-local | `ba8bebb2c0854441…` | 32370 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/skill-creator/SKILL.md` |
| project-local | `ba8bebb2c0854441…` | 32370 | `~/diGiTaLdiVe/my-supremepowers/skills/skill-creator/SKILL.md` |
| project-local | `ba8bebb2c0854441…` | 32370 | `~/diGiTaLdiVe/p-market/03-plugin-dev-toolkit/skills/skill-creator/SKILL.md` |
| project-local | `8c0ce23bb87be91f…` | 11547 | `~/github/Mini-Agent/mini_agent/skills/skill-creator/SKILL.md` |
| project-local | `faf5931f553dc9f1…` | 19058 | `~/iterm2/Codex/skills/.system/skill-creator/SKILL.md` |
| project-local | `faf5931f553dc9f1…` | 19058 | `~/iterm2/Codex/skills/skill-creator/SKILL.md` |
| project-local | `ba8bebb2c0854441…` | 32370 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/skill-creator/SKILL.md` |
| project-local | `ba8bebb2c0854441…` | 32370 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/skill-creator/SKILL.md` |

## `subagent-driven-development` (skill)

- Members: **57**
- Distinct hashes: **11**
- Classifications: backup/archive=11, canonical-source=2, cache/vendored=8, host-runtime=11, project-local=25

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `3fe606f9b2f51279…` | 10742 | `~/.agent-skills-backup-2026-08-06/skills/software-development/subagent-driven-development/SKILL.md` |
| backup/archive | `9c77bfc8dbc83cef…` | 11007 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/software-development/subagent-driven-development/SKILL.md` |
| backup/archive | `d06872db6594b8c3…` | 10034 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/subagent-driven-development/SKILL.md` |
| backup/archive | `9c77bfc8dbc83cef…` | 11007 | `~/.agent-skills-backup-2026-08-18/skills/software-development/subagent-driven-development/SKILL.md` |
| backup/archive | `d06872db6594b8c3…` | 10034 | `~/.agent-skills-backup-2026-08-18/skills/subagent-driven-development/SKILL.md` |
| backup/archive | `9c77bfc8dbc83cef…` | 11007 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/software-development/subagent-driven-development/SKILL.md` |
| backup/archive | `d06872db6594b8c3…` | 10034 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/subagent-driven-development/SKILL.md` |
| backup/archive | `4c1267bfc1ea7bde…` | 9961 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/subagent-driven-development/SKILL.md` |
| backup/archive | `4c1267bfc1ea7bde…` | 9961 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-subagent-driven-development/SKILL.md` |
| backup/archive | `994b89a5d294eadd…` | 9976 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/subagent-driven-development/SKILL.md` |
| backup/archive | `4c1267bfc1ea7bde…` | 9961 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `905a2b9be59b734d…` | 12546 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `8dd1b8e698edec37…` | 32339 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `081ad3869e55c80b…` | 12139 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `724ff7f5edf539a7…` | 9809 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `ec0fd2f064b2559a…` | 10128 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/disabled/subagent-driven-development/SKILL.md` |
| cache/vendored | `faf4613f3eb45032…` | 200 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `905a2b9be59b734d…` | 12546 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/subagent-driven-development/SKILL.md` |
| cache/vendored | `905a2b9be59b734d…` | 12546 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/subagent-driven-development/SKILL.md` |
| canonical-source | `9c77bfc8dbc83cef…` | 11007 | `~/.agent-skills/skills/software-development/subagent-driven-development/SKILL.md` |
| canonical-source | `d06872db6594b8c3…` | 10034 | `~/.agent-skills/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `724ff7f5edf539a7…` | 9809 | `~/.gemini/supremepower/core/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `724ff7f5edf539a7…` | 9809 | `~/.gemini/supremepower/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `4c1267bfc1ea7bde…` | 9961 | `~/.qwen/integrations/supremepower/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `4c1267bfc1ea7bde…` | 9961 | `~/.qwen/skills/superpowers-subagent-driven-development/SKILL.md` |
| host-runtime | `994b89a5d294eadd…` | 9976 | `~/.qwen/superpowers/4.2.0/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `994b89a5d294eadd…` | 9976 | `~/.qwen/superpowers/a98c5dfc9de0/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `ec0fd2f064b2559a…` | 10128 | `~/.qwen/superpowers/skills/disabled/subagent-driven-development/SKILL.md` |
| host-runtime | `724ff7f5edf539a7…` | 9809 | `~/.qwen/superpowers/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `994b89a5d294eadd…` | 9976 | `~/iterm2/.qwen/superpowers/4.2.0/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `994b89a5d294eadd…` | 9976 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/subagent-driven-development/SKILL.md` |
| host-runtime | `724ff7f5edf539a7…` | 9809 | `~/iterm2/.qwen/superpowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `3fe606f9b2f51279…` | 10742 | `~/.hermes/skills/software-development/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `ec0fd2f064b2559a…` | 10128 | `~/ESO/EsoMystic/extensions/supremepower/skills/disabled/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/ESO/EsoMystic/extensions/supremepower/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `4c1267bfc1ea7bde…` | 9961 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/integrations/supremepower/skills/subagent-driven-development/SKILL.md` |
| project-local | `ec0fd2f064b2559a…` | 10128 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/disabled/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `4c1267bfc1ea7bde…` | 9961 | `~/diGiTaLdiVe/my-supremepowers/integrations/supremepower/skills/subagent-driven-development/SKILL.md` |
| project-local | `ec0fd2f064b2559a…` | 10128 | `~/diGiTaLdiVe/my-supremepowers/skills/disabled/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/diGiTaLdiVe/my-supremepowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `4c1267bfc1ea7bde…` | 9961 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/github/my-powers/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/github/my-powers/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/github/my-powers/superpowers/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/github/my-powers/superpowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/iterm2/Codex/superpowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/iterm2/skills/subagent-driven-development/SKILL.md` |
| project-local | `994b89a5d294eadd…` | 9976 | `~/iterm2/superpowers/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/subagent-driven-development/SKILL.md` |
| project-local | `724ff7f5edf539a7…` | 9809 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/subagent-driven-development/SKILL.md` |
| project-local | `4c1267bfc1ea7bde…` | 9961 | `~/tmp/zij3oup9_recovered/my-supremepowers/integrations/supremepower/skills/subagent-driven-development/SKILL.md` |

## `test-driven-development` (skill)

- Members: **51**
- Distinct hashes: **8**
- Classifications: backup/archive=11, canonical-source=2, cache/vendored=7, host-runtime=10, project-local=21

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `71f488c0eb8e494a…` | 19779 | `~/.agent-skills-backup-2026-08-06/skills/software-development/test-driven-development/SKILL.md` |
| backup/archive | `a580936ca6542876…` | 20075 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/software-development/test-driven-development/SKILL.md` |
| backup/archive | `9720942ee255a313…` | 9823 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/test-driven-development/SKILL.md` |
| backup/archive | `a580936ca6542876…` | 20075 | `~/.agent-skills-backup-2026-08-18/skills/software-development/test-driven-development/SKILL.md` |
| backup/archive | `9720942ee255a313…` | 9823 | `~/.agent-skills-backup-2026-08-18/skills/test-driven-development/SKILL.md` |
| backup/archive | `a580936ca6542876…` | 20075 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/software-development/test-driven-development/SKILL.md` |
| backup/archive | `9720942ee255a313…` | 9823 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/test-driven-development/SKILL.md` |
| backup/archive | `dc536a29c7c28c16…` | 10019 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/test-driven-development/SKILL.md` |
| backup/archive | `dc536a29c7c28c16…` | 10019 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-test-driven-development/SKILL.md` |
| backup/archive | `7dee67b4af6bdccc…` | 9867 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/test-driven-development/SKILL.md` |
| backup/archive | `dc536a29c7c28c16…` | 10019 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/test-driven-development/SKILL.md` |
| cache/vendored | `7dee67b4af6bdccc…` | 9867 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/test-driven-development/SKILL.md` |
| cache/vendored | `bf1b8216e523851a…` | 9015 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/test-driven-development/SKILL.md` |
| cache/vendored | `7dee67b4af6bdccc…` | 9867 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/test-driven-development/SKILL.md` |
| cache/vendored | `7dee67b4af6bdccc…` | 9867 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/test-driven-development/SKILL.md` |
| cache/vendored | `2e8c1801a6fd612c…` | 186 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/test-driven-development/SKILL.md` |
| cache/vendored | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/test-driven-development/SKILL.md` |
| cache/vendored | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/test-driven-development/SKILL.md` |
| canonical-source | `a580936ca6542876…` | 20075 | `~/.agent-skills/skills/software-development/test-driven-development/SKILL.md` |
| canonical-source | `9720942ee255a313…` | 9823 | `~/.agent-skills/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/.gemini/supremepower/core/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/.gemini/supremepower/skills/test-driven-development/SKILL.md` |
| host-runtime | `dc536a29c7c28c16…` | 10019 | `~/.qwen/integrations/supremepower/skills/test-driven-development/SKILL.md` |
| host-runtime | `dc536a29c7c28c16…` | 10019 | `~/.qwen/skills/superpowers-test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/.qwen/superpowers/4.2.0/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/.qwen/superpowers/a98c5dfc9de0/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/.qwen/superpowers/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/.qwen/superpowers/4.2.0/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/test-driven-development/SKILL.md` |
| host-runtime | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/.qwen/superpowers/skills/test-driven-development/SKILL.md` |
| project-local | `39361054f58ecc8d…` | 10306 | `~/.hermes/hermes-agent/skills/software-development/test-driven-development/SKILL.md` |
| project-local | `39361054f58ecc8d…` | 10306 | `~/.hermes/skills/software-development/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/ESO/EsoMystic/extensions/supremepower/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/Pictures/ideoGram/Sora-aLt/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/diGiTaLdiVe/my-supremepowers/skills/test-driven-development/SKILL.md` |
| project-local | `dc536a29c7c28c16…` | 10019 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/github/my-powers/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/github/my-powers/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/github/my-powers/superpowers/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/github/my-powers/superpowers/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/Codex/superpowers/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/iterm2/superpowers/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/test-driven-development/SKILL.md` |
| project-local | `7dee67b4af6bdccc…` | 9867 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/test-driven-development/SKILL.md` |

## `using-git-worktrees` (skill)

- Members: **53**
- Distinct hashes: **12**
- Classifications: backup/archive=8, canonical-source=1, cache/vendored=8, host-runtime=11, project-local=25

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `fdc71b2abf3c047f…` | 5595 | `~/.agent-skills-backup-2026-08-06/skills/using-git-worktrees/SKILL.md` |
| backup/archive | `fdc71b2abf3c047f…` | 5595 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/using-git-worktrees/SKILL.md` |
| backup/archive | `fdc71b2abf3c047f…` | 5595 | `~/.agent-skills-backup-2026-08-18/skills/using-git-worktrees/SKILL.md` |
| backup/archive | `fdc71b2abf3c047f…` | 5595 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/using-git-worktrees/SKILL.md` |
| backup/archive | `51f920de3137051d…` | 5744 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/using-git-worktrees/SKILL.md` |
| backup/archive | `51f920de3137051d…` | 5744 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-using-git-worktrees/SKILL.md` |
| backup/archive | `de9dcde34840eee0…` | 5635 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/using-git-worktrees/SKILL.md` |
| backup/archive | `51f920de3137051d…` | 5744 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `085a45ee3de432bd…` | 7983 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `8cfb86f121269e8f…` | 6813 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `de9dcde34840eee0…` | 5635 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `2a27e8e8c923b104…` | 5593 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `b9040494943885c6…` | 5788 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/disabled/using-git-worktrees/SKILL.md` |
| cache/vendored | `777ea83e5443cd0d…` | 302 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `085a45ee3de432bd…` | 7983 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/using-git-worktrees/SKILL.md` |
| cache/vendored | `085a45ee3de432bd…` | 7983 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/using-git-worktrees/SKILL.md` |
| canonical-source | `fdc71b2abf3c047f…` | 5595 | `~/.agent-skills/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `2a27e8e8c923b104…` | 5593 | `~/.gemini/supremepower/core/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `2a27e8e8c923b104…` | 5593 | `~/.gemini/supremepower/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `00cd683ec3f9ffe1…` | 5745 | `~/.qwen/integrations/supremepower/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `00cd683ec3f9ffe1…` | 5745 | `~/.qwen/skills/superpowers-using-git-worktrees/SKILL.md` |
| host-runtime | `44492e40df7e179e…` | 5636 | `~/.qwen/superpowers/4.2.0/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `44492e40df7e179e…` | 5636 | `~/.qwen/superpowers/a98c5dfc9de0/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `b9040494943885c6…` | 5788 | `~/.qwen/superpowers/skills/disabled/using-git-worktrees/SKILL.md` |
| host-runtime | `2a27e8e8c923b104…` | 5593 | `~/.qwen/superpowers/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `de9dcde34840eee0…` | 5635 | `~/iterm2/.qwen/superpowers/4.2.0/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `de9dcde34840eee0…` | 5635 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/using-git-worktrees/SKILL.md` |
| host-runtime | `4e2aeeb740335d91…` | 5592 | `~/iterm2/.qwen/superpowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `911eb6dce472f11d…` | 5787 | `~/ESO/EsoMystic/extensions/supremepower/skills/disabled/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/ESO/EsoMystic/extensions/supremepower/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `51f920de3137051d…` | 5744 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/integrations/supremepower/skills/using-git-worktrees/SKILL.md` |
| project-local | `911eb6dce472f11d…` | 5787 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/disabled/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/Pictures/ideoGram/Sora-aLt/skills/using-git-worktrees/SKILL.md` |
| project-local | `51f920de3137051d…` | 5744 | `~/diGiTaLdiVe/my-supremepowers/integrations/supremepower/skills/using-git-worktrees/SKILL.md` |
| project-local | `911eb6dce472f11d…` | 5787 | `~/diGiTaLdiVe/my-supremepowers/skills/disabled/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/diGiTaLdiVe/my-supremepowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `51f920de3137051d…` | 5744 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/github/my-powers/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/github/my-powers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/github/my-powers/superpowers/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/github/my-powers/superpowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/iterm2/Codex/superpowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/iterm2/skills/using-git-worktrees/SKILL.md` |
| project-local | `de9dcde34840eee0…` | 5635 | `~/iterm2/superpowers/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/using-git-worktrees/SKILL.md` |
| project-local | `4e2aeeb740335d91…` | 5592 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/using-git-worktrees/SKILL.md` |
| project-local | `51f920de3137051d…` | 5744 | `~/tmp/zij3oup9_recovered/my-supremepowers/integrations/supremepower/skills/using-git-worktrees/SKILL.md` |

## `verification-before-completion` (skill)

- Members: **45**
- Distinct hashes: **5**
- Classifications: backup/archive=8, canonical-source=1, cache/vendored=7, host-runtime=10, project-local=19

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `ea52d15aabaf72bc…` | 4201 | `~/.agent-skills-backup-2026-08-06/skills/verification-before-completion/SKILL.md` |
| backup/archive | `247a1b2a51db101d…` | 4564 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/verification-before-completion/SKILL.md` |
| backup/archive | `247a1b2a51db101d…` | 4564 | `~/.agent-skills-backup-2026-08-18/skills/verification-before-completion/SKILL.md` |
| backup/archive | `247a1b2a51db101d…` | 4564 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/verification-before-completion/SKILL.md` |
| backup/archive | `a89eea62cebf957a…` | 4353 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/verification-before-completion/SKILL.md` |
| backup/archive | `a89eea62cebf957a…` | 4353 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-verification-before-completion/SKILL.md` |
| backup/archive | `ea52d15aabaf72bc…` | 4201 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/verification-before-completion/SKILL.md` |
| backup/archive | `a89eea62cebf957a…` | 4353 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `ea52d15aabaf72bc…` | 4201 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `2befe7fc55bcadaa…` | 3646 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `ea52d15aabaf72bc…` | 4201 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `ea52d15aabaf72bc…` | 4201 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `c4eb60af66af1bd0…` | 346 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/verification-before-completion/SKILL.md` |
| cache/vendored | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/verification-before-completion/SKILL.md` |
| canonical-source | `247a1b2a51db101d…` | 4564 | `~/.agent-skills/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/.gemini/supremepower/core/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/.gemini/supremepower/skills/verification-before-completion/SKILL.md` |
| host-runtime | `a89eea62cebf957a…` | 4353 | `~/.qwen/integrations/supremepower/skills/verification-before-completion/SKILL.md` |
| host-runtime | `a89eea62cebf957a…` | 4353 | `~/.qwen/skills/superpowers-verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/.qwen/superpowers/4.2.0/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/.qwen/superpowers/a98c5dfc9de0/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/.qwen/superpowers/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/.qwen/superpowers/4.2.0/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/verification-before-completion/SKILL.md` |
| host-runtime | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/.qwen/superpowers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/ESO/EsoMystic/extensions/supremepower/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/Pictures/ideoGram/Sora-aLt/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/diGiTaLdiVe/my-supremepowers/skills/verification-before-completion/SKILL.md` |
| project-local | `a89eea62cebf957a…` | 4353 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/github/my-powers/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/github/my-powers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/github/my-powers/superpowers/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/github/my-powers/superpowers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/Codex/superpowers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/iterm2/superpowers/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/verification-before-completion/SKILL.md` |
| project-local | `ea52d15aabaf72bc…` | 4201 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/verification-before-completion/SKILL.md` |

## `writing-plans` (skill)

- Members: **52**
- Distinct hashes: **11**
- Classifications: backup/archive=11, canonical-source=2, cache/vendored=7, host-runtime=10, project-local=22

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `b930d5746acc1b0c…` | 7229 | `~/.agent-skills-backup-2026-08-06/skills/software-development/writing-plans/SKILL.md` |
| backup/archive | `70ce3f920387cce9…` | 7496 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/software-development/writing-plans/SKILL.md` |
| backup/archive | `2baedc777ed5fa3b…` | 7478 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/writing-plans/SKILL.md` |
| backup/archive | `70ce3f920387cce9…` | 7496 | `~/.agent-skills-backup-2026-08-18/skills/software-development/writing-plans/SKILL.md` |
| backup/archive | `2baedc777ed5fa3b…` | 7478 | `~/.agent-skills-backup-2026-08-18/skills/writing-plans/SKILL.md` |
| backup/archive | `70ce3f920387cce9…` | 7496 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/software-development/writing-plans/SKILL.md` |
| backup/archive | `2baedc777ed5fa3b…` | 7478 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/writing-plans/SKILL.md` |
| backup/archive | `2e6b93677418ff00…` | 3416 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/writing-plans/SKILL.md` |
| backup/archive | `2e6b93677418ff00…` | 3416 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-writing-plans/SKILL.md` |
| backup/archive | `2046e5b955aa16c2…` | 3264 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/writing-plans/SKILL.md` |
| backup/archive | `2e6b93677418ff00…` | 3416 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/writing-plans/SKILL.md` |
| cache/vendored | `4fd4627d2c023678…` | 6100 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/writing-plans/SKILL.md` |
| cache/vendored | `48508f44bbfd7d24…` | 7053 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/writing-plans/SKILL.md` |
| cache/vendored | `90056bad3d5f196f…` | 6046 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/writing-plans/SKILL.md` |
| cache/vendored | `2046e5b955aa16c2…` | 3264 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/writing-plans/SKILL.md` |
| cache/vendored | `634393902acba76c…` | 171 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/writing-plans/SKILL.md` |
| cache/vendored | `4fd4627d2c023678…` | 6100 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/writing-plans/SKILL.md` |
| cache/vendored | `4fd4627d2c023678…` | 6100 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/writing-plans/SKILL.md` |
| canonical-source | `70ce3f920387cce9…` | 7496 | `~/.agent-skills/skills/software-development/writing-plans/SKILL.md` |
| canonical-source | `2baedc777ed5fa3b…` | 7478 | `~/.agent-skills/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/.gemini/supremepower/core/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/.gemini/supremepower/skills/writing-plans/SKILL.md` |
| host-runtime | `2e6b93677418ff00…` | 3416 | `~/.qwen/integrations/supremepower/skills/writing-plans/SKILL.md` |
| host-runtime | `2e6b93677418ff00…` | 3416 | `~/.qwen/skills/superpowers-writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/.qwen/superpowers/4.2.0/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/.qwen/superpowers/a98c5dfc9de0/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/.qwen/superpowers/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/iterm2/.qwen/superpowers/4.2.0/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/writing-plans/SKILL.md` |
| host-runtime | `2046e5b955aa16c2…` | 3264 | `~/iterm2/.qwen/superpowers/skills/writing-plans/SKILL.md` |
| project-local | `489ffe3cd2f9003c…` | 7958 | `~/.hermes/skills/software-development/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/ESO/EsoMystic/extensions/supremepower/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/writing-plans/SKILL.md` |
| project-local | `2e6b93677418ff00…` | 3416 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/integrations/supremepower/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/writing-plans/SKILL.md` |
| project-local | `2e6b93677418ff00…` | 3416 | `~/diGiTaLdiVe/my-supremepowers/integrations/supremepower/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/diGiTaLdiVe/my-supremepowers/skills/writing-plans/SKILL.md` |
| project-local | `2e6b93677418ff00…` | 3416 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/github/my-powers/core/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/github/my-powers/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/github/my-powers/superpowers/core/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/github/my-powers/superpowers/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/iterm2/Codex/superpowers/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/iterm2/skills/writing-plans/SKILL.md` |
| project-local | `8a9198d4d9efbcad…` | 3266 | `~/iterm2/superpowers/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/writing-plans/SKILL.md` |
| project-local | `2046e5b955aa16c2…` | 3264 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/writing-plans/SKILL.md` |
| project-local | `2e6b93677418ff00…` | 3416 | `~/tmp/zij3oup9_recovered/my-supremepowers/integrations/supremepower/skills/writing-plans/SKILL.md` |

## `writing-skills` (skill)

- Members: **52**
- Distinct hashes: **8**
- Classifications: backup/archive=8, canonical-source=1, cache/vendored=8, host-runtime=11, project-local=24

Assessment: name-only collision; content differs and must be reviewed as separate variants.

| Classification | SHA-256 | Bytes | Path |
|---|---|---:|---|
| backup/archive | `934cd0dfd9ece2da…` | 22444 | `~/.agent-skills-backup-2026-08-06/skills/writing-skills/SKILL.md` |
| backup/archive | `934cd0dfd9ece2da…` | 22444 | `~/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/writing-skills/SKILL.md` |
| backup/archive | `934cd0dfd9ece2da…` | 22444 | `~/.agent-skills-backup-2026-08-18/skills/writing-skills/SKILL.md` |
| backup/archive | `934cd0dfd9ece2da…` | 22444 | `~/.agent-skills/backups/agent-skills-20260815-024526/skills/writing-skills/SKILL.md` |
| backup/archive | `c063183c113b79d5…` | 22628 | `~/.gemini/backups/re-ole-20260415/.qwen/integrations/supremepower/skills/writing-skills/SKILL.md` |
| backup/archive | `c063183c113b79d5…` | 22628 | `~/.gemini/backups/re-ole-20260415/.qwen/skills/superpowers-writing-skills/SKILL.md` |
| backup/archive | `d83a09d6a1c6976f…` | 22465 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/4.2.0/skills/writing-skills/SKILL.md` |
| backup/archive | `c063183c113b79d5…` | 22628 | `~/.gemini/backups/re-ole-20260415/.qwen/superpowers/skills/writing-skills/SKILL.md` |
| cache/vendored | `38ba648975ae6ba5…` | 22624 | `~/.codex/.tmp/plugins/plugins/superpowers/skills/writing-skills/SKILL.md` |
| cache/vendored | `d34db5c8aed6a4e0…` | 26360 | `~/.codex/plugins/cache/openai-curated-remote/superpowers/6.3.0/skills/writing-skills/SKILL.md` |
| cache/vendored | `38ba648975ae6ba5…` | 22624 | `~/.cursor/plugins/cache/cursor-public/superpowers/b7a8f76985f1e93e75dd2f2a3b424dc731bd9d37/skills/writing-skills/SKILL.md` |
| cache/vendored | `6ffe287552c1ca9c…` | 22463 | `~/.gemini/antigravity-cli/plugins/supremepower/core/skills/writing-skills/SKILL.md` |
| cache/vendored | `99e51d55dbe282e2…` | 22623 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/disabled/writing-skills/SKILL.md` |
| cache/vendored | `5858213d0e11e76c…` | 186 | `~/.gemini/antigravity-cli/plugins/supremepower/skills/writing-skills/SKILL.md` |
| cache/vendored | `38ba648975ae6ba5…` | 22624 | `~/iterm2/.claude/plugins/claude-plugins-official/superpowers/5.1.0/skills/writing-skills/SKILL.md` |
| cache/vendored | `38ba648975ae6ba5…` | 22624 | `~/iterm2/Codex/.tmp/plugins/plugins/superpowers/skills/writing-skills/SKILL.md` |
| canonical-source | `934cd0dfd9ece2da…` | 22444 | `~/.agent-skills/skills/writing-skills/SKILL.md` |
| host-runtime | `6ffe287552c1ca9c…` | 22463 | `~/.gemini/supremepower/core/skills/writing-skills/SKILL.md` |
| host-runtime | `6ffe287552c1ca9c…` | 22463 | `~/.gemini/supremepower/skills/writing-skills/SKILL.md` |
| host-runtime | `c063183c113b79d5…` | 22628 | `~/.qwen/integrations/supremepower/skills/writing-skills/SKILL.md` |
| host-runtime | `c063183c113b79d5…` | 22628 | `~/.qwen/skills/superpowers-writing-skills/SKILL.md` |
| host-runtime | `d83a09d6a1c6976f…` | 22465 | `~/.qwen/superpowers/4.2.0/skills/writing-skills/SKILL.md` |
| host-runtime | `d83a09d6a1c6976f…` | 22465 | `~/.qwen/superpowers/a98c5dfc9de0/skills/writing-skills/SKILL.md` |
| host-runtime | `99e51d55dbe282e2…` | 22623 | `~/.qwen/superpowers/skills/disabled/writing-skills/SKILL.md` |
| host-runtime | `6ffe287552c1ca9c…` | 22463 | `~/.qwen/superpowers/skills/writing-skills/SKILL.md` |
| host-runtime | `d83a09d6a1c6976f…` | 22465 | `~/iterm2/.qwen/superpowers/4.2.0/skills/writing-skills/SKILL.md` |
| host-runtime | `d83a09d6a1c6976f…` | 22465 | `~/iterm2/.qwen/superpowers/a98c5dfc9de0/skills/writing-skills/SKILL.md` |
| host-runtime | `6ffe287552c1ca9c…` | 22463 | `~/iterm2/.qwen/superpowers/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/ESO/EsoMystic/extensions/supremepower/core/skills/writing-skills/SKILL.md` |
| project-local | `99e51d55dbe282e2…` | 22623 | `~/ESO/EsoMystic/extensions/supremepower/skills/disabled/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/ESO/EsoMystic/extensions/supremepower/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/core/skills/writing-skills/SKILL.md` |
| project-local | `c063183c113b79d5…` | 22628 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/integrations/supremepower/skills/writing-skills/SKILL.md` |
| project-local | `99e51d55dbe282e2…` | 22623 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/disabled/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/core/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/PYTHON_MARKETPLACE_MASTER/SupremePowers/superpowers/skills/writing-skills/SKILL.md` |
| project-local | `c063183c113b79d5…` | 22628 | `~/diGiTaLdiVe/my-supremepowers/integrations/supremepower/skills/writing-skills/SKILL.md` |
| project-local | `99e51d55dbe282e2…` | 22623 | `~/diGiTaLdiVe/my-supremepowers/skills/disabled/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/diGiTaLdiVe/my-supremepowers/skills/writing-skills/SKILL.md` |
| project-local | `c063183c113b79d5…` | 22628 | `~/diGiTaLdiVe/p-market/01-devflow-pro/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/github/my-powers/core/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/github/my-powers/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/github/my-powers/superpowers/core/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/github/my-powers/superpowers/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/iterm2/Codex/superpowers/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/iterm2/skills/writing-skills/SKILL.md` |
| project-local | `d83a09d6a1c6976f…` | 22465 | `~/iterm2/superpowers/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/tmp/zij3oup9_recovered/my-supremepowers/core/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/core/skills/writing-skills/SKILL.md` |
| project-local | `6ffe287552c1ca9c…` | 22463 | `~/tmp/zij3oup9_recovered/my-supremepowers/extensions/supremepower/skills/writing-skills/SKILL.md` |
| project-local | `c063183c113b79d5…` | 22628 | `~/tmp/zij3oup9_recovered/my-supremepowers/integrations/supremepower/skills/writing-skills/SKILL.md` |

## Recommended handling

1. Consolidate only exact-hash canonical/projection/archive groups after checking symlink ownership.
2. For name-only collisions, select a canonical variant based on source quality and current behavior; do not overwrite automatically.
3. Keep project-local variants unless explicitly promoted or retired.
4. Re-run projection health after any promotion or retirement.
