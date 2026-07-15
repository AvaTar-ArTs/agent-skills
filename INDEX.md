# ~/.agent-skills - Current Runtime Index

Last audited: 2026-07-15.

This tree is the canonical local source for reusable agents and skills. The
legacy `/Users/steven/.agents` path is maintained as a compatibility symlink to
this directory; new runtime configuration should point directly at
`/Users/steven/.agent-skills`.

## At a Glance

| Area | Current count | Notes |
|------|---------------|-------|
| `agents/` root files | 108 | Non-hidden files directly under `agents/` |
| `agents/` all files | 221 | Non-hidden files under all agent subdirectories |
| `skills/` top-level directories | 92 | Non-hidden dirs; hidden `.system/` also present, plus one top-level symlink |
| Direct/root-visible skills | 74 | `SKILL.md` files within depth 2 |
| Local expanded skills | 181 | All local `SKILL.md` files |
| Symlink-followed runtime-visible skills | 182 | Includes linked/reference-visible skill material |

## Runtime Links

Claude and Codex should resolve through the canonical `.agent-skills` tree:

```text
/Users/steven/.agents -> /Users/steven/.agent-skills
/Users/steven/.claude/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.claude/skills -> /Users/steven/.agent-skills/skills
/Users/steven/.codex/agents -> /Users/steven/.agent-skills/agents
/Users/steven/.codex/superpowers -> /Users/steven/.agent-skills/skills/using-superpowers
```

Codex note: `/Users/steven/.codex/skills` is an existing managed directory with
system skills, not a symlink to this tree.

## Operating Notes

- Use `/Users/steven/.agent-skills` as the canonical path in new configuration.
- Keep `/Users/steven/.agents` only as a compatibility alias for older tools.
- Treat `skills/.system/` and `skills/skill-porter-examples/` as vendored/reference
  material; their duplicate skill names are intentional unless promoted.
- Treat root `agents/*.md` files as the runtime primary surface when matching by
  filename; categorized `agents/<group>/*.md` copies are retained for organization.
- Preserve local history and generated reports unless cleanup is explicitly
  requested.
- Put temporary generated outputs under `tmp/`, `tmp-csv/`, or `tmp-md/`.
- Treat cache, session, credential, and runtime-state paths as non-importable.

## Useful Entry Points

- `skills/using-superpowers/SKILL.md` - process authority for SupremePower /
  using-superpowers requests.
- `skills/ecosystem-intelligence/SKILL.md` - ecosystem audit and topology work.
- `skills/cross-tool-memory/SKILL.md` - shared memory bridge workflows.
- `skills/agmsg/SKILL.md` - cross-agent messaging workflows.
