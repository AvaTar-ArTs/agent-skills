# Three-Way Audit: ~/.agents, ~/.Agent-skills, GitHub AvaTar-ArTs/.agents

Generated: 2026-07-12T11:38:08
GitHub snapshot: `9d0849a Add repository README`

## Scope
- `local_agents`: `/Users/steven/.agents`
- `active_agent_skills`: `/Users/steven/.agent-skills`
- `github_agents`: `/Users/steven/.agent-skills/tmp/github-avatar-arts-dot-agents`
- Active comparison excludes: `.codex-history, .git, tmp, tmp-csv, tmp-md`
- GitHub comparison excludes: `plugins`
- Outputs are stored in the workspace `tmp/` folder, not `/private/tmp`.
- No source tree was modified.

## File Counts
- `local_agents`: 1024 files, 398 dirs
- `active_agent_skills`: 1089 files, 388 dirs
- `github_agents`: 1052 files, 370 dirs

## Presence Counts
Legend: L=local `~/.agents`, A=active `~/.Agent-skills`, G=GitHub clone with `plugins/` excluded.
- `A`: 39
- `AG`: 87
- `L`: 56
- `LA`: 3
- `LAG`: 960
- `LG`: 5

## Decision Summary
- Active `.Agent-skills` remains the better runtime base for Codex.
- Local `~/.agents` contributes a small set of absent registry/docs and nested `agent.md` variants worth cherry-picking.
- GitHub adds almost nothing non-plugin that is not already represented locally or in active `.Agent-skills`: only a tiny non-plugin candidate set remains after excluding `plugins/`.

## Highest-Priority Promotion Candidates
- `agents/AGENT_NORMALIZATION_REGISTRY.md`
- `agents/REGISTRY.md`
- `agents/SUBAGENTS_GUIDE.md`
- `agents/SUBAGENT_QUICK_REFERENCE.md`
- `agents/api-specialist/agent.md`
- `agents/backend-architect/agent.md`
- `agents/database-specialist/agent.md`
- `agents/devops-engineer/agent.md`
- `agents/frontend-architect/agent.md`
- `agents/javascript-expert/agent.md`
- `agents/performance-engineer/agent.md`
- `agents/python-expert/agent.md`
- `agents/security-engineer/agent.md`
- `agents/system-architect/agent.md`
- `agents/technical-writer/agent.md`
- `agents/testing-specialist/agent.md`
- `agents/find-docs/SKILL.md`

## Local ~/.agents Candidates Not Active
- `agents/.gitkeep`
- `agents/AGENT_NORMALIZATION_REGISTRY.md`
- `agents/REGISTRY.md`
- `agents/SUBAGENTS_GUIDE.md`
- `agents/SUBAGENT_QUICK_REFERENCE.md`
- `agents/api-specialist/agent.md`
- `agents/backend-architect/agent.md`
- `agents/context-management/agent.md`
- `agents/database-specialist/agent.md`
- `agents/devops-engineer/agent.md`
- `agents/ecosystem-learning/agent.md`
- `agents/ecosystem-synergy/agent.md`
- `agents/find-docs/SKILL.md`
- `agents/frontend-architect/agent.md`
- `agents/ice-tracker-assistant/agent.md`
- `agents/integrated-evolution/agent.md`
- `agents/javascript-expert/agent.md`
- `agents/performance-engineer/agent.md`
- `agents/python-expert/agent.md`
- `agents/security-engineer/agent.md`
- `agents/self-evolution/agent.md`
- `agents/self-evolution-plan.md`
- `agents/system-architect/agent.md`
- `agents/task-management/agent.md`
- `agents/technical-writer/agent.md`
- `agents/testing-specialist/agent.md`
- `skills/agmsg/.agmsg`
- `skills/agmsg/db/config.yaml`

## GitHub Candidates Not Active, plugins/ Excluded
- `skills/agmsg/.agmsg`
- `skills/agmsg/db/config.yaml`

## Repo-Only Buckets, plugins/ Excluded
- `skills`: 2

## Same-Path Differences
- Local `.agents` vs active same-path differences: 94
- GitHub vs active same-path differences: 2

## Avoid / Do Not Promote
- `agents/workspace-ecosystem-audit-data/*`: generated historical audit data; useful as evidence, not active runtime config.
- `skills/agmsg/db/*`: runtime DB artifacts; do not copy into active skill source.
- `.DS_Store`: Finder metadata.
- `plugins/*`: explicitly out of scope per your correction.

Full JSON: `/Users/steven/.agent-skills/tmp/agents_three_way_audit.json`
