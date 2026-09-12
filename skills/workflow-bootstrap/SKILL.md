---
name: workflow-bootstrap
description: Defines mandatory workflows and where skills/agents live on this machine. Use when starting creative work, multi-step implementation, or when the user asks how skills and agents are organized. Ensures brainstorm before coding and plan-before-implement discipline.
---

# Workflow Bootstrap

Canonical library: **`~/.agent-skills`**. Skills: **`~/.agent-skills/skills/<name>/SKILL.md`**. Agents: **`~/.agent-skills/agents/`**.

`~/.supremepower` is **not** present. Do not load or write there.

## Where things live (this machine, 2026-09-11)

| Type | Path | Kind |
|------|------|------|
| Canonical skills | `~/.agent-skills/skills/<name>/SKILL.md` | **real** git tree |
| Canonical agents | `~/.agent-skills/agents/` | **real** |
| `npx skills` door | `~/.agents/skills` | **symlink →** `~/.agent-skills/skills` |
| `npx` lockfile | `~/.agents/.skill-lock.json` | stays beside the door |
| Claude | `~/.claude/skills`, `~/.claude/agents` | **symlink →** canonical |
| Codex `superpowers` | `~/.codex/superpowers` | **symlink →** `using-superpowers` |
| Codex / Cursor / Gemini / Qwen / Hermes / Grok `skills/` | under each `~/.<host>/` | often **real copies** — do not edit as source |
| Superpowers port source | `~/iterm2/superpowers/skills/` | real, not the runtime library |
| `~/.supremepower` | — | **missing** |

If `~/.agents/skills` is a real directory again, restore the symlink. Do not `rm -rf` it; `mv` aside, then `ln -s`. Prefer copying new skills **into canonical**, not `npx add` into `~/.agents` (that has replaced the door).

## Mandatory workflows

**Before creative work (features, components, behavior, video, new skill packs):**
1. Use **brainstorming** to explore intent, requirements, and design.
2. Document the design (e.g. `~/.agent-skills/docs/plans/YYYY-MM-DD-<topic>-design.md`).
3. Only then implement or spend generation credits.

**Before multi-step implementation:**
1. Use **writing-plans** for a bite-sized plan.
2. Save under `docs/plans/YYYY-MM-DD-<feature>.md` (canonical repo or the project).
3. Optionally **using-git-worktrees** for an isolated branch.
4. Use **executing-plans** (or **subagent-driven-development** if tasks are independent) with review checkpoints.

**After a major step:**
- **requesting-code-review** / **receiving-code-review** against the plan.

## Skill chain

- **brainstorming** → design doc → **writing-plans** → plan doc → **executing-plans** (or **subagent-driven-development**) → **finishing-a-development-branch**.
- **test-driven-development** during implementation; **using-git-worktrees** when isolating a branch.
- **systematic-debugging** before any fix; **verification-before-completion** before any completion claim.
- **dispatching-parallel-agents** when 2+ independent problems; **writing-skills** when authoring skills.

## When a skill applies

If a task matches a skill description, use that skill. Do not skip mandatory workflows (brainstorm before coding or expensive I2V; plan before multi-step implementation).

## Cross-ecosystem

For how Claude, Codex, Cursor, Gemini, Qwen, Grok, and `npx` relate, use **ecosystem-clarity** (still stale on `~/.supremepower` until that skill is updated the same way). Source of truth for *paths* is this file plus `~/.agent-skills/INDEX.md`.
