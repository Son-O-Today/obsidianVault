#!/usr/bin/env python3
"""Append a captured note into the Obsidian vault inbox."""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_VAULT = '/root/Documents/obsidianVault'
VAULT = Path(os.environ.get('OBSIDIAN_VAULT_PATH', DEFAULT_VAULT))
INBOX = VAULT / '00-Inbox'
MAX_TITLE_LEN = 80


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9\uac00-\ud7a3]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'note'


def truncate_title(text: str) -> str:
    text = ' '.join(text.split())
    return text[:MAX_TITLE_LEN].rstrip()


def stable_id(source: str, title: str, body: str) -> str:
    payload = f'{source}\n{title}\n{body}'.encode('utf-8')
    return hashlib.sha1(payload).hexdigest()[:12]


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    for i in range(2, 1000):
        candidate = parent / f'{stem} ({i}){suffix}'
        if not candidate.exists():
            return candidate
    raise SystemExit(f'could not find unique filename for {path}')


def run_vault_script(script_name: str, failure_message: str) -> None:
    script = VAULT / 'scripts' / script_name
    proc = subprocess.run(
        ['/usr/bin/python3', str(script)],
        cwd=VAULT,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        combined = (proc.stdout or '') + (proc.stderr or '')
        raise SystemExit(combined.strip() or failure_message)
    if proc.stdout:
        print(proc.stdout.strip())
    if proc.stderr:
        print(proc.stderr.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--body', required=True)
    parser.add_argument('--source', default='manual')
    parser.add_argument('--kind', default='capture')
    parser.add_argument('--tags', default='inbox')
    args = parser.parse_args()

    run_vault_script('pull_vault_git.py', 'vault pull failed')

    INBOX.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    stamp = now.strftime('%Y-%m-%d %H%M')
    title = truncate_title(args.title)
    file_title = slugify(title)
    filename = f'{stamp} - {file_title}.md'
    path = unique_path(INBOX / filename)
    note_id = stable_id(args.source, title, args.body)
    tags = ', '.join(t.strip() for t in args.tags.split(',') if t.strip()) or 'inbox'

    content = (
        '---\n'
        f'title: {title}\n'
        f'id: {note_id}\n'
        f'created: {now.isoformat().replace("+00:00", "Z")}\n'
        f'source: {args.source}\n'
        f'kind: {args.kind}\n'
        'status: inbox\n'
        f'tags: [{tags}]\n'
        '---\n\n'
        f'# {title}\n\n'
        '## Raw\n\n'
        f'{args.body}\n'
    )

    path.write_text(content, encoding='utf-8')
    print(path)

    run_vault_script('sync_vault_git.py', 'vault sync failed')
    run_vault_script('notify_local_pull.py', 'local pull notify failed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
