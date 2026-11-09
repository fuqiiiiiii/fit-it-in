# Why fit-it-in exists

## Four planners, four funerals

In August 2026 I built a personal planning system with Claude: Apple Calendar and Reminders as the hub, a morning plan at 9:00, a weekly review every Sunday night, and a dashboard folder.

It died in under two weeks. So did versions 2, 3 and 4. Each one was better designed than the last, and each one stopped the same way: one missed day, then another, then I stopped opening it.

In mid-September I stopped redesigning and asked a different question: **what did all four have in common when they died?**

1. **They kept score.** Done, missed, carried over, streaks. After a few bad days, opening the planner meant facing a list of my failures. So I didn't open it.
2. **Restarting cost too much.** One trip was enough to break the routine, and getting back in meant rebuilding state first.
3. **Nobody was waiting.** Everything that *did* get done had an outside commitment behind it: a client, a team, a class deadline. The planner itself had none.

## The design that came out of it

Each rule is the opposite of one cause of death:

| Cause of death | Rule |
|---|---|
| Keeping score | **Record only what was done, never what wasn't.** No backlog, no streaks, no overdue marks. Nothing to feel behind on. |
| Expensive restarts | **Every day starts fresh.** The only things that persist are deadlines and a one-line status. Miss a week and the next brief is as clean as the first. |
| Nobody waiting | **Deadlines are the input.** The system only plans things that have a real due date, the one kind of thing that already gets done. |
| (Learned later) Over-planning | **Fill at most 2/3 of free time.** Estimates × 1.6. The rest stays white space, unnamed and unquestioned. |
| (Learned later) Losing control | **It suggests, you pick.** Nothing goes on the calendar without a reply. |

Version 5 went live on Sept 14. On Sept 15 it went silent: the scheduled task ran on my laptop, and the laptop was asleep. On Sept 16 I moved it to the cloud. It has run almost every morning since.

## Build vs. buy

Before building, I checked what already existed (prices as listed in Sept 2026):

- **Guided planners** (you plan, the app helps): Sunsama ~$20/mo, Akiflow ~$15/mo
- **Auto-schedulers** (the app plans for you): Motion ~$19/mo, Reclaim ~$8/mo, Morgen ~$30/mo (~$15 billed yearly)
- **Open source**: nothing mature that does a morning conversation plus scheduling into gaps. The largest project I found, Super Productivity, doesn't auto-schedule.

The auto-schedulers were the closest fit, and also the clearest mismatch. Motion's own docs say that if a task doesn't fit your normal hours, it will schedule it *outside* them to meet the deadline. That's exactly the white space I was trying to protect.

So I built it. The interesting part is what "building" meant:

**There is no app code.** The whole product is a ~240-line plain-English rules file ([`AGENTS.md`](../AGENTS.md)). Claude reads it every morning, along with your calendar, and follows it. Google Calendar is the database. A scheduled task is the server.

That's the real shift AI brings to build vs. buy. I built it by talking to Claude, not by opening a code editor. **What's left is maintenance, and the maintenance is the rules themselves.** Within weeks my rules file grew from 88 lines to over 200, one bug fix at a time. Every rule fixed one case and made the whole file a bit harder to reason about. So the file now has a budget: add a rule only after something actually went wrong, rewrite before adding, and cut anything that never fired once it passes 250 lines.

If you're building AI products, that's the part worth stealing: **when the product is a prompt, the hard problem moves from writing code to keeping the rules small.**

## How it was tested

Before publishing, I replayed the rules against three real past days and compared the result with the brief I had actually received each morning. I also ran seven made-up scenarios aimed at the rules most likely to break. Each run used a fresh agent that could see only the rules. Fifteen gaps came up and were fixed. Details: [`tests/RESULTS.md`](../tests/RESULTS.md).

## Honest limits

- One real user so far: me
- Google Calendar only; one time zone; no sleep after midnight
- Needs a GitHub account and a Claude plan with Claude Code and scheduled tasks. That's a real barrier for non-technical people.
