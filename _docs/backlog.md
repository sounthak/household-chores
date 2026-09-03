# Household Chores — Backlog

_Derived from [plan.md](plan.md). Each task is small enough to finish in one
sitting. Tasks are grouped by build phase and ordered so each one builds on the
last._

---

## Phase 1 — Foundations

| # | Task | Notes |
|---|------|-------|
| 1 | Define `Household` model (name, created date) | One household per group of roommates/family. |
| 2 | Define `Member` model (FK to Household, FK to User, `is_admin` flag) | Links Django auth users to a household; admin flag gates chore management. |
| 3 | Define `Chore` model (FK to Household, name, effort score, recurrence) | Effort score is a positive integer representing difficulty/time. |
| 4 | Define `Assignment` model (FK to Chore, FK to Member, assigned date, completed date, `is_done` bool) | Tracks who owes what and whether it's finished. |
| 5 | Register all models in Django admin | Quick way to create test data before any UI exists. |
| 6 | Add seed data management command (`python manage.py seed`) | Pre-populates a household, members, and chores for local development. |

## Phase 2 — Assignment engine

| # | Task | Notes |
|---|------|-------|
| 7 | Write `get_effort_totals(household, window_days=30)` utility | Returns each member's completed-effort sum over the rolling monthly window. |
| 8 | Write `assign_chores(household)` service function | Distributes unassigned chores to the member with the lowest effort total, repeating until all chores are assigned. |
| 9 | Handle roll-over logic — carry incomplete assignments into the next period | If `is_done` is False when a new cycle starts, the assignment stays with the same member and its effort debt persists. |
| 10 | Add unit tests for the assignment engine | Cover: even split, uneven effort scores, roll-over of undone chores, single-member household edge case. |

## Phase 3 — API & views

| # | Task | Notes |
|---|------|-------|
| 11 | Install Django REST Framework, add to `INSTALLED_APPS` | Foundation for a JSON API the mobile frontend will consume. |
| 12 | `POST /api/households/` — create a household (creator becomes admin) | Returns household id and invite info. |
| 13 | `GET /api/chores/` — list chores assigned to the current member | Filtered by household; shows effort score and done status. |
| 14 | `POST /api/chores/` — admin creates a chore with name & effort score | Validates that requester is household admin. |
| 15 | `PATCH /api/assignments/{id}/complete/` — tap-to-complete | Sets `is_done=True` and `completed_date=now`. Only the assigned member can mark it. |
| 16 | `POST /api/assignments/generate/` — trigger auto-assignment | Calls `assign_chores()` and returns the new assignment list. Admin-only. |

## Phase 4 — Polish

| # | Task | Notes |
|---|------|-------|
| 17 | `GET /api/members/effort-summary/` — per-member effort totals | Returns each member's name and rolling-30-day effort for a simple balance view. |
| 18 | `GET /api/assignments/history/` — completed chore history | Paginated list of past assignments, newest first. |
| 19 | Add request authentication (token or session) | Lock all endpoints to authenticated household members. |
| 20 | Write a minimal smoke-test script or Postman collection | Exercises the full flow: create household → add chores → generate assignments → complete a chore → check effort summary. |
