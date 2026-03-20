MOP: [NVA05A-MOP-Electrical-Thermographic Survey-Thermal Scanning Gallery 109.111.docx](https://stackinfrastructure.sharepoint.com/:w:/r/sites/Operations/_layouts/15/Doc.aspx?sourcedoc=%7B146F554A-F614-4C5F-B75C-9A0EC43D5CF4%7D&file=NVA05A-MOP-Electrical-Thermographic%20Survey-Thermal%20Scanning%20Gallery%20109.111.docx&action=default&mobileredirect=true)
JSA: [Job Safety Analysis - NVA05A - Thermal Scanning DH110.docx](https://stackinfrastructure.sharepoint.com/:w:/s/AMER-CriticalOperations/IQCQ_jRGGJ-qQq1k1N32uFYqAbk116AvAXB7Zsc8MnNyd6w?e=rCvzEX)

# MOP Feedback

Here is a detailed compliance review of your uploaded procedure:

---

# **Issues Found**

### **1. Section 04 Boilerplate Deviations (Verbatim Requirement)**

Section 04 must match the approved template exactly. The following deviations were identified when compared to the “What Good Looks Like” document :

- **Deviation in personnel description:**
    
    - Procedure states:
        
        > “Complete Pre-maintenance brief with all personnel involved with this procedure including vendor personnel.”
        
    - Template requires:
        
        > “Complete Pre-maintenance brief with all qualified and affected personnel, including vendors involved with this procedure.”
        
- **Deviation in system readiness statement:**
    
    - Procedure states:
        
        > “Ensure the facility Electrical and Mechanical systems are in a normal lineup and no other work that affects the systems in this procedure are in progress.”
        
    - Template requires:
        
        > “Facility Electrical and Mechanical systems are in a normal lineup. No other work that affects systems in this procedure in progress.”
        

These are **non-compliant** because Section 04 requires **verbatim alignment**, regardless of intent.

---

### **2. PPE Deficiency – FCW Sections (Critical)**

In multiple FCW sections (e.g., _Mechanical Gallery 109 – FCW’s SOURCE 1_ and similar sections), the procedure states:

> “Don all appropriate PPE according to the Arc Flash Label.”  
> PPE table includes only:
> 
> - “Safety glasses or safety goggles”
>     
> - “Hearing protection”
>     
> - “Electrical safety shoes”
>     

However, the same sections explicitly instruct:

> “Disconnect panel will need to be unlocked… open the door”  
> “Perform IR scan… inside electrical compartment”

**Issue:**

- Opening energized electrical compartments and accessing internal components constitutes **equipment manipulation under electrical hazard conditions**.
    
- The PPE listed does **not include arc-rated clothing, gloves, or face shield**, despite Section 03 identifying arc flash risks and magnitudes.
    

**Why this is non-compliant:**

- The rulebook requires **arc flash PPE when manipulating or exposing energized electrical components**.
    
- Minimal PPE (safety glasses, shoes) is insufficient for the stated hazard levels.
    

---

### **3. PPE Inconsistency Across Similar Tasks (Recommended Standardization Issue)**

There is inconsistent PPE application for similar activities:

- **PDU / MDP sections:**  
    Require arc-rated PPE (e.g., 4 cal/cm², 40 cal/cm² suits)
    
- **FCW sections:**  
    Only require minimal PPE for **similar actions (opening panels, accessing energized components)**
    

This inconsistency creates ambiguity and increases risk of improper PPE selection during execution.

---

# **Recommended Improvements**

### **1. Clarify Electrical Work Condition (Energized Work Justification)**

The procedure repeatedly involves:

- Opening panels
    
- Accessing energized components
    
- Performing IR scans under load
    

While this is implied, it would improve clarity to explicitly state that:

- Work is performed **energized and under load for thermographic purposes**
    

This helps reinforce why PPE and boundaries are required.

---

### **2. Strengthen PPE Continuity Language**

Although PPE steps are generally well placed, adding a clarifying statement such as:

- PPE remains in effect until task completion or “Doff PPE”
    

would improve procedural clarity, especially given the length and repetition of sections.

---

### **3. Arc Flash Boundary Verification**

The procedure frequently states:

> “Set up ARC Flash Boundary…”

Consider adding:

- A verification step confirming boundary distance aligns with **arc flash label values**
    

This is a best-practice enhancement for field execution consistency.

---

# **Summary**

- **Critical Issues:**
    
    - Section 04 is **not verbatim compliant**
        
    - **Inadequate PPE** in FCW sections during energized electrical work
        
- **Recommended Improvements:**
    
    - Clarify energized work condition
        
    - Improve PPE continuity clarity
        
    - Strengthen arc flash boundary verification
        

---

If you want, I can walk through one FCW section and show exactly how PPE expectations should align with the hazard table—without rewriting your procedure, just pinpointing the gap more precisely.


# JSA Feedback

Here is your **Gap Analysis and Recommendations** comparing the JSA () against the MOP ():

---

# **Gap Analysis and Recommendations**

## ⚙️ Observations (Overall Alignment)

- The JSA **correctly identifies major electrical hazards** (arc flash, shock) and aligns with listed equipment energy levels in the MOP.
    
- PPE levels in the JSA generally **match arc flash values defined in the MOP tables**.
    
- However, the JSA is **equipment-based**, while the MOP is **task-sequenced and action-driven**—this creates significant coverage gaps.
    

---

## ⚠️ Missing or Incomplete (Key Gaps)

### 1. **Missing Core Work Steps from MOP**

The JSA does not capture the actual physical tasks being performed:

- Opening panel doors and removing dead fronts
    
- Performing IR scans on energized components
    
- Reinstalling covers and securing panels
    
- Switching AMS to maintenance/normal
    
- Operating FCW units (S1 ↔ S2 transfers)
    
- Unlocking/locking cabinet doors and bypass mechanisms
    
- Removing IR port covers and panel covers (UODP work)
    

👉 Current JSA only states “Accessing panel,” which **does not reflect real exposure points**

---

### 2. **Unaddressed High-Risk Tasks**

From the MOP, several **high-risk activities are not analyzed in the JSA**:

- **Dead front removal/install** (explicit arc flash exposure)
    
- **Working inside energized equipment for scanning**
    
- **Breaker manipulation / AMS switching**
    
- **Opening compartments using bypass mechanisms (pen use near energized parts)**
    

---

### 3. **Missing Hazard Categories**

JSA focuses almost entirely on electrical hazards and misses:

- **Dropped object hazards** (removing dead fronts, covers)
    
- **Ergonomic strain** (handling large panel covers, repetitive scanning)
    
- **Pinch/cut hazards** (panel edges, doors, latches)
    
- **Tool-related hazards** (screwdrivers near energized components)
    
- **Trip hazards** (barricades, tools in gallery aisles)
    

---

### 4. **Controls Are PPE-Only (Lack of Actionable Controls)**

Current JSA controls are primarily PPE listings.

Missing critical controls clearly required by the MOP:

- Establishing and maintaining **arc flash boundaries**
    
- Ensuring **unqualified personnel remain outside boundaries**
    
- **Two-person lift requirement** for panel removal
    
- **Verification steps** (breaker positions, camera storage)
    
- **Tool control and insulated tool usage**
    
- **Secure panel reinstallation before leaving task**
    

---

### 5. **No Task Sequencing / Exposure Progression**

The MOP clearly follows a pattern:

1. Set boundaries
    
2. Adjust system state (AMS)
    
3. Don PPE
    
4. Open equipment
    
5. Perform scan
    
6. Close/restore
    

The JSA does not reflect this sequence, which:

- Prevents proper hazard timing
    
- Makes supervision and auditing difficult
    

---

### 6. **FCW Operational Steps Not Covered**

The MOP includes **active equipment switching (S1 → S2 → S1)** with:

- Load transfer risk
    
- Equipment malfunction potential
    

These are **completely absent** from the JSA.

---

### 7. **UODP-Specific Exposure Not Captured**

Missing hazards related to:

- Removing IR port covers
    
- Exposing bus bars
    
- Accessing STS feeder breakers
    

These represent **direct energized exposure beyond standard panel access**

---

## 💡 Recommendations (Targeted Improvements)

### 1. **Convert JSA to Task-Based Structure**

Replace “Accessing [equipment]” with steps such as:

- Set up arc flash boundary
    
- Open panel / remove dead front
    
- Perform thermal scan
    
- Reinstall panel components
    
- Restore system to normal
    

---

### 2. **Add Missing High-Risk Tasks Explicitly**

Ensure JSA includes:

- Dead front removal/install
    
- IR scanning inside energized panels
    
- AMS switching operations
    
- Cabinet door/bypass mechanism operation
    

---

### 3. **Expand Hazard Identification**

Include:

- Mechanical (pinch, dropped objects)
    
- Ergonomic (lifting panels, repetitive scanning)
    
- Tool-related hazards
    
- Environmental (trip hazards from barricades/tools)
    

---

### 4. **Upgrade Controls to Actionable Language**

Replace PPE-only controls with:

- “Establish arc flash boundary per label and install barricades”
    
- “Use insulated tools when removing panel covers”
    
- “Use two-person lift for panel removal where required”
    
- “Verify correct panel and label prior to access”
    
- “Secure all covers and fasteners before leaving equipment”
    

---

### 5. **Incorporate Boundary and Personnel Controls**

- Explicitly state:
    
    - Maintain limited/restricted approach boundaries
        
    - Keep unqualified personnel outside barricades
        

---

### 6. **Add Equipment Operation Controls (FCW / Switching)**

- Verify load transfer status before and after switching
    
- Monitor for alarms during S1/S2 transitions
    
- Confirm system returned to normal state
    

---

### 7. **Align PPE with Task (Not Just Equipment)**

- Tie PPE to **specific activities**:
    
    - Panel removal = highest exposure
        
    - External scanning = reduced PPE where applicable
        

---

## ✅ Complete / Aligned

- Electrical hazard identification (arc flash, shock)
    
- PPE levels generally aligned with arc flash values
    
- Equipment coverage (PDU, MDP, RMDP, UODP, FCW)
    

---

## 🔍 Key Clarification

Before refining further:

**The MOP requires opening energized equipment and removing dead fronts.**  
Can you confirm:

1. Are all scans performed **fully energized (no LOTO)**?
    
2. Are **infrared windows available on any equipment**, or is full exposure always required?
    
3. Is there a **two-person requirement policy** for panel removal at your site?
    

These will affect how conservative the controls should be.