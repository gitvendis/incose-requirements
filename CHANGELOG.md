# Changelog

## 1.1.1 (2026-10-24)

This release ports the portable corrections from the requirements review pilot.

1. Artifact kind is separate from architectural or organizational level. Classification uses the statement's role and provenance, including justified design constraints.
2. Typed trace relations distinguish derivation, allocation, satisfaction, decisions, dependencies, evidence and supersession.
3. Review covers every applicable rule in context. The linter uses partial heuristics; an empty finding list does not prove conformance.
4. Register guidance checks meaningful values for all 16 starred minimum attributes without imposing a project's schema or inventing values.
5. Change guidance preserves approval provenance, reviewed revisions and existing authorization. Changed meaning does not inherit prior approval.
6. The linter flags an incomplete `shall` obligation and performance words even when a number occurs elsewhere. Defined terms remain configurable with `--terms`.
7. Bounded standard-library regression tests cover these wording cases and CLI behavior. They do not establish INCOSE conformance.

## 1.1.0 (2026-10-17)

This release corrects the skill against the INCOSE GtWR v4 summary sheet.

1. `NOTICE` now contains the full INCOSE copyright notice, which the summary sheet requires in each derivative work.
2. Each level now has its own verification and validation question, as in the summary sheet. The realized system is validated against the needs and verified against the design input requirements.
3. The suggested register columns now include the minimum attributes A5, A28 and A29.
4. The check procedure now covers each rule that the linter does not find, and characteristics C1 to C15.
5. The skill marks its own conventions, so that a reader can tell them from INCOSE text.
6. Rule names in `references/rules.md` now match the summary sheet.
7. The linter accepts R15 logical expressions such as `[X AND Y]`. It finds "as" (R35), "intent of" and "reason for" (R20). It accepts slash units such as `L/min`, flags a number that has no unit, and reports each word under one rule only.

## 1.0.0 (2026-10-17)

First public release. The release includes the skill, the rules and attributes references, a worked example and the `req_lint.py` linter.
