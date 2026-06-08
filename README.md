# Obsidian Vault

This vault uses a compiled-knowledge layout for personal notes, team knowledge,
and AI-agent operations.

## Structure

- `00-Inbox/` - quick capture and unprocessed automated notes
- `01-Raw/` - immutable source material: web clips, transcripts, PDFs, exports
- `02-Notes/` - human-authored working and evergreen notes
- `03-Wiki/` - LLM-maintained compiled wiki pages
- `04-MOCs/` - Maps of Content and topic entry points
- `05-Graphs/` - reviewed Graphify reports and graph snapshots
- `Automation/` - sync contracts, agent protocols, and operating rules
- `Templates/` - reusable Obsidian note templates
- `scripts/` - local/server sync and capture commands
- `90-Archive/` - inactive or superseded notes

## Sync Commands

Local Obsidian edits:

```bash
scripts/obsidian save
scripts/옵시디언 저장
```

Equivalent direct command:

```bash
python3 scripts/sync_local_to_server.py
```

Server-side capture:

```bash
python3 scripts/save_to_obsidian.py --title "Title" --body "Body" --source telegram
```

## Bidirectional Flow

Server captures:

```text
server pull latest -> write to 00-Inbox -> commit/push -> notify local pull
```

Local edits:

```text
local pull latest -> commit/push -> notify server pull
```

## Environment

Set `OBSIDIAN_VAULT_PATH` when the vault path is not the script default.

Local machine notifying the server:

- `OBSIDIAN_SERVER_SSH_HOST`
- `OBSIDIAN_SERVER_SSH_USER`
- `OBSIDIAN_SERVER_SSH_PORT` optional, defaults to `22`
- `OBSIDIAN_SERVER_VAULT_PATH`
- `OBSIDIAN_SERVER_SSH_KEY` optional

Server notifying the local machine:

- `OBSIDIAN_LOCAL_SSH_HOST`
- `OBSIDIAN_LOCAL_SSH_USER`
- `OBSIDIAN_LOCAL_SSH_PORT` optional, defaults to `22`
- `OBSIDIAN_LOCAL_VAULT_PATH`
- `OBSIDIAN_LOCAL_SSH_KEY` optional

## Knowledge Workflow

Use `00-Inbox` for unprocessed captures, promote durable sources into `01-Raw`,
compile durable knowledge into `03-Wiki`, and create topic navigation in
`04-MOCs`.

Graphify uses `graphify-out/` as its live query index. Reviewed graph artifacts
should be mirrored into `05-Graphs/` as snapshots. The default graph corpus should
focus on `03-Wiki`, `04-MOCs`, `Automation`, `Templates`, `scripts`, and root
operating docs; exclude inbox captures, raw sources, human working notes, agent
skill files, and previous graph outputs.

Raw sources should not be silently modified by agents. LLM-maintained wiki pages
must preserve source attribution and use wikilinks for cross-references.
