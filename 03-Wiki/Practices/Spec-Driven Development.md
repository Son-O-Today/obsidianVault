---
title: Spec-Driven Development
created: 2026-06-08T00:00:00+09:00
source: compiled
kind: wiki
status: compiled
tags: [wiki, ai-agent, software-development, workflow, spec-driven-development, enterprise]
aliases: [SDD, Spec Driven Development, Specification-Driven Development]
sources:
  - "[[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]"
---

# Spec-Driven Development

## Summary

Spec-Driven Development는 AI가 구현 목표를 추측하지 않도록 요구사항, acceptance criteria, 기술 설계, 구현 task를 먼저 확정하는 개발 방식이다. AI 코딩 시대에는 "코드를 바로 생성"하는 것보다 "무엇을 생성해야 하는지 명확한 spec을 먼저 작성"하는 것이 품질과 추적성을 높인다.

GitHub Spec Kit, Amazon Kiro, OpenSpec, BMAD Method, Spec Kitty 등 여러 도구와 방법론이 이 방향으로 수렴하고 있다.

## 기본 흐름

```text
요구사항
-> Acceptance Criteria
-> 기술 설계
-> 구현 Task
-> AI 구현
-> Spec 대비 검증
-> 인간 승인
```

## 핵심 산출물

- 요구사항: 사용자가 원하는 결과와 범위를 정리한다.
- Acceptance Criteria: 완료 여부를 판정할 수 있는 조건을 명시한다.
- Technical Design: 아키텍처, 데이터 모델, API, 보안 제약을 정리한다.
- Task Breakdown: agent가 실행 가능한 작은 작업으로 나눈다.
- Verification: 테스트, lint, security scan, spec match review로 구현을 검증한다.

## 주요 구현체

- GitHub Spec Kit
- Amazon Kiro
- OpenSpec
- BMAD Method
- Spec Kitty
- Claude Code, Codex, Cursor에서 쓰는 자체 spec-first workflow

## 기업에서 선호되는 이유

- AI가 목표와 제약을 추측하는 일을 줄인다.
- 요구사항과 생성 코드 사이의 추적성을 만든다.
- acceptance criteria를 테스트로 전환하기 쉽다.
- 아키텍처, 보안, compliance 제약을 구현 전에 명시할 수 있다.
- PR 리뷰 기준을 "spec과 일치하는가"로 정리할 수 있다.
- 규제나 감사가 필요한 조직에서 변경 근거를 남기기 쉽다.

## 기업 도입 근거

Amazon Kiro는 enterprise 고객으로 Siemens, FINRA, Rackspace, Appian, SmugMug, Mondelez, Hughes Network Systems, Netsmart 등을 공개한다. Kiro의 핵심 메시지는 spec-driven development이며, 이는 SDD가 기업 환경에서 받아들여질 가능성이 높다는 간접 근거다.

GitHub Spec Kit도 [[Agentic DevOps]]와 결합하기 쉬운 spec-first 도구다. 기업은 이를 통해 issue와 PR 사이에 더 명확한 요구사항·설계 계층을 둘 수 있다.

## 한계

- 작은 버그 수정이나 탐색적 실험에는 절차가 과할 수 있다.
- spec을 잘못 쓰면 agent가 잘못된 요구사항을 정확하게 구현한다.
- spec 작성 책임과 승인 책임을 정하지 않으면 문서만 늘어난다.
- 현업에서는 모든 작업에 SDD를 강제하기보다 작업 크기와 위험도에 따라 hybrid로 적용하는 편이 현실적이다.

## 적용 기준

SDD를 강하게 적용할 작업:

- 신규 제품이나 큰 기능
- 데이터 모델 또는 API가 바뀌는 작업
- 보안, 권한, 결제, compliance와 관련된 작업
- 여러 팀이 동시에 이해해야 하는 변경

가볍게 적용할 작업:

- 작은 UI 수정
- 명확한 버그 수정
- 실험적 prototype
- 내부 스크립트의 사소한 변경

## Related

- [[OpenSpec과 Spec Kit]]
- [[Agentic DevOps]]
- [[AI-DLC]]
- [[AI 에이전트 지식 운영]]
- [[지식 컴파일]]

## Sources

- [[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]
- https://github.github.com/spec-kit/
- https://kiro.dev/enterprise/
- https://kiro.dev/about/
- https://www.infoq.com/articles/enterprise-spec-driven-development/
