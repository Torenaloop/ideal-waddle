# Work Notes Enhancement Guide - NVA05A Project

## Files Enhanced in This Batch

### 1. Meeting Notes
**File:** `1770241714441_CANCELLED-D2D_Safety-Ops_Sync_Up_-_7-19-2024.md`
- **PARA:** Archive (cancelled meeting)
- **Status:** Cancelled
- **Project:** NVA05A
- **Key Tags:** #work #meeting #safety #operations #cancelled

### 2. Email Thread
**File:** `1770241714443_RE_NVA05A_Emergency_Evacuation_Maps.md`
- **PARA:** Project (active deliverable)
- **Status:** Complete
- **Project:** NVA05A
- **Key Tags:** #work #email #safety #emergency-planning #evacuation-maps

### 3. Quick Links Reference
**File:** `1770241714443_06_07_24_Activity.md`
- **PARA:** Resource (reference links)
- **Status:** Active
- **Project:** NVA05A
- **Key Tags:** #work #quick-links #D2D-checklist #resources

---

## New Work-Related Properties Added

### Meeting Notes Properties
```yaml
Meeting Time: 09:00-09:30
Meeting Type: Teams Meeting
Attendees: [list of people]
Topic: [meeting subject]
```

### Email Properties
```yaml
Date Received: YYYY-MM-DD
Date Original: YYYY-MM-DD (if forwarded/replied)
From: [sender name]
To: [recipients list]
Cc: [cc recipients]
Attachments: [list of files]
Subject: [email subject]
```

### Reference Links Properties
```yaml
Type: Resource Links
Project: [project code]
```

---

## New Tag Categories for Work

### Project/Location Tags
- `#NVA05A` - Project identifier
- `#D2D-checklist` - Design to Delivery checklist

### Work Type Tags
- `#work` - General work-related
- `#meeting` - Meeting notes
- `#email` - Email threads
- `#quick-links` - Resource collections
- `#resources` - Reference materials

### Topic Tags
- `#safety` - Safety-related items
- `#operations` - Operational topics
- `#emergency-planning` - Emergency preparedness
- `#evacuation-maps` - Evacuation procedures
- `#EHS` - Environmental Health & Safety

### Status Tags
- `#cancelled` - Cancelled events

---

## Suggested Folder Structure for Work Notes

```
Work/
├── Projects/
│   └── NVA05A/
│       ├── Meetings/
│       │   └── 1770241714441_CANCELLED-D2D_Safety-Ops_Sync_Up_-_7-19-2024.md
│       ├── Emails/
│       │   └── 1770241714443_RE_NVA05A_Emergency_Evacuation_Maps.md
│       └── Resources/
│           └── 1770241714443_06_07_24_Activity.md
```

---

## Bases Views You Can Create

### 1. **NVA05A Project Dashboard**
Show all notes tagged with `#NVA05A`
- Filter by: Status, Priority, Date
- Columns: File Name, Status, Priority, Date, Type
- Sort by: Date (newest first)

### 2. **Meeting Tracker**
Show all notes tagged with `#meeting`
- Filter by: Status (Completed, Cancelled, Scheduled)
- Columns: Meeting Time, Attendees, Topic, Status
- Sort by: Date

### 3. **Action Items Across Project**
Create a view that shows all unchecked checkboxes from NVA05A notes
- Great for tracking open items across meetings, emails, and resources

### 4. **Email Threads by Subject**
Show all email notes
- Filter by: Project, From, To
- Columns: Subject, Date Received, From, Attachments
- Sort by: Date Received

---

## Dataview Queries for Work Notes

### All NVA05A Items
```dataview
TABLE Status, Priority, Date, "Meeting Time" as Time
FROM #NVA05A 
SORT Date DESC
```

### Open Action Items
```dataview
TASK
FROM #NVA05A 
WHERE !completed
GROUP BY file.link
```

### Safety-Related Items
```dataview
LIST
FROM #safety 
WHERE Project = "NVA05A"
SORT Date DESC
```

---

## Best Practices for Work Notes

### 1. **Consistent Naming**
Keep the timestamp prefix for imported items:
- Makes them sortable by import date
- Easy to trace back to Outlook/Teams

### 2. **Link Project Files**
Use the `Related` property to connect:
- Meeting notes to email follow-ups
- Resource links to relevant meetings
- Action items across documents

### 3. **Track Attendees**
List all meeting participants in YAML for:
- Easy filtering by person
- Understanding who needs follow-up

### 4. **Preserve Attachments**
Note attached files in YAML so you can:
- Track important documents
- Link to actual files in your system

### 5. **Update Status Regularly**
- Cancelled → Archive cancelled meetings
- Complete → Mark finished deliverables
- Active → Keep current work items visible

---

## Creating Related Project Notes

Consider creating these hub notes to link everything together:

### `NVA05A Project.md`
```yaml
---
PARA: Project
Status: In Progress
tags:
  - work
  - project
  - data-center
Project Code: NVA05A
---

# NVA05A Project

## Overview
[Project description]

## Key Resources
- [[1770241714443_06_07_24_Activity]] - Quick links
- D2D Checklist
- OneDrive Folder

## Recent Meetings
- [[1770241714441_CANCELLED-D2D_Safety-Ops_Sync_Up_-_7-19-2024]]

## Safety Items
- [[1770241714443_RE_NVA05A_Emergency_Evacuation_Maps]]
```

### `D2D Checklist.md`
```yaml
---
PARA: Area
Status: Active
tags:
  - work
  - checklist
  - process
---

# D2D (Design to Delivery) Checklist

## Overview
Standard checklist for data center project delivery

## Related Projects
- [[NVA05A Project]]

## Key Sections
- EHS Tab
- Operations Items
- Safety Items
```

---

## Next Steps

1. ✅ Download the 3 enhanced files
2. 📁 Place them in your Work/Projects/NVA05A folder structure
3. 🔗 Create the hub notes (NVA05A Project, D2D Checklist)
4. 📊 Set up a Bases view for NVA05A project tracking
5. 🔄 Repeat this process for other work projects!

---

## Tips for Future Work Note Imports

When importing more work notes:
- Keep meeting notes separate from email threads
- Use consistent project tags (#ProjectCode)
- Always include attendee lists for meetings
- Link related notes via the Related property
- Track action items with checkboxes
- Add priority levels based on urgency
