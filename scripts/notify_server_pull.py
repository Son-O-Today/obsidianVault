#!/usr/bin/env python3
"""Optionally trigger a pull on the server-side Obsidian vault over SSH."""
from __future__ import annotations

import os
import shlex
import subprocess


def main() -> int:
    host = os.environ.get('OBSIDIAN_SERVER_SSH_HOST', '').strip()
    user = os.environ.get('OBSIDIAN_SERVER_SSH_USER', '').strip()
    vault_path = os.environ.get('OBSIDIAN_SERVER_VAULT_PATH', '').strip()
    port = os.environ.get('OBSIDIAN_SERVER_SSH_PORT', '22').strip() or '22'
    identity = os.environ.get('OBSIDIAN_SERVER_SSH_KEY', '').strip()

    if not host or not user or not vault_path:
        print('Server SSH pull not configured; skipping')
        return 0

    remote_cmd = (
        f"cd {shlex.quote(vault_path)} && "
        f"/usr/bin/python3 scripts/pull_vault_git.py"
    )
    ssh_cmd = ['ssh', '-p', port, '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=8']
    if identity:
        ssh_cmd.extend(['-i', identity])
    ssh_cmd.extend([f'{user}@{host}', remote_cmd])

    proc = subprocess.run(ssh_cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        stderr = (proc.stderr or '').strip()
        stdout = (proc.stdout or '').strip()
        detail = stderr or stdout or f'exit code {proc.returncode}'
        print(f'Warning: server SSH pull trigger failed: {detail}')
        return 0

    if proc.stdout:
        print(proc.stdout.strip())
    if proc.stderr:
        print(proc.stderr.strip())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
