# Plugin Creator Deep Audit

Date: 2026-08-08  
Canonical source reviewed: `~/.codex/skills/.system/plugin-creator/`  
Mirror reviewed: `~/.agent-skills/skills/.system/plugin-creator/`  
Codex CLI reviewed: `codex-cli 0.147.0`

## Outcome

The skill is structurally valid and its happy-path scaffold works, but it is not yet a single-source, failure-safe implementation. Four high-severity consistency/reliability defects and five medium-severity contract gaps were confirmed by source inspection or isolated executable tests.

No source fixes were made during this audit.

## Evidence base

- Read all 1,689 lines across the skill instructions, two references, four scripts, and agent metadata.
- Compared the complete Codex and `.agent-skills` directory trees.
- Compiled all Python scripts successfully.
- Ran the skill validator successfully.
- Ran seven isolated regression probes successfully; several probes intentionally prove that an invalid state is currently accepted or retained.
- Checked current `codex plugin`, `plugin add`, `plugin list`, and marketplace command behavior.
- Confirmed the configured official marketplace root and observed actual `./plugins/<name>` resolution.

## High-severity findings

### H1 — Canonical and mirror implementations have behavioral drift

The two copies have matching `SKILL.md` and `agents/openai.yaml`, but these files differ:

- `references/plugin-json-spec.md`
- `scripts/validate_plugin.py`

The Codex validator supports inline MCP server objects, `logoDark`, and app categories; the `.agent-skills` validator is older and rejects or omits those capabilities. A plugin can therefore pass in one ecosystem and fail in another.

Required correction: choose one authoritative source, make the other a generated mirror or symlink, and add a parity check covering the whole directory—not only metadata files.

### H2 — The canonical reference shows a manifest field the validator rejects

`plugin-json-spec.md` includes and documents `hooks`, while `validate_plugin.py` excludes `hooks` from allowed top-level fields. `SKILL.md` itself correctly says hooks are unsupported in `plugin.json`.

Impact: an agent following the exact reference sample can generate a plugin that the same skill rejects.

### H3 — Cachebuster accepts and documents invalid version bases

`update_plugin_cachebuster.py` accepts any non-empty version and preserves everything before `+`. The update reference explicitly shows:

```text
dev-build+other-tag → dev-build+codex.local-...
```

The validator requires strict semantic versioning, so the updater succeeds and then validation fails. This was reproduced by the regression harness.

Required correction: validate the base version before rewriting it and remove or replace the invalid documentation example.

### H4 — Scaffold plus marketplace update is not transactional

The script creates the plugin directory and manifest before updating the marketplace. When marketplace update fails—such as a duplicate entry without `--force`—the requested command exits unsuccessfully but leaves a second plugin scaffold behind.

Required correction: preflight both destinations before writing, stage writes atomically, or roll back files created by the failed invocation.

## Medium-severity findings

### M1 — Folder/name identity is not validated

The documented invariant requires the outer directory name to match `plugin.json.name`. Renaming the generated folder caused no validation error.

### M2 — Default scaffold declares a missing skills directory

Every generated manifest includes `"skills": "./skills/"`, but the default command creates no `skills/` directory unless `--with-skills` is supplied. The validator accepts this missing declared path.

Required correction: either always create `skills/`, omit the field when unused, or make validation enforce declared-path existence.

### M3 — Existing nameless marketplaces are accepted

When an existing marketplace JSON contains `plugins` but no top-level `name`, creation succeeds unless `--marketplace-name` was explicitly supplied. This violates the documented marketplace root contract.

### M4 — Force writes are direct and unrecoverable

Manifest, companion, marketplace, and cachebuster writes are direct replacements. There is no temporary-file swap, backup, fsync, or rollback. `--force` can therefore destroy the previous valid state or leave truncated JSON if interrupted.

### M5 — Default personal marketplace is not provisioned in this environment

`~/.agents/plugins/marketplace.json` is absent. The read-only/default smoke attempt could not create `~/.agents` under the active sandbox without additional authorization. This is an environment readiness issue, not proof that Codex's documented personal-marketplace path is wrong.

Before first use, the skill should preflight the path and clearly request authorization before creating it.

## Low-severity findings

### L1 — No bundled tests

The system skill ships no regression suite for scaffolding, validation, marketplace mutation, path semantics, or cachebuster behavior.

### L2 — Lint and formatting debt

Ruff reported 13 findings: non-executable files carrying shebangs, import ordering, exception-type preferences, and unused `noqa` comments. One duplicate unreachable `return` is also present in `validate_skill_manifest`.

Because the instructions invoke scripts through `python3`, non-executable mode is not currently a runtime defect.

### L3 — Trigger metadata overstates marketplace creation

The frontmatter says personal-marketplace entries are created “by default,” while the default quick-start command does not pass `--with-marketplace`. Marketplace output is optional and flag-driven.

## Marketplace-path conclusion

The earlier concern that `./plugins/<name>` necessarily resolves beneath the JSON file directory was not supported by the CLI evidence. The official marketplace file is under:

```text
~/.codex/.tmp/plugins/.agents/plugins/marketplace.json
```

while `codex plugin marketplace list` reports its root as:

```text
~/.codex/.tmp/plugins
```

and `codex plugin list` resolves `./plugins/<name>` beneath that reported root. The path convention is real, but the reference should say “configured marketplace root” rather than imply the JSON file's parent directory.

Implicit discovery of a newly created `~/.agents/plugins/marketplace.json` was not tested because doing so would mutate user configuration.

## Security and safety assessment

Positive controls:

- Plugin names are normalized and cannot directly carry path traversal sequences.
- Plugin roots and marketplace paths are resolved explicitly.
- Asset validation rejects absolute paths, `..`, and paths escaping the plugin archive.
- JSON/YAML parsing does not execute arbitrary code.
- Marketplace policy values use constrained CLI choices.

Residual risks:

- User-selected output paths can target arbitrary writable locations by design.
- Direct writes follow normal filesystem behavior, including symlinks, and are not atomic.
- The marketplace updater preserves malformed pre-existing entries and has no full marketplace validator.
- `--category` accepts empty or arbitrary text without validation.

## Recommended repair sequence

1. Establish the Codex copy as source of truth and regenerate/symlink the full `.agent-skills` mirror.
2. Add regression tests before changing behavior, using `test_plugin_creator_audit.py` as the starting defect matrix.
3. Fix the hooks contradiction and cachebuster semver validation.
4. Add transactional preflight/rollback and atomic JSON writes.
5. Enforce folder/name, declared component paths, marketplace root name, and marketplace entry shape.
6. Clarify marketplace-root path resolution and first-use authorization.
7. Run parity, unit, smoke, validation, and Codex CLI integration checks before release.

## Boundaries

- No plugin was installed or removed.
- No marketplace was added, removed, or modified.
- No credentials, history, or private session content were inspected.
- Temporary test fixtures were isolated under the system temporary directory.
