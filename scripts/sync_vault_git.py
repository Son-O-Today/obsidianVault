#!/usr/bin/env python3
"""Stage, commit, and push the Obsidian vault.

This script is intentionally conservative:
- exits quietly if there are no changes
- stages all vault changes
- creates one commit only when there is something to commit
- pushes the current branch to its tracked remote

Usage:
  python3 scripts/sync_vault_git.py
  python3 scripts/sync_vault_git.py --message "obsidian: sync"
  python3 scripts/sync_vault_git.py --dry-run
"""
from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=VAULT,
        text=True,
        capture_output=True,
        check=check,
    )


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run(['git', *args], check=check)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--message', default='')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    branch = git('branch', '--show-current').stdout.strip()
    if not branch:
        raise SystemExit('Could not determine current branch')

    status = git('status', '--porcelain').stdout.strip()
    if not status:
        print('No changes to sync')
        return 0

    if args.dry_run:
        print('--- git status --porcelain ---')
        print(status)
        print(f'Would stage, commit, and push on branch {branch}')
        return 0

    git('add', '-A')

    staged = git('diff', '--cached', '--name-only').stdout.strip()
    if not staged:
        print('No staged changes after add')
        return 0

    message = args.message.strip()
    if not message:
        now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        message = f'vault sync: {now}'

    commit = git('commit', '-m', message, check=False)
    if commit.returncode != 0:
        combined = (commit.stdout or '') + (commit.stderr or '')
        if 'nothing to commit' in combined.lower():
            print('Nothing to commit')
            return 0
        raise SystemExit(combined.strip() or 'git commit failed')

    push = git('push', 'origin', branch, check=False)
    if push.returncode != 0:
        combined = (push.stdout or '') + (push.stderr or '')
        raise SystemExit(combined.strip() or 'git push failed')

    if push.stdout:
        print(push.stdout.strip())
    if push.stderr:
        print(push.stderr.strip())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
