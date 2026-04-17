---
PARA: Area
Status: Done 🙌
Priority: Medium
type: cab-procedure-review
created: 2026-03-24T14:30:00
tags:
  - cab
  - procedure-review
Procedure ID:
Procedure Title:
Procedure Version:
Document Category:
Site:
Review Type:
Review Trigger:
Review Due Date: 2026-04-15
CAB Meeting Date: 2026-04-15
CAB Meeting Note:
Procedure Owner:
Subject Matter Expert:
Reviewer:
Management Approval:
CAB Decision:
Decision Date:
Next Review Date:
---

# East Region - Medium Risk CAB - 2026-04-15 Transcript

## Procedure Summary
> Brief description of what this procedure covers and its scope.

## Reason for Review
- 

## Changes Proposed / Under Review
| Section | Current Text | Proposed Change | Rationale |
|---------|-------------|-----------------|-----------|
| | | | |

## Reference Material Checked
- [ ] Regulatory/compliance references reviewed
- [ ] Related procedures cross-checked
- [ ] Previous version change history reviewed
- [ ] Site-specific requirements considered

## Review Notes


## Peer Review Feedback
- **Reviewer:**
- **Date:**
- **Findings:**

## CAB Discussion Summary
> Link to [[CAB Meeting - 2026-04-17]] for full context.

- **Decision:** 
- **Conditions / Stipulations:**
- **Effective Date:**

## Action Items
- [ ] 

## Revision History
| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| | | | |


Feedback from this weeks CAB. And attached transcript.

# Critical Operations (CritOps)

## East Region – Medium Risk CAB

### Meeting Review

**Meeting Title:** East Region Medium Risk CAB – Weekly Review  
**Date/Time:** April 15, 2026 (CAB for week of 4/16)  
**Attendees:**  
James Sedoruk (Chair), Justin Lloyd, Kaitlyn Lail, Nicholas Mansberger, Michael Gay, Colin Edris, Joe Kendra, David Nuckolls, Syed Abidi, others  
**Source:**

---

# Executive Summary

This was a **moderate-volume CAB with strong operational depth**, particularly in:

- **Electrical switching / ATS operations**
- **UPS / battery system remediation**
- **Large-scale IR scanning procedures**
- **Network failover validation**

### Key Outcomes

- All cases **approved (no holds)**
- Several **important risks surfaced but accepted or mitigated**
- Continued trend of:
    - **Strong SME engagement**
    - But **inconsistent pre-CAB readiness**

---

# Case Reviews

---

## 1. Case 174414 – NVAA 05A

### ATS House Annual PM (Generator Transfer + IR Scan)

**Decision:** ✅ Approved

---

## Key Risks Identified

- **Live transfer to generator under load**
- **Open cabinet IR scanning (arc flash exposure)**
- **Vesda / fire detection false alarms during generator run**
- **Potential generator auto-timeout mid-test**

---

## Strengths

- Clear step-by-step transfer sequences (screenshots = good practice)
- Pre/post UPS checks included
- Fire system coordination considered
- Generator runtime confirmed (no timeout issue)

---

## Action Items (Even Though Approved)

|Responsible|Action|
|---|---|
|Operations Team|Confirm **generator run mode does not auto-timeout** during evolution|
|Team|Ensure **fire alarm / Vesda coordination is executed** prior to generator run|
|Field Team|Validate **arc flash boundaries and PPE enforcement during open cabinet scans**|
|Team|Verify **elevator impact is communicated and controlled**|

---

## Leadership Take

👉 **Well-structured MOP, good control of electrical risk**

---

## 2. Case 181151 – NVAA 06A

### UPS Battery Cabinet Replacement (Remediation Work)

**Decision:** ✅ Approved

---

## Key Risks

- Multi-vendor interaction (Toshiba, Vertiv, Fire, Rigging)
- **Line tamer (sprinkler) interaction with energized equipment**
- Working on **live UPS infrastructure (even if on reserve)**
- Physical handling of **battery cabinet (heavy + energized systems nearby)**

---

## Key Discussion Point (Important)

> Joe challenged: _“Why is this medium risk?”_

Response:

- Classified as **Medium for visibility**, not risk

👉 This is a **policy/process inconsistency**

---

## Action Items

|Responsible|Action|
|---|---|
|Kait / Team|Ensure **strict vendor sequencing (Fire → Vertiv → Toshiba)** is enforced|
|Team|Verify **line tamer isolation + LOTO fully validated before work**|
|Operations|Maintain **continuous escort + fire watch during evolution**|
|Leadership|Re-evaluate **risk classification methodology (visibility ≠ risk)**|

---

## Leadership Take

⚠️ **Execution likely safe, but classification logic is flawed**

---

## 3. Case 168200 – NVAA 05A

### IR Scan – Data Hall 110 (Large Multi-System Evolution)

**Decision:** ✅ Approved

---

## Key Risks

- Extremely large scope:
    - PDUs, MDPs, RMDPs, FCWs, CCRP, etc.
- **Frequent cabinet openings (arc flash exposure)**
- **Manual source transfers (FCWs)**
- **Human error risk due to MOP size (~50+ pages)**

---

## Key Discussion Insight

Nick raised a **very strong point**:

> “52-page MOP increases risk of administrative error”

James response:

- Flow-based execution reduces that risk

👉 Both are right:

- Flow is good
- But **cognitive overload risk is real**

---

## Action Items

|Responsible|Action|
|---|---|
|Field Team|Strictly follow **breaker position verification before/after each scan**|
|Team|Ensure **picture capture + storage verification discipline**|
|Operators|Validate **BMS alarms during FCW source transfers**|
|Leadership|Consider future **modular MOP structure for large evolutions**|

---

## Leadership Take

⚠️ **Technically strong, but human factors risk is high**

---

## 4. Case 180390 – SVY 01 A/B

### Nexus Upgrade (Modius Impact)

**Decision:** ✅ Approved

---

## Key Risks

- **Modius tunnel outage (~5–10 min)**
- Cross-region dependency

---

## Action Items

|Responsible|Action|
|---|---|
|IT Team|Ensure **bridge coverage during change**|
|Ops|Confirm **site awareness of Modius outage**|
|Team|Validate **staffing during event window**|

---

## Leadership Take

👉 Routine / well-understood work

---

## 5. Case 181365 – NVAA 05A

### ISP Failover Test

**Decision:** ✅ Approved

---

## Key Risks

- Temporary loss of:
    - BMS / EPMS visibility
    - Internet connectivity
- Risk of:
    - **Failover not working during real maintenance event**

---

## Key Strength

- This is **proactive validation before a 6-hour ISP outage**

👉 This is **exactly the right behavior**

---

## Action Items

|Responsible|Action|
|---|---|
|Syed / IT|Confirm **bridge communication includes correct site personnel**|
|IT Team|Validate **failover AND failback behavior**|
|Ops|Confirm **visibility + comms during failover test**|

---

## Leadership Take

✅ **Strong operational foresight**

[2026.04.16 Weekly Medium CAB -EAST.docx](https://stackinfrastructure-my.sharepoint.com/personal/jsedoruk_stackinfra_com/Documents/Microsoft%20Teams%20Chat%20Files/2026.04.16%20Weekly%20Medium%20CAB%20-EAST.docx)