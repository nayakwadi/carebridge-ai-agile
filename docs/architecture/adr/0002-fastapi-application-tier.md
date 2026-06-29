# ADR 0002 — FastAPI for the application tier

## Status

Accepted.

## Context

The application tier is the heart of CareBridge: it validates every request, authenticates users,
enforces business rules, writes the HIPAA-style audit trail, and serves cached aggregates. It is
the only tier that touches PHI, so request/response correctness and a self-describing API contract
matter a great deal. The team is Python-fluent, and the data shapes (patients, care plans, tasks)
benefit from strong typing at the boundary. We also expect future I/O-bound integrations
(downstream FHIR calls, notifications) where non-blocking concurrency would help.

## Decision

Use **FastAPI** (with Pydantic and SQLAlchemy) for the application tier, served on port `8000`
with interactive Swagger UI at `/docs`. Pydantic schemas validate input and shape output;
SQLAlchemy models map to the PostgreSQL schema; a custom middleware writes the audit log; PyJWT
handles token issue/verify.

## Consequences

**Positive**

- **Auto-generated OpenAPI / Swagger** — the `/docs` UI and machine-readable contract come for
  free, which is invaluable for frontend integration and for demonstrating the API to reviewers.
- **Pydantic validation** rejects malformed requests at the edge and, on the way out, restricts
  responses to declared fields — a direct PHI-minimization control rather than a convention.
- **Native async** gives headroom to make future external I/O non-blocking without a framework
  change.
- **Middleware model** made the cross-cutting audit trail clean: one `BaseHTTPMiddleware` wraps
  every `/api` request, so logging can't be forgotten per-endpoint.
- Lightweight and fast to develop; minimal boilerplate compared to heavier frameworks.

**Negative / trade-offs**

- Smaller "batteries-included" surface than Django — no built-in admin, ORM, or auth, so those are
  assembled from libraries (SQLAlchemy, PyJWT) and owned by us.
- Async correctness requires discipline (avoiding blocking calls in async paths).
- A younger ecosystem than Flask/Django means fewer long-tail third-party integrations.

## Alternatives considered

- **Flask.** Mature and minimal, but lacks first-class async, native request/response validation,
  and auto OpenAPI; we'd hand-roll the schema validation and docs that FastAPI provides out of the box.
- **Django (+ DRF).** Excellent batteries (admin, ORM, auth) and great for large teams, but
  heavier than needed here, synchronous by default, and its conventions push toward a more
  monolithic shape than our clean three-tier boundary wants.
- **Node/Express or NestJS.** Viable, but would split the stack across two language ecosystems; the
  team's Python fluency and the typing benefits of Pydantic favored staying in Python.
