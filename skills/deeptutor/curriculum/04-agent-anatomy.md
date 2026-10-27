# Agent Anatomy

Agents have richer frontmatter than skills because they're autonomous workers.

## Agent frontmatter specification

```yaml
---
name: my-agent
description: What this agent does and when to use it
tools:
  - read_file
  - write_file
  - start_search
  - start_process
model: claude-sonnet-4-6
triggers:
  - "review code"
  - "audit security"
---
```

### Fields

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | Yes | Unique identifier |
| `description` | Yes | When to activate this agent |
| `tools` | No | Restrict which tools the agent can use |
| `model` | No | Override the default model |
| `triggers` | No | Phrases that activate this agent |

### Tool restriction

Agents can be restricted to specific tools for safety:

```yaml
tools:
  - read_file        # Can read files
  - start_search     # Can search
  # Cannot: write_file, start_process, edit_block
```

This creates a **read-only** agent that can analyze but not modify.

## Agent body

After frontmatter, the agent body is its **system prompt** — the persistent instructions it follows:

```markdown
You are a security auditor. Your job is to:
1. Scan code for vulnerabilities
2. Check for hardcoded secrets
3. Verify authentication patterns
4. Report findings in a structured format

Never modify files. Only report findings.
```

## Missing frontmatter (common issue)

Your audit found **17 agent files** without frontmatter. These were fixed by adding:

```yaml
---
name: <derived from filename>
description: Agent file at <path>
---
```

Without frontmatter, agents can't be discovered or loaded by the system.

## Try it yourself

```bash
# Show agents with tool restrictions
grep -l "tools:" ~/.agent-skills/agents/*.md | head -10

# Show agents with model overrides
grep -l "model:" ~/.agent-skills/agents/*.md | head -10

# Find agents without frontmatter (should be 0 after cleanup)
for f in ~/.agent-skills/agents/*.md; do
  head -1 "$f" | grep -q "^---" || echo "NO FRONTMATTER: $f"
done
```

## Next

→ [05: How Skills Load](05-how-skills-load.md)
