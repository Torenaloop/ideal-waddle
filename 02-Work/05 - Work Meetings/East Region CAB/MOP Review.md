Based on review of **TX-P2-160 Oil Gauge Replacement – MOP** , the procedure **partially aligns** with a typical Control of Hazardous Energy (Lockout/Tagout) Administrative Procedure (AP), but it contains several compliance gaps and clarity issues that would likely prevent full compliance with a formal LOTO AP and OSHA 29 CFR 1910.147 / NFPA 70E requirements.

Below are audit-style findings.

---

## **Section 01 – MOP Overview**

**Finding:** Scope describes isolation strategy but does not clearly define the full hazardous energy boundary for TX-P2-160.  
**Recommendation:**

- Explicitly identify **all energy sources** (primary, secondary, control power, backfeed, stored energy, induced voltage, and generator sources).
    
- Include a clearly defined **Energy Control Boundary statement** consistent with the LOTO AP.
    

---

## **Section 03 – Risk & Safety Requirements**

**Finding 1:** Arc flash incident energy values are provided, but no reference to the governing study revision or labeling verification.  
**Recommendation:**

- Reference the current Arc Flash Study revision date to confirm alignment with NFPA 70E.
    
- Confirm PPE category selection aligns with the listed cal/cm² values.
    

**Finding 2:** Only electrical energy is listed. No stored mechanical, thermal, or pressure hazards are addressed (e.g., oil pressure, stored spring energy in switches).  
**Recommendation:**

- Add all forms of hazardous energy per OSHA 1910.147(b) definition.
    

---

## **Section 04 – Pre-Maintenance Brief**

**Finding:** LOTO roles are defined (Controller, Qualified Persons), which aligns with typical AP structure; however, there is no explicit requirement to:

- Verify employee authorization level
    
- Confirm affected employee notification documentation
    
- Perform periodic inspection validation (if required by AP)
    

**Recommendation:**

- Add a step requiring verification that all personnel applying locks are **Authorized Employees under the LOTO AP**.
    
- Add explicit affected employee notification documentation language.
    

---

## **Section 05 – Detailed Procedure**

### **A. Control Power Isolation (Panel 1ULPA8 – CKT #7)**

**Finding:**  
LOTO is applied to control power early in the procedure but is removed during re-energization before upstream primary energy sources are fully restored.

**Compliance Risk:**  
Potential violation of sequential re-energization requirements under most LOTO APs.

**Recommendation:**

- Clarify sequence: control power should only be restored after all upstream isolation devices are returned to normal configuration and all personnel are clear.
    

---

### **B. Generator Transfers Prior to LOTO**

**Finding:**  
The procedure transfers all lineups to generator prior to isolation. This is operationally sound but creates a dual-source environment during switching.

**Compliance Concern:**  
The document does not explicitly state that generator sources are considered hazardous energy sources subject to LOTO verification.

**Recommendation:**

- Add explicit statement that generator output breakers are part of the hazardous energy isolation plan.
    
- Clarify whether MSB primary LOTO at P2-160 sufficiently isolates generator backfeed risk.
    

---

### **C. Isolation of U3-MVS-02 and U4-MVS-02**

**Finding 1:**  
Way switches are opened, grounded, locked, and placed in group lockbox — this aligns with group LOTO practices.

**Finding 2 (Critical):**  
No **documented verification of absence of voltage at the point of work after all isolation steps are complete**, prior to gauge replacement.

Although non-contact testing is performed at TX-P2-160 test ports, this is done **before confirmation that all upstream isolation steps are complete**, and no adequately rated contact meter test is documented.

**Compliance Risk:**

- NFPA 70E requires an adequately rated test instrument to verify absence of voltage.
    
- Many LOTO APs prohibit sole reliance on non-contact voltage testers.
    

**Recommendation:**

- Require properly rated contact voltage tester verification phase-to-phase and phase-to-ground.
    
- Include instrument rating verification step.
    
- Require test-before-touch immediately prior to beginning oil gauge work.
    

---

### **D. Group Lockbox Process**

**Finding:**  
Keys are placed in group lockbox; however:

- No step requires each Authorized Employee to verify zero energy prior to applying their personal lock.
    
- No documented verification that all personal locks are removed prior to re-energization beyond general instruction.
    

**Recommendation:**

- Add formal **Group LOTO verification step**.
    
- Add a documented “All Clear Verification” prior to removal of last lock.
    

---

### **E. Stored Energy / Transformer Secondary**

**Finding (Major Gap):**  
The procedure does not address:

- Transformer secondary induced voltage
    
- Capacitive coupling
    
- Stored charge bleed-down time
    
- Oil expansion pressure or mechanical hazard
    

**Recommendation:**

- Add minimum wait time or discharge verification if required by your LOTO AP.
    
- Confirm grounding method satisfies AP and NFPA 70E requirements.
    

---

### **F. Re-Energization Sequence**

**Finding:**  
LOTO removal is fragmented (e.g., removal of personal locks at multiple points in procedure).

**Compliance Risk:**  
Potential violation of standard LOTO AP sequence requiring:

1. Work area inspection
    
2. Tool removal verification
    
3. Guard replacement
    
4. Affected employee notification
    
5. Removal of personal locks
    
6. Removal of group lock
    
7. Re-energization
    

**Recommendation:**

- Consolidate re-energization steps into a clearly defined **LOTO Release Procedure** section aligned to the LOTO AP.
    

---

## **Section 06 – Back-Out Procedure**

**Finding:**  
Back-out steps address operational recovery but do not specify how hazardous energy isolation is maintained during abnormal condition response.

**Recommendation:**

- Clarify that LOTO remains in place unless COM authorizes controlled re-energization per AP.
    

---

# Overall Compliance Determination

|Area|Compliance Status|
|---|---|
|Group LOTO Structure|Generally aligned|
|Lock Application|Aligned|
|Zero Energy Verification|**Not fully compliant**|
|Generator Hazard Recognition|Partially compliant|
|Stored Energy Consideration|Not addressed|
|Re-Energization Sequence|Needs improvement|
|OSHA 1910.147 Alignment|Partial|
|NFPA 70E Absence of Voltage|**Insufficiently documented**|

---

# Final Determination

**This MOP does NOT fully comply with a comprehensive Control of Hazardous Energy (LOTO) Administrative Procedure.**

Primary deficiencies:

1. Inadequate documented absence-of-voltage verification method.
    
2. Incomplete hazardous energy identification.
    
3. Re-energization sequence lacks formal structured release process.
    
4. Generator source treatment not clearly integrated into energy control boundary.
    
5. Stored/induced energy not addressed.
    

---

If you would like, I can:

- Crosswalk this MOP directly against your specific LOTO AP (if uploaded), or
    
- Provide a redlined version with corrective language inserted inline for compliance.