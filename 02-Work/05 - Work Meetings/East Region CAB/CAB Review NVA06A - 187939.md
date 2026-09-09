

I compared the attached **DH110 FCW Internal Fitting Visual Inspection MOP** against the attached **CRAH Isolation and Restoration JSA**. I grouped the repeated FCW inspection sequence into common physical work tasks and excluded administrative steps such as notifications, approvals, BMS checks, CMMS updates, and sign-offs. The MOP is specifically for **internal fitting visual inspection of DH110 FCWs**, requires items including gloves, protective eyewear, protective footwear, fall protection, CRAH/FCW triangle key, and a manlift, and identifies electrical shock risk plus the operational risk of isolating more than one CRAH/FCW at a time. The JSA currently lists broader CRAH isolation/restoration tasks, including breaker opening, CRAH inspection/cleaning, scissor lift use, and glycol transfer.

### Recommended Task / Hazard / Control / PPE Section

|Step/Task|Hazard|Controls|PPE|
|---|---|---|---|
|Stage tools, PPE, LOTO devices, and establish work area for FCW inspection|Slips, trips, struck-by tools/materials, wrong equipment selection|Verify the exact FCW ID before work. Stage only tools required for visual inspection. Keep walkways clear and maintain housekeeping around the FCW. Confirm LOTO devices, triangle key, inspection materials, and lift equipment are available before physical work begins.|Safety glasses, gloves, safety footwear|
|Use manlift/aerial lift to access FCW upper panels, if required|Fall from height, lift tip-over, struck-by/dropped objects|Note: Assumed lift use because the MOP lists a manlift and fall protection. Use only trained/authorized lift operators. Complete pre-use lift inspection. Set lift on level, stable surface. Maintain guardrails. Do not climb or stand on rails. Barricade or control the area below when overhead work is occurring.|Safety glasses, hard hat, gloves, safety footwear, fall protection as required by site/lift policy|
|Open FCW Power Supply B and Power Supply A disconnects for the selected unit|Electrical shock, arc flash, wrong source isolation, loss of cooling redundancy|Isolate only one FCW at a time to maintain required redundancy. Positively identify the correct unit and both electrical sources. Open Power Supply B, verify OFF/indicator lights extinguished, then open Power Supply A and verify OFF/indicator lights extinguished, consistent with the MOP sequence. Apply LOTO to both sources before opening panels or contacting internal areas.|Safety glasses, electrical gloves, arc-rated PPE as required by site electrical assessment, safety footwear|
|Verify zero energy before opening FCW panels|Electrical shock from residual, backfeed, or alternate source; reliance on indicator lights only|Do not rely solely on extinguished indicator lights. Verify absence of voltage using an approved, calibrated meter and live-dead-live method where applicable. Confirm both Source A and Source B are isolated and locked/tagged before panel removal.|Safety glasses, electrical gloves as required, gloves, safety footwear|
|Remove FCW top panels near filters|Cuts/lacerations, pinch points, dropped panels/tools, awkward body position|Use proper FCW/CRAH triangle key and hand tools. Secure panels during removal. Use two-person handling if panel size/position creates strain or drop potential. Place removed panels in a stable location outside walking paths. Keep hands clear of pinch points.|Safety glasses, cut-resistant gloves, hard hat if overhead/elevated, safety footwear|
|Remove insulation around internal GruvLok fitting|Skin/eye irritation from insulation, cuts, debris, possible contact with condensate/glycol residue if leakage is present|Remove only the insulation necessary for visual inspection. Avoid tearing or scattering insulation. Stop work and escalate if wet insulation, leakage, damaged fittings, or unexpected material condition is found. Keep debris contained and clear from equipment openings.|Safety glasses, gloves, long sleeves as needed, safety footwear|
|Perform visual inspection of GruvLok internal fitting|Accidental adjustment of fitting, pinch/cut exposure, contact with leaking fluid, working in restricted space|Maintain visual-only scope. The MOP states Poole and Kent are not to have tools capable of tightening GruvLok fittings. Do not loosen, tighten, torque, or disturb fittings. Verify required visual conditions only, including bolt pad gap, no metal-to-metal contact, and no over-torqued indications. Stop and escalate failed conditions.|Safety glasses, gloves, safety footwear|
|Reinstall insulation and FCW panels|Pinch points, cuts, dropped objects, incomplete equipment reassembly|Reinstall insulation to original condition unless directed otherwise. Reinstall all panels securely before re-energization. Account for tools, debris, and removed materials. Verify personnel are clear before restoring power.|Safety glasses, cut-resistant gloves, hard hat if elevated/overhead, safety footwear|
|Close Power Supply A and Power Supply B disconnects to restore the selected FCW|Electrical shock, arc flash, unexpected equipment startup, restoration in wrong sequence|Remove LOTO only after all authorized persons are clear and removal is authorized. Restore power in the MOP sequence: close Power Supply A, then Power Supply B. Stand clear of equipment during switching. Verify abnormal conditions are not present before proceeding to the next FCW.|Safety glasses, electrical gloves, arc-rated PPE as required by site electrical assessment, safety footwear|
|Clear work area after each FCW inspection|Slip/trip hazards, left-behind tools, debris in equipment area|Remove tools, debris, insulation scraps, and materials before moving to the next FCW. Confirm panels are secure and the work area is safe for normal operations.|Safety glasses, gloves, safety footwear|

**Rationale:** I treated the MOP as a repeated dual-source FCW isolation, elevated-access, panel-removal, insulation-handling, visual-inspection, and re-energization task; administrative notification, BMS, approval, CMMS, and sign-off steps were excluded from the physical hazard analysis.

---

## Gap Analysis and Recommendations

✅ **Complete/Aligned:** The JSA recognizes electrical exposure during breaker operation and CRAH inspection, including arc flash and electrical shock hazards. It also includes general LOTO language for de-energizing equipment before maintenance.

⚠️ **Missing or Incomplete:** The JSA does not match the specific MOP title or scope. The MOP is for **DH110 FCW internal GruvLok fitting visual inspection**, while the JSA is titled **CRAH Isolation and Restoration** and includes broader work such as “inspection and cleaning.” Update the JSA activity/task wording to match the FCW visual inspection scope.

⚠️ **Missing or Incomplete:** The JSA does not clearly identify the **dual electrical sources** shown in the MOP: **Power Supply B** and **Power Supply A**. The JSA should specify that both sources must be isolated, locked/tagged, and verified before panels are removed.

💡 **Recommendation:** Replace “Opening input power breaker” with a more specific task such as: **“Open and LOTO FCW Power Supply B and Power Supply A disconnects; verify absence of voltage before panel removal.”**

⚠️ **Missing or Incomplete:** The JSA control “Wear Arc flash gear” is too generic. It should include qualified-person switching, positive equipment identification, operation of the correct disconnects, appropriate arc-rated PPE based on the equipment label/site electrical assessment, and standing clear during switching.

⚠️ **Missing or Incomplete:** The MOP calls for verifying OFF position and extinguished indicator lights, but the JSA should also require **zero-energy verification with a calibrated meter** before internal work. Indicator lights alone should not be treated as proof of absence of voltage.

💡 **Recommendation:** Add: **“Verify zero energy using an approved calibrated meter after LOTO; do not rely solely on indicator lights.”**

⚠️ **Missing or Incomplete:** The JSA does not address **removal and reinstallation of FCW panels**, which is a repeated physical task in the MOP. This creates missing hazards for sharp edges, pinch points, dropped panels/tools, and ergonomic strain.

⚠️ **Missing or Incomplete:** The JSA does not address **removal and reinstallation of insulation around the internal fitting**, which is a repeated physical step in the MOP. Add hazards for insulation irritation, debris, cuts, and potential fluid contact if leakage is discovered.

⚠️ **Missing or Incomplete:** The JSA does not include the MOP’s critical operational control that **only one FCW per Data Hall will be isolated at a time** to maintain N+1 cooling. This is a key procedure-specific risk control.

💡 **Recommendation:** Add a control such as: **“Isolate only one FCW at a time; verify no other work affects the cooling lineup before proceeding to the next unit.”**

⚠️ **Missing or Incomplete:** The JSA does not include a restoration/re-energization task. The MOP repeatedly requires reinstalling panels and then closing Power Supply A and Power Supply B. Add hazards and controls for re-energization, unexpected startup, personnel clearance, tool removal, and controlled LOTO removal.

⚠️ **Potentially Irrelevant:** The JSA includes **“Transfer the glycol from the Tote to the glycol makeup tank.”** This activity does not appear in the MOP’s detailed work sequence and should be removed unless glycol transfer is actually part of this job.

⚠️ **Potentially Irrelevant / Needs Confirmation:** The JSA references **“Using the scissor lift,”** while the MOP required materials list references a **manlift** and fall protection. Keep the elevated-work hazard only if a lift is actually required to access the panels, but revise the task wording to match the equipment being used.

⚠️ **Potentially Irrelevant:** The JSA includes **“CRAH unit inspection and cleaning,”** but the MOP states the work is **visual only** and includes a control that the contractor does not have tools to tighten GruvLok fittings. Remove “cleaning” unless it is intended to be performed.

⚠️ **PPE Alignment Issue:** The MOP lists gloves, protective eyewear, protective footwear, fall protection, and manlift; the JSA lists safety glasses, cut-resistant gloves, arc flash suit, safety boots, hard hat, and electrical gloves. Reconcile the required PPE so it reflects the actual tasks: electrical switching/LOTO, elevated access, panel handling, and insulation handling.

⚠️ **Document Currency Issue:** The JSA approval shown is **Jan. 6, 2025**, while the MOP approval section shows **June 11, 2026**. The JSA should be reviewed/updated for this specific MOP before use.

### Clarifications to Confirm Before Field Use

1. Is a **manlift/scissor lift** actually required to remove the FCW top panels, or can the panels be accessed from floor level?
    
2. Is **any glycol handling or transfer** part of this job, or is glycol exposure limited only to incidental contact if a leak is discovered during inspection?
    

**Disclaimer:** This JSA Aid provides general guidance based on the provided information and a standard hazard–control reference. It does not replace competent supervision, required permits, site-specific procedures, or regulatory requirements.




