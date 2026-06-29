# ADR 0001 — Three-tier architecture

## Status

Accepted.

## Context

CareBridge is a patient care-coordination platform handling PHI for hospital care teams, targeting
HIPAA + SOC 2 Type II readiness before general availability. We need an architecture that (a)
isolates PHI behind an auditable boundary, (b) lets a browser UI, business logic, and durable
storage evolve and scale independently, and (c) is simple enough for a single team to run and a
reviewer to reason about. The product is a fairly conventional CRUD-plus-workflow application
(patients → care plans → tasks), not an event-streaming or analytics system.

## Decision

Adopt a classic **three-tier architecture** with hard boundaries:

- **Presentation** — React 18 + TypeScript (Vite). Renders the dashboard, patient list, and
  care-plan Kanban board. Holds no database credentials and never talks to storage directly.
- **Application** — FastAPI REST API. Owns validation, authentication, business rules, the
  HIPAA-style audit trail, and caching. This is the only tier that touches PHI.
- **Data** — PostgreSQL (system of record) plus Redis (ephemeral aggregate cache).

All cross-tier traffic is explicit: the browser speaks JSON/HTTP to the API over a CORS-scoped
origin; the API speaks SQL to Postgres and a key/value protocol to Redis.

## Consequences

**Positive**

- A single security choke point: every PHI request crosses the API, where audit logging and auth
  are enforced uniformly. This is what makes a credible HIPAA access trail possible.
- Each tier scales on its own curve — static/CDN frontend, stateless horizontally-scaled API,
  vertically-scaled Postgres with read replicas.
- Clear separation of concerns keeps changes local: UI work can't break the data model, and schema
  changes are mediated by typed schemas at the API edge.
- The model is widely understood, which lowers onboarding cost and review friction.

**Negative / trade-offs**

- More moving parts than a monolith-with-templates: three deployable units to build, wire, and
  operate (mitigated locally by Docker Compose — see ADR 0004).
- Network hops between tiers add latency versus an in-process design (mitigated by caching
  aggregates and indexing hot paths).
- Some boilerplate is duplicated across tiers (e.g. types described in both TypeScript and Pydantic).

## Alternatives considered

- **Monolithic server-rendered app** (e.g. Django templates). Simpler to deploy, but couples the
  UI to the request cycle and weakens the clean PHI boundary we want for HIPAA; harder to evolve
  the frontend independently.
- **Microservices.** Overkill for a single bounded domain at MVP scale; the operational and
  distributed-systems overhead would dwarf the benefit. The three-tier split can evolve toward
  services later if a domain genuinely needs it.
- **Serverless / BaaS (e.g. Firebase).** Fast to start, but cedes control over the audit trail,
  data residency (EU/Canada expansion), and least-privilege data access that a regulated health
  product requires.
