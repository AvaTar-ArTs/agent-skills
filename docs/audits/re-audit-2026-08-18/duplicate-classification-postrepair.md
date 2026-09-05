# Duplicate Classification — 2026-08-18 post-repair

This report distinguishes a metadata/name collision from an identical-content duplicate. A same-name group is not a deletion recommendation: members may be canonical, projected, cached, archived, or project-local variants.

## Counts

- Skill same-name groups: **1836**
- Agent same-name groups: **450**
- Exact skill-content groups: **2162**
- Exact agent-content groups: **810**

## Interpretation

- Name-only: same declared frontmatter name, but content and/or provenance may differ. Keep separate until behavior, source, and lifecycle are reviewed.
- Exact-content: same SHA-256 file content. These are candidates for projection consolidation only when provenance and runtime ownership agree.
- Neither category authorizes deleting project-local, plugin-managed, backup, or compatibility copies.

## Representative same-name groups

| Kind | Name | Members | Example paths |
|---|---|---:|---|
| skill | `imagegen` | 6 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/.system/imagegen/SKILL.md<br>/Users/steven/.agent-skills/skills/.system/imagegen/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/.system/imagegen/SKILL.md |
| skill | `openai-docs` | 6 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/.system/openai-docs/SKILL.md<br>/Users/steven/.agent-skills/skills/.system/openai-docs/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/.system/openai-docs/SKILL.md |
| skill | `plugin-creator` | 8 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/.system/plugin-creator/SKILL.md<br>/Users/steven/.agent-skills/skills/.system/plugin-creator/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/.system/plugin-creator/SKILL.md |
| skill | `skill-creator` | 37 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/.system/skill-creator/SKILL.md<br>/Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/skill-creator/SKILL.md<br>/Users/steven/.agent-skills/deeptutor/deeptutor/tutorbot/skills/skill-creator/SKILL.md |
| skill | `skill-installer` | 13 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/.system/skill-installer/SKILL.md<br>/Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/skill-installer/SKILL.md<br>/Users/steven/.agent-skills/skills/.system/skill-installer/SKILL.md |
| skill | `agent-creation-guidance` | 13 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/agent-creation-guidance/SKILL.md<br>/Users/steven/.agent-skills/skills/agent-creation-guidance/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/agent-creation-guidance/SKILL.md |
| skill | `agent-development` | 24 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/agent-development/SKILL.md<br>/Users/steven/.agent-skills/skills/agent-development/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/agent-development/SKILL.md |
| skill | `agmsg` | 6 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/agmsg/SKILL.md<br>/Users/steven/.agent-skills/skills/agmsg/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/agmsg/SKILL.md |
| skill | `ai-video-generation` | 4 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/ai-video-generation/SKILL.md<br>/Users/steven/.agent-skills/skills/ai-video-generation/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/ai-video-generation/SKILL.md |
| skill | `apple` | 5 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/apple/SKILL.md<br>/Users/steven/.agent-skills/skills/apple/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/apple/SKILL.md |
| skill | `apple-notes` | 7 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/apple/apple-notes/SKILL.md<br>/Users/steven/.agent-skills/skills/apple/apple-notes/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/apple/apple-notes/SKILL.md |
| skill | `apple-reminders` | 7 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/apple/apple-reminders/SKILL.md<br>/Users/steven/.agent-skills/skills/apple/apple-reminders/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/apple/apple-reminders/SKILL.md |
| skill | `findmy` | 7 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/apple/findmy/SKILL.md<br>/Users/steven/.agent-skills/skills/apple/findmy/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/apple/findmy/SKILL.md |
| skill | `imessage` | 7 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/apple/imessage/SKILL.md<br>/Users/steven/.agent-skills/skills/apple/imessage/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/apple/imessage/SKILL.md |
| skill | `macos-computer-use` | 6 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/apple/macos-computer-use/SKILL.md<br>/Users/steven/.agent-skills/skills/apple/macos-computer-use/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/apple/macos-computer-use/SKILL.md |
| skill | `ask-matt` | 4 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/ask-matt/SKILL.md<br>/Users/steven/.agent-skills/skills/ask-matt/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/ask-matt/SKILL.md |
| skill | `audiocraft-audio-generation` | 10 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/audiocraft-audio-generation/SKILL.md<br>/Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/mlops/models/audiocraft/SKILL.md<br>/Users/steven/.agent-skills/skills/audiocraft-audio-generation/SKILL.md |
| skill | `automation-recommender` | 14 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/automation-recommender/SKILL.md<br>/Users/steven/.agent-skills/skills/automation-recommender/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/automation-recommender/SKILL.md |
| skill | `claude-code` | 11 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/autonomous-ai-agents/claude-code/SKILL.md<br>/Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/claude-code/SKILL.md<br>/Users/steven/.agent-skills/skills/autonomous-ai-agents/claude-code/SKILL.md |
| skill | `codex` | 11 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/autonomous-ai-agents/codex/SKILL.md<br>/Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/codex/SKILL.md<br>/Users/steven/.agent-skills/skills/autonomous-ai-agents/codex/SKILL.md |
| skill | `ecosystem-layering` | 6 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/autonomous-ai-agents/ecosystem-layering/SKILL.md<br>/Users/steven/.agent-skills/skills/autonomous-ai-agents/ecosystem-layering/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/autonomous-ai-agents/ecosystem-layering/SKILL.md |
| skill | `hermes-agent` | 7 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/autonomous-ai-agents/hermes-agent/SKILL.md<br>/Users/steven/.agent-skills/skills/autonomous-ai-agents/hermes-agent/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/autonomous-ai-agents/hermes-agent/SKILL.md |
| skill | `opencode` | 7 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/autonomous-ai-agents/opencode/SKILL.md<br>/Users/steven/.agent-skills/skills/autonomous-ai-agents/opencode/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/autonomous-ai-agents/opencode/SKILL.md |
| skill | `axolotl` | 4 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/axolotl/SKILL.md<br>/Users/steven/.agent-skills/skills/axolotl/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/axolotl/SKILL.md |
| skill | `belt` | 4 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/belt/SKILL.md<br>/Users/steven/.agent-skills/skills/belt/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/belt/SKILL.md |
| skill | `blackbox` | 4 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/blackbox/SKILL.md<br>/Users/steven/.agent-skills/skills/blackbox/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-18/backups/agent-skills-20260815-024526/skills/blackbox/SKILL.md |
| skill | `brainstorm` | 6 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/brainstorm/SKILL.md<br>/Users/steven/.agent-skills/skills/brainstorm/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/brainstorm/SKILL.md |
| skill | `brainstorming` | 47 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/brainstorming/SKILL.md<br>/Users/steven/.agent-skills/skills/brainstorming/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/brainstorming/SKILL.md |
| skill | `build-mcp-app` | 22 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/build-mcp-app/SKILL.md<br>/Users/steven/.agent-skills/skills/build-mcp-app/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/build-mcp-app/SKILL.md |
| skill | `build-mcp-server` | 22 | /Users/steven/.agent-skills/backups/agent-skills-20260815-024526/skills/build-mcp-server/SKILL.md<br>/Users/steven/.agent-skills/skills/build-mcp-server/SKILL.md<br>/Users/steven/.agent-skills-backup-2026-08-06/skills/build-mcp-server/SKILL.md |

Complete machine-readable membership:
- `name-duplicate-groups.csv`
- `exact-duplicate-groups.csv`
- `home-capability-index-postrepair.json`
- `control-plane-postrepair/deduplication.json`
