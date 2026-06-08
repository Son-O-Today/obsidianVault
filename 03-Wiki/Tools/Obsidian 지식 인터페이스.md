---
title: Obsidian 지식 인터페이스
created: 2026-06-06T00:00:00+09:00
source: web-research-2026-06-05-llm-wiki-graphify
kind: wiki
status: compiled
tags: [wiki, obsidian, knowledge-interface]
aliases: [Obsidian, 옵시디언]
sources:
  - "[[2026-06-05 - LLM Wiki와 Graphify 웹 조사]]"
---

# Obsidian 지식 인터페이스

## 역할

Obsidian은 [[LLM Wiki]]를 사람이 읽고 편집하고 탐색하는 인터페이스다. Markdown과
Git을 사용하므로 특정 데이터베이스에 종속되지 않고, 사람과 에이전트가 같은 파일을
공유할 수 있다.

## 주요 기능

- Wikilink: 개념 간 명시적 연결을 만든다.
- Backlinks: 어떤 페이지가 현재 개념을 참조하는지 보여준다.
- Graph View: hub, 고아 노트, 주제 cluster를 시각적으로 확인한다.
- Frontmatter: 상태, 종류, 출처, 태그를 기계가 읽을 수 있게 기록한다.
- Templates: 사람이 쓰는 노트와 에이전트가 쓰는 노트의 형태를 통일한다.

## 이 Vault에서의 역할

- `01-Raw`: 근거 자료를 보존한다.
- `02-Notes`: 사람이 생각하고 작성한다.
- `03-Wiki`: 에이전트가 컴파일된 지식을 관리한다.
- `04-MOCs`: 사람이 주제별로 진입한다.
- `05-Graphs`: [[Graphify]] 결과를 보관한다.

## 한계

Obsidian Graph View는 명시적인 wikilink를 시각화하지만, 문서에 암묵적으로 존재하는
의미 관계를 자동 추론하지는 않는다. 이 부분은 [[Graphify]] 같은 분석 계층이 보완한다.

## 관련

- [[LLM Wiki]]
- [[Graphify]]
- [[지식 컴파일]]
