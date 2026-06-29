-- CareBridge — Data tier schema (canonical DDL).
-- Auto-loaded by the postgres container on first boot via docker-entrypoint-initdb.d.
-- The FastAPI backend mirrors these tables as SQLAlchemy models (create_all is a
-- no-op when the schema already exists), so this file is the single source of truth.

CREATE TABLE IF NOT EXISTS care_team_members (
    id          SERIAL PRIMARY KEY,
    full_name   VARCHAR(120) NOT NULL,
    role        VARCHAR(60)  NOT NULL,   -- Physician | Nurse | Care Coordinator | Social Worker | Pharmacist
    email       VARCHAR(160) NOT NULL UNIQUE,
    specialty   VARCHAR(120),
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS patients (
    id                SERIAL PRIMARY KEY,
    mrn               VARCHAR(20)  NOT NULL UNIQUE,   -- Medical Record Number (de-identified demo data)
    full_name         VARCHAR(120) NOT NULL,
    date_of_birth     DATE         NOT NULL,
    primary_condition VARCHAR(160) NOT NULL,
    risk_level        VARCHAR(10)  NOT NULL DEFAULT 'medium'
                       CHECK (risk_level IN ('low', 'medium', 'high')),
    status            VARCHAR(20)  NOT NULL DEFAULT 'active'
                       CHECK (status IN ('active', 'discharged', 'transferred')),
    created_at        TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS care_plans (
    id          SERIAL PRIMARY KEY,
    patient_id  INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    title       VARCHAR(160) NOT NULL,
    goal        TEXT,
    status      VARCHAR(20) NOT NULL DEFAULT 'active'
                 CHECK (status IN ('draft', 'active', 'on_hold', 'completed')),
    start_date  DATE,
    target_date DATE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS tasks (
    id            SERIAL PRIMARY KEY,
    care_plan_id  INTEGER NOT NULL REFERENCES care_plans(id) ON DELETE CASCADE,
    title         VARCHAR(200) NOT NULL,
    description   TEXT,
    status        VARCHAR(20) NOT NULL DEFAULT 'todo'
                   CHECK (status IN ('todo', 'in_progress', 'blocked', 'done')),
    priority      VARCHAR(10) NOT NULL DEFAULT 'medium'
                   CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
    assignee_id   INTEGER REFERENCES care_team_members(id) ON DELETE SET NULL,
    due_date      DATE,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- HIPAA-style audit trail. Every API request that touches PHI is appended here by
-- application-tier middleware. Append-only by convention; no UPDATE/DELETE grants
-- would be issued in a real deployment.
CREATE TABLE IF NOT EXISTS audit_log (
    id           SERIAL PRIMARY KEY,
    occurred_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    actor        VARCHAR(160),         -- authenticated subject (or 'anonymous')
    action       VARCHAR(20)  NOT NULL,-- READ | WRITE
    method       VARCHAR(10)  NOT NULL,
    path         VARCHAR(300) NOT NULL,
    status_code  INTEGER      NOT NULL,
    client_ip    VARCHAR(64)
);

CREATE INDEX IF NOT EXISTS idx_care_plans_patient ON care_plans(patient_id);
CREATE INDEX IF NOT EXISTS idx_tasks_care_plan    ON tasks(care_plan_id);
CREATE INDEX IF NOT EXISTS idx_tasks_status       ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_audit_occurred_at  ON audit_log(occurred_at);
