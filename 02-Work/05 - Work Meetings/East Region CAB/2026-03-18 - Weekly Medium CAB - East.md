---
type: meeting
status: active
created: 2026-03-18
updated: 2026-03-18
meeting_date: 2026-03-18
participants: []
project:
tags: []
---

![[Pasted image 20260318081046.png]]

## Pending this week

## ⏹️168200 | NVA05A |  IR Scan-DH110 APM

- MOP: [ChatGPT - Safety Procedure Reviewer](https://chatgpt.com/g/g-690238d8e798819193744fe297b52661-safety-procedure-reviewer/c/69bae688-a980-8328-9aab-395ac50e884d)
- JSA: [ChatGPT - JSA Copilot](https://chatgpt.com/g/g-6914a910faf88191afb16c926d399378-jsa-copilot/c/69bae750-6214-8331-ab09-e3ff8dcd2c2b)

## ✅ 177443 | NVA06A | FTE of U3-MVS-2 and U4-MVS-01 - Gerald has reviewed and closed in Asana

## ⏹️177661 | NVA06A | CRAH.E-1217 - 01 Restoration

MOP: [ChatGPT - Safety Procedure Reviewer](https://chatgpt.com/g/g-690238d8e798819193744fe297b52661-safety-procedure-reviewer/c/69baebf5-ee38-8327-a6bb-1eebcf7283ec) 
JSA: [ChatGPT - JSA Copilot](https://chatgpt.com/g/g-6914a910faf88191afb16c926d399378-jsa-copilot/c/69baebe6-3a40-832f-8137-4534a04c2c72)

--- 
**Issues Found**

---

**1. Section 04 – Boilerplate Deviation (Verbatim Mismatch)**

Per review requirement, **Section 04 must match the “What Good Looks Like” document verbatim**, and only boilerplate alignment is evaluated here.

**🔎 Deviation Identified:**

In your procedure (Section 04 – Pre-Maintenance Brief), the following text appears:

> “Complete Pre-maintenance brief with all personnel involved with this procedure.”

However, the approved template states:

> “Complete Pre-maintenance brief with all qualified and affected personnel, including vendors involved with this procedure.”

The omission of **“qualified and affected”** and **“including vendors”** is a deviation from the required boilerplate language.

📌 **Issue:** Section 04 does not match the approved template verbatim.  
This must be corrected to align exactly with the “What Good Looks Like” document.

---

**2. PPE Not Donned Prior to Electrical Manipulation**

Section 03 identifies electrical hazards with magnitudes up to:

- “ERDP-P5-210 – Electrical – 0.92 cal/cm2”  
    
- “ERDP-P3-110 – Electrical – 0.89 cal/cm2”  
    

Section 05 includes active breaker and disconnect manipulation steps, including:

> “OPEN Power Supply B disconnect switch to remove secondary source.”  
> “OPEN Power Supply A disconnect switch to remove primary source.”  
> “CLOSE Power Supply A disconnect switch.”  
> “CLOSE Power Supply B disconnect switch.”

These are **electrical manipulation steps**, not verification-only actions.

However:

- There is **no “Don PPE” step**  
    
- There is **no PPE table**  
    
- There is **no indication of arc-rated or electrical PPE prior to operating disconnects**  
    

**Rulebook Requirement:**

When manipulating electrical equipment (open/close breakers or disconnects), PPE must be donned beforehand and supported by a PPE table.

📌 **Issue:** Electrical disconnects are operated without a preceding “Don PPE” instruction and without a PPE table defining required equipment.

This is a compliance deficiency.

---

**3. Missing Live-Dead-Live (LDL) Verification**

This procedure performs a full electrical isolation:

- Disconnect switches opened  
    
- Power supplies verified OFF  
    
- Indicator lights checked  
    

However, there is **no Live-Dead-Live verification step** prior to vendor work.

The template requires:

> “Verify the absence of Energy by performing a Live-Dead-Live prior to execution of work.”

There is also no instruction to:

- Test A→B, A→C, etc.  
    
- Perform meter verification  
    
- Compel vendor LDL verification  
    

Because this procedure involves:

- Electrical isolation  
    
- Opening disconnects  
    
- Servicing equipment  
    

📌 **Issue:** Required Live-Dead-Live verification is missing prior to vendor inspection.

This is a **critical safety omission**.

---

**4. Vendor LDL Responsibility Not Stated**

Vendor work is performed:

> “Handoff equipment to Vendor for inspection of Victaulic fittings…”

However, the procedure does **not** include:

- “Compel Vendor to Verify the absence of Energy.”  
    
- Vendor LDL verification signature  
    
- Explicit requirement for vendor to perform their own LDL  
    

When vendors perform work after electrical isolation, the procedure must explicitly state their responsibility to perform LDL.

📌 **Issue:** Vendor LDL responsibility is not documented.

---

**5. LOTO Log Update – Restoration Section (Compliant)**

The procedure includes:

> “Update LOTO Log.”

This satisfies the rule requiring a log update during LOTO release.

✔ No issue here.

---

**6. Live-Dead-Live Table Presence**

There is **no LDL table included at all** in Section 05.

Per review rule:

- A blank LDL table is acceptable.  
    
- Omission of the LDL section entirely when electrical isolation is performed is **not acceptable**.  
    

📌 **Issue:** LDL section and test point table are missing.

---

**Recommended Improvements**

---

**1. Clarify Electrical Isolation for CRAH.E-1138-01-1138**

For CRAH.E-1138-01-1138, the procedure states:

> “Verify that Power Supply A and Power Supply B are both in the OFF position…”

But it does **not** explicitly state to OPEN the disconnects prior to this verification (unlike the 1217 unit).

For clarity and audit defensibility, consider explicitly documenting:

- OPEN Power Supply A  
    
- OPEN Power Supply B  
    
- Apply LOTO (if required by site practice)  
    

This avoids ambiguity in the isolation sequence.

---

**2. Vendor Scope Typographical Error**

Under:

**CRAH.E-1138-01-1138 Vendor Inspection**

The procedure states:

> “Handoff equipment to Vendor for inspection of Victaulic fittings on CRAH.E-1217-01-1217.”

This appears to reference the wrong equipment.

📌 Recommend correcting equipment reference for accuracy.

---

**Summary of Compliance Status**

**Critical Safety Deficiencies:**

- ❌ Missing Live-Dead-Live verification  
    
- ❌ No PPE donning prior to electrical manipulation  
    
- ❌ No PPE table  
    
- ❌ Vendor LDL responsibility not documented  
    
- ❌ Section 04 boilerplate mismatch  
    

These items require correction before the procedure can be considered compliant.

## ⏹️177804 | NVA06A | Drywall Remediation in DH 110

### MOP: [ChatGPT - Safety Procedure Reviewer](https://chatgpt.com/g/g-690238d8e798819193744fe297b52661-safety-procedure-reviewer/c/69baea9f-fe98-8331-bdf1-7153641c47a8)
### JSA:  [ChatGPT - JSA Copilot](https://chatgpt.com/g/g-6914a910faf88191afb16c926d399378-jsa-copilot/c/69baeab6-18b0-8329-984d-d6288ebf6083)


