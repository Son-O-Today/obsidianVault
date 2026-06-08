# Vault Agent Protocol

This file is the schema and operating contract for AI agents working in this
Obsidian vault.

## Folder Ownership

- `00-Inbox/`: agents may append new capture notes.
- `01-Raw/`: agents may add source files, but must not rewrite source content.
- `02-Notes/`: human-authored notes; agents may edit only when asked.
- `03-Wiki/`: LLM-maintained compiled knowledge. Agents may create and update.
- `04-MOCs/`: topic maps and indexes. Agents may update when wiki changes.
- `05-Graphs/`: reviewed graph reports and snapshots mirrored from `graphify-out/`.
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
4. Use Obsidian wikilink syntax for concepts, entities, projects, and sources.
5. Preserve citations or source references for factual claims.
6. Mark uncertainty and contradictions explicitly.
7. Append operational findings to relevant notes instead of burying them in chat.

## Sync Rules

Before writing generated notes, pull the latest Git state. After writing, commit
and push. If history diverges, stop and require manual conflict resolution.

## graphify

This project has a live knowledge graph at graphify-out/ with god nodes,
community structure, and cross-file relationships. `05-Graphs/` keeps reviewed
copies of graph reports and snapshots for human browsing.

When the user types `/graphify`, invoke the `skill` tool with `skill: "graphify"` before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- Keep `.graphifyignore` focused on compiled and operational knowledge: include `03-Wiki/`, `04-MOCs/`, `Automation/`, `Templates/`, `scripts/`, and root operating docs; exclude `00-Inbox/`, `01-Raw/`, `02-Notes/`, `.agents/`, `.codex/`, `graphify-out/`, `05-Graphs/`, and archives.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
