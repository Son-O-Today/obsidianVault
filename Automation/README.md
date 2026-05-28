# Automation contract

This folder documents how future scripts or webhooks should write into the vault.

## Recommended flow
1. Write new items into `00-Inbox/` first.
2. Include YAML frontmatter with `source`, `created`, and `kind`.
3. Use a filename format like `YYYY-MM-DD HHmm - short-title.md` or a slug if the title is stable.
4. Link to related notes with `[[wikilinks]]` when known.
5. Move mature notes into `02-Notes/` or `03-References/`.

## Suggested metadata fields
- `title`
- `created`
- `source`
- `kind`
- `tags`
- `id` (optional stable identifier)
- `url` (if captured from the web)

## Safety rules
- Never overwrite a note silently if it already exists; append or create a new version.
- Keep raw captures separate from curated notes.
- Preserve original text when possible.
