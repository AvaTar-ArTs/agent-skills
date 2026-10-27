# What are Skills?

A **skill** is a folder containing a `SKILL.md` file that teaches the AI assistant how to perform a specific task well.

## Key concept

Skills are **not code that runs**. They are **instruction documents** that get loaded into the AI's context when relevant. Think of them as expert playbooks.

## Your library

Your canonical skill library lives at:
```
~/.agent-skills/skills/
```

It currently contains **322 top-level folders with a `SKILL.md`**, measured 2026-10-27. Shelves inside those folders hold more `SKILL.md` files; `find ~/.agent-skills/skills -name SKILL.md` reports **608** overall.

## Example: what a skill looks like

Here's the structure of a real skill in your library:

```
skills/writing-skills/
├── SKILL.md                    ← the main instruction file
├── anthropic-best-practices.md ← reference docs
├── graphviz-conventions.dot    ← supporting assets
├── persuasion-principles.md
├── render-graphs.js
├── testing-skills-with-subagents.md
├── examples/                   ← worked examples
└── versions/                   ← version history
```

The `SKILL.md` file contains:
1. **Frontmatter** (name, description) — tells the system when to load this skill
2. **Instructions** — detailed guidance for the AI
3. **References** to supporting files in the same folder

## Skills vs code

| Aspect | Skill | Script/Program |
|--------|-------|----------------|
| What it is | Markdown instructions | Executable code |
| How it works | Loaded into AI context | Runs in a process |
| Who executes it | The AI assistant | The interpreter/runtime |
| Where it lives | `~/.agent-skills/skills/` | `~/scripts/`, `~/python/` |
| File format | `.md` (Markdown) | `.py`, `.js`, `.sh` |

## Try it yourself

```bash
# List your skills
ls ~/.agent-skills/skills/

# Read a simple skill
cat ~/.agent-skills/skills/shell/SKILL.md

# Read a complex skill with sub-files
ls ~/.agent-skills/skills/writing-skills/
```

## Next

→ [02: What are Agents?](02-what-are-agents.md)
