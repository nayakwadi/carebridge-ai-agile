# ADR 0003 — PostgreSQL for the data tier

## Status

Accepted.

## Context

CareBridge's domain is inherently relational: patients have care plans, care plans have tasks, and
tasks are assigned to care-team members. The data carries clinical meaning and regulatory weight,
so integrity is non-negotiable — a task must not reference a non-existent plan, a patient's MRN
must be unique, and a status must never fall outside its allowed set. We also need a tamper-evident
audit trail and, looking ahead to EU/Canada expansion, predictable data-residency and operational
characteristics.

## Decision

Use **PostgreSQL 16** as the system of record, with the schema defined canonically in
`database/init.sql` and enforced in the database itself:

- `FOREIGN KEY` constraints with deliberate cascade rules (`ON DELETE CASCADE` for
  patient → plan → task; `ON DELETE SET NULL` for task → assignee).
- `CHECK` constraints for enumerated values (risk level, statuses, priority).
- `UNIQUE` natural keys (`patients.mrn`, `care_team_members.email`).
- Indexes on the hot access paths and on `audit_log.occurred_at`.

Redis 7 sits alongside as an ephemeral, best-effort cache for aggregates only — it holds no PHI and
is never the source of truth.

## Consequences

**Positive**

- **ACID transactions** guarantee that multi-row writes (e.g. a plan and its tasks) are atomic and
  consistent — essential for clinical data.
- **Integrity in the database** means invalid state is impossible to persist even via a direct SQL
  path, not just unlikely via the app. Constraints are a safety net under application bugs.
- **Mature operations**: replication, point-in-time recovery, fine-grained role-based grants
  (enabling least-privilege and an append-only `audit_log`), and broad managed-service support
  (RDS/Cloud SQL) for the EU/Canada footprint.
- Rich SQL and `TIMESTAMPTZ` support make audit and timeline queries straightforward.

**Negative / trade-offs**

- A rigid schema means structural changes require migrations and coordination (acceptable, and
  arguably desirable, for regulated data).
- Horizontal write scaling is harder than with some NoSQL stores — mitigated for now by read
  replicas and aggregate caching; not a concern at MVP scale.
- Requires a disciplined migration tool (Alembic) before GA to keep schema changes reviewable.

## Alternatives considered

- **MongoDB / document store.** Flexible schema and easy horizontal scaling, but our data is
  relational, not document-shaped; we'd reimplement referential integrity and enum validation in
  application code and lose the in-database guarantees that matter most for clinical/regulated data.
- **MySQL/MariaDB.** A reasonable relational alternative, but PostgreSQL's constraint expressiveness,
  `TIMESTAMPTZ` handling, and feature depth made it the stronger fit; no compelling reason to prefer it.
- **SQLite.** Used in the automated tests for speed and isolation, but unsuitable as the production
  system of record (concurrency, scaling, operational tooling).
