# Vault Agent Protocol

This file is the schema and operating contract for AI agents working in this
Obsidian vault.

## Folder Ownership

- `00-Inbox/`: agents may append new capture notes.
- `01-Raw/`: agents may add source files, but must not rewrite source content.
- `02-Notes/`: human-authored notes; agents may edit only when asked.
- `03-Wiki/`: LLM-maintained compiled knowledge. Agents may create and update.
- `04-MOCs/`: topic maps and indexes. Agents may update when wiki changes.
- `05-Graphs/`: graph outputs, reports, and snapshots.
- `Automation/`: operating rules. Edit carefully and keep backward compatible.
- `90-Archive/`: inactive material. Do not restore or delete without request.

## Frontmatter

Machine-written Markdown should include:

```yaml
---
title:
created:
source:
kind: capture
status: inbox
tags: [inbox]
id:
url:
---
```

Allowed `kind` values:

- `capture`
- `raw`
- `source`
- `note`
- `wiki`
- `moc`
- `report`
- `automation`

Allowed `status` values:

- `inbox`
- `reviewed`
- `compiled`
- `stale`
- `contradicted`
- `archived`

## LLM Wiki Rules

1. Treat `01-Raw/` as source of truth.
2. Compile durable knowledge into `03-Wiki/`.
3. Update `04-MOCs/` when adding important wiki pages.
4. Use `[[wikilinks]]` for concepts, entities, projects, and sources.
5. Preserve citations or source references for factual claims.
6. Mark uncertainty and contradictions explicitly.
7. Append operational findings to relevant notes instead of burying them in chat.

## Sync Rules

Before writing generated notes, pull the latest Git state. After writing, commit
and push. If history diverges, stop and require manual conflict resolution.
