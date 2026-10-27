---
name: using-paste-mcp
description: >-
  Use when saving or retrieving clipboard/pinboard items via Paste MCP: search
  Paste, never echo secrets, create titled text/link/color only, pin to a named
  private board. Not for inventing new Paste types or writing images/files.
---

# using-paste-mcp

search Paste → never echo secrets → create titled text/link/color only → pin to a named private board.

This is not an official Paste feature. Official MCP authors only `text`, `link`, and `color` (`#RRGGBB`). Images and files must be copied in-app. Shared pinboards are not writable.

Project copy (keep in sync): `/Users/steven/github/paste-mcp/skills/using-paste-mcp/SKILL.md`.

## When

- User wants a reusable clipboard fill, identity snippet, or pinboard pin.
- `user-Paste` tools are available (or `mcp_auth` first if discovery failed).

Do not use this skill to dump history, reprint `sk-` / Bearer / `ghp_` strings, or create a new item *kind*.

## Sequence (required)

1. **Authenticate** if tools are unavailable: `mcp_auth` on `user-Paste`.
2. **search** — summarize by `id`, `type`, `title`, pinboard name. Redact API-key-shaped previews. Never paste secret-shaped `read_item` bodies into chat, Engram, or widgets.
3. **list_pinboards** — private board by name; `create_pinboard` if missing. Not shared boards.
4. **create titled text/link/color only** — `create_item` with `content` and `list_id`, then `update_item` for the title. MCP cannot author images/files.
5. **Existing history item** — `search` then `add_item_to_pinboard`. Still never echo secrets.

## Hard no

- Echo clipboard secrets into the transcript, titles, Engram, or git.
- Destructive delete without explicit user confirm plus tool `confirm: true`.
- Scan all of `~/` for Paste data.
