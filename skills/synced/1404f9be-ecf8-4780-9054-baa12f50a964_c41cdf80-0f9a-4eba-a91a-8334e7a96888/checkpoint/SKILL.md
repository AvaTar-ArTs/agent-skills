---
name: checkpoint
description: >
  Use this skill at the start of any work session that involves multiple steps,
  a long conversation, or a clear deliverable — especially when the user names
  a goal upfront ("review my codebase", "audit my revenue", "build a product",
  "help me plan X"). Also invoke when the user asks "where were we?",
  "before that...", "let's review where we began", "checkpoint", or
  "what were we trying to do?" — or whenever you notice the conversation has
  gone 10+ turns without referencing the original goal. The skill prevents
  mission drift by locking in the session anchor at the start and surfacing it
  on demand throughout.
---

# Checkpoint — Conversation Anchor Skill

Long conversations drift. The goal stated in message 1 can be invisible by message 30.
This skill locks in the original mission and makes it easy to re-surface it at any point.

---

## When to invoke

**At session start** — when the user states a goal, task, or question that will take multiple turns. Capture the anchor before any work begins.

**On demand** — when the user asks:
- "where were we?", "what were we doing?"
- "before that, let's review...", "let me step back"
- "checkpoint", "/checkpoint", "status"

**Proactively** — when you notice:
- The conversation is 10+ turns deep without referencing the original goal
- The current work is in a clearly different domain than the stated goal
- You're about to go deep on something that feels adjacent, not central

---

## Step 1 — Set the anchor (do this once, at session start)

Capture four things. Keep each short — one sentence max.

```
MISSION:      What the user actually wants to accomplish
CONSTRAINTS:  What to avoid, not do, or stay within
DELIVERABLES: What done looks like (specific outputs, files, decisions)
IN SCOPE:     The space we're working in
```

**Example — this session:**
```
MISSION:      Find missed revenue opportunities in ~/
CONSTRAINTS:  Don't build new things — find what's already there
DELIVERABLES: Specific assets identified + Gumroad listings written
IN SCOPE:     ~/  (home directory audit)
```

Write the anchor to a file at the start of the session:
```
~/.session-checkpoint.md  (or wherever is convenient)
```

Then confirm it with the user in one line:
> "Anchored: [one-line summary]. Tell me if I have it wrong."

If the user corrects it, update and re-confirm. This is the only moment to set it.

---

## Step 2 — Checkpoint on demand

When invoked mid-session, output the full status block:

```
━━━ CHECKPOINT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION:      [original goal]
DELIVERABLES: [what done looks like]

DONE:
  ✓ [completed item 1]
  ✓ [completed item 2]

IN PROGRESS / NEXT:
  → [current thread]

QUEUED (found but not done):
  · [item 1]
  · [item 2]

DRIFTED (interesting but off-mission):
  ⚠ [topic] — set aside, revisit later?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Keep DONE and QUEUED factual — only things the user confirmed or that are in `/mnt/user-data/outputs/` count as done. Don't count "identified" as done unless the user has it in hand.

---

## Step 3 — Drift detection

Before going deep on any new thread, run a one-sentence internal check:

> "Does this serve the MISSION, or is it interesting for a different reason?"

If interesting but not central: name it, park it, continue.

> "Found [X] — worth its own session, but not what we're here for. Noting it and moving on."

If the user wants to pursue it anyway, that's fine — but first offer to update the anchor:

> "This shifts us to [new goal]. Want me to update the anchor, or keep the original and treat this as a detour?"

The user decides. The skill enforces clarity, not rigidity.

---

## Step 4 — Session close (optional)

At the end of a session, or when the user says "wrap up" / "summary":

```
━━━ SESSION SUMMARY ━━━━━━━━━━━━━━━━━━━━━━━━━━

ORIGINAL MISSION: [anchor]

SHIPPED:
  ✓ [item] → [location/price/status]
  ✓ [item] → [location/price/status]

FOUND BUT NOT SHIPPED:
  · [item] — [blocker or next action]

PARKED (out of scope this session):
  · [item] — [why parked]

NEXT SESSION SHOULD START WITH:
  → [most important next action]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## What counts as drift vs. a legitimate detour

**Drift** — the mission is forgotten, not paused. Work is happening in a different domain with no explicit decision to go there. The user would be surprised to be reminded of the original goal.

**Detour** — the user consciously chose to explore something adjacent. The original mission is still the frame. The user knows they'll return.

The skill handles both: drift gets flagged, detours get acknowledged and parked cleanly.

---

## Tone

Brief. Factual. No drama about being off-track. The checkpoint is a tool, not a judgment. One line to re-anchor, then back to work.

---

## Session file format (for persistence across turns)

```markdown
# Session Anchor — [date]

## Mission
[one sentence]

## Constraints
[one sentence or bullet list]

## Deliverables
[specific outputs]

## Log
- [timestamp] Anchored
- [timestamp] Checkpoint called — [brief status]
- [timestamp] Detour: [topic] — parked
- [timestamp] [item] SHIPPED → [location]
```

Update the log as the session progresses. Read it at the start of each checkpoint call to reconstruct state accurately.
