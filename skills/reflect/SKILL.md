---
name: reflect
description: "Mid-conversation reflection that pauses execution and zooms out from detail-mode: re-reads the whole conversation from the original goal forward, runs a 5-dimension reassessment (Macro / Gap / Reflective / Bias / Contextual), then turns it into durable learning and one smallest-viable evolution. Use when the user says 'reflect', 'take a step back', 'step back', 'zoom out', 'are we missing something', 'bigger picture', 'sanity check this', 'are we on track', 'are we overthinking this', 'forest for the trees', or 'comprehend learn evolve' — or whenever a long run has gone deep on detail without a strategic check-in, or the user sounds stuck (a stuck feeling usually means the framing needs a reset, not more detail)."
license: MIT
metadata:
  derived_from: "claude-code-skills marketplace / productivity/reflect (cs-reflect v1.0.0)"
  evolved_for: "multi-host ~/.agent-skills ecosystem (memory stores, checkpoints, self-evolution agents)"
  version: 2.0.0
---

# Reflect — comprehend → learn → evolve

> **Portability:** pure-reasoning skill. No external tools required. Where the machine has a
> memory store, the *Learn* and *Evolve* phases persist there; where it does not, they are
> delivered in-thread and offered for saving.

Mid-conversation, this skill **pauses execution** and produces a frank reassessment — then goes
one step further than reflection alone: it converts the reassessment into a **durable lesson**
and **one concrete evolution**. Output is flowing analysis (no headers, conversational tone)
across three phases — **Comprehend → Learn → Evolve** — ending with a mandatory directional
recommendation: **continue, pivot, or pause to answer a specific question**.

## Invocation triggers

**Explicit:** "reflect", "take a step back"/"step back", "zoom out", "are we missing something",
"bigger picture", "what are we missing", "let's pause", "sanity check this", "are we on track",
"are we overthinking this", "forest for the trees", "comprehend learn evolve".

**Implicit (no phrase needed):** 10+ turns deep on implementation detail with no strategic
check-in; repeated dead-ends or pivots; the user shows signs of being stuck or frustrated.
On an implicit signal, **ask** whether to step back — do not invoke unannounced.

## Stop directive

Halt the in-progress task. Reflection is a pause, not a side-quest. Continuing detail work while
"reflecting on the side" collapses reflection-in-action with reflection-on-action and defeats the
purpose.

## Phase 0 — Orient (cheap, always)

Recover, from the actual conversation rather than memory: the **original requested outcome**,
**prior approvals and corrections**, **verified results**, and the **next unresolved step**.
If context is absent, say what is unknown instead of inventing continuity.

## Phase 1 — Comprehend (the 5 dimensions)

Re-read the **full conversation from the original goal forward** — not just recent turns. That
discipline is what separates reflection from a local summary: the framing at turn one defines
what counts as "on track", and drift is invisible from inside the drift.

1. **Macro perspective** — what did the user actually set out to do? Has the work drifted from
   it, and in which direction? Anchor it: *"the goal at turn N was X; we are now at Y."*
2. **Gap analysis** — unverified assumptions; missing stakeholders/consumers; skipped constraints;
   dismissed alternatives worth revisiting; external factors ignored.
3. **Reflective inquiry** — right problem, or an adjacent easier one? A simpler path over-complicated?
   A harder, more valuable path avoided? What would a fresh reviewer see?
4. **Bias check** — confirmation, sunk cost, anchoring, complexity, recency. Name each one found,
   cite the evidence, and give the corrective move. **Do not** manufacture a bias that is not there.
5. **Contextual alignment** — does the direction serve the user's real goals, and is it the best
   use of their time right now?

## Phase 2 — Learn (what generalizes)

Distil the single most useful **transferable lesson** from this run, and classify it:

| Class | Meaning | Where it usually belongs |
|---|---|---|
| **Fact** | durable state of the world | a memory note (`reference-*`) |
| **Preference / rule** | how the user wants work done | a `feedback-*` note or `AGENTS.md` |
| **Capability gap** | a skill/agent/hook that should exist | canonical `skills/` or `agents/` |
| **Defect** | something built that is broken | an issue / a fix plan |
| **Open question** | genuinely unresolved | an open-threads list + checkpoint |

State it as one sentence you would hand to the next session, and say where it should live.

## Phase 3 — Evolve (the smallest durable change)

Pick the **single smallest change** that would prevent this lesson from being re-learned, and
choose its home deliberately:

- a **memory note** under the host memory store (e.g. `~/.claude/memory/`, `~/.Codex/memory/`);
- a **feedback rule** / `AGENTS.md` line;
- a **skill / agent / hook** in the canonical library (`~/.agent-skills/…`);
- a **code/config fix**.

For anything larger than one file, **delegate** to the existing evolution agents rather than
duplicating them — `~/.agent-skills/agents/self-evolution.md` and
`~/.agent-skills/agents/integrated-evolution.md` — and say so. Prefer **one verified incremental
improvement** over a speculative sweep. Write it (if authorized and additive) or queue it with the
exact path and a one-line rationale.

## Tone and format rules

- **Flowing prose** — no headers, no bullet lists in the delivered reflection.
- **Tight but thorough** — neither a one-liner nor a wall of text.
- **Direct critique** when warranted, anchored to specific conversation moments.
- **Validation** when warranted, with specific reasons — *not* vague reassurance.
- **No manufactured problems** — if the path is genuinely solid, say so and explain why.

## Closing recommendation (mandatory)

End every run with exactly one of:

- **Continue.** {specific reasoning}
- **Pivot to {X}**, away from {what to drop}. {specific evidence}
- **Pause for {Q}.** Without answering this, the next step risks {specific cost}.

Never end with "consider your options" or "think about it more" — that is introspection without
resolution.

## Memory surfaces on this machine (for Learn / Evolve)

- `~/.claude/memory/` (+ `MEMORY.md` index) — the richest curated store.
- `~/.Codex/memory/`, `~/.gemini/memory/`, `~/.qwen/memories/`, `~/.grok/memory-v2/` — host stores.
- `~/.agent-skills/memory/shared.sqlite` — `decisions` table; query via
  `~/.agent-skills/skills/self-evolving-memory/scripts/query_memory.py`; insert-only with a dated `.bak`.
- `~/.agent-skills/docs/checkpoints/` — dated session checkpoints.
- `~/.agent-skills/hooks/capability-continuity.md` — the continuity contract to honor.

## Anti-patterns to reject

- Hardcoded user names or domain specifics; structured-report output when prose is required.
- Manufactured problems, or vague reassurance.
- Re-reading only recent turns instead of the whole conversation.
- Skipping the closing recommendation, or stopping at reflection without the Learn/Evolve phases.
- Continuing the in-progress task while "reflecting on the side".

---

**Version:** 2.0.0 — derived from the marketplace `cs-reflect` v1.0.0 (Path-B conversion of
`megaprompts/02-reflect-megaprompt.md`), evolved with the machine-native **Learn/Evolve** phases
and memory-surface wiring.
