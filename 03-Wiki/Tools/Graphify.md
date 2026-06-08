---
title: Graphify
created: 2026-06-06T00:00:00+09:00
source: web-research-2026-06-05-llm-wiki-graphify
kind: wiki
status: compiled
tags: [wiki, graphify, knowledge-graph, ai-agent]
aliases: [knowledge graph analysis]
sources:
  - "[[2026-06-05 - LLM Wiki와 Graphify 웹 조사]]"
---

# Graphify

## 정의

Graphify는 코드와 문서에서 엔티티와 관계를 추출해 질의 가능한 knowledge graph를
만드는 도구다. 이 Vault에서는 [[LLM Wiki]]를 대체하는 것이 아니라, Wiki와 운영
스크립트의 관계를 분석하는 보조 계층이다.

## Obsidian과의 역할 분담

- [[Obsidian 지식 인터페이스]]: 사람이 작성·검토·탐색하는 Markdown 환경.
- [[LLM Wiki]]: 원본을 재사용 가능한 지식 페이지로 컴파일하는 기억 계층.
- Graphify: 파일과 개념의 연결을 그래프로 추출해 에이전트 질의를 지원하는 분석 계층.

## 주요 결과

- `graph.json`: 에이전트와 CLI가 질의하는 구조화된 그래프.
- `graph.html`: 사람이 브라우저에서 탐색하는 시각화.
- `GRAPH_REPORT.md`: hub, community, 주요 연결을 요약한 보고서.

## 신뢰 수준

- `EXTRACTED`: 원본 구조에서 직접 확인된 관계.
- `INFERRED`: 모델이 문맥을 바탕으로 추론한 관계.
- `AMBIGUOUS`: 검토가 필요한 불확실한 관계.

추론된 edge는 사실로 확정하지 않고 검토 후보로 취급해야 한다.

## 적용 범위

품질이 높은 `03-Wiki`, `04-MOCs`, 운영 문서와 스크립트를 우선 분석한다.
`00-Inbox`는 잡음이 많기 때문에 기본 그래프에서 제외하는 편이 적합하다.

## 관련

- [[LLM Wiki]]
- [[Obsidian 지식 인터페이스]]
- [[AI 에이전트 지식 운영]]
- [[LLM Wiki와 에이전트 지식 관리 MOC]]

## 출처

- [[2026-06-05 - LLM Wiki와 Graphify 웹 조사]]
- https://github.com/safishamsi/graphify
