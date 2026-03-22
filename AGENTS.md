# Capstone Sub-Agent Guide

This repository uses project-level sub-agents to keep implementation work separated by responsibility.

## Active Sub-Agents

### 1. Frontend Integration Agent
- Purpose: Owns frontend-facing integration work across UI, API wiring, and user interaction flows.
- Scope:
  - Connect frontend clients to backend or AI APIs
  - Define request/response contracts needed by UI consumers
  - Coordinate auth, CORS, routing, and client-facing error handling
  - Prepare integration points for future frontend apps even if the UI code is stored outside this repository
- Primary directories:
  - `/home/yjjang/capstone/backend`
  - `/home/yjjang/capstone/ai`
  - `/home/yjjang/capstone/docs`
- Avoid:
  - Owning core infrastructure provisioning
  - Refactoring unrelated backend internals unless required for integration

### 2. Infrastructure Management Agent
- Purpose: Owns runtime environment, deployment plumbing, observability, and operational reliability.
- Scope:
  - Maintain Docker, Compose, environment wiring, and service startup flow
  - Manage monitoring and operational configuration
  - Standardize deployment-related scripts and container responsibilities
  - Review networking, volumes, ports, and secret handling patterns
- Primary directories:
  - `/home/yjjang/capstone/infra`
  - `/home/yjjang/capstone/docker-compose.yml`
  - `/home/yjjang/capstone/prometheus.yml`
  - `/home/yjjang/capstone/.env`
- Avoid:
  - Changing product logic unless infra changes require a small compatibility edit

### 3. Integrated System Management Agent
- Purpose: Owns cross-service coordination, end-to-end behavior, and system-level consistency.
- Scope:
  - Coordinate workflows spanning `agent`, `ai`, `backend`, and infrastructure
  - Validate service boundaries and inter-service contracts
  - Resolve integration regressions that affect multiple domains
  - Keep high-level architecture, docs, and operational behavior aligned
- Primary directories:
  - `/home/yjjang/capstone/agent`
  - `/home/yjjang/capstone/ai`
  - `/home/yjjang/capstone/backend`
  - `/home/yjjang/capstone/docs`
  - `/home/yjjang/capstone/infra`
- Avoid:
  - Absorbing all work by default when a domain-specific agent can own it clearly

## Routing Rules

- Use the Frontend Integration Agent when the task is mainly about UI-facing API integration, client contracts, or frontend connectivity.
- Use the Infrastructure Management Agent when the task is mainly about containers, deployment, observability, networking, environment configuration, or runtime operations.
- Use the Integrated System Management Agent when the task spans multiple services or needs end-to-end coordination.
- If a task crosses boundaries, the Integrated System Management Agent should coordinate, but domain-specific changes should stay with the owning agent when possible.

## Collaboration Rules

- Agents are not alone in the codebase and must not revert changes they did not make.
- Prefer narrow ownership for edits to reduce overlap and merge conflicts.
- Document interface changes that affect another agent's work.
- When a task changes environment variables, ports, routes, or service contracts, update relevant docs in `/home/yjjang/capstone/docs` or nearby configuration comments.
- If a task is ambiguous, prefer the smallest responsible agent first; escalate to Integrated System Management only when coordination is needed.

## Current Repository Mapping

- `backend/`: API and service integration surface
- `ai/`: AI service logic and model-facing integration
- `agent/`: agent orchestration or agent-specific workflows
- `infra/`: deployment and environment support
- `docs/`: shared architecture and coordination notes

