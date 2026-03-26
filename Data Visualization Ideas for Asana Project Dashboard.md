





> [!NOTE] Original Question
> Can you help me with ideas on creating meaningful data visualizations in the following project in Asana? I've included a screen shot of a list view of the tasks/deliverables grouped by category and further subdivided into "compliance" - things we can check on remotely, versus "site" - those items we have to check on in-person. Also, I included a screen shot of the default dashboard widgets for said project.


Looking at your screenshots, you've got a really solid data structure to work with — the combination of EHS category sections, Compliance/Site sub-grouping, Priority, Verification Method, Regulatory Reference, Frequency, and Status gives you a lot of meaningful slices. Here's how I'd think about building out the dashboard beyond the defaults:

---

## Audit Progress & Completion

These are the most critical during an active audit cycle.

**Completion % by Section (bar chart)** — As you mark tasks complete, a chart showing % done per EHS category (Documentation, Electrical, Emergency Preparedness, etc.) immediately tells you where you're ahead and where you're lagging. This is more actionable than raw task counts.

**Compliance vs. Site completion rate (two number widgets or a grouped bar)** — Since Site items require in-person visits, tracking those separately from remote-checkable Compliance items lets you plan site visit scheduling. If Site items are consistently behind, it's a scheduling signal, not a workload signal.

**Status breakdown (pie/donut: Not Started / In Progress / Complete / N/A)** — A simple status snapshot across all 101 criteria. Most useful as a header-level health check.

---

## Priority & Risk Focus

**Incomplete High-priority tasks (number widget with filter)** — A simple count of High-priority items still at "Not Started" or overdue. This is your executive-level risk indicator. You can pair it with a task list widget filtered to High + incomplete so the number is actionable, not just informational.

**Priority distribution by section (stacked bar)** — Shows which categories carry the most High-priority criteria. Useful for site visit prioritization — if Emergency Preparedness has 6 Highs and Hot Work has 1, you know where to focus first.

---

## Verification Method Planning

**Task count by Verification Method (bar or donut)** — Document Review, Physical Inspection, Visual Verification, Employee Interview each require different logistics. Knowing you have, say, 30 Document Reviews and 40 Physical Inspections shapes how you structure the audit day.

**Incomplete tasks by Verification Method** — Same as above but filtered to incomplete only. As the audit progresses, this becomes a to-do planner by _type of work_ rather than just by topic.

---

## Regulatory Coverage

**Tasks by Regulatory Reference (bar chart)** — Showing how many criteria tie to 29 CFR 1910.38 vs. STACK EHS Policy vs. other citations gives you a compliance framework view. Useful for reporting to leadership or legal.

---

## Frequency / Scheduling View

**Biannual vs. Annual vs. Ongoing breakdown** — Less useful during an active audit, but very useful post-audit for planning cadence. A number widget showing how many Ongoing items exist is a good persistent reminder that some criteria never fully "close."

---

## What Asana's Dashboard Can Actually Support

A few practical notes on what's buildable natively:

- **Number widgets** work great for filtered counts (High + Incomplete, Site + Not Started, etc.)
- **Bar charts** can be grouped by any single-select custom field — so Priority, Audit Type, Verification Method, Frequency all work
- **Donut/pie** is available for single-select fields — your Compliance/Site split is already there
- **Task list widgets** filtered by specific criteria act as live action lists
- The **completion over time** chart becomes genuinely useful once you start checking things off — right now it's flat because nothing is complete yet

The gap in Asana's native dashboard is **cross-field charts** (e.g., Priority × Section as a stacked bar). For that kind of analysis you'd need to export to Excel or build something in Power BI — which given your existing dashboard work would be a natural fit for a post-audit review view.

---

Want me to help you think through the specific widget configurations (filters, groupings) for any of these, or sketch out what a well-structured dashboard layout might look like?