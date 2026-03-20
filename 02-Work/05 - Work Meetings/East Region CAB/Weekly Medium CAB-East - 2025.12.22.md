---
Date: 2025-12-22
Time: 14:30
Location:
Work Person:
tags:
---
**Critical Operations (CritOps)**

**East Region – Medium Risk CAB**

**Meeting Minutes**

**Meeting Title:** East Region Medium Risk CAB – Weekly Review  
**Date/Time:** December 22, 2025, 7:14 PM  
**Attendees (as captured):**  
James Sedoruk, Austin Greenbacker, Ruslan Shafagatov, Gerald Aldajuste, Spencer Lecheler, Bryan Day, Joe Kendra, Justin Lloyd, James Crane  
**Additional attendees:** Not Provided  
**Meeting Type:** Regular Weekly Medium-Risk CAB Session

---

**Meeting Summary**

The CAB reviewed a single work activity involving RPP overutilization alarms and required troubleshooting for NVA 02E. The session followed the revised CAB approach, emphasizing a high-level operational walkthrough rather than line-by-line procedural review. During discussion, the work was reclassified from Medium to High Risk due to temporary single-sourcing at the rack level. Required procedural updates, documentation corrections, and escalation to High CAB were identified and agreed upon prior to execution.

---

**Topics Discussed**

---

**1. CAB Review Approach Alignment**

**Discussion Summary**

- James reiterated the transition away from line-by-line MOP reviews toward **high-level explanations of work scope, intent, and execution method**.
- The objective is to ensure shared understanding, highlight risks, and confirm leadership awareness rather than re-reviewing previously approved procedural steps.
- Attendees agreed this approach improves efficiency and clarity.

---

**2. Case 168470 – NVA 02E**

**RPP P316 TAC 01 / TAC 03A**

**Overutilization Alarms – Troubleshooting & Repairs**

**Presenters:** Austin Greenbacker (summary), Ruslan Shafagatov (procedure walkthrough)

**Discussion Summary**

- Following energization of branch circuits, the RPP began reporting **sporadic and inflated amperage readings**, triggering repeated overutilization alarms at both branch and main breaker levels.
- Upstream CDP feeder readings remained stable, indicating a likely **RPP internal issue** (suspected control board or ribbon cable).
- Vendor troubleshooting will require **de-energizing the RPP**, connecting diagnostic equipment, and potentially replacing components during the same outage window.

**Operational Approach (High-Level)**

- Two-team execution model:

- **Team A (Red Zone):** Customer-facing, rack verification, branch breaker operations.
- **Team B (Gallery):** Feeder breaker isolation, lockout/tagout.

- Steps include:

- Recording initial breaker positions.
- Verifying rack stability and alternate source availability.
- Sequentially opening branch breakers under customer direction.
- Isolating upstream feeder breaker and applying LOTO (STAC + vendor).
- Performing live–dead–live testing with vendor signoff.
- Handing off RPP to vendor for diagnostics/repairs.
- Re-energization following reverse order with rack-by-rack verification.

**Risk Classification Discussion**

- Despite rack-level redundancy, isolating the RPP results in **temporary single sourcing**, creating elevated exposure if a secondary failure occurs.
- James confirmed alignment with Spencer: the activity must be treated as **High Risk**, requiring escalation to High CAB for leadership visibility.

**PPE & Safety Clarifications**

- Corrected PPE classification at the RPP: **Category 1**, not 40 cal.
- Vendor PPE compliance is enforced operationally; vendor signature required for live–dead–live testing.
- Ladder permit and High-Risk warning statement must be added per AP requirements.

**Load Verification Discussion**

- Traditional before/after load logging is not effective due to battery discharge behavior of power shelves.
- Stability verification will rely on **rack-by-rack walkthroughs with the customer**, confirming alternate source availability and no service impact.

---

**3. Documentation & Process Corrections**

**Discussion Summary**

- NetSuite case linked to an incorrect version of the MOP; correct version must be uploaded and linked.
- Warning statement placement clarified: should appear **immediately before critical power-transfer steps**, not only at the document header.
- High Risk designation requires additional approvals and warning language per the AP.

---

**Consolidated Action Items Table**

|   |   |   |   |   |
|---|---|---|---|---|
|**#**|**Responsible Party**|**Action Required**|**Related Case / Topic**|**Due Date**|
|1|Austin Greenbacker|Update NetSuite case to link the correct MOP version|Case 168470|Immediate|
|2|Austin Greenbacker / Ruslan Shafagatov|Reclassify work from Medium to **High Risk** in documentation|Case 168470|Immediate|
|3|Austin Greenbacker|Add required **High Risk warning statement** at appropriate procedural step(s)|Case 168470|Before High CAB|
|4|Austin Greenbacker|Add ladder permit to supporting documents|Case 168470|Before High CAB|
|5|Ruslan Shafagatov|Correct PPE designation at RPP (Category 1, not 40 cal)|Case 168470|Before approval|
|6|Team|Add vendor **live–dead–live signature requirement** to MOP|Case 168470|Before approval|
|7|Austin Greenbacker|Notify Joe and James once updates are complete for approval|Case 168470|Upon completion|
|8|James Sedoruk|Approve updated MOP in Playbook and mark ready in NetSuite|Case 168470|After updates|
|9|James Sedoruk / Team|Present case at High CAB (scheduled for next day)|High CAB Escalation|As scheduled|

---


# Agenda



# Notes



# Follow-up Tasks


