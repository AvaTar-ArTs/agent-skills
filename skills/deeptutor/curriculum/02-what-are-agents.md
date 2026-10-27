# What are Agents?

An **agent** is a specialized AI worker with its own system prompt, tools, and sometimes its own model. Unlike skills (which are passive instructions), agents are **active workers** that can execute tasks independently.

## Agents vs Skills

| Aspect | Agent | Skill |
|--------|-------|-------|
| What it is | Autonomous worker | Instruction document |
| Has tools? | Yes (restricted set) | No (uses host tools) |
| Runs in | Isolated context | Main conversation |
| System prompt | Own dedicated prompt | Part of host prompt |
| Frontmatter | `name`, `description`, `tools`, `model` | `name`, `description` |

## Where agents live

Your canonical agents directory:
```
~/.agent-skills/agents/
```

Claude loads seven agents from `~/.claude/agents/` (recounted 2026-10-27): `code-investigator`, `conversation-analyzer`, `export-knowledge-curator`, `eza-comprehender`, `filesystem-inventory`, `repo-clean`, and `review`. This archive is not that load path. Its root holds the paired markdown copies; numbered packs and `_incoming/` are history and often differ by bytes from the root file of the same name:
```
agents/
├── 1-eng-specialist-pack/    ← engineering specialists
├── 2-personal-tooled/        ← personal workflow agents
├── 3-contains-studio/        ← studio/creative agents (quarantined copies removed)
├── 5-misc-personal/          ← personal utility agents
├── _incoming/                ← new/unsorted agents
├── commands/                 ← command-style agents
└── <name>.md                 ← top-level canonical agents
```

## Example: agent frontmatter

```yaml
---
name: code-reviewer
description: Reviews code for quality, security, and best practices
tools:
  - read_file
  - start_search
  - start_process
model: claude-sonnet-4-6
---
You are a senior code reviewer. Review the provided diff for:
1. Security vulnerabilities
2. Performance issues
3. Code style violations
...
```

## Try it yourself

```bash
# List your agents
ls ~/.agent-skills/agents/*.md | head -20

# Read an agent's frontmatter
head -20 ~/.agent-skills/agents/system-architect.md

# Count agents by category
for d in ~/.agent-skills/agents/*/; do echo "$(basename "$d"): $(ls "$d"/*.md 2>/dev/null | wc -l)"; done
```

## Next

→ [03: Skill Anatomy](03-skill-anatomy.md)
