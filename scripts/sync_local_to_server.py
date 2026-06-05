#!/usr/bin/env python3
"""Sync the local Obsidian vault to origin, then notify the server to pull."""
from __future__ import annotations

import argparse
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(os.environ.get('OBSIDIAN_VAULT_PATH', Path(__file__).resolve().parents[1]))


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ['/usr/bin/python3', *args],
        cwd=VAULT,
        text=True,
        capture_output=True,
    )


def print_output(proc: subprocess.CompletedProcess[str]) -> None:
    if proc.stdout:
        print(proc.stdout.strip())
    if proc.stderr:
        print(proc.stderr.strip())


def require_success(proc: subprocess.CompletedProcess[str], message: str) -> None:
    if proc.returncode != 0:
        combined = (proc.stdout or '') + (proc.stderr or '')
        raise SystemExit(combined.strip() or message)
    print_output(proc)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--message', default='')
    args = parser.parse_args()

    pull = run_script('scripts/pull_vault_git.py')
    require_success(pull, 'local vault pull failed')

    message = args.message.strip()
    if not message:
        now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        message = f'local vault sync: {now}'

    sync = run_script('scripts/sync_vault_git.py', '--message', message)
    require_success(sync, 'local vault sync failed')

    notify = run_script('scripts/notify_server_pull.py')
    require_success(notify, 'server pull notify failed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
