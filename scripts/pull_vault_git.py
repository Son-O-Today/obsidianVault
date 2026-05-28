#!/usr/bin/env python3
"""Fetch and fast-forward the Obsidian vault from its tracked remote.

This script is intended for the local Obsidian machine or any clone that should
stay in sync with the server-side vault.

Behavior:
- exits quietly if there is nothing to update
- fetches the remote
- fast-forwards the current branch only
- refuses to merge automatically if history diverged

Usage:
  python3 scripts/pull_vault_git.py
  python3 scripts/pull_vault_git.py --dry-run
"""
from __future__ import annotations

import argparse
import subprocess
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
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    branch = git('branch', '--show-current').stdout.strip()
    if not branch:
        raise SystemExit('Could not determine current branch')

    git('fetch', 'origin')

    local = git('rev-parse', branch).stdout.strip()
    remote = git('rev-parse', f'origin/{branch}').stdout.strip()

    if local == remote:
        print('Already up to date')
        return 0

    if args.dry_run:
        print(f'Would fast-forward {branch} from {local[:7]} to {remote[:7]}')
        return 0

    merge_base = git('merge-base', branch, f'origin/{branch}').stdout.strip()
    if merge_base != local:
        raise SystemExit(
            'Local branch has diverged from origin; manual conflict resolution required'
        )

    pull = git('pull', '--ff-only', 'origin', branch, check=False)
    if pull.returncode != 0:
        combined = (pull.stdout or '') + (pull.stderr or '')
        raise SystemExit(combined.strip() or 'git pull failed')

    if pull.stdout:
        print(pull.stdout.strip())
    if pull.stderr:
        print(pull.stderr.strip())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
