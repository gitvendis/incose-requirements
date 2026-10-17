#!/usr/bin/env python3
"""Flag wording problems in need and requirement statements.

The rule numbers follow the INCOSE Guide to Writing Requirements v4 summary
sheet (INCOSE-TP-2010-006-04, June 2023; Copyright (c) 2023 by INCOSE). The
checker finds candidates only. It cannot judge necessity, feasibility,
correctness against a parent or whether a statement is free of design.

Usage:
    req_lint.py [FILE ...] [--json] [--strict]

Each non-empty line that does not start with "#" is one statement. A line may
start with an ID followed by a colon or a tab, for example "DIR-SYS-003: The ...".
Reads standard input when no file is given. Exit status is 0, or 1 with
--strict when a statement has a finding.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass

VAGUE = [
    "some", "any", "allowable", "several", "many", "a lot of", "a few",
    "almost always", "very nearly", "nearly", "about", "close to", "almost",
    "approximate", "approximately", "ancillary", "relevant", "routine", "common",
    "generic", "significant", "flexible", "expandable", "typical", "sufficient",
    "adequate", "appropriate", "efficient", "effective", "proficient",
    "reasonable", "customary",
    # Skill convention: not in the GtWR R7 list.
    "user-friendly", "easy",
]
ESCAPE = [
    "so far as is possible", "as far as possible", "as little as possible",
    "where possible", "as much as possible", "if it should prove necessary",
    "if necessary", "to the extent necessary", "as appropriate", "as required",
    "to the extent practical", "if practicable",
]
OPEN_ENDED = ["including but not limited to", "etc", "and so on"]
INFINITIVES = [
    "be designed to", "be able to", "be capable of", "to enable", "to allow",
]
COMBINATORS = [
    "and", "or", "then", "unless", "but", "as well as", "but also", "however",
    "whether", "meanwhile", "whereas", "on the other hand", "otherwise",
]
PURPOSE = [
    "in order to", "so that", "purpose of", "intent of", "reason for",
    "with the intent",
]
PRONOUNS = ["it", "its", "they", "them", "their", "this", "these", "those", "he", "she"]
ABSOLUTES = ["all", "every", "always", "never", "100%", "100 %"]
UNIVERSAL = ["all", "any", "both"]
TEMPORAL = [
    "eventually", "until", "before", "after", "once", "earliest", "latest",
    "instantaneous", "instantaneously", "simultaneous", "simultaneously", "at last",
]
# Phrases that contain "as" but are not a temporal "as" (GtWR R35). The R8 and
# R19 phrases are reported by their own rules.
NOT_TEMPORAL_AS = [
    "as well as", "such as", "as follows", "as specified in", "as defined in",
    "the same as", "as far as possible", "so far as is possible",
    "as little as possible", "as much as possible", "as appropriate",
    "as required",
]
# An R15 logical expression: a bracket with AND, OR or XOR in capitals, or a
# NOT before a bracket. It is not subordinate text (R21) or a combinator (R19).
LOGICAL = re.compile(r"(?:\bNOT\s+)?\[[^\]]*\b(?:AND|OR|XOR)\b[^\]]*\]")
UNMEASURED = [
    "fast", "faster", "slow", "quick", "quickly", "high", "higher", "low",
    "lower", "large", "small", "improve", "minimize", "minimise", "maximize",
    "maximise", "optimize", "optimise", "real time", "real-time",
]
WEAK_MODALS = ["should", "may", "might", "could", "will", "must", "can"]
UNITS = re.compile(
    r"^(%|percent|ms|s|sec|seconds?|minutes?|min|hours?|h|hr|days?|hz|khz|mhz|"
    r"ghz|db|dbm|dbw|w|kw|mw|m|km|nm|nmi|ft|kg|g|gb|mb|tb|kb|cores?|x|×|"
    r"entities|entity|runs?|replications?|episodes?|instances?|workers?|"
    r"vignettes?|seeds?|times|knots?|kt|deg|degrees?|rad|lux|k|items?|"
    r"l|litres?|liters?|ml|bar|pa|kpa|psi|n|nm|v|a|ma|°c|°f|c)(?!\w)",
    re.IGNORECASE,
)


EXTRA_TERMS: list[str] = []


@dataclass
class Finding:
    rule: str
    text: str
    hint: str


def _has_phrase(statement: str, phrase: str) -> bool:
    pattern = r"(?<![\w-])" + re.escape(phrase) + r"(?![\w-])"
    return re.search(pattern, statement, re.IGNORECASE) is not None


def _phrases(statement: str, phrases: list[str]) -> list[str]:
    return [p for p in phrases if _has_phrase(statement, p)]


# Multi-word defined terms (GtWR R4) are masked before the word checks, so the
# "and" or "common" inside a term is not read as a combinator or vague word.
# Add project terms with --terms <file>.
DEFINED_TERMS = [
    "command and control", "measures of effectiveness",
    "measures of performance", "capability and performance",
    "research and development", "operations and maintenance",
]
TBX = re.compile(r"\s*\[(?:TBD|TBR|TBS)\]", re.IGNORECASE)


def check(statement: str) -> tuple[str, list[Finding]]:
    # "[TBD]" and "[TBR]" mark values that are not yet known or agreed.
    s = TBX.sub("", statement.strip())
    s = LOGICAL.sub("LOGIC", s)
    for term in DEFINED_TERMS + EXTRA_TERMS:
        s = re.sub(re.escape(term), "TERM", s, flags=re.IGNORECASE)
    low = s.lower()
    findings: list[Finding] = []
    is_req = _has_phrase(low, "shall")
    is_need = re.search(r"\bneeds?\b", low) is not None and not is_req
    kind = "requirement" if is_req else "need" if is_need else "unclassified"

    def add(rule: str, words: list[str] | str, hint: str) -> None:
        if words:
            text = ", ".join(words) if isinstance(words, list) else words
            findings.append(Finding(rule, text, hint))

    if kind == "unclassified":
        modals = _phrases(low, WEAK_MODALS)
        add("R1", "no 'shall' or 'need'" + (f" (uses {', '.join(modals)})" if modals else ""),
            "Use 'The <stakeholders> need the <entity> to ...' or "
            "'The <entity> shall ...'.")
    if is_req and len(re.findall(r"\bshall\b", low)) > 1:
        add("R18", "more than one 'shall'", "Split into one statement per obligation.")
    if is_req and re.search(r"\bshall\s+be\s+\w+(ed|en)\b(?:\s+\w+){0,4}\s+\bby\b", low):
        add("R2", "passive 'shall be ... by'", "Make the responsible entity the subject.")
    if re.search(r"^(when [^,]*,\s*)?(a|an)\s", low):
        add("R5", "indefinite article at the subject", "Use 'the' for the entity.")
    # "any" is reported once, under R32.
    add("R7", [w for w in _phrases(low, VAGUE) if w != "any"],
        "Replace with a measurable value or a defined term.")
    add("R8", _phrases(low, ESCAPE), "Remove the escape clause; state the condition.")
    add("R9", _phrases(low, OPEN_ENDED), "Enumerate each member of the set.")
    add("R10", _phrases(low, INFINITIVES), "Use the verb directly: 'shall <verb>'.")
    if _has_phrase(low, "and/or"):
        add("R15", "and/or", "Use [X AND Y] or [X OR Y] explicitly.")
    if re.search(r"\bnot\b|n't\b", low):
        add("R16", "not", "State what the entity does instead.")
    for m in re.finditer(r"(\S+)/(\S+)", s):
        left, right = m.group(1), m.group(2)
        is_unit = re.search(r"\d", left) or (len(left) <= 4 and len(right) <= 4 and left.isalpha())
        if not is_unit and m.group(0).lower() != "and/or":
            add("R17", m.group(0), "Avoid '/'; use words, except in units and fractions.")
    combos = [w for w in _phrases(low, COMBINATORS) if w not in ("and", "or") or is_req]
    add("R19", combos, "Check whether two thoughts are joined; split if so.")
    add("R20", _phrases(low, PURPOSE), "Move the purpose into the rationale attribute.")
    if re.search(r"[()\[\]]", s):
        add("R21", "parentheses or brackets", "Remove subordinate text in brackets.")
    add("R24", _phrases(low, PRONOUNS), "Replace the pronoun with the noun it refers to.")
    add("R26", _phrases(low, ABSOLUTES), "Avoid unreachable absolutes; use 'each' or a value.")
    add("R32", [w for w in _phrases(low, UNIVERSAL) if w != "all" or "R26" not in
                [f.rule for f in findings]],
        "Use 'each' for universal quantification. 'Any' is also an R7 vague term.")
    temporal = _phrases(low, TEMPORAL)
    as_text = low
    for phrase in NOT_TEMPORAL_AS:
        as_text = re.sub(re.escape(phrase), " ", as_text)
    if _has_phrase(as_text, "as"):
        temporal.append("as")
    add("R35", temporal, "State the timing explicitly with a value.")
    has_number = re.search(r"\d", s) is not None
    if not has_number:
        add("R34", _phrases(low, UNMEASURED), "Give a measurable target and range.")
    for m in re.finditer(r"(?<![\w.-])(\d[\d,]*(?:\.\d+)?)(?![\w.-]*-)(\s*)(\S*)", s):
        before = s[max(0, m.start() - 12):m.start()].lower()
        if re.search(r"(§|section|sections|icd|adr|step|phase|stage|level|version|v|http|status|code|gate|rule|table|figure|appendix|chapter|item)\s*$", before):
            continue
        nxt = m.group(3).strip(".,;:")
        unit = nxt.split("/")[0].lower()
        # A unit, or a count of a named thing ("3 operators", "1 copy").
        counted = nxt.isalpha() and (nxt.lower().endswith("s") or m.group(1) == "1")
        if not nxt or not (UNITS.match(unit) or counted):
            add("R6", m.group(1), "Give the unit of measure for each number.")
    return kind, findings


def _split_id(line: str) -> tuple[str, str]:
    m = re.match(r"^\s*((?=[A-Z0-9-]*\d)[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)\s*[:\t]\s*(.+)$", line)
    return (m.group(1), m.group(2)) if m else ("", line.strip())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="*")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--terms", help="file with one extra defined term per line")
    args = parser.parse_args(argv)
    if args.terms:
        with open(args.terms, encoding="utf-8") as handle:
            EXTRA_TERMS.extend(t.strip() for t in handle if t.strip())

    lines: list[str] = []
    if args.files:
        for name in args.files:
            with open(name, encoding="utf-8") as handle:
                lines.extend(handle.read().splitlines())
    else:
        lines = sys.stdin.read().splitlines()

    results = []
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        ident, statement = _split_id(line)
        kind, findings = check(statement)
        results.append({"id": ident, "kind": kind, "statement": statement,
                        "findings": [asdict(f) for f in findings]})

    if args.json:
        json.dump(results, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for r in results:
            label = f"{r['id']} " if r["id"] else ""
            print(f"{label}[{r['kind']}] {r['statement']}")
            if not r["findings"]:
                print("  no wording findings (context rules still need review)")
            for f in r["findings"]:
                print(f"  {f['rule']}: {f['text']} -> {f['hint']}")
    flagged = any(r["findings"] for r in results)
    return 1 if args.strict and flagged else 0


if __name__ == "__main__":
    sys.exit(main())
