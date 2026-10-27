#!/usr/bin/env python3
"""extract_transcript.py - read-only extractor: Claude Code session .jsonl -> compact masked timeline + findings.
v2 of audit_extract.py (v1 kept untouched). Changes vs v1:
  * X21 fix: the secret mask no longer eats ordinary identifiers (v1 turned 'skip_host_skill_discovery' into <token>
    because 'sk' + 16 chars matched). v2 requires a delimiter or digit after the prefix (sk-, sk_, ghp_, AIza...).
  * masked-line counter: reports how many lines were masked so hidden evidence is noticed.
  * extra signals: classifier blocks, queue-operation corrections (mid-turn user messages), skill/agent/tool counts,
    token-shape hits counted (never printed).
Usage: python3 -I audit_extract_v2.py <session.jsonl> <out_dir>"""
import json, re, sys, os, collections

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
MASK = [(re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+'), '<email>'),
        (re.compile(r'(?<![A-Za-z0-9])(?:sk|pk|rk)[-_][A-Za-z0-9_\-]{16,}'), '<token>'),
        (re.compile(r'(?<![A-Za-z0-9])(?:ghp|gho|ghs|ghu|github_pat|xox[bpa]|AIza)[-_]?[A-Za-z0-9_\-]{16,}'), '<token>'),
        (re.compile(r'(?i)(bearer\s+)[A-Za-z0-9_\-\.=]{20,}'), r'\1<token>'),
        (re.compile(r'(?i)(token|secret|password|apikey|api_key)(["\']?\s*[:=]\s*["\']?)[^\s"\',}]{8,}'), r'\1\2<masked>')]
SHAPES = {'sk-/pk-': re.compile(r'(?<![A-Za-z0-9])(?:sk|pk)[-_][A-Za-z0-9_\-]{20,}'),
          'ghp_/gho_/github_pat': re.compile(r'(?<![A-Za-z0-9])(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}'),
          'AIza': re.compile(r'AIza[A-Za-z0-9_\-]{30,}'), 'Bearer-long': re.compile(r'(?i)bearer\s+[A-Za-z0-9_\-\.=]{30,}'),
          'jwt-like': re.compile(r'eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}')}
masked_lines = 0

def mask(t):
    global masked_lines
    o = t
    for rx, rep in MASK: t = rx.sub(rep, t)
    if t != o: masked_lines += 1
    return t

def clip(t, n):
    t = mask(' '.join(str(t).split()))
    return t if len(t) <= n else t[:n] + f' ...[{len(t)} chars]'

def blocks(msg):
    c = msg.get('content') if isinstance(msg, dict) else msg
    if isinstance(c, str): return [{'type': 'text', 'text': c}]
    return c or []

rows, stats, tools, shape_hits, errs = [], collections.Counter(), collections.Counter(), collections.Counter(), []
with open(SRC, encoding='utf-8', errors='replace') as f:
    for i, line in enumerate(f):
        for k, rx in SHAPES.items():
            n = len(rx.findall(line))
            if n: shape_hits[k] += n
        try: d = json.loads(line)
        except Exception: stats['bad_json'] += 1; continue
        ty = d.get('type'); ts = (d.get('timestamp') or '')[:19]; stats['lines'] += 1
        if ty == 'queue-operation' and d.get('operation') == 'enqueue':
            rows.append((i, ts, 'QUEUED_USER', clip(d.get('content', ''), 400), 0)); stats['queued_user'] += 1; continue
        if ty not in ('user', 'assistant'): stats['other_' + str(ty)] += 1; continue
        for b in blocks(d.get('message')):
            bt = b.get('type')
            if bt == 'text':
                t = b['text']; kind = 'USER' if ty == 'user' else 'ASSISTANT'
                if ty == 'user' and (t.lstrip().startswith(('<system-reminder>', '<local-command', '<task-notification', '<teammate', 'Base directory', 'Called the', 'The following', 'Note:', '[Image', 'Tool loaded'))
                                     or 'teammate-message' in t[:80]): kind = 'USER_SYS'
                rows.append((i, ts, kind, clip(t, 700 if kind != 'USER_SYS' else 160), len(t))); stats[kind] += 1
            elif bt == 'tool_use':
                n = b.get('name'); tools[n] += 1; inp = b.get('input', {})
                brief = inp.get('command') or inp.get('file_path') or inp.get('pattern') or inp.get('description') or inp.get('skill') or inp.get('prompt') or json.dumps(inp)[:200]
                rows.append((i, ts, 'TOOL:' + str(n), clip(brief, 260), 0)); stats['tool_use'] += 1
            elif bt == 'tool_result':
                c = b.get('content')
                if isinstance(c, list): c = ' '.join(x.get('text', '[image]') if isinstance(x, dict) else str(x) for x in c)
                c = str(c or ''); err = bool(b.get('is_error'))
                if 'auto mode classifier' in c: stats['classifier_blocks'] += 1
                rows.append((i, ts, 'RESULT' + ('_ERR' if err else ''), clip(c, 200), len(c))); stats['tool_result'] += 1
                if err: errs.append((ts, clip(c, 140)))
            elif bt == 'image': stats['images'] += 1
with open(os.path.join(OUT, 'timeline.tsv'), 'w', encoding='utf-8') as o:
    o.write('line\tts\tkind\ttext\tlen\n')
    for r in rows: o.write('\t'.join(str(x).replace('\t', ' ') for x in r) + '\n')
json.dump({'stats': dict(stats), 'tools': tools.most_common(), 'rows': len(rows), 'masked_lines': masked_lines,
           'token_shape_hits_in_raw_transcript(counts only)': dict(shape_hits), 'errors': errs}, open(os.path.join(OUT, 'stats.json'), 'w'), indent=1)
print(json.dumps({'stats': dict(stats), 'top_tools': tools.most_common(14), 'rows': len(rows), 'masked_lines': masked_lines,
                  'token_shape_hits(counts only)': dict(shape_hits), 'n_errors': len(errs)}, indent=1))
