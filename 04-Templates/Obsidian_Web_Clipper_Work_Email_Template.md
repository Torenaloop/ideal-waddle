# Obsidian Web Clipper Template: Work Emails

## Template Code

```handlebars
---
para: {{#if (contains title "ENV AUDIT")}}Projects{{else if (contains title "EHS Goals")}}Areas{{else}}Areas{{/if}}
area: {{#if (contains title "ATL01A")}}Site Operations Management{{else}}Work Communications{{/if}}
document_type: Email
from: "{{#if author}}{{author}}{{else}}[Extract from content]{{/if}}"
to: "[Your name/email]"
date: "{{date:YYYY-MM-DD}}"
received: "{{time:YYYY-MM-DD HH:mm}}"
subject: "{{title}}"
site: {{#if (contains title "ATL01A")}}ATL01A{{else if (contains title "CHI01")}}CHI01A{{else if (contains title "DFW01")}}DFW01A{{else if (contains title "POR01")}}POR{{else if (contains title "NVA01")}}NVA01A{{else if (contains title "NAL01")}}NAL01A{{else if (contains title "TOR01")}}TOR01A{{else if (contains title "SVY01")}}SVY01A{{/if}}
project: {{#if (contains title "Environmental Audit")}}2025 Environmental Audit{{else if (contains title "EHS Goals")}}2025 EHS Performance Goals{{/if}}
related_files:
  - "[[David Nuckolls Hub]]"
{{#if (contains title "Jesse Kenser")}}  - "[[Jesse Kenser Hub]]"{{/if}}
{{#if (contains title "Jack Gillian")}}  - "[[Jack Gillian Hub]]"{{/if}}
{{#if (contains title "Matt Goetz")}}  - "[[Matt Goetz Hub]]"{{/if}}
{{#if (contains title "Matt Saucedo")}}  - "[[Matt Saucedo Hub]]"{{/if}}
{{#if (contains title "Kate")}}  - "[[Kate Hub]]"{{/if}}
{{#if (contains title "ATL01A")}}  - "[[ATL01A Site Hub]]"{{/if}}
{{#if (contains title "Environmental Audit")}}  - "[[2025 Environmental Audit Project Hub]]"{{/if}}
{{#if (contains title "EHS Goals")}}  - "[[2025 EHS Performance Goals Hub]]"{{/if}}
tags:
  - email
  - work
{{#if (contains title "ENV AUDIT")}}  - env-audit{{/if}}
{{#if (contains title "SOSPES")}}  - sospes{{/if}}
{{#if (contains title "Training")}}  - training{{/if}}
{{#if (contains title "ATL01A")}}  - atl01a{{/if}}
{{#if (contains title "audit")}}  - audits{{/if}}
{{#if (contains title "meeting")}}  - meetings{{/if}}
{{#if (contains title "action")}}  - action-items{{/if}}
{{#if (contains author "anteagroup")}}  - antea-group{{/if}}
---

# Email: {{title}}

## Email Metadata
**From**: {{#if author}}{{author}}{{else}}[Extract from email header]{{/if}}
**To**: [Your name/role]
**Date**: {{date:MMMM DD, YYYY}}
**Time**: {{time:HH:mm}}
**Subject**: {{title}}

---

## Email Content

{{content}}

---

## Quick Analysis

### Key Points
- [Extract main point 1]
- [Extract main point 2]
- [Extract main point 3]

### Action Items
- [ ] [Action item 1 with owner and due date]
- [ ] [Action item 2 with owner and due date]

### Decisions Made
- [Decision 1]
- [Decision 2]

### Questions Raised
- [Question 1]
- [Question 2]

---

## Context & Connections

### Related To
{{#if (contains title "ATL01A")}}
- **Site**: [[ATL01A Site Hub]]
- **COM**: [[Jack Gillian Hub]]
{{/if}}
{{#if (contains title "Environmental Audit")}}
- **Project**: [[2025 Environmental Audit Project Hub]]
- **Vendor**: Antea Group
{{/if}}
{{#if (contains title "EHS Goals")}}
- **Framework**: [[2025 EHS Performance Goals Hub]]
- **Performance**: [[2025 EHS Goals - COMs]]
{{/if}}

### People Mentioned
{{#if (contains content "Jesse Kenser" "jkenser")}}
- [[Jesse Kenser Hub]]
{{/if}}
{{#if (contains content "David Nuckolls" "dnuckolls")}}
- [[David Nuckolls Hub]]
{{/if}}
{{#if (contains content "Jack Gillian" "jgillian")}}
- [[Jack Gillian Hub]]
{{/if}}
{{#if (contains content "Matt Goetz" "mgoetz")}}
- [[Matt Goetz Hub]]
{{/if}}
{{#if (contains content "Matt Saucedo" "msaucedo")}}
- [[Matt Saucedo Hub]]
{{/if}}

---

## Follow-Up

### Next Steps
- [ ] Reply by: [date]
- [ ] Forward to: [person]
- [ ] Add to meeting agenda: [meeting name]
- [ ] Update: [relevant hub or project file]

### Related Documents
- [Link to related emails]
- [Link to meeting notes]
- [Link to project files]

---

## Email Storage
**Original Location**: Outlook / Gmail
**Clipped**: {{time:YYYY-MM-DD HH:mm}}
**Email ID**: [Paste message ID if needed for reference]

---

*Email captured via Obsidian Web Clipper*
```

---

## How to Use This Template

### 1. Install Obsidian Web Clipper
- Available as browser extension (Chrome, Firefox, Safari, Edge)
- Or use bookmarklet version
- Official Obsidian Web Clipper documentation: https://help.obsidian.md/Plugins/Web+Clipper

### 2. Add This Template to Web Clipper

**In Web Clipper Settings**:
1. Open Web Clipper settings in your browser
2. Go to "Templates" section
3. Click "Add New Template"
4. Name it: "Work Email"
5. Paste the template code above
6. Set trigger: Activate when URL contains "mail.google.com" or "outlook.office.com"

### 3. Customize for Your Workflow

**Edit the PARA Classification Logic**:
```handlebars
para: {{#if (contains title "ENV AUDIT")}}Projects{{else}}Areas{{/if}}
```
Add your own project keywords to auto-classify.

**Add Your Stakeholders**:
```handlebars
{{#if (contains title "Your Colleague")}}  - "[[Your Colleague Hub]]"{{/if}}
```

**Add Your Sites**:
```handlebars
site: {{#if (contains title "YOUR_SITE_CODE")}}YOUR_SITE_CODE{{/if}}
```

**Add Your Tags**:
```handlebars
{{#if (contains title "your-keyword")}}  - your-tag{{/if}}
```

---

## Template Features

### Automatic PARA Classification
- Detects project keywords (ENV AUDIT, EHS Goals) → Projects
- Defaults to Areas for general work
- Edit conditions to match your projects

### Auto-Linking to Hubs
- Detects names in title/content
- Automatically adds links to person hubs
- Links to site hubs when site codes detected
- Links to project hubs when project keywords found

### Smart Tagging
- Auto-tags based on subject content
- Site codes become tags (atl01a, chi01a, etc.)
- Project keywords become tags (env-audit, sospes)
- Vendor detection (antea-group from email domain)

### Email Metadata Captured
- From/To/Date/Subject preserved
- Timestamp of when clipped
- Link to original email location

### Action Item Extraction
- Template includes section for action items
- Checkboxes for task tracking
- Space for owners and due dates

### Context Preservation
- Full email content preserved
- Metadata maintained
- Cross-references suggested

---

## Usage Examples

### Example 1: Environmental Audit Email

**Email Subject**: "ENV AUDIT - Fw EXTERNAL STACK - Env. Audit Dashboard Discussion"

**Auto-Generated**:
- `para: Projects`
- `project: 2025 Environmental Audit`
- Links to: David Nuckolls Hub, 2025 Environmental Audit Project Hub
- Tags: #email, #work, #env-audit
- Related files automatically populated

---

### Example 2: ATL01A Site Email

**Email Subject**: "ATL01A - Generator Testing Schedule"

**Auto-Generated**:
- `para: Areas`
- `area: Site Operations Management`
- `site: ATL01A`
- Links to: ATL01A Site Hub, Jack Gillian Hub, David Nuckolls Hub
- Tags: #email, #work, #atl01a
- Related files include site hub

---

### Example 3: 1:1 Follow-Up Email

**Email Subject**: "Follow-up from our 1:1 - SOSPES observations"

**Auto-Generated**:
- `para: Areas`
- `area: Work Communications`
- Links to: David Nuckolls Hub
- Tags: #email, #work, #sospes, #meetings
- Detects people mentioned in content

---

## Advanced Customization

### Add Email Threading
Track email conversations by adding:

```handlebars
thread_id: "{{#if url}}{{url}}{{else}}[manual entry]{{/if}}"
in_reply_to: "[[Previous Email Subject]]"
```

### Add Priority Detection

```handlebars
priority: {{#if (contains title "URGENT" "ASAP" "CRITICAL")}}High{{else if (contains title "FYI")}}Low{{else}}Medium{{/if}}
```

### Add Sender Organization

```handlebars
sender_org: {{#if (contains author "stackinfra")}}STACK{{else if (contains author "anteagroup")}}Antea Group{{else}}External{{/if}}
```

### Add Email Type Classification

```handlebars
email_type: {{#if (contains title "Re:" "RE:")}}Reply{{else if (contains title "Fw:" "FW:")}}Forward{{else}}Original{{/if}}
```

---

## Workflow Integration

### 1. Clip Email from Outlook/Gmail
- Open email in browser
- Click Web Clipper extension
- Select "Work Email" template
- Click "Clip"
- Email saved to Obsidian

### 2. Process Email in Obsidian
- Review email content
- Extract action items (fill in checkbox section)
- Identify key points
- Add to relevant hub notes
- Link to related meetings or projects

### 3. Follow-Up Workflow
- Check off action items as completed
- Update related hub notes with outcomes
- Link response emails to original
- Archive when fully processed

---

## Tips for Success

### 1. Clean Up After Clipping
Web Clipper captures everything, including:
- Email signatures (usually unnecessary)
- Forwarded message headers (can be redundant)
- HTML formatting artifacts

**Solution**: Do a quick cleanup pass after clipping:
- Delete repetitive signatures
- Remove excess forwarded headers
- Keep only essential content

### 2. Extract Action Items Promptly
- Don't let action items sit in email format
- Extract to checkbox format immediately
- Assign owners and due dates
- Link to relevant project/hub files

### 3. Link Strategically
- Not every person mentioned needs a hub link
- Focus on key stakeholders
- Link to project/site hubs for context
- Over-linking is better than under-linking

### 4. Use Consistent Naming
When manually adding people/sites:
- Use exact hub names: `[[Jack Gillian Hub]]` not `[[Jack G]]`
- Use site codes: `ATL01A` not `Atlanta`
- Use project names: `2025 Environmental Audit` not `Audit Project`

### 5. Tag Thoughtfully
- Too many tags = tag fatigue
- Focus on: site codes, projects, people, topics
- Use tags for filtering/searching
- Review tag usage quarterly, consolidate as needed

---

## Maintenance

### Regular Reviews
**Weekly**:
- Review captured emails
- Ensure action items extracted
- Update related hubs with outcomes

**Monthly**:
- Check tag usage, consolidate similar tags
- Update template if new projects/sites added
- Archive completed email threads

**Quarterly**:
- Review auto-linking logic effectiveness
- Update PARA classification rules
- Clean up orphaned email notes

---

## Alternative: Simplified Version

If the full template is too complex, here's a minimal version:

```handlebars
---
para: Areas
document_type: Email
from: "{{author}}"
date: "{{date:YYYY-MM-DD}}"
subject: "{{title}}"
tags:
  - email
  - work
---

# Email: {{title}}

**From**: {{author}}
**Date**: {{date:MMMM DD, YYYY}}

---

{{content}}

---

## Action Items
- [ ] 

## Related To
- [[David Nuckolls Hub]]

---

*Clipped: {{time:YYYY-MM-DD HH:mm}}*
```

**Benefits**:
- Faster to process
- Less auto-magic, more manual control
- Easier to customize on-the-fly

---

## Troubleshooting

### Web Clipper Not Detecting Email
- Ensure you're on the email reading pane (not inbox list)
- Try refreshing the page
- Check Web Clipper has permission for email domain

### Auto-Links Not Working
- Verify hub names match exactly (case-sensitive)
- Check hub files exist in vault
- Use `[[Hub Name]]` format, not variations

### Wrong PARA Classification
- Review classification logic in template
- Add specific project keywords
- Default to Areas if unsure

### Too Much HTML Formatting
- Web Clipper settings: Choose "Readable" or "Simplified" content extraction
- Manually clean up after clipping
- Consider using email's "Print" view before clipping

---

## Integration with Existing Batches

### Links to Previous Work
This template auto-connects emails to your existing 10 hubs:
1. Rhett Hub (Personal)
2. Kelsey & Celebrations Hub (Personal)
3. Jesse Kenser Hub (Work Executive) ✓
4. Kate Hub (Work Executive) ✓
5. David Nuckolls Hub (Work Team) ✓
6. Matt Goetz Hub (Work Team) ✓
7. Matt Saucedo Hub (Work Team) ✓
8. 2025 Environmental Audit Project Hub (Project) ✓
9. 2025 EHS Performance Goals Hub (Area) ✓
10. ATL01A Site Hub (Area - Site) ✓

Plus new hubs as you create them (Jack Gillian, other sites, other COMs).

### Supports Ecosystem Replication
This template implements your Outlook → Obsidian migration from [[Ecosystem Replication]]:
- Outlook emails now captured in Obsidian
- Preserved with full context and metadata
- Linked to existing knowledge graph
- Action items extracted and tracked

---

## Summary

This Web Clipper template enables you to:
✅ Capture work emails directly into Obsidian
✅ Auto-classify with PARA methodology
✅ Auto-link to relevant hubs and projects
✅ Auto-tag for easy filtering and search
✅ Extract action items with checkboxes
✅ Preserve full context and metadata
✅ Integrate with your existing 80-file knowledge base

**Next Steps**:
1. Install Obsidian Web Clipper
2. Add this template
3. Customize for your specific needs
4. Start clipping important emails
5. Process weekly, archive monthly

---

*Template created: February 5, 2025*
*Compatible with: Obsidian Web Clipper v1.0+*
*Integrates with: PARA methodology, Hub architecture, Existing 80-file knowledge base*
