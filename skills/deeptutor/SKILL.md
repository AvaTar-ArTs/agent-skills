---
name: deeptutor
description: >
  Interactive tutor that teaches how Desktop Commander agents and skills work,
  using the actual ~/.agent-skills library (322 top-level folders with SKILL.md and 608 SKILL.md files overall, measured 2026-10-27) as live curriculum.
  Use when the user wants to learn how skills load, how agents are structured,
  how the ecosystem connects, or how to create/modify skills and agents.
---

# deeptutor

An interactive, progressive tutor for the Desktop Commander agents/skills ecosystem.

## How to use

Walk the user through lessons in order, or jump to a specific topic:

| Lesson | Topic | When to use |
|--------|-------|-------------|
| [01](curriculum/01-what-are-skills.md) | What are skills? | Starting from zero |
| [02](curriculum/02-what-are-agents.md) | What are agents? | After lesson 01 |
| [03](curriculum/03-skill-anatomy.md) | Skill anatomy | When editing/creating skills |
| [04](curriculum/04-agent-anatomy.md) | Agent anatomy | When editing/creating agents |
| [05](curriculum/05-how-skills-load.md) | How skills load | Debugging skill discovery |
| [06](curriculum/06-active-skills-projection.md) | Active-skills projection | Understanding symlink trees |
| [07](curriculum/07-creating-skills.md) | Creating skills | Building new skills |
| [08](curriculum/08-creating-agents.md) | Creating agents | Building new agents |
| [09](curriculum/09-ecosystem-map.md) | Ecosystem map | Understanding host landscape |
| [10](curriculum/10-troubleshooting.md) | Troubleshooting | When things break |
| [11](curriculum/11-reference-architecture.md) | Reference architecture | Full system overview |

## Teaching approach

1. **Read real files** — every example comes from `~/.agent-skills/skills/`
2. **Progressive complexity** — start with concepts, build to architecture
3. **Try-it-yourself** — exercises use the user's actual library
4. **No fabrication** — quote real code, show real paths

## Quick start

For a new user, read lessons 01-03 in order.
For skill creation, jump to 03 then 07.
For debugging, jump to 05 then 10.
For full architecture, read 11.
