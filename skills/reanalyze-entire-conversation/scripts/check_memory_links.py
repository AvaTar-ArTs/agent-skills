#!/usr/bin/env python3
"""check_memory_links.py - read-only integrity check of a markdown memory directory (MEMORY.md index + notes).
Reports: index links that do not resolve, notes missing from the index, and [[wiki-links]] whose target note does not exist.
Writes nothing. Usage: python3 -I check_memory_links.py <memory_dir> [--glob 'pattern*.md' ...]  (default: all notes)"""
import glob, os, re, sys

d = os.path.expanduser(sys.argv[1]).rstrip('/') + '/'
globs = [a for a in sys.argv[2:] if a != '--glob'] or ['*.md']
index = open(d + 'MEMORY.md', encoding='utf-8').read()
links = re.findall(r'\]\(([^)]+\.md)\)', index)
broken = [l for l in links if not os.path.exists(d + l)]
notes = {os.path.basename(p) for p in glob.glob(d + '*.md')} - {'MEMORY.md'}
unindexed = sorted(notes - set(links))
names = {n[:-3] for n in notes}
dead, total = set(), 0
for g in globs:
    for p in glob.glob(d + g):
        if os.path.basename(p) == 'MEMORY.md': continue
        body = re.sub(r'`[^`\n]*`', '', open(p, encoding='utf-8').read())   # ignore inline code: notes may DESCRIBE the [[link]] syntax
        for w in re.findall(r'\[\[([^\]]+)\]\]', body):
            total += 1
            if w not in names: dead.add(w)
print(f'index links: {len(links)} | broken: {len(broken)} {broken[:5]}')
print(f'note files: {len(notes)} | not in index: {len(unindexed)} {unindexed[:6]}')
print(f'wiki-links checked: {total} | dead targets: {len(dead)} {sorted(dead)[:8]}')
