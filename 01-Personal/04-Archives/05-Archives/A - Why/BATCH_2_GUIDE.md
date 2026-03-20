# Updated Tagging Guide - Batch 2

## Files Enhanced in This Batch

### Personal/Family Notes
1. **Alamo Bowl '23** - Event memory (archived)
2. **Kelsey Christmas '23 Gift Ideas** - Gift list (archived)
3. **Rhett Christmas '23 Gift Ideas** - Gift list (archived)

### Educational/Reference Notes
4. **Isaac Newton** - Historical figure reference
5. **Three Laws of Motion** - Physics concept
6. **Law of Inertia** - Physics concept
7. **JJK** - Entertainment/media reference

### Obsidian Tutorial Notes
8. **Start Here** - Getting started guide
9. **Vault is just a local folder** - Vault management
10. **Plugins make Obsidian special for you** - Plugin info
11. **Format Your Note** - Markdown formatting
12. **First Note (Part 1)** - Introduction
13. **ChatGPT Work Workspace Example** - Structure example
14. **2023-09-01 Workspaces** - Template/test note

## New Tag Categories Added

### Education & Learning
- `#physics` - Physics topics
- `#science` - General science
- `#education` - Educational content
- `#Isaac-Newton` - Specific to Newton's work

### Entertainment & Media
- `#anime` - Japanese animation
- `#manga` - Japanese comics
- `#entertainment` - General entertainment
- `#gaming` - Video games

### Events & Memories
- `#event` - Specific events
- `#memory` - Memorable moments

### Gift Planning
- `#gift-ideas` - Gift brainstorming
- `#Christmas` - Holiday gifts

### Obsidian System
- `#obsidian` - Obsidian app related
- `#tutorial` - Tutorial content
- `#reference` - Reference material
- `#markdown` - Markdown formatting
- `#plugins` - Plugin information
- `#vault-management` - Vault organization
- `#workspace` - Workspace setup
- `#vault-structure` - How to organize

### General Organization
- `#template` - Note templates
- `#historical-figure` - Notable people from history

## Folder Organization Suggestions

Based on your vault structure (`01-Personal/06-Person/Family/`), here's where to place files:

```
Vault Root/
├── 01-Personal/
│   ├── 01-Daily Notes/
│   │   └── (date-based notes like 202508260953.md)
│   ├── 02-Projects/
│   │   ├── 2025 School Year.md
│   │   └── Fantasy Football.md
│   ├── 03-Areas/
│   │   ├── School.md
│   │   └── Sports.md
│   ├── 04-Archives/
│   │   ├── Alamo Bowl '23.md
│   │   ├── Kelsey Christmas '23 Gift Ideas.md
│   │   └── Rhett Christmas '23 Gift Ideas.md
│   ├── 05-Resources/
│   │   ├── Baseball.md
│   │   ├── Birthday.md
│   │   ├── Perfect Performance.md
│   │   ├── Isaac Newton.md
│   │   ├── Three Laws of Motion.md
│   │   ├── Law of Inertia.md
│   │   └── JJK.md
│   └── 06-Person/
│       └── Family/
│           ├── 02-Rhett.md
│           └── Kelsey.md
└── 09-Meta/ (or Obsidian Tutorial/)
    ├── Start Here.md
    ├── Vault is just a local folder.md
    ├── Plugins make Obsidian special for you.md
    ├── Format Your Note.md
    ├── First Note (Part 1).md
    ├── ChatGPT Work Workspace Example.md
    └── 2023-09-01 Workspaces.md
```

## Property Patterns by Note Type

### Event/Memory Notes
```yaml
PARA: Archive
Status: Complete
Date: YYYY-MM-DD
Event Type: [Game|Party|Trip|etc]
Location: City, State
Related: [links to people who attended]
Archive After: YYYY-MM-DD
```

### Gift List Notes
```yaml
PARA: Archive (or Project if active)
Status: [In Progress|Complete]
Year: YYYY
Person: [[Link to person]]
Type: Gift List
Related: [other gift lists]
```

### Educational/Reference Notes
```yaml
PARA: Resource
Type: [Concept|Person|Theory]
Subject: [Physics|Math|History|etc]
Related: [related concepts]
```

### Media/Entertainment Notes
```yaml
PARA: Resource
Type: Media
Related: [who watches/reads it]
Progress: [watching/reading progress]
```

## Quick Actions

### After Downloading Files:

1. **Sort by Category** (use the folder structure above)
   - Move archived items to `04-Archives/`
   - Move tutorial notes to `09-Meta/` or delete if not needed
   - Move person notes to `06-Person/Family/`
   - Move education notes to `05-Resources/`

2. **Update Links**
   - Search for `[[01-Personal/06-Person/Family/Rhett]]` 
   - Replace with `[[02-Rhett]]` if that's your preferred link style
   - Do the same for Kelsey

3. **Create Missing Notes**
   - You reference `[[Kelsey]]` - create this note if it doesn't exist
   - You reference `[[Diamond Heroes]]` - create if needed

4. **Clean Up Tutorial Notes**
   - Keep them in a separate folder for reference
   - Or delete them if you don't need the tutorials anymore

## Dataview Queries for New Content

### All Archived Events
```dataview
TABLE Date, "Event Type" as Type, Location
FROM #event 
WHERE PARA = "Archive"
SORT Date DESC
```

### Gift Ideas by Person
```dataview
TABLE Year, Status, file.lists as "Items"
FROM #gift-ideas 
WHERE Type = "Gift List"
SORT Year DESC, Person ASC
```

### Educational Resources
```dataview
TABLE Subject, Type, Related
FROM #education OR #physics OR #science
WHERE PARA = "Resource"
SORT Subject ASC, file.name ASC
```

### Entertainment Tracking
```dataview
TABLE Type, Progress, Related
FROM #anime OR #manga OR #entertainment
WHERE PARA = "Resource"
```

## Next Steps

1. ✅ Download all enhanced files (you've done this!)
2. 📁 Organize files into appropriate folders
3. 🔗 Update any broken links
4. 🗑️ Decide what to do with tutorial notes
5. 📊 Set up Dataview queries in your dashboard
6. 🔄 Establish a review routine

## Tips for Maintaining Your System

- **Archive old gift lists** each January
- **Update educational notes** as you learn more
- **Add photos/details** to memory notes while fresh
- **Review PARA categories** quarterly
- **Tag consistently** - pick one style and stick with it
