# Graph Report - .  (2026-06-08)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 131 nodes · 151 edges · 18 communities (15 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6dbee21a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]

## God Nodes (most connected - your core abstractions)
1. `Graphify` - 18 edges
2. `LLM Wiki` - 12 edges
3. `지식 컴파일` - 11 edges
4. `AI 에이전트 지식 운영` - 10 edges
5. `Obsidian Vault` - 9 edges
6. `main()` - 6 edges
7. `Vault Agent Protocol` - 6 edges
8. `Automation Contract` - 5 edges
9. `{{title}}` - 5 edges
10. `git()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Agents Protocol` --conceptually_related_to--> `Obsidian Vault`  [EXTRACTED]
  AGENTS.md → README.md
- `Obsidian Vault` --conceptually_related_to--> `Applications: 개인과 팀의 지식 관리`  [EXTRACTED]
  README.md → 03-Wiki/Applications/개인과 팀의 지식 관리.md
- `Obsidian Vault` --conceptually_related_to--> `Graphify`  [EXTRACTED]
  README.md → 03-Wiki/Tools/Graphify.md
- `Obsidian 지식 인터페이스` --conceptually_related_to--> `Obsidian`  [EXTRACTED]
  03-Wiki/Tools/Obsidian_지식_인터페이스.md → Automation/README.md
- `Obsidian` --conceptually_related_to--> `LLM Wiki`  [EXTRACTED]
  Automation/README.md → 03-Wiki/Tools/Obsidian_지식_인터페이스.md

## Import Cycles
- None detected.

## Communities (18 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.10
Nodes (20): Agents Protocol, LLM Wiki, Obsidian, Obsidian 지식 인터페이스, 지식 컴파일, Applications: 개인과 팀의 지식 관리, Graphify, Bidirectional Flow (+12 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (17): AI 에이전트 지식 운영, 관련, 입력과 출력, 정의, 컴파일 원칙, 품질 기준, 지식 컴파일, 관련 (+9 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (16): 도구, 시작점, 열린 질문, 원본, 적용, AI 에이전트 지식 운영, Automation Contract, Knowledge Compilation (+8 more)

### Community 3 - "Community 3"
Cohesion: 0.25
Nodes (7): RAG와의 관계, 관련, 운영 루프, 정의, 출처, 핵심 계층, LLM Wiki

### Community 4 - "Community 4"
Cohesion: 0.43
Nodes (7): Path, main(), run_vault_script(), slugify(), stable_id(), truncate_title(), unique_path()

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (5): Folder Ownership, Frontmatter, LLM Wiki Rules, Sync Rules, Vault Agent Protocol

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (5): 개인 지식 관리, 공통 위험, 관련, 기대 결과, 팀 지식 관리

### Community 7 - "Community 7"
Cohesion: 0.67
Nodes (5): main(), print_output(), CompletedProcess, require_success(), run_script()

### Community 8 - "Community 8"
Cohesion: 0.33
Nodes (5): Key points, Related, Sources, Summary, {{title}}

### Community 9 - "Community 9"
Cohesion: 0.70
Nodes (4): git(), main(), CompletedProcess, run()

### Community 10 - "Community 10"
Cohesion: 0.70
Nodes (4): git(), main(), CompletedProcess, run()

### Community 11 - "Community 11"
Cohesion: 0.40
Nodes (4): Core pages, Open questions, Start here, {{title}}

### Community 12 - "Community 12"
Cohesion: 0.40
Nodes (4): Extracted claims, Notes, Source, {{title}}

## Knowledge Gaps
- **69 isolated node(s):** `install_local_pull_service.sh script`, `Path`, `개인 지식 관리`, `팀 지식 관리`, `기대 결과` (+64 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Graphify` connect `Community 0` to `Community 1`, `Community 2`, `Community 3`, `Community 5`?**
  _High betweenness centrality (0.266) - this node is a cross-community bridge._
- **Why does `LLM Wiki` connect `Community 3` to `Community 0`, `Community 1`, `Community 2`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **What connects `install_local_pull_service.sh script`, `Path`, `개인 지식 관리` to the rest of the system?**
  _69 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.09956709956709957 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.12280701754385964 - nodes in this community are weakly interconnected._