




# Handoff: Excel EHS Audit → Asana Project Migration

## Context

## I'm David, Operations EHS Manager at STACK Infrastructure. I manage Environmental, Health & Safety programs across 51+ data center facilities. I've been migrating Excel-based audit assessments into Asana projects using a CSV-import workflow that Claude helped me develop through several iterations. This document captures everything you need to replicate the approach for a new audit. Also, the key elements will be (1) the following folder and its files: G:\My Drive\EHS\2023 Health and Safety Audit Spreadsheets (2) My Asana account

## What We're Doing

## Taking an EHS audit that currently lives in Excel spreadsheets (a template + site-specific copies) and producing a **clean CSV** optimized for Asana's AI-powered CSV importer, so that when uploaded it creates a well-structured Asana project with sections, custom fields, task descriptions, and no duplication issues. The output CSV is not the final product — **Asana's native AI importer is the final product**. The CSV is engineered to give that AI importer the best possible input so it generates a rich, usable project.

## Proven Workflow (Step by Step)

### Step 1: Examine the Excel Files

I'll upload two files:

- A **template** spreadsheet (the master audit criteria, usually blank for scoring)
- A **site-specific** copy (same criteria, pre-filled with site name and year) Read both files completely using pandas and openpyxl. Map out:
- All columns and what they contain
- How many audit items (rows)
- What categories/groupings exist
- What fields are for auditor input vs. fixed criteria
- Any columns that are internal/administrative (e.g., "Keep?", "Reworded?") that should NOT carry into Asana

### Step 2: Build the CSV — Structure Rules

The CSV must follow these rules exactly (learned through trial and error): **DO:**

- Produce exactly **one row per audit item** — no more, no fewer than the source spreadsheet
- Include a `Section` column with the category name (e.g., "Confined Space", "Electrical Safety") — Asana can use this to auto-create sections or the user can group by it after import
- Fill **every cell** in every row — no blanks. Every column must have a value for every task
- Use `csv.QUOTE_MINIMAL` when writing (not `QUOTE_ALL`)
- Verify zero duplicate task names before saving **DO NOT:**
- Do NOT insert "section header" rows (rows where the Name ends with `:` and other fields are blank). This was tried in v1 and caused Asana to create duplicate columns on the X-axis and duplicate tasks on the Y-axis. The blank cells in those rows caused the importer to interpret multiple conflicting schemas
- Do NOT use `QUOTE_ALL` — excessive quoting can confuse the importer
- Do NOT include internal/administrative columns from the Excel (like "Keep?", "Reworded?", or "Denominator" as a standalone column — fold the reference number into the task name instead)

### Step 3: Column Design

These are the columns that worked well, in order:

|Column|What Goes In It|Asana Mapping|
|---|---|---|
|**Name**|`[ref#] Action-oriented task name`|→ Task Name|
|**Section**|Category name from the audit (e.g., "Emergency Preparedness")|→ Section grouping|
|**Description**|Rich multi-line text with original criteria, audit type context, regulatory references, verification guidance, and scoring rubric|→ Task Description|
|**Audit Type**|"Compliance" or "Site" (or whatever the audit's type taxonomy is)|→ Custom Field (Dropdown)|
|**Priority**|"High" / "Medium" / "Low" — assigned by regulatory severity|→ Custom Field (Dropdown)|
|**Verification Method**|"Document Review" / "Physical Inspection" / "Employee Interview" / "Visual Verification" (can be combined with `/`)|→ Custom Field (Text or Dropdown)|
|**Regulatory Reference**|OSHA CFR citations, NFPA, ANSI, EPA, ASHRAE, etc. (combined with `/`)|→ Custom Field (Text)|
|**Frequency**|"Annual" / "Semi-Annual" / "Quarterly" / "Monthly" / "Per Use" / "Ongoing" / "Biannual Audit" — extracted from criteria text|→ Custom Field (Dropdown)|
|**Status**|Pre-set to "Not Started" for every row|→ Custom Field (Dropdown)|

### Step 4: Enrichment Logic

The value-add of this process is transforming flat audit questions into Asana-ready task data. Here's what to generate: **Task Names:** Convert question-format criteria ("Are there records of...?") into action-oriented names ("Verify records of..."). Prefix with the reference/denominator number in brackets: `[3.2] Verify periodic LOTO program audit performed at least annually`. Strip trailing question marks and "Note:" addendums. **Priority Assignment:** Map based on regulatory severity:

- **High:** OSHA-critical items — LOTO, confined space, electrical/arc flash, emergency response, fall protection, SPCC, Legionella, respiratory, hot work, scaffolding, MEWP, first aid/AED, stop work authority, ERP
- **Medium:** Training, inspections, documentation, permits, JHAs, SDS, PPE, hazmat, fire extinguishers, drills, noise
- **Low:** Everything else (signage, recycling, general housekeeping, water availability) **Regulatory References:** Map criteria and categories to specific standards (29 CFR citations, NFPA, ANSI, ASHRAE, EPA rules). When no specific standard applies, use the company policy reference (e.g., "STACK EHS Policy"). **Verification Method:** Derive from audit type + criteria keywords:
- "Site" audit type → Physical Inspection
- Keywords like "record", "document", "file", "plan", "SharePoint" → Document Review
- Keywords like "trained", "demonstrate", "knowledge" → Employee Interview
- Keywords like "posted", "labeled", "marked", "sign" → Visual Verification
- Can combine multiple methods with `/` **Frequency:** Extract from criteria text — look for "annually", "semi-annual", "quarterly", "monthly", "daily", "before each use", "regular/routine". Default to the audit cycle name (e.g., "Biannual Audit") when no frequency is stated. **Description:** Build a structured multi-line description for each task:

```
AUDIT CRITERIA: [original question verbatim]
Audit Type: [type] ([Document/Record Review or Physical Site Inspection])
Reference #: [denominator]
Regulatory Basis: [mapped references]
VERIFICATION GUIDANCE:
- [3 context-appropriate bullet points based on audit type]
SCORING: Pass / Fail / N/A
```

### Step 5: Validate Before Delivering

- Confirm row count matches the source spreadsheet exactly
- Assert zero duplicate task names
- Verify no blank cells anywhere
- Spot-check a few task names for natural readability
- Print priority distribution and frequency distribution as a sanity check

---

## Asana Import Instructions (for me, post-CSV)

1. Create a fresh Asana project (or use an existing one — but know that imports ADD to existing projects, they don't replace)
2. Before importing: create the custom fields as Dropdown fields in the project (Priority, Audit Type, Status, Frequency, Verification Method) — the importer can then map CSV columns to them. Text fields work for Regulatory Reference
3. Import the CSV → map columns during the import wizard
4. After import: Group by the Section column to organize tasks into category sections

---

## What I'll Provide for the Next Audit

- The Excel template file (master audit criteria)
- A site-specific copy if available
- Any context about what the audit covers, what the categories mean, and what the scoring approach is
- Whether the Asana project will be standalone or part of a portfolio

---

## Key Lesson from Previous Iterations

**The single most important rule:** Every row must be a complete, fully-populated task row. No structural tricks like blank "section divider" rows. The Asana AI importer handles a clean, flat, uniform CSV extremely well — but it breaks badly when rows have inconsistent column populations. The enrichment and structure should be IN the cell values, not in the row layout.