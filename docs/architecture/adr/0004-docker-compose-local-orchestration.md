# ADR 0004 — Docker Compose for local orchestration

## Status

Accepted.

## Context

CareBridge is a three-tier system: a React/Vite frontend, a FastAPI backend, PostgreSQL, and Redis.
For a reviewer to evaluate the project — and for engineers to onboard — bringing the whole stack up
must be trivial, reproducible, and identical across machines. Database schema and seed data need to
load deterministically on first boot, and the API must not start serving before the database is
ready. This is a local-development and demonstration concern; production deployment is a separate
problem with separate tooling.

## Decision

Use **Docker Compose** (`docker-compose.yml`) to orchestrate four services — `web`, `api`, `db`,
`cache` — brought up with a single command:

```bash
docker compose up --build
```

- `db` (postgres:16-alpine) mounts `./database` into `docker-entrypoint-initdb.d`, so `init.sql`
  then `seed.sql` run in alphabetical order on first boot.
- `db` and `cache` expose health checks; `api` declares `depends_on` with
  `condition: service_healthy`, so it waits for a ready database before serving.
- Configuration (DB URL, Redis URL, JWT secret, CORS origin, API base URL) is injected via
  environment variables with safe local defaults; no secrets are committed.

## Consequences

**Positive**

- **One-command, reproducible stack** — the full system, schema-loaded and seeded, comes up
  identically on any machine with Docker. Ideal for onboarding and for portfolio reviewers.
- **Deterministic startup** via health checks and `depends_on` eliminates the classic "API booted
  before the DB" race.
- **Environment parity** for the application tiers reduces "works on my machine" drift.
- **Self-documenting topology** — the compose file is a readable map of the architecture, ports,
  and dependencies.

**Negative / trade-offs**

- Compose is a single-host tool — it does **not** provide the autoscaling, rolling deploys,
  service discovery, or self-healing a production cluster needs.
- It is not the production deployment artifact, so there is some divergence between local Compose
  and prod orchestration to manage.
- Requires Docker on every developer machine.

## Alternatives considered

- **Local-native install** (run Postgres/Redis/uvicorn/Vite by hand). No Docker dependency, but
  brittle, version-drift-prone, and slow to onboard — the opposite of reproducible.
- **Kubernetes (k3d/minikube) locally.** Closer to production, but heavyweight and steep for a
  local dev/demo loop; the YAML and operational overhead aren't justified at this stage.
- **Production orchestration (ECS / Kubernetes).** This is the intended **production** path, not a
  local one. Compose covers local dev and demonstration; a real deployment would target
  **ECS or Kubernetes** with managed Postgres (RDS/Cloud SQL), managed Redis, secrets from a
  secrets manager, and CI/CD — out of scope for this ADR.
