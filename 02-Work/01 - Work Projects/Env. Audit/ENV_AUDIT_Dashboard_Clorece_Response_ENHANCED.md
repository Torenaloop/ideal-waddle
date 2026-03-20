---
para: Projects
project: 2025 Environmental Audit
sub_project: Power BI Dashboard Development
status: Active
priority: High
date: 2025-02-27
email_thread: true
thread_position: Response to David's follow-up
from: Clorece Hammitt (Antea Group)
to: David Nuckolls (STACK)
related_files:
  - "[[2025 Environmental Audit Project Hub]]"
  - "[[ENV AUDIT - Dashboard Discussion]]"
  - "[[ENV AUDIT - Fw Dashboard Discussion (David Forward)]]"
tags:
  - env-audit
  - 2025-audit-cycle
  - power-bi
  - data-quality
  - technical-clarification
  - spreadsheet-controls
  - picklists
stakeholders:
  - Clorece Hammitt (Antea - Business Analytics)
  - David Nuckolls (STACK - Ops EHS Manager)
  - Maya Anichini (Antea - Project Manager)
---

# ENV AUDIT - Clorece's Technical Clarification on Dashboard Requirements

|   |   |
|---|---|
|**Subject**|**Re: [EXTERNAL] STACK - Env. Audit Dashboard Discussion**|
|**From**|**Clorece Hammitt** (Antea Group)|
|**To**|**David Nuckolls** (STACK)|
|**Date**|**Thursday, February 27, 2025 10:22 AM**|
|**In Response To**|David's follow-up question (Feb 27, 7:28 AM)|

---

## Clorece's Response

> Hello!
> 
> Yes, so sorry for the delay here, but I wanted to check in with our project team at Antea yesterday for some clarification. All of these questions and items in the audits are going to be translated into spreadsheet(s) with the findings (I believe Maya has sent the empty version), and that does look to follow the same format used previously. **The topics/subtopics/questions doesn't matter, just more that the final spreadsheet used for compiling the findings is the same.** And I further impressed the need for **picklists wherever possible** on the file so they can get those implemented.
> 
> Hopefully this helps!

---

## Key Technical Clarifications

### Critical Understanding ✅
**What matters for Power BI**:
- ✅ **Final findings spreadsheet format** must remain identical to 2022-2023
- ✅ **Picklists** must be implemented wherever possible
- ✅ **Column structure** must not change

**What doesn't affect Power BI**:
- ❌ Topics, subtopics, or question wording (these can vary)
- ❌ How questions are phrased to site personnel
- ❌ Site-specific customizations in audit protocols

### Data Architecture

```
Audit Questions (Variable) 
    ↓
Findings (Standardized Format)
    ↓
Spreadsheet (Fixed Structure with Picklists)
    ↓
Power BI Dashboard (Automated Visualization)
```

---

## Picklist Implementation

### Purpose
- Ensures data consistency across all sites
- Prevents free-text entry variations
- Enables accurate dashboard filtering and aggregation
- Reduces data cleaning requirements

### Implementation Requirements
Clorece "impressed the need" for picklists to Antea project team, indicating this is a **high-priority data quality control**.

### Likely Picklist Fields (based on typical audit structure)
- Finding severity (e.g., Critical, Major, Minor, Observation)
- Finding status (e.g., Open, In Progress, Closed)
- Regulatory category (e.g., Air, Waste, Water, Stormwater)
- Site/Facility ID codes
- Responsible party
- Compliance status

---

## Context: David's Original Question

**David asked (Feb 26)**:
> Do we have the list of questions/things that will be evaluated? The legacy dashboard and spreadsheet consolidate/code the findings in such a way that it is not super intuitive to reverse engineer the items to be evaluated wholistically.

**David followed up (Feb 27)**:
> Hey Clorece - regarding Maya's question of the spreadsheet/questions being fundamentally sound for ease of transition into Power BI, I wanted to ask you if you've had a chance to take a look and provide comment?

---

## Clorece's Resolution

### What She Validated
1. ✅ Consulted with Antea project team for clarification
2. ✅ Confirmed spreadsheet format matches previous cycle
3. ✅ Verified Maya sent the "empty version" (template)
4. ✅ Emphasized picklist implementation to project team

### What She Clarified
- **Format consistency** is the critical factor, not question content
- **Picklists** are essential for data quality
- **Dashboard compatibility** is preserved by maintaining spreadsheet structure

---

## Action Items Resolved
- [x] Clorece reviewed spreadsheet format for Power BI compatibility
- [x] Clorece confirmed with Antea project team
- [x] Clorece communicated picklist requirements to project team

## Outstanding Action Items
- [ ] Antea project team implements picklists in findings template
- [ ] David reviews empty findings template sent by Maya
- [ ] David confirms grey columns will be populated by STACK team

---

## Technical Notes

### Why This Matters
This email provides crucial **separation of concerns**:
- **Audit protocol** (questions) = flexible, site-specific
- **Findings capture** (spreadsheet) = rigid, standardized, must not change

This allows:
- Auditors to customize questions per site regulations
- STACK to maintain consistent reporting
- Power BI to function without modification
- Historical comparison to 2022-2023 baseline

### Data Quality Strategy
By insisting on picklists, Clorece is preventing:
- Typos and variations in text entry
- Inconsistent categorization
- Manual data cleaning requirements
- Dashboard filter failures
- Reporting inaccuracies

---

## Cross-References
- See [[ENV AUDIT - Dashboard Discussion]] for full meeting context
- See [[ENV AUDIT - Fw Dashboard Discussion (David Forward)]] for David's internal communication
- See [[2025 Environmental Audit Project Hub]] for overall project
- Related to [[David Nuckolls Hub]] - technical implementation lead
- Related to [[Bridge Construction-Ops EHS Gap]] - strategic initiative

---

## Contact Information

**Clorece Hammitt**
Project Manager | Business Analytics Lead
Antea®Group | St. Paul, MN
Office: +1 651 639 9449
Direct: +1 218 565 2790
Email: clorece.hammitt@anteagroup.us

**David Nuckolls**
Operations Environmental, Health, and Safety Manager
STACK Americas
Email: dnuckolls@stackinfra.com
Mobile: 405-863-1218
