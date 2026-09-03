# Household Chores

A mobile, phone-first app that **fairly assigns** shared household chores using **effort-weighted balancing**, so no single person carries more of the load than anyone else.

## How it works

- A **household admin** sets up the chore list and assigns each chore an **effort score** (points reflecting difficulty/time).
- The tool **auto-assigns** chores to balance each person's **total effort over a monthly window** — if someone is light one week, they pick up more later in the month to even out.
- Assignees mark a chore done with a **self-report tap** (trust-based, no verification). Completing it earns the chore's effort points.
- A chore that isn't done **rolls over to the same person**, carrying its effort debt into the next period until completed.

## v1 features

1. **Effort-weighted auto-assignment** — chores split by point value, not just count.
2. **Monthly fairness balancing** — effort evened out over a rolling monthly window.
3. **Admin-defined chores & scores** — one person owns the list and effort values.
4. **Tap-to-complete with roll-over** — self-report done; unfinished chores carry forward.

## Out of scope for v1

Reminders / push notifications, rewards or gamification, completion verification or disputes, preference-based assignment, group voting on scores, and a fairness dashboard.

## Documentation

See [`_docs/plan.md`](_docs/plan.md) for the full plan and scope.
