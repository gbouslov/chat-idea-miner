"""Find your AI chats and turn them into small, readable shards.

Mechanical only: find files, keep what you and the assistant actually said, drop tool noise,
and split into shards a subagent can read in one go. It makes no judgment about ideas.

Usage:
  python3 scripts/extract.py --out work                 # your real chats (default locations)
  python3 scripts/extract.py --examples --out work      # the invented demo chats
  python3 scripts/extract.py --add PATH --out work      # extra exports (ChatGPT/Claude conversations.json, Hermes .jsonl)
"""
import argparse, glob, json, os, re, sys
from datetime import datetime, timezone

HOME = os.path.expanduser('~')
NOISE = re.compile(r'^(<system-reminder>|<command-|<local-command|<environment_context>|# AGENTS\.md instructions|Caveat: The messages below|\[Request interrupted)', re.I)

def clean(text):
    if not isinstance(text, str): return ''
    text = re.sub(r'<system-reminder>.*?</system-reminder>', '', text, flags=re.S).strip()
    return '' if not text or NOISE.match(text) else text

def blocks_text(content):
    if isinstance(content, str): return clean(content)
    out = []
    for b in content or []:
        if isinstance(b, dict) and b.get('type') in ('text', 'input_text', 'output_text'):
            t = clean(b.get('text'))
            if t: out.append(t)
    return '\n'.join(out)

def day(t):
    if t is None: return ''
    if isinstance(t, (int, float)): return datetime.fromtimestamp(t, timezone.utc).strftime('%Y-%m-%d')
    return str(t)[:10]

def read_claude_code(path):
    turns, when = [], ''
    for line in open(path, errors='ignore'):
        try: x = json.loads(line)
        except Exception: continue
        if x.get('type') not in ('user', 'assistant') or x.get('isSidechain') or x.get('isMeta'): continue
        m = x.get('message') or {}
        t = blocks_text(m.get('content'))
        if t:
            when = when or day(x.get('timestamp'))
            turns.append((m.get('role') or x['type'], t))
    return when, turns

def read_codex(path):
    turns, when = [], ''
    for line in open(path, errors='ignore'):
        try: x = json.loads(line)
        except Exception: continue
        p = x.get('payload') or {}
        if x.get('type') == 'session_meta': when = day(p.get('timestamp') or x.get('timestamp'))
        if x.get('type') == 'response_item' and p.get('type') == 'message' and p.get('role') in ('user', 'assistant'):
            t = blocks_text(p.get('content'))
            if t: turns.append((p['role'], t))
    return when, turns

def read_generic_sessions(path):
    """Hermes `sessions export --format jsonl`, or any JSONL of {messages:[{role, content}]}."""
    out = []
    for line in open(path, errors='ignore'):
        try: s = json.loads(line)
        except Exception: continue
        msgs = s.get('messages') or []
        turns = [(m.get('role'), blocks_text(m.get('content'))) for m in msgs if m.get('role') in ('user', 'assistant')]
        turns = [(r, t) for r, t in turns if t]
        if turns: out.append((s.get('title') or s.get('id') or '', day(s.get('started_at') or s.get('created_at') or (msgs[0].get('timestamp') if msgs else None)), turns))
    return out

def read_conversations_json(path):
    """ChatGPT export (mapping tree) or Claude.ai export (chat_messages)."""
    data = json.load(open(path, errors='ignore'))
    out = []
    for c in data if isinstance(data, list) else []:
        turns = []
        if 'mapping' in c:
            nodes = sorted((n for n in c['mapping'].values() if n.get('message')), key=lambda n: n['message'].get('create_time') or 0)
            for n in nodes:
                m = n['message']; role = (m.get('author') or {}).get('role')
                parts = (m.get('content') or {}).get('parts') or []
                t = clean('\n'.join(p for p in parts if isinstance(p, str)))
                if role in ('user', 'assistant') and t: turns.append((role, t))
        elif 'chat_messages' in c:
            for m in c['chat_messages']:
                role = 'user' if m.get('sender') == 'human' else 'assistant'
                t = clean(m.get('text') or blocks_text(m.get('content')))
                if t: turns.append((role, t))
        if turns: out.append((c.get('title') or c.get('name') or '', day(c.get('create_time') or c.get('created_at')), turns))
    return out

def collect(roots, extra):
    chats = []
    cc = roots.get('claude')
    if cc:
        for f in glob.glob(os.path.join(cc, '*', '*.jsonl')):
            when, turns = read_claude_code(f)
            if turns: chats.append({'source': 'claude-code', 'file': f, 'project': os.path.basename(os.path.dirname(f)), 'date': when, 'turns': turns})
    cx = roots.get('codex')
    if cx:
        for f in glob.glob(os.path.join(cx, '**', '*.jsonl'), recursive=True):
            when, turns = read_codex(f)
            if turns: chats.append({'source': 'codex', 'file': f, 'project': '', 'date': when, 'turns': turns})
    for p in extra:
        files = glob.glob(os.path.join(p, '**', '*'), recursive=True) if os.path.isdir(p) else [p]
        for f in files:
            if f.endswith('conversations.json'):
                for title, when, turns in read_conversations_json(f):
                    chats.append({'source': 'chat-export', 'file': f, 'project': title, 'date': when, 'turns': turns})
            elif f.endswith('.jsonl'):
                for title, when, turns in read_generic_sessions(f):
                    chats.append({'source': 'hermes-or-jsonl', 'file': f, 'project': title, 'date': when, 'turns': turns})
    return chats

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='work')
    ap.add_argument('--examples', action='store_true')
    ap.add_argument('--add', action='append', default=[])
    ap.add_argument('--shard-chars', type=int, default=60000)
    ap.add_argument('--since', default='', help='only chats on or after YYYY-MM-DD')
    ap.add_argument('--keep-assistant', type=int, default=400, help='chars of each assistant reply to keep for context')
    a = ap.parse_args()
    here = os.path.join(os.path.dirname(__file__), '..', 'examples')
    if a.examples:
        roots = {'claude': os.path.join(here, 'claude-code', 'projects'), 'codex': os.path.join(here, 'codex', 'sessions')}
        extra = [os.path.join(here, 'chatgpt-export'), os.path.join(here, 'hermes-export')]
    else:
        roots = {'claude': os.path.join(HOME, '.claude', 'projects'), 'codex': os.path.join(HOME, '.codex', 'sessions')}
        extra = []
    extra += a.add
    chats = sorted((c for c in collect(roots, extra) if c['date'] >= a.since), key=lambda c: c['date'])
    os.makedirs(os.path.join(a.out, 'shards'), exist_ok=True)
    shards, cur, size = [], [], 0
    for i, c in enumerate(chats):
        c['id'] = f'c{i:04d}'
        body = '\n'.join(f"{'YOU' if r == 'user' else 'AI'}: {t if r == 'user' else t[:a.keep_assistant]}" for r, t in c['turns'])
        shown = os.path.normpath(c['file'])
        shown = os.path.relpath(shown, os.path.normpath(os.path.join(here, '..'))) if a.examples else shown.replace(HOME, '~', 1)
        c['file'] = shown
        block = f"### {c['id']} | {c['date']} | {c['source']} | {c['project']}\nfile: {shown}\n{body}\n"
        if cur and size + len(block) > a.shard_chars:
            shards.append(cur); cur, size = [], 0
        cur.append(block); size += len(block)
    if cur: shards.append(cur)
    for n, s in enumerate(shards):
        open(os.path.join(a.out, 'shards', f'shard-{n:02d}.md'), 'w').write('\n'.join(s))
    by = {}
    for c in chats: by[c['source']] = by.get(c['source'], 0) + 1
    manifest = {'chats': len(chats), 'by_source': by, 'shards': len(shards), 'first': chats[0]['date'] if chats else None, 'last': chats[-1]['date'] if chats else None}
    json.dump(manifest, open(os.path.join(a.out, 'manifest.json'), 'w'), indent=1)
    print(json.dumps(manifest))

if __name__ == '__main__':
    main()
