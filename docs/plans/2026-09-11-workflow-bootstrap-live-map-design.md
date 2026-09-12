# Design: workflow-bootstrap live map → `~/.agent-skills/skills`

Date: 2026-09-11  
Gate: brainstorming  
Status: approved to implement `workflow-bootstrap` only (`/brainstorm and begin`)

## Objective

Make `workflow-bootstrap` describe this machine: canonical skills live in `~/.agent-skills/skills/`. Stop naming `~/.supremepower` as if it exists.

## Non-goals (this slice)

- Do not rewrite every stale Supremepower mention (`ecosystem-clarity` is a follow-up).
- Do not generate the map from a live script.
- Do not commit marketplace skill copies or push.
- Do not start Mother I2V.

## Authoritative inputs

- Canonical: `~/.agent-skills/skills`, `~/.agent-skills/agents`
- Door: `~/.agents/skills` → canonical (must stay a symlink)
- Claude: `~/.claude/skills` and `agents` → canonical
- `~/.supremepower`: missing
- Mandatory chains (brainstorm → plan → execute → verify) stay

## Approach (chosen)

**A — Edit `skills/workflow-bootstrap/SKILL.md` in canonical.** One file. Same methodology, new “where things live” table.

Rejected: B (also rewrite ecosystem-clarity now) — extra scope. C (auto-generated map) — new toolchain.

## Verification

- File contains `~/.agent-skills/skills` and does not treat `~/.supremepower` as live.
- Door still a symlink after the edit.
- Mandatory workflow sections preserved.

## Next

After this file: `writing-plans` only if more docs/skills need the same map. Mother video still needs its own brainstorm.
