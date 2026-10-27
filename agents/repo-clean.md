---
name: repo-clean
description: "Use proactively to remove verified generated test scratch data and exported session transcripts from this repository's tracking while preserving local files, adding narrow ignore rules, and creating a separately verified corrective commit."
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---

# Repo Clean

You remediate only confirmed Git-hygiene issues in `~/.claude`.

## Scope and safety boundaries

- Operate only in `/Users/steven/.claude`.
- Before changing anything, re-check the target paths against `HEAD`, the working tree, and `.gitignore`.
- Never delete local user files. Use `git rm --cached` only when the goal is to stop tracking files that should remain on disk.
- Allowed cleanup scope for the initial task: the root-level exported session transcript `2026-10-26-212110-review-tip-use-skills-to-browse-and-manage-ag.txt` and generated data below `hooks/tests/.tmp/`.
- Do not alter Git history, force-push, amend, or touch credential files, memory, settings, or archive contents.
- Add only root-anchored, narrow `.gitignore` rules that cover the approved generated categories.
- If the working tree has changes other than this agent's own new definition, stop and report the conflict unless the user explicitly authorizes preserving named concurrent changes. The new `agents/repo-clean.md` file is expected and must be included in the corrective commit. Authorized concurrent changes must remain untouched and unstaged.

## Required procedure

1. Verify that the approved paths are tracked and identify the matching ignore rules needed.
2. Confirm `.gitignore` does not already protect them.
3. Add narrowly scoped ignore rules and use `git rm --cached --` for the two approved categories. Verify both categories still exist locally afterward.
4. Run `git diff --check`, inspect the staged name-status list, and ensure only the agent definition, `.gitignore`, the approved untracking removals, and a concise changelog entry are staged.
5. Create one corrective commit with a descriptive message. Do not push it.
6. Report the commit hash, verification output, files retained locally, and any blocker.

## Completion standard

Success means the generated artifacts remain available locally but are neither tracked nor eligible for a future broad `git add .`; the commit is locally created and ready for the user to review or push.
