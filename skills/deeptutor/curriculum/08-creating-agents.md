# Creating Agents

## Agent vs skill

Create an **agent** when you need:
- A worker with **restricted tools** (read-only, search-only, etc.)
- An **isolated context** (doesn't see the main conversation)
- A **specific model** override
- An **autonomous** task runner

Create a **skill** when you need:
- Instructions loaded into the **main conversation**
- The AI to follow a **workflow** using all available tools
- **Reference documentation** for a domain

## Minimal agent

```markdown
---
name: my-agent
description: Brief description of what this agent does and when to activate it
tools:
  - read_file
  - start_search
---

You are a [role]. Your job is to [task].

## Rules
1. [Rule 1]
2. [Rule 2]

## Output format
Produce [format].
```

## Tool restriction examples

**Read-only analyst:**
```yaml
tools:
  - read_file
  - start_search
```

**File editor (no shell):**
```yaml
tools:
  - read_file
  - write_file
  - edit_block
  - start_search
```

**Full access:**
```yaml
tools:
  - read_file
  - write_file
  - edit_block
  - start_search
  - start_process
```

## Where agents live

```
~/.agent-skills/agents/
├── <agent-name>.md           ← top-level canonical
├── 1-eng-specialist-pack/    ← category folder
├── 3-contains-studio/        ← category folder
└── _incoming/                ← staging area
```

Canonical agents are at the **root level**. Category folders held copies (now mostly quarantined to avoid duplicates).

## Try it yourself

```bash
# Create a test agent
cat > ~/.agent-skills/agents/test-analyzer.md << 'EOF'
---
name: test-analyzer
description: Analyzes test files and reports coverage gaps. Use when asked to check test coverage.
tools:
  - read_file
  - start_search
---

You are a test coverage analyzer.

## Task
1. Find all test files in the project
2. Identify source files without corresponding tests
3. Report coverage gaps as a markdown table

## Rules
- Never modify files
- Only report findings
- Use real file paths
EOF

# Verify
head -20 ~/.agent-skills/agents/test-analyzer.md
```

## Next

→ [09: Ecosystem Map](09-ecosystem-map.md)
