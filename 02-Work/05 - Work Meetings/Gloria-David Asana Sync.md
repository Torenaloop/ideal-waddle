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
- [ ] "maybe it is a we create a rule that pulls anything labelled task a *corrective action* to another section" - #jesse-kenser 

## Follow-ups


## Agenda

# EHS Asana Dashboard — Remediation Runbook

Step-by-step. Written 2026-09-22 against verified live state.

**Read this first:** of the 16 remediation steps below, **5 are requests to Gloria** and **11 need no request from anyone**. The most common failure mode here is asking an admin for something you already have. Do not open the meeting until you've read "What not to ask for."

---

## What NOT to ask for

|Don't ask|Why|
|---|---|
|"Create a workspace Status field for EHS"|She already did, 14 Apr 2026. `Status (EHS)`, gid `1214066574917703`. It's been in the library unused for five months.|
|"Create portfolio-level fields for West Region like East has"|East has exactly one portfolio field (`Priority`, gid `1206586651881428`) and so does West. They are already identical, and it's unset on all 11 projects.|
|"Apply Status (EHS) to our projects"|Needs no admin rights. Done on POR03B in one API call.|
|"Fix the portfolio dashboard widgets"|Widget configuration is yours, not an admin function.|
|"Make the five other audit fields global"|They already are, and they already roll up correctly.|

---

# PART 1 — The five things to actually request

Do these in order. Steps R1–R2 are the substance; R3–R5 are the prevention.

### R1 — Six project-level custom fields

**Ask:**

> "I need six fields that attach to the _project_, not to tasks — so the portfolio can compare sites against each other. Task fields chart fine at portfolio level; what they can't do is describe a project. I can't group the portfolio by Region or chart conformance by site from data living on tasks."

|#|Field|Type|Options|
|---|---|---|---|
|1|Region|Single-select|East (blue), Central (green), West (orange), Canada (purple)|
|2|Audit Phase|Single-select|Not Scheduled (warm gray), Scheduled (blue), Fieldwork Complete (yellow-green), Draft Report (yellow), Report Issued (green), Closed (aqua)|
|3|Conformance %|Number|percentage, 0 decimals|
|4|Open Findings|Number|0 decimals|
|5|Critical & High Findings|Number|0 decimals|
|6|Lead Auditor|Single-select|Clinton Sharp, Dale Gross|

**⚠ The one thing that must not be skipped — get the final names back in writing.** This is precisely what failed in April. Say verbatim:

> "If any of these collide with another team's field name, append (EHS) like you did before — but please send me the **exact final field names** when you're done. Last time the rename to 'Status (EHS)' meant our projects were built against a field just called 'Status,' and Asana silently created local copies instead of binding to yours. I want to bind to the real thing this round."

**Done when:** you have her written confirmation of the six final names.

---

### R2 — Ask her to check for reusable existing fields

**Ask:**

> "Before you create Region — is there already one in the library that fits? I'd rather reuse than add a seventh name."

**Done when:** she confirms reuse-or-create for each of the six.

---

### R3 — Guardrail against shadow fields _(highest long-term value)_

**Ask:**

> "The Status problem wasn't a slow-admin problem, it was a guardrail problem. A project owner can create a project-local field whose name is close to a library field, and nothing warns anyone. We lost five months of portfolio reporting to that and only found it by auditing field GIDs. Is there a way to restrict field creation at project level, or at least surface a warning, so people get pushed toward the library instead of around it? With 51+ facilities coming, that's the difference between this happening once and every year."

**Done when:** you have a yes/no and, if no, a documented reason you can cite later.

---

### R4 — Resolve the naming collision at its source

**Ask:**

> "The '(EHS)' suffix you had to use is what caused the mismatch. Two options: can the other team's plain 'Status' be renamed, or can we agree a convention so library fields are unmistakable when someone's picking one?"

**Also worth asking:** who owns custom field gid `1211374033381430`? It's a second field also named "Status" that appears on 67 multi-homed tasks in NVA01A. Two fields named "Status" on one task is a live trap for anyone building a chart.

---

### R5 — Standing intake, so this isn't a meeting next year

**Ask:**

> "This is the second time I've queued behind your calendar for field creation, and 2027 will be a third. Is there a path to create library fields directly, or a lighter-weight route than a meeting each time?"

**Fallback if no:**

> "Can we agree a standing intake — I send the spec in your format, you execute when you get to it, no meeting required?"

---

# PART 2 — The eleven things needing no request

Grouped by dependency. Nothing here is blocked on Gloria.

## Phase A — Data layer (must come first)

**A1. Migrate the 11 legacy projects onto `Status (EHS)`.** Add the library field, map Pass→Met, Fail→Not Met, NA→N/A on the 100 scored criteria only; leave the 29 section markers blank. _Status: POR03B done and verified. 10 remaining._ **Verify:** re-read every task and diff old field vs new — require 0 mismatches.

**A2. Clear the milestone scores in the legacy field — POR01A and NVA01A.** POR01A has ≥27 section markers carrying a Status value (Pass Count reads 115 on a 100-criterion audit). NVA01A has 12. **Verify:** Status Distribution totals exactly 100 with no Task type filter.

**A3. Audit the other 9 projects for the same milestone-scoring error.** **Verify:** each project's scored count equals exactly 100.

**A4. Fill the two unrated fails.** POR02A (20 fails, 19 rated) and POR03A (7 fails, 6 rated) each have one Not Met with no Priority (EHS). Filter to `Status = Fail` AND `Priority (EHS) is empty`. **Verify:** Fail Count equals Fails by Priority total in every project.

## Phase B — Project dashboards (after A1 per project)

**B1. Re-point the six scoring widgets to `Status (EHS)`** and rename Pass/Fail language to Met / Not Met. UI only — not API-editable. **Verify (POR03B):** 83 / 7 / 100 / 100 / 10 / 7.

**B2. Remove the `Completion status = Incomplete` filter** from the four inventory widgets in all 11 projects. Keep `Task type = Task`. **Verify:** Items by Audit Type reads 100; Verification Method reads 125 (multi-enum, so a criterion with two methods counts twice).

**B3. Finish the two East Region projects left pending** — NVA05A and NVA06A/B still carry the original filters.

**B4. Remove the legacy project-local Status field** from each project once its widgets verify. Leaving it creates two fields named "Status" on every task — the exact trap in R4.

## Phase C — Portfolio dashboards (after Phase A completes region-wide)

**C1. Rebuild the three dead widgets** against `Status (EHS)`: Total Fails Across All Sites, Overall Status Distribution, Fails by Verification Method. **Verify:** West reads 39 total Not Met (5 + 20 + 7 + 7).

**C2. Fix `Assessment Completion by Site`** — it charts _incomplete_ counts while titled "Completion," so finished sites vanish and lagging sites show tallest. Re-point to completed counts or retitle "Open Items by Site."

**C3. Fix `Pass/Fail by Site`** — currently grouped by due-date status (Upcoming / Completed / Overdue / Unscheduled), not by Status.

**C4. Fix `Task completion over time`** — scoped to incomplete tasks, so "Completed" flatlines at zero.

## Phase D — Prevention (do before the next site generation)

**D1. Verify the master templates bind to library fields**, not local copies — Phase 1 `1216986911312532`, Phase 2 `1216989475774362`. Phase 2 already uses the global Status (EHS); confirm Phase 1 and confirm neither carries the Completion-status widget filters.

**D2. Populate the project fields** from R1 across all 21 sites once created — and bind by selecting from the library, never by typing a name.

---

# PART 3 — Sequencing

```
R1 ─────────────────────────────► D2   (can't populate fields that don't exist)
R3, R4, R5  (independent — no downstream dependency)

A1 ──► B1 ──► B4
A2, A3, A4 ──► C1   (portfolio numbers are wrong until task data is clean)
A1 (all 11) ──► C1 ──► C2, C3, C4
D1  (independent — do before next generation, not after)
```

**The only true blocker on Gloria is D2.** Everything in Phases A, B and C can proceed today regardless of how the meeting goes.

---

# PART 4 — Verification checklist

Run top to bottom. Any row that fails means the step above it isn't finished.

|#|Check|Expected|
|---|---|---|
|1|Every project's Status (EHS) scored count|exactly 100|
|2|Every project's section markers on Status (EHS)|29 blank|
|3|Old field vs new field diff, per project|0 mismatches|
|4|Fail Count vs Fails by Priority, per project|equal|
|5|Items by Audit Type, per project|100|
|6|Total tasks by Verification Method, per project|125|
|7|Only one field named "Status" visible on any task|true|
|8|West portfolio — Total Not Met Across All Sites|39|
|9|West portfolio — Overall Status Distribution|renders, totals 400|
|10|Portfolio "Completion" chart|finished sites show tallest, not absent|

---

## Reference

- `Status (EHS)` — gid `1214066574917703` — Met `1214066834482721` / Not Met `1214066834482722` / N/A `1214066834482723` / Partially Met `1218692204071109`
- Per-project GIDs and migration status: `status-ehs-migration-log.md`
- Defect detail: `west-region-dashboard-triage.md`, `east-region-dashboard-corrections.md`

# DRAFT 2 - Gloria Gonzales — Meeting Prep, Wed 23 Sep 2026, 11:00

Revised 2026-09-22 after verifying the April field history and the live portfolio configuration. Changes from the prior version are marked **[REVISED]**.

Two items here are things you **tell** her, not ask her. Do both before the ask.

## Agenda — 30 minutes

|#|Item|Time|Purpose|
|---|---|---|---|
|1|Where the program stands|3 min|Context; shows her April work paid off|
|2|Heads-up: two changes to library fields|4 min|Disclosure, not approval|
|3|Heads-up: her Status field was never applied **[NEW]**|3 min|Disclosure + sets up item 5|
|4|The ask — 6 portfolio-level fields|9 min|Main request|
|5|Governance — the guardrail ask **[REVISED]**|8 min|Highest leverage item on this page|
|6|Timeline and next steps|3 min|Close with dates|

## 1. Where it stands — your opener

> "Quick context before the ask. Since you set up those six fields in April, we've built the whole 2026 audit program on top of them — 21 site projects, one per facility, 301 criteria each, all rolled into a portfolio called 2026 H&S Audit. DFW01A and DFW01B are scored and closed out; the other 19 are shells waiting on ISS fieldwork. The fields you created are what makes that consistent across all 21."

Roughly 6,300 tasks carrying her field schema. Worth her knowing.

## 2. Disclosure — two library fields changed

Asana warned both times that the change reached beyond your projects.

- **Status (EHS)** — options renamed Pass → Met, Fail → Not Met, NA → N/A, and **Partially Met** added. Asana flagged **4 projects and portfolios**. No data lost; every existing value carried to the renamed option.
- **Priority (EHS)** — **Critical** added alongside High/Medium/Low. Asana flagged **37 projects and portfolios**. Purely additive; nothing existing changed.

> "Two things I changed that I want you to hear from me. I renamed the options on Status (EHS) to match the Met / Partially Met / Not Met / N/A language our executive report template uses, and I added Critical to Priority (EHS) because the ISS checklists score severity on a Critical-to-Low scale. Asana warned that Status touches 4 projects and Priority touches 37. No values were lost in either case. If another team was relying on the Pass/Fail wording, tell me and I'll split ours into a separate field instead."

Say it plainly and move on. The offer to split is genuine — make it and mean it.

**If she pushes back:** fallback is a new EHS-only conformance field, and we bulk-set 602 task values across DFW01A/B to repopulate. Annoying, not hard. Don't defend the change; offer the remedy.

**Useful fact if she asks who the 4 are** _(verified 2026-09-22)_: the 11 legacy East/West Region assessment projects do **not** use Status (EHS) at all — they carry their own project-local Status fields. So the rename's blast radius is genuinely small and confined to the new Phase 2 generation.

## 3. Disclosure — her Status field was never applied **[NEW]**

This is new information as of yesterday, and it reframes item 5. Deliver it as fact, not apology.

Her 14 April reply says:

> "I just made all the fields available in STACK Infra library. I had to add (EHS) to a 'Status' and 'Priority' because they were already in use by another team."

She created `Status (EHS)` (gid `1214066574917703`) as asked. But the East and West Region site projects, built 20–21 April, were configured with a field named plain **"Status"** — so Asana created a fresh project-local field on each project instead of binding to hers. Five of six fields wired to the library correctly. Status did not, because the name she was required to use didn't match the name being typed.

Consequence: every portfolio-level chart that depends on Status reads zero or blank in **both** regions, and has since April. Her field sat unused in the library for five months.

> "One more thing you should hear from me. That Status field you created in April — it never actually got attached to the site projects. They were built with a field just called 'Status,' so Asana spun up a separate project-local copy on each one instead of using yours. Five of your six fields wired up correctly. That one didn't, purely because of the naming. It's why our portfolio rollup has been reading zero since April. I'm fixing it now — no action needed from you."

**Do not turn this into an ask.** Applying an existing library field needs no admin rights; it was done on one project yesterday in a single API call. This item exists to be honest and to give item 5 its evidence.

## 4. The ask — six portfolio-level fields

**[REVISED] — corrected rationale.** The previous framing ("task-level fields don't surface as portfolio grouping or charting dimensions") is not accurate and she may know it: the West portfolio has a working chart, _Total incomplete tasks by Audit Type_, built on her task-level Audit Type field. Global task fields do chart at portfolio level. Use the narrower, correct argument:

> "The fields you made are task-level — they live on each of the 301 criteria, and they do chart at portfolio level; that part works. What they can't do is describe the _project_. I can't group the portfolio list by Region, or chart conformance by site, from data that lives on tasks. That needs fields that attach to the project itself. Same wall as April, one level up."

Then the list:

1. **Region** — Single-select: East (blue), Central (green), West (orange), Canada (purple)
2. **Audit Phase** — Single-select: Not Scheduled (warm gray), Scheduled (blue), Fieldwork Complete (yellow-green), Draft Report (yellow), Report Issued (green), Closed (aqua)
3. **Conformance %** — Number, percentage format, 0 decimals
4. **Open Findings** — Number, 0 decimals
5. **Critical & High Findings** — Number, 0 decimals
6. **Lead Auditor** — Single-select: Clinton Sharp, Dale Gross

Volunteer three things without being asked — they make you easy to say yes to:

- **Name collisions** — "If any of these hit another team's field name, append (EHS) like you did with Status and Priority. That worked well." _(Given item 3, add: "and tell me the exact final name so I bind to yours rather than creating a duplicate.")_
- **What you left out** — "I skipped a Site Code field since project names carry the code, and skipped audit dates since built-in project start/due dates handle it. Six fields, not nine."
- **[NEW] Conformance % is a maintained snapshot** — "Worth flagging: Conformance % is a number I keep current by hand. Once the task-level Status rolls up properly, the portfolio will also be able to compute conformance from the criteria directly, and the two could disagree. I'm treating the project field as the reporting headline and task data as source of truth. Saying it now so it isn't a surprise later."

## 5. Governance — the guardrail ask **[REVISED — highest leverage item]**

Previously framed as "give me standing permission to create fields." Item 3 gives you a stronger and more specific case. Lead with the guardrail; keep standing permission as the second ask.

**Ask A — prevent shadow fields.**

> "The Status problem wasn't a slow-admin problem, it was a guardrail problem. A project owner can create a project-local field with a name close to a library field, and nothing warns anyone. We lost five months of portfolio reporting to that and only caught it by auditing field GIDs. Is there a way to restrict field creation at the project level, or at least surface a warning, so people are pushed toward the library instead of around it? With 51+ facilities coming, that's the difference between this happening once and happening every year."

**Ask B — the naming convention.**

> "Related — the '(EHS)' suffix you had to use is exactly what caused the mismatch. Can the other team's plain 'Status' be renamed, or can we agree a convention so library fields are unmistakable at the point someone picks one?"

**Ask C — template governance.**

> "Before the next site generation, can we confirm the Phase 1 and Phase 2 master templates are bound to library fields rather than local copies? If they aren't, every new facility inherits the same trap."

**Ask D — standing intake (the original item 4).**

> "Bigger picture — this is the second time I've queued behind your calendar for field creation, and 2027 will be a third. Is there a path to create library fields directly, or a lighter-weight route than a meeting each time? Happy to work inside whatever naming convention or review step you want."

If no: **"Can we agree a standing intake — I send the spec in your format, you execute when you get to it, no meeting required?"** That removes most of the friction.

## 6. Timeline — close here

> "ISS fieldwork starts with the POR trip, and Clint mentioned trip one may slide to November. I'd like the fields in place before the first report lands so sites get populated as results come in rather than in a batch at the end. Does end of next week work on your side?"

Confirm the loop: she builds, you populate all 21, you send her the portfolio link so she can see it working. She did exactly that for you in April with the "Testing Task Distribution" project — returning the favor lands well.

## Likely questions, with answers ready

**"Why can't you just do this yourself?"** **[REVISED]**

> "Library field creation sits with admins, and the tooling I have can apply existing library fields but not create new ones. Everything downstream of the field existing, I can do."

_(The prior answer — "the Asana API doesn't expose field creation at all" — is overstated; Asana's public API does have a custom-field creation endpoint. Don't say it. The version above is true and she can't contradict it.)_

**"Will this clutter the library for everyone else?"**

> "Portfolio fields only appear where they're added. These six only show up on the 2026 H&S Audit portfolio unless someone deliberately adds them elsewhere."

**"Who keeps the values current?"**

> "I do. Conformance %, Open Findings, and Critical & High get updated as each site's report is issued — roughly 21 updates over the audit cycle, not an ongoing burden."

**"Can we reuse anything that already exists?"**

> "Please check — Region especially. If there's an existing Region field that fits, I'd rather use it than add a seventh name to the library."

**[NEW] "Didn't I already build you a Status field?"**

> "You did, and it was right. It just never got attached to the projects — they were built with a locally-named 'Status' instead. That's on our build side, not yours. I'm migrating the eleven legacy projects onto your field this week."

## Facts verified 2026-09-22 (in case she probes)

- `Status (EHS)` gid `1214066574917703`, workspace-global, options Met / Not Met / N/A / Partially Met.
- The five other April fields are workspace-global and roll up correctly today: Audit Type `1214066834559481`, Priority (EHS) `1214066597036565`, Verification Method `1214066812683081`, Regulatory Reference `1214066597522707`, Frequency `1214066834915854`.
- Both East and West portfolios carry exactly one custom field setting — `Priority` gid `1206586651881428` — and it is unset on all 11 projects.
- Each of the 11 legacy projects carries its own private Status field with a distinct GID. Full list in `status-ehs-migration-log.md`.

# DRAFT 1  

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