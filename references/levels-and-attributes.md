# Levels, attributes and a worked example

Paraphrased from the INCOSE Guide to Writing Requirements v4 summary sheet
(INCOSE-TP-2010-006-04, June 2023). Copyright (c) 2023 by INCOSE. See the
`NOTICE` file for the full copyright notice. Text marked "Skill convention" is
guidance from this skill, not from the summary sheet.

## Definitions

- **Entity:** one item that a concept, need or requirement applies to.
  Examples: an organization, a business unit, a project, a supplier, a service,
  a procedure, the system of interest (system, subsystem or system element), a
  product, a process, or a class of stakeholder such as users or operators.
- **Lifecycle concepts:** how the organization expects to acquire, build,
  verify, operate, maintain and retire the entity.
- **Need statement:** a formal transformation of sources or lifecycle concepts
  into an agreed expectation for the entity.
- **Integrated set of needs:** the agreed needs for one entity and its external
  interfaces. The finished entity is **validated** against it.
- **Requirement statement:** a formal transformation of sources, needs or
  higher-level requirements into an agreed obligation for the entity.
- **Design input requirements:** the set of requirement statements for one
  entity. The finished entity is **verified** against it.
- **Design output specifications:** the outputs of architecture and design
  definition. The realized element is built and verified to them.
- **Need expression or requirement expression:** the statement plus its
  attributes.

The life-cycle flow: stakeholder expectations → lifecycle concepts and needs
definition → integrated set of needs → design input requirements definition →
design input requirements → architecture and design definition → design output
specifications → implementation and integration → realized element.

Each artifact has its own verification and validation. Verification asks
whether the artifact was defined, designed or built correctly. Validation asks
whether it is still the right thing. The summary sheet names these checks:

| Artifact | Verification | Validation |
|---|---|---|
| Integrated set of needs | Needs verification: are the needs defined correctly? | Needs validation: are we building the right thing? |
| Design input requirements | Requirements verification: are the requirements defined correctly? | Requirements validation: are we building the right thing? |
| Design output specifications | Design verification: did we design it right? | Design validation: do we have the right design? |
| Realized system | System verification against the design input requirements: did we build it right? | System validation against the needs: did we build the right thing? |

Attributes A28 and A29 record the verification and validation status of the
statement itself. Attributes A13 and A14 record the results for the realized
system.

## Attributes

An asterisk marks the minimum set that the summary sheet recommends for each
entry.

| Group | Attributes |
|---|---|
| Intent | A1 Rationale\*, A2 Trace to parent\*, A3 Trace to source\*, A4 States and modes, A5 Allocation or budgeting\* |
| Verification and validation | A6 Success criteria\*, A7 Strategy\*, A8 Method\*, A9 Responsible organization\*, A10 Level, A11 Phase, A12 Condition of use, A13 Results, A14 Status |
| Maintenance | A15 Unique identifier\*, A16 Unique name, A17 Originator or author\*, A18 Date entered, A19 Owner\*, A20 Stakeholders, A21 Change board, A22 Change proposed, A23 Version, A24 Approval date, A25 Date of last change, A26 Stability or volatility, A27 Responsible person, A28 Verification status of the statement\*, A29 Validation status of the statement\*, A30 Status of the need or requirement, A31 Implementation status, A32 Trace to interface definition, A33 Trace to dependent peers, A34 Priority\*, A35 Criticality or essentiality\*, A36 Implementation risk\*, A37 Risk mitigation, A38 Key driving need or requirement, A39 Comments, A40 Type or category |
| Applicability and reuse | A41 Applicability, A42 Region, A43 Country, A44 State or province, A45 Market segment, A46 Business unit |
| Product line | A47 Product line, A48 Common entries, A49 Variant entries |

### Suggested register columns

Skill convention: if the project has no register yet, propose these columns.
They cover each attribute that the summary sheet marks with an asterisk.

| Column | Attributes | Notes |
|---|---|---|
| ID and name | A15, A16 | `N-<area>-NNN`, `DIR-<area>-NNN`, `DOS-<element>-NNN`. Never reuse an ID. |
| Level and type | A40, R29 | need, design input or design output; function, performance, interface, constraint or quality |
| Statement | — | One statement in the agreed pattern. Values not yet agreed are marked TBD or TBR. |
| Rationale | A1 | Why the entry exists. Put the purpose here, not in the statement (R20). |
| Parent and source | A2, A3, A32 | Parent IDs; source document, decision or owner direction with date; interface definition reference |
| Allocation | A5 | The child entity or the budget share that the entry is allocated to |
| Verification or validation | A6, A7, A8, A9 | Success criterion, method (test, analysis, inspection, demonstration), who does it |
| Owner and author | A19, A17 | |
| Priority, criticality, risk | A34, A35, A36, A38 | Mark key driving entries |
| Stability | A26 | `stable` or `volatile` |
| Statement verification and validation | A28, A29 | Is the statement defined correctly against the rules? Is it the right statement against its parent? `open`, `passed` or `failed`, with date |
| Status | A30, A24, A25 | `proposed`, `agreed` (with the owner's date), `baselined`, `retired` |

Keep the system verification and validation results (A13, A14) and the
implementation status (A31) in the record that owns them. Link to them. Do not
copy them.

## How flexibility is managed

Skill convention: do not label requirements "hard" or "soft". The summary
sheet does not use those terms. Show flexibility with two things:

1. **Level.** A need is the stable anchor. A design input requirement changes
   only with a recorded reason. A design output specification changes with the
   design.
2. **Attributes.** Priority (A34), criticality (A35), stability (A26), key
   driving status (A38) and TBD or TBR markings tell the reader which values
   are firm and which can move.

## Worked example

The entity is a backup service for project folders. Each statement below
passes `scripts/req_lint.py` with no wording findings. The context rules
still need a human review.

| ID | Statement | Rationale, parent and notes |
|---|---|---|
| N-BK-001 | The project teams need the backup service to return a lost project folder on the same working day. | Source: owner direction, with date. Validated with the project teams. |
| DIR-BK-001 | When the administrator requests the restore of the project folder, the backup service shall restore the project folder to the state of the most recent nightly backup within 4 hours [TBR]. | Parent N-BK-001. The value is proposed, not agreed, so it is marked TBR. |
| DIR-BK-002 | The backup service shall retain each nightly backup for 30 days. | Parent N-BK-001. A loss is sometimes found days later. |
| DIR-BK-003 | The backup service shall store each backup copy at the second site. | Parent N-BK-001. A constraint at the design input level. The rationale (one site fire must not destroy both copies) justifies it under GtWR R31. |
| DOS-OBJ-001 | The object storage design shall restore the 50 GB reference folder within 2 hours. | Parent DIR-BK-001. If the team picks another design, this entry is replaced. DIR-BK-001 and N-BK-001 stay unchanged. |
