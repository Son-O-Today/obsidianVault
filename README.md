# Obsidian Vault

This vault is organized for both manual note-taking and future automation.

## Structure
- `00-Inbox/` — quick capture area for incoming notes and webhook drops
- `01-Daily/` — daily logs
- `02-Notes/` — evergreen notes and working notes
- `03-References/` — reference material and source notes
- `Attachments/` — images and files
- `Templates/` — reusable note templates
- `Automation/` — rules and contracts for incoming automated notes
- `90-Archive/` — inactive notes

## Automation convention
Use YAML frontmatter for all machine-written notes when possible:

```yaml
---
title: Example note
created: 2026-05-27T12:00:00Z
source: telegram
kind: capture
tags: [inbox]
---
```

Prefer one note per atomic idea or event. Keep filenames stable and human-readable.
