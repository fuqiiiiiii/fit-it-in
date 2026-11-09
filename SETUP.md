# Daily Planner · Setup (first run)

Read together with `AGENTS.md`; section numbers like §5 refer to that file.

Goal: the user answers as little as possible. **Infer first, ask only what you can't infer.**

1. **Check the environment.** You must be running in a session that has this repository as its working folder, with the Google Calendar connector available. If the calendar connector is missing, tell the user exactly which connector to connect and stop. If the repository isn't the working folder, tell the user to start the session from their repository, then stop: the scheduled task created later only sees the folder if it's created from a session that has it.
2. **Read before asking.** List the user's calendars and the next 7 days of events. Infer: time zone; which calendars look fixed (classes, work, shared); which one is their own primary calendar; recurring habits that look like anchors; their email address.
3. **Show what you found, then ask exactly one required question**:
   ```
   Here's what I found:
   · Time zone: <tz>
   · Fixed schedule (I'll only read these): <calendars>
   · I'll put work blocks and deadlines in: <primary calendar>
     (Want a separate calendar instead? Create one called "Planner" in Google Calendar and tell me.)

   One thing I need: what time should your daily plan arrive each morning?
   ```
4. **One optional question**: "Optional, skip if you like: when do you usually eat lunch and dinner, and do you commute?" Skipped → leave those fields empty; never invent a routine.
5. **Preview.** Draw today's brief (§5) from their real calendar. Ask "Look right?" Put corrections into the profile: structured fields where they fit, otherwise one line in the profile's **Extra rules** section.
6. **Write config.** Copy `config/profile.example.md` → `config/profile.md` and `config/settings.example.md` → `config/settings.md`, fill in the values, commit `config: initial setup`, push. If the push fails, stop and say so.
7. **Create the daily scheduled task** from this session:
   - Name `Daily Planner brief`; runs in the cloud, needs no computer
   - Schedule: `CRON_TZ=<their time zone> <minute> <hour> * * *` at their chosen time, so daylight saving is handled automatically. If the scheduler moves the minute, tell the user the exact time
   - Prompt (copy exactly, filling in the language):
     > Daily Planner morning run. Read AGENTS.md in this repository and follow it in **Morning brief** mode (§5). Afterwards the user may reply in this session; handle replies with §6–§9. Language: <language>.
   - Turn push notifications on, email notifications off (the brief sends its own email)
   - Report which approval setting the task got. If its runs will ask for approval, tell the user they can switch it to automatic approval in the task's settings
8. **Close the loop.** One message: when and where the first brief arrives, plus three things they can say ("lab report due Fri", "essay done", "send my plan at 8"). Then go back to what they originally asked, if anything.

Never ask about the capacity caps, buffer, or minimum gap during setup. Defaults apply; the user changes them later in plain words.
