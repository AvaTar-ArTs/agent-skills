---
name: structured-asset-pipeline
description: "Generic structured asset pipeline for reproducible multi-unit image, audio, and video generation via contract-first adapters or semantic provider backends. Use for batch generation, comic pages, album art, voiceovers, music tracks, storyboard-to-assets, shot manifests, regenerate unit N, or generate-from-spec workflows."
version: 1.1.0
license: MIT
metadata:
  tags: [pipeline, image-generation, audio-generation, video-generation, adapters, creative, provenance]
---

# structured-asset-pipeline

Generic, reproducible multi-asset production:

```text
source/content
  -> analysis
  -> unit specs
  -> approval gate
  -> semantic operation / adapter / backend
  -> durable asset records
  -> verification
  -> report + checkpoint
```

The skill owns **unit discipline, reproducibility, persistence, and verification**. It does not own canon, provider-specific creative semantics, or the higher-level story/music reasoning supplied by domain skills.

## Contract boundary

See `docs/SKILL_WORKFLOW_CONTRACT.md`.

```yaml
skill_contract:
  version: 1
  id: creative.structured-asset-pipeline
  kind: execution-workflow
  inputs:
    - source content or approved unit manifests
    - output scope
    - execution constraints
    - optional reference assets with typed roles
  outputs:
    - unit specifications
    - provider/local job records when execution occurs
    - durable asset references
    - verification report
    - resumable checkpoint
  dependencies:
    - verification-before-completion
  semantic_capabilities:
    - compile unit spec
    - submit/generate unit
    - persist result
    - regenerate unit
    - verify artifact
  provider_constraints:
    - never infer provider success from mock/dry-run
    - never silently change semantic operation kind
    - never silently change protected unit fields
```

## When to use

Use this skill when the user wants to:

- generate a **batch or series** of images, clips, audio, pages, shots, covers, or mockups
- execute an approved `ShotManifest`/unit inventory
- produce **reproducible** outputs that can be partially regenerated
- regenerate specific units from preserved specs
- run local or hosted generation while keeping provider differences behind an adapter/backend boundary
- preserve enough provenance and checkpoint state for another agent to continue

**When not to use:** A single one-off asset with no reproducibility, lineage, or batch need. A lone artifact does not automatically justify a manifest.

## Provider and execution modes

Provider choice is downstream of the semantic unit definition.

Supported conceptual modes:

```text
provider/live
local
mock
dry-run
planning-only
```

These modes must remain distinguishable in logs and completion reports.

A provider may be reached through:

- MCP/tool binding
- provider SDK/API
- local backend such as ComfyUI
- CLI adapter
- orchestrator supplied by the host system

Do not make the workflow definition depend on one transport.

## Run directory layout

When the host workflow is filesystem-based, use a layout like:

```text
assets/{slug}/
├── source-{slug}.md
├── analysis.md
├── plan.md
├── characters/            # optional canonical identity descriptions/manifests
├── refs/                  # typed reference assets/provenance records
├── specs/
│   ├── 00-meta.yaml
│   └── NN-{kind}-{slug}.yaml
├── prompts/               # optional human-readable prompt/revision dumps
├── out/                   # persisted local outputs when local files are promised
├── logs/run.jsonl
├── checkpoints/
│   └── latest.yaml
└── report.md
```

A remote-first host may persist equivalent objects in a durable graph/store instead. Do not invent local files just to mimic this layout if the authoritative system already provides durable artifact identities.

## Progress checklist

```text
Pipeline Progress:
- [ ] Step 1: Intake + secret strip + source inventory
- [ ] Step 2: Analyze or import authoritative analysis
- [ ] Step 3: Plan/import unit specs
- [ ] Step 4: Confirm execution mode, backend constraints, scope, and review gates
- [ ] Step 5: Optional spec/keyframe review
- [ ] Step 6: Execute via semantic tool, adapter, or provider backend
- [ ] Step 7: Persist + verify every required result
- [ ] Step 8: Evaluate/approve where the domain workflow requires it
- [ ] Step 9: Report + checkpoint
```

## Hard rules (R1–R16)

| Rule | Summary |
|---|---|
| R1 | Persist or durably identify the unit spec before execution. |
| R2 | Filesystem adapters use absolute paths; never rely on CWD. |
| R3 | Verify every promised output in the persistence model actually used. |
| R4 | Preserve prior versions before regenerate; never silently destroy lineage. |
| R5 | Respect the domain/user approval gate before paid, destructive, or expensive execution. |
| R6 | Make defaults visible; do not conceal consequential inferred values. |
| R7 | Strip secrets from source artifacts, logs, prompts, and manifests. |
| R8 | References use explicit roles and provenance; text anchors and reference assets are both valid when supported. |
| R9 | Partial workflows and partial failures are first-class and resumable. |
| R10 | Provider-specific transport belongs behind one adapter/backend boundary. |
| R11 | Preserve machine-readable failure categories/status even when transport-specific exit codes differ. |
| R12 | Never claim success from a transient response alone; verify the promised durable result. |
| R13 | Never claim provider/live execution from mock, local, dry-run, or planning output. |
| R14 | Do not silently change operation kind, identity/canon anchors, dimensions, seed policy, model family, or adapter weights when contractual. |
| R15 | Generation success and creative approval are separate statuses. |
| R16 | Preserve source/parent lineage for derived, edited, remixed, reframed, upscaled, or composite assets. |

## Typed references

The earlier pipeline treated text descriptions as the only safe consistency mechanism. That is too narrow for modern creative systems.

Use the strongest references allowed by the chosen backend and rights context, while making their role explicit.

Recommended reference roles:

```yaml
references:
  - id: character-canon-01
    role: continuity
    source: "durable asset or manifest id"
  - id: pose-07
    role: generation
    source: "reference asset id"
  - id: target-quality-02
    role: evaluation
    source: "approved example id"
```

Keep at least these conceptual roles distinct when applicable:

- **authoring** — helps design the requested artifact
- **generation** — supplied to or used by the executor
- **evaluation** — used to judge the result
- **continuity** — protects recurring identity/state across units

Do not assume every provider supports every reference role. Provider capability is an execution concern.

## Unit specification

A unit spec should contain only the fields required to reproduce and verify that unit, plus references to higher-level canonical artifacts rather than copied competing truth.

Example:

```yaml
unit:
  unit_id: scene-01-shot-004
  kind: image
  operation: generate
  prompt_manifest_ref: prompt-019
  scene_ref: scene-01
  shot_manifest_ref: shot-004
  reference_ids: [character-canon-01, pose-07]
  protected_fields:
    dimensions: [1920, 1080]
    seed_policy: locked
  output_requirements:
    format: png
    width: 1920
    height: 1080
  execution:
    mode: provider
    backend: null
```

For music/video/domain-specific work, use the canonical higher-level schema supplied by that domain skill or host system rather than forcing everything into this example.

## Step 1: Intake

- inventory source material
- identify authoritative vs reference vs inferred inputs
- strip credentials/session material from persisted sources
- preserve stable source IDs where available
- record rights/license restrictions when supplied by the surrounding workflow

## Step 2: Analyze or import analysis

Do not redo authoritative analysis merely because this pipeline can analyze content.

Examples:

- a `music-to-video` workflow may already provide a `CueMap` and `ShotManifest`
- a comic workflow may already provide panel/layout contracts
- a canon system may already provide character/location identity manifests

Reuse them and record their identifiers.

## Step 3: Plan units

Compile the approved domain plan into execution units.

Each unit must have:

- stable local or canonical ID
- semantic operation kind
- required inputs/references
- protected constraints
- expected output(s)
- verification criteria
- dependency ordering when relevant

Repeated appearances of the same entity remain distinct unit/scene instances.

## Step 4: Confirm execution

Before paid/destructive execution, confirm or inherit an already-approved decision for:

- scope/unit count
- execution mode
- backend/provider constraints
- cost/budget boundaries when relevant
- review gates
- regeneration/overwrite policy
- output persistence target

An explicit approval already given to the upstream domain workflow counts. Do not manufacture a redundant approval loop.

Use dry-run/compile mode where available to validate requests before spending provider credits.

## Step 5: Optional review

Domain workflows may require reviewing:

- specs
- prompt manifests
- keyframes
- contact sheets
- character identity consistency
- license/rights gates

This skill honors those gates but does not redefine them.

## Step 6: Execute

Execution may happen through an adapter, MCP semantic tool, local backend, or provider SDK.

For filesystem CLI adapters:

```bash
python /absolute/path/to/adapter.py \
  --spec /absolute/run/specs/01-cover.yaml \
  --out  /absolute/run/out/01-cover.png
```

For semantic/provider systems, record equivalent request/job/result identifiers rather than pretending the CLI shape is universal.

After submit:

1. capture job/request identity
2. wait/poll only as the host/tool supports
3. capture result identity/status
4. persist the promised artifact
5. verify the promised artifact
6. record provenance/lineage
7. checkpoint progress

## Failure model

Preserve machine-readable failure categories. Recommended portable categories:

```text
invalid-input
auth
network
provider-error
unsupported
persistence-failure
verification-failure
rights-or-license-block
cancelled
partial
```

A legacy CLI adapter may still use numeric exit codes, for example:

```text
0 ok
1 invalid
2 auth
3 api/network
4 verify-fail
5 unsupported
```

Map transport-specific errors into the portable category in the run log/report.

Retry only when the error is plausibly transient and the domain/provider policy allows it. Never silently retry a destructive or expensive operation indefinitely.

## Regeneration

Regeneration is a transform/new attempt, not an erasure of history.

Before regenerating:

- retain the prior asset/version ID
- record why regeneration was requested
- retain source/parent linkage
- preserve or explicitly change protected fields
- create a new attempt/job record

Filesystem fallback:

```text
01-cover.png
01-cover-backup-YYYYMMDD-HHMMSS.png
```

A durable asset store should prefer versioned IDs over filename-only backup semantics.

## Verification

Invoke `verification-before-completion` before saying the batch is complete.

For every required unit verify the actual promised representation:

### Local file

- exists at exact path
- non-empty
- parseable/valid media when applicable
- required dimensions/duration/type match

### Remote/durable asset

- stable asset ID exists
- result/job status is complete
- asset is retrievable from the owning system
- expected metadata/type/version match
- transient URL is not the only identity when durable persistence was promised

Then separately record domain evaluation/approval status if required.

## Checkpoint

Long/multi-unit runs should write or persist a checkpoint like:

```yaml
checkpoint:
  id: run-2026-08-17-001
  workflow: creative.structured-asset-pipeline
  stage: execute
  total: 24
  completed: [shot-001, shot-002]
  failed: [shot-003]
  remaining: [shot-004]
  artifact_ids: []
  attempt: 1
  last_error: "shot-003: provider-error"
```

A checkpoint is not a completion claim.

## Completion report

The report must account for the whole approved scope:

```yaml
completion:
  execution_mode: provider
  requested: 24
  completed: 21
  failed: 2
  blocked: 1
  verified_assets: []
  unverified_assets: []
  evaluation_status: partial
  checkpoint_ref: run-2026-08-17-001
```

Never hide failures inside a successful batch narrative.

## Relationship to domain skills

### `creative/music-to-video`

Owns musical analysis, audiovisual mapping, SceneGraph/shot planning, continuity, edit, and evaluation. This pipeline can execute its approved keyframe/clip units reproducibly.

### `creative/songwriting-and-ai-music`

Owns songwriting/music craft. This pipeline can execute approved track variants or derivative unit specs, but should not silently rewrite the song identity.

### `creative/comfyui`

Can act as a local backend when the unit's semantic operation and protected fields have already been defined.

## Pitfalls

1. **CWD drift** — filesystem adapters must use absolute paths.
2. **Transient URL mistaken for artifact** — persist/verify the promised durable output.
3. **Overwrite disguised as regeneration** — preserve version/lineage.
4. **Secrets in source prompts/logs** — strip credentials and session material.
5. **Reference-role collapse** — authoring, generation, evaluation, and continuity are not interchangeable.
6. **Provider semantics leaking upward** — keep transport details behind the adapter/backend.
7. **Mock/live confusion** — execution mode must remain truthful.
8. **Generation = approval** — false; evaluation/approval is a separate gate.
9. **Silent protected-field drift** — surface changes to seed, dimensions, model family, adapter weights, or identity anchors.
10. **Spec-only completion** — planning/spec generation does not equal media generation unless that was the requested scope.

## Future extensions

This pipeline is intentionally generic. Domain-specific skills should build on it rather than accrete into one giant generation skill.

Useful future adapters/bridges include:

- canonical `ShotManifest` -> unit compilation
- `ProviderJob` / `RenderCheckpoint` persistence
- Content Universe artifact/provenance bridge
- provider capability negotiation
- license/rights preflight gates
- distributed or parallel unit scheduling
- contact-sheet/evaluation-grid automation
