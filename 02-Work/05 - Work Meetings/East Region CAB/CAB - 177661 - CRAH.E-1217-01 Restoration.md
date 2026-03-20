MOP: [NVA06A-MOP-Mechanical-Construction Support-CRAH-1217-01 Isolation and Restoration.docx](https://stackinfrastructure.sharepoint.com/:w:/r/sites/Operations/_layouts/15/Doc.aspx?sourcedoc=%7B91C13D55-606D-41BE-AC1A-3A7E3D0DCFA7%7D&file=NVA06A-MOP-Mechanical-Construction%20Support-CRAH-1217-01%20Isolation%20and%20Restoration.docx&action=default&mobileredirect=true)
JSA: [JSA - CRAH Isolation and Restoration.docx](https://stackinfrastructure.sharepoint.com/:w:/s/AMER-CriticalOperations/IQAsYFzATSBYSbLrt0GttVDlAbSaKJ-bOo5eMizvddmV6WI)


# MOP Feedback

Here is a structured compliance review of your uploaded procedure:  

---

# **Issues Found**

### **1. Missing Live-Dead-Live (LDL) Verification (Critical)**

- **Relevant Steps (Section 05 – Isolation of CRAH):**
    
    > “OPEN Power Supply B disconnect switch…”  
    > “OPEN Power Supply A disconnect switch…”
    
- **Issue:**  
    The procedure performs **electrical isolation of disconnect switches**, but there is **no Live-Dead-Live verification step** to confirm absence of voltage.
    
- **Rulebook Requirement:**  
    When electrical isolation occurs, LDL verification is mandatory prior to work.
    
- **Impact:**  
    This is a **critical safety omission**.
    

---

### **2. Missing Vendor LDL Requirement (Critical)**

- **Relevant Section:** Vendor inspection (Section 05, Section 3)
    
- **Issue:**  
    The procedure hands off equipment to the vendor but does **not require the vendor to perform their own Live-Dead-Live verification**.
    
- **Rulebook Requirement:**
    
    > Vendor must explicitly perform LDL when interacting with isolated electrical equipment.
    

---

### **3. PPE Not Donned Prior to Electrical Manipulation (Critical)**

- **Relevant Steps:**
    
    > “OPEN Power Supply B disconnect switch…”  
    > “OPEN Power Supply A disconnect switch…”
    
- **Issue:**  
    These are **electrical manipulation actions**, yet there is **no “Don PPE” step prior**.
    
- **Additional Issue:**  
    There is **no PPE table** defined anywhere in Section 05.
    
- **Rulebook Requirement:**
    
    - PPE must be donned **before any manipulation of energized equipment**
        
    - Each PPE section must include a **corresponding PPE table**
        

---

### **4. LOTO Log Update Missing During Application (Critical)**

- **Relevant Steps:**
    
    > “Apply LOTO to CHWS valve (21037)”  
    > “Record LOTO Identifier: ________”
    
- **Issue:**  
    While identifiers are recorded, there is **no instruction to update the LOTO log at the time of application**.
    
- **Note:**  
    A later step exists:
    
    > “Update LOTO Log.” (Section 6)
    
- **Deficiency:**  
    The rulebook requires log updates **when locks/tags are applied and removed**, not only at completion.
    
- **Required Fix:**  
    Add explicit instruction:  
    **“Add the correct verbiage to update the LOTO log.”**
    

---

### **5. Missing Group LOTO / Personal Lock Verification (Critical)**

- **Relevant Section:** Entire LOTO process
    
- **Issue:**  
    There is **no step requiring all personnel (including vendors) to apply personal locks/tags** or verification by the controller.
    
- **Rulebook Requirement (from template):**
    
    > “Controller must verify that each person… has applied a personal lock and tag… and must update the LOTO Log.”
    

---

### **6. Section 04 Boilerplate Deviations (Verbatim Requirement)**

Section 04 must match the template exactly. The following deviations were identified:

- **Deviation 1:**
    
    > “Complete Pre-maintenance brief with all personnel involved with this procedure.”  
    > **Template requires:**  
    > “...with all qualified and affected personnel, including vendors…”
    
- **Deviation 2:**
    
    > “Ensure the facility Electrical and Mechanical systems are in a normal lineup and no other work…”  
    > **Template requires exact phrasing:**  
    > “Facility Electrical and Mechanical systems are in a normal lineup. No other work…”
    
- **Deviation 3 (minor but still non-verbatim):**  
    Slight wording differences in multiple lines (e.g., punctuation, phrasing structure)
    
- **Issue:**  
    Section 04 is **not verbatim compliant** with the “What Good Looks Like” document
    

---

# **Recommended Improvements**

### **1. Clarify Electrical Risk Alignment**

- Section 03 includes:
    
    > “Risk of electric shock…”  
    > and a **Type and Magnitude table**
    
- This is compliant, but consider explicitly linking:
    
    - Electrical risks → specific steps in Section 05  
        This improves traceability.
        

---

### **2. Add Explicit PPE Continuity Language**

- Once PPE is donned (to be added), clarify that:
    
    - PPE remains in effect until restoration is complete  
        This avoids ambiguity during long procedures.
        

---

### **3. Improve Section Numbering Consistency**

- Multiple duplicated section labels:
    
    - “Section 5” appears multiple times for different activities
        
- While not a compliance violation, this can:
    
    - Cause confusion during execution
        
    - Lead to incorrect step referencing
        

---

# **Summary**

This procedure contains several **critical safety compliance gaps**, primarily:

- Missing **Live-Dead-Live verification**
    
- Missing **vendor LDL requirement**
    
- Missing **PPE before electrical manipulation**
    
- Incomplete **LOTO log usage during application**
    
- Missing **group LOTO verification**
    
- **Section 04 not verbatim compliant**
    

These issues should be addressed before approval or execution.

---

If you want, I can walk through exactly where to insert each missing step (LDL, PPE, LOTO log language) without rewriting your procedure.



# JSA Feedback

### Task / Hazard / Control Analysis (Derived from MOP)

|Step/Task|Hazard|Controls|PPE|
|---|---|---|---|
|Isolate CRAH in BMS (functional shutdown)|Unexpected unit operation / airflow changes|Verify unit is disabled and no automatic restart; confirm system stability before field work|Safety glasses, gloves|
|Close CHWS/CHWR valves (multiple locations)|Pressurized fluid release; pinch points|Slowly close valves; verify pressure conditions; maintain body positioning clear of valve path|Safety glasses, gloves|
|Open electrical disconnects (A & B)|Arc flash / electrical shock|Open disconnects using proper stance; apply LOTO; verify zero energy state with approved method|Arc flash suit, electrical gloves, safety glasses|
|Apply LOTO to valves and electrical sources|Stored energy / unexpected energization|Apply personal locks/tags; verify isolation (try-start or test); document LOTO IDs|Safety glasses, gloves|
|Remove CRAH panels|Sharp edges; dropped objects|Use proper tools; maintain control of panels; secure removed components|Cut-resistant gloves, safety glasses, hard hat|
|Perform visual inspection (Victaulic fittings)|Contact with energized components (if not isolated); ergonomic strain|Verify zero energy before inspection; maintain safe posture; no tools applied per MOP|Safety glasses, gloves|
|Drain system (if failed inspection)|Glycol exposure; slips; pressure release|Use controlled draining methods; contain fluids; stage spill kit; follow SDS|Safety glasses, gloves|
|Repair Victaulic couplings|Pinch points; tool-related injuries|Use proper torque tools; follow manufacturer torque limits; maintain hand placement awareness|Gloves, safety glasses|
|Pressure testing (air + hydro)|Line rupture; stored pressure release|Use calibrated gauges; increase pressure gradually; maintain exclusion zone|Safety glasses, gloves|
|Glycol transfer setup and pumping|Chemical exposure; hose failure; spills|Verify hose connections; stage spill kit; monitor transfer continuously|Safety glasses, gloves|
|Restore valves (throttling open)|Water hammer; pressure surge|Open valves slowly; coordinate with system monitoring personnel|Safety glasses, gloves|
|Remove LOTO and re-energize CRAH|Arc flash; unexpected startup|Remove LOTO per procedure; verify system readiness; stand clear during energization|Arc flash PPE, safety glasses|
|Restore system in BMS|Unexpected system response|Confirm stable operation post-startup; monitor alarms|Safety glasses|

---

## Gap Analysis and Recommendations

### ⚙️ Observations

- The JSA captures **some key hazards** (electrical shock, arc flash, fall from height, glycol exposure).
    
- The MOP includes **significantly more detailed physical work steps** than reflected in the JSA.
    
- Overall, the JSA is **incomplete and under-representative of actual task risk exposure**.
    

---

### ⚠️ Missing or Incomplete

**1. Major task coverage gaps (not in JSA):**

- Valve isolation and throttling (multiple steps)
    
- Full LOTO application and verification
    
- Panel removal
    
- Pressure testing (air + hydro)
    
- Drain and repair activities
    
- System restoration (valves + electrical re-energization)
    

👉 These are **high-risk activities** present in the MOP but absent in the JSA.

---

**2. Electrical safety incomplete**

- JSA only references “opening breaker” and general shock hazard
    
- Missing:
    
    - Dual power sources (A & B disconnects)
        
    - Verification of zero energy
        
    - Re-energization hazards
        

---

**3. Mechanical / pressure hazards missing**

- No mention of:
    
    - Stored pressure in hydronic lines
        
    - Risk of rupture during testing
        
    - Water hammer during restoration
        

---

**4. LOTO not explicitly treated as a task**

- JSA mentions LOTO in a control, but:
    
    - Not treated as a **critical step with its own hazards**
        
    - Missing verification requirement
        

---

**5. Incomplete controls (too generic)**  
Examples:

- “Wear arc flash gear” → lacks:
    
    - Approach boundaries
        
    - Verification of de-energization
        
- “Ensure de-energized” → no validation method
    

---

**6. PPE alignment gaps**

- JSA includes arc flash PPE globally, but:
    
    - Does not differentiate when it is required vs not
        
    - Missing consideration for:
        
        - Pressure testing (face shield recommended)
            
        - Drain/chemical exposure escalation
            

---

### 💡 Recommendations

- **Expand JSA task list** to align with MOP sequence:
    
    - Isolation (mechanical + electrical)
        
    - LOTO application
        
    - Inspection
        
    - Drain/repair/testing (conditional path)
        
    - Glycol transfer
        
    - Restoration (mechanical + electrical)
        
- **Add missing hazard categories:**
    
    - Stored pressure / line rupture
        
    - Water hammer
        
    - Pinch points (valves, couplings)
        
    - Dropped objects (panel removal)
        
- **Strengthen controls with specificity:**
    
    - “Apply LOTO and verify zero energy with approved test method”
        
    - “Open/close valves slowly to prevent pressure surge”
        
    - “Establish exclusion zone during pressure testing”
        
- **Separate critical steps:**
    
    - Treat **LOTO**, **pressure testing**, and **re-energization** as independent steps
        
- **Refine PPE application:**
    
    - Use task-based PPE instead of global listing
        
    - Ensure arc flash PPE tied specifically to energized work exposure
        

---

### ✅ Summary

- The current JSA is **partially aligned but significantly incomplete** relative to the MOP.
    
- Key risks—especially **pressure, mechanical, and restoration hazards**—are not adequately addressed.
    
- Updating the JSA to reflect the full task sequence will materially improve safety coverage and audit readiness.
    

---

**Disclaimer:**  
This JSA Aid provides general guidance based on the provided information and a standard hazard–control reference. It does not replace competent supervision, required permits, site-specific procedures, or regulatory requirements.