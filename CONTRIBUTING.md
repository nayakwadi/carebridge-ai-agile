# Contributing to CareBridge

CareBridge is a 3-tier (React/TypeScript · FastAPI/Python · PostgreSQL) AI-assisted patient care-coordination platform, orchestrated with Docker Compose.

## Local development

Pick the path that matches what you're changing.

### Full stack (recommended)

Brings up the frontend, backend, PostgreSQL, and Redis together with one command:

```bash
docker compose up --build
```

Copy `.env.example` to `.env` first if you haven't already.

### Backend only

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
ruff check app tests
```

`pytest` must pass and `ruff check` must be clean before you open a PR.

### Frontend only

```bash
cd frontend
npm install
npm run dev          # local dev server with hot reload
npm run typecheck    # must pass before you open a PR
```

## Branching model

We use **short-lived feature branches off `main`**. Branch, make a focused change, open a PR, merge, and delete the branch. Keep branches small and rebased on the latest `main` to avoid drift — long-running branches are discouraged.

Suggested naming: `feat/<short-slug>`, `fix/<short-slug>`, `docs/<short-slug>`.

## Commit messages

We follow [Conventional Commits](https://www.conventionalcommits.org/). Use a type prefix and an imperative summary:

```
feat(api): add care-plan status transitions
fix(frontend): correct Kanban column drop target
docs(agile-ai): add backlog-prioritization artifact
test(backend): cover audit-log middleware READ/WRITE paths
chore(ci): bump ruff version
```

Common types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`.

## Pull request process

1. Branch off `main`, make your change, and ensure the relevant checks above pass.
2. Open a PR and fill out the [PR template](.github/pull_request_template.md).
3. Keep PRs small and single-purpose — easier to review, safer to revert.
4. A PR merges once it meets the Definition of Done and has a passing review.

## Definition of Done

A change is **done** only when all of the following are true:

- **Code** — implemented, follows existing style, and is scoped to the change.
- **Tests** — new behavior is covered; `pytest` (backend) and `npm run typecheck` (frontend) pass.
- **Docs** — user-facing or architectural changes are documented (e.g. under `docs/`).
- **Audit-safe** — because CareBridge handles PHI, any change touching data access preserves the HIPAA-style audit trail (READ/WRITE logging) and introduces no new way to read PHI without a logged trail.

## Filing issues

Use the templates under [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE):

- **User stories / feature requests** — [user-story template](.github/ISSUE_TEMPLATE/user_story.md)
- **Bugs** — [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)

Choosing the right template keeps the backlog refinable and triage fast.
