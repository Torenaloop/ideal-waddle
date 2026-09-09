
The procedure covers de-energizing PDU-P1-120-02-BSW04, replacing Tap Box DD 311-312(BLUE), and re-energizing the circuit; it also identifies arc flash risk, MEWP fall risk, and 28.3 cal/cm² electrical exposure. The submitted JSA only includes one task, “Opening/Closing Breakers,” with arc flash/electrical shock controls.

### Recommended JSA Task/Hazard/Control Section

|Step/Task|Hazard|Controls|PPE|
|---|---|---|---|
|Open PDU-P1-120-02-BSW04 output breaker and apply LOTO|Arc flash, electrical shock, incorrect equipment operation, unexpected energization|Verify correct equipment ID before switching. Establish arc flash boundary. Keep panel dead fronts in place. Stand to the side when operating the breaker. Use qualified personnel only. Open breaker per procedure, apply LOTO, and verify lock/tag placement before proceeding. Stop work if equipment state does not match expected condition.|40 cal/cm² arc-rated clothing or arc flash suit, 40 cal/cm² arc flash hood, Class 0 rubber gloves with leather protectors, hard hat, safety glasses or goggles, hearing protection, leather work shoes.|
|Access tap box work area using MEWP|Fall from elevation, MEWP tip-over, collision/struck-by, dropped objects|Inspect MEWP before use. Use only trained/authorized MEWP operators. Operate on stable/level surface. Maintain guardrails and remain inside platform. Use a spotter where congestion or overhead obstructions exist. Barricade or control the work area below to prevent personnel exposure to dropped objects.|Fall arrestor, high-visibility vest, hard hat, safety glasses or goggles, hearing protection, leather work shoes.|
|Prepare tap box DD 311-312(BLUE) for removal|Electrical shock, arc flash, unexpected breaker closure, contact with energized components|Verify correct tap box designation. Confirm all tap box breakers are open. Confirm all whips are disconnected. Verify actuator interlock bars block breaker closure before unlatching. Add an explicit absence-of-voltage verification step before physical removal where feasible and required by site procedure.|Fall arrestor, cut-resistant gloves, hard hat, safety glasses or goggles, hearing protection, leather work shoes.|
|Release, remove, and support existing tap box|Dropped load, struck-by, pinch points, hand injury, ergonomic strain|Support the tap box before pressing/holding the actuator. Keep hands clear of latch, rail, and interlock pinch points. Use two-person handling, lifting aid, or controlled lowering method if weight or position creates strain. Maintain secure footing in the MEWP platform. Control tools and parts to prevent drops.|Fall arrestor, cut-resistant gloves, hard hat, safety glasses or goggles, hearing protection, leather work shoes.|
|Install replacement tap box and secure latch/interlock|Pinch points, dropped object, improper seating, future electrical fault from poor installation|Align tap box to the Databar rail before release. Keep hands clear while engaging latch and actuator. Verify latch is engaged. Turn actuator interlock to locked position. Verify interlock bars are in the expected position before allowing breaker operation. Confirm installation is mechanically secure before re-energization.|Fall arrestor, cut-resistant gloves, hard hat, safety glasses or goggles, hearing protection, leather work shoes.|
|Remove LOTO and close PDU-P1-120-02-BSW04 output breaker|Arc flash, electrical shock, unexpected fault, unauthorized energization|Confirm tap box work is complete, tools/personnel are clear, covers/latches/interlocks are secured, and affected personnel are notified before LOTO removal. Remove LOTO only by authorized personnel. Establish arc flash boundary. Stand to the side when closing the breaker. Close breaker per procedure and verify normal load/no unexpected alarms after energization.|40 cal/cm² arc-rated clothing or arc flash suit, 40 cal/cm² arc flash hood, Class 0 rubber gloves with leather protectors, hard hat, safety glasses or goggles, hearing protection, leather work shoes.|
|Clear tools/materials and restore work area|Slip/trip hazards, sharp edges, dropped objects, blocked access/egress|Remove debris, packaging, unused parts, tools, and barricades when safe to do so. Verify walkways and access panels are clear. Account for tools and materials before final turnover.|Cut-resistant gloves as needed, safety glasses, hard hat, leather work shoes.|

**Rationale:** The closest applicable hazard/control matches are electrical switching, LOTO/zero-energy control, elevated work/MEWP, material handling, dropped-object exposure, pinch-point/hand injury, and housekeeping.

### Gap Analysis and Recommendations

- ✅ **Complete/Aligned:** Arc flash and electrical shock are relevant and are included in the JSA for opening/closing breakers.
    
- ⚠️ **Missing or Incomplete:** The JSA does not cover the physical tap box replacement scope, including MEWP use, fall exposure, whips disconnected, actuator interlock operation, tap box release/removal, and installation steps shown in the MOP.
    
- ⚠️ **Missing or Incomplete:** LOTO is not addressed in the JSA even though the MOP requires opening PDU-P1-120-02-BSW04 and placing LOTO before proceeding to the tap box work.
    
- ⚠️ **Missing or Incomplete:** The JSA does not address dropped object, pinch point, struck-by, or ergonomic hazards during removal/installation of the tap box.
    
- ⚠️ **Missing or Incomplete:** The JSA does not explicitly require fall protection or MEWP controls, although the MOP identifies MEWP fall risk and requires fall arrestor use.
    
- ⚠️ **PPE Mismatch:** The JSA lists **Class00 gloves**, while the MOP switching PPE lists **Class 0 rubber gloves with leather protectors**. Confirm the required glove class against the equipment voltage, arc flash label, and site electrical safety requirements before final approval.
    
- ⚠️ **Sequence Clarification Needed:** The MOP shows tap box removal steps and later references client voltage verifications, but the provided sequence does not clearly show an absence-of-voltage verification immediately before releasing/removing the tap box. Add or confirm that verification step before physical removal.
    
- 💡 **Recommendation:** Replace the single JSA row with the six physical work-task rows above, or add them beneath the existing breaker-switching row.
    
- 💡 **Recommendation:** Change generic control language such as “proper PPE related to ARC Flash labeling” to the specific MOP-required PPE and the 28.3 cal/cm² exposure basis where applicable.
    
- 💡 **Recommendation:** Verify document naming/scope: the uploaded MOP filename and overview reference DH120 tap box replacement, while the visible document header references “DH110 PDU Energization.” This should be corrected or clarified before supervisor approval.
    

**Clarifications to confirm before final JSA signoff:**

1. Does the procedure require absence-of-voltage verification at the tap box before step 18.8/18.9 removal?
    
2. Should electrical gloves be Class 0 or Class 00 for this task?
    
3. Should the JSA title be updated from “Datahall Busway Energization” to “PDU Output Breaker De-Energization / Tap Box Replacement / Re-Energization”?
    

