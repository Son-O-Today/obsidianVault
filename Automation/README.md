# Automation Contract

This vault is designed for bidirectional server/local Git sync and LLM-maintained
knowledge compilation.

## Server Capture

Server-side agents should use:

```bash
python3 scripts/save_to_obsidian.py --title "..." --body "..." --source telegram
```

Flow:

```text
pull latest -> create note in 00-Inbox -> commit/push -> notify local pull
```

## Local Sync

Local Obsidian edits should use:

```bash
scripts/obsidian save
```

or:

```bash
scripts/옵시디언 저장
```

Flow:

```text
pull latest -> commit/push -> notify server pull
```

## Knowledge Compilation

Agents should treat the vault as layered memory:

- `00-Inbox/`: unprocessed capture
- `01-Raw/`: source of truth
- `03-Wiki/`: compiled knowledge
- `04-MOCs/`: navigation
- `05-Graphs/`: graph reports

Do not overwrite existing notes silently. Create unique filenames or merge
carefully with clear source attribution.
