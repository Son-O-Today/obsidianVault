---
title: OpenSpec과 Spec Kit 비교
created: 2026-06-10T00:00:00+09:00
source: conversation-research
kind: raw
status: reviewed
tags: [source, ai-agent, software-development, workflow, spec-driven-development, openspec, spec-kit]
source_id: conversation-research-2026-06-10-openspec-spec-kit
---

# OpenSpec과 Spec Kit 비교

> 이 문서는 2026-06-10 대화에서 정리한 OpenSpec과 GitHub Spec Kit의 목적, 흐름, 차이점, Superpowers 결합 방식을 기록한다.

## 요약

OpenSpec과 GitHub Spec Kit은 모두 [[Spec-Driven Development]] 도구다. AI가 채팅 내용만 보고 바로 코딩하지 않도록 구현 전에 요구사항과 설계를 파일로 확정한다.

핵심 차이는 적용 강도다.

- OpenSpec: 변경 단위로 가볍고 유연하게 spec을 관리한다.
- Spec Kit: 프로젝트 공통 원칙부터 요구사항, 계획, task까지 단계적으로 관리한다.

개인 또는 소규모 프로젝트에서 Superpowers와 함께 쓸 때는 OpenSpec이 중복이 적다. 여러 팀이 공통 품질·보안·접근성 규칙을 따라야 한다면 Spec Kit이 더 적합하다.

## OpenSpec

OpenSpec은 AI coding assistant를 위한 경량 spec-driven development framework다. 요구사항이 채팅 기록에만 남아 생기는 예측 불가능성을 줄이는 것이 목적이다.

### 기본 흐름

```text
/opsx:propose
-> /opsx:apply
-> /opsx:archive
```

기능을 제안하면 변경별 폴더를 만든다.

```text
openspec/
└── changes/
    └── add-dark-mode/
        ├── proposal.md
        ├── specs/
        ├── design.md
        └── tasks.md
```

각 산출물의 역할:

- `proposal.md`: 변경 이유와 범위
- `specs/`: 요구사항과 시나리오
- `design.md`: 기술적 접근
- `tasks.md`: 구현 작업 목록

구현이 끝나면 변경 내용을 archive하고 기존 spec에 반영한다.

### 특징

- 단계 사이를 자유롭게 오가며 수정할 수 있다.
- 기존 프로젝트인 brownfield에 적용하기 쉽다.
- 변경마다 독립적인 명세와 이력을 남긴다.
- 25개 이상의 AI coding tool을 지원한다.
- 기본 workflow가 단순하다.
- 개인 프로젝트부터 기업 프로젝트까지 확장할 수 있다.
- 2026-06-10 공식 저장소 표시 기준 약 53.9k stars다.

### 장점

- 절차가 가볍다.
- 작은 기능과 변경에도 적용하기 쉽다.
- 채팅 context가 사라져도 요구사항과 결정이 남는다.
- Superpowers의 구현 workflow와 역할 중복이 비교적 적다.

### 한계

- 조직 전체의 개발 원칙을 강하게 통제하는 기능은 Spec Kit보다 약하다.
- spec의 품질은 작성자와 AI의 판단에 의존한다.
- 기본 workflow만으로 테스트와 code review를 강제하지 않는다.

### 설치

```bash
npm install -g @fission-ai/openspec@latest
cd project
openspec init
```

## GitHub Spec Kit

Spec Kit은 GitHub가 만든 체계적인 spec-driven development toolkit이다. 프로젝트 공통 원칙, 요구사항, 기술 계획, task, 구현을 명시적인 단계로 관리한다.

### 기본 흐름

```text
constitution
-> specify
-> plan
-> tasks
-> implement
```

주요 명령:

```text
/speckit.constitution  프로젝트 공통 원칙 정의
/speckit.specify       요구사항과 user story 정의
/speckit.plan          기술 stack과 구현 설계 작성
/speckit.tasks         실행 가능한 작업으로 분해
/speckit.implement     작업 구현
```

생성 구조의 예:

```text
.specify/
├── memory/
│   └── constitution.md
├── templates/
└── scripts/

specs/
└── 001-feature/
    ├── spec.md
    ├── plan.md
    └── tasks.md
```

### Constitution

Spec Kit의 중요한 차별점은 프로젝트 전체가 따라야 할 원칙을 먼저 선언하는 것이다.

예:

- 테스트 없는 기능은 병합하지 않는다.
- 접근성 기준을 충족해야 한다.
- 개인정보를 로그에 남기지 않는다.
- 새로운 library 도입 시 필요성을 설명한다.
- 성능과 보안 검사를 통과해야 한다.

이 원칙은 이후 spec, plan, implementation 판단에 계속 사용된다.

### 특징

- GitHub 공식 프로젝트다.
- 30개 이상의 AI coding agent를 지원한다.
- 요구사항과 기술 계획을 명확히 분리한다.
- 생성한 task를 GitHub Issue로 변환할 수 있다.
- extension과 조직용 preset을 지원한다.
- 2026-06-10 공식 저장소 표시 기준 약 111k stars다.

### 장점

- 여러 개발자와 agent에게 공통 기준을 적용하기 좋다.
- 요구사항, 설계, 구현 사이의 추적성이 강하다.
- 보안, 테스트, 접근성 같은 조직 정책을 명문화할 수 있다.
- GitHub Issue와 Pull Request workflow에 연결하기 쉽다.

### 한계

- OpenSpec보다 문서와 단계가 많다.
- 작은 수정에는 절차가 과할 수 있다.
- Superpowers와 함께 사용하면 planning, task breakdown, implementation 단계가 중복될 수 있다.

## 비교

| 항목 | OpenSpec | Spec Kit |
|---|---|---|
| 방향 | 가볍고 유연함 | 체계적이고 엄격함 |
| 관리 단위 | 개별 변경 | 프로젝트 원칙과 기능 |
| 절차 | propose, apply, archive | constitution, specify, plan, tasks, implement |
| 단계 변경 | 자유로움 | 순차적인 phase gate 성격 |
| 조직 공통 원칙 | 상대적으로 약함 | constitution으로 강하게 관리 |
| 기존 프로젝트 | 적용하기 쉬움 | 초기 설정과 정리가 더 필요 |
| 작은 기능 | 적합 | 다소 무거움 |
| 기업·다중 팀 | 적용 가능 | 더 적합 |
| Superpowers 결합 | 역할 중복이 적음 | 계획·구현 단계가 많이 겹침 |

## Superpowers와의 결합

### 개인·소규모 프로젝트

```text
Obsidian
-> OpenSpec
-> Superpowers
-> GitHub PR·CI
```

역할:

- Obsidian: 조사, 결정 근거, 장기 지식
- OpenSpec: 변경별 요구사항, 설계, acceptance criteria
- Superpowers: 구현 계획, TDD, subagent 실행, code review
- GitHub: Pull Request, CI, 보안 검사, 인간 승인

### 기업·다중 팀 프로젝트

```text
Spec Kit
-> Superpowers의 TDD·디버깅·리뷰
-> Agentic DevOps
```

Spec Kit이 명세와 계획을 담당한다. Superpowers는 TDD, systematic debugging, code review, verification에 집중시켜 workflow 중복을 줄인다.

## 판단

현재 사용자의 작업 방식에는 OpenSpec이 더 잘 맞는다.

근거:

- Obsidian으로 조사와 장기 지식을 이미 관리한다.
- 구현 전에 요구사항을 구체적으로 작성한다.
- Superpowers가 planning, TDD, subagent 구현, review를 담당할 수 있다.
- 따라서 Spec Kit 전체 workflow보다 OpenSpec의 가벼운 변경 명세 계층이 중복이 적다.

다음 조건에서는 Spec Kit을 선택한다.

- 여러 팀이나 agent가 같은 저장소에서 작업한다.
- 보안, 접근성, 테스트, 성능 규칙을 공통으로 강제해야 한다.
- 요구사항에서 GitHub Issue와 구현까지 추적성이 필요하다.
- 규제, 감사, 승인 절차가 중요하다.

## 출처

- OpenSpec: https://github.com/Fission-AI/OpenSpec
- GitHub Spec Kit: https://github.com/github/spec-kit
- Spec Kit Documentation: https://github.github.io/spec-kit/
- Superpowers: https://github.com/obra/superpowers

## 후속 컴파일

- [[OpenSpec과 Spec Kit]]
- [[Spec-Driven Development]]
- [[Agentic DevOps]]
