# fit-it-in

**Finds where your work fits in a packed calendar. You pick, it books.**

Every morning, Claude reads your calendars (classes, meetings, gym) and draws your day, with the open windows labelled A, B, C. Say *"essay due Friday, ~2h"* and it suggests where it fits. Reply *"B"*. Nothing lands on your calendar until you do.

<!-- demo GIF coming soon: morning chart → "essay due Fri, ~2h" → ★ candidates → reply "A" → block appears in Google Calendar -->

Auto-schedulers decide for you. This one only suggests. It never reshuffles your day on its own, and it never keeps a list of what you didn't do.

**~240 lines of plain-English rules · no app code · Claude + Google Calendar · English & [中文](README.zh.md)**
Used by its author almost every morning since Sept 16, 2026 · 20+ deadlines planned.

---

## Is this for you?

- You've set up Notion / Todoist / a bullet journal and quit within a month
- Your week changes all the time: classes, shifts, meetings
- You live in Google Calendar and already use Claude

## Install (about 5 minutes)

You need: a GitHub account, a Claude plan that includes Claude Code and scheduled tasks, and Google Calendar (Gmail optional, for the email copy).

1. Click **Use this template** → create a **private** repository. That repository is your planner: your settings live there.
2. In Claude, connect **GitHub** and **Google Calendar**, then start a Claude Code session on your new repository.
3. Say anything, e.g. *"hi"* or *"I have an essay due Friday"*. Setup starts by itself.

Setup reads your calendar first, so it asks you one question (*what time should your plan arrive?*) and one optional one (meals and commute). It shows you a preview of today, then creates the daily task for you.

## What your morning looks like

```
Wed 9/16

06 ░░ Wake
07 ░░ Breakfast
08 ░░
09 ░░ Leave 9:15
10 ░▓ Intro to Economics · Hall 210
11 ▓░
12 ░░ Lunch
13 ░░
14 ▓░ Advisor call
15 ░█ Essay · Polish + submit
16 ██
17 █░
18 ░█ Run
19 ░░ Dinner
20 ░░
21 ░░
22 ░░ Sleep 22:30

 ▓ fixed  █ on your planner  ░ free

Lab report due Fri, nothing on your calendar for it yet

Open windows
 A 13:00–14:00  home    ██ 1h
 B 17:30–18:30  home    ██ 1h
 C 19:45–22:15  home    █████ 2h30
```

One row per hour, two cells per row (each = 30 min). Arrives in the app and, if you want, by email.

## Adding a deadline

```
You:     stats problem set due Friday, about 2 hours
Claude:  Stats problem set · due Fri · plan 3h12 (2h + 60% buffer)

         ★A Wed 13:00–16:30  home    ███████ 3h30  fits in one go
          B Wed 19:00–21:00  home    ████    2h    pair with E
         ★C Thu 13:45–16:00  campus  ████    2h15  pair with E
          E Fri 08:00–09:15  home    ██      1h15  finishing only

         A is the only window that fits it in one go. If you'd rather keep Wed light, C+E.
         Reply with letters, e.g. "A" or "C E"
You:     A
Claude:  Added to your planner. If it doesn't suit, drag it in Google Calendar.
```

## Just talk to it

| Say | It does |
|---|---|
| "lab report due Mon, ~2h" | Offers windows; books only after you pick |
| "essay done" | Clears the deadline |
| "move the essay to Thursday" | Offers new windows |
| "I leave at 7 on Tue/Thu now" | Updates your routine |
| "send my plan at 8" / "pause" | Changes or pauses the daily brief |

## Not for you if…

- You want streaks, completion rates or a backlog. This deliberately has none of them.
- You work night shifts or sleep after midnight (not supported yet)
- You switch time zones often (one time zone only)
- You use Outlook or Apple Calendar (Google Calendar only for now)

## FAQ

**Why is there no to-do list?** Every unfinished item on a list is a small debt. Debt piles up and the list becomes something you avoid opening. Here, deadlines live as all-day notes on your calendar, and each day is planned fresh.

**Why does it only fill 2/3 of my free time?** The rest is white space on purpose. Plans that use 100% of the day break at the first surprise. Weekends get 1/3.

**Why did my 2h become 3h12?** Things usually take ~60% longer than we guess. Say "no buffer" if you disagree.

**Where is my data?** In your own private repository and your own Google account. There is no server.

**Can I change the rules?** Yes. Your settings are in `config/`, and you can change them in plain words. The behavior itself is in [`AGENTS.md`](AGENTS.md). It's plain English, and you can edit it.

## How it was built and tested

- [The story](docs/story.md): five versions, four of which died within two weeks, and what that taught me about building vs. buying
- [Test results](tests/RESULTS.md): rules replayed against real past days, plus 7 scenarios

MIT License
