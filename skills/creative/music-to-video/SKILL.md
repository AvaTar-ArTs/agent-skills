---
name: music-to-video
description: "Turn an existing song, cue, soundtrack, or approved music identity into a reproducible visual narrative and video-production plan. Use for music videos, lyric-driven visual stories, song-to-storyboard work, beat-synced shot planning, or multi-provider audio-to-video pipelines."
version: 1.0.0
license: MIT
metadata:
  tags: [music-video, storyboard, scenegraph, shot-manifest, creative, video, audio]
triggers:
  - music video
  - song to video
  - turn this song into visuals
  - storyboard this track
  - make shots from lyrics
  - beat synced video
  - visualize this soundtrack
---

# Music to Video

Convert music into a visual production system without flattening the track into a pile of unrelated image prompts.

The song is both narrative source and timing grammar. Musical structure, lyrical events, motifs, dynamics, instrumentation, silence, transitions, and recurring identities should shape the visual plan.

## Contract

```yaml
skill_contract:
  version: 1
  id: creative.music-to-video
  kind: creative-workflow
  dependencies:
    - brainstorming when visual direction is unresolved
    - verification-before-completion before any completion claim
  optional_dependencies:
    - creative/songwriting-and-ai-music
    - creative/structured-asset-pipeline
  inputs:
    - approved audio or durable audio reference
    - lyrics or transcript when available
    - project/canon context when available
    - MusicWorldBible when available
    - MusicIdentityManifest when available
    - stems, BPM, key, section map, or analysis when available
    - visual references and continuity anchors when available
  outputs:
    - MusicVisualAnalysis
    - CueMap
    - VisualDirection
    - SceneGraph or equivalent scene plan
    - ShotManifest or equivalent shot plan
    - RenderPlan-ready shot specifications
    - EvaluationReport
    - ExportManifest
  semantic_capabilities:
    - analyze audio
    - map song structure
    - plan scenes
    - plan shots
    - generate or select keyframes
    - generate motion
    - synchronize edit to audio
    - evaluate continuity
    - export and archive
  provider_constraints:
    - remain provider-neutral until execution
    - never claim provider execution from mock, local planning, or dry-run output
    - never silently substitute one operation for another
  verification:
    - promised artifacts exist
    - timeline covers intended track duration or explicitly declared excerpt
    - shot identifiers are unique
    - source/canon anchors are preserved
    - partial failures are surfaced
    - final completion claim passes verification-before-completion
  checkpoints:
    - intake
    - music-analysis
    - visual-direction
    - scene-plan
    - shot-plan
    - keyframes
    - motion
    - edit
    - evaluation
    - export
```

See `docs/SKILL_WORKFLOW_CONTRACT.md` for the shared boundary between skills, workflows, tools, providers, and durable memory.

## Non-negotiable invariants

1. **Do not re-invent approved music identity.** If `MusicWorldBible`, `MusicIdentityManifest`, approved lyrics, motif definitions, stems, or prior analysis exist, consume them before deriving replacements.
2. **Do not overwrite source truth.** Enhancements and visual interpretations must be new revisions or derived artifacts, not silent mutations of lyrics, canon, prompt history, or approved manifests.
3. **Skill routing is not provider routing.** This skill defines the creative process. Concrete image, video, audio, local-render, or editing providers are chosen later.
4. **Scene intent and shot execution are different layers.** A `SceneGraph` expresses narrative/visual state; a `ShotManifest` expresses camera- and render-level units.
5. **Repeated entities remain repeated instances.** Do not collapse multiple appearances of the same character, object, symbol, or location into one scene instance.
6. **Generation is not approval.** Generated media must pass continuity/evaluation gates before release or archive status is treated as approved.
7. **Partial completion stays partial.** Save checkpoints and failed-unit state instead of claiming the whole video succeeded.
8. **Preserve lineage.** Derived keyframes, clips, edits, upscales, remixes, reframes, and composites retain source/parent references when supported.

## Before starting

Collect the strongest available source set in this order:

1. Approved/final audio or exact track version.
2. Existing music identity artifacts (`MusicWorldBible`, `MusicIdentityManifest`, cue bible, motif map).
3. Lyrics, transcript, section labels, BPM/key, stems, MIDI, waveform markers, or provider metadata.
4. Project canon, character/location identity anchors, rights restrictions, adaptation constraints.
5. Existing storyboard, visual language, palette, StyleDNA, SceneGraph, or reference assets.
6. Output constraints: aspect ratio, duration, platform, frame rate, resolution, budget, backend limits.

If an authoritative artifact already contains a value, reuse it and cite/reference it in the plan rather than guessing a new value.

## The 16-phase workflow

### 01. Ingest

Create a source inventory. Distinguish authoritative inputs from references and newly inferred analysis.

Record at minimum:

```yaml
source_inventory:
  track_id: null
  track_version: null
  duration: null
  lyrics_ref: null
  music_world_bible_ref: null
  music_identity_manifest_ref: null
  canon_refs: []
  visual_refs: []
  rights_or_license_refs: []
```

Checkpoint: `intake`.

### 02. Analyze music

Analyze only what is not already authoritatively supplied.

Useful dimensions:

- duration and time base
- tempo/BPM and meter when meaningful
- key/harmonic center when useful
- instrumentation and vocal identities
- energy curve
- density and spectral changes
- major transitions, drops, breaks, solos, silences
- recurring musical motifs
- emotional trajectory
- stem-specific events when stems exist

Mark each analytical claim as observed, supplied, or inferred when provenance matters.

### 03. Extract structure

Build a time-coded section map.

```yaml
sections:
  - id: intro
    start: 0.0
    end: 12.4
    energy: 2
    lyric_event: null
    musical_events: []
    motifs: []
```

Do not force verse/chorus grammar onto music that uses another form. Instrumental, ambient, through-composed, electronic, game-score, and experimental tracks need their own structural language.

### 04. Map story and lyrics

Translate the track into visual beats without requiring every lyric to become a literal shot.

For each section identify:

- narrative purpose
- lyric event or subtext
- character state
- setting/world state
- reveal or unresolved question
- recurring symbol/motif
- continuity requirements
- desired degree of literalness

Choose among literal, metaphorical, performance, abstract, documentary, hybrid, or other appropriate visual modes per section.

### 05. Define visual language

If visual direction is unresolved, invoke `brainstorming` before production planning.

Freeze an approved `VisualDirection` that may include:

```yaml
visual_direction:
  premise: ""
  format: narrative|performance|abstract|hybrid
  palette: []
  texture: []
  lighting: []
  camera_language: []
  editing_language: []
  typography: []
  protected_identity_anchors: []
  negative_anchors: []
  recurring_visual_motifs: []
```

Checkpoint: `visual-direction`.

### 06. Build SceneGraph

Create scene-level narrative/visual state before individual shots.

Each scene should capture:

- stable scene ID
- time range / song sections served
- location and environment state
- entity instances and canonical identity references
- action/emotion
- reader/viewer knowledge state when narrative
- visual motifs
- continuity anchors
- source/canon references
- intended transitions

If an external system supplies a canonical `SceneGraph` schema, use that schema rather than redefining it here.

Checkpoint: `scene-plan`.

### 07. Build ShotManifest

Compile each scene into unique shot units.

Minimum conceptual fields:

```yaml
shot:
  shot_id: "scene-01-shot-001"
  scene_id: "scene-01"
  start: 12.4
  end: 15.1
  framing: ""
  camera: ""
  action: ""
  emotion: ""
  characters: []
  location_ref: null
  style_profile_ref: null
  reference_ids: []
  continuity_anchors: []
  seed_policy: null
  output_requirements: {}
  review_status: planned
```

The manifest should be compilable into concrete provider/local `RenderPlan` requests without letting the provider rewrite canon or identity.

Checkpoint: `shot-plan`.

### 08. Generate or select keyframes

Use approved shots to create/select visual anchors.

Prefer representative keyframes before expensive full-motion generation. Evaluate:

- identity consistency
- composition
- environment continuity
- palette/style fidelity
- required props/symbols
- text safety if typography is present
- compatibility with planned motion

Persist exact prompt/manifests, reference roles, provider/local mode, job IDs, model/workflow identifiers, seeds when available, and resulting asset IDs.

Checkpoint: `keyframes`.

### 09. Generate motion

Generate or assemble motion only from approved shot intent and keyframes where used.

Backends may include hosted video providers, local ComfyUI workflows, animation tools, 3D, procedural systems, motion graphics, human editing, or combinations.

A backend must not silently change protected identity anchors, model family, adapter weights, seed policy, dimensions, or semantic operation kind where those are contractual inputs.

Checkpoint: `motion`.

### 10. Synchronize to audio

Build the editorial timeline from musical events, not merely equal clip lengths.

Useful sync strategies:

- phrase boundaries
- downbeats and pickups
- drum/transient accents
- harmonic changes
- lyric entrances
- sustained-note holds
- breakdowns and silences
- motif recurrence
- energy ramps

Do not over-cut simply because beats exist. Visual rhythm can intentionally counterpoint the music.

### 11. Continuity check

Audit across neighboring and recurring shots:

- character identity
- wardrobe/state
- location topology
- props
- lighting/time-of-day
- visual motifs
- screen direction
- typography
- color story
- camera grammar
- narrative causality

Record continuity failures as actionable shot IDs, not vague aesthetic criticism.

### 12. Edit

Assemble the actual or planned timeline with transitions, overlays, titles, effects, speed changes, and audio treatment.

Preserve source clip IDs and transformation lineage. An edit decision should be traceable to its inputs when the toolchain supports durable metadata.

Checkpoint: `edit`.

### 13. Evaluate

Evaluate separately from generation.

Recommended lenses:

- music/visual synchronization
- narrative clarity
- emotional arc
- character/canon continuity
- visual coherence without monotony
- shot usefulness
- artifact defects
- typography/readability
- platform-safe framing
- rights/license constraints
- release requirements

Distinguish objective failures, contract failures, and subjective preferences.

Checkpoint: `evaluation`.

### 14. Export

Create an `ExportManifest` describing the actual outputs.

```yaml
export:
  master_video: null
  audio_ref: null
  duration: null
  resolution: null
  frame_rate: null
  aspect_ratio: null
  captions: []
  thumbnails: []
  alternate_versions: []
  source_project_ref: null
  approved_asset_ids: []
```

Verify files/objects exist before claiming export success.

### 15. Publish

Publishing is optional and should be explicit.

Before publishing, confirm:

- exact edition/version
- platform requirements
- title/description/credits
- rights and licensing status
- caption/subtitle requirements
- thumbnail and metadata
- destination/account authorization

Do not treat a rendered master as published content.

### 16. Archive

Archive enough evidence to reproduce, repair, or reinterpret the project:

- source inventory
- music analysis and section map
- visual direction
- SceneGraph
- ShotManifest
- prompt/manifests
- provider/local job records
- checkpoints and failures
- evaluations/approvals
- edit/export manifests
- final asset IDs/paths
- provenance and lineage links

Checkpoint: `export` or a durable completion checkpoint defined by the host system.

## CueMap

The `CueMap` is the bridge between musical time and visual time.

```yaml
cue_map:
  - cue_id: "cue-001"
    start: 0.0
    end: 8.0
    section_id: intro
    musical_function: establish
    lyric_function: none
    visual_function: establish-world
    motif_refs: []
    scene_refs: [scene-01]
    shot_refs: []
```

A cue may span multiple shots, and a shot may intentionally cross musical boundaries. The map expresses editorial intent rather than forcing a one-to-one relation.

## Provider-neutral execution

This skill may call whatever semantic capabilities are available, but it should not hard-code one provider as the workflow definition.

Examples:

```text
analyze_track
plan_scene
plan_shots
generate_image
edit_image
generate_video
extend_video
upscale
compose_timeline
evaluate_asset
export_video
```

A host system may route those operations to Suno-derived metadata, Ideogram, OpenAI, Runway, Veo, local ComfyUI, TouchDesigner, Blender, FFmpeg, an NLE, or other compatible systems. Provider capability and current availability are execution concerns.

## Relationship to other creative skills

### `songwriting-and-ai-music`

Use it upstream when the song, lyrics, musical identity, or generation prompt is still being authored. Once a track/version is approved, hand its identity artifacts into this skill instead of starting musical ideation over.

### `structured-asset-pipeline`

Use it as an execution/reproducibility helper when the workflow needs batches of keyframes, clips, audio derivatives, or regenerable units. `music-to-video` owns audiovisual reasoning and timing; `structured-asset-pipeline` owns generic unit-to-asset discipline.

### `comfyui`

Use it when local graph-based image/video generation is the chosen backend. The `ShotManifest` and approved keyframes should drive the backend rather than allowing node/workflow defaults to redefine the creative plan.

## Completion gate

Before saying the music video workflow is complete:

1. Invoke `verification-before-completion`.
2. Verify every promised artifact/output against the approved scope.
3. Confirm whether execution was real provider/local execution, dry-run, planning-only, or mixed.
4. Report incomplete shots, failed jobs, missing rights/license evidence, or unapproved outputs explicitly.
5. Preserve a checkpoint that another agent can resume without reconstructing the project from chat history.