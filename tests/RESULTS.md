# Test results · 2026-10-30

Executor: a fresh agent that sees only the rules and the fixture, no other context.

## Backtest (3 real past days, rules v1 vs. the briefs the old personal system actually sent)

| Day | Structure (rows, fixed events, anchors, work blocks, leave time, reminder) | Window differences | Cause |
|---|---|---|---|
| Sun | match | 1 evening window vs 2 | config had no dinner time (old system inferred one) |
| Mon | match | morning window 15 min longer; evening window differs | config missed a "get ready" buffer; a block was moved after that morning |
| Tue | match | evening window larger | a block that existed that morning was later deleted |

No difference traced to the rules' core logic. Differences were config gaps (fixed) or calendar edits made after the brief was sent.

## Scenarios (tests/scenarios.md)

| | Tests | v1 | After fixes |
|---|---|---|---|
| S1 | long busy stretch → ⚠ no meal | pass, but rule fired on normal days too | pass (flags 08:45–17:00 only) |
| S2 | weekend + task that needs splitting | pass (format for split tasks undefined → added) | — |
| S3 | daily cap already reached | partial: starred over-cap windows | rule added: label `over <day>'s cap`, no ★ if avoidable |
| S4 | reminder line only for the right deadline | pass, but false ⚠ no meal | pass, no false flag |
| S5 | only split windows fit; one overlaps an anchor | pass | — |
| S6 | email fails; cancelled class; backstop item on another day | pass (honest failure line) | — |

## Rule gaps found and fixed (commit 5a479da)

1. Scheduled run without config would start setup unattended → now prints one line and stops
2. Timed events marked "free" (e.g. auto-added from email) were ambiguous → timed events are always busy
3. Backstop item vs. a cancellation note → cancellation wins, row marked `(changed)`
4. "Round to 5 minutes" clashed with durations like `6h24` → clock times rounded, durations exact
5. Commute home undefined → starts after the day's last event away from home
6. Over-cap candidates could get ★ → labelled, not starred when avoidable
7. Half-hour cells with mixed occupancy, overlapping events → tie-break defined
8. ⚠ no meal fired on every normal day → redefined as a long busy stretch
9. Reminder window, "related block", multiple reminders → defined
10. Split-task candidate format → defined

## Known limits of this round
- One-shot runs only; a multi-day recurring run is not yet observed
- A brand-new user's GitHub/Google authorization path is untested
- Setup and deadline-intake flows were tested on fixtures, not live calendars

## Round 2 · 2026-10-30

- **S7 (generality)**: a remote worker with no commute, days off Tue/Wed and a 10:00 wake-up time was handled by config alone: the chart ran 10–23, the Tue cap was 1/3 and the "nothing before 11:00" extra rule held. Four rules were clarified: session-only status line, updating an existing deadline event, starring when every option is over the cap, and single vs. paired windows. Sleep after midnight stays out of scope for v1.
- **Chinese version backtest (Mon)**: wording matches the original personal system. The morning window `08:15–09:15 1h` is identical to the brief actually sent that day, and the no-meal span is close to it. The evening window differs because of a later calendar edit.
- **Fixed**: "related block" matched by exact name prefix gave false reminders (e.g. `Speech · 写稿` for `Public Speaking Speech`). It now matches any block that clearly names the task.
