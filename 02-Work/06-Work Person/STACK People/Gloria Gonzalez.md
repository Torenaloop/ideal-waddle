---
Company: STACK Infrastructure
Org: EHS
Location: Denver, CO
Job Title: Program Manager
Email: ggonzales@stackinfra.com
Phone: 765-631-0775
tags:
  - EHS
Reports to:
  - "[[Donna Lynch]]"
---
*NAME*

- [ ] Ask her to: When you do reach out, you can share this exact list of what you need created as org-level fields: 
---
Here's a draft — written to give Gloria enough context without over-explaining, and leaving a natural handoff point for you to paste the field spec:

---

# 2026-04-13 Asana Admin Request for creating Org/Workspace-Level Fields

**Subject:** Asana Admin Request — Org-Level Custom Fields for EHS Assessment Projects

Hi Gloria,

Hope you're doing well. I wanted to reach out with an admin request related to the EHS internal assessment projects I've been building out in Asana.

I'm currently developing a standardized assessment template (Pilot 4 - Crit Ops EHS Assessment) that I plan to duplicate across the 7 sites in my East Region portfolio. The goal is to use Asana's portfolio dashboard to roll up assessment progress, compliance status, and audit findings across all sites in one view — which is where I need your help.

To make the portfolio-level reporting work, the custom fields on these projects need to be created at the **org/workspace level** rather than at the project level. Project-level fields don't surface as grouping or filtering dimensions in portfolio dashboards, which limits our ability to see things like pass/fail rates or high-priority findings across all sites at once.

I have **6 custom fields** I'd like created at the workspace level. I've listed them below with the exact field names, types, and option values (including colors) so it should be a straightforward setup on your end:

_[Paste field spec list here]_

Once these are in place, I'll swap the current project-level fields in the template for the org-level versions, then duplicate the template into the site projects. Let me know if you have any questions or need me to walk through the use case — happy to jump on a quick call.

Thanks so much for your help on this.

David

---

A few notes: I used "Gloria Gonzalez" based on what you mentioned — double-check spelling against her Asana profile (the summary from our earlier session shows her listed as "Gloria Gonzales"). Also, if Gloria is actually a colleague rather than someone in an IT/ops admin role, you may want to soften the technical framing slightly. But as written, this should give her everything she needs to action it without back-and-forth.
---



1. **Status** — Single-select: Pass (green), Fail (red), NA (blue)
2. **Audit Type** — Single-select: Compliance (blue), Site (green)
3. **Priority** — Single-select: High (red), Medium (yellow), Low (green) — check if the existing org-level Priority field can be reused
4. **Verification Method** — Multi-select: Document Review (blue), Physical Inspection (green), Visual Verification (aqua), Employee Interview (purple)
5. **Frequency** — Single-select: Annual (red), Biannual Audit (orange), Quarterly (yellow), Monthly (yellow-green), Daily (green), Per Use (aqua), Ongoing (blue)
6. **Regulatory Reference** — Text field