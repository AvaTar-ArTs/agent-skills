# Plugin Creator Review

Date: 2026-08-08  
Scope: canonical Codex `plugin-creator` skill, mirrored agent-skills copy, scripts, references, and marketplace behavior.

## Executive result

The skill is well-structured and its Codex and `.agent-skills` copies are byte-identical. The metadata files also match. The review found workflow reliability and environment-integration issues that should be fixed before treating the skill as production-grade.

## Findings

### High — personal marketplace path is not provisioned here

The documented default is `~/.agents/plugins/marketplace.json`, but that path does not currently exist in this environment. A default `--with-marketplace` smoke test failed while attempting to create `~/.agents`.

This is an environment integration issue, not proof that the path is invalid in every Codex installation. The skill should either provision/verify this destination explicitly or document the local canonical marketplace path used by this installation.

### High — partial scaffold remains after marketplace failure

`create_basic_plugin.py` creates the plugin directory and manifest before updating the marketplace. If marketplace creation fails, the plugin remains partially created without the requested marketplace entry.

Recommended fix: stage the marketplace update and plugin creation transactionally, or provide rollback on failure and report the exact retained path.

### Medium — marketplace source-path semantics need an executable check

The skill hardcodes `./plugins/<plugin-name>` while the default plugin directory is `~/plugins/<plugin-name>` and the marketplace file is `~/.agents/plugins/marketplace.json`. The reference says Codex resolves this convention specially, but the script itself does not verify that the referenced source exists.

Recommended fix: add a preflight that resolves and checks the marketplace source path according to Codex semantics, with a smoke test for both personal and repo-local marketplaces.

### Medium — validator does not enforce folder/name identity

The skill requires the outer folder name and `plugin.json.name` to match, but `validate_plugin.py` only checks that `name` is a non-empty string. A malformed plugin can therefore pass validation despite violating the documented invariant.

### Medium — force writes are not recoverable

`--force` can overwrite an existing plugin manifest or marketplace entry. Writes are direct rather than atomic and no backup is created. A failed or interrupted write could leave invalid JSON.

### Low — no bundled automated tests

The skill contains scripts and references but no dedicated test suite. Current validation covers manifest structure, not end-to-end marketplace creation, rollback, path resolution, or cachebuster/reinstall behavior.

## Verified strengths

- Codex and `.agent-skills` `SKILL.md` files match byte-for-byte.
- Codex and `.agent-skills` `openai.yaml` metadata match byte-for-byte.
- Explicit temporary-marketplace smoke test created and validated a plugin successfully.
- Validator checks strict semver, required metadata, URL schemes, assets, unsupported fields, and TODO markers.
- Marketplace policy defaults and overwrite behavior are documented clearly.

## Recommended repair order

1. Confirm and provision the canonical personal marketplace location.
2. Add rollback or atomic staging for scaffold plus marketplace creation.
3. Enforce folder-name/manifest-name equality.
4. Add personal and repo-local marketplace smoke tests.
5. Add safe backup/atomic replacement behavior for `--force`.

## Limitations

This was a static and executable smoke review. It did not install a plugin into Codex, call external services, inspect credentials, or modify the skill source.
