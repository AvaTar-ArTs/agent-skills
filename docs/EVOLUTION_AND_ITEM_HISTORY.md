# Evolution and Item History

## 2026-07-13 Session: Ecosystem Integration

### Memory Database Evolution
- Created shared.sqlite in ~/.agent-skills/memory/
- 21 decisions recorded across session
- Patterns tracked: agent-pack-organization, cross-tool-memory

### Poolside Integration Evolution  
- Added mcp.json with filesystem + memory servers
- Created symlinks for all 178 skills and 200+ agents
- Configured settings.yaml with memory_path

### NocturneMelodies Integration
- Added memory symlink
- Added skill symlinks (brainstorming, agent-creation-guidance)  
- Created music-agent-pipeline.sh

## 2026-09-05 Session: Research Skill Integration & Runtime Exclusions
- Preserved research capabilities (`skills/research/`) including arXiv, Blogwatcher, LLM Wiki, Polymarket, and Research Paper Writing templates.
- Updated `.gitignore` to exclude runtime state artifacts (`agent-skills-meta.csv.summary.json`, `agent-skills-meta.duplicates.csv`, deep tutor logs).
- Created `agents/documentation.md` to complete 103/103 100% root MD/TOML agent pair coverage.
- Committed and pushed to branch `repair/integrate-agent-skills` (PR #4).

## 2026-10-05 Session: Lineage, Restore, and Self-Evaluation
- Established `AvaTar-ArTs/agent-skills` as canonical; `AvaTar-ArTs/.Agent-skills` is a 1,049/1,050-file subset (blob-hash comparison).
- Restored 69 support files for 11 skills from `.Agent-skills@5dc4c75`; previously absent from both repositories.
- Recorded six self-evaluation items (S1–S6), including the new rule: deletion reviews must scan prose as well as code for references into the deleted tree.
- Checkpoint: [2026-10-05 Lineage and Restore](checkpoints/2026-10-05-agent-skills-lineage-and-restore.md).
