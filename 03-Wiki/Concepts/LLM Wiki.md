---
title: LLM Wiki
created: 2026-06-06T00:00:00+09:00
source: web-research-2026-06-05-llm-wiki-graphify
kind: wiki
status: compiled
tags: [wiki, llm-wiki, knowledge-management]
aliases: [LLM 위키, compiled knowledge]
sources:
  - "[[2026-06-05 - LLM Wiki와 Graphify 웹 조사]]"
---

# LLM Wiki

## 정의

LLM Wiki는 원천 자료를 질문할 때마다 다시 검색하는 대신, LLM이 자료를 미리 읽고
구조화된 Markdown 지식으로 컴파일해 지속적으로 유지하는 방식이다.

## 핵심 계층

- **Raw sources**: 기사, 논문, 대화 기록, 회의록처럼 수정하지 않는 근거 자료.
- **Wiki**: 원본에서 추출·종합한 개념, 엔티티, 비교, 요약 페이지.
- **Schema**: 파일 구조, 메타데이터, 링크와 유지보수 절차를 정의한 운영 규약.

## 운영 루프

1. **Ingest**: 새 원본을 수집하고 관련 지식 페이지를 찾는다.
2. **Compile**: 새 사실을 기존 페이지에 병합하거나 새 원자적 페이지를 만든다.
3. **Query**: 원본보다 Wiki와 MOC를 먼저 탐색해 답한다.
4. **Refine**: 답변에서 나온 가치 있는 결론을 다시 Wiki에 반영한다.
5. **Lint**: 고아 노트, 깨진 링크, 모순, 오래된 주장을 점검한다.

## RAG와의 관계

LLM Wiki는 RAG를 완전히 대체하지 않는다. 반복적으로 사용하는 고가치 지식은
Wiki로 미리 컴파일하고, 세부 근거나 최신 정보가 필요할 때 원본 검색과 웹 검색을
병행하는 계층형 접근이 적합하다.

## 관련

- [[지식 컴파일]]
- [[Obsidian 지식 인터페이스]]
- [[Graphify]]
- [[AI 에이전트 지식 운영]]
- [[LLM Wiki와 에이전트 지식 관리 MOC]]

## 출처

- [[2026-06-05 - LLM Wiki와 Graphify 웹 조사]]
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
