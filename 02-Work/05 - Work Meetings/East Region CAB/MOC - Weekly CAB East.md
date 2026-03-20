**East Region – Medium Risk CAB**

**Meeting Minutes**

**Meeting Title:** East Region Medium Risk CAB – Weekly Review  
**Date/Time:** January 28, 2026, 7:25 PM  
**Attendees (as captured):**  
James Sedoruk, David James, Syed Abidi, Joe Kendra, Daniel Stevenson, Nicholas Mansberger, Todd Lipcsey, Jack Gillian  
**Additional attendees:** Network Engineering (Syed Abidi)  
**Meeting Type:** Regular Weekly Medium-Risk CAB Session

---

**Meeting Summary**

The CAB reviewed a single work activity related to ISP failover testing at NVA 01A. The discussion focused on validating a newly installed secondary 10 Gb Cogent circuit, confirming service dependencies, identifying gaps in prior validation, and ensuring appropriate customer notification and monitoring coverage. While the work was technically sound, the group agreed additional preparation was required before execution, including customer communications, alarm validation testing, and rescheduling to allow sufficient notice and weather risk mitigation.

---

**Topics Discussed**

---

**1. Case 173087 – NVA 01A**

**Cogent ISP Failover Testing**

**Presenters:** David James (overview), Syed Abidi (technical walkthrough)

**Discussion Summary**

- Scope involves **controlled failover testing** from the primary Zayo ISP circuit to the secondary Cogent 10 Gb circuit and subsequent restoration.
- Maintenance window proposed: **1 hour**, with brief interruptions expected:

- Internet traffic disruption: ~5–10 minutes
- Modius tunnel disruption: up to ~10–20 minutes (worst case)

- Testing validates:

- Internet traffic failover to Cogent
- Modius tunnel establishment over secondary ISP
- Ability to revert to Zayo if issues arise

**Identified Concerns**

- The secondary 10 Gb Cogent circuit was installed and connected prior to formal CAB validation.
- While traffic had passed on the circuit elsewhere, **full service validation (email alarms, EPMS/BMS alerting)** had not yet been confirmed for NVA 01A.
- Guest Wi-Fi services and customer portal access may be briefly impacted during failover.
- EPMS visibility via Modius would be unavailable during tunnel disruption, requiring manual monitoring.

**Decisions**

- The group agreed this activity should proceed, but **not on the originally scheduled date**.
- The maintenance will be **rescheduled by approximately one week** to allow:

- Proper customer notification
- Site staffing and monitoring readiness
- Alarm and email validation steps to be added
- Reduced risk from forecasted weather conditions

---

**2. Customer Communication & Monitoring Requirements**

**Discussion Summary**

- Customer notification is required due to potential impacts to:

- Guest Wi-Fi
- Online client portal access

- Local BMS visibility will remain; EPMS/Modius visibility will be temporarily unavailable.
- Site teams must be prepared for **manual walk-through monitoring** during the window.
- Alarm validation (email, EPMS, BMS) must be explicitly tested while operating on the secondary ISP.

---

**3. Schedule Adjustment**

**Discussion Summary**

- Original execution date (Jan 29) deferred.
- New target date agreed: **February 5, 2026**.
- CAB review will occur ahead of that date once updates are completed.

---

**Consolidated Action Items Table**

| **#** | **Responsible Party**           | **Action Required**                                                                             | **Related Case** | **Due Date**        |
| ----- | ------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------- | ------------------- |
| 1     | David James / Syed Abidi        | Update MOP to include validation of email alarms, EPMS, and BMS alerting while on secondary ISP | Case 173087      | Before resubmission |
| 2     | Syed Abidi                      | Coordinate with Todd to define alarm-trigger testing steps during failover                      | Case 173087      | Before resubmission |
| 3     | Todd Lipcsey                    | Coordinate and issue customer notification regarding guest Wi-Fi and portal impact              | Case 173087      | Prior to Feb 5      |
| 4     | David James                     | Reschedule maintenance window to **Feb 5, 2026**                                                | Case 173087      | Immediate           |
| 5     | David James / Syed Abidi        | Resubmit updated case for CAB review                                                            | Case 173087      | Before next CAB     |
| 6     | James Sedoruk / Nick Mansberger | Review updated submission once resubmitted                                                      | Case 173087      | Upon resubmission   |
| 7     | Site Operations                 | Ensure staffing and manual monitoring plan during EPMS/Modius outage                            | Case 173087      | Prior to execution  |