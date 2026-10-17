# INCOSE Requirements skill

![INCOSE Requirements skill: a person and a robot turn a need into a checked requirement](assets/logo.jpg)

This skill helps an AI coding agent write and test needs and requirements. It uses the needs-and-requirements model of INCOSE, the International Council on Systems Engineering. It also uses the 42 rules of the INCOSE Guide to Writing Requirements (GtWR) v4. The skill works with Claude Code and Codex. The current version is 1.1.0.

## What the skill does

The skill sorts each statement into one of three levels:

1. A need statement tells what the stakeholders expect. It contains no design.
2. A design input requirement is an obligation on the system that a test can verify.
3. A design output specification tells what one chosen design must do.

The skill then tests each statement against the GtWR rules and proposes a rewrite. It keeps the trace from each child statement to its parent. If a derived requirement costs too much or cannot be met, the skill changes the child and keeps the parent need.

## Install

Clone the repository into the skills folder of your agent. For Claude Code, run this command:

```bash
git clone https://github.com/gitvendis/incose-requirements.git ~/.claude/skills/incose-requirements
```

For one project only, clone it into `.claude/skills/incose-requirements` in that project. For Codex, clone it into `.agents/skills/incose-requirements` in the project. The agent uses the skill when you state a goal, a threshold or a requirement. You can also ask for the skill by name.

## Run the linter alone

The folder includes `scripts/req_lint.py`, a linter (a tool that finds wording problems). It needs Python 3 and no other packages. Put one statement on each line of a text file, then run this command:

```bash
python3 scripts/req_lint.py statements.txt
```

Add `--json` for output that a program can read. Add `--strict` to exit with status 1 when a statement has a finding. Add `--terms <file>` to name the multi-word terms of your project, so that the linter does not split them. The linter finds candidates only. A person must still judge necessity, feasibility and the trace to the parent.

## Files

The skill has four files. The agent reads `SKILL.md` first and opens the other files when it needs them.

| File | Contents |
|---|---|
| `SKILL.md` | The three levels, the classification questions, the test procedure and the change procedure |
| `references/rules.md` | Characteristics C1 to C15 and rules R1 to R42, with the rules that the linter finds |
| `references/levels-and-attributes.md` | Definitions, attributes A1 to A49, suggested register columns and a worked example |
| `scripts/req_lint.py` | The linter |

## Source and license

The rules are paraphrased from the INCOSE Guide to Writing Requirements v4 Summary Sheet (INCOSE-TP-2010-006-04, June 2023). That sheet is Copyright (c) 2023 by INCOSE. Its copyright notice must stay with each derivative work, so `NOTICE` contains the notice in full. The statement patterns, procedures and examples are guidance from this project. This project is not an INCOSE product. For the full Guide and the Needs and Requirements Manual, go to the INCOSE store.

This project is released under the Apache License 2.0. Read `LICENSE` and `NOTICE` for the terms.
