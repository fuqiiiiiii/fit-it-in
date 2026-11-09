# Profile (example)

> Template. Setup copies this to `config/profile.md` and fills in your values.
> Everything below is a fictional example. Edit `profile.md` freely, or just tell Claude in plain words.

## Basics

```yaml
language: en                     # en | zh
timezone: America/Los_Angeles
email: alex@example.com          # where the email copy of the brief goes
brief_time: "07:00"
delivery: [email, session]       # or [session]
deadline_prefix: "Due · "        # title prefix of deadline events on the planner calendar
```

## Calendars

```yaml
fixed_calendars:                 # read only
  - Classes
  - Work shifts
planner_calendar: alex@example.com   # the one calendar Claude writes to
anchors:                         # recurring habits on the planner calendar; they take time but are never tracked
  - Gym
  - Run
```

## Routine

Leave a field empty if you don't want Claude to plan around it. Empty is never treated as free time made up by Claude; it simply isn't subtracted.

```yaml
wake: "06:30"
sleep: "22:30"
meals:
  breakfast: { mon-fri: "07:30-08:00", sat-sun: "09:00-09:30" }
  lunch:     { all: "12:00-12:45" }
  dinner:    { all: "19:00-19:45" }
commute:
  minutes: 25                    # one way
  leave:   { mon: "08:45", wed: "08:45", fri: "09:15" }
  # days not listed = no commute
```

## Fixed recurring items (backstop)

Things that happen every week but may be missing from your calendars. Claude adds them to the picture if a calendar doesn't show them.

| Day | What | Time | Where |
|---|---|---|---|
| Fri | Lab section | 14:00–15:30 | Science 210 |

## Extra rules (plain words)

One line each. Use this for anything the fields above can't express.

- On gym days (Mon, Thu), lunch moves to right after the gym.
- Never schedule work after 21:30 on Sundays.

## Not managed

Things this planner should never schedule or mention.

- Errands and chores (I use a separate reminders app)
- Social media posting
