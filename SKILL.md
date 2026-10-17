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
  version: "1.0.0"
  source: "INCOSE Guide to Writing Requirements v4 summary sheet, INCOSE-TP-2010-006-04, June 2023"
---

# INCOSE needs and requirements

This skill turns statements from the owner, the plan and the design records into
well-formed needs and requirements, and keeps the parent-child trace between
them. It has three modes:

1. **Check.** Classify a statement, test it against the rules, and propose a
   rewrite. Use this mode during a session when the user says something that
   reads like a need or a requirement.
2. **Write.** Add or edit entries in the requirement register.
3. **Change.** Revise a derived requirement when evidence shows that it is
   infeasible, too costly or too complex. Keep its parent unchanged.

## The three levels

The INCOSE Needs and Requirements Manual (NRM) separates three kinds of
statement. Use these terms. Do not use "hard" and "soft" requirements.

| Level | What it states | Pattern | Checked by | Who changes it |
|---|---|---|---|---|
| **Need statement** (ID `N-…`) | An expectation that the stakeholders agreed: what the entity must do or be, from their point of view. It contains no solution. | `The <stakeholders> need the <entity> to <capability> <condition>.` | **Validation:** are we building the right thing? | Only the stakeholders, through the owner |
| **Design input requirement** (ID `DIR-…`) | A verifiable obligation on the entity, transformed from one or more needs. It is still free of design choices, unless a rationale justifies a constraint. | `When <condition>, the <entity> shall <action> <object> <performance with range>.` | **Verification:** did we build it right? | The owner, with a recorded change and its effect on the parent need |
| **Design output specification** (ID `DOS-…`) | What a chosen architecture or design must do to meet the design input requirements: the specification for one candidate or element. | The same requirement pattern, with the design element as the subject | Design verification | The design owner. A design change replaces it. |

Rules that follow from the levels:

- A need does not change because a design is hard. A design input requirement
  changes only with a recorded reason. A design output specification changes
  whenever the design changes.
- "Derived requirement" means a child that is traced to a parent. A design input
  requirement is derived from needs. A design output specification is derived
  from design input requirements through an architecture decision. A child at
  the next level of the architecture (a subsystem) gets its own needs and
  design input requirements, allocated from the parent.
- Source requirements from outside the project (a customer specification, a
  contract or a standard) keep their source identity. Never rewrite them.
  Trace project needs to them as attribute A3, trace to source.

## Classify a statement

Ask these questions in order:

1. Does it say what a stakeholder expects, in the stakeholder's terms, with no
   design? It is a **need**.
2. Does it oblige the entity (a system, a subsystem, a software library) to a
   measurable result, independent of which design is chosen? It is a **design
   input requirement**.
3. Does it name a design element, a candidate product, a module or a
   technique? It is a **design output specification**, unless a rationale
   makes it a constraint at the design input level. Rule R31 allows such a
   constraint only with a rationale.
4. Is it a test threshold, a gate or a pass mark? It is usually the
   success criterion (attribute A6) of a design input requirement, not a
   separate requirement. A gate that has its own obligation becomes a design
   input requirement.
5. Is it a plan step, a task or a decision about who does what? It is not a
   requirement. It belongs in the project plan or a decision record.

## Check procedure

1. Run the automated checker on the statements:
   `python3 <skill-folder>/scripts/req_lint.py <file>`
   (one statement per line), or pipe text on standard input. Add `--json` for
   machine output and `--terms <file>` for the project's multi-word defined
   terms. The checker finds wording problems only. Its findings are
   candidates, not verdicts.
2. Then judge the rules that need context (see `references/rules.md`):
   C1 necessary, C2 appropriate to level, C6 feasible, C8 correct against the
   parent, R4 defined terms, R23 reference to an interface definition or
   model, R27 explicit conditions, R31 solution free, R33 range of values,
   R34 measurable performance.
3. Check the set, not only the statement: C10 complete, C11 consistent (no
   overlap, same units, same terms), C12 feasible together, R30 each statement
   once.
4. Report in this form:
   - level and proposed ID;
   - the rewritten statement;
   - a table of findings: rule, problem, fix. Cite rules as `GtWR R7`, so
     that a reader does not confuse them with other IDs such as risk numbers;
   - parent (A2) and source (A3);
   - missing minimum attributes (see `references/levels-and-attributes.md`);
   - values that are not yet known, marked **TBD** (to be determined) or
     **TBR** (to be resolved: a proposed value that is not agreed).

## Session behavior

- When the user says something requirement-like, give a short check: level,
  rewrite and the top findings. Do not stop the user's task to do this. Put a
  full check in the report or the register edit.
- Do not check casual speech, questions or plans that are not stated as
  obligations.
- An owner decision comes only from the user in chat. Record its date. A
  statement that an agent drafted "on the owner's behalf" stays **proposed**
  until the owner agrees to it.
- Never edit the canonical register to make a check pass. Propose the edit, and
  apply it when the user asks.

## Change a derived requirement

When evidence shows that a child is infeasible, too costly or too complex:

1. Record the evidence: command or method, date, result and limits.
2. Keep the parent. Propose another child that still meets the parent, or a
   new value for a TBR.
3. If no child can meet the parent, say that the **parent is at risk** and
   send it to the owner. Never weaken a need to fit a design.
4. Update the owning row in place. Keep the ID. Record the old value, the new
   value, the reason and the date. Do not add a second register.
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

The rules, characteristics, attribute names and level definitions in this skill
and its `references/` folder are paraphrased from the *INCOSE Guide to Writing
Requirements v4 – Summary Sheet* (INCOSE-TP-2010-006-04, June 2023), by the
INCOSE Requirements Working Group. The life-cycle figure in that sheet is by
M. Ryan and L. Wheatcraft. Copyright (c) 2023 by INCOSE. The summary sheet
grants permission to reproduce it and to make derivative works, with
attribution and its copyright notice. Get the full Guide, the Needs and
Requirements Manual and the Guide to Needs and Requirements from the INCOSE
store. This skill paraphrases only the summary sheet. It does not use the full
Guide or the NRM, and it is not an INCOSE product.
