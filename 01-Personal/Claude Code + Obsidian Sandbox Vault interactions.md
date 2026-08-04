# 2026-03-20 - 14:21

---
  Vault Summary

  Scale

  - 7,229 markdown files total
  - 2,894 files imported from Notion
  - 152 daily notes spanning mid-2025 to early 2026
  - 9 Obsidian Bases for database-style views

  Structure

  Personal (01-Personal/)
  - Daily notes organized by month
  - Projects: PMP certification, Spring Break trips, Power Platform training, Virginia living plans
  - Areas: Family members (Rhett, Kelsey), cars, finance, food, organic health tracking
  - Rhett has deep sub-structure: School, Sports (Baseball/Football with pitching velocity notes, hitting drills),
  Celebrations (Birthday, Christmas gift lists)
  - Weekly reviews in 02-Areas/11-Weekly Reviews/

  Work (02-Work/)
  - Clear PARA structure: Projects, Areas, Resources, Archives, Meetings, People, Tasks
  - Heavy focus on STACK Infrastructure data center operations
  - Site codes: ATL01A, NAL01A, NVA01A, NVA02DE, NVA05A, NVA05D, NVA06AB
  - Key projects: Environmental Audits (Antea Group), D2D Checklist, Bridge Construction-Ops EHS Gap
  - Asana integration with goals hierarchy (Donna → Jesse → Nuckolls → direct reports)
  - EHS (Environmental Health & Safety) manager role content

  Clippings & Imports
  - Web clippings folder with articles
  - Large Notion import (likely previous system)
  - GPT conversation exports

  YAML Frontmatter Patterns
  ┌───────────────┬─────────────────────────────────────────────┐
  │     Type      │                 Fields Used                 │
  ├───────────────┼─────────────────────────────────────────────┤
  │ meeting       │ meeting_date, participants, project, status │
  ├───────────────┼─────────────────────────────────────────────┤
  │ project       │ status, owner, start, due                   │
  ├───────────────┼─────────────────────────────────────────────┤
  │ email         │ Date Received, From, To, Cc, Attachments    │
  ├───────────────┼─────────────────────────────────────────────┤
  │ note          │ created, updated, tags                      │
  ├───────────────┼─────────────────────────────────────────────┤
  │ PARA-enhanced │ PARA, Status, Priority, Related             │
  └───────────────┴─────────────────────────────────────────────┘
  Inconsistency noted: Some notes use full PARA schema, many older/imported notes have no frontmatter.

  Top Tags
  ┌────────────────────────────┬───────┬───────────────────────────┐
  │            Tag             │ Count │          Purpose          │
  ├────────────────────────────┼───────┼───────────────────────────┤
  │ #discuss-with-person-a     │ 5,621 │ Action marker for 1-on-1s │
  ├────────────────────────────┼───────┼───────────────────────────┤
  │ #ATL01A / #NVA05A etc.     │ 40-10 │ Site identifiers          │
  ├────────────────────────────┼───────┼───────────────────────────┤
  │ #CAB                       │ 22    │ Change Advisory Board     │
  ├────────────────────────────┼───────┼───────────────────────────┤
  │ #OpsEHS / #ConstructionEHS │ 14/7  │ Work domain tags          │
  ├────────────────────────────┼───────┼───────────────────────────┤
  │ #Rhett / #Kelsey           │ 12/11 │ Family member tags        │
  └────────────────────────────┴───────┴───────────────────────────┘
  Link Patterns

  Heavy use of:
  - Bases: [[Tasks (Personal).base]], [[KTBR.base]], [[Meetings.base]]
  - Project hubs: [[2025 Environmental Audit Project Hub]], [[David Nuckolls Hub]]
  - Notion aliased links: [[Notion/NVA05A|NVA05A]]

---


How I Can Help You

  1. Standardize Frontmatter

  Many notes (especially Notion imports) lack consistent YAML. I could:
  - Batch-add PARA classification to untagged notes
  - Normalize Status values across the vault
  - Add missing type: fields to meetings, emails, projects

  2. Clean Up Duplicates

  I noticed duplicate folder structures (e.g., 00-Daily Notes/00-Daily Notes/ nesting). I could:
  - Identify redundant files
  - Flatten unnecessary folder nesting
  - Consolidate duplicate notes

  3. Create Hub Notes / MOCs

  Build Map of Content notes for:
  - Your work sites (ATL01A, NVA series) linking all relevant meetings, tasks, people
  - Baseball training resources (consolidate pitching/hitting drill notes)
  - Environmental Audit project (everything Antea Group related)

  4. Extract & Track Action Items

  The #discuss-with-person-a tag (5,600+ uses) suggests a pattern. I could:
  - Find all unchecked action items across work notes
  - Create a consolidated action item view
  - Identify overdue items from meeting notes

  5. Dataview Query Development

  Write queries for:
  - "All meetings with Donna in last 30 days"
  - "Open tasks by site code"
  - "Upcoming due dates across projects"

  6. Template Refinement

  Your 04-Templates/ has good templates. I could:
  - Create site-specific meeting templates (pre-filled with common attendees)
  - Build a daily note template with embedded queries
  - Add quick-capture templates for the patterns I see (EQW notes, CAB entries)

  7. Tag Cleanup & Consolidation

  Some tags overlap (#work vs #Work, #meeting vs #Meeting). I could:
  - Create a master tag taxonomy
  - Bulk-rename inconsistent tags
  - Identify orphaned/rarely-used tags

  8. Notion Import Cleanup

  Those 2,894 Notion files likely have:
  - Broken internal links
  - Redundant alias paths ([[Notion/NVA05A|NVA05A]])
  - Properties that don't match your current schema

  ---
  What would be most valuable to tackle first?