# Rules and characteristics (paraphrased)

Paraphrased from the INCOSE Guide to Writing Requirements v4 summary sheet
(INCOSE-TP-2010-006-04, June 2023). Copyright (c) 2023 by INCOSE. See the
`NOTICE` file for the full copyright notice. The numbers and names match the
source, so findings can cite them.

Text marked "Skill convention" is guidance from this skill, not from the
summary sheet. "Auto" marks rules for which `scripts/req_lint.py` has partial
heuristics. Review every applicable rule in context, including those with no
automated finding. Neither an empty finding list nor this table proves conformance.

## Characteristics of one statement (C1-C9)

| ID | Name | Meaning in short |
|---|---|---|
| C1 | Necessary | It states a capability, characteristic, constraint or quality that a lifecycle concept, need, source or higher-level requirement requires. |
| C2 | Appropriate | Its intent and detail suit the level of the entity it applies to: the level of abstraction, organization or architecture. |
| C3 | Unambiguous | Each intended reader understands it in only one way. |
| C4 | Complete | It gives the capability, characteristic, constraint, conditions or quality that its parent or source needs. |
| C5 | Singular | It states one capability, characteristic, constraint or quality. |
| C6 | Feasible | It can be met within the constraints of the entity (cost, schedule, technical, legal, ethical, safety) with acceptable risk. |
| C7 | Verifiable | Its wording lets you show that it is met to the satisfaction of the approving authority: by validation for a need, by verification for a requirement. |
| C8 | Correct | It represents its lifecycle concept, need, source or higher-level requirement accurately. |
| C9 | Conforming | It follows an approved standard pattern and the style guide for needs and requirements. |

## Characteristics of a set (C10-C15)

| ID | Name | Meaning in short |
|---|---|---|
| C10 | Complete | The set stands alone. It covers what the entity needs at its level without another set. |
| C11 | Consistent | Each entry is unique. No two entries conflict or overlap. Units and measurement systems are the same throughout. The same words mean the same thing, and terms match the architecture model, the project glossary and the project data dictionary. |
| C12 | Feasible | The whole set can be met together within the constraints of the entity, with acceptable risk. |
| C13 | Comprehensible | A reader can tell what the entity must do and how it relates to the larger system that it is part of. |
| C14 | Able to be validated | You can show that the set of needs leads to the goals, expectations and lifecycle concepts, and that the set of requirements leads to the needs and higher-level requirements. |
| C15 | Correct | The set as a whole represents its concepts, needs, sources or parents accurately. |

## Rules R1-R42

| ID | Name | What to check | Auto |
|---|---|---|---|
| R1 | Structured Statements | The statement follows one of the agreed patterns. Skill convention: a requirement uses "shall" and a need uses "need" (patterns in `../SKILL.md`). | yes |
| R2 | Active Voice | The responsible entity is the subject. The checker flags some "shall be <verb>ed by" forms; other passive constructions still need review. | yes |
| R3 | Appropriate Subject-Verb | The subject and verb suit the entity that the statement refers to. | |
| R4 | Defined Terms | Each term is defined in the glossary or data dictionary. | |
| R5 | Definite Articles | Use "the", not "a". | yes |
| R6 | Common Units of Measure | Each number has an explicit, consistent unit in one common measurement system, in terms of the thing that the number refers to. | yes |
| R7 | Vague Terms | No vague amounts such as some, any, allowable, several, many, a lot of, a few, almost always, very nearly, nearly, about, close to, almost, approximate. No vague adjectives such as ancillary, relevant, routine, common, generic, significant, flexible, expandable, typical, sufficient, adequate, appropriate, efficient, effective, proficient, reasonable, customary. Skill convention: the checker also flags user-friendly and easy. | yes |
| R8 | Escape Clauses | No "so far as is possible", "as little as possible", "where possible", "as much as possible", "if it should prove necessary", "if necessary", "to the extent necessary", "as appropriate", "as required", "to the extent practical", "if practicable". | yes |
| R9 | Open-Ended Clauses | No "including but not limited to", "etc.", "and so on". | yes |
| R10 | Superfluous Infinitives | No "to be designed to", "to be able to", "to be capable of", "to enable", "to allow". | yes |
| R11 | Separate Clauses | Use a separate clause for each condition or qualification. | |
| R12-R14 | Correct Grammar, Spelling, Punctuation | Use correct grammar, spelling and punctuation. The sheet names R14 "Correct Punctuation" on page 3 and "Correct Condition" in its matrix on page 4. This skill follows page 3. | |
| R15 | Logical Expressions | Use a defined convention for logical expressions, such as `[X AND Y]`, `[X OR Y]`, `[X XOR Y]`, `NOT [X OR Y]`. Skill convention: write "and/or" as one of these. | yes |
| R16 | Use of "Not" | Avoid "not". | yes |
| R17 | Use of Oblique Symbol | No "/" except in units (km/h) and fractions. | yes |
| R18 | Single Thought Sentence | One sentence with one thought, conditioned and qualified by sub-clauses. The checker flags more than one "shall". | yes |
| R19 | Combinators | Avoid words that join clauses: and, or, then, unless, but, as well as, but also, however, whether, meanwhile, whereas, on the other hand, otherwise. The checker ignores AND, OR and XOR inside an R15 bracket. | yes |
| R20 | Purpose Phrases | No phrase that gives the purpose of, the intent of or the reason for the statement. Skill convention: put the reason in the rationale attribute (A1). | yes |
| R21 | Parentheses | No parentheses or brackets that contain subordinate text. An R15 logical expression is not subordinate text. Skill convention: the markers `[TBD]` and `[TBR]` after a value are allowed, from the management of unknowns in the Needs and Requirements Manual (NRM). | yes |
| R22 | Enumeration | Name each member of a set instead of a group noun. | |
| R23 | Supporting Diagram, Model, or ICD | For complex behavior, refer to the diagram, model or interface control document (ICD) that supports it. | |
| R24 | Pronouns | No personal or indefinite pronouns. The checker also flags this, these and those. | yes |
| R25 | Headings | The statement does not depend on its heading to be understood. | |
| R26 | Absolutes | No unachievable absolutes: 100 % reliability, 100 % availability, all, every, always, never. | yes |
| R27 | Explicit Conditions | State when the statement applies. Do not leave it to context. | |
| R28 | Multiple Conditions | For one action with several conditions, state how the conditions combine. Do not give a list of actions for one condition. | |
| R29 | Classification | Classify each entry by the aspect of the problem or system that it addresses. Skill convention: function, performance, interface, constraint or quality. | |
| R30 | Unique Expression | Each need or requirement appears once and only once. | |
| R31 | Solution Free | No implementation unless a rationale justifies the constraint on the design. | |
| R32 | Universal Qualification | Use "each" instead of "all", "any" or "both" for universal quantification. | yes |
| R33 | Range of Values | Each quantity has a range of values, suited to the entity, against which the entity is verified or validated. | |
| R34 | Measurable Performance | Each performance target is specific and measurable. Skill convention: the checker flags words such as fast, high, minimize and optimize even when an unrelated number occurs elsewhere. A finding still needs contextual review for a defined, measurable target. | yes |
| R35 | Temporal Dependencies | Define timing explicitly. Avoid eventually, until, before, after, as, once, earliest, latest, instantaneous, simultaneous, at last. | yes |
| R36 | Consistent Terms and Units | Each term and unit matches the project ontology across the sets, the models and the other artifacts. | |
| R37 | Acronyms | Each acronym is used the same way across the sets, the models and the other artifacts. | |
| R38 | Abbreviations | Avoid abbreviations. | |
| R39 | Style Guide | Use a project-wide style guide. | |
| R40 | Decimal Format | Use one decimal format and a consistent number of significant digits. | |
| R41 | Related Needs and Requirements | Group related needs and requirements. | |
| R42 | Structured Sets | Organize the set to a defined structure or template, such as the register columns in `levels-and-attributes.md`. | |
