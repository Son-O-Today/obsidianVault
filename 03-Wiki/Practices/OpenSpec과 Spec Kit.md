---
title: OpenSpec과 Spec Kit
created: 2026-06-10T00:00:00+09:00
source: compiled
kind: wiki
status: compiled
tags: [wiki, ai-agent, software-development, workflow, spec-driven-development, openspec, spec-kit]
aliases: [OpenSpec vs Spec Kit, OpenSpec Spec Kit 비교]
sources:
  - "[[2026-06-10 - OpenSpec과 Spec Kit 비교]]"
---

# OpenSpec과 Spec Kit

## Summary

OpenSpec과 GitHub Spec Kit은 AI가 코드를 작성하기 전에 요구사항과 설계를 파일로 확정하는 [[Spec-Driven Development]] 도구다.

- OpenSpec은 변경별 spec을 가볍고 유연하게 관리한다.
- Spec Kit은 프로젝트 원칙부터 구현 task까지 체계적으로 관리한다.

개인·소규모 프로젝트에서 Superpowers와 함께 사용할 때는 OpenSpec이 중복이 적다. 여러 팀에 공통 품질·보안·접근성 정책을 강제해야 한다면 Spec Kit이 더 적합하다.

## OpenSpec

기본 흐름:

```text
propose
-> apply
-> archive
```

변경마다 다음 산출물을 관리한다.

- proposal: 변경 이유와 범위
- specs: 요구사항과 시나리오
- design: 기술적 접근
- tasks: 구현 작업 목록

강점:

- 기존 프로젝트에 도입하기 쉽다.
- 작은 기능에도 적용할 수 있다.
- 단계 사이를 자유롭게 수정할 수 있다.
- Superpowers의 planning과 역할 중복이 비교적 적다.

주의점:

- 조직 전체 정책을 강제하는 기능은 Spec Kit보다 약하다.
- 테스트와 code review는 별도 workflow가 담당해야 한다.

## Spec Kit

기본 흐름:

```text
constitution
-> specify
-> plan
-> tasks
-> implement
```

핵심은 `constitution`이다. 프로젝트가 따라야 할 품질, 테스트, UX, 성능, 보안 원칙을 정의하고 이후 요구사항과 구현 판단의 기준으로 사용한다.

강점:

- 여러 개발자와 agent에게 공통 규칙을 적용한다.
- 요구사항, 기술 계획, task, 구현 사이의 추적성이 강하다.
- task를 GitHub Issue로 변환할 수 있다.
- 조직용 extension과 preset을 사용할 수 있다.

주의점:

- 작은 변경에는 절차가 무거울 수 있다.
- Superpowers와 planning, task breakdown, implementation이 중복될 수 있다.

## Comparison

| 기준 | OpenSpec | Spec Kit |
|---|---|---|
| 적용 강도 | 가벼움 | 엄격함 |
| 관리 중심 | 변경 단위 | 프로젝트 원칙과 기능 |
| 기존 프로젝트 | 도입하기 쉬움 | 초기 정리가 더 필요 |
| 작은 기능 | 적합 | 과할 수 있음 |
| 다중 팀·기업 | 가능 | 더 적합 |
| 정책 강제 | 상대적으로 약함 | constitution으로 강함 |
| Superpowers 조합 | 중복이 적음 | 역할 분리가 필요 |

## Recommended Stack

개인·소규모 프로젝트:

```text
Obsidian
-> OpenSpec
-> Superpowers
-> GitHub PR·CI
```

기업·다중 팀 프로젝트:

```text
Spec Kit
-> Superpowers의 TDD·디버깅·리뷰
-> [[Agentic DevOps]]
```

## Decision

현재 사용 방식에는 OpenSpec을 우선 추천한다.

- Obsidian이 장기 지식과 조사 기록을 담당한다.
- OpenSpec이 변경별 요구사항과 acceptance criteria를 담당한다.
- Superpowers가 계획, TDD, subagent 구현, review를 담당한다.
- GitHub가 PR, CI, 보안 검사, 인간 승인을 담당한다.

보안·접근성·테스트 원칙을 여러 팀에 강제하거나 감사 가능한 추적성이 필요해지면 Spec Kit으로 전환하는 것이 적절하다.

## Related

- [[Spec-Driven Development]]
- [[Agentic DevOps]]
- [[GitHub 인기 AI 코딩 워크플로우]]

## Sources

- [[2026-06-10 - OpenSpec과 Spec Kit 비교]]
- https://github.com/Fission-AI/OpenSpec
- https://github.com/github/spec-kit
- https://github.github.io/spec-kit/
- https://github.com/obra/superpowers
