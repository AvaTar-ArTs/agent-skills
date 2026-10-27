#!/usr/bin/env python3
import argparse, hashlib, json, mimetypes, os, stat, sys
from datetime import datetime
from pathlib import Path

def hash_bytes(path, max_bytes):
    if max_bytes == 0:
        return None
    h = hashlib.sha1()
    read = 0
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            read += len(chunk)
            if max_bytes and read > max_bytes:
                return None
            h.update(chunk)
    return h.hexdigest()

def is_textish(path):
    m, _ = mimetypes.guess_type(path)
    if m is None:
        return False
    return m.startswith('text') or any(path.endswith(ext) for ext in ('.json','.jsonl','.md','.txt','.toml','.yaml','.yml','.ini','.cfg','.conf','.log'))

def preview(path, max_bytes):
    if max_bytes == 0:
        return None
    try:
        with open(path, 'rb') as f:
            data = f.read(max_bytes)
        return data.decode('utf-8', errors='ignore')
    except Exception:
        return None

def scan(root, args, next_id_start):
    entries = []
    root = Path(root)
    id_counter = next_id_start

    def record_path(p: Path, parent_id: int, typ: str):
        nonlocal id_counter
        try:
            st = p.lstat()
        except FileNotFoundError:
            return None
        entry_id = id_counter
        id_counter += 1
        rec = {
            'id': entry_id,
            'parent_id': parent_id,
            'path': str(p),
            'path_prefix': str(root),
            'name': p.name,
            'ext': p.suffix.lower() if typ == 'file' else '',
            'is_hidden': p.name.startswith('.'),
            'size_bytes': st.st_size,
            'mtime_iso': datetime.fromtimestamp(st.st_mtime).isoformat(),
            'type': typ,
            'hash_sha1': None,
            'preview': None,
        }
        if typ == 'file':
            rec['hash_sha1'] = hash_bytes(p, args.max_hash_bytes)
            if is_textish(str(p)):
                rec['preview'] = preview(p, args.max_preview_bytes)
        entries.append(rec)
        return entry_id

    # record root dir itself
    root_id = record_path(root, parent_id=0, typ='dir')

    for dirpath, dirnames, filenames in os.walk(root, followlinks=args.follow_symlinks):
        dirnames[:] = [d for d in dirnames if d not in args.exclude_dir_name]
        current_parent = None
        if dirpath:
            # parent id lookup is O(1) by scanning last recorded match
            # find matching path in entries (safe because we record dirs before children)
            for rec in reversed(entries):
                if rec['path'] == dirpath:
                    current_parent = rec['id']
                    break
        if current_parent is None:
            current_parent = root_id

        for d in dirnames:
            record_path(Path(dirpath) / d, parent_id=current_parent, typ='dir')
        for name in filenames:
            record_path(Path(dirpath) / name, parent_id=current_parent, typ='symlink' if os.path.islink(Path(dirpath)/name) else 'file')

    return entries, id_counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--roots', nargs='+', required=True)
    ap.add_argument('--out', default='inventory.json')
    ap.add_argument('--max-hash-bytes', type=int, default=2_000_000)
    ap.add_argument('--max-preview-bytes', type=int, default=4000)
    ap.add_argument('--follow-symlinks', action='store_true')
    ap.add_argument('--exclude-dir-name', nargs='*', default=['.git','node_modules','.cache','__pycache__'])
    args = ap.parse_args()

    all_entries = []
    next_id = 1
    for r in args.roots:
        if not Path(r).exists():
            print(f"warn: missing {r}", file=sys.stderr)
            continue
        recs, next_id = scan(r, args, next_id)
        all_entries.extend(recs)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump({
            'generated_at': datetime.now().isoformat(),
            'roots': args.roots,
            'max_hash_bytes': args.max_hash_bytes,
            'max_preview_bytes': args.max_preview_bytes,
            'entries': all_entries,
        }, f, indent=2)
    print(f"wrote {len(all_entries)} entries -> {out_path}")

if __name__ == '__main__':
    main()
