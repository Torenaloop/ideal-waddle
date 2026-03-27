---
PARA: Resource
Status: Active
Priority: High
tags: [incident-management, workflow, EHS]
---

> [!tip] **Viewing tip** — switch to **Reading Mode** (Ctrl/Cmd + E) to see this diagram rendered.

<style>

.sl-wrap {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-size: 11.5px;
  color: #1a1a1a;
  width: 100%;
  overflow-x: auto;
}
.sl-title {
  background: linear-gradient(135deg, #1a2e4a 0%, #2c4a6e 100%);
  color: #fff;
  padding: 12px 18px;
  font-size: 13.5px;
  font-weight: 700;
  text-align: center;
  border-radius: 8px 8px 0 0;
  letter-spacing: 0.2px;
}
.sl-table {
  width: 100%;
  border-collapse: collapse;
  border: 1.5px solid #999;
  border-top: none;
  border-radius: 0 0 8px 8px;
  overflow: hidden;
  table-layout: fixed;
}
.sl-corner {
  width: 68px;
  background: #e0e0e0;
  border: 1px solid #bbb;
}
.sl-ph {
  padding: 8px 6px;
  font-weight: 700;
  font-size: 11px;
  color: #fff;
  text-align: center;
  border: 1px solid rgba(255,255,255,0.25);
  letter-spacing: 0.2px;
  vertical-align: middle;
}
.sl-lbl {
  text-align: center;
  vertical-align: middle;
  font-weight: 700;
  font-size: 10px;
  color: #fff;
  padding: 4px 3px;
  line-height: 1.3;
  border: 1px solid rgba(255,255,255,0.15);
  width: 68px;
}
.sl-cell {
  padding: 5px;
  vertical-align: top;
  border: 1px solid #ddd;
}
.sl-card {
  border-radius: 5px;
  border: 1.5px solid;
  padding: 6px 8px;
  min-height: 72px;
  font-size: 11px;
  line-height: 1.5;
  color: #111111 !important;
}
.sl-card ul {
  margin: 0;
  padding-left: 13px;
}
.sl-card li {
  margin-bottom: 2px;
  color: #111111 !important;
}
.sl-card b, .sl-card strong {
  color: #000000 !important;
}
.sl-card span {
  color: inherit !important;
}
.sl-empty {
  min-height: 72px;
  border-radius: 5px;
  background: repeating-linear-gradient(
    45deg, transparent, transparent 5px,
    rgba(0,0,0,0.04) 5px, rgba(0,0,0,0.04) 10px
  );
  border: 1px dashed #ccc;
}
.esc-badge {
  display: inline-block;
  margin-top: 4px;
  padding: 2px 5px;
  border-radius: 3px;
  font-size: 9.5px;
  font-weight: 600;
  background: #3b1a00;
  color: #ffe8c0;
  border: 1px solid #7a3a00;
  line-height: 1.4;
}
.sl-legend {
  background: #e8e8e8;
  border: 1.5px solid #bbb;
  border-top: none;
  border-radius: 0 0 8px 8px;
  padding: 7px 14px;
  font-size: 10px;
  color: #222 !important;
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
  align-items: center;
}
.sl-swatch {
  display: inline-block;
  width: 12px; height: 12px;
  border-radius: 2px;
  border: 1px solid rgba(0,0,0,0.2);
  vertical-align: middle;
  margin-right: 3px;
}

</style>

<div class="sl-wrap">
  <div class="sl-title">
    STACK Infrastructure &mdash; Incident Management &amp; Reporting Workflow &nbsp;|&nbsp; Swim Lane by Role
  </div>
  <table class="sl-table">
    <thead>
      <tr><th class="sl-corner"></th><th class="sl-ph" style="background:#2c5f8a">1 &mdash; Prevention</th><th class="sl-ph" style="background:#8B2500">2 &mdash; Immediate Response</th><th class="sl-ph" style="background:#8a5a00">3 &mdash; Reporting</th><th class="sl-ph" style="background:#3b5e2b">4 &mdash; Investigation</th><th class="sl-ph" style="background:#1a5c6b">5 &mdash; Follow-up &amp; Close</th></tr>
    </thead>
    <tbody>
      <tr><td class="sl-lbl" style="background:#1e3a5f">All<br>Personnel</td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#dce9f5;border-color:#2c5f8a;border-width:2px;color:#111111"><ul><li>Follow all STACK safety procedures</li><li><b>Stop Work Authority:</b> any person may stop work if an unsafe condition is identified &mdash; no retribution</li><li>Report all observed hazards to supervisor</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#fce8e4;border-color:#8B2500;border-width:2px;color:#111111"><ul><li>Report incident immediately to supervisor</li><li>Call 911 for any medical emergency</li><li>Administer first aid / CPR if trained &amp; safe</li><li>Restrict access to the incident scene</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#fdf6dc;border-color:#8a5a00;border-width:2px;color:#111111"><ul><li>Report <b>all</b> incidents before end of work shift</li><li>Enter incident record in <b>SOSPES</b></li><li>Near-misses: report within <b>24 hours</b></li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#e6f2e0;border-color:#3b5e2b;border-width:2px;color:#111111"><ul><li>Participate in investigation when requested</li><li>Provide written witness statements</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#d6eff3;border-color:#1a5c6b;border-width:2px;color:#111111"><ul><li>Complete any required updated safety training</li><li>Apply lessons learned to daily work</li></ul></div></td></tr><tr><td class="sl-lbl" style="background:#5c1a00">Supervisor</td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#dce9f5;border-color:#2c5f8a;border-width:2px;color:#111111"><ul><li>Enforce all STACK safety procedures</li><li>Ensure JSA / HRA is completed before high-risk work</li><li>Verify hazard controls are adequate</li><li>Confirm all staff understand Stop Work rights</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#fce8e4;border-color:#8B2500;border-width:2px;color:#111111"><ul><li>Ensure 911 is notified for emergencies</li><li>Notify site security immediately</li><li>Direct injured employee to medical care; arrange transport</li><li>Secure and preserve the incident scene</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#fdf6dc;border-color:#8a5a00;border-width:2px;color:#111111"><ul><li>Complete <b>First Report of Injury</b></li><li>Submit all reports within required timeframe</li><li>Confirm SOSPES entry is accurate &amp; complete</li><li>Identify initial corrective actions</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#e6f2e0;border-color:#3b5e2b;border-width:2px;color:#111111"><ul><li><b>Investigate ASAP</b> after scene is stable</li><li>Secure scene &amp; collect / preserve evidence</li><li>Interview witnesses; document statements</li><li>Conduct <b>RCA</b> if required</li><li>Submit completed reports within timeframe</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#d6eff3;border-color:#1a5c6b;border-width:2px;color:#111111"><ul><li>Identify &amp; implement corrective actions</li><li>Share lessons learned with team</li></ul></div></td></tr><tr><td class="sl-lbl" style="background:#2e4a1a">COM /<br>Dev. Mgr</td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#dce9f5;border-color:#2c5f8a;border-width:2px;color:#111111"><ul><li>Respond to Stop Work notifications &amp; mitigate hazards</li><li>Assist supervisors with prevention &amp; corrective actions</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#fce8e4;border-color:#8B2500;border-width:2px;color:#111111"><ul><li>Act as supervisor point of contact if unavailable</li><li>Support immediate response</li><li>Notify contractor / vendor orgs of incidents involving their staff</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#fdf6dc;border-color:#8a5a00;border-width:2px;color:#111111"><ul><li>Complete first reports of injury</li><li>Notify contractor orgs; provide copy of final reports</li><li><b>Trigger Safety@stackinfra.com</b> for SERIOUS incidents</li><li><span class="esc-badge">&#8681; Notifies VP EHS for serious incidents</span></li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#e6f2e0;border-color:#3b5e2b;border-width:2px;color:#111111"><ul><li>Participate in root cause investigation</li><li>Assign corrective action accountabilities; manage timeline</li><li><span class="esc-badge">&#8681; Submits completed RCA to VP of EHS</span></li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#d6eff3;border-color:#1a5c6b;border-width:2px;color:#111111"><ul><li>Evaluate corrective action effectiveness</li><li>Verify no new hazards introduced</li><li>Share lessons learned broadly across teams</li></ul></div></td></tr><tr><td class="sl-lbl" style="background:#2a1a5c">VP of EHS</td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#dce9f5;border-color:#2c5f8a;border-width:2px;color:#111111"><ul><li>Develop &amp; maintain Incident Management Procedure</li><li>Conduct minimum 3-year procedure reviews</li><li>Champion Stop Work Authority culture</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#fce8e4;border-color:#8B2500;border-width:2px;color:#111111"><ul><li>Available for serious / fatality incidents</li><li>Engage General Counsel if OSHA arrives on-site</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#fdf6dc;border-color:#8a5a00;border-width:2px;color:#111111"><ul><li><b>OSHA Notification:</b> Fatality &rarr; <b>8 hours</b></li><li>Hospitalisation / Amputation / Eye Loss &rarr; <b>24 hours</b></li><li>California: serious injuries &rarr; <b>8 hours</b></li><li>Canada (AB / ON): per provincial rules</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#e6f2e0;border-color:#3b5e2b;border-width:2px;color:#111111"><ul><li><b>Review ALL final RCA reports</b></li><li>Confirm root causes properly identified</li><li>Make systemic procedure changes</li><li>Distribute findings to leadership</li></ul></div></td><td class="sl-cell" style="background:#f9f9f9"><div class="sl-card" style="background:#d6eff3;border-color:#1a5c6b;border-width:2px;color:#111111"><ul><li>Update procedures for systemic issues</li><li>Record OSHA-required reports if directed by agency</li></ul></div></td></tr><tr><td class="sl-lbl" style="background:#5c3a00">Dir.,<br>Risk Mgmt</td><td class="sl-cell" style="background:#eef3f9"><div class="sl-empty"></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-empty"></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#fdf6dc;border-color:#8a5a00;border-width:2px;color:#111111"><ul><li>Coordinate with employee &amp; manager on claim</li><li>Complete Incident Report Form for workers&rsquo; comp carrier</li><li><b>Notify carrier within 24 hrs</b> (US) or Provincial Board (Canada)</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#e6f2e0;border-color:#3b5e2b;border-width:2px;color:#111111"><ul><li>Support investigation as needed</li><li>Coordinate with TPAs on claim documentation</li></ul></div></td><td class="sl-cell" style="background:#eef3f9"><div class="sl-card" style="background:#d6eff3;border-color:#1a5c6b;border-width:2px;color:#111111"><ul><li><b>Manage all open claims to closure</b></li><li>Coordinate with Third-Party Administrators (TPAs)</li><li>Assist identifying light duty opportunities</li></ul></div></td></tr><tr><td class="sl-lbl" style="background:#5c1a1a">External<br>(OSHA / WC<br>/ EMS)</td><td class="sl-cell" style="background:#fff5f5"><div class="sl-empty"></div></td><td class="sl-cell" style="background:#fff5f5"><div class="sl-card" style="background:#fce8e4;border-color:#8B2500;border-width:2px;color:#111111"><ul><li><b>911 / Emergency Services</b></li><li>Fire &bull; Police &bull; EMS</li><li>Respond to on-site medical emergencies</li></ul></div></td><td class="sl-cell" style="background:#fff5f5"><div class="sl-card" style="background:#fdf6dc;border-color:#8a5a00;border-width:2px;color:#111111"><ul><li><b>OSHA</b> &mdash; receives regulatory notifications</li><li><b>Workers&rsquo; Comp Carrier</b> &mdash; initiates claim</li><li><b>EPA / State Agency</b> &mdash; environmental incidents</li><li><b>Client (e.g., Journey)</b> &mdash; client-specific reports</li></ul></div></td><td class="sl-cell" style="background:#fff5f5"><div class="sl-empty"></div></td><td class="sl-cell" style="background:#fff5f5"><div class="sl-card" style="background:#d6eff3;border-color:#1a5c6b;border-width:2px;color:#111111"><ul><li>Claim adjudication &amp; closure</li><li>OSHA recordkeeping if required by directive</li></ul></div></td></tr>
    </tbody>
  </table>
  <div class="sl-legend">
    <b>Phases:</b> <span class="sl-swatch" style="background:#dce9f5;border-color:#2c5f8a"></span>1 &mdash; Prevention &nbsp; <span class="sl-swatch" style="background:#fce8e4;border-color:#8B2500"></span>2 &mdash; Immediate Response &nbsp; <span class="sl-swatch" style="background:#fdf6dc;border-color:#8a5a00"></span>3 &mdash; Reporting &nbsp; <span class="sl-swatch" style="background:#e6f2e0;border-color:#3b5e2b"></span>4 &mdash; Investigation &nbsp; <span class="sl-swatch" style="background:#d6eff3;border-color:#1a5c6b"></span>5 &mdash; Follow-up &amp; Close&nbsp;&nbsp; <span class="esc-badge" style="font-size:9px">&#8681; badge</span> = cross-lane escalation / notification
  </div>
</div>
