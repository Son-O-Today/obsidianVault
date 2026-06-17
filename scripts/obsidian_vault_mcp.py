#!/usr/bin/env python3
"""Small MCP server for this Obsidian vault.

The server intentionally exposes vault-shaped actions instead of broad file
system access. It uses the MCP stdio transport with newline-delimited JSON-RPC.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List


DEFAULT_VAULT = Path(__file__).resolve().parents[1]
VAULT = Path(os.environ.get("OBSIDIAN_VAULT_PATH", DEFAULT_VAULT)).expanduser().resolve()

READ_EXCLUDES = {
    ".git",
    ".obsidian",
    ".codex",
    ".DS_Store",
    "graphify-out",
    "90-Archive",
}
WRITE_FOLDERS = {
    "00-Inbox",
    "03-Wiki",
    "04-MOCs",
}
MAX_READ_CHARS = 60000


def respond(message_id: Any, result: Dict[str, Any]) -> None:
    sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": message_id, "result": result}, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def error(message_id: Any, code: int, message: str) -> None:
    sys.stdout.write(
        json.dumps(
            {"jsonrpc": "2.0", "id": message_id, "error": {"code": code, "message": message}},
            ensure_ascii=False,
        )
        + "\n"
    )
    sys.stdout.flush()


def text_result(text: str) -> Dict[str, Any]:
    return {"content": [{"type": "text", "text": text}], "isError": False}


def tool_error(text: str) -> Dict[str, Any]:
    return {"content": [{"type": "text", "text": text}], "isError": True}


def safe_rel_path(path_text: str) -> Path:
    rel = Path(path_text)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("path must be relative to the vault and may not contain '..'")
    path = (VAULT / rel).resolve()
    if not path.is_relative_to(VAULT):
        raise ValueError("path escapes the vault")
    if any(part in READ_EXCLUDES for part in rel.parts):
        raise ValueError(f"path is excluded: {path_text}")
    return path


def iter_markdown_files(folders: Iterable[str] | None = None) -> Iterable[Path]:
    roots = [VAULT / folder for folder in folders or [] if folder]
    if not roots:
        roots = [VAULT]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            rel = path.relative_to(VAULT)
            if any(part in READ_EXCLUDES for part in rel.parts):
                continue
            yield path


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\uac00-\ud7a3]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "note"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(2, 1000):
        candidate = path.with_name(f"{path.stem} ({index}){path.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"could not find unique filename for {path}")


def note_id(source: str, title: str, body: str) -> str:
    payload = f"{source}\n{title}\n{body}".encode("utf-8")
    return hashlib.sha1(payload).hexdigest()[:12]


def frontmatter(title: str, source: str, kind: str, status: str, tags: List[str], body: str) -> str:
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return (
        "---\n"
        f"title: {title}\n"
        f"id: {note_id(source, title, body)}\n"
        f"created: {now}\n"
        f"source: {source}\n"
        f"kind: {kind}\n"
        f"status: {status}\n"
        f"tags: [{', '.join(tags)}]\n"
        "---\n\n"
    )


def call_search_notes(args: Dict[str, Any]) -> Dict[str, Any]:
    query = str(args.get("query", "")).strip()
    if not query:
        return tool_error("query is required")
    folders = args.get("folders")
    if isinstance(folders, str):
        folders = [folders]
    if folders is not None and not isinstance(folders, list):
        return tool_error("folders must be a list of folder names")
    limit = min(int(args.get("limit", 20)), 50)
    query_lower = query.lower()
    results = []
    for path in iter_markdown_files(folders):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        haystack = text.lower()
        if query_lower not in haystack:
            continue
        idx = haystack.find(query_lower)
        start = max(0, idx - 140)
        end = min(len(text), idx + len(query) + 220)
        snippet = " ".join(text[start:end].split())
        results.append(
            {
                "path": str(path.relative_to(VAULT)),
                "modified": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                "snippet": snippet,
            }
        )
        if len(results) >= limit:
            break
    return text_result(json.dumps({"query": query, "count": len(results), "results": results}, ensure_ascii=False, indent=2))


def call_read_note(args: Dict[str, Any]) -> Dict[str, Any]:
    path_text = str(args.get("path", "")).strip()
    if not path_text:
        return tool_error("path is required")
    try:
        path = safe_rel_path(path_text)
    except ValueError as exc:
        return tool_error(str(exc))
    if not path.exists() or not path.is_file():
        return tool_error(f"note not found: {path_text}")
    if path.suffix.lower() != ".md":
        return tool_error("read_note only reads Markdown files")
    text = path.read_text(encoding="utf-8", errors="replace")
    truncated = len(text) > MAX_READ_CHARS
    if truncated:
        text = text[:MAX_READ_CHARS] + "\n\n[truncated]"
    return text_result(json.dumps({"path": path_text, "truncated": truncated, "content": text}, ensure_ascii=False, indent=2))


def call_list_recent_notes(args: Dict[str, Any]) -> Dict[str, Any]:
    folder = str(args.get("folder", "")).strip()
    folders = [folder] if folder else None
    limit = min(int(args.get("limit", 20)), 50)
    notes = []
    for path in iter_markdown_files(folders):
        try:
            stat = path.stat()
        except OSError:
            continue
        notes.append((stat.st_mtime, path))
    notes.sort(reverse=True)
    results = [
        {
            "path": str(path.relative_to(VAULT)),
            "modified": datetime.fromtimestamp(mtime, timezone.utc).isoformat(),
        }
        for mtime, path in notes[:limit]
    ]
    return text_result(json.dumps({"count": len(results), "results": results}, ensure_ascii=False, indent=2))


def call_create_inbox_note(args: Dict[str, Any]) -> Dict[str, Any]:
    title = str(args.get("title", "")).strip()
    body = str(args.get("body", "")).strip()
    source = str(args.get("source", "manual")).strip() or "manual"
    if not title or not body:
        return tool_error("title and body are required")
    folder = VAULT / "00-Inbox"
    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H%M")
    path = unique_path(folder / f"{stamp} - {slugify(title[:80])}.md")
    content = frontmatter(title[:80], source, "capture", "inbox", ["inbox"], body) + f"# {title[:80]}\n\n## Raw\n\n{body}\n"
    path.write_text(content, encoding="utf-8")
    return text_result(json.dumps({"created": str(path.relative_to(VAULT))}, ensure_ascii=False, indent=2))


def call_create_wiki_note(args: Dict[str, Any]) -> Dict[str, Any]:
    title = str(args.get("title", "")).strip()
    body = str(args.get("body", "")).strip()
    sources = args.get("sources", [])
    if isinstance(sources, str):
        sources = [sources]
    if not title or not body:
        return tool_error("title and body are required")
    folder = VAULT / "03-Wiki"
    folder.mkdir(parents=True, exist_ok=True)
    path = unique_path(folder / f"{slugify(title)}.md")
    source_text = "\n".join(f"- [[{source}]]" for source in sources if str(source).strip())
    sources_section = f"\n\n## Sources\n\n{source_text}\n" if source_text else ""
    content = frontmatter(title, "mcp", "wiki", "compiled", ["wiki"], body) + f"# {title}\n\n{body}{sources_section}"
    path.write_text(content, encoding="utf-8")
    return text_result(json.dumps({"created": str(path.relative_to(VAULT))}, ensure_ascii=False, indent=2))


def call_append_to_moc(args: Dict[str, Any]) -> Dict[str, Any]:
    path_text = str(args.get("path", "")).strip()
    text = str(args.get("text", "")).strip()
    if not path_text or not text:
        return tool_error("path and text are required")
    try:
        path = safe_rel_path(path_text)
    except ValueError as exc:
        return tool_error(str(exc))
    rel = path.relative_to(VAULT)
    if not rel.parts or rel.parts[0] != "04-MOCs":
        return tool_error("append_to_moc can only write under 04-MOCs")
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else f"# {path.stem}\n"
    separator = "" if existing.endswith("\n") else "\n"
    path.write_text(existing + separator + text + "\n", encoding="utf-8")
    return text_result(json.dumps({"updated": str(rel)}, ensure_ascii=False, indent=2))


def call_graphify_query(args: Dict[str, Any]) -> Dict[str, Any]:
    question = str(args.get("question", "")).strip()
    if not question:
        return tool_error("question is required")
    try:
        proc = subprocess.run(
            ["graphify", "query", question],
            cwd=str(VAULT),
            text=True,
            capture_output=True,
            timeout=45,
        )
    except FileNotFoundError:
        return tool_error("graphify command was not found")
    except subprocess.TimeoutExpired:
        return tool_error("graphify query timed out")
    output = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode != 0:
        return tool_error(output.strip() or "graphify query failed")
    return text_result(output.strip() or "graphify query returned no output")


TOOLS = {
    "search_notes": {
        "description": "Search Markdown notes in the Obsidian vault by literal text.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "folders": {"type": "array", "items": {"type": "string"}},
                "limit": {"type": "integer", "minimum": 1, "maximum": 50},
            },
            "required": ["query"],
        },
        "handler": call_search_notes,
    },
    "read_note": {
        "description": "Read a Markdown note by vault-relative path.",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
        "handler": call_read_note,
    },
    "list_recent_notes": {
        "description": "List recently modified Markdown notes, optionally under one folder.",
        "inputSchema": {
            "type": "object",
            "properties": {"folder": {"type": "string"}, "limit": {"type": "integer", "minimum": 1, "maximum": 50}},
        },
        "handler": call_list_recent_notes,
    },
    "create_inbox_note": {
        "description": "Create a capture note under 00-Inbox with vault frontmatter.",
        "inputSchema": {
            "type": "object",
            "properties": {"title": {"type": "string"}, "body": {"type": "string"}, "source": {"type": "string"}},
            "required": ["title", "body"],
        },
        "handler": call_create_inbox_note,
    },
    "create_wiki_note": {
        "description": "Create a compiled wiki note under 03-Wiki.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "body": {"type": "string"},
                "sources": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["title", "body"],
        },
        "handler": call_create_wiki_note,
    },
    "append_to_moc": {
        "description": "Append text to a Markdown MOC under 04-MOCs.",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string"}, "text": {"type": "string"}},
            "required": ["path", "text"],
        },
        "handler": call_append_to_moc,
    },
    "graphify_query": {
        "description": "Run graphify query against the vault knowledge graph.",
        "inputSchema": {
            "type": "object",
            "properties": {"question": {"type": "string"}},
            "required": ["question"],
        },
        "handler": call_graphify_query,
    },
}


def list_tools() -> List[Dict[str, Any]]:
    return [
        {
            "name": name,
            "description": meta["description"],
            "inputSchema": meta["inputSchema"],
        }
        for name, meta in TOOLS.items()
    ]


def handle_request(message: Dict[str, Any]) -> None:
    method = message.get("method")
    message_id = message.get("id")
    if message_id is None:
        return

    if method == "initialize":
        respond(
            message_id,
            {
                "protocolVersion": "2025-06-18",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "obsidian-vault", "version": "0.1.0"},
                "instructions": (
                    "Use this server for /Users/che60/auser/obsidianVault. "
                    "Respect AGENTS.md: treat 01-Raw as source material, write captures to 00-Inbox, "
                    "compiled knowledge to 03-Wiki, and MOCs to 04-MOCs. Do not delete files."
                ),
            },
        )
    elif method == "tools/list":
        respond(message_id, {"tools": list_tools()})
    elif method == "tools/call":
        params = message.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        tool = TOOLS.get(name)
        if tool is None:
            respond(message_id, tool_error(f"unknown tool: {name}"))
            return
        try:
            respond(message_id, tool["handler"](args))
        except Exception as exc:
            respond(message_id, tool_error(f"{type(exc).__name__}: {exc}"))
    elif method == "ping":
        respond(message_id, {})
    else:
        error(message_id, -32601, f"method not found: {method}")


def main() -> int:
    if not VAULT.exists():
        print(f"vault path does not exist: {VAULT}", file=sys.stderr)
        return 1
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError as exc:
            print(f"invalid json from client: {exc}", file=sys.stderr)
            continue
        handle_request(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
