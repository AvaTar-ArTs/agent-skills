#!/usr/bin/env python3
"""Validate a SKILL.md against all hermes-agent conventions.

Usage: python validate-skill.py skills/<category>/<name>/SKILL.md
"""

import sys, yaml, re, pathlib

def validate(path):
    content = pathlib.Path(path).read_text()
    errors = []

    # 1. Starts with ---
    if not content.startswith("---"):
        errors.append("SKILL.md must start with '---' (no leading blank line or BOM)")

    # 2. Has closing ---
    m = re.search(r'\n---\s*\n', content[3:])
    if not m:
        errors.append("No closing '---' found after frontmatter")
        if errors:
            return errors
        return errors

    fm_end = m.start() + 3
    try:
        fm = yaml.safe_load(content[3:fm_end])
    except yaml.YAMLError as e:
        errors.append(f"YAML parse error: {e}")
        return errors

    if not isinstance(fm, dict):
        errors.append("Frontmatter must be a YAML mapping")
        return errors

    # 3. Required fields
    for field in ["name", "description"]:
        if field not in fm:
            errors.append(f"Missing required field: '{field}'")

    # 4. Name constraints
    if "name" in fm:
        name = fm["name"]
        if len(name) > 64:
            errors.append(f"Name '{name}' exceeds 64 chars (is {len(name)})")
        if name != name.lower():
            errors.append(f"Name '{name}' must be lowercase")
        if " " in name:
            errors.append(f"Name '{name}' must use hyphens, not spaces")

    # 5. Description constraints
    if "description" in fm:
        desc = fm["description"]
        if len(desc) > 1024:
            errors.append(f"Description exceeds 1024 chars (is {len(desc)})")
        if not desc.startswith("Use when"):
            errors.append("Description should start with 'Use when ...'")

    # 6. Peer-matched fields (not enforced but every peer has them)
    for field in ["version", "author", "license", "platforms"]:
        if field not in fm:
            errors.append(f"Missing peer-matched field: '{field}' — not enforced but every peer has it")

    # 7. Metadata block
    if "metadata" not in fm:
        errors.append("Missing 'metadata' block — not enforced but every peer has it")
    elif "hermes" not in fm.get("metadata", {}):
        errors.append("Missing 'metadata.hermes' block — needed for tags and related_skills")
    else:
        meta = fm["metadata"]["hermes"]
        if "tags" not in meta:
            errors.append("Missing 'metadata.hermes.tags'")
        if "related_skills" not in meta:
            errors.append("Missing 'metadata.hermes.related_skills'")

    # 8. Body after frontmatter
    body = content[m.end()+3:]
    if len(body.strip()) == 0:
        errors.append("No body content after frontmatter")

    # 9. File size
    if len(content) > 100_000:
        errors.append(f"File exceeds 100,000 chars (is {len(content)})")

    # 10. Structure sections
    for section in ["## Overview", "## When to Use", "## Common Pitfalls", "## Verification Checklist"]:
        if section not in body:
            errors.append(f"Missing section: '{section}'")

    # 11. related_skills cross-references
    if "metadata" in fm and "hermes" in fm.get("metadata", {}):
        for skill_name in fm["metadata"]["hermes"].get("related_skills", []):
            repo_skills_dir = pathlib.Path(path).parents[2]
            found = False
            for cat_dir in repo_skills_dir.iterdir():
                if cat_dir.is_dir() and (cat_dir / skill_name / "SKILL.md").exists():
                    found = True
                    break
            if not found:
                errors.append(f"related_skill '{skill_name}' not found in-repo — will break for other clones")

    print(f"=== Validation: {path} ===")
    print(f"  Size: {len(content)} chars")
    if "name" in fm:
        print(f"  Name: {fm['name']} ({len(fm['name'])} chars)")
    if "description" in fm:
        desc_ok = len(fm["description"]) <= 1024
        print(f"  Description: {len(fm['description'])} chars {'OK' if desc_ok else 'OVER LIMIT'}")
    if "platforms" in fm:
        print(f"  Platforms: {fm['platforms']}")

    if errors:
        print(f"\n  {len(errors)} issue(s) found:")
        for e in errors:
            print(f"    X {e}")
        return 1
    else:
        print(f"\n  All checks passed")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} skills/<category>/<name>/SKILL.md")
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))
