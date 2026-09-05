# Skill Workflow Convergence Design

Date: 2026-08-17
Status: approved for implementation by explicit user request to apply the previously proposed workflow improvements

## Objective

Evolve `agent-skills` from a collection of useful behavioral instructions into a more interoperable process layer that can coordinate planning, creative production, semantic tools/MCPs, provider backends, durable artifacts, and verification without duplicating provider SDKs or external canonical schemas.

## Design decisions

### 1. Keep skill routing separate from provider routing

A skill answers how the task should be approached. A provider router answers where a defined operation should execute. Tools/MCPs sit between those layers as capability interfaces.

Preferred flow:

```text
user intent
  -> skill discovery
  -> process/domain workflow
  -> semantic operation
  -> tool/MCP
  -> provider/local backend
  -> artifacts/provenance
  -> verification
```

### 2. Preserve the existing superpowers methodology

`using-superpowers` remains the authority for skill discovery. `brainstorming` remains the design gate for unresolved work. The changes refine rather than replace those methods.

### 3. Recognize already-approved design

The prior brainstorming rule required a new approval cycle for every implementation. The revised rule treats explicit user approval or a supplied approved specification as satisfying the design gate. This avoids redundant clarification while retaining a structured handoff.

### 4. Add a repository-wide skill workflow contract

`docs/SKILL_WORKFLOW_CONTRACT.md` defines portable concepts for:

- identity and triggers
- inputs/outputs
- dependencies
- semantic capabilities
- tool/provider boundaries
- verification
- artifacts
- checkpoints
- cross-skill handoffs

The contract references external semantic artifact names when useful but does not redefine their external schemas.

### 5. Add `creative/music-to-video`

The new domain workflow consumes an existing approved song/cue and any existing music identity/canon artifacts. It converts musical structure into a visual narrative, SceneGraph-equivalent scene plan, ShotManifest-equivalent shot plan, render-ready units, evaluation, export, and archive state.

Its canonical phases are:

1. Ingest
2. Analyze music
3. Extract structure
4. Map story/lyrics
5. Define visual language
6. Build SceneGraph
7. Build ShotManifest
8. Generate/select keyframes
9. Generate motion
10. Synchronize to audio
11. Continuity check
12. Edit
13. Evaluate
14. Export
15. Publish
16. Archive

### 6. Provider-neutral by default

The workflow can be executed through hosted providers, local ComfyUI or other graph systems, editing tools, MCPs, CLIs, or human steps. The skill owns audiovisual reasoning and workflow gates, not provider transport.

### 7. Verification and lineage are required

Completion means promised outputs were verified, not merely that generation calls returned. Partial failures are checkpointed. Derived assets retain source/parent lineage when the surrounding toolchain supports durable identity.

## Compatibility

- Existing skill loaders continue to use `SKILL.md` frontmatter and Markdown.
- No new runtime dependency is introduced.
- The machine-readable examples are optional semantic conventions.
- Existing creative execution skills remain valid and can serve as downstream helpers.
- External schemas such as SceneGraph or ShotManifest remain owned by their canonical systems.

## Acceptance criteria

- `using-superpowers` explains skill/workflow/tool/provider separation and structured handoff discipline.
- `brainstorming` supports approved-design recognition, authoritative inputs, ambiguity classification, and a structured handoff.
- `docs/SKILL_WORKFLOW_CONTRACT.md` documents the shared contract.
- `skills/creative/music-to-video/SKILL.md` exists with provider-neutral 16-phase production flow, checkpoints, invariants, and verification gate.
- Repository index exposes the new workflow entry points.
- PR diff is reviewed before completion is claimed.