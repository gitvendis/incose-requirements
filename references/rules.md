# Rules and characteristics (paraphrased)

Paraphrased from the INCOSE Guide to Writing Requirements v4 summary sheet
(INCOSE-TP-2010-006-04, June 2023). Copyright (c) 2023 by INCOSE. See the notice
in `../SKILL.md`. The numbers match the source, so findings can cite them.

"Auto" marks the rules that `scripts/req_lint.py` finds. The checker finds
candidates only. Judge each one in context.

## Characteristics of one statement (C1-C9)

| ID | Name | Meaning in short |
|---|---|---|
| C1 | Necessary | It states something that a parent need, source or concept actually requires. Remove it, and something is missing. |
| C2 | Appropriate | Its detail suits the level of the entity it applies to: no design detail in a need, no system-wide claim on a module. |
| C3 | Unambiguous | Each reader understands it in only one way. |
| C4 | Complete | It gives the capability, conditions and performance that its parent needs. Nothing is left implied. |
| C5 | Singular | It states one capability, characteristic, constraint or quality. |
| C6 | Feasible | It can be met within cost, schedule, technical, legal, ethical and safety limits, with acceptable risk. |
| C7 | Verifiable | You can show that it is met: by validation for a need, by verification for a requirement. |
| C8 | Correct | It represents its parent or source accurately. |
| C9 | Conforming | It follows the agreed pattern and the project style guide. |

## Characteristics of a set (C10-C15)

| ID | Name | Meaning in short |
|---|---|---|
| C10 | Complete | The set covers what the entity needs at its level without depending on another set. |
| C11 | Consistent | Each entry is unique. No two entries conflict or overlap. Units and terms are the same throughout and match the glossary and architecture model. |
| C12 | Feasible | The whole set can be met together within the limits. |
| C13 | Comprehensible | A reader can tell what the entity must do and how it fits into the larger system. |
| C14 | Able to be validated | You can show that meeting the set meets the needs and higher-level requirements. |
| C15 | Correct | The set as a whole represents its parents or sources accurately. |

## Rules R1-R42

| ID | Name | What to check | Auto |
|---|---|---|---|
| R1 | Structured statements | The statement follows one agreed pattern (see `../SKILL.md`). A requirement uses "shall". A need uses "need". | yes |
| R2 | Active voice | The responsible entity is the subject. Flag "shall be <verb>ed by". | yes |
| R3 | Appropriate subject and verb | The subject is the entity at this level, and the verb is something that entity can do. | |
| R4 | Defined terms | Each term is in the project glossary or the register's definitions. Example: "reference workstation". | |
| R5 | Definite articles | Use "the", not "a" or "an", for the entity and its objects. | yes |
| R6 | Units of measure | Each number has an explicit unit in one measurement system. | yes |
| R7 | Vague terms | No vague amounts or adjectives such as some, several, many, about, nearly, approximately, sufficient, adequate, appropriate, efficient, typical, flexible, significant, reasonable. | yes |
| R8 | Escape clauses | No "where possible", "as far as possible", "if necessary", "as required", "as appropriate", "if practicable". | yes |
| R9 | Open-ended clauses | No "including but not limited to", "etc.", "and so on". | yes |
| R10 | Superfluous infinitives | No "be able to", "be capable of", "be designed to", "to enable", "to allow". | yes |
| R11 | Separate clauses | Each condition or qualification has its own clause. | |
| R12-R14 | Grammar, spelling, punctuation | Correct grammar, spelling and punctuation. | |
| R15 | Logical expressions | Use a defined convention such as `[X AND Y]`, `[X OR Y]`. No "and/or". | yes |
| R16 | Use of "not" | Avoid "not". State what the entity does. | yes |
| R17 | Oblique symbol | No "/" except in units (km/h) and fractions. | yes |
| R18 | Single thought | One sentence, one thought, with its sub-clauses. Flag more than one "shall". | yes |
| R19 | Combinators | Avoid words that join two thoughts: and, or, then, unless, but, as well as, however, whether, whereas, otherwise. | yes |
| R20 | Purpose phrases | No "in order to", "so that", "for the purpose of". Put the reason in the rationale attribute (A1). | yes |
| R21 | Parentheses | No text in brackets or parentheses. The markers `[TBD]` and `[TBR]` after a value are allowed. | yes |
| R22 | Enumeration | Name each member of a set instead of a group noun. | |
| R23 | Diagram, model or ICD | For complex behavior, refer to the interface control document (ICD), model or diagram that defines it. | |
| R24 | Pronouns | No personal or indefinite pronouns: it, they, this, these, those. | yes |
| R25 | Headings | The statement makes sense without its heading. | |
| R26 | Absolutes | No unreachable absolutes: 100 %, all, every, always, never. | yes |
| R27 | Explicit conditions | State when the statement applies. Do not leave it to context. | |
| R28 | Multiple conditions | For one action with several conditions, state how the conditions combine. | |
| R29 | Classification | Classify each entry (function, performance, interface, constraint, quality). | |
| R30 | Unique expression | Each need or requirement appears once in the set. | |
| R31 | Solution free | No design or implementation unless a rationale justifies the constraint. | |
| R32 | Universal quantification | Use "each" instead of "all", "any" or "both". | yes |
| R33 | Range of values | Each quantity has a range or tolerance against which the entity is verified. | |
| R34 | Measurable performance | Each performance claim has a specific, measurable target. Flag "fast", "high", "minimize", "optimize" without a number. | yes |
| R35 | Temporal dependencies | Define timing explicitly. Avoid eventually, until, before, after, once, earliest, latest, instantaneous, simultaneous. | yes |
| R36 | Consistent terms and units | Terms and units match the project ontology across the whole set and the models. | |
| R37 | Acronyms | Each acronym is used the same way everywhere and is in the glossary. | |
| R38 | Abbreviations | Avoid abbreviations. | |
| R39 | Style guide | Follow the project style guide. | |
| R40 | Decimal format | Use one decimal format and a consistent number of significant digits. | |
| R41 | Related entries together | Group related needs and requirements. | |
| R42 | Structured sets | Organize the set to a defined template, such as the register columns in `levels-and-attributes.md`. | |
