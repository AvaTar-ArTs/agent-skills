# Creating Skills

## The minimal skill

At minimum, create a folder with a `SKILL.md`:

```bash
mkdir -p ~/.agent-skills/skills/my-new-skill
cat > ~/.agent-skills/skills/my-new-skill/SKILL.md << 'EOF'
---
name: my-new-skill
description: Does X when the user asks for Y
---

# My New Skill

## When to use
Use when the user wants to Y.

## How to do it
1. Step one
2. Step two
3. Step three
EOF
```

## The description field is critical

The `description` determines when this skill gets loaded. Make it:
- **Specific** — describe the exact trigger condition
- **Natural** — use the words a user would say
- **Differentiated** — don't overlap with existing skills

**Bad:** `description: General utility skill`
**Good:** `description: Create and manage Notion database templates with linked properties`

## Progressive disclosure pattern

For complex skills, use progressive disclosure:

```
skills/my-skill/
├── SKILL.md              ← Concise overview (loaded first)
├── references/
│   ├── api-guide.md      ← Detailed API docs (loaded on demand)
│   └── examples.md       ← Worked examples
└── scripts/
    └── helper.py         ← Supporting scripts
```

In `SKILL.md`, reference sub-files:
```markdown
For API details, see [references/api-guide.md](references/api-guide.md).
```

## Quality checklist

Before finalizing a skill:

- [ ] Frontmatter has `name` and `description`
- [ ] Description matches actual use cases
- [ ] Instructions are clear and actionable
- [ ] Examples use real file paths
- [ ] No credentials or secrets
- [ ] No fabricated content
- [ ] Sub-files are referenced, not duplicated

## Creating via the skill-creator tool

Desktop Commander has a built-in skill creator at:
```
~/.desktop-commander/skills/skill-creator/SKILL.md
```

It provides templates and validation for new skills.

## Try it yourself

```bash
# Create a test skill
mkdir -p ~/.agent-skills/skills/test-skill
cat > ~/.agent-skills/skills/test-skill/SKILL.md << 'EOF'
---
name: test-skill
description: A test skill created by deeptutor
---

# Test Skill

This skill was created as a learning exercise.
It does nothing — it just proves you can create a skill.

## Try it
Ask the AI: "use the test-skill"
If it loads, you succeeded.
EOF

# Verify it exists
cat ~/.agent-skills/skills/test-skill/SKILL.md
```

## Next

→ [08: Creating Agents](08-creating-agents.md)
