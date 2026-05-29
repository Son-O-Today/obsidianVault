#!/usr/bin/env python3
"""Optionally trigger a pull on a local Obsidian machine over SSH.

This is best-effort only. If the SSH target is not configured, the local
machine is offline, or the connection fails, the script prints a warning and
exits successfully so server-side note capture is never blocked.

Environment variables:
- OBSIDIAN_LOCAL_SSH_HOST: required to enable SSH triggering
- OBSIDIAN_LOCAL_SSH_USER: required to enable SSH triggering
- OBSIDIAN_LOCAL_SSH_PORT: optional, defaults to 22
- OBSIDIAN_LOCAL_VAULT_PATH: required to enable the remote pull command
- OBSIDIAN_LOCAL_SSH_KEY: optional SSH identity file path
"""
from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path


def main() -> int:
    host = os.environ.get('OBSIDIAN_LOCAL_SSH_HOST', '').strip()
    user = os.environ.get('OBSIDIAN_LOCAL_SSH_USER', '').strip()
    vault_path = os.environ.get('OBSIDIAN_LOCAL_VAULT_PATH', '').strip()
    port = os.environ.get('OBSIDIAN_LOCAL_SSH_PORT', '22').strip() or '22'
    identity = os.environ.get('OBSIDIAN_LOCAL_SSH_KEY', '').strip()

    if not host or not user or not vault_path:
        print('Local SSH pull not configured; skipping')
        return 0

    remote_cmd = (
        f"cd {shlex.quote(vault_path)} && "
        f"/usr/bin/python3 scripts/pull_vault_git.py"
    )
    ssh_cmd = [
        'ssh',
        '-p', port,
        '-o', 'BatchMode=yes',
        '-o', 'ConnectTimeout=8',
    ]
    if identity:
        ssh_cmd.extend(['-i', identity])
    ssh_cmd.extend([f'{user}@{host}', remote_cmd])

    proc = subprocess.run(ssh_cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        stderr = (proc.stderr or '').strip()
        stdout = (proc.stdout or '').strip()
        detail = stderr or stdout or f'exit code {proc.returncode}'
        print(f'Warning: local SSH pull trigger failed: {detail}')
        return 0

    out = (proc.stdout or '').strip()
    if out:
        print(out)
    err = (proc.stderr or '').strip()
    if err:
        print(err)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
