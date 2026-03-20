Feedback:

**Document Reviewed:** NVA06A-MOP – TX-HOUSE Kirk Key Installation

---

# **Issues Found**

---

## 1. Missing Explicit LOTO Log Update After Each LOTO Application (Critical)

Throughout Section 05, multiple LOTO applications are performed, for example:

- “Place LOTO on breaker ATS-1CHDP1-FB.”
    
- “Place LOTO on breaker 1HDP1-MCB.”
    
- “Apply LOTO to the MSB-P3-110-GB.”
    
- “Place LOTO on breaker MSB-P3-110-UB.”
    
- “Place LOTO on load break switch U1-01-3.”
    

Each location includes:

> “Record LOTO identifier # ______”

However, the procedure does **not consistently instruct personnel to update the LOTO Log immediately after applying each lock**, as required by the rulebook.

The only global reference appears at the end:

> “Update LOTO Log.”

### Why this is non-compliant:

Per LOTO Identifier Tracking requirements:

- When locks are applied, the procedure must explicitly require updating the LOTO Log.
    
- Log updates cannot be deferred to the end of the procedure.
    

### Required Correction:

After each LOTO application step, add the required instruction:

> **“Add the correct verbiage to update the LOTO log.”**

This applies to:

- ATS-1CHDP1-FB
    
- 1HDP1-MCB
    
- MSB-P3-110-GB
    
- MSB-P3-110-UB
    
- U1-01-3 load break switch
    

This is a **critical compliance deficiency**.

---

## 2. Live-Dead-Live (LDL) Verification – Vendor Responsibility Stated (Compliant) but Missing Internal Verification Confirmation

Under:

> “Vendor will open the SECONDARY side door and using a ‘Pumpkin Head’ voltage (<1000v) non-contact tester, test for zero voltage.”

And:

> “Vendor will open PRIMARY side door and using a ‘Pumpkin Head’ high voltage non-contact tester, test for zero voltage.”

A Live-Dead-Live test table is included (Live → Test Points → Live), which is correct and compliant.

However:

- The procedure does not explicitly state that the vendor must perform their own **Live-Dead-Live verification using an adequately rated meter** before work begins.
    
- It relies on a non-contact tester reference.
    

### Why this is non-compliant:

For vendor-performed LDL:

- The procedure must clearly require the vendor to perform their own LDL verification.
    
- The presence of a table is compliant, but the responsibility statement must be explicit.
    

### Required Clarification:

Add explicit language such as:

> “Vendor shall perform and document Live-Dead-Live verification prior to beginning work.”

Vendor PPE documentation is **not required**, and its absence is compliant.

---

## 3. Medium Voltage Switching – PPE vs. Hazard Table Alignment (Critical PPE Concern)

Section 03 lists:

> TX-HOUSE (Secondary) – **124.4 cal/cm²**  
> TX-HOUSE (Primary) – **19.1 cal/cm²**  
> U1-MVS-01 (U1-01-3) – **38 cal/cm²**

However, during Medium Voltage switching (e.g., U1-MVS-01 operations), PPE tables consistently specify:

> “40 Cal/cm2 Arc-rated clothing”  
> “40 Cal/cm2 arc flash suit hood”

### Why this is non-compliant:

If the secondary exposure is **124.4 cal/cm²**, a 40 cal/cm² suit does **not** match the magnitude listed in Section 03.

If 124.4 cal/cm² represents a direct exposure condition not applicable to switching position, this must be clarified in Section 03 (exposure condition column).

Currently:

- Hazard table shows 124.4 cal/cm².
    
- PPE listed is 40 cal/cm².
    
- No engineering control or boundary clarification is stated.
    

This creates a **mismatch between hazard magnitude and required PPE**.

This is a **critical PPE compliance issue** unless engineering controls or working distance assumptions are documented.

---

## 4. LOTO Release – Missing Explicit LOTO Log Update Before Removal

In the restoration section, LOTO devices are removed:

Examples:

- “Remove LOTO from MSB-P3-110-UB”
    
- “Remove LOTO from breaker MSB-P3-110-GB”
    
- “Remove LOTO from load break switch U1-01-3”
    
- “Remove LOTO from 1HDP1-MCB”
    
- “Remove LOTO from ATS-1CHDP1-FB”
    

There is no repeated instruction stating:

> Controller must update the LOTO Log prior to removal.

### Why this is non-compliant:

The rulebook requires explicit instruction to update the LOTO log before removing devices.

A single “Update LOTO Log” at the end does not satisfy release-stage documentation control.

### Required Correction:

Add log update instruction immediately before or after each LOTO removal.

---

## 5. Minor Documentation Control – U1-MVS-01 vs U2-MVS-01 Clarification

Isolation is performed at:

> “Proceed to U1-MVS-01.”

Restoration references:

> “Proceed U2-MVS-01.”

The overview states isolation occurs at:

> “U1-MVS-01 (U1-01-03)”

The involvement of U2-MVS-01 during restoration should be clarified in Section 01 overview to prevent confusion during field execution.

This is a documentation clarity issue.

---

# **Recommended Improvements**

---

## 1. Clarify Energy State During SKRU Key Transfers

The procedure includes multiple Kirk Key (SKRU) transfers and breaker manipulations.

Recommend adding a short clarifying statement:

> “Equipment remains energized during key transfer operations unless otherwise specified.”

This ensures operators understand energized status at all times.

---

## 2. Add STOP WORK Triggers During Critical Switching

For example:

> “WARNING: Opening the Utility Breaker is the critical step which will de-energize the MSB”

Recommend adding:

> “If breaker does not respond as expected, STOP WORK and notify COM.”

This strengthens procedural control during high-risk switching.

---

## 3. Consider Explicit Wait Times for MV Capacitive Discharge

After:

> “OPEN VFI switch by depressing the handle to the down position.”

There is no documented wait time before grounding and LDL.

If manufacturer guidance requires a discharge time, consider adding it.

---

# **Summary**

### Critical Issues:

1. Missing required LOTO log update instruction after each lock application.
    
2. Missing required LOTO log update instruction before each lock removal.
    
3. PPE mismatch with 124.4 cal/cm² hazard listing unless exposure clarification is added.
    
4. Vendor LDL responsibility not explicitly stated.
    

### Compliant Elements:

- Section 04 boilerplate matches approved template.
    
- Hazard magnitude table is present and properly structured.
    
- LDL test tables are included.
    
- LOTO identifiers are captured.
    
- Maintenance Mode (AMS) usage is clearly sequenced.
    
- Vendor involvement is defined.
    

---

This procedure is structurally strong and technically detailed, but the **LOTO documentation control and PPE alignment must be corrected before approval**.

---


If you would like, I can provide exact insertion language locations for the required LOTO log updates.

Understood. Below are the **exact insertion locations and required language** to bring the LOTO documentation into full compliance.

Document referenced: **NVA06A-MOP – TX-HOUSE Kirk Key Installation**

---

# 🔴 REQUIRED INSERTIONS — LOTO APPLICATION STAGE

For **each location below**, insert the required statement **immediately after the line where the LOTO is placed and the identifier is recorded.**

---

## 1️⃣ ATS-1CHDP1-FB

Current text:

> “Place LOTO on breaker ATS-1CHDP1-FB.”  
> “Record LOTO identifier. _____________”

### ✅ Insert immediately after:

> **Controller must update the LOTO Log with lock identifier, breaker designation, date, and personnel applying lock.**

---

## 2️⃣ 1HDP1-MCB

Current text:

> “Place LOTO on breaker 1HDP1-MCB.”  
> “Record LOTO identifier. _____________”

### ✅ Insert:

> **Controller must update the LOTO Log with lock identifier, breaker designation, date, and personnel applying lock.**

---

## 3️⃣ MSB-P3-110-GB

Current text:

> “Apply LOTO to the MSB-P3-110-GB.”  
> “Record LOTO identifier # _____________”

### ✅ Insert:

> **Controller must update the LOTO Log with lock identifier, breaker designation, date, and personnel applying lock.**

---

## 4️⃣ MSB-P3-110-UB

Current text:

> “Place LOTO on breaker MSB-P3-110-UB.”  
> “Record LOTO identifier # __________”

### ✅ Insert:

> **Controller must update the LOTO Log with lock identifier, breaker designation, date, and personnel applying lock.**

---

## 5️⃣ U1-01-3 Load Break Switch (Medium Voltage)

Current text:

> “Place LOTO on load break switch U1-01-3.”  
> “Record LOTO identifier # ________________”

### ✅ Insert:

> **Controller must update the LOTO Log with lock identifier, switch designation, date, and personnel applying lock.**

---

# 🔴 REQUIRED INSERTIONS — LOTO REMOVAL STAGE

For **each removal step**, the log must be updated **before device removal**.

Insert the required language **immediately BEFORE each “Remove LOTO…” instruction.**

---

## 6️⃣ MSB-P3-110-UB (Restoration Section)

Current text:

> “Remove LOTO from MSB-P3-110-UB”

### ✅ Insert immediately before:

> **Controller must verify all authorized personnel are clear and update the LOTO Log prior to removing this device.**

---

## 7️⃣ MSB-P3-110-GB

Current text:

> “Remove LOTO from breaker MSB-P3-110-GB.”

### ✅ Insert before removal:

> **Controller must verify all authorized personnel are clear and update the LOTO Log prior to removing this device.**

---

## 8️⃣ U1-01-3 Load Break Switch

Current text:

> “Remove LOTO from load break switch U1-01-3.”

### ✅ Insert before removal:

> **Controller must verify all authorized personnel are clear and update the LOTO Log prior to removing this device.**

---

## 9️⃣ 1HDP1-MCB

Current text:

> “Remove LOTO from 1HDP1-MCB.”

### ✅ Insert before removal:

> **Controller must verify all authorized personnel are clear and update the LOTO Log prior to removing this device.**

---

## 🔟 ATS-1CHDP1-FB

Current text:

> “Remove LOTO from ATS-1CHDP1-FB.”

### ✅ Insert before removal:

> **Controller must verify all authorized personnel are clear and update the LOTO Log prior to removing this device.**

---

# ⚠️ Why This Is Required

Per rulebook:

- LOTO log updates must occur at **each application**
    
- LOTO log updates must occur **prior to each removal**
    
- A single “Update LOTO Log” at the end of the procedure is not sufficient
    

These insertions bring the procedure into full compliance with:

- LOTO identifier tracking requirements
    
- Documentation control standards
    
- Group lock accountability requirements
    

---

If you would like, I can now:

- Provide exact vendor LDL clarification insertion language
    
- Or resolve the 124.4 cal/cm² PPE mismatch issue next
    

Let me know which you’d like to address.