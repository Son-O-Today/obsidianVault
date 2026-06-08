---
title: LLM Wiki와 Graphify 웹 조사
created: 2026-06-05T00:00:00Z
source: web-research
kind: raw
status: reviewed
tags: [source, llm-wiki, obsidian, graphify, ai-agent, knowledge-management]
source_id: web-research-2026-06-05-llm-wiki-graphify
---

# LLM Wiki와 Graphify 웹 조사

> 이 문서는 2026-06-05에 수집·정리한 조사 기록이다. 이후 컴파일된 지식은
> [[LLM Wiki]], [[Graphify]], [[Obsidian 지식 인터페이스]]에서 관리한다.

## 요약

Andrej Karpathy의 LLM Wiki 패턴은 RAG처럼 질문 시점마다 원문 조각을 다시 찾는 방식이 아니라, 원천 자료를 미리 읽고 구조화된 Markdown wiki로 컴파일해 두는 접근이다. Obsidian은 사람이 읽고 탐색하는 IDE가 되고, LLM은 wiki를 쓰고 유지보수하는 프로그래머가 된다.

Graphify는 이 wiki/문서/코드 저장소를 다시 knowledge graph로 바꾸는 계층이다. Obsidian의 wikilink 그래프는 사람이 보는 지식 연결망이고, Graphify의 `graph.json`, `GRAPH_REPORT.md`, query/path/explain 명령은 AI 에이전트가 쓰는 구조화된 탐색 계층에 가깝다.

현재 vault에는 `00-Inbox`, `02-Notes`, `Automation`, `Templates`, `scripts` 구조가 있으므로, `raw -> wiki -> graph -> agent context` 흐름을 얹기 좋다.

## Karpathy의 LLM Wiki 이론

핵심 전환은 "검색"에서 "컴파일"로 옮기는 것이다.

- Raw sources: 기사, 논문, 이미지, 데이터, 회의록, Slack/Telegram 로그 같은 원천 자료. 원칙적으로 immutable이어야 한다.
- Wiki: LLM이 생성하고 유지하는 Markdown 계층. 요약, entity page, concept page, comparison, overview, synthesis가 들어간다.
- Schema: `AGENTS.md`, `CLAUDE.md`, workflow 문서처럼 LLM에게 vault 구조, 파일명 규칙, frontmatter, 링크 규칙, ingest/query/lint 절차를 알려주는 운영 규약이다.

운영 단위는 세 가지다.

- Ingest: 새 원천 자료를 넣고 관련 summary/entity/concept/index/log를 갱신한다.
- Query: wiki를 먼저 읽고 답변하며, 가치 있는 답변은 다시 wiki page로 저장한다.
- Lint: 고아 노트, 깨진 링크, 모순, 오래된 주장, 빠진 cross-reference, 추가 웹서치가 필요한 빈틈을 정기 점검한다.

중요한 점은 LLM이 모든 노트를 임의로 새로 쓰는 것이 아니라, 기존 wiki에 병합하고 모순을 표시하며 index/log를 갱신해야 한다는 것이다.

## Obsidian의 역할

Obsidian은 이 시스템에서 저장소이자 시각화 계층이다.

- Markdown 파일과 Git을 그대로 쓴다.
- Wikilink가 지식 그래프의 기본 edge가 된다.
- Graph View는 hub, orphan, topic cluster를 사람이 빠르게 보는 도구다.
- Dataview를 붙이면 frontmatter 기반 대시보드가 가능하다.
- Web Clipper를 붙이면 웹 자료를 raw source로 빨리 수집할 수 있다.

추천 폴더 구조:

```text
00-Inbox/        # 자동 캡처, 아직 정리되지 않은 입력
01-Raw/          # 웹클립, PDF 추출, 회의록, Telegram 원문
02-Notes/        # 사람이 직접 쓰는 working/evergreen note
03-Wiki/         # LLM이 유지하는 compiled wiki
04-MOCs/         # Map of Contents, 주제별 진입점
05-Graphs/       # Graphify 출력, graph report, snapshots
Automation/      # 운영 규약, 에이전트 계약
Templates/
scripts/
90-Archive/
```

현재 vault에서는 `01-Raw`, `03-Wiki`, `04-MOCs`, `05-Graphs`를 추가하면 충분하다.

## Graphify의 역할

Graphify는 코드, 문서, 논문, 다이어그램 등을 노드와 엣지로 추출해 queryable knowledge graph를 만든다. Tree-sitter 기반 정적 분석과 LLM 기반 의미 추출을 결합하고, NetworkX 그래프와 Leiden community detection을 사용한다.

Obsidian과 결합할 때의 역할 분담:

- Obsidian: 사람이 읽는 wiki, 수동 편집, graph view.
- LLM Wiki: raw source를 Markdown wiki로 컴파일하고 갱신.
- Graphify: vault/wiki/code/scripts를 graph로 분석해서 hub, surprising connection, path, query 결과를 에이전트에 제공.

실전에서는 Graphify를 전체 vault에 바로 돌리기보다, 먼저 `03-Wiki`, `Automation`, `scripts` 같은 품질이 높은 영역에 돌리는 편이 좋다. `00-Inbox`는 잡음이 많으므로 제외하거나 별도 그래프로 분리한다.

## 관련 GitHub 레포

### Ar9av/obsidian-wiki

AI agent가 Obsidian wiki를 만들고 유지하도록 skill 파일을 설치하는 프레임워크다. Claude Code, Codex, Cursor, Gemini 등 여러 agent에 wiki skill을 설치하는 방식이고, manifest로 ingest delta를 추적한다.

적용 포인트:

- 현재 vault의 `Automation/`에 agent workflow를 명시하는 방식과 잘 맞는다.
- 여러 agent가 같은 vault를 읽고 쓰는 환경에서 skill 기반 프로토콜을 줄 수 있다.

### green-dalii/obsidian-llm-wiki

Obsidian Community Plugin 형태의 Karpathy LLM Wiki 구현체다. 단일 파일/폴더 ingest, wiki query, lint, index regenerate, schema suggestion을 Obsidian 안에서 실행한다.

적용 포인트:

- 터미널 대신 Obsidian UI 안에서 wiki 생성/질의를 하고 싶을 때 적합하다.
- provider 설정이 필요하며, local Ollama도 옵션으로 지원한다.

### atomicstrata/llm-wiki-compiler

CLI 기반의 LLM Wiki compiler다. raw source를 typed pages로 컴파일하고, citation, hybrid retrieval, graph expansion, local viewer, MCP server, export를 제공한다.

적용 포인트:

- 현재처럼 Git 동기화와 script 기반 운영을 하는 vault에는 CLI 방식이 잘 맞는다.
- `llmwiki query --save`, `llmwiki lint`, `llmwiki serve` 같은 명령을 agent workflow에 넣기 쉽다.

### safishamsi/graphify

AI coding assistant용 knowledge graph skill이다. 프로젝트 폴더를 graph로 만들고, assistant가 `graphify query`, `graphify path`, `graphify explain`을 우선 사용하도록 설정할 수 있다.

적용 포인트:

- vault 자체보다 `scripts`, `Automation`, `03-Wiki`를 분석해 agent 운영 지식을 구조화하는 데 강하다.
- 코드, 문서, SQL schema, PDF, 이미지 등 다양한 입력을 하나의 graph로 묶을 수 있다.

## 운영 활용 사례

### 개인 지식 관리

입력:

- Telegram/웹클립/독서노트/논문/PDF/회의 메모

처리:

- `00-Inbox`에 저장
- 사람이 중요도를 판단해 `01-Raw`로 승격
- LLM이 `03-Wiki/entities`, `03-Wiki/concepts`, `03-Wiki/sources`, `04-MOCs`를 갱신
- Graphify가 주기적으로 hub/orphan/surprise connection을 보고

출력:

- 주제별 MOC
- 프로젝트별 briefing
- 주간 리뷰
- "내가 X에 대해 알고 있는 것" 질의 응답

### 팀 지식 관리

입력:

- Slack thread, meeting transcript, PR discussion, design doc, customer call

처리:

- raw source는 immutable로 보관
- LLM이 결정사항, open question, 책임자, 관련 시스템을 wiki page로 갱신
- human review를 거쳐 active 상태로 승격

출력:

- 신규 팀원 onboarding map
- 시스템별 architecture MOC
- 반복 질문 FAQ
- 결정 이력과 모순 탐지

### AI 에이전트 운영

입력:

- agent session logs
- Codex/Claude 작업 기록
- 실패한 명령과 해결책
- repo별 운영 runbook

처리:

- `Automation/Agent Protocol.md`에 agent 행동 규약 작성
- `03-Wiki/agents`에 문제-해결 패턴 축적
- Graphify로 scripts와 runbook의 dependency/path 분석

출력:

- 새 agent 세션 시작 시 읽을 compact context pack
- "이 repo에서 sync가 실패하면 무엇을 확인해야 하나" 같은 운영 질의
- 실패 사례 Error Book
- agent별 기억 편향/반복 실수 lint

## 현재 vault에 적용하는 제안

1. 폴더 추가

```text
01-Raw/
03-Wiki/
04-MOCs/
05-Graphs/
```

2. source frontmatter 표준화

```yaml
---
title:
created:
source:
kind: raw | capture | source | wiki | moc | report
status: inbox | reviewed | compiled | stale | contradicted | archived
tags: []
url:
source_id:
---
```

3. agent 명령 설계

```text
옵시디언 저장      # 로컬 변경 commit/push/server pull
옵시디언 수집      # 현재 대화/웹 자료를 00-Inbox 또는 01-Raw에 저장
옵시디언 컴파일    # 01-Raw 변경분을 03-Wiki로 컴파일
옵시디언 점검      # broken links, stale claims, orphan pages, contradictions lint
옵시디언 그래프    # Graphify 실행 후 05-Graphs에 report 저장
옵시디언 질의 X    # wiki/graph 우선으로 X에 답하고 가치 있으면 저장
```

4. Git 운영

- raw source와 wiki output을 모두 Git에 저장한다.
- LLM이 수정하는 계층과 사람이 수정하는 계층을 분리한다.
- server/local 양방향 sync는 기존 `scripts/sync_local_to_server.py`, `scripts/save_to_obsidian.py` 흐름을 유지한다.
- 동시 ingest를 피하려면 lock file 또는 Git 상태 검사(`git status --porcelain`)를 명령 시작 전에 강제한다.

## 주의점

- LLM Wiki는 RAG를 완전히 대체한다기보다, 반복적으로 쓰는 고가치 지식을 미리 컴파일하는 계층이다.
- blind compilation은 중요한 사실을 누락할 수 있다. 연구에서도 compile/evaluate/refine 루프가 필요하다는 결과가 나온다.
- Graphify 출력의 inferred edge는 검증된 사실이 아니라 탐색 후보로 봐야 한다.
- 개인/팀 wiki는 사용자의 기존 관점을 강화하는 편향이 생길 수 있으므로 contradiction, minority hypothesis, stale claim을 구조적으로 남겨야 한다.
- raw source는 LLM이 수정하지 못하게 분리해야 한다.

## 참고 자료

- Andrej Karpathy, LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Ar9av/obsidian-wiki: https://github.com/Ar9av/obsidian-wiki
- green-dalii/obsidian-llm-wiki: https://github.com/green-dalii/obsidian-llm-wiki
- atomicstrata/llm-wiki-compiler: https://github.com/atomicstrata/llm-wiki-compiler
- safishamsi/graphify: https://github.com/safishamsi/graphify
- Graphify docs/site: https://graphify.net/tw/
- Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki: https://arxiv.org/abs/2605.25480
- WiCER: Wiki-memory Compile, Evaluate, Refine Iterative Knowledge Compilation for LLM Wiki Systems: https://arxiv.org/abs/2605.07068
- Memory as Metabolism: A Design for Companion Knowledge Systems: https://arxiv.org/abs/2604.12034

## 연결 노트

- [[LLM Wiki와 에이전트 지식 관리 MOC]]
- [[LLM Wiki]]
- [[Graphify]]
- [[Obsidian 지식 인터페이스]]
