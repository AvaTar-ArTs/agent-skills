# my-supremepowers Consolidation

Date: 2026-07-15

`/Users/steven/.agent-skills` is the sole active runtime repository.
`/Users/steven/my-supremepowers` is retained as a historical/upstream lab, not
as a runtime dependency.

## Consolidated into `.agent-skills`

- Replaced the external `skills/design-taste-frontend` symlink with a local
  vendored directory.
- Imported unique candidate skills:
  - `skills/brainstorm`
  - `skills/cua-driver`
  - `skills/find-docs`
  - `skills/tooluniverse`
- Corrected `skills/autonomous-ai-agents/claude-code` from the upstream
  Claude Code version so OpenAI Codex remains under
  `skills/autonomous-ai-agents/codex`.

## Deliberately not imported wholesale

`my-supremepowers` has many disabled copies, dirty worktree deletions, old
absolute paths, and duplicate skill identities. Bulk sync would reintroduce
stale runtime material. Future imports should be reviewed skill-by-skill.

## Runtime rule

Runtime links and source references should point at:

```text
/Users/steven/.agent-skills
```

Do not add runtime symlinks back to `~/my-supremepowers`.
