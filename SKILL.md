---
name: incose-requirements
description: |
  Check, classify, write and revise needs and requirements with the INCOSE
  needs-and-requirements model: need statements, design input requirements
  and design output specifications. Check each statement against the INCOSE
  Guide to Writing Requirements v4 rules R1-R42 and characteristics C1-C15.
  Use when the user states something the system must do or be: a goal, a
  threshold, a gate, a constraint, an acceptance criterion, "we need", "must",
  "shall", "target", "at least". Use when you write or revise a requirement
  register, a plan acceptance clause, a design decision or an interface
  obligation. Use when a derived requirement proves infeasible or too costly.
  Also use when the user says INCOSE, GtWR, NRM, need statement, design input,
  design output, derived requirement, traceability, TBD or TBR.
license: Apache-2.0
compatibility: claude-code codex
metadata:
  version: "1.1.1"
  source: "INCOSE Guide to Writing Requirements v4 summary sheet, INCOSE-TP-2010-006-04, June 2023"
---

# INCOSE needs and requirements

This skill turns statements from the owner, the plan and the design records into
well-formed needs and requirements, and preserves the meaning of their trace
relations. It has three modes:

1. **Check.** Classify a statement, test it against the rules, and propose a
   rewrite. Use this mode during a session when the user says something that
   reads like a need or a requirement.
2. **Write.** Add or edit entries in the requirement register.
3. **Change.** Revise a derived requirement when evidence shows that it is
   infeasible, too costly or too complex. Keep its parent unchanged.

## Artifact kind and entity level

Need statements, design input requirements and design output specifications
are artifact kinds in the summary sheet's life-cycle figure. They are not
three levels of an architecture. Record the entity and its architectural or
organizational level separately. A system, subsystem, element or organization
can have needs and design input requirements appropriate to its own level
(GtWR C2). A module name alone does not make a statement a design output.

| Artifact kind | What it states | Verification and validation | Who changes it |
|---|---|---|---|
| **Need statement** (ID `N-…`) | An agreed stakeholder expectation for an entity to perform a function or have a quality within constraints. Avoid implementation detail unless a recorded rationale justifies a design constraint (GtWR R31). | Needs verification: are the needs defined correctly? Needs validation: are we building the right thing? The realized system is **validated** against the needs. | Only the stakeholders, through the owner |
| **Design input requirement** (ID `DIR-…`) | An agreed, verifiable obligation transformed from sources, needs or higher-level requirements for the entity. Avoid implementation detail unless a recorded rationale justifies a design constraint (GtWR R31). | Requirements verification: are the requirements defined correctly? Requirements validation: are we building the right thing? The realized system is **verified** against the design input requirements. | The owner, with a recorded change and its effects |
| **Design output specification** (ID `DOS-…`) | An output of a chosen architecture or design that specifies a candidate or element to satisfy design input requirements. | Design verification: did we design it right? Design validation: do we have the right design? | The design owner, subject to applicable approved requirements and decisions |

Skill conventions, not from the summary sheet (the sheet refers to the
patterns in Appendix C of the full Guide):

- Need pattern: `The <stakeholders> need the <entity> to <capability> <condition>.`
- Requirement pattern: `When <condition>, the <entity> shall <action> <object> <performance with range>.`
  A design output specification uses the same pattern with the design
  element as the subject.
- Do not label requirements "hard" or "soft". Show flexibility with the artifact kind
  and the attributes instead (see `references/levels-and-attributes.md`).

## Trace relations

Skill convention: use typed relations rather than treating every link as
parent-child derivation. The vocabulary below is skill guidance, not a
prescribed INCOSE schema. Record the relation, its direction and target ID or
revision in the owning record; do not create a parallel register.

- **Source:** the originating document or owner direction (A3).
- **Derivation:** a child obligation transformed from a parent need or
  requirement (A2), with rationale that preserves the parent's intent.
- **Allocation:** assignment of an obligation or performance budget to an
  entity (A5). Allocation is not, by itself, a newly agreed need.
- **Satisfaction:** a design output's claimed fulfillment of a requirement.
  A link alone does not prove fulfillment.
- **Decision:** the architecture or design decision governing a design output.
- **Dependency:** an interface or dependent peer (A32, A33).
- **Verification/validation:** criteria and evidence assessing a specified
  obligation or need; retain the distinction between the two activities.
- **Supersession:** the recorded replacement relationship between revisions
  or decisions, preserving their lifecycle and approval history.

A need does not change because a design is hard. A design change still has to
meet applicable approved obligations. Source requirements from outside the
project keep their source identity and wording. Trace project entries to them
through A3. The conceptual ability to define subsystem needs does not change
the owner-approved entity scope or authorize new agreed entries.

## Classify a statement

First identify the entity, its architectural or organizational level, the
source and approval state. Then classify the statement by its role:

1. A stakeholder expectation for the entity is a **need**. A documented
   rationale can justify a design constraint here under GtWR R31.
2. A verifiable obligation supplied as input to design for that entity is a
   **design input requirement**. It may be derived from sources, needs or
   higher-level requirements, including allocation to a subsystem. GtWR R31
   permits a design constraint here only with a documented rationale.
3. A specification produced by a chosen architecture or design is a **design
   output specification**. Judge its role and provenance; naming a module,
   technique or candidate product is insufficient to determine its kind.
4. A test threshold, gate or pass mark is often a success criterion (A6).
   Determine which obligation it assesses. A gate with its own obligation may
   be a requirement. Do not turn a proposed criterion into an agreed value.
5. A plan step or task belongs in the project plan; an architecture decision
   belongs in a decision record. Neither automatically creates a product requirement.

## Check procedure

1. Run the automated checker on the statements:
   `python3 <skill-folder>/scripts/req_lint.py <file>`
   (one statement per line), or pipe text on standard input. Add `--json` for
   machine output and `--terms <file>` for the project's multi-word defined
   terms. The checker finds wording problems only. Its findings are
   candidates, not verdicts.
2. Review every applicable GtWR R1-R42 in `references/rules.md` in context,
   including rules marked "Auto" when the checker reports no finding. Those
   checks are partial heuristics; silence is not a pass. Confirm or reject
   findings, record justified not-applicable dispositions, and identify any
   rules left unreviewed. Do not claim full rule coverage from lint alone.
3. Judge each characteristic of the statement, C1 to C9. Give C7 verifiable
   and C2 appropriate to level the most care, because no checker finds them.
4. Check the set, not only the statement: C10 to C15, R30 each statement
   once, R41 related entries together and R42 structured set.
5. Report in this form:
   - artifact kind, entity, architectural or organizational level and proposed ID;
   - the rewritten statement;
   - a table of findings: rule, problem, fix. Cite rules as `GtWR R7`,
     so that a reader does not confuse them with other IDs such as risk numbers;
   - typed trace relations, including parent (A2), source (A3) and allocation (A5);
   - missing minimum attributes (see `references/levels-and-attributes.md`);
   - values that are not yet known, marked **TBD** (to be determined) or
     **TBR** (to be resolved: a proposed value that is not agreed);
   - the proposed statement verification status (A28) and statement
     validation status (A29).

## Session behavior

- When the user says something requirement-like, give a short check: artifact kind,
  rewrite and the top findings. Do not stop the user's task to do this. Put a
  full check in the report or the register edit.
- Do not check casual speech, questions or plans that are not stated as
  obligations.
- An owner decision comes only from the user in chat. Record its date. A
  statement that an agent drafted "on the owner's behalf" stays **proposed**
  until the owner agrees to it. Preserve the originating chat reference and
  reviewed statement revision. Apply authorization already given for that
  revision and scope; do not ask for the same approval again.
- Never edit the canonical register to make a check pass. Propose the edit, and
  apply it when the user asks.

## Change a derived requirement

When evidence shows that a child is infeasible, too costly or too complex:

1. Record the evidence: command or method, date, result and limits.
2. Keep the parent. Propose another child that still meets the parent, or a
   new value for a TBR.
3. If no child can meet the parent, say that the **parent is at risk** and
   route the decision to the owner. Never weaken a need to fit a design.
4. Follow the project's change workflow for authority, revision history, impact
   review, evidence applicability and closure. Apply already authorized changes
   to the owning row in place. Keep the ID and the prior approved revision; do
   not transfer its approval to changed meaning. Record the old value, the new
   value, the reason, the date, unresolved impacts and residual work there.
5. Set attribute A26, stability, to `volatile` for a child that changes often.

## Project rules that apply

- Keep one register of needs and requirements for each entity. If the project
  has a register, use it and follow its column rules. If it has none, propose
  the columns in `references/levels-and-attributes.md`.
- Keep source requirements in the records that own them. Trace to them. Do not
  copy them.
- Keep verification results and implementation status in the record that owns
  them. Link to that record from the register.
- A test path is a candidate for coverage. It is not evidence that a
  requirement is met. Keep "implemented", "verified" and "qualified" separate.
- Never change frozen test protocols or their thresholds to meet a
  requirement. A changed criterion needs a new, versioned registration.

## Source and notice

The rules, characteristics, attribute names, definitions and the
verification and validation questions in this skill and its `references/`
folder are paraphrased from the *INCOSE Guide to Writing Requirements v4 –
Summary Sheet* (INCOSE-TP-2010-006-04, June 2023), by the INCOSE Requirements
Working Group. The life-cycle figure in that sheet is by M. Ryan and
L. Wheatcraft. Copyright (c) 2023 by INCOSE. The `NOTICE` file in this skill
folder contains the full INCOSE copyright notice, which the sheet requires in
each derivative work.

The statement patterns, the ID scheme, the procedures, the register columns,
the worked example and each item marked "Skill convention" are guidance from
this skill. They are not INCOSE text. The skill does not quote the full Guide
or the Needs and Requirements Manual. Get those from the INCOSE store. This
skill is not an INCOSE product.
