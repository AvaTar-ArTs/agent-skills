# Active-Skills Projection

The **active-skills** directory is a curated set of symlinks into the canonical library. It controls which skills are "active" for a given host.

## How it works

```
~/.agent-skills/active-skills/
├── writing-skills -> ../skills/writing-skills
├── code-review -> ../skills/code-review
├── xlsx -> ../skills/xlsx
└── ...  (308 symlinks, recounted 2026-10-27)
```

Each symlink points to a skill in the canonical `skills/` directory. Only skills with active-skills links are loaded by certain hosts.

## Why this exists

Not every skill should be active at once. The active-skills tree lets you:
- **Curate** which skills are available
- **Control context size** (fewer skills = less prompt overhead)
- **Override** skill locations (some links point to different paths)

## The projection problem

Your recent cleanup found that some active-skills links had **drifted**:

| Link | Was pointing to | Fixed to |
|------|----------------|----------|
| imagegen | `skills/.system/imagegen` | `../skills/imagegen` |
| openai-docs | `skills/.system/openai-docs` | `../skills/openai-docs` |
| plugin-creator | `skills/.system/plugin-creator` | `../skills/plugin-creator` |
| find-skills | `../skills/find-skills` (missing) | `.desktop-commander/skills/find-skills` |

These `.system/` paths were stale from an earlier projection. The fix was repointing, not deleting.

## The `.system/` directory

```
~/.agent-skills/skills/.system/
├── skill-creator/    ← internal system skill
└── skill-installer/  ← internal system skill
```

These are infrastructure skills used by the active-skills mechanism itself.

## Try it yourself

```bash
# Count active skills
ls ~/.agent-skills/active-skills/ | wc -l

# Show all link targets
ls -la ~/.agent-skills/active-skills/ | head -20

# Find any non-symlink entries
find ~/.agent-skills/active-skills -maxdepth 1 ! -type l -not -name ".*" | head -10

# Verify all links resolve
for l in ~/.agent-skills/active-skills/*; do
  test -e "$l" || echo "BROKEN: $l"
done
```

## Next

→ [07: Creating Skills](07-creating-skills.md)
