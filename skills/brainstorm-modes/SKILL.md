---
name: brainstorm-modes
description: "Use when the user explicitly asks for brainstorm modes, brainstorming mode, or a brainstorm-mode workflow. Route to the canonical `brainstorming` skill, which handles requirements discovery, alternative comparison, design approval, and transition to planning before implementation."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [brainstorming, compatibility, design, workflow-gate]
    related_skills: [brainstorming, writing-plans]
disable-model-invocation: true
changelog:
  - "2026-08-15: Added as an explicit-only compatibility alias routed to canonical brainstorming."
  - "2026-10-05: Appended 'Choose the mode first' (RED baseline: agent skipped lens selection, converged on 3 ideas, invented brand facts under time pressure). Existing text unchanged."
---

# Brainstorm Modes Compatibility Alias

Load `brainstorming` and follow its canonical workflow. This alias exists so
existing prompts that say “brainstorm modes” continue to resolve without creating
a second design process or competing automatic trigger.

## Choose the mode first (before any idea or question)

Name one mode in your first line, then follow its reference file. It sets the kind of thinking; `brainstorming` sets the gates.

| Mode | Use when | Reference |
|---|---|---|
| creative | ideas, names, "give me options" | `references/creative.md` (8–12 unfiltered → one filter → surface 3) |
| content | words, voice, labels, captions, copy | `references/content.md` |
| design | structure, hierarchy, flow | `references/design.md` |
| strategy | "should we", priorities, A vs B | `references/strategy.md` |
| logic | how something actually behaves, edge cases | `references/logic.md` |
| research | "what exists / what's missing" | `references/research.md` (output the gap, not the data) |
| code | which technical approach | `references/code.md` |

**Hurry changes length, not process.** "Quick", "just go" or "I'm in a hurry" means shorter output. It never means skipping the mode or jumping to a pick.

**Recall before inventing.** Before writing names, slogans or brand facts, check memory (Engram, `~/.agent-skills/memory/shared.sqlite`, `~/.claude/memory/`) for the real ones. Don't make up call signs, frequencies or taglines.

| Rationalization | Reality |
|---|---|
| "Following the process would miss what they asked for" | Naming the mode takes one line; it's what makes the ideas right. |
| "Three good ideas is enough" | Creative mode generates 8–12 before filtering; three is convergence too early. |
| "I'll fill in brand details plausibly" | Plausible-but-invented details are wrong details. Recall or ask. |
