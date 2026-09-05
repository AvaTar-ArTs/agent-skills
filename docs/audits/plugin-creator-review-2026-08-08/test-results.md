# Plugin Creator Audit Test Results

Date: 2026-08-08

## Validation

- Python compilation: passed for all four canonical scripts and the audit harness.
- Skill structure validation: passed.
- Codex CLI command compatibility: `plugin add`, `plugin list`, `plugin marketplace add`, and `plugin marketplace list` are present in `codex-cli 0.147.0`.
- Ruff: 13 findings; no automatic fixes applied.

## Regression probes

Seven tests ran and passed in 2.448 seconds:

1. Default scaffold validates despite its declared `skills/` directory being absent.
2. Full optional scaffold validates.
3. Folder/manifest name mismatch passes validation.
4. Duplicate marketplace failure leaves the second plugin scaffold.
5. Existing marketplace without a top-level name is accepted.
6. Invalid semver base is rewritten successfully and then rejected by validation.
7. Name normalization succeeds while empty and overlength names fail.

“Passed” means each probe observed the current behavior it was designed to test. It does not mean every observed behavior is desirable.
