---
title: GitHub 인기 AI 코딩 워크플로우
created: 2026-06-08T00:00:00+09:00
source: compiled
kind: wiki
status: compiled
tags: [wiki, github, ai-agent, software-development, workflow, methodology]
aliases: [인기 AI 코딩 워크플로우, AI coding workflow ranking, GitHub AI workflow ranking]
sources:
  - "[[2026-06-08 - GitHub 인기 AI 코딩 워크플로우 조사]]"
---

# GitHub 인기 AI 코딩 워크플로우

## Summary

GitHub stars 기준으로 인기 있는 AI 코딩 워크플로우는 대부분 계획, spec, task 분해, agent 실행, 테스트, 리뷰를 구조화한다. 단순히 AI에게 코드를 생성시키는 도구보다, AI가 일할 수 있는 개발 절차를 만드는 방법론이 인기를 얻고 있다.

2026-06-08 조사 기준 상위권은 Superpowers, GitHub Spec Kit, GSD, OpenSpec, BMAD Method다.

## Ranking

| 순위 | 프로젝트 | Stars | 핵심 |
|---:|---|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 221k | 스킬 기반 AI 코딩 방법론 |
| 2 | [GitHub Spec Kit](https://github.com/github/spec-kit) | 110k | GitHub 공식 spec-driven toolkit |
| 3 | [GSD](https://github.com/gsd-build/get-shit-done) | 64k | context engineering + spec-driven workflow |
| 4 | [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 53.4k | lightweight spec-driven framework |
| 5 | [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | 48.8k | PRD, architecture, epic/story 기반 AI agile |
| 6 | [Claude Task Master](https://github.com/eyaltoledano/claude-task-master) | 27.3k | PRD를 agent task로 분해 |
| 7 | [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 23.2k | Claude Code command, agent, persona, MCP 확장 |
| 8 | [Spec Kitty](https://github.com/Priivacy-ai/spec-kitty) | 1.3k | spec, plan, task, agent loop, review |
| 9 | [MoAI-ADK](https://github.com/modu-ai/moai-adk) | 1.1k | SPEC-first agentic development kit |
| 10 | [bkit](https://github.com/popup-studio-ai/bkit-claude-code) | 556 | Claude Code PDCA workflow plugin |

## Patterns

상위 프로젝트는 이름과 구현 방식은 다르지만 다음 패턴을 공유한다.

- 먼저 요구사항이나 spec을 만든다.
- 작업을 agent가 실행 가능한 단위로 쪼갠다.
- 구현 전에 계획이나 설계를 승인한다.
- 테스트, 리뷰, gap detection, self-repair 같은 검증 루프를 둔다.
- 결과를 PR, branch, report, task status 같은 기존 개발 산출물로 남긴다.

## Categories

### Spec-first

GitHub Spec Kit, OpenSpec, Spec Kitty, MoAI-ADK, BMAD Method는 [[Spec-Driven Development]]와 직접 맞닿아 있다. 이 계열은 요구사항과 acceptance criteria를 먼저 고정하고, 이후 agent 구현과 검증을 붙인다.

### Project-management 중심

BMAD Method와 Claude Task Master는 PRD, epic, story, task, subtask, dependency 같은 제품 개발 관리 단위를 중요하게 다룬다. 기능이 커질수록 이 계열이 유리하다.

### Claude Code 중심

Superpowers, SuperClaude Framework, bkit은 Claude Code 또는 유사 agentic coding harness에 붙여 쓰기 좋다. command, agent, skill, hook, MCP, PDCA 같은 실행 계층을 제공한다.

### 검증 루프 중심

bkit, GSD, Superpowers, MoAI-ADK는 구현 이후의 분석, 리뷰, 테스트, gap detection, 반복 수정에 무게를 둔다. 품질 gate가 중요한 팀에 더 적합하다.

## Selection Guide

| 필요 | 우선 검토 |
|---|---|
| 가장 큰 개발자 traction | Superpowers |
| GitHub 조직 표준화 | GitHub Spec Kit |
| 가벼운 spec-first 시작 | OpenSpec, Spec Kitty |
| PRD와 story 기반 제품 개발 | BMAD Method |
| PRD를 task로 분해 | Claude Task Master |
| Claude Code 운영 강화 | Superpowers, SuperClaude Framework, bkit |
| 검증과 반복 수정 자동화 | bkit, GSD, MoAI-ADK |

## Enterprise Relevance

GitHub stars는 개발자 관심도 지표이지 기업 도입량 지표는 아니다. 기업 현업 사용 가능성을 따로 보면 GitHub Spec Kit은 [[Agentic DevOps]]와 결합하기 쉬워 조직 도입 가능성이 높고, BMAD Method는 문서와 story 기반 개발을 원하는 팀에 적합하다. Superpowers는 stars 규모가 압도적이지만, 전사 도입 근거보다 개인/소규모 팀의 실사용 가능성이 더 강한 신호다.

기업에서는 보통 단일 오픈소스 방법론을 그대로 도입하기보다 다음 조합을 쓴다.

```text
[[Spec-Driven Development]]
+ agent execution
+ CI/CD
+ security gate
+ human review
+ [[Agentic DevOps]]
```

## Related

- [[Spec-Driven Development]]
- [[Agentic DevOps]]
- [[AI-DLC]]
- [[AI 에이전트 지식 운영]]

## Sources

- [[2026-06-08 - GitHub 인기 AI 코딩 워크플로우 조사]]
- [[2026-06-08 - AI 코딩 워크플로우와 기업 도입 조사]]
