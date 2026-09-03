# Household Chores — Project Plan

_Last updated: 2026-09-03_

## Core purpose

A mobile, phone-first app that **fairly assigns** shared household chores using
**effort-weighted balancing**, so that no single person carries more of the load
than anyone else.

## How it works

- A **household admin** sets up the full chore list and assigns each chore an
  **effort score** (points reflecting difficulty/time).
- The tool **auto-assigns** chores to balance each person's **total effort over a
  monthly window** — if someone is light one week, they pick up more later in the
  month to even out.
- Assignees mark a chore done with a **self-report tap** (trust-based, no
  verification step). Completing it earns the chore's effort points.
- A chore that isn't done **rolls over to the same person**, carrying its effort
  debt into the next period until completed.

## Platform

Mobile app, phone-first.

## v1 features (the scope we settled on)

1. **Effort-weighted auto-assignment** — chores are distributed by point value, not
   just count, so the split reflects real effort.
2. **Monthly fairness balancing** — effort is evened out over a rolling monthly
   window rather than reset weekly.
3. **Admin-defined chores & scores** — one person owns the chore list and effort
   values, keeping scoring consistent.
4. **Tap-to-complete with roll-over** — self-report completion; unfinished chores
   stay with the assignee and carry their effort debt forward.

## Deliberately out of v1

Reminders / push notifications, rewards or gamification, completion verification or
disputes, preference-based assignment, group voting on scores, and a fairness
dashboard.

## Still undecided

- Household size and how members join (invite code vs shared login).
- Whether one-off chores exist alongside recurring ones.

## Rough build phases

1. **Foundations** — data model (households, members, chores, effort scores,
   assignments, completions), auth, and household membership.
2. **Assignment engine** — effort-weighted distribution logic with the monthly
   balancing window and roll-over handling.
3. **Core mobile UI** — admin chore setup, per-person chore list, tap-to-complete.
4. **Polish** — running effort balance per member, basic history/visibility.
