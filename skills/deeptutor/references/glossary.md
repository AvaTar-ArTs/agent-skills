# Glossary

| Term | Definition |
|------|-----------|
| **Skill** | A folder containing SKILL.md with instructions for the AI |
| **Agent** | An autonomous worker with its own prompt, tools, and context |
| **Frontmatter** | YAML block at the start of SKILL.md or agent .md (name, description) |
| **Canonical library** | `~/.agent-skills/skills/` — the source of truth |
| **Active-skills** | Curated symlinks from active-skills/ into canonical skills/ |
| **Projection** | A host-specific view of skills (Hermes, Claude, Cursor each have one) |
| **Host drift** | When a projection diverges from canonical (especially Cursor copies) |
| **Progressive disclosure** | Pattern: load SKILL.md first, sub-files on demand |
| **MCP** | Model Context Protocol — external tool servers (NOT skills) |
| **Smoke audit** | `run-agent-skills-smoke.sh` — checks broken links, duplicates, frontmatter |
| **Door** | A symlink that lets a host discover a skill in the canonical library |
| **Quarantine** | Moved duplicates with manifest for safe restore |
| **Exact duplicate** | Two files with identical SHA-256 content hash |
| **Name duplicate** | Two skills/agents with the same name field |
| **Description match** | How the system decides which skill to load (request ↔ description) |
| **Context bloat** | When too many skills inflate the AI's prompt, slowing responses |
| **Deep module** | A module with a small interface hiding complex internals |
| **HAR** | HTTP Archive — browser network traffic capture |
| **stdio** | Standard input/output transport for MCP servers |
