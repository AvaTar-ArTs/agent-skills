# Skill Workflow Contract

This document defines the shared semantic boundary between reusable agent skills, workflow orchestration, execution tools, provider backends, and durable memory.

The goal is interoperability without turning `agent-skills` into a provider SDK or a second CreativeOS implementation.

## Layer boundaries

| Layer | Responsibility | Must not own |
|---|---|---|
| Skill | How to reason about and conduct a task | Provider-specific transport |
| Workflow | Ordered semantic operations, gates, checkpoints | Canonical provider credentials |
| Tool / MCP | Exposed semantic capability | Creative intent or canon authority |
| Provider backend | Concrete execution against local or hosted systems | Skill-selection policy |
| Durable memory / Content Universe | IDs, evidence, provenance, lineage, checkpoints | Provider-specific behavior |

Skill routing and provider routing are different decisions. A skill decides **how the task should be approached**. A provider router decides **where an already-defined semantic operation should execute**.

## Minimum skill contract

Every new or substantially revised workflow skill should make these concepts explicit, either in frontmatter or in a clearly labeled contract section:

- **Identity**: stable skill name and purpose.
- **Triggers**: situations that should cause the skill to be considered.
- **Inputs**: required and optional user, project, canon, or artifact inputs.
- **Outputs**: artifacts or decisions produced by the skill.
- **Dependencies**: skills or semantic capabilities that must precede or accompany it.
- **Tool bindings**: capabilities the skill may call without hard-coding a provider when provider-neutral execution is possible.
- **Provider boundary**: what belongs to a concrete backend rather than the skill.
- **Verification**: observable evidence required before completion can be claimed.
- **Artifacts**: files, manifests, graphs, reports, or media that must be persisted.
- **Checkpoints**: resumable states for workflows that may be interrupted or partially fail.

## Recommended machine-readable shape

This is a portable conceptual schema, not a requirement to introduce a runtime dependency:

```yaml
skill_contract:
  version: 1
  id: creative.music-to-video
  kind: creative-workflow
  triggers: []
  inputs: []
  outputs: []
  dependencies: []
  semantic_capabilities: []
  provider_constraints: []
  verification: []
  artifacts: []
  checkpoints: []
```

Use stable semantic names for outputs where an external system already defines them. Examples include `SceneGraph`, `ShotManifest`, `PromptManifest`, `MusicWorldBible`, `MusicIdentityManifest`, `ProviderJob`, and `RenderCheckpoint`.

These names are interoperability hooks, not permission for the skill repository to redefine external schemas.

## Handoff envelope

When one skill hands work to another, prefer a compact explicit envelope over prose-only context:

```yaml
handoff:
  from_skill: brainstorming
  to_skill: writing-plans
  intent: "What is being built or changed"
  approved_approach: "Chosen design"
  constraints: []
  protected_invariants: []
  source_artifacts: []
  required_outputs: []
  unresolved_questions: []
  verification_requirements: []
```

For creative pipelines, also carry canonical IDs or source references when available. Never silently replace an existing approved artifact with a newly inferred one.

## Checkpoint model

Long or multi-provider workflows should define named checkpoints. A checkpoint records enough information to resume without pretending failed or incomplete stages succeeded.

Minimum checkpoint fields:

```yaml
checkpoint:
  id: "stable-run-local-id"
  workflow: "skill/workflow identifier"
  stage: "current semantic stage"
  completed: []
  remaining: []
  artifact_ids: []
  attempt: 1
  last_error: null
```

A checkpoint is workflow state, not a success claim.

## Verification rules

1. Invoke `verification-before-completion` before claiming a workflow is complete.
2. Verify the artifacts promised by the skill, not merely that a tool call returned.
3. Provider, local, mock, and dry-run execution must remain distinguishable.
4. Partial failures must be surfaced and checkpointed.
5. A provider URL or transient response is not durable identity.
6. Preserve source and parent lineage for transforms, remixes, edits, and derived media.
7. Do not overwrite original user prompts, canon, source lyrics, or approved manifests during enhancement.

## Creative workflow invariants

Creative skills should preserve these boundaries whenever relevant:

- Canon or identity belongs to the project/canon layer, not to a generation provider.
- Authoring references, generation references, evaluation references, and continuity references are different roles.
- Scene-level intent and shot-level render instructions are different abstraction levels.
- The same entity may appear multiple times in a scene; appearances must not collapse into one instance.
- A generated artifact is not approved merely because generation succeeded.
- Release or publishing steps should point to exact approved artifact/version identifiers when such identifiers exist.

## Meta-routing pattern

The preferred high-level flow is:

```text
user intent
  -> applicable-skill discovery
  -> process skill (brainstorming/debugging/research as needed)
  -> approved design / structured handoff
  -> implementation or creative workflow skill
  -> semantic tool operations
  -> provider backend(s)
  -> durable artifacts + provenance
  -> verification
  -> completion report
```

This contract intentionally leaves execution technology open. A compatible workflow may use MCP, a CLI, a local script, a hosted provider, a human production step, or a combination of them.