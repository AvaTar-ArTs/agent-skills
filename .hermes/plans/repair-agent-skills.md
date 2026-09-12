# Agent Skills Repair and Add-on Integration Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Restore accidental Claude-to-Codex substitutions in the canonical agent-skills repository while preserving legitimate Codex content, intentional local additions, and the selected upstream skills in Hermes only.

**Architecture:** Treat `/Users/steven/.agent-skills` as the canonical authored source. Treat `~/.hermes/skills` as the Hermes runtime projection for the three explicitly selected upstream skills. Repair tracked files by comparing them to `HEAD` and changing only evidence-backed accidental substitutions; do not reset the dirty worktree or overwrite unrelated user changes.

**Tech Stack:** Git, Python/read-only audit scripts, Markdown/YAML frontmatter, Hermes skills CLI, repository runtime audit.

---

## Approved Scope

1. Restore clearly accidental substitutions where the current worktree changed Claude-specific names, commands, paths, URLs, model identifiers, or provider labels to Codex, based on direct `git diff` evidence.
2. Preserve legitimate Codex references in Codex-specific files and preserve unrelated changes in the dirty worktree.
3. Keep intentional untracked additions unless they are verified to be accidental copies of the three upstream installs in the repository itself.
4. Ensure these three skills remain installed in Hermes only:
   - `~/.hermes/skills/ci-cd-and-automation`
   - `~/.hermes/skills/mcp-builder`
   - `~/.hermes/skills/webapp-testing`
5. Do not delete the reversible quarantine at `/Users/steven/.skills-cli-quarantine-20260910-220853`.
6. Do not commit, push, rewrite history, read secrets, or modify credential files.

## Research Findings

Focused `npx skills find` and web research found:

- `addyosmani/agent-skills@ci-cd-and-automation` — 30.4K installs; strong CI quality-gate complement.
- `anthropics/skills@mcp-builder` — official Anthropic MCP workflow; 113K+ installs in the prior audit.
- `anthropics/skills@webapp-testing` — official Anthropic Playwright web QA workflow; 153K+ installs in the prior audit.
- `wshobson/agents@git-advanced-workflows` — 17.7K installs; candidate for later comparison, not automatic installation.
- `vercel-labs/agent-browser@agent-browser` — candidate browser CLI layer; compare against existing `cua-driver` and installed `webapp-testing` before adoption.
- `openai/codex` and `openai/skills` — official Codex sources; inspect selectively rather than bulk-installing.
- `sickn33/agentic-awesome-skills` — large catalog with useful coverage but too broad for bulk import.

No additional add-on is approved for installation in this repair pass because the local ecosystem already has broad coverage and the worktree has pre-existing modifications.

## Selection Record

```yaml
skill_selection:
  intent: "Repair canonical agent-skills content and safely add high-value engineering workflows."
  process_skills:
    - using-superpowers
    - systematic-debugging
    - writing-plans
    - subagent-driven-development
  domain_skills:
    - ci-cd-and-automation
    - mcp-builder
    - webapp-testing
  implementation_skills:
    - test-driven-development
  verification_skills:
    - verification-before-completion
    - workspace-ecosystem-audit
  semantic_capabilities:
    - git-diff-repair
    - runtime-projection-audit
    - skill-source-comparison
  provider_decisions_deferred:
    - additional skills.sh installs beyond the three approved Hermes skills
```

---

## Task 1: Inventory and classify dirty changes

**Objective:** Produce a bounded classification of tracked modifications and untracked additions without changing files.

**Files:**
- Read: `git status`, `git diff`, `scripts/audit_runtime.py`
- Reference: `README.md`, `INDEX.md`, `docs/SKILL_WORKFLOW_CONTRACT.md`

**Steps:**
1. Record current `git status --short --branch` and the current `HEAD`.
2. Identify tracked files whose diff contains Claude-specific text replaced by Codex or invalid Codex-derived identifiers.
3. Identify untracked directories created by the earlier skills CLI attempt and compare timestamps/content with the quarantine manifest.
4. Mark each candidate as `restore`, `preserve`, `quarantine-only`, or `defer`.

**Verification:** The classification must not include credential files, unrelated generated files, or legitimate Codex-specific content.

## Task 2: Restore accidental provider substitutions

**Objective:** Repair only the evidence-backed accidental Claude-to-Codex substitutions in tracked skill authorities.

**Likely files from the current diff:**
- `skills/autonomous-ai-agents/claude-code/SKILL.md`
- `skills/claude-code/SKILL.md`
- `skills/claude-handoff/SKILL.md`
- `skills/agmsg/SKILL.md`
- `skills/belt/SKILL.md`
- `skills/blackbox/SKILL.md`
- `skills/ccassist/SKILL.md`
- `skills/chat-history-export/SKILL.md`
- `skills/content-strategy/SKILL.md`
- `skills/create-agents/SKILL.md`
- `skills/create-skill/SKILL.md`
- `skills/cua-driver/SKILL.md`
- `skills/dspy/SKILL.md`
- `skills/find-skills/SKILL.md`
- `skills/git-guardrails-claude-code/SKILL.md`
- `skills/hermes-agent-spawning/SKILL.md`
- `skills/instructor/SKILL.md`
- `skills/mcporter/SKILL.md`
- `skills/ml-paper-writing/SKILL.md`
- `skills/setup-matt-pocock-skills/SKILL.md`
- `skills/setup-ts-deep-modules/SKILL.md`
- `skills/writing-for-agents/SKILL.md`

**Rules:**
1. Compare each current file with `HEAD`; do not replace an entire file from `HEAD`.
2. Restore provider-specific content from `HEAD` when the current change is a pure accidental substitution or provider corruption.
3. Preserve intentional improvements in the same file when they are not part of the substitution.
4. Keep `skills/codex/SKILL.md` Codex-specific; repair only an accidental cross-reference such as `related_skills: [Codex, ...]` if evidence proves the intended identifier is `claude-code`.
5. Restore valid provider/model identifiers such as `claude-sonnet-*` and `dspy.Claude` in Anthropic examples; do not invent newer model versions.
6. Preserve legitimate multi-provider lists containing both Claude and Codex.

**Testing:**
- Run frontmatter/structure validation through the repository’s available audit tooling.
- Search the changed files for invalid patterns: `name: Codex` in Claude-specific files, `Codex-sonnet`, `dspy.Codex`, `@anthropic-ai/Codex`, `.Codex/` substitutions, and duplicated `AGENTS.md` where `CLAUDE.md` was present in `HEAD`.

## Task 3: Keep intentional additions and Hermes-only installs separated

**Objective:** Ensure the approved upstream skills are available to Hermes without accidental repository copies or broad agent projections.

**Checks:**
1. Confirm each approved skill has `SKILL.md` under `~/.hermes/skills/<name>/`.
2. Confirm the repo does not contain a newly copied duplicate of those three skills unless the user explicitly chooses to promote it later.
3. Preserve the quarantine manifest and do not delete it.
4. Do not run `npx skills add --agent '*'` again.

## Task 4: Two-stage review

**Objective:** Validate spec compliance and code/document quality separately.

**Spec review:**
- Every provider-specific accidental substitution is restored.
- Legitimate Codex material is preserved.
- Intentional additions and unrelated dirty changes remain.
- Hermes-only skill paths are present.
- No destructive cleanup or commit occurred.

**Quality review:**
- Markdown frontmatter remains valid.
- Commands, URLs, provider names, and model IDs are internally consistent.
- No broad search-and-replace artifacts remain in the repaired files.
- Changes are minimal and provenance-preserving.

## Task 5: Final integration verification

**Commands:**

```bash
python3 scripts/audit_runtime.py --pretty
bash hooks/tests/test-pre-tool-autocontext.sh

git diff --check
git status --short --branch
```

**Expected result:** Runtime audit completes, hook test passes, `git diff --check` reports no whitespace errors, the three Hermes skills are present, and unrelated pre-existing worktree changes remain unmodified.

**Stop condition:** Do not commit or push. If a repair would require guessing about intentional content, leave it unchanged and report it for review.
