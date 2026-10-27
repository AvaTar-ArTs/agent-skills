# Skill Anatomy

Every skill follows the same structure. Let's dissect a real one.

## The frontmatter

Every `SKILL.md` starts with YAML frontmatter:

```yaml
---
name: run-agent-skills
description: Run, test, smoke-check, audit, or health-check the ~/.agent-skills library
---
```

**Required fields:**
- `name` — unique identifier, matches the folder name
- `description` — tells the system WHEN to load this skill (trigger matching)

**Optional fields:**
- `creator` — who made it
- `tags` — categorization

## The body

After frontmatter, the skill body contains:

1. **Overview** — what this skill does
2. **When to use** — trigger conditions
3. **How to use** — step-by-step instructions
4. **Examples** — real worked examples
5. **References** — links to supporting files

## Progressive disclosure

Skills use **progressive disclosure** — the main `SKILL.md` is concise, with details in sub-files:

```
skills/writing-skills/
├── SKILL.md                          ← main (loaded first)
├── anthropic-best-practices.md       ← loaded on demand
├── persuasion-principles.md          ← loaded on demand
├── examples/
│   └── example-skill/SKILL.md        ← reference example
└── versions/
    └── v2-draft/SKILL.md             ← version history
```

The AI reads `SKILL.md` first, then loads sub-files only when needed.

## Real example: a minimal skill

From your library — `skills/shell/SKILL.md`:

```
---
name: shell
description: Shell command execution guidance
---
```

Just frontmatter + a short description. That's a valid skill.

## Real example: a complex skill

`skills/writing-skills/` has **12 files** including examples, reference docs, and version history. The main SKILL.md references them all.

## Try it yourself

```bash
# Find the smallest skill
for d in ~/.agent-skills/skills/*/; do
  echo "$(wc -c < "$d/SKILL.md" 2>/dev/null || echo 0) $d"
done | sort -n | head -5

# Find the largest skill
for d in ~/.agent-skills/skills/*/; do
  echo "$(du -sh "$d" 2>/dev/null | cut -f1) $(basename "$d")"
done | sort -rh | head -10

# Count files per skill
for d in ~/.agent-skills/skills/*/; do
  echo "$(find "$d" -type f | wc -l) $(basename "$d")"
done | sort -rn | head -10
```

## Next

→ [04: Agent Anatomy](04-agent-anatomy.md)
