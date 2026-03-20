---
para: Projects
project: 2025 Environmental Audit
sub_project: Power BI Dashboard Development
status: Active
priority: High
date: 2025-02-27
date_range: 2025-02-20 to 2025-02-27
email_thread: true
thread_participants:
  - David Nuckolls (STACK)
  - Maya Anichini (Antea Group)
  - Clorece Hammitt (Antea Group)
  - Becky Matich (Antea Group)
  - Jesse Kenser (STACK)
  - Donna Lynch (STACK)
related_files:
  - "[[2025 Environmental Audit Project Hub]]"
  - "[[ENV AUDIT - Re Dashboard Discussion (Clorece Response)]]"
  - "[[ENV AUDIT - Fw Dashboard Discussion (David Forward)]]"
tags:
  - env-audit
  - 2025-audit-cycle
  - power-bi
  - dashboard-dev
  - data-quality
  - spreadsheet-controls
  - technical-coordination
  - antea-group
stakeholders:
  - Maya Anichini (Antea - Project Manager)
  - Clorece Hammitt (Antea - Business Analytics Lead)
  - David Nuckolls (STACK - Ops EHS Manager)
  - Jesse Kenser (STACK - Project Owner)
---

# ENV AUDIT - Dashboard Discussion Email Thread

|   |   |
|---|---|
|**Subject**|**[EXTERNAL] STACK - Env. Audit Dashboard Discussion**|
|**From**|**Maya Anichini** (Antea Group)|
|**To**|**David Nuckolls, Clorece Hammitt**|
|**Date**|**February 24-27, 2025**|
|**Meeting Date**|**Monday, February 24, 2025 11:30 AM-12:00 PM**|

## Thread Summary
Technical coordination meeting and follow-up regarding Power BI dashboard requirements for the 2025 Environmental Audit cycle. Focus on ensuring data consistency, spreadsheet controls, and seamless transition from 2022-2023 audit data to current cycle.

---

## Meeting Purpose (Feb 24, 2025)

**Original Invitation from Maya Anichini:**
> Setting this time aside for us to discuss the Env. Audit Dashboard to ensure data can easily be populated from this year's audits.

**Microsoft Teams Meeting**
- Meeting ID: 258 828 543 707
- Passcode: TW6sC2Cx

---

## Meeting Notes & Key Decisions

### Primary Question
**Is there anything different this time around compared to the 2022-2023 Operations Environmental Audit?**

### Questions Addressed

#### 1. New or Dropped Questions
- **New questions**: Yes → Maya to forward previous protocol/questionnaire and proposed protocol to David and Clorece
- **Dropped questions**: TBD → Reference files needed

#### 2. Dashboard Aesthetics
- **Changes from 2022-2023**: David to pose this question to Donna Lynch
- **Reference file**: `Jan 2023 Env Assessment Dashboard.pbix`

#### 3. Power BI Risks to Control
- **Lock down spreadsheets** (STACK - David responsible)
- **Socialize to rest of STACK Ops EHS**: No going rogue manipulating spreadsheets/tables. Must be consistent and uniform, otherwise Dashboard will have issues
- **Static location/file path** as source of information for dashboard

### Dashboard Technical Requirements

**Data File Reference**: `STACK Audit Power BI Data File.xlsm`

**Spreadsheet Control Rules**:
- ✅ **OKAY**: Adding rows
- ❌ **AVOID**: 
  - Renaming columns
  - Adding or removing columns
  - Anything that can be a picklist should be a picklist
  - Must use same naming convention for column headers
  - Must establish consistent date format

**Historical Context**:
- "2022-2023 Operations Environmental Data" = last audit data baseline
- Safety audit conducted in late 2023 (separate initiative)

---

## Action Items & Assignments

### David Nuckolls
- [ ] Lock down spreadsheets as much as possible
- [ ] Socialize spreadsheet/dashboard guidelines to all STACK Ops EHS team members
- [ ] Schedule sync with Clorece to cross-reference protocols and ensure spreadsheet consistency
- [ ] Review attached audit findings template to confirm it matches 2022/2023 format
- [ ] Confirm grey columns (requested by Donna/Jesse) will be filled by STACK team
- [ ] Ask Donna about dashboard aesthetics/visual changes from 2022-2023
- [ ] Reach out to Clorece/Maya for touchpoint to review spreadsheet modifications
- [ ] Request protocol/questionnaire documents in accessible format (Word or Excel)

**David's Question (Feb 26)**:
> Do we have the list of questions/things that will be evaluated? The legacy dashboard and spreadsheet consolidate/code the findings in such a way that it is not super intuitive to reverse engineer the items to be evaluated wholistically.

### Clorece Hammitt (Antea Group)
- [ ] Will keep team within scope
- [ ] Alert team to any asks that are out of scope requiring additional budget
- [ ] Review spreadsheet/questions for compatibility with Power BI dashboard

### Maya Anichini (Antea Group)
- [ ] Forward previous protocol/questionnaire and proposed protocol to David and Clorece
- [ ] Provide audit findings template for review
- [ ] Clarify: audit question wording should NOT affect dashboard (dashboard shows findings only)

### Becky Matich (Antea Group)
- [ ] Provide questionnaire and document request to Operations team
- [ ] Available for questions on protocol/audit topics

**Becky's Response (Feb 26)**:
Provided questionnaire and document request. Recommended Ops teams focus on **topics** (air, waste, etc.) rather than specific questions, since auditor questions vary by site based on permits and local regulations.

---

## Key Technical Points

### Dashboard Data Flow
1. **Audit questions** (vary by site) → 
2. **Findings** (captured in standardized spreadsheet) → 
3. **Power BI Dashboard** (visualizes findings)

**Critical Understanding**: 
- The audit questions can be customized per site
- The findings spreadsheet format MUST remain consistent
- Dashboard reads from findings, not from raw questions

### Data Quality Controls
- **Picklists**: Essential for categorical data (prevents free-text inconsistency)
- **Naming conventions**: Must be identical to 2022-2023 structure
- **Date formats**: Must be standardized across all entries
- **Column structure**: Cannot change without breaking dashboard
- **File paths**: Must remain static for automated refresh

### Scope Management
- Antea Group (Clorece) monitors for scope creep
- Changes to dashboard requirements may trigger budget discussions
- Core deliverable: Same dashboard as 2022-2023, populated with 2025 data

---

## References & Attachments

**Power BI Files**:
- `Jan 2023 Env Assessment Dashboard.pbix` (previous dashboard for visual reference)
- `STACK Audit Power BI Data File.xlsm` (data source template)

**Documents**:
- Pre-audit questionnaire (to be shared by Maya)
- Document request spreadsheet (to be shared by Maya)
- Previous protocol vs. proposed protocol comparison

---

## Timeline Notes

**David Nuckolls OOO**: February 24, 2025 - March 7, 2025
**Becky Matich PTO**: March 6 - 16

---

## Cross-References
- See [[ENV AUDIT - Re Dashboard Discussion (Clorece Response)]] for Clorece's technical clarification
- See [[ENV AUDIT - Fw Dashboard Discussion (David Forward)]] for David's internal forward
- See [[2025 Environmental Audit Project Hub]] for overall project coordination
- See [[Doc Request Questionnaire]] for site preparation checklist
- Related to [[Jesse Kenser Hub]] - project owner
- Related to [[David Nuckolls Hub]] - technical lead
- Related to [[Bridge Construction-Ops EHS Gap]] - strategic alignment

---

## Meeting Participants

**STACK Infrastructure**:
- David Nuckolls - Operations Environmental, Health, and Safety Manager
- Jesse Kenser - Project Owner (CC)
- Donna Lynch - EHS Leadership (CC, delegated to Jesse)

**Antea Group**:
- Maya Anichini, M.S., CSP - Senior Project Manager
- Clorece Hammitt - Project Manager | Business Analytics Lead
- Becky Matich - Senior Project Manager
- Clay Mareschal - (CC)

---

## Contact Information

**Antea Group Lead**:
Maya Anichini, M.S., CSP
Senior Project Manager | USA
Cell: +1 607 201 3920
Email: maya.anichini@anteagroup.us

**STACK Lead**:
David Nuckolls
Operations Environmental, Health, and Safety Manager
STACK Americas
Email: dnuckolls@stackinfra.com
Mobile: 405-863-1218
