# Troubleshooting

Common issues and fixes from real cleanup sessions.

## Broken symlinks

**Symptom:** Skill exists but doesn't load
**Cause:** Active-skills link points to wrong path
**Fix:**
```bash
# Find broken links
find ~/.agent-skills/active-skills -type l ! -exec test -e {} \; -print

# Check where it points
ls -la ~/.agent-skills/active-skills/broken-skill

# Repoint to correct location
ln -sfn ../skills/correct-skill ~/.agent-skills/active-skills/broken-skill
```

## Duplicate skills

**Symptom:** Same skill loads twice, wasting context tokens
**Cause:** Exact content copies at different paths
**Fix:**
```bash
# Run the canonical audit
cd ~/.agent-skills
bash ~/scripts/run-agent-skills-smoke.sh audit

# Check audit.json for exact_duplicates
cat tmp/smoke/*/audit.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for h, paths in d['skills']['exact_duplicates'].items():
    print(f'DUPLICATE: {paths}')
"
```

## Missing frontmatter

**Symptom:** Agent exists but never activates
**Cause:** No YAML frontmatter block
**Fix:**
```bash
# Find files without frontmatter
for f in ~/.agent-skills/agents/*.md; do
  head -1 "$f" | grep -q "^---" || echo "MISSING: $f"
done

# Add minimal frontmatter
sed -i '' '1i\
---\
name: agent-name\
description: Agent description\
---\
' ~/.agent-skills/agents/broken-agent.md
```

## Host drift (Cursor)

**Symptom:** Cursor has different skill content than canonical
**Cause:** Cursor copies skills instead of linking
**Fix:** Periodically sync from canonical, or accept that Cursor may lag.

## Context bloat

**Symptom:** AI responses slow down, `context` shows 70%+ usage
**Cause:** Too many skills loaded
**Fix:**
```bash
# Count active skills
ls ~/.agent-skills/active-skills/ | wc -l

# Prune inactive/unused skills from active-skills
# (only keep skills you actually use)
```

## Running the full audit

```bash
cd ~/.agent-skills
bash ~/scripts/run-agent-skills-smoke.sh audit
# Expected: 0 failed, broken_links=0
```

## Next

→ [11: Reference Architecture](11-reference-architecture.md)
