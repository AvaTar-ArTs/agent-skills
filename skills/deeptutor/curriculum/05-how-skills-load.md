# How Skills Load

Understanding skill discovery and loading is key to debugging why a skill does or doesn't activate.

## The loading chain

```
User request
    ↓
Host (Desktop Commander / Hermes / Claude / Cursor)
    ↓
Skill discovery: scan skills directories
    ↓
Match: compare request against skill descriptions
    ↓
Load: inject SKILL.md into AI context
    ↓
Execute: AI follows skill instructions
```

## Discovery paths

Different hosts discover skills from different locations:

| Host | Skills path | Mechanism |
|------|-------------|-----------|
| Desktop Commander | `~/.agents/skills/` | Direct scan |
| Hermes | `~/.hermes/skills/` | Projected + cached |
| Claude Code | `~/.claude/skills/` | Symlink doors |
| Cursor | `~/.cursor/skills/` | Real copies (drifts!) |

## The canonical library

Your **canonical** skill library is:
```
~/.agent-skills/skills/    (330 directories, 580 skills after cleanup)
```

Other paths are **projections** or **copies** of this canonical source.

## How matching works

When you ask the AI to do something, it checks your request against every skill's `description` field:

```
User: "create a new skill for invoice generation"
    ↓
Match found: skill-creator (description mentions "create a new skill")
    ↓
Load: ~/.agent-skills/skills/skill-creator/SKILL.md
    ↓
AI follows the skill's instructions
```

## Why skills sometimes don't load

1. **Description doesn't match** — the trigger words don't align with your request
2. **Skill is in a nested subdirectory** — some hosts only scan top-level
3. **Broken symlink** — the active-skills projection has a dangling link
4. **Host drift** — Cursor copies skills but doesn't keep them synced

## Try it yourself

```bash
# See what Desktop Commander sees
ls ~/.agents/skills/ | wc -l

# Compare with canonical
ls ~/.agent-skills/skills/ | wc -l

# Check for broken links in active-skills
find ~/.agent-skills/active-skills -type l ! -exec test -e {} \; -print
```

## Next

→ [06: Active-Skills Projection](06-active-skills-projection.md)
