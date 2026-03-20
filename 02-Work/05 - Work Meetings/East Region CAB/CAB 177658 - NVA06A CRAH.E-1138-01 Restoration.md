Feedback

Below is the compliance review of:

**“CRAH.E-1138-01-1138 and CRAH.E-1217-01-1217 Isolation and Restoration – MOP”**

---

# **Issues Found**

---

## 1. Section 04 – Boilerplate Not Verbatim (Structural Non-Compliance)

Section 04 is required to match the approved “What Good Looks Like” boilerplate **verbatim**.

In this document, the structure is altered:

- The heading shows:
    

> **Section 04 – Detailed Procedure**

Followed by:

> **Pre-Maintenance Brief**

In the approved template, Section 04 must be titled **“Pre-Maintenance Brief”** and formatted exactly as the standard boilerplate section. Here, Section 04 is labeled as “Detailed Procedure,” which is a structural deviation.

This is a compliance issue because Section 04 is treated as a strict boilerplate verification section.

---

## 2. Duplicate Section Numbering – Section 06

The document contains:

- **Section 06 – Back-out Procedures**
    
- Followed again by:
    
    > **Section 06 – MOP Approval permission of site management.**
    

Section numbering must be sequential and correctly labeled. The second “Section 06” should be renumbered (likely Section 07). This is a structural compliance issue.

---

## 3. Electrical Hazard Present – No Live-Dead-Live (LDL) Verification Step

### Electrical hazards are explicitly identified:

Section 03 lists electrical energy sources with magnitudes:

> CRAH.E-1138-01-1138 Power Supply A and B Disconnects – Electrical – 0.31 cal/cm2  
> ERDP-P3-110 – Electrical – 0.89 cal/cm2

Additionally, Section 05 includes breaker and disconnect manipulation:

> “OPEN Power Supply B disconnect switch…”  
> “OPEN Power Supply A disconnect switch…”

Because:

- Electrical energy is identified in Section 03, **and**
    
- Electrical disconnects are operated in Section 05,
    

A **Verification of Hazardous Energy Isolation (Live-Dead-Live)** step is required prior to work execution.

No Live-Dead-Live table or voltage verification step is included anywhere in Section 05.

This is a **critical omission**.

---

## 4. Electrical Disconnect Manipulation Without PPE Donning Step

The procedure includes electrical manipulation steps such as:

> “OPEN Power Supply B disconnect switch…”  
> “CLOSE Power Supply A disconnect switch…”

However, Section 05 does **not** include a “Don PPE” step with an associated PPE table prior to operating these disconnects.

Per PPE verification rules:

- When manipulating electrical equipment (open/close disconnects), PPE **must be donned beforehand**.
    
- A PPE table must specify required arc-rated PPE when arc flash values are listed in Section 03.
    

Because arc flash magnitudes are defined (0.25–0.92 cal/cm²), and electrical equipment is operated, a PPE section is required prior to those steps.

This is a **compliance issue**.

---

## 5. LOTO Log Update Timing

During isolation steps, the procedure states:

> “Record LOTO Identifier: ______”

However, there is **no instruction immediately after applying LOTO devices** to update the LOTO log.

The only LOTO log reference appears at completion:

> “Update LOTO Log.”

Per rulebook requirements:

- When locks are applied, the procedure must require updating the LOTO log.
    
- When locks are removed, the procedure must require updating the LOTO log.
    

The application portion does not explicitly instruct updating the LOTO log.

This must be corrected.

**Required correction language:**

> Add the correct verbiage to update the LOTO log.

---

## 6. No Explicit Verification of Absence of Electrical Energy on CRAH.E-1138-01-1138

For CRAH.E-1138-01-1138, the procedure states:

> “Verify that Power Supply A and Power Supply B are both in the OFF position and the indicator lights are extinguished.”

Indicator light verification is **not equivalent** to a Live-Dead-Live test.

Because:

- Electrical hazards are listed in Section 03,
    
- Electrical disconnects are manipulated,
    
- LOTO is applied,
    

A formal absence-of-voltage verification step is required.

This is a **critical safety omission**.

---

# **Recommended Improvements**

---

## 1. Clarify Vendor Electrical Responsibility (If Applicable)

Vendors are performing inspection work. While this scope appears mechanical (Victaulic inspection), if vendors are exposed to electrical hazard boundaries during inspection, the procedure should clearly state whether:

- Electrical verification has been performed and documented, and
    
- Vendors are required to perform their own Live-Dead-Live (if applicable).
    

This is not clearly defined.

---

## 2. Improve Energy Isolation Clarity for CRAH.E-1138-01-1138

For CRAH.E-1138-01-1138, disconnects are verified OFF, but there is no explicit step stating they are OPENED during this procedure (unlike CRAH.E-1217-01-1217, which explicitly states OPEN).

Clarifying whether these are normally open, previously isolated, or require active operation would improve technical clarity and audit defensibility.

---

# **Summary of Critical Findings**

- Section 04 not verbatim compliant (structural issue)
    
- Duplicate Section 06 numbering
    
- Electrical hazard identified but **no Live-Dead-Live verification**
    
- Electrical disconnects operated with **no PPE donning step**
    
- LOTO log update not required at time of application
    
- Absence-of-voltage not formally verified
    

---

If corrected, this MOP can be brought into full compliance.

Please let me know if you would like a redline-style breakdown by page and step number for revision tracking.