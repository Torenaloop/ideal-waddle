# Obsidian Tagging & Property System Guide

## PARA Structure
Your notes now follow the PARA methodology:

- **Projects** - Things with a deadline (School year, Fantasy Football)
- **Areas** - Ongoing responsibilities (Sports, School subject area)
- **Resources** - Reference material (Birthday, Baseball info, Person notes)
- **Archive** - Completed/inactive items

## Standard Properties Schema

### Required Properties
```yaml
PARA: [Project|Area|Resource|Archive]
Status: [Active|In Progress|Complete|On Hold|Archived]
Priority: [High|Medium|Low]
tags: [array of relevant tags]
```

### Optional Properties (use as needed)
```yaml
Start Date: YYYY-MM-DD
Due Date: YYYY-MM-DD
Parent Goal: "[[Link to parent note]]"
Child Goal: "[[Link to child/subtask note]]"
Related: [array of related note links]
Progress: [Not Started|In Progress|Complete]
Type: [Person|Event|Activity|Reference]
```

## Tag Categories

### People
- `#Rhett` - Main person tags
- `#Kelsey` - Family members
- `#family` - General family activities

### Activities
- `#sports` - General sports
- `#Football` - Specific sports
- `#Baseball`
- `#fitness` - Training/exercise

### Life Areas
- `#School` - Education related
- `#education`
- `#teacher-communication`
- `#curriculum`

### Events
- `#Birthday`
- `#Christmas`
- `#celebration`

### Organization
- `#quick-capture` - Quick notes
- `#calendar` - Calendar items
- `#reminder`

## Best Practices

### 1. Tag Consistently
Use lowercase for multi-word tags: `#speed-training` not `#Speed Training`

### 2. Link Liberally
Use `[[double brackets]]` to create connections between notes

### 3. Update Status Regularly
Keep Status and Progress fields current for better tracking

### 4. Use Parent/Child Relationships
Connect related goals and projects hierarchically

### 5. Add Dates
Include Start Date and Due Date for time-bound items

## Dataview Query Examples

### Active Projects for Rhett
```dataview
TABLE Status, Priority, "Due Date" as Due
FROM #Rhett 
WHERE PARA = "Project" AND Status = "In Progress"
SORT Priority ASC, "Due Date" ASC
```

### All Sports Activities
```dataview
LIST
FROM #sports 
WHERE Status = "Active"
SORT file.name ASC
```

### High Priority Items
```dataview
TASK
FROM #Rhett 
WHERE Priority = "High" AND Status != "Complete"
```

## Your Current Note Structure

### Person Notes
- **02-Rhett.md** - Central hub for all Rhett-related notes
- Links to all major life areas

### Project Notes
- **Fantasy Football.md** - Time-bound family activity
- **2025 School Year.md** - Annual school tracking
- **School.md** - Ongoing education tracking

### Area Notes  
- **Sports.md** - Ongoing sports participation
- **Perfect Performance.md** - Training facility/schedule

### Resource Notes
- **Baseball.md** - Sport-specific reference
- **Birthday.md** - Annual celebration planning
- **202508260953.md** - Quick capture note

## Migration Tips

1. **Backup first** - Copy your vault before making changes
2. **Start small** - Update 5-10 notes to test the system
3. **Use templates** - Create note templates with pre-filled properties
4. **Review weekly** - Adjust tags and properties as your system evolves
5. **Stay flexible** - PARA is a framework, adapt it to your needs

## Next Steps

1. Copy these enhanced notes into your vault
2. Update any file paths/links that point to your specific folder structure
3. Create templates based on these examples
4. Set up Dataview queries in your dashboard
5. Establish a weekly review routine to maintain the system
