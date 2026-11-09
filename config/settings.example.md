# Settings (example)

> Template. Setup copies this to `config/settings.md` unchanged.
> These defaults come from six weeks of daily use by the author. Change them in plain words ("no buffer", "cap weekdays at half"), or edit the file.

```yaml
weekday_cap: 0.667      # plan at most 2/3 of the day's free gaps; the rest stays white space on purpose
weekend_cap: 0.333      # weekend days: at most 1/3
weekend_days: [sat, sun]   # your days off, e.g. [tue, wed]
buffer: 1.6             # your estimates × 1.6, because things usually take ~60% longer than we expect
min_gap: 45             # minutes; shorter gaps are ignored
split_threshold: 180    # minutes; longer tasks are split into 2–4 steps
reminder_days: 3        # brief mentions a deadline this close that has no block yet
no_meal_hours: 4        # flag stretches this long without a meal
chart_start: auto       # first hour drawn; auto = your wake hour
chart_end: auto         # last hour drawn; auto = your sleep hour
show_hints: true        # one-line usage hint at the bottom of the brief
```
