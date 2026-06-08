# 05-Graphs

Reviewed graph outputs and reports.

Graphify writes its live query index to `graphify-out/` because the CLI defaults
to `graphify-out/graph.json`. After rebuilding the graph, mirror the human-facing
artifacts here:

- `GRAPH_REPORT.txt`
- `graph.json`
- `graph.html`
- `manifest.json`

Keep reports as `.txt` inside this folder so Obsidian's graph view does not turn
Graphify report links into large artificial hubs. `graphify-out/` keeps the live
`GRAPH_REPORT.md` required by Graphify, but Obsidian should ignore that
directory.

The graph corpus should stay focused on compiled and operational knowledge:
`03-Wiki/`, `04-MOCs/`, `Automation/`, `Templates/`, `scripts/`, and root
operating docs. Exclude inbox captures, raw sources, human working notes,
previous graph outputs, and agent skill implementation files.
