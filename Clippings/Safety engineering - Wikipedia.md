---
title: Safety engineering - Wikipedia
source: https://en.wikipedia.org/wiki/Safety_engineering
author: "[[Contributors to Wikimedia projects]]"
published: 2001-12-16
created: 2025-07-23
description:
tags:
  - clippings
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/ISS_impact_risk.jpg/330px-ISS_impact_risk.jpg)

NASA's illustration showing high impact risk areas for the International Space Station

**Safety engineering** is an [engineering](https://en.wikipedia.org/wiki/Engineering "Engineering") [discipline](https://en.wikipedia.org/wiki/Branches_of_science "Branches of science") which assures that engineered [systems](https://en.wikipedia.org/wiki/System "System") provide acceptable levels of [safety](https://en.wikipedia.org/wiki/Safety "Safety"). It is strongly related to [industrial engineering](https://en.wikipedia.org/wiki/Industrial_engineering "Industrial engineering") / [systems engineering](https://en.wikipedia.org/wiki/Systems_engineering "Systems engineering"), and the subset [system safety](https://en.wikipedia.org/wiki/System_safety "System safety") engineering. Safety engineering assures that a [life-critical system](https://en.wikipedia.org/wiki/Life-critical_system "Life-critical system") behaves as needed, even when components [fail](https://en.wikipedia.org/wiki/Failure "Failure").

## Analysis techniques

Analysis techniques can be split into two categories: [qualitative](https://en.wikipedia.org/wiki/Qualitative_research "Qualitative research") and [quantitative](https://en.wikipedia.org/wiki/Quantitative_research "Quantitative research") methods. Both approaches share the goal of finding causal dependencies between a [hazard](https://en.wikipedia.org/wiki/Hazard "Hazard") on system level and failures of individual components. Qualitative approaches focus on the question "What must go wrong, such that a system hazard may occur?", while quantitative methods aim at providing estimations about probabilities, rates and/or severity of consequences.

The complexity of the technical systems such as Improvements of Design and Materials, Planned Inspections, Fool-proof design, and Backup Redundancy decreases risk and increases the cost. The risk can be decreased to ALARA (as low as reasonably achievable) or ALAPA (as low as practically achievable) levels.

Traditionally, safety analysis techniques rely solely on skill and expertise of the safety engineer. In the last decade [model-based](https://en.wikipedia.org/wiki/Model-based_systems_engineering "Model-based systems engineering") approaches, like STPA (Systems Theoretic Process Analysis), have become prominent. In contrast to traditional methods, model-based techniques try to derive relationships between causes and consequences from some sort of model of the system.

The two most common fault modeling techniques are called [failure mode and effects analysis](https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis "Failure mode and effects analysis") (FMEA) and [fault tree analysis](https://en.wikipedia.org/wiki/Fault_tree_analysis "Fault tree analysis") (FTA). These techniques are just ways of finding problems and of making plans to cope with failures, as in [probabilistic risk assessment](https://en.wikipedia.org/wiki/Probabilistic_risk_assessment "Probabilistic risk assessment"). One of the earliest complete studies using this technique on a commercial nuclear plant was the [WASH-1400](https://en.wikipedia.org/wiki/WASH-1400 "WASH-1400") study, also known as the Reactor Safety Study or the Rasmussen Report.

Failure Mode and Effects Analysis (FMEA) is a bottom-up, [inductive](https://en.wikipedia.org/wiki/Inductive_reasoning "Inductive reasoning") analytical method which may be performed at either the functional or piece-part level. For functional FMEA, failure modes are identified for each function in a system or equipment item, usually with the help of a functional [block diagram](https://en.wikipedia.org/wiki/Block_diagram "Block diagram"). For piece-part FMEA, failure modes are identified for each piece-part component (such as a valve, connector, resistor, or diode). The effects of the failure mode are described, and assigned a probability based on the [failure rate](https://en.wikipedia.org/wiki/Failure_rate "Failure rate") and failure mode ratio of the function or component. This quantization is difficult for software ---a bug exists or not, and the failure models used for hardware components do not apply. Temperature and age and manufacturing variability affect a resistor; they do not affect software.

Failure modes with identical effects can be combined and summarized in a Failure Mode Effects Summary. When combined with criticality analysis, FMEA is known as [Failure Mode, Effects, and Criticality Analysis](https://en.wikipedia.org/wiki/Failure_Mode,_Effects,_and_Criticality_Analysis "Failure Mode, Effects, and Criticality Analysis") or FMECA.

Fault tree analysis (FTA) is a top-down, [deductive](https://en.wikipedia.org/wiki/Deductive_reasoning "Deductive reasoning") analytical method. In FTA, initiating primary events such as component failures, human errors, and external events are traced through [Boolean logic](https://en.wikipedia.org/wiki/Boolean_logic "Boolean logic") gates to an undesired top event such as an aircraft crash or nuclear reactor core melt. The intent is to identify ways to make top events less probable, and verify that safety goals have been achieved.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Fault_tree.svg/250px-Fault_tree.svg.png)

A fault tree diagram

Fault trees are a logical inverse of success trees, and may be obtained by applying [de Morgan's theorem](https://en.wikipedia.org/wiki/De_Morgan%27s_laws "De Morgan's laws") to success trees (which are directly related to [reliability block diagrams](https://en.wikipedia.org/wiki/Reliability_block_diagram "Reliability block diagram")).

FTA may be qualitative or quantitative. When failure and event probabilities are unknown, qualitative fault trees may be analyzed for minimal cut sets. For example, if any minimal cut set contains a single base event, then the top event may be caused by a single failure. Quantitative FTA is used to compute top event probability, and usually requires computer software such as CAFTA from the [Electric Power Research Institute](https://en.wikipedia.org/wiki/Electric_Power_Research_Institute "Electric Power Research Institute") or [SAPHIRE](https://en.wikipedia.org/wiki/SAPHIRE "SAPHIRE") from the [Idaho National Laboratory](https://en.wikipedia.org/wiki/Idaho_National_Laboratory "Idaho National Laboratory").

Some industries use both fault trees and [event trees](https://en.wikipedia.org/wiki/Event_tree "Event tree"). An event tree starts from an undesired initiator (loss of critical supply, component failure etc.) and follows possible further system events through to a series of final consequences. As each new event is considered, a new node on the tree is added with a split of probabilities of taking either branch. The probabilities of a range of "top events" arising from the initial event can then be seen.

The offshore oil and gas industry uses a qualitative safety systems analysis technique to ensure the protection of offshore production systems and platforms. The analysis is used during the design phase to identify process engineering hazards together with risk mitigation measures. The methodology is described in the [American Petroleum Institute](https://en.wikipedia.org/wiki/American_Petroleum_Institute "American Petroleum Institute") Recommended Practice 14C *Analysis, Design, Installation, and Testing of Basic Surface Safety Systems for Offshore Production Platforms.*

The technique uses system analysis methods to determine the safety requirements to protect any individual process component, e.g. a vessel, [pipeline](https://en.wikipedia.org/wiki/Pipeline_transport "Pipeline transport"), or [pump](https://en.wikipedia.org/wiki/Pump "Pump").[^1] The safety requirements of individual components are integrated into a complete platform safety system, including liquid containment and emergency support systems such as fire and gas detection.[^1]

The first stage of the analysis identifies individual process components, these can include: flowlines, headers, [pressure vessels](https://en.wikipedia.org/wiki/Pressure_vessel "Pressure vessel"), atmospheric vessels, [fired heaters](https://en.wikipedia.org/wiki/Industrial_furnace "Industrial furnace"), exhaust heated components, pumps, [compressors](https://en.wikipedia.org/wiki/Compressor "Compressor"), pipelines and [heat exchangers](https://en.wikipedia.org/wiki/Heat_exchanger "Heat exchanger").[^2] Each component is subject to a safety analysis to identify undesirable events (equipment failure, process upsets, etc.) for which protection must be provided.[^3] The analysis also identifies a detectable condition (e.g. [high pressure](https://en.wikipedia.org/wiki/High_pressure "High pressure")) which is used to initiate actions to prevent or minimize the effect of undesirable events. A Safety Analysis Table (SAT) for pressure vessels includes the following details.[^3] [^4]

<table><tbody><tr><th colspan="3">Safety Analysis Table (SAT) pressure vessels</th></tr><tr><th>Undesirable event</th><th>Cause</th><th>Detectable abnormal condition</th></tr><tr><td>Overpressure</td><td>Blocked or restricted outlet<p>Inflow exceeds outflow</p><p>Gas blowby (from upstream)</p><p>Pressure control failure</p><p>Thermal expansion</p><p>Excess heat input</p></td><td>High pressure</td></tr><tr><td>Liquid overflow</td><td>Inflow exceeds outflow<p>Liquid slug flow</p><p>Blocked or restricted liquid outlet</p><p>Level control failure</p></td><td>High liquid level</td></tr></tbody></table>

Other undesirable events for a pressure vessel are under-pressure, gas blowby, leak, and excess temperature together with their associated causes and detectable conditions.[^4]

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Vessel_level_instrumentation.jpg/250px-Vessel_level_instrumentation.jpg)

Vessel level instrumentation

Once the events, causes and detectable conditions have been identified the next stage of the methodology uses a Safety Analysis Checklist (SAC) for each component.[^5] This lists the safety devices that may be required or factors that negate the need for such a device. For example, for the case of liquid overflow from a vessel (as above) the SAC identifies:[^6]

- A4.2d - High level sensor (LSH) [^7]
	- 1\. LSH installed.
	- 2\. Equipment downstream of gas outlet is not a flare or vent system and can safely handle maximum liquid carry-over.
	- 3\. Vessel function does not require handling of separate fluid phases.
	- 4\. Vessel is a small trap from which liquids are manually drained.
![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Vessel_pressure_instrumentation.jpg/250px-Vessel_pressure_instrumentation.jpg)

Vessel pressure instrumentation

The analysis ensures that two levels of protection are provided to mitigate each undesirable event. For example, for a pressure vessel subjected to over-pressure the primary protection would be a PSH (pressure switch high) to shut off inflow to the vessel, secondary protection would be provided by a [pressure safety valve](https://en.wikipedia.org/wiki/Safety_valve "Safety valve") (PSV) on the vessel.[^8]

The next stage of the analysis relates all the sensing devices, shutdown valves (ESVs), trip systems and emergency support systems in the form of a Safety Analysis Function Evaluation (SAFE) chart.[^2] [^9]

<table><tbody><tr><th colspan="4" rowspan="2">Safety Analysis Function Evaluation (SAFE) chart</th><td>Close inlet valve</td><td>Close outlet valve</td><td>Alarm</td></tr><tr><td>ESV-1a</td><td>ESV-1b</td><td></td></tr><tr><td>Identification</td><td>Service</td><td>Device</td><td>SAC reference</td><td></td><td></td><td></td></tr><tr><td rowspan="5">V-1</td><td rowspan="5">HP separator</td><td>PSH</td><td>A4.2a1</td><td>X</td><td></td><td>X</td></tr><tr><td>LSH</td><td>A4.2d1</td><td>X</td><td></td><td>X</td></tr><tr><td>LSL</td><td>A4.2e1</td><td></td><td>X</td><td>X</td></tr><tr><td>PSV</td><td>A4.2c1</td><td></td><td></td><td></td></tr><tr><td>etc.</td><td></td><td></td><td></td><td></td></tr><tr><td>V-2</td><td>LP separator</td><td>etc.</td><td></td><td></td><td></td><td></td></tr></tbody></table>

X denotes that the detection device on the left (e.g. PSH) initiates the shutdown or warning action on the top right (e.g. ESV closure).

The SAFE chart constitutes the basis of Cause and Effect Charts which relate the sensing devices to [shutdown valves](https://en.wikipedia.org/wiki/Shut_down_valve "Shut down valve") and plant trips which defines the functional architecture of the [process shutdown](https://en.wikipedia.org/wiki/Plant_process_and_emergency_shutdown_systems#Process_shutdown_\(PSD\) "Plant process and emergency shutdown systems") system.

The methodology also specifies the systems testing that is necessary to ensure the functionality of the protection systems.[^10]

API RP 14C was first published in June 1974.[^11] The 8th edition was published in February 2017.[^12] API RP 14C was adapted as ISO standard ISO 10418 in 1993 entitled *Petroleum and natural gas industries — Offshore production installations — Analysis, design, installation and testing of basic surface process safety systems.*[^13] The latest edition of ISO 10418 was published in 2019. [^14]

## Safety certification

Typically, safety guidelines prescribe a set of steps, deliverable documents, and exit criterion focused around planning, analysis and design, implementation, verification and validation, configuration management, and quality assurance activities for the development of a safety-critical system.[^15] In addition, they typically formulate expectations regarding the creation and use of [traceability](https://en.wikipedia.org/wiki/Requirements_traceability "Requirements traceability") in the project. For example, depending upon the criticality level of a requirement, the [US Federal Aviation Administration](https://en.wikipedia.org/wiki/Federal_Aviation_Administration "Federal Aviation Administration") guideline [DO-178B/C](https://en.wikipedia.org/wiki/DO-178C "DO-178C") requires [traceability](https://en.wikipedia.org/wiki/Requirements_traceability "Requirements traceability") from [requirements](https://en.wikipedia.org/wiki/Requirement "Requirement") to [design](https://en.wikipedia.org/wiki/Design "Design"), and from [requirements](https://en.wikipedia.org/wiki/Requirement "Requirement") to [source code](https://en.wikipedia.org/wiki/Source_code "Source code") and executable [object code](https://en.wikipedia.org/wiki/Object_code "Object code") for software components of a system. Thereby, higher quality traceability information can simplify the certification process and help to establish trust in the maturity of the applied development process.[^16]

Usually a failure in safety- [certified](https://en.wikipedia.org/wiki/Product_certification "Product certification") systems is acceptable if, on average, less than one life per 10 <sup>9</sup> hours of continuous operation is lost to failure.{as per FAA document AC 25.1309-1A} Most Western [nuclear reactors](https://en.wikipedia.org/wiki/Nuclear_reactors "Nuclear reactors"), medical equipment, and commercial [aircraft](https://en.wikipedia.org/wiki/Aircraft "Aircraft") are certified to this level. The cost versus loss of lives has been considered appropriate at this level (by [FAA](https://en.wikipedia.org/wiki/FAA "FAA") for aircraft systems under [Federal Aviation Regulations](https://en.wikipedia.org/wiki/Federal_Aviation_Regulations "Federal Aviation Regulations")).[^17] [^18] [^19]

## Preventing failure

![](https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Survival_redundancy.svg/250px-Survival_redundancy.svg.png)

A NASA graph shows the relationship between the survival of a crew of astronauts and the amount of redundant equipment in their spacecraft (the "MM", Mission Module).

Once a failure mode is identified, it can usually be mitigated by adding extra or redundant equipment to the system. For example, nuclear reactors contain dangerous [radiation](https://en.wikipedia.org/wiki/Radiation "Radiation"), and nuclear reactions can cause so much [heat](https://en.wikipedia.org/wiki/Heat "Heat") that no substance might contain them. Therefore, reactors have emergency core cooling systems to keep the temperature down, shielding to contain the radiation, and engineered barriers (usually several, nested, surmounted by a [containment building](https://en.wikipedia.org/wiki/Containment_building "Containment building")) to prevent accidental leakage. [Safety-critical systems](https://en.wikipedia.org/wiki/Safety-critical_system "Safety-critical system") are commonly required to permit no [single event or component failure](https://en.wikipedia.org/wiki/Single_point_of_failure "Single point of failure") to result in a catastrophic failure mode.

Most [biological](https://en.wikipedia.org/wiki/Biology "Biology") organisms have a certain amount of redundancy: multiple organs, multiple limbs, etc.

For any given failure, a fail-over or redundancy can almost always be designed and incorporated into a system.

There are two categories of techniques to reduce the probability of failure: Fault avoidance techniques increase the reliability of individual items (increased design margin, de-rating, etc.). Fault tolerance techniques increase the reliability of the system as a whole (redundancies, barriers, etc.).[^20]

Safety engineering and reliability engineering have much in common, but safety is not reliability. If a medical device fails, it should fail safely; other alternatives will be available to the surgeon. If the engine on a single-engine aircraft fails, there is no backup. Electrical power grids are designed for both safety and reliability; telephone systems are designed for reliability, which becomes a safety issue when emergency (e.g. US [911](https://en.wikipedia.org/wiki/911_\(emergency_telephone_number\) "911 (emergency telephone number)")) calls are placed.

[Probabilistic risk assessment](https://en.wikipedia.org/wiki/Probabilistic_risk_assessment "Probabilistic risk assessment") has created a close relationship between safety and reliability. Component reliability, generally defined in terms of component [failure rate](https://en.wikipedia.org/wiki/Failure_rate "Failure rate"), and external event probability are both used in quantitative safety assessment methods such as FTA. Related probabilistic methods are used to determine system [Mean Time Between Failure (MTBF)](https://en.wikipedia.org/wiki/Mean_time_between_failures "Mean time between failures"), system availability, or probability of mission success or failure. Reliability analysis has a broader scope than safety analysis, in that non-critical failures are considered. On the other hand, higher failure rates are considered acceptable for non-critical systems.

Safety generally cannot be achieved through component reliability alone. Catastrophic failure probabilities of 10 <sup>−9</sup> per hour correspond to the failure rates of very simple components such as [resistors](https://en.wikipedia.org/wiki/Resistor "Resistor") or [capacitors](https://en.wikipedia.org/wiki/Capacitor "Capacitor"). A complex system containing hundreds or thousands of components might be able to achieve a MTBF of 10,000 to 100,000 hours, meaning it would fail at 10 <sup>−4</sup> or 10 <sup>−5</sup> per hour. If a system failure is catastrophic, usually the only practical way to achieve 10 <sup>−9</sup> per hour failure rate is through redundancy.

When adding equipment is impractical (usually because of expense), then the least expensive form of design is often "inherently fail-safe". That is, change the system design so its failure modes are not catastrophic. Inherent fail-safes are common in medical equipment, traffic and railway signals, communications equipment, and safety equipment.

The typical approach is to arrange the system so that ordinary single failures cause the mechanism to shut down in a safe way (for nuclear power plants, this is termed a [passively safe](https://en.wikipedia.org/wiki/Passive_nuclear_safety "Passive nuclear safety") design, although more than ordinary failures are covered). Alternately, if the system contains a hazard source such as a battery or rotor, then it may be possible to remove the hazard from the system so that its failure modes cannot be catastrophic. The U.S. Department of Defense Standard Practice for System Safety (MIL–STD–882) places the highest priority on elimination of hazards through design selection.[^21]

One of the most common fail-safe systems is the overflow tube in baths and kitchen sinks. If the valve sticks open, rather than causing an overflow and damage, the tank spills into an overflow. Another common example is that in an [elevator](https://en.wikipedia.org/wiki/Elevator "Elevator") the cable supporting the car keeps [spring-loaded brakes](https://en.wikipedia.org/w/index.php?title=Spring-loaded_brake&action=edit&redlink=1 "Spring-loaded brake (page does not exist)") open. If the cable breaks, the brakes grab rails, and the elevator cabin does not fall.

Some systems can never be made fail safe, as continuous availability is needed. For example, loss of engine thrust in flight is dangerous. Redundancy, fault tolerance, or recovery procedures are used for these situations (e.g. multiple independent controlled and fuel fed engines). This also makes the system less sensitive for the reliability prediction errors or quality induced uncertainty for the separate items. On the other hand, failure detection & correction and avoidance of common cause failures becomes here increasingly important to ensure system level reliability.[^22]

## See also

- [ARP4761](https://en.wikipedia.org/wiki/ARP4761 "ARP4761") – Aerospace recommended practice from SAE International
- [Earthquake engineering](https://en.wikipedia.org/wiki/Earthquake_engineering "Earthquake engineering") – Study of earthquake-resistant structures
- [Effective safety training](https://en.wikipedia.org/wiki/Effective_safety_training "Effective safety training")
- [Forensic engineering](https://en.wikipedia.org/wiki/Forensic_engineering "Forensic engineering") – Investigation of failures associated with legal intervention
- [Hazard and operability study](https://en.wikipedia.org/wiki/Hazard_and_operability_study "Hazard and operability study") – Study of risks in a plan or operation
- [IEC 61508](https://en.wikipedia.org/wiki/IEC_61508 "IEC 61508") – International standard for safety-related systems
- [Loss-control consultant](https://en.wikipedia.org/wiki/Loss-control_consultant "Loss-control consultant")
- [Nuclear safety](https://en.wikipedia.org/wiki/Nuclear_safety "Nuclear safety") – Regulations for uses of radioactive materials
- [Occupational medicine](https://en.wikipedia.org/wiki/Occupational_medicine "Occupational medicine") – Medical specialty concerned with the maintenance of health in the workplace
- [Occupational safety and health](https://en.wikipedia.org/wiki/Occupational_safety_and_health "Occupational safety and health") – Field concerned with the safety, health and welfare of people at work
- [Process safety](https://en.wikipedia.org/wiki/Process_safety "Process safety") – Study, prevention, and management of major hazardous material accidents in process plants
- [Reliability engineering](https://en.wikipedia.org/wiki/Reliability_engineering "Reliability engineering") – Sub-discipline of systems engineering that emphasizes dependability
- [Risk assessment](https://en.wikipedia.org/wiki/Risk_assessment "Risk assessment") – Estimation of risk associated with exposure to a given set of hazards
- [Risk management](https://en.wikipedia.org/wiki/Risk_management "Risk management") – Identification, evaluation and control of risks
- [Safety life cycle](https://en.wikipedia.org/wiki/Safety_life_cycle "Safety life cycle")
- [Zonal safety analysis](https://en.wikipedia.org/wiki/Zonal_safety_analysis "Zonal safety analysis")

### Associations

- [Institute of Industrial Engineers](https://en.wikipedia.org/wiki/Institute_of_Industrial_Engineers "Institute of Industrial Engineers") – Professional society for the support of the industrial engineering profession
- [International System Safety Society](http://www.system-safety.org/)

## References

### Notes

### Sources

- [Lees, Frank](https://en.wikipedia.org/wiki/Frank_Lees "Frank Lees") (2005). *Loss Prevention in the Process Industries* (3 ed.). Elsevier. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-7506-7555-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-7506-7555-0 "Special:BookSources/978-0-7506-7555-0").
- [Kletz, Trevor](https://en.wikipedia.org/wiki/Trevor_Kletz "Trevor Kletz") (1984). *Cheaper, safer plants, or wealth and safety at work: notes on inherently safer and simpler plants*. I.Chem.E. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-85295-167-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-85295-167-5 "Special:BookSources/978-0-85295-167-5").
- [Kletz, Trevor](https://en.wikipedia.org/wiki/Trevor_Kletz "Trevor Kletz") (2001). *An Engineer's View of Human Error* (3 ed.). I.Chem.E. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-85295-430-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-85295-430-0 "Special:BookSources/978-0-85295-430-0").
- [Kletz, Trevor](https://en.wikipedia.org/wiki/Trevor_Kletz "Trevor Kletz") (1999). *HAZOP and HAZAN* (4 ed.). Taylor & Francis. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-85295-421-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-85295-421-8 "Special:BookSources/978-0-85295-421-8").
- [Lutz, Robyn R.](https://en.wikipedia.org/wiki/Robyn_Lutz "Robyn Lutz") (2000). [*Software Engineering for Safety: A Roadmap*](http://www.cs.ucl.ac.uk/staff/A.Finkelstein/fose/finallutz.pdf) (PDF). The Future of Software Engineering. ACM Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-58113-253-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-58113-253-3 "Special:BookSources/978-1-58113-253-3"). Retrieved 31 August 2006.
- Grunske, Lars; Kaiser, Bernhard; Reussner, Ralf H. (2005). ["Specification and Evaluation of Safety Properties in a Component-based Software Engineering Process"](https://researchbank.swinburne.edu.au/file/51c018aa-fef1-4d08-a8ff-0f0d4237770d/1/PDF%20%28Accepted%20manuscript%29.pdf) (PDF). *Component-Based Software Development for Embedded Systems*. Lecture Notes in Computer Science. Vol. 3778. Springer. pp. 737– 738. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.69.7756](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.69.7756). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/11591962\_13](https://doi.org/10.1007%2F11591962_13). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-30644-3](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-30644-3 "Special:BookSources/978-3-540-30644-3").
- [US DOD](https://en.wikipedia.org/wiki/United_States_Department_of_Defense "United States Department of Defense") (10 February 2000). [*Standard Practice for System Safety*](http://www.faa.gov/regulations_policies/handbooks_manuals/aviation/risk_management/ss_handbook/media/app_h_1200.pdf) (PDF). Washington, DC: US DOD. MIL-STD-882D. Retrieved 7 September 2013.
- [US FAA](https://en.wikipedia.org/wiki/Federal_Aviation_Administration "Federal Aviation Administration") (30 December 2000). [*System Safety Handbook*](http://www.faa.gov/regulations_policies/handbooks_manuals/aviation/risk_management/ss_handbook/). Washington, DC: US FAA. Retrieved 7 September 2013.
- [NASA](https://en.wikipedia.org/wiki/NASA "NASA") (16 December 2008). [*Agency Risk Management Procedural Requirements*](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_8000_004A_). NASA. NPR 8000.4A.
- Leveson, Nancy (2011). [*Engineering a Safer World - Systems Thinking Applied To Safety*](http://sunnyday.mit.edu/safer-world/index.html). Engineering Systems. The MIT Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-262-01662-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-01662-9 "Special:BookSources/978-0-262-01662-9"). Retrieved 3 July 2012.

## External links

- [U.S. Army Pamphlet 385-16 System Safety Management Guide](http://www.apd.army.mil/jw2/xmldemo/p385_16/head.asp)

[^1]: API RP 14C p.1

[^2]: API RP 14C p.vi

[^3]: API RP 14C p.15-16

[^4]: API RP 14C p.28

[^5]: API RP 14C p.57

[^6]: API RP 14C p.29

[^7]: ["ISO 14617-1:2005 Graphical symbols for diagrams — Part 1: General information and indexes"](https://www.iso.org/standard/41838.html). [International Organization for Standardization](https://en.wikipedia.org/wiki/International_Organization_for_Standardization "International Organization for Standardization").

[^8]: API RP 14C p.10

[^9]: API RP 14C p.80

[^10]: API RP 14C Appendix D

[^11]: Farrell, Tim (1978). ["Impact of API 14C on the Design And Construction of Offshore Facilities"](https://www.onepetro.org/conference-paper/SPE-7147-MS). *All Days*. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2118/7147-MS](https://doi.org/10.2118%2F7147-MS). Retrieved 7 February 2019.

[^12]: ["API RP 14C"](https://global.ihs.com/doc_detail.cfm?document_name=API%20RP%2014C&item_s_key=00010460). Retrieved 7 February 2019.

[^13]: ["ISO 10418"](https://www.iso.org/standard/38067.html). Retrieved 7 February 2019.

[^14]: ["ISO 10418"](https://www.iso.org/standard/55440.html). Retrieved 2 January 2025.

[^15]: Rempel, Patrick; Mäder, Patrick; Kuschke, Tobias; [Cleland-Huang, Jane](https://en.wikipedia.org/wiki/Jane_Cleland-Huang "Jane Cleland-Huang") (2014-01-01). "Mind the gap: Assessing the conformance of software traceability to relevant guidelines". *Proceedings of the 36th International Conference on Software Engineering*. ICSE 2014. New York, NY, USA: ACM. pp. 943– 954. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.660.2292](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.660.2292). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/2568225.2568290](https://doi.org/10.1145%2F2568225.2568290). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9781450327565](https://en.wikipedia.org/wiki/Special:BookSources/9781450327565 "Special:BookSources/9781450327565"). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [12976464](https://api.semanticscholar.org/CorpusID:12976464).

[^16]: Mäder, P.; Jones, P. L.; Zhang, Y.; [Cleland-Huang, J.](https://en.wikipedia.org/wiki/Jane_Cleland-Huang "Jane Cleland-Huang") (2013-05-01). "Strategic Traceability for Safety-Critical Projects". *IEEE Software*. **30** (3): 58– 66. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/MS.2013.60](https://doi.org/10.1109%2FMS.2013.60). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0740-7459](https://search.worldcat.org/issn/0740-7459). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [16905456](https://api.semanticscholar.org/CorpusID:16905456).

[^17]: ANM-110 (1988). [*System Design and Analysis*](http://www.faa.gov/documentLibrary/media/Advisory_Circular/AC%2025.1309-1A.pdf) (PDF). [Federal Aviation Administration](https://en.wikipedia.org/wiki/Federal_Aviation_Administration "Federal Aviation Administration"). Advisory Circular AC 25.1309-1A. Retrieved 2011-02-20.`{{[cite book](https://en.wikipedia.org/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: numeric names: authors list ()

[^18]: S–18 (2010). [*Guidelines for Development of Civil Aircraft and Systems*](http://standards.sae.org/arp4754a). [Society of Automotive Engineers](https://en.wikipedia.org/wiki/Society_of_Automotive_Engineers "Society of Automotive Engineers"). ARP4754A.`{{[cite book](https://en.wikipedia.org/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: numeric names: authors list ()

[^19]: S–18 (1996). [*Guidelines and methods for conducting the safety assessment process on civil airborne systems and equipment*](http://www.sae.org/technical/standards/ARP4761). [Society of Automotive Engineers](https://en.wikipedia.org/wiki/Society_of_Automotive_Engineers "Society of Automotive Engineers"). ARP4761.`{{[cite book](https://en.wikipedia.org/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: numeric names: authors list ()

[^20]: Tommaso Sgobba.["Commercial Space Safety Standards: Let's Not Re-Invent the Wheel"](http://www.spacesafetymagazine.com/spaceflight/commercial-spaceflight/commercial-space-safety-standards-lets-not-re-invent-wheel/). 2015.

[^21]: [*Standard Practice for System Safety*](https://web.archive.org/web/20170131151951/https://acc.dau.mil/adl/en-US/683694/file/75173/MIL-STD-882E%20Final%202012-05-11.pdf) (PDF). E. [U.S. Department of Defense](https://en.wikipedia.org/wiki/United_States_Department_of_Defense "United States Department of Defense"). 1998. MIL-STD-882. Archived from [the original](https://acc.dau.mil/adl/en-US/683694/file/75173/MIL-STD-882E%20Final%202012-05-11.pdf) (PDF) on 2017-01-31. Retrieved 2012-05-11.

[^22]: Bornschlegl, Susanne (2012). [*Ready for SIL 4: Modular Computers for Safety-Critical Mobile Applications*](https://www.menmicro.com/downloads/search/dl/sk/%22White%20Paper%3A%20Ready%20for%20SIL4%3A%20Modular%20Computers%20for%20Safety-Critical%20Mobile%20Applications%22/dx/1/) (pdf). MEN Mikro Elektronik. Retrieved 2015-09-21.