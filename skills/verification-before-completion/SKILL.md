---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, passing, generated, exported, published, or successfully executed, before committing or creating PRs; requires fresh evidence that matches the actual claim, including tests, artifact checks, provider/job status, or release verification as appropriate
---

# Verification Before Completion

## Overview

Claiming work is complete without verification is not efficiency. It is an unsupported assertion.

**Core principle: Evidence before claims, always.**

Verification must match the thing being claimed. A passing linter cannot prove a build; an API response cannot prove a file was persisted; a rendered master cannot prove publication; a mock result cannot prove a provider call occurred.

## The Iron Law

```text
NO COMPLETION CLAIMS WITHOUT FRESH, CLAIM-MATCHED VERIFICATION EVIDENCE
```

If you have not gathered fresh evidence for the actual claim in the current work cycle, you cannot claim it is complete.

## The Gate Function

Before claiming any status or expressing satisfaction:

1. **IDENTIFY** — What observable evidence would prove this exact claim?
2. **RUN / FETCH / INSPECT** — Gather the full fresh evidence.
3. **READ** — Check exit codes, failures, artifact state, job state, and relevant scope.
4. **MATCH** — Does the evidence prove the claim being made?
   - If NO: state the actual status and the gap.
   - If YES: make the claim and cite/report the evidence.
5. **CHECK SCOPE** — Verify every promised output, not merely a representative sample unless sampling was explicitly the acceptance method.
6. **ONLY THEN** — Report completion.

Skip any step and the result is unverified.

## Evidence Depends on the Claim

| Claim | Requires | Not sufficient |
|---|---|---|
| Tests pass | Fresh full test output with 0 failures | Previous run, "should pass" |
| Linter clean | Fresh lint output with 0 errors | Formatter output |
| Build succeeds | Fresh build exit 0 | Linter/tests alone |
| Bug fixed | Original symptom/regression evidence passes | Code changed |
| Requirements met | Requirement-by-requirement acceptance check | Tests alone |
| File generated | File/object exists, is non-empty/valid as applicable | Tool said "success" |
| Batch complete | Every required unit accounted for as success/failure | One sample asset |
| Provider executed | Provider/job evidence from real execution mode | Mock/local/dry-run result |
| Export complete | Exact declared export artifacts exist and validate | Timeline/project exists |
| Published | Destination confirms exact edition/version is live or accepted | Render/upload request started |
| Creative workflow complete | Required manifests/assets/checkpoints/evaluations satisfy scope | Attractive preview |
| Research complete | Requested questions covered and source/evidence requirements met | Search performed |
| Agent completed | VCS/artifact diff plus independent verification | Agent reports "success" |

## Execution-Mode Truthfulness

Always preserve the distinction between:

- provider/live execution
- local execution
- mock execution
- dry-run/compiled request
- planning/specification only

Never upgrade one mode into another in the completion report.

Examples:

```text
✅ "Dry-run compiled 24 render requests; no provider execution was performed."
❌ "Generated 24 shots" when only requests/specs exist.

✅ "Provider job 123 completed and returned asset A; asset A was persisted and validated."
❌ "Asset complete" because the submit call returned 200.
```

## Artifact Verification

For workflows that produce artifacts, identify the promised artifact set before verifying.

For local files, check as applicable:

- exact expected path
- existence
- non-zero size
- parseability or media validity
- dimensions/duration/type where contractual
- checksum when required

For remote/durable objects, check as applicable:

- stable asset/job identifier
- completed status
- retrievability through the owning system
- expected metadata/type/version
- persistence beyond a transient response URL when durable output was promised

A transient provider URL is not automatically durable identity.

## Partial Work and Checkpoints

Partial completion is a valid state. Do not hide it.

For a multi-unit or long-running workflow report:

```yaml
verification_summary:
  requested: 24
  completed: 21
  failed: 2
  blocked: 1
  checkpoint: render-motion
  failures:
    - shot-017
    - shot-021
  blocked_items:
    - shot-023
```

Preserve enough checkpoint information to resume without reconstructing state from chat.

## Creative and Media Verification

Generation success and creative approval are different gates.

When the workflow defines evaluation/approval, verify both separately:

1. **Execution gate** — the requested asset was actually produced.
2. **Contract gate** — required dimensions, references, identity/canon anchors, timing, text, etc. were respected.
3. **Evaluation gate** — continuity/quality review occurred where required.
4. **Approval gate** — the artifact has the explicit status required for release/use.

Do not call an asset approved merely because it rendered.

For transforms, verify source/parent lineage is retained when the surrounding system requires provenance.

## Git / Pull Request Verification

Before a commit or PR completion claim:

1. Inspect the actual changed-file list/diff.
2. Confirm only intended files changed.
3. Run the strongest available repository validation.
4. Check workflow/CI status when CI exists and has run.
5. If CI has not run or no runnable environment is available, say exactly what was and was not verified.

Do not claim "CI passes" when CI is absent, pending, skipped, or inaccessible.

## Regression Tests

For a regression claim, prefer a red-green verification cycle when practical:

```text
write test -> run with fix (pass)
reproduce/revert fix or otherwise prove test catches original fault (fail)
restore fix -> run again (pass)
```

A test that only passes once does not prove it would have caught the regression.

## Red Flags

Stop if you are about to:

- say "should", "probably", or "seems" as a substitute for evidence
- express satisfaction before verification
- commit/push/open a PR without inspecting the changes
- trust an agent/tool/provider success message without independent evidence appropriate to the claim
- rely on a partial check while reporting the whole scope complete
- equate spec generation with asset generation
- equate render completion with approval
- equate upload with publication
- equate mock/dry-run with provider execution
- hide failed units inside a successful batch total
- say a workflow is reproducible without preserving its required manifests/config/identity

## Rationalization Prevention

| Excuse | Reality |
|---|---|
| "Should work now" | Gather the proof. |
| "I'm confident" | Confidence is not evidence. |
| "The tool returned success" | Verify the promised output. |
| "The provider URL opens" | That may still be transient. |
| "The preview looks right" | Check the contract and scope. |
| "Most units passed" | Report the failures and checkpoint. |
| "The agent said it was done" | Verify independently. |
| "Tests pass, so requirements are done" | Check requirements too. |
| "CI will catch it" | Inspect current CI state; don't predict it. |

## Shared Workflow Contract

For skills using structured handoffs/checkpoints, align verification with `docs/SKILL_WORKFLOW_CONTRACT.md`.

The verification skill does not redefine each domain's acceptance criteria. It enforces that the criteria promised by that domain workflow are actually checked before completion is claimed.

## The Bottom Line

**No shortcuts for verification. Match evidence to the claim.**

Run, fetch, inspect, and validate what proves the actual result. Report partial states truthfully. Then, and only then, claim completion.
