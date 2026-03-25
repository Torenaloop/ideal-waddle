---
type: email
sender: Reid Thomas
sender_email:
recipient:
date: 2026-03-25
subject: AP UPDATE - Operational Risk Classification Standard Now in Effect
priority:
  - High
status: published
tags:
  - email
  - CAB
  - APUpdates
projects:
action_items:
due_date:
---
## Outlook CoPilot Prompt 
- "Can you turn this into a flow chart that calls out what different roles need to do in chronological order"
- ![[Pasted image 20260325121628.png]]
## Email Details

**From:** {{Reid Thomas}}
**To:** {{recipient}} -> All of Mike Casey's org?
**Date:** 2026-03-25
**Subject:** {{AP UPDATE - Operational Risk Classification Standard Now in Effect}}

---

## Email Content


# ✅ **Summary: STACK AMER–Operational Risk Classification Standard (AP)**

This standard defines **how operational risk is evaluated and classified** for maintenance and operational activities at STACK AMER sites. The goal is to ensure work is performed safely and without compromising system **availability**, **redundancy**, or **client uptime**.

## **1. Purpose of the Standard**

- Establish a consistent method for identifying and assigning **risk levels** to site work.
- Ensure risks are properly escalated and reviewed (CAB, EHS, leadership).
- Protect critical infrastructure supporting **client IT loads**.

## **2. Core Concept: Redundancy Drives Risk**

The document details how **electrical and cooling redundancy states** (N, N+1, 2N, etc.) influence risk classification.

### **Key redundancy principles:**

- Impaired or partially functional equipment **cannot** be counted as redundant.
- Redundancy is initially based on **design**, but may be temporarily adjusted using validated **load-based conditions**.
- When uncertainty exists, always apply the **higher risk level**.
- Intentional transfer of live client load is **automatically HIGH RISK**, regardless of redundancy.

## **3. Redundancy State Definitions**

### **Electrical Systems**

- **N:** Single path supporting load; failure causes impact.
- **N+1:** One spare component/path.
- **2N:** Two fully independent systems.

### **Cooling Systems**

- **N:** No spare cooling capacity.
- **N+1:** One redundant cooling component.
- **2N:** Two fully independent cooling paths.

## **4. Risk Classification Rules**

Activities are classified into **Baseline, Low, Medium, or High Risk**, depending on redundancy, system impact, and work scope.

### ✅ **Baseline Risk**

- Administrative or non-impactful work.
- No breaker/valve manipulation, no LOTO, no lineup change.

### ✅ **Low Risk**

- Single-source LOTO that does **not** change system lineup.
- Cooling redundancy remains **N+2 or greater**.
- Work is isolated and does not affect critical paths.

### ✅ **Medium Risk**

- Reduces system redundancy to **N+1** at any point.
- Isolation or manipulation of live systems supporting load.
- Cross-system coordination where failure would reduce redundancy.
- Firmware/logic/configuration changes affecting system behavior.

### ✅ **High Risk**

- Reduces redundancy to **N** (single-threaded).
- Any **intentional load transfer** within electrical topology.
- MV work, energized work, CSE, crane/lifts.
- Actions that create Single Points of Failure affecting multiple suites or sites.

## **5. Notification Requirements**

- **EHS review** is required for all **Medium and High Risk** activities prior to CAB.
- Work impacting **utility metering, MV loops, or billing paths** must be reviewed by TechOpsUtilityBillingSupport before CAB.

## **6. Major Risk Threshold Rules**

- **Electrical:**
    
    - N+1 = **Medium Risk**
    - N = **High Risk**
    - All load transfers = **High Risk**
- **Cooling:**
    
    - N+2 or better = **Low Risk**
    - N+1 = **Medium Risk**
    - N = **High Risk**

## **7. Additional Guidance**

The document emphasizes:

- Always classify based on the **lowest redundancy state** during any phase of work.
- Redundancy cannot be downgraded using load-based adjustments if equipment is impaired or conditions are unclear.
- Contingency/back-out plans must be validated for Medium/High Risk work.

## **8. Appendices & References**

Includes definitions (Glossary), version history, document approval, and references to related Administrative Policies:

- Critical Operations Procedure Program
- Maintenance Program Standards
- CAB Standards

If you’d like, I can also:  
✅ Create a **1-page summary**  
✅ Generate a **training slide deck**  
✅ Turn this into a **flowchart** or **quick reference guide**  
✅ Help you apply this classification to a specific maintenance activity

---

## Action Items

- [ ] 

---

## Notes & Context

[Add any additional thoughts, context, or related information]

---

## Related Links



All information is sourced directly from the file content you uploaded.

