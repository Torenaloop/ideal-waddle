Feedback

**Document Reviewed:** _FTE of U3-MVS-02 and U4-MVS-01 – MOP_

---

# **Issues Found**

## 1) Live-Dead-Live (LDL) verification is missing (Critical)

Section 03 lists high arc-flash energies and MV switching activities (e.g., U3-MVS-02 and U4-MVS-01 at **73.3 cal/cm²**, UMVS at **55.6 cal/cm²**) and Section 05 includes multiple **switching operations (OPEN/CLOSE)** using remote operators and “three-way puffer switch” actions.

However, the procedure does **not** include any explicit step to **verify absence of voltage** using a **Live-Dead-Live** method at the isolation points prior to work/handling conditions (nor a LDL table/section).

Examples of energized switching without LDL section:

- “REI … give a ‘3,2,1 count’ to **CLOSE Switch U4-2**…”
    
- “REI … move three-way puffer switch for **U3-02-1 from OPEN to CLOSED**…”
    
- “REI … **CLOSE switch U3-02-2**…”
    
- “REI … **CLOSE switch U4-01-2** … verify cross-tie functionality.”
    

### Why this is non-compliant:

Where the procedure performs isolation/LOTO activities and MV switching actions, LDL verification (or an LDL section/table) is required to confirm absence of hazardous electrical energy at defined test points.

---

## 2) LOTO tracking is incomplete: no lock identifiers + no LOTO log update step (Critical)

Section 05 repeatedly instructs REI to “apply YELLOW locks” and to remove “LOTO” at multiple switches, e.g.:

- “REI to apply YELLOW locks to Switch U3-02-2 / U3-02-3 / … / U3-02-6.”
    
- “REI … apply YELLOW locks to Switch U4-01-2 / U4-01-3 / … / U4-01-6.”
    
- “REI at U4-UMVS to **remove LOTO** to Switch U4-2.”
    
- “REI … **remove LOTO** from U3-02-2.”
    
- “REI … **remove LOTO** from switch U4-01-2.”
    
- Backout: “REI to apply LOTO to Switch U4-2.”
    

But the procedure does **not** include:

- Any “Record LOTO identifier # ____” fields, and
    
- Any instruction to **update the LOTO log** when locks are applied/removed.
    

### Why this is non-compliant:

Per the LOTO identifier tracking rule, when LOTO is used the procedure must include verbiage to **update the LOTO log**.  
**Required instruction:** “Add the correct verbiage to update the LOTO log.”

---

## 3) PPE table does not match the stated hazard magnitudes (Critical PPE mismatch)

Section 03 lists arc flash magnitudes up to **73.3 cal/cm²** (U3-MVS-02 and U4-MVS-01) and **55.6 cal/cm²** (UMVS).

But Section 05 PPE instruction states:

- “REI to don **40/cal arc flash suit**.” (and later again)
    

### Why this is non-compliant:

A 40 cal suit does **not** align with the listed 55.6 / 73.3 cal/cm² magnitudes unless the procedure explicitly documents engineered controls, working distances, arc-reduction, or boundaries that reduce incident energy at the working position. The procedure provides boundaries (246 in / 282 in) but does **not** explain how that translates into PPE category selection or reduced exposure condition.

---

## 4) PPE sequencing issue: switching actions occur before “Don PPE” step (Critical)

The first explicit “don 40/cal arc flash suit” step occurs **after** several MV cabinet access and verification steps, including:

- “OPEN cabinet doors…” (U3-UMVS, U3-MVS-02, U4-MVS-01, U4-UMVS)
    
- Applying YELLOW locks on multiple switches
    
- Establishing CAZ zones
    

Given Section 03 MV hazards and the procedure involving opening MV enclosures, PPE should be clearly required **before** those exposure actions (unless those actions are strictly outside boundary / non-exposure tasks, which is not stated).

### Why this is non-compliant:

Per PPE verification rules: when actions involve manipulation/access that could expose electrical hazards, PPE must be donned beforehand. The procedure currently leaves ambiguity and places PPE too late relative to exposure steps.

---

## 5) LOTO removal language conflicts with earlier “apply YELLOW locks”

Early steps say REI applies YELLOW locks to various switches (U3-02-2…U3-02-6 and U4-01-2…U4-01-6). Later steps include:

- “REI … remove LOTO from U3-02-2.”
    
- “REI … remove LOTO from switch U4-01-2.”
    

It’s unclear whether these are the same “YELLOW locks” or separate LOTO devices.

### Why this is a compliance issue:

Locking scheme must be unambiguous (what is being removed, by whom, under what authorization). As written, it creates a risk of removing the wrong device or misunderstanding the lock status.

---

# **Recommended Improvements**

## A) Add explicit vendor/contractor responsibility statements

The procedure relies heavily on REI actions. Recommend adding a clear line that REI is responsible for executing LDL (if added) and applying/removing their own locks per site LOTO program (without requiring the internal procedure to document REI PPE details).

## B) Strengthen “STOP WORK” triggers during energization steps

You have one trigger:

- “IF power was not received… follow BACK OUT procedure.”
    

Recommend adding stop-work triggers for:

- Unexpected alarms/indications at voltage sensing screens
    
- Any abnormal SF6 condition
    
- Any failure of remote operator response
    

## C) Make CAZ/arc flash boundary implementation explicit

You list boundaries, but the procedure should clearly state:

- Barricade placement distance (already implied by CAZ zones)
    
- Who controls entry
    
- That unqualified persons remain outside boundary
    

---

