---
title: AI-DLC
created: 2026-06-08T00:00:00+09:00
source: compiled
kind: wiki
status: compiled
tags: [wiki, ai-agent, software-development, workflow, enterprise, aws]
aliases: [AWS AI-DLC, AI-Driven Development Lifecycle, AL-DLC]
sources:
  - "[[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]"
---

# AI-DLC

## Summary

AI-DLC는 AWS가 제시한 AI-Driven Development Lifecycle이다. 요구사항 정의, 구축, 운영을 하나의 생명주기로 묶고, 각 단계에서 AI agent가 계획·질문·실행·검증을 보조한다.

BMAD나 bkit처럼 이름 붙은 AI 개발 방법론 중에서는 기업 도입 근거가 비교적 강하다. Altisource의 legacy modernization 사례와 Serverworks의 도입 발표가 공개되어 있다.

## Lifecycle

```text
Inception
사업 요구사항, user story, acceptance criteria 결정

Construction
아키텍처, 도메인 모델, 코드, 테스트 생성 및 검토

Operations
배포, 모니터링, 장애 대응 및 개선
```

## 반복 루프

AI-DLC는 한 번에 코드를 생성하는 방식이 아니라 인간과 AI가 반복적으로 결정을 좁히는 방식에 가깝다.

```text
AI가 계획 작성
-> AI가 질문
-> 인간이 핵심 결정
-> AI가 실행
-> 자동 검증
-> 인간 승인
```

## 기업 도입 근거

- Altisource는 35만 줄 legacy code 현대화, 개발 생산성 25% 증가, 코드 취약점 54% 감소, 4개월 동안 신규 애플리케이션 4개 출시 사례를 공개했다.
- Serverworks는 2026년 1월 AI-DLC를 자사 개발·운영 프로세스에 도입하고 검증한다고 발표했다.
- AWS는 Amazon Q Developer와 Kiro 생태계에서 AI-DLC workflow를 사용할 수 있도록 공개했다.

## 현업 적합성

- AWS 기반 조직이 기존 개발·운영 흐름에 AI agent를 붙이기 쉽다.
- 요구사항, 구현, 운영을 따로 보지 않고 하나의 lifecycle로 연결한다.
- Jira, Bitbucket, Figma, 데이터베이스 같은 기업 도구를 MCP로 연결하는 패턴과 잘 맞는다.
- [[Spec-Driven Development]]와 결합하면 요구사항 추적성과 구현 검증이 강화된다.

## 한계

- AWS 생태계 의존도가 높아질 수 있다.
- 조직의 CI/CD, 보안 검사, 리뷰 프로세스가 약하면 AI-DLC만으로 품질을 보장하기 어렵다.
- 작은 버그 수정까지 전체 lifecycle로 다루면 절차가 무거워질 수 있다.

## Related

- [[Agentic DevOps]]
- [[Spec-Driven Development]]
- [[AI 에이전트 지식 운영]]

## Sources

- [[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]
- https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
- https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/
- https://github.com/awslabs/aidlc-workflows
- https://aws.amazon.com/solutions/case-studies/altisource-case-study/
- https://www.serverworks.co.jp/news/20260116_aws_ai-dlc.html
