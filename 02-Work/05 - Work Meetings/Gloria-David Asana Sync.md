---
type: meeting
status: active
created: 2026-09-22
updated: 2026-09-22
meeting_date: 2026-09-23
participants:
  - Gloria Gonzalez
project:
  - Asana Implementation
tags:
  - Work/Goal/2026
---
# Gloria-David Asana Sync

## Agenda

## Notes

## Decisions

## Action Items
- [ ] 

## Follow-ups

Here's your prep. One thing to flag up front: two items on this agenda are things you should tell her rather than ask her — I changed two library fields she owns, and she shouldn't find out by stumbling on them.

## Agenda — 30 minutes

|#|Item|Time|Purpose|
|---|---|---|---|
|1|Where the program stands|3 min|Context; shows her April work paid off|
|2|Heads-up: two changes to library fields|4 min|Disclosure, not approval|
|3|The ask — 6 portfolio-level fields|12 min|Main event|
|4|Standing permission going forward|5 min|Removes the bottleneck permanently|
|5|Timeline and next steps|5 min|Close with dates|

## 1. Where it stands — your opener

> "Quick context before the ask. Since you set up those six fields in April, we've built the whole 2026 audit program on top of them — 21 site projects, one per facility, 301 criteria each, all rolled into a portfolio called 2026 H&S Audit. DFW01A and DFW01B are scored and closed out; the other 19 are shells waiting on ISS fieldwork. The fields you created are what makes that consistent across all 21."

That's roughly 6,300 tasks carrying her field schema. Worth her knowing.

## 2. The disclosure — do this before the ask

Two library fields she created now look different, and Asana warned both times that the change reached beyond my projects:

- **Status (EHS)** — renamed the options Pass → Met, Fail → Not Met, NA → N/A, and added **Partially Met**. Asana flagged it as impacting **4 projects and portfolios**. No data was lost; every existing value carried across to the renamed option automatically.
- **Priority (EHS)** — added **Critical** alongside High/Medium/Low. Asana flagged **37 projects and portfolios**. This one is purely additive — nothing that existed changed.

> "Two things I changed that I want you to hear from me. I renamed the options on Status (EHS) to match the Met / Partially Met / Not Met / N/A language our executive report template uses, and I added Critical to Priority (EHS) because the ISS checklists score severity on a Critical-to-Low scale. Asana warned that Status touches 4 projects and Priority touches 37. No values were lost in either case. If another team was relying on the Pass/Fail wording, tell me and I'll split ours into a separate field instead."

Say it plainly and move on. The offer to split it is genuine — make it, and mean it.

**If she pushes back:** the fallback is a new EHS-only conformance field, and we bulk-set 602 task values across DFW01A/B to repopulate it. Annoying but not hard. Don't defend the change; just offer the remedy.

## 3. The ask — six portfolio-level fields

Frame the _why_ before the list, because it's the part that isn't obvious:

> "The fields you made are task-level — they live on each of the 301 criteria. What I need now is a different animal: fields that attach to the project itself, so the portfolio dashboard can compare sites against each other. Task-level fields don't surface as portfolio grouping or charting dimensions. Same wall we hit in April, one level up."

Then the list:

1. **Region** — Single-select: East (blue), Central (green), West (orange), Canada (purple)
2. **Audit Phase** — Single-select: Not Scheduled (warm gray), Scheduled (blue), Fieldwork Complete (yellow-green), Draft Report (yellow), Report Issued (green), Closed (aqua)
3. **Conformance %** — Number, percentage format, 0 decimals
4. **Open Findings** — Number, 0 decimals
5. **Critical & High Findings** — Number, 0 decimals
6. **Lead Auditor** — Single-select: Clinton Sharp, Dale Gross

Two things to volunteer without being asked, because they make you easy to say yes to:

- **Name collisions** — "If any of these hit another team's field name, append (EHS) like you did with Status and Priority. That worked well."
- **What you left out** — "I deliberately skipped a Site Code field since the project names carry the code, and skipped audit dates since the built-in project start/due dates handle it. Six fields, not nine."

## 4. The highest-leverage ask — don't skip this

This is the one that's easy to forget and worth more than the six fields:

> "Bigger picture — this is the second time I've had to queue up behind your calendar for field creation, and 2027 will be a third. Is there a way to grant me the ability to create fields in the library directly, or a lighter-weight path than a meeting each time? I'm happy to work inside whatever naming convention or review step you want."

If the answer is no, the fallback ask: **"Can we agree on a standing intake — I send the spec in your format, you execute when you get to it, no meeting required?"** That still removes most of the friction.

## 5. Timeline — close here

> "ISS fieldwork starts with the POR trip, and Clint mentioned trip one may slide to November. I'd like the fields in place before the first report lands so sites get populated as results come in rather than in a batch at the end. Does end of next week work on your side?"

Then confirm the loop: she builds, you populate all 21, you send her the portfolio link so she can see it working — she did exactly that for you in April with the "Testing Task Distribution" project, and returning the favor lands well.

## Likely questions, with answers ready

**"Why can't you just do this yourself?"**

> "Field library creation sits with admins — and separately, the Asana API doesn't expose field creation at all, so even automation can't route around it. Everything downstream of the field existing, I can do."

**"Will this clutter the library for everyone else?"**

> "Portfolio fields only appear where they're added. These six only show up on the 2026 H&S Audit portfolio unless someone deliberately adds them elsewhere."

**"Who keeps the values current?"**

> "I do. Conformance %, Open Findings, and Critical & High get updated as each site's report is issued — roughly 21 updates over the audit cycle, not an ongoing burden."

**"Can we reuse anything that already exists?"**

> "Please check — Region especially. If there's an existing Region field that fits, I'd rather use it than add a seventh name to the library."

---

Want me to put this in a doc you can pull up on your phone during the call?