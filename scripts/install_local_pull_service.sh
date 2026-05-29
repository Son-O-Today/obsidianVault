#!/usr/bin/env bash
set -euo pipefail

VAULT_PATH="${1:-}"
if [[ -z "$VAULT_PATH" ]]; then
  echo "usage: sudo $0 /absolute/path/to/obsidianVault" >&2
  exit 1
fi

SERVICE_PATH="/etc/systemd/system/obsidian-vault-pull.service"

cat > "$SERVICE_PATH" <<EOF
[Unit]
Description=Pull Obsidian vault on boot
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=$VAULT_PATH
ExecStart=/usr/bin/python3 $VAULT_PATH/scripts/pull_vault_git.py

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now obsidian-vault-pull.service
systemctl status --no-pager --full obsidian-vault-pull.service | sed -n '1,20p'
