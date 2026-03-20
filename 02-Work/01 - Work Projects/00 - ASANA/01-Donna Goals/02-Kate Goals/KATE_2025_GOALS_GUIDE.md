# Kate 2025 Construction EHS Goals Enhancement Guide

> **Navigation Tip:** All file names below are clickable wiki links!

## Overview
Enhanced 7 Construction EHS leadership notes for Kate, adding the Construction side to your complete organizational hierarchy.

---

## Files Enhanced - By Category

### 🎯 Goals Overview (2 files)
1. [[02-Kate_Goals|02-Kate Goals]] - Goals folder overview
2. [[Kate_2025_Goals|Kate 2025 Goals]] - Complete 5 goals list

### 📋 Individual Goals (5 files)
3. [[Kate_2025_Goal_1|Kate 2025 Goal 1]] - **Internal Communications** ⭐
4. [[Kate_2025_Goal_2|Kate 2025 Goal 2]]
5. [[Kate_2025_Goal_3|Kate 2025 Goal 3]]
6. [[Kate_2025_Goal_4|Kate 2025 Goal 4]]
7. [[Kate_2025_Goal_5|Kate 2025 Goal 5]]

---

## 🎊 EXPANDED HIERARCHY - 60 FILES TOTAL!

```
Donna (CEO)
    ├── Jesse (Operations EHS) - 20 files
    │   └── Team: Nuckolls, Goetz, Saucedo (30 files)
    │
    └── Kate (Construction EHS) - 7 files ✅ NEW!
        └── Team: Fisher, others (TBD)
            ↓
        Bridge Construction-Ops EHS Gap (3 files)
        └── Connects both departments
```

**New Total: 60 Enhanced Files!**
- 53 files (previous batches)
- 7 Kate files (this batch)

---

## Kate's 5 Goals

### Goal 1: Internal Communications ⭐⭐⭐
- **Theme:** #Improve_Internal_Communication
- **Purpose:** Bridge Construction-Ops EHS gap
- **Parent Goal:** [[Improve Internal Communications]]
- **Sub-Goals:**
  - [[Fisher 2025 Goal 1]]
  - Kate 2025 Goal 1 (execution)
- **Integration:** 
  - Links to [[Bridge Construction-Ops EHS Gap]]
  - Counterpart to [[Goetz 2025 Goal 3]] (Ops side)
  - Supports [[NVA06A D2D]] handovers

### Goal 2
- **Focus:** [To be defined]
- **Status:** In Progress

### Goal 3
- **Focus:** [To be defined]
- **Status:** In Progress

### Goal 4
- **Focus:** [To be defined]
- **Status:** In Progress

### Goal 5
- **Focus:** [To be defined]
- **Status:** In Progress

---

## Construction vs Operations EHS

### Kate's Domain (Construction EHS)
- **Phase:** Construction/build phase
- **Focus:** Site safety during construction
- **Deliverable:** D2D checklist, handover to Operations
- **Team:** Construction EHS personnel

### Jesse's Domain (Operations EHS)
- **Phase:** Operations/running phase
- **Focus:** Ongoing facility operations
- **Receives:** Handovers from Construction
- **Team:** Nuckolls, Goetz, Saucedo, Fisher (shared)

### The Bridge
**Goal 1 (Kate) ↔ Goal 3 (Goetz)**
- Kate improves Construction side communication
- Goetz improves Operations side communication
- Together they bridge the gap!

---

## Key Connections Established

### Goal 1 Deep Dive

**Kate Goal 1 supports:**
```
Improve Internal Communications (Company Goal)
    ↓
Bridge Construction-Ops EHS Gap (Strategic Initiative)
    ↓
├── Kate Goal 1 (Construction side)
│   └── Fisher Goal 1 (sub-goal support)
│
└── Goetz Goal 3 (Operations side)
    └── Supports NVA06A D2D handovers
```

### Cross-Department Integration
- **Fisher:** Works with BOTH Kate and Jesse's teams
- **D2D Projects:** NVA06A benefits from Kate's communication improvements
- **Handovers:** Better Construction→Ops transitions

---

## Folder Structure Recommendation

```
Work/
├── Executive Goals/
│   ├── Jesse/ (Operations EHS - 20 files)
│   └── Kate/ (Construction EHS - 7 files) ✅ NEW
│       ├── 02-Kate Goals.md (overview)
│       ├── Kate 2025 Goals.md (main list)
│       └── Individual Goals/
│           ├── Goal 1.md ⭐ (Internal Communications)
│           ├── Goal 2.md
│           ├── Goal 3.md
│           ├── Goal 4.md
│           └── Goal 5.md
│
├── Goals/
│   └── 2025/
│       ├── Nuckolls/ (16 files)
│       ├── Goetz/ (7 files)
│       ├── Saucedo/ (7 files)
│       └── Fisher/ (TBD - referenced in Kate Goal 1)
│
└── Strategic Initiatives/
    └── Bridge Construction/ (3 files)
        └── Links both Kate and Jesse
```

---

## Bases Views You Can Create

### 1. **Full Organization Goals (60 Files)**
```
Filter: #goals AND #2025
Columns: Department, Manager, Goal, Theme, Status
Group By: Department (ConstructionEHS, OpsEHS)
Sort: Department, Manager
```

### 2. **Construction EHS Dashboard**
```
Filter: Manager = "Kate" AND Year = 2025
Columns: Goal Number, Goal Name, Status
Sort: Goal Number
```

### 3. **Bridge Initiative View (Both Sides)**
```
Filter: Related contains "Bridge Construction-Ops EHS Gap"
OR Related contains "Improve Internal Communications"
Columns: Department, Employee, Goal, Role
Group By: Department
```

### 4. **Cross-Department Collaboration**
```
Filter: (Manager = "Kate" OR Manager = "Jesse") AND #Improve_Internal_Communication
Columns: Department, Goal, Counterpart
```

---

## Dataview Queries

### Kate's Goals
```dataview
TABLE 
  "Goal Number" as Goal,
  Status,
  "Parent Goal" as Parent
FROM #ConstructionEHS AND #goals
WHERE Manager = "Kate"
SORT "Goal Number"
```

### Construction vs Operations Goals
```dataview
TABLE 
  Department,
  Manager,
  "Goal Number" as Goal
FROM #goals AND #2025
WHERE Manager = "Kate" OR Manager = "Jesse"
GROUP BY Department
```

### Bridge Communication Goals
```dataview
LIST
FROM #Improve_Internal_Communication AND #goals
WHERE Year = 2025
```

---

## Action Items After Importing

### Immediate
- [ ] Download all 7 Kate files + guide
- [ ] Create Kate folder in Executive Goals
- [ ] Place files in appropriate locations
- [ ] Verify links to Jesse and Bridge initiative files

### Fill in Blanks
- [ ] Complete Goal 2, 3, 4, 5 descriptions
- [ ] Add Donna's goal alignments for all 5 goals
- [ ] Add specific deliverables and metrics
- [ ] Define Construction EHS team structure

### Connect to Ecosystem
- [ ] Link Kate goals to Jesse goals where relevant
- [ ] Update [[Bridge Construction-Ops EHS Gap]] with Kate's role
- [ ] Add Fisher's goals (referenced in Kate Goal 1)
- [ ] Create Construction-Ops comparison views

### Set Up Tracking
- [ ] Create Kate Goals Dashboard
- [ ] Create Construction-Operations bridge view
- [ ] Set up cross-department tracking
- [ ] Schedule quarterly reviews

---

## The Complete Picture Now

### What You Have (60 Files)

**CEO Level (Donna):**
- Not yet enhanced

**Executive Level (40 files):**
- Jesse (Operations): 20 files
- Kate (Construction): 7 files ✅ NEW

**Team Level (30 files):**
- Nuckolls: 16 files
- Goetz: 7 files
- Saucedo: 7 files
- Fisher: Referenced (TBD)

**Strategic Level (3 files):**
- Bridge Construction-Ops EHS Gap
- Safety Scope Site Integration
- Initiative hub

---

## Key Insights

### Two Sides of EHS
Your organization has TWO EHS departments:
- **Construction EHS** (Kate) - Build phase
- **Operations EHS** (Jesse) - Run phase

### The Bridge is Real
Goal 1 shows the bridge in action:
- Kate Goal 1 (Construction side)
- Goetz Goal 3 (Operations side)  
- Both improve the handover interface

### Fisher's Cross-Functional Role
Fisher appears to support BOTH departments:
- Referenced in Kate Goal 1
- Referenced in multiple Ops goals
- Likely a bridge person

---

## Next Steps

1. ✅ Download all 7 files + guide
2. 📁 Organize into Kate folder
3. 🔗 Verify links to all 53 previous files
4. 📊 Create Construction-Ops comparison views
5. 🤝 Document Fisher's role (when you upload Fisher's goals)
6. 📈 Set up dual-department tracking

**Your organizational hierarchy now includes BOTH departments!** 🎉

**Updated Total: 60 Enhanced Files**
- 40 executive/leadership files (Jesse + Kate)
- 30 team member files
- 3 strategic initiative files

Ready for the next batch! 🚀
