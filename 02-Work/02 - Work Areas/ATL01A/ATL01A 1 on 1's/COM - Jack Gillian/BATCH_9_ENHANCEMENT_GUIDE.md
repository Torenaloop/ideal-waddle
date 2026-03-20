---
# Site-Specific Enhancement Guide
## Batch 9: ATL01A (Atlanta Data Center)

### Overview
This batch consists of **9 files** (7 enhanced + 2 new hubs) focused on **site-specific operational management** for ATL01A. This introduces a new pattern: **site-level knowledge organization** that will scale across all 14 data center facilities.

---

## Files Enhanced in This Batch

### 📅 **Meeting Date Files (6 files)**
1. `ATL01A_Meeting_2024-07-29_ENHANCED.md`
2. `ATL01A_Meeting_2024-08-26_ENHANCED.md`
3. `ATL01A_Meeting_2024-09-30_ENHANCED.md`
4. `ATL01A_Meeting_2024-10-28_ENHANCED.md`
5. `ATL01A_Meeting_2024-11-25_ENHANCED.md`
6. `ATL01A_Meeting_2024-12-NA_ENHANCED.md` (cancelled)

**Original Status**: Empty placeholder files
**Enhancement Approach**: Created template structure noting meetings occurred but notes weren't captured

**Key Features**:
- YAML with site, participants, date metadata
- Status note explaining no content captured
- Typical agenda topics based on standing items
- Links to both site hub and person hub
- Series navigation (previous/next meetings)

**Why Include Empty Files?**:
- Preserves meeting history (shows monthly cadence)
- Provides template for future note-taking
- Documents relationship continuity
- Enables pattern recognition (gaps, frequency)

---

### 📋 **COM Contact Note (1 file)**
**Original**: `COM_-_Jack_Gillian.md` (5 bullet points)
**Enhanced**: `Jack_Gillian_Contact_Note_ENHANCED.md`

**Enhancements Added**:
- Comprehensive YAML with site, role, regional context
- Expanded each of 5 standing topics with full context
- Linked to EHS goals and audit project
- Explained Chubb IH coordination
- Performance framework connections
- Meeting history integration

**Standing Topics Explained**:
1. **Generator Maintenance/Runs** - Chubb IH coordination, insurance compliance
2. **Audit Findings Action Plan** - 2025 audit prep, Q1 closure goals
3. **SOSPES Items** - Safety observation program, monthly target
4. **Client Business Reviews** - Customer relationship management
5. **Training** - EQW within 60 days, EHS Learning Path completion

---

### 🏢 **Site Hub (NEW)**
**Created**: `ATL01A_Site_Hub.md`

**Purpose**: Central repository for all ATL01A facility information

**Contents**:
- Facility overview and address
- Key personnel (Jack Gillian COM, David Nuckolls EHS support)
- 2025 audit details (Kara Van Blarcum auditor, proposed dates)
- Equipment & infrastructure (generators, cooling, electrical)
- EHS compliance (permits, reporting, NOV tracking)
- Safety programs (SOSPES, training, incident response)
- Customer management (business reviews, tours)
- Coordination requirements (Chubb, auditors, vendors)
- Performance metrics (operational and EHS)
- Meeting history (links to all 6 meeting files)
- Success indicators and support triggers

**PARA Classification**: Areas (ongoing operational responsibility)

---

### 👤 **Person Hub (NEW)**
**Created**: `Jack_Gillian_Hub.md`

**Purpose**: Central profile for Jack Gillian as ATL01A COM

**Contents**:
- Role overview and responsibilities
- Site accountability (ATL01A)
- EHS performance framework (2025 goals)
- Key relationships (reports to, manages, coordinates with)
- Standing topics and focus areas
- 2025 audit responsibilities (pre/during/post)
- Performance criteria by category
- Meeting cadence with David Nuckolls
- Development opportunities and career path
- Communication preferences
- Success indicators and support needs

**PARA Classification**: Areas (ongoing relationship management)

---

## Unique Characteristics of This Batch

### Site-Level Granularity
**Previous Batches**: Organizational level (projects, goals, frameworks)
**This Batch**: Individual facility level (specific site, specific manager)

**Why This Matters**:
- Operations happen at site level
- Each site has unique context (equipment, customers, permits)
- COM is accountable for site performance
- Hub architecture enables navigation from strategic to tactical

---

### Empty Files with Structure
**First Batch** to include empty placeholder files with enhancement:
- Acknowledges meetings occurred
- Preserves relationship history
- Provides template for future
- Documents cadence and patterns

**Alternative Rejected**: Skipping empty files entirely
**Rationale**: Meeting history is valuable even without notes; shows continuity

---

### Dual Hub Architecture
**Site Hub + Person Hub** cross-referenced:
- Site hub: "Jack Gillian manages this site" → [[Jack Gillian Hub]]
- Person hub: "Jack manages this site" → [[ATL01A Site Hub]]
- Meeting files link to both
- Contact note links to both

**Benefits**:
- Navigate from site perspective (what's happening at ATL01A?)
- Navigate from person perspective (what's Jack responsible for?)
- See connections between people and places

---

## PARA Classification Decisions

### Meeting Files: Areas
**Why Areas (ongoing responsibility) not Projects (temporary)**:
- Monthly 1:1s are ongoing management rhythm
- No end date (continues indefinitely)
- Part of standard COM supervision
- Not tied to specific project

### Contact Note: Areas
**Why Areas not Resources (reference)**:
- Living document used in ongoing meetings
- Standing topics evolve over time
- Active management tool, not static reference

### Both Hubs: Areas
**Why Areas**:
- Ongoing operational responsibilities
- No completion state
- Maintained and updated continuously
- Part of standard operations structure

---

## Cross-Reference Network

### Within This Batch (9 files)
```
ATL01A Site Hub (central)
    ├── Links to Jack Gillian Hub
    ├── Links to Jack Gillian Contact Note
    └── Links to all 6 meeting files

Jack Gillian Hub (central)
    ├── Links to ATL01A Site Hub
    ├── Links to Jack Gillian Contact Note
    └── Links to all 6 meeting files

Each Meeting File
    ├── Links to ATL01A Site Hub
    ├── Links to Jack Gillian Hub
    └── Links to David Nuckolls Hub

Jack Gillian Contact Note
    ├── Links to ATL01A Site Hub
    ├── Links to Jack Gillian Hub
    └── Links to all 6 meeting files
```

---

### To Previous Batches (71 existing files)

**To 2025 Environmental Audit Project Hub** (Batch 7):
- ATL01A is one of 14 sites being audited
- Kara Van Blarcum assigned as auditor
- Proposed dates: Week of 4/14 or 4/21
- Jack Gillian listed as site contact
- Audit findings closure tied to COM performance goals

**To David Nuckolls Hub** (Batch 1):
- David conducts monthly 1:1s with Jack
- Provides EHS support to ATL01A
- Manages Jack's performance per EHS goals
- Coordinates audit preparation

**To 2025 EHS Goals - COMs** (Batch 8):
- Jack evaluated on this framework
- Audit completion, SOSPES, training, NOVs
- 5-point scale (Below → Outstanding)
- Specific criteria for each category

**To ENV AUDIT Files** (Batch 7):
- [[ENV AUDIT - Master Schedule and Contacts]] lists ATL01A details
- [[02-Work/04 - Work Archives/Daily Notes 2/2025-02-27/ENV AUDIT - Proposed Dates]] tracks ATL01A date selection

---

## Pattern for Future Site Batches

### Anticipated Structure
If future batches follow this pattern (and description suggests they will):

**Per Site, Expect**:
- 6-12 monthly meeting date files
- 1 COM contact note
- 1 Site Hub
- 1 COM Hub (person hub)

**Projected Totals**:
- **14 sites** in 2025 audit = 14 site batches
- ~10 files per site × 14 = **~140 additional files**
- **14 Site Hubs** + **14 COM Hubs** = **28 new hubs**

---

### Regional Distribution
Based on [[ENV AUDIT - Master Schedule and Contacts]]:

**East Region (David Nuckolls)** - 6 sites:
- ATL01A - Jack Gillian (this batch) ✅
- NAL01A - Matt Honaker
- NVA01A - Todd Lipcsey
- NVA02D - Joe Kendra
- NVA05A - Drew Van Kleek
- TOR01A - Denis Davidov

**Central Region (Matt Saucedo)** - 4 sites:
- CHI01A - Sorin Bean
- CHI01B - Robert Sylvester
- DFW01A - Travis Gilbert
- DFW01B - Logan Parish

**West Region (Matt Goetz + Eileen Flama)** - 5 sites:
- POR01A - Matt DeZinno
- POR02A - Justin Kelly
- POR03A - Alex Stiegemeier
- SVY01A - Matthew Waymire
- SVY01B - Matthew Waymire (same COM for both)

---

### Scaling Considerations

**Hub Proliferation**:
- Current: 8 hubs (Batches 1-8)
- After all sites: 8 + 28 = **36 hubs** total
- Is this too many?

**Answer**: No - appropriate granularity
- Each site hub serves specific facility
- Each COM hub serves specific manager
- Alternative (one "all sites" hub) would be unwieldy
- Hub architecture makes 36 hubs navigable

**Search Strategy**:
- Tag-based: `#site-hub` finds all 14 site hubs
- Tag-based: `#com` finds all 14 COM hubs
- Region tags: `#east-region`, `#central-region`, `#west-region`
- Site-specific: `#atl01a` finds everything ATL01A

---

## Key Insights from This Batch

### Monthly Management Rhythm
Empty meeting files reveal **David Nuckolls' COM management approach**:
- Monthly 1:1 cadence (4-week intervals)
- Consistent schedule (late July, late Aug, late Sept, late Oct, late Nov)
- December gap (holiday/vacation)
- Structured agenda (standing topics)

This pattern likely applies to all COMs David manages.

---

### Standing Topics Framework
Jack's 5 standing topics provide template for all COM conversations:
1. **Equipment Coordination** (generators at ATL01A; may vary by site)
2. **Audit Findings** (universal - all sites have findings to close)
3. **SOSPES** (universal - all COMs evaluated on observations)
4. **Client Relationships** (universal - all sites have customers)
5. **Training** (universal - all COMs evaluated on team training)

**Reusable Structure** for other COM contact notes.

---

### Chubb IH Coordination
**New stakeholder identified**: Chubb (insurance/industrial hygiene)
- Generator testing requires advance coordination
- Insurance compliance documentation
- Appears to be organization-wide (not just ATL01A)
- Add to stakeholder tracking

---

### Performance-Topic Alignment
Jack's standing topics **perfectly align** with [[2025 EHS Goals - COMs]]:
- Audit findings → Environmental audit completion goal
- SOSPES → Safety observation goal
- Training → EHS Learning Path & EQW completion goals
- Generator coordination → Operational readiness (not explicit goal but supports compliance)
- Client reviews → Customer satisfaction (not EHS goal but COM responsibility)

**This is intentional design**: Monthly 1:1 topics = areas where COM is evaluated.

---

## Enhancement Statistics

### Batch Size
- **Original files**: 7 (6 empty meetings + 1 contact note with 5 bullets)
- **Enhanced files**: 9 (7 enhanced + 2 hubs created)
- **Total pages**: ~55 (estimated printed pages)

### Content Added
- **YAML blocks**: 9
- **Cross-references**: 60+ individual links
- **Tags**: 15+ unique tags
- **Hub files**: 2 (Site + Person)
- **Meeting templates**: 6 (with reusable structure)

### Organizational Impact
- **Sites documented**: 1 (ATL01A) - first of 14
- **COMs profiled**: 1 (Jack Gillian) - first of 14
- **Meeting history**: 6 months preserved
- **Standing topics**: Reusable framework established

---

## Document Naming Conventions

### Pattern Used
- **Meeting files**: `ATL01A_Meeting_YYYY-MM-DD_ENHANCED.md`
- **Contact note**: `Jack_Gillian_Contact_Note_ENHANCED.md`
- **Site hub**: `ATL01A_Site_Hub.md`
- **Person hub**: `Jack_Gillian_Hub.md`

### Site Code Prefix
- `ATL01A` = Atlanta site 01A
- Site codes from [[ENV AUDIT - Master Schedule and Contacts]]
- Enables sorting by site
- Clear geographic identification

### Date Format
- `YYYY-MM-DD` for chronological sorting
- `2024-12-NA` for cancelled/not applicable

---

## Quality Assurance Checklist

### ✅ All Files Include
- [x] YAML frontmatter with appropriate PARA classification
- [x] Site code (ATL01A) and/or person name (Jack Gillian)
- [x] Related files cross-references
- [x] Tag structure for discovery
- [x] Links to David Nuckolls Hub (relationship manager)
- [x] Links to 2025 EHS Goals and Audit Project

### ✅ Meeting Files Include
- [x] Status note explaining no content captured
- [x] Typical agenda topics (standing items)
- [x] Links to both site hub and person hub
- [x] Series navigation (previous/next)

### ✅ Contact Note Includes
- [x] All 5 standing topics expanded with context
- [x] Links to EHS goals and audit project
- [x] Explanation of Chubb IH coordination
- [x] Performance framework connections

### ✅ Site Hub Includes
- [x] Facility details and address
- [x] Key personnel with hub links
- [x] 2025 audit details
- [x] Equipment and infrastructure
- [x] EHS compliance requirements
- [x] Safety programs
- [x] Performance metrics
- [x] Meeting history
- [x] Success indicators

### ✅ Person Hub Includes
- [x] Role and responsibilities
- [x] Site accountability
- [x] Performance framework (EHS goals)
- [x] Key relationships
- [x] Standing topics
- [x] Audit responsibilities
- [x] Development opportunities
- [x] Communication preferences
- [x] Success indicators

---

## Integration with Previous Batches

### Total Files Now: 80 (71 previous + 9 this batch)
### Total Hubs Now: 10 (8 previous + 2 this batch)

**Hub Progression**:
1. Rhett Hub (Personal)
2. Kelsey & Celebrations Hub (Personal)
3. Jesse Kenser Hub (Work Executive)
4. Kate Hub (Work Executive)
5. David Nuckolls Hub (Work Team)
6. Matt Goetz Hub (Work Team)
7. 2025 Environmental Audit Project Hub (Project)
8. 2025 EHS Performance Goals Hub (Area)
9. **ATL01A Site Hub** (Area - Site) ← This batch
10. **Jack Gillian Hub** (Area - Person/COM) ← This batch

---

### How This Batch Connects

**To David Nuckolls Hub** (Batch 1):
- David manages Jack Gillian
- Conducts monthly 1:1s at ATL01A
- Provides EHS support to site
- All 6 meeting files link to David's hub

**To 2025 Environmental Audit Project Hub** (Batch 7):
- ATL01A is Site #1 in audit roster
- Jack Gillian is site contact
- Audit findings closure is standing topic
- Pre/during/post audit responsibilities documented

**To 2025 EHS Goals - COMs** (Batch 8):
- Jack evaluated per this framework
- Standing topics align with goal criteria
- Performance targets referenced throughout
- Success indicators match goal levels

**To Future Site Batches** (Batches 10+):
- Template for remaining 13 sites
- Reusable structure for meeting files
- Standing topics framework applicable to all COMs
- Hub architecture scales to all sites

---

## Use Cases by Role

### For David Nuckolls (EHS Manager)
**Primary Use**: Monthly 1:1 preparation and COM management
1. Review [[ATL01A Site Hub]] before meeting for context
2. Check [[Jack Gillian Hub]] for performance status
3. Reference [[Jack Gillian Contact Note]] for standing topics
4. Take notes in monthly meeting files (template provided)
5. Track Jack's progress against [[2025 EHS Goals - COMs]]

---

### For Jack Gillian (COM)
**Primary Use**: Performance tracking and resource reference
1. Review [[Jack Gillian Hub]] to understand expectations
2. Use [[Jack Gillian Contact Note]] to prepare for 1:1s
3. Check [[ATL01A Site Hub]] for audit and compliance status
4. Track progress on standing topics
5. Reference [[2025 EHS Goals - COMs]] for performance targets

---

### For Regional Leadership
**Primary Use**: COM performance oversight
1. Review [[ATL01A Site Hub]] for facility status
2. Check [[Jack Gillian Hub]] for COM performance
3. Compare across sites (when other site hubs exist)
4. Identify support needs or escalation requirements

---

### For Future Site Batch Enhancement
**Primary Use**: Template for remaining sites
1. Use ATL01A meeting files as template
2. Adapt contact note structure to site-specific topics
3. Clone site hub structure with site-specific details
4. Clone person hub structure for each COM
5. Apply same tag structure and cross-references

---

## Common Questions & Answers

### Q: Why enhance empty meeting files?
**A**: Preserves meeting history, documents relationship cadence, provides template for future note-taking, enables pattern recognition. Alternative (deleting them) loses historical context.

---

### Q: Will 14 site hubs + 14 COM hubs (28 total) be too many?
**A**: No. Each hub serves specific facility or manager. Tags enable filtering (`#site-hub`, `#com`, `#east-region`). Alternative (one "all sites" hub) would be 100+ pages and unnavigable. Hub architecture makes 28 hubs manageable.

---

### Q: Why separate contact note and person hub?
**A**: Different purposes. Contact note is working document for meetings (standing topics). Person hub is comprehensive profile (role, performance, relationships, development). Contact note is tactical; person hub is strategic. Both link to each other.

---

### Q: What if other sites don't have same standing topics?
**A**: Standing topics will vary by site. Jack's 5 topics are ATL01A-specific (though many will be universal like audit findings, SOSPES, training). Each site's contact note should reflect that site's actual discussion topics. Framework is reusable; content is customized.

---

### Q: Should we create regional hubs too (East, Central, West)?
**A**: Not yet. See if needed after a few more site batches. If pattern emerges of regional-level coordination or decisions, then create regional hubs. For now, site hubs + regional manager hubs (David Nuckolls, Matt Goetz, Matt Saucedo) provide sufficient structure.

---

## Next Steps

### Immediate Actions (User)
1. Import all 9 files into Obsidian vault
2. Verify links resolve correctly
3. Review hub structures to ensure they match workflow
4. Adapt templates if needed before next site batch

---

### For Next Site Batch (Batch 10+)
1. Choose next site (recommend staying in East region: NAL01A, NVA sites, or TOR01A)
2. Apply this batch's template structure
3. Customize contact note topics to site specifics
4. Create site hub and COM hub
5. Enhance meeting files with same approach

---

### Ongoing Maintenance
1. Add new meeting notes as they occur (use template)
2. Update contact note if standing topics evolve
3. Update site hub with audit outcomes, performance milestones
4. Update person hub with career developments
5. Track performance against EHS goals in hubs

---

## Future Batch Opportunities

### Immediate Next Steps (Site Batches)
Recommended sequence to complete East Region first:
- **Batch 10**: NAL01A (Matt Honaker)
- **Batch 11**: NVA01A (Todd Lipcsey)
- **Batch 12**: NVA02D (Joe Kendra)
- **Batch 13**: NVA05A (Drew Van Kleek)
- **Batch 14**: TOR01A (Denis Davidov)

Then move to other regions (Central, West).

---

### Alternative Batch Options
- **Project-specific**: If major initiative emerges at ATL01A
- **Incident-specific**: If significant incident requires documentation
- **Customer-specific**: If major customer relationship needs tracking
- **Regional-specific**: If regional patterns emerge requiring hub

---

## Key Takeaways

### For Site-Level Management
1. **Monthly 1:1 cadence** is standard COM supervision approach
2. **Standing topics** create consistency and accountability
3. **Hub architecture** enables navigation from site or person perspective
4. **Performance alignment** ensures topics match evaluation criteria

### For Knowledge Management
1. **Empty files with structure** preserve history and provide templates
2. **Dual hubs** (site + person) serve different use cases
3. **Cross-references** create rich context web
4. **Scalable pattern** works for 1 site or 14 sites

### For Obsidian Enhancement
1. **Template first** approach saves time on repetitive content
2. **Hub architecture** makes large vaults navigable
3. **Tag structure** enables filtering and discovery
4. **PARA classification** works at site-level granularity

---

## Summary

Batch 9 successfully established the **site-level management pattern** with ATL01A as the template. Created **9 files** (7 enhanced + 2 hubs) documenting monthly COM supervision, standing coordination topics, and comprehensive site/person profiles. This pattern will scale across remaining 13 sites, eventually adding ~140 files and 28 hubs to create complete operational knowledge base.

**Total Files Enhanced: 80** (71 previous + 9 this batch)
**Total Hubs Created: 10** (including first site hub and first COM hub)

Ready for the next site! 🏢

---

*Enhancement completed: February 5, 2025*
*Batch number: 9 of ongoing series*
*Methodology: PARA + Hub Architecture + Site-Level Granularity*
