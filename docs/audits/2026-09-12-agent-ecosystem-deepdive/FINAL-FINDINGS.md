# Final findings — local AI-agent ecosystem

**Date:** 2026-09-12  
**Scope:** `~/iterm2`, `~/.agents`, `~/.agent-skills`, and `~/.hermes`  
**Mode:** Read-only audit; no secrets, tokens, session contents, database contents, or credential values were read or copied.

## Executive conclusion

This is not one repository with a few duplicate folders. It is a multi-surface ecosystem with three different kinds of state:

1. **Authored capability:** `~/.agent-skills` — the strongest current canonical candidate.
2. **Host projections:** `~/.agents/skills`, `~/.codex/skills`, and mixed Hermes skill links.
3. **Runtime/control state:** `~/.hermes` — a powerful execution environment, not a skill mirror.

The safest operating model is therefore **canonical source → verified host projections → separately governed runtimes**. Cleanup, merging, or broad synchronization before proving loader behavior would risk deleting newer host-specific behavior or exposing runtime state as portable capability.

## Findings, ranked

### P0 — Preserve boundaries; do not deduplicate yet

- `~/.agents/skills` currently resolves to `~/.agent-skills/skills` and should remain the compatibility projection.
- `~/.agents/skills.bak-2026-09-11-1402-copy` is migration evidence, not an active source.
- The backup comparison found 24 content differences and one backup-only skill, `video-marketing`.
- Raw duplicate counts from workspace scans are not cleanup instructions: generated files, empty files, vendor trees, caches, and runtime artifacts dominate the signal.
- Filename collisions are not identity. Path, content hash, provenance, and loader use must agree before any merge or removal.

### P1 — Canonical authority is probable, not proven

`~/.agent-skills/skills` is the strongest authority candidate because it is the current authored tree, has catalogs and audit documentation, and is the target of the live `~/.agents/skills` symlink. However, the repository is dirty, other host trees exist, and catalogs may be stale. The next proof is a read-only loader/projection probe, not a filesystem assumption.

### P1 — Hermes is a separate high-power control plane

Hermes contains skills, delegation, terminal and browser access, MCP integrations, sessions, caches, models, and persistent state. It should not be counted as another authored skill repository. Its configured delegation is bounded by depth and concurrency, but MCP inheritance and a high iteration budget still increase blast radius.

The most important operational risk is the enabled Suno surface: login, cookie save/load, authenticated-session restoration, browser capture, generation, and downloads. These need explicit approval gates and should not be inherited by child agents by default.

### P1 — Safety defaults need hardening before trust expansion

The audit identified these configured concerns:

- `tirith_fail_open: true`
- lazy installs enabled
- destructive slash confirmation disabled
- stop verification disabled
- child MCP inheritance enabled
- mutable `npx -y chrome-devtools-mcp@latest`

These are configuration risks, not proof of exploitation. They should be changed only after reviewing Hermes' exact schema and intended workflows, then verified with a safe probe.

### P2 — Repair the broken projection deliberately

`~/.hermes/skills/video-marketing` is a broken symlink. Its target is absent from the canonical tree, while a historical copy exists in the backup tree. Do not silently restore it: first decide whether the capability was intentionally retired, superseded by newer video skills, or still required. If retained, restore it through an approved canonical-source decision, not by pointing live Hermes at the backup.

### P2 — Establish capability parity as a maintained artifact

The new `skill-drift-ledger.json` records hashes and disposition for canonical-only, backup-only, identical, and divergent skills. It is a useful first parity ledger, but it does not yet prove runtime loading or behavioral parity. Add host projection paths, triggers, required tools/MCP, and a verification date as loader probes are completed.

## Specialist and agent perspectives reconciled

- **`filesystem-inventory` / `tree-explorer`:** established structural boundaries, size hotspots, symlink state, and the distinction between physical footprint and authored source.
- **`local-ecosystem-auditor`:** reinforced the safe classification of cleanup candidates, review-required material, do-not-remove runtime state, and security actions.
- **`ecosystem-analyzer` / topology review:** identified the invalid single-repository assumption and treated the backup as a divergent migration fork rather than a second authority.
- **Architecture review:** separated WorkVault/`iterm2` as a private control-plane workspace from product repositories, nested repositories, generated exports, and runtime history.
- **`capability-atlas`:** supplied the right unit of comparison: stable function, trigger, input/output contract, host rendering, parity test, and drift note—not merely same-name files.
- **`security-engineer` / independent security review:** rated Hermes as high-risk for untrusted prompts or content because browser, terminal, authenticated MCP, cookie, download, and delegation surfaces coexist.
- **`tool-evaluator`:** supports verifying actual need and runtime health before adding or leaving enabled MCP/tool surfaces; configured presence is not successful operation.
- **`workflow-orchestrator`:** supports the ordered, reversible path: inventory → topology/drift → capability parity → minimal automation → verification.
- **`ralph-self-audit`:** corrected the plan away from destructive cleanup and away from claiming absolute canonical authority from a single scan.
- **`verification-before-completion`:** requires loader behavior, symlink targets, manifest/frontmatter validity, command availability, and MCP health to be tested before claiming the ecosystem is fully understood or hardened.

These roles converge on the same result: **preserve provenance first; normalize only after authority and behavior are verified.**

## Evidence and limitations

Verified structural signals include:

- Canonical direct skills: 254; recursive `SKILL.md` files: 521.
- Historical backup direct skills: 227; intersection: 226; identical: 202; different: 24.
- Canonical agent definition files: 315.
- Hermes direct skills: 69; recursive contracts: 159; symlinks: 59; broken: 1.
- WorkVault scan: 48,894 files, with duplicate counts heavily affected by empty/generated/runtime noise.
- WorkVault boundary CSV: 12,043 path-preserving rows; reconstructed paths existed and were unique, while filename collisions were unsafe for identity.

Not established:

- absolute canonical authority across every host;
- actual loader behavior for every projection;
- MCP server health or credential validity;
- whether `video-marketing` was intentionally retired;
- whether every configured Hermes toolset is runtime-enabled;
- behavioral parity between same-name skills.

## Workspace duplicate-candidate refinement

The supplied Supremepowers/workspace classification is directionally correct and should be adopted as a triage policy, with one measurement caveat: the recommended absolute-path rescan covered only `iterm2/{agents,skills,commands}` plus `~/.agent-skills`; it did not cover the whole workspace or every named candidate directory.

The rescan produced 9,195 rows, 3,661 duplicate groups, and 8,020 duplicate rows. It found only 40 workspace agent files, 50 workspace skills, and 13 workspace commands because most capability records came from `~/.agent-skills`. Therefore, absence from this rescan is not evidence that a workspace candidate does not exist.

Targeted path-preserving checks confirmed:

- `rules.json`: two identical 560,333-byte files inside the same Agnix plugin release, likely a bundled knowledge/rules duplication; preserve until package layout and loader references are checked.
- `multi_modal_ai_merge_system.py`: two byte-identical 35,334-byte copies in `Ai-Merge-GitHub/` and `Ai-Merge-System/`, plus a distinct 35,372-byte `Ai-Merge/` variant; this is a provenance/branch-lineage question, not safe deduplication.
- `rest_request.py`: 30 identical copies under `Codex/.tmp/plugins/.../life-science-research`; this is strongly consistent with generated or vendored plugin packaging and belongs in the runtime/generated exclusion boundary unless provenance proves otherwise.

Adopt these operational classes:

- **Human review:** `Ai-Merge-*`, `rules/`, `agnix-rules/`, `knowledge-base/`, authored `agents/`, `scripts/`, `tools/`, `tests/`, and `mcp/`.
- **Preserve unless proven obsolete:** versioned docs, resources, knowledge bundles, third-party trees, package/vendor directories, and `META-INF/`.
- **Exclude from cleanup:** session history, archives, `.tmp`, generated/SSR output, terminal-update state, and IPC/runtime directories.

This supports the repository-boundary conclusion: `~/iterm2` is a private control-plane workspace containing portable capability renderings, independent repositories, generated/vendor material, and private runtime evidence—not one canonical source repository.

## Final decision

**No cleanup, merge, deletion, backup restoration, MCP installation, or security-setting change is justified solely by this audit.** The ecosystem is sufficiently mapped to proceed safely with a small verification phase:

1. probe host loaders and projection resolution;
2. review the 24 drift entries using the parity ledger;
3. decide the fate of `video-marketing`;
4. pin and health-check required MCPs;
5. harden Hermes defaults behind an explicit configuration change;
6. rerun verification and update the ledger.

## Durable references

- Audit overview: `README.md`
- Root inventory: `surface-inventory.json`
- Initial parity comparison: `skill-parity.json`
- Drift ledger: `skill-drift-ledger.json`
- Audit registry: `~/.agent-skills/docs/AUDITS-CATALOG.md`
