# Scenario tests

Each scenario replaces the live connectors with fixed data. Use `config/profile.example.md` as the profile (user "Alex") and `config/settings.example.md` as the settings, unless the scenario says otherwise. Calendar events are listed per calendar. Planner calendar = `alex@example.com`. Anchors: Gym, Run. Deadline prefix `Due · `.

Produce exactly the message you would send the user in that situation, nothing else. Do not call any real tools.

---

## S1 · Morning brief, long stretch without a meal

Now: Mon 2026-11-02 07:00. Mode: morning brief. Delivery: Gmail send returns success.
Profile override: lunch is empty for all days.

Classes: Econ 101 09:30–11:00 (Hall 210) · Statistics 11:15–13:30 (Hall 105) · Seminar 13:45–15:30 (Room 12)
alex@example.com: Gym 16:00–17:00 (recurring)
No deadline events.

## S2 · Weekend, add a deadline that needs splitting

Now: Sat 2026-11-07 10:00. Mode: user message in chat.
User: "I have an essay due Monday 9am, probably about 4 hours."
Classes: nothing Sat/Sun. alex@example.com: Run Sun 10:00–10:45 (recurring). No other events.
Assume any calendar write you decide to make succeeds.

## S3 · Weekday cap already reached

Now: Tue 2026-11-03 07:00 (brief already sent). Mode: user message in chat.
User: "quiz tomorrow, need about 1 hour to review"
Classes Tue: none. Tue free gaps after routine total 6h (assume this is correct).
alex@example.com Tue: "Report · Draft" 09:00–11:00, "Report · Revise" 13:00–15:00 (both work blocks, 4h total). Wed: Classes 09:00–17:00 (one block, "Lab day").
Deadline events: "Due · Report" Thu.

## S4 · Morning brief reminder line

Now: Wed 2026-11-04 07:00. Mode: morning brief. Delivery: Gmail send returns success.
Classes Wed: Econ 101 09:30–11:00 (Hall 210).
alex@example.com Wed: "Lab report · Analysis" 14:00–15:30.
Deadline events (all-day, free):
- "Due · Lab report" on Fri 11/6
- "Due · Reading response" on Thu 11/5
- "Due · Final project" on Mon 11/9
No work blocks exist for Reading response or Final project.

## S5 · Only split windows fit, one overlaps an anchor

Now: Thu 2026-11-05 08:00. Mode: user message in chat.
User: "problem set due Friday 5pm, about 90 minutes"
Assume the only free gaps before the deadline (after routine) are:
- Thu 13:00–14:15 (home)
- Thu 17:00–18:30 (home)  ← Run anchor 17:30–18:15 sits inside this gap on alex@example.com
- Fri 08:00–09:15 (home)
Nothing else is free before Fri 17:00.

## S6 · Morning brief, email fails

Now: Thu 2026-11-05 07:00. Mode: morning brief.
Classes Thu: Lab section 14:00–15:30 is NOT on any calendar this week (the profile lists it as a fixed recurring item on Fri only). Econ 101 is cancelled; the Classes calendar has no events today.
alex@example.com: no events. No deadlines.
Delivery: Gmail send returns error "401 Unauthorized".

## S7 · A different kind of user (generality)

Use THIS profile and settings instead of the example files:

Profile: language en · timezone America/New_York · email sam@example.com · brief 10:30 · delivery [session] · prefix `Due · ` · fixed_calendars [Work] · planner_calendar sam@example.com · anchors [Climbing] · wake 10:00 · sleep 01:00 is NOT supported, so Sam uses sleep 23:45 · meals: lunch all 13:30–14:15, dinner all 20:00–20:45 · no commute (works from home) · Extra rules: "Never schedule anything before 11:00." · Not managed: none.
Settings: defaults, except weekend_days [tue, wed] and chart_start/chart_end auto.

Now: Tue 2026-11-03 10:30. Mode: morning brief. Delivery: session only.
Work: no events (Tuesday is Sam's day off). sam@example.com: Climbing 16:00–18:00 (recurring).
Deadline events: "Due · Portfolio update" on Thu 11/5, no work block.
Then the user replies in the same session: "portfolio update, about 3 hours". Produce that reply too.
