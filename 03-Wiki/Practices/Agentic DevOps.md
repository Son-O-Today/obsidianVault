---
title: Agentic DevOps
created: 2026-06-08T00:00:00+09:00
source: compiled
kind: wiki
status: compiled
tags: [wiki, ai-agent, software-development, devops, workflow, enterprise, github]
aliases: [GitHub Agentic DevOps, Agentic SDLC]
sources:
  - "[[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]"
---

# Agentic DevOps

## Summary

Agentic DevOps는 AI agent를 기존 DevOps와 SDLC에 끼워 넣는 워크플로우다. 핵심은 AI가 issue나 요구사항을 받아 계획과 구현을 수행하되, Pull Request, CI/CD, 보안 검사, 인간 리뷰를 병합 경계로 유지하는 것이다.

현재 공개 근거 기준으로 기업에서 가장 넓게 쓰이는 AI 개발 워크플로우는 특정 오픈소스 방법론보다 GitHub 기반 Agentic DevOps에 가깝다.

## 기본 흐름

```text
Issue 또는 요구사항
-> AI 계획
-> 에이전트 구현
-> Draft Pull Request
-> CI 테스트와 보안 검사
-> 인간 리뷰
-> 수정 반복
-> Merge
```

## 기업 도입 근거

- GitHub Copilot 도입 조직은 77,000개 이상으로 공개되었다.
- Fortune 100의 90% 이상이 GitHub를 사용한다는 GitHub 공개 자료가 있다.
- GitHub Actions는 평일 기준 하루 4,000만 개 이상의 job을 실행한다는 자료가 있다.
- GitHub는 enterprise 환경에서 agentic AI를 기존 SDLC에 통합하는 가이드를 제공한다.

대표 사례:

- EY는 개발자 2,000명에게 Copilot을 배포했고 AI 생성 코드 120만 줄 이상을 채택했다고 공개했다.
- Carvana는 specification을 production code로 변환하는 agent workflow 사례로 언급된다.
- Grupo Boticário는 GitHub 공개 자료에서 개발 생산성 증가 사례로 소개된다.

## 왜 현업에 잘 맞는가

- 기존 GitHub Issue, Pull Request, Actions, code review 문화를 유지한다.
- AI agent의 권한을 draft PR 생성까지로 제한하기 쉽다.
- 테스트, lint, security scan, deployment gate를 기존 자동화에 얹을 수 있다.
- 신규 방법론을 전사적으로 가르치는 비용보다 도입 비용이 낮다.
- 실패 시 책임 경계가 PR과 reviewer에 남는다.

## 설계 원칙

- AI agent는 변경 초안을 만든다.
- CI/CD와 보안 검사는 merge gate로 둔다.
- 인간 reviewer가 승인권을 가진다.
- 작은 변경은 issue 기반으로 처리하고, 큰 변경은 [[Spec-Driven Development]]로 요구사항과 acceptance criteria를 먼저 만든다.
- 반복되는 실패와 운영 지식은 [[AI 에이전트 지식 운영]]에 축적한다.

## 한계

- 기존 테스트와 CI 품질이 낮으면 agent가 만든 PR을 제대로 검증하지 못한다.
- issue가 모호하면 agent가 잘못된 구현을 그럴듯하게 만들 수 있다.
- 기업마다 내부 규칙과 권한 모델이 달라 표준화된 단일 방법론으로 보기 어렵다.

## Related

- [[Spec-Driven Development]]
- [[AI-DLC]]
- [[AI 에이전트 지식 운영]]

## Sources

- [[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]
- https://github.com/newsroom/press-releases/coding-agent-for-github-copilot
- https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/enabling-developers/integrating-agentic-ai
- https://github.com/customer-stories/ey
