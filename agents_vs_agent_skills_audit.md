# ~/.agents vs ~/.Agent-skills Audit

Generated: 2026-07-12T11:32:00

## Scope
- Source/reference tree: `/Users/steven/.agents`
- Active comparison tree: `/Users/steven/.agent-skills`
- Method: full file traversal, SHA-256 content hashes, relative path comparison, moved-file detection by hash, and metadata/content heuristics for text frontmatter.
- No files were modified.

## Counts
- agents_files: 1024
- agents_dirs: 398
- active_files: 1138
- active_dirs: 415
- same_rel_identical: 869
- same_rel_different: 94
- agents_only: 61
- agents_only_duplicate_elsewhere_in_active: 13
- agents_only_unique: 48
- active_only: 175
- active_only_duplicate_elsewhere_in_agents: 37
- active_only_unique: 138

## High-Level Finding
`~/.agents` is mostly a reference/source tree now. `~/.Agent-skills` is generally more organized and more complete, especially for active Codex use. The useful work is selective cherry-picking, not wholesale replacement.

## Best Candidates From ~/.agents Not Present In ~/.Agent-skills
These are unique by content and not obvious runtime/state or stale audit files.
- `agents/AGENT_NORMALIZATION_REGISTRY.md`
- `agents/REGISTRY.md`
- `agents/SUBAGENTS_GUIDE.md`
- `agents/SUBAGENT_QUICK_REFERENCE.md`
- `agents/backend-architect/agent.md`
- `agents/database-specialist/agent.md`
- `agents/devops-engineer/agent.md`
- `agents/find-docs/SKILL.md`
- `agents/frontend-architect/agent.md`
- `agents/javascript-expert/agent.md`
- `agents/performance-engineer/agent.md`
- `agents/python-expert/agent.md`
- `agents/security-engineer/agent.md`
- `agents/self-evolution-plan.md`
- `agents/system-architect/agent.md`
- `agents/technical-writer/agent.md`
- `agents/testing-specialist/agent.md`
- `skills/agmsg/db/config.yaml`

## Outdated Or Lower-Priority ~/.agents Material
Same relative path exists in both trees, but active `.Agent-skills` is newer or content differs in the active direction.
- `agents/.DS_Store`: active newer; size delta agents-active=10240
- `skills/workspace-ecosystem-audit/SKILL.md`: active newer; size delta agents-active=-164
- `agents/devops-automator.md`: active newer; size delta agents-active=1309
- `agents/frontend-developer.md`: active newer; size delta agents-active=1335
- `agents/date-checker.md`: active newer; size delta agents-active=980
- `agents/skill-installer/SKILL.md`: active newer; size delta agents-active=-17
- `agents/iterm2-ecosystem-dev.md`: active newer; size delta agents-active=2563
- `agents/skill-porter/simple-claude-skill/SKILL.md`: active newer; size delta agents-active=-12
- `agents/skill-porter/README.md`: active newer; size delta agents-active=-9
- `agents/skill-porter/api-connector-gemini/GEMINI.md`: active newer; size delta agents-active=-11
- `agents/skill-porter/before-after/code-formatter-converted/GEMINI.md`: active newer; size delta agents-active=-11
- `agents/skill-porter/before-after/code-formatter-converted/SKILL.md`: active newer; size delta agents-active=-12
- `agents/skill-porter/before-after/api-connector-converted/GEMINI.md`: active newer; size delta agents-active=-11
- `agents/skill-porter/before-after/api-connector-converted/SKILL.md`: active newer; size delta agents-active=-12
- `agents/context-fetcher.md`: active newer; size delta agents-active=1109
- `agents/skill-creator/SKILL.md`: active newer; size delta agents-active=-9
- `agents/ai-engineer.md`: active newer; size delta agents-active=1327
- `agents/rapid-prototyper.md`: active newer; size delta agents-active=1854
- `agents/skill-creator/references/openai_yaml.md`: active newer; size delta agents-active=-5
- `agents/file-creator.md`: active newer; size delta agents-active=1095
- `agents/git-workflow.md`: active newer; size delta agents-active=1136
- `agents/test-writer-fixer.md`: active newer; size delta agents-active=2562
- `agents/knowledge-fetcher.md`: active newer; size delta agents-active=1142
- `agents/studio-coach.md`: active newer; size delta agents-active=1835
- `agents/documentation/agent.md`: active newer; size delta agents-active=-5
- `agents/api-specialist.md`: active newer; size delta agents-active=938
- `agents/agent-creation-guidance.md`: active newer; size delta agents-active=128
- `agents/ai-music-video-creator.md`: active newer; size delta agents-active=236
- `agents/ai-workflow-manager.md`: active newer; size delta agents-active=119
- `agents/ai-xeo.md`: active newer; size delta agents-active=89
- `agents/avatararts-organizer.md`: active newer; size delta agents-active=98
- `agents/backend-architect.md`: active newer; size delta agents-active=351
- `agents/capability-atlas.md`: active newer; size delta agents-active=1322
- `agents/code-reviewer.md`: active newer; size delta agents-active=1645
- `agents/content-consolidator.md`: active newer; size delta agents-active=105
- `agents/content-organizer.md`: active newer; size delta agents-active=254
- `agents/context-handoff-compiler.md`: active newer; size delta agents-active=1633
- `agents/context-management.md`: active newer; size delta agents-active=-155
- `agents/database-specialist.md`: active newer; size delta agents-active=282
- `agents/devops-engineer.md`: active newer; size delta agents-active=349
- `agents/documentation-management.md`: active newer; size delta agents-active=20
- `agents/ecosystem-analyzer.md`: active newer; size delta agents-active=261
- `agents/ecosystem-learning.md`: active newer; size delta agents-active=-155
- `agents/ecosystem-synergy.md`: active newer; size delta agents-active=-152
- `agents/filesystem-inventory.md`: active newer; size delta agents-active=152
- `agents/frontend-architect.md`: active newer; size delta agents-active=336
- `agents/ice-tracker-assistant.md`: active newer; size delta agents-active=-142
- `agents/integrated-evolution.md`: active newer; size delta agents-active=-161
- `agents/javascript-expert.md`: active newer; size delta agents-active=338
- `agents/knowledge-automation-strategist.md`: active newer; size delta agents-active=276
- `agents/notebooklm-enhancement-advisor.md`: active newer; size delta agents-active=1714
- `agents/path-list-analyzer.md`: active newer; size delta agents-active=185
- `agents/performance-engineer.md`: active newer; size delta agents-active=312
- `agents/project-launch-manager.md`: active newer; size delta agents-active=271
- `agents/python-expert.md`: active newer; size delta agents-active=300
- `agents/revenue-optimizer.md`: active newer; size delta agents-active=119
- `agents/security-engineer.md`: active newer; size delta agents-active=320
- `agents/self-evolution.md`: active newer; size delta agents-active=-143
- `agents/seo-keyword-analyst.md`: active newer; size delta agents-active=151
- `agents/system-analyzer.md`: active newer; size delta agents-active=231
- `agents/system-architect.md`: active newer; size delta agents-active=347
- `agents/task-management.md`: active newer; size delta agents-active=-146
- `agents/technical-writer.md`: active newer; size delta agents-active=307
- `agents/testing-specialist.md`: active newer; size delta agents-active=329
- `agents/tree-explorer.md`: active newer; size delta agents-active=269
- `agents/workflow-orchestrator.md`: active newer; size delta agents-active=2525
- `agents/xeo-strategist.md`: active newer; size delta agents-active=101
- `agents/ux-researcher.md`: active newer; size delta agents-active=1790
- `agents/visual-storyteller.md`: active newer; size delta agents-active=1785
- `agents/support-responder.md`: active newer; size delta agents-active=1765
- `agents/brand-guardian.md`: active newer; size delta agents-active=1720
- `agents/app-store-optimizer.md`: active newer; size delta agents-active=1711
- `agents/api-tester.md`: active newer; size delta agents-active=1725
- `agents/performance-benchmarker.md`: active newer; size delta agents-active=1744
- `agents/test-results-analyzer.md`: active newer; size delta agents-active=1667
- `agents/finance-tracker.md`: active newer; size delta agents-active=1745
- `agents/infrastructure-maintainer.md`: active newer; size delta agents-active=1778
- `agents/workflow-optimizer.md`: active newer; size delta agents-active=1670
- `agents/legal-compliance-checker.md`: active newer; size delta agents-active=1756
- `agents/analytics-reporter.md`: active newer; size delta agents-active=1804
- ... 12 more in JSON

## ~/.agents Files Already Present Elsewhere In ~/.Agent-skills
These are not missing; they appear to have been relocated/reorganized in the active tree.
- `agents/.gitkeep` -> `skills/creative/pixel-art/scripts/__init__.py, skills/creative/structured-asset-pipeline/scripts/common/__init__.py, skills/creative/structured-asset-pipeline/tests/__init__.py`
- `agents/api-specialist/agent.md` -> `agents/api-specialist.md`
- `agents/context-management/agent.md` -> `agents/5-misc-personal/context-management.md`
- `agents/ecosystem-learning/agent.md` -> `agents/5-misc-personal/ecosystem-learning.md`
- `agents/ecosystem-synergy/agent.md` -> `agents/5-misc-personal/ecosystem-synergy.md`
- `agents/ice-tracker-assistant/agent.md` -> `agents/5-misc-personal/ice-tracker-assistant.md`
- `agents/integrated-evolution/agent.md` -> `agents/5-misc-personal/integrated-evolution.md`
- `agents/self-evolution/agent.md` -> `agents/5-misc-personal/self-evolution.md`
- `agents/task-management/agent.md` -> `agents/5-misc-personal/task-management.md`
- `agents/workspace-ecosystem-audit-data/docs-07-09-21:01.csv` -> `skills/workspace-ecosystem-audit/references/workspace-ecosystem-audit-data-docs.csv`
- `agents/workspace-ecosystem-audit-data/enriched-workspace-ecosystem-audit-data.csv` -> `skills/workspace-ecosystem-audit/references/workspace-ecosystem-audit-data-index.csv`
- `skills/agmsg/.agmsg` -> `skills/creative/pixel-art/scripts/__init__.py, skills/creative/structured-asset-pipeline/scripts/common/__init__.py, skills/creative/structured-asset-pipeline/tests/__init__.py`
- `skills/agmsg/db/messages.db-wal` -> `skills/creative/pixel-art/scripts/__init__.py, skills/creative/structured-asset-pipeline/scripts/common/__init__.py, skills/creative/structured-asset-pipeline/tests/__init__.py`

## Unique ~/.agents Buckets
- `agents`: 44
- `skills`: 4

## Notes
- `agents/workspace-ecosystem-audit-data/` in `.agents` contains large generated CSV/JSON/DB-style audit outputs. Treat as historical evidence, not active runtime material.
- `skills/agmsg/db/*` in `.agents` contains live-ish message DB artifacts. Do not copy into `.Agent-skills`; active writable DB roots are managed elsewhere.
- `.DS_Store` files are ignored for promotion decisions.
- `~/.agent-skills` is the canonical local workspace; legacy audits may mention differently cased paths.

Full machine-readable report: `/private/tmp/agents_vs_agent_skills_audit.json`
