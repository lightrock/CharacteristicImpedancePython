# AGENTS.md

This repository is an information-first physics research instrument. Treat it
like a chain-of-evidence project, not a casual numerology sandbox.

## Core Thesis

The project tests whether the pre-2019 CODATA significant-digit representation
of the characteristic impedance of vacuum (`Z0`) behaves like an unusually
generative binary information seed.

The stance is:

- Constants are compressed information artifacts produced by experiment,
  apparatus, theory, unit convention, uncertainty, rounding, and consensus.
- Units are encoding transformations to be tested, not a reason to dismiss the
  question.
- The project must expose its degrees of freedom: source catalog, encoding rule,
  transform, search target, baselines, and failure conditions.

Do not give the user grief about "mere units" or "mere numerology." The right
scientific response is to make the claim explicit, preserve evidence, add
controls, and let the tests decide.

## Evidence Boundaries

Keep these catalogs conceptually separate:

- `docs/codata/` is the official pre-2019 CODATA 2014 evidence chain.
  It contains 336 official rows parsed from the legacy NIST-style source.
- `docs/tokens/legacy-physics-token-catalog.md` and `.csv` preserve the
  non-CODATA rows that the legacy BigCalc2 project appended after the official
  NIST table.

The appended token rows include quark mass-signature tokens such as:

```text
Q_UP      2.2   -> 22   -> 10110
Q_DOWN    4.7   -> 47   -> 101111
Q_STRANGE 96    -> 96   -> 1100000
Q_CHARM   1.275 -> 1275 -> 10011111011
Q_BOTTOM  4.18  -> 418  -> 110100010
Q_TOP     173.1 -> 1731 -> 11011000011
```

The legacy project placed those rows in `NIST_CODATA.TXT` so the same software
could treat quarks, hadrons, and candidate mass signatures like named constants
during binary scans. Preserve that fact. Do not silently mix official CODATA and
legacy tokens without saying so.

## Quark-Token Scan Discipline

Short quark bit patterns are high-noise probes. Do not overinterpret raw hits
from tiny low-precision tokens such as `Q_UP` (`10110`) or raw `Q_DOWN`
(`101111`) without strong controls. Many unrelated constants will contain such
short patterns by chance.

For first-pass quark-grouping experiments, prioritize the longer and more
specific quark signatures:

```text
Q_CHARM   10011111011   length 11
Q_BOTTOM  110100010     length 9
Q_TOP     11011000011   length 11
```

Also prioritize the longer Z0 closure-style quark words preserved in the
Z0 binary-structure notes:

```text
DOWN closure word     10111101      length 8
STRANGE closure word  1100000011    length 10
```

Report token length with every hit table. Separate raw-token scans from
closure-word scans. Compare apparent groupings against shuffled, same-length,
and same-density controls before calling a pattern meaningful.

## Genetic Decomposition Discipline

Quark work is not only substring counting. Preserve the legacy BigCalc2 idea of
"genetic sequence" as compression and recipe-finding: a target constant may be
represented by a short sequence of quark tokens, official constant tokens,
Z0 facets, literal leftovers, and later XOR-run fragments.

Before implementing this, read `docs/experiments/quark-genetic-sequence.md`.
Keep these views separate in code and reports:

- Direct genetic material view: decompose target bits into named token strings.
- Run-tape view: evolve a seed by circular XOR and scan emitted tape fragments.
- Comparison view: ask whether constants/tokens found in the decomposition also
  appear in the XOR run output.

Every genetic decomposition report must state allowed token catalogs,
orientation/transform rules, whether overlaps/circular wrap were allowed,
literal leftovers, coverage percentage, token count, and controls used.

## Chain-Of-Evidence Rules

- Keep raw/source/generated artifacts separate.
- Do not hand-edit generated CODATA binary or bits-only files. Rebuild them.
- When adding a derived file, state the source file and conversion rule.
- When running scans, report the catalog used: official CODATA only, legacy
  tokens only, or combined.
- Preserve null results and failed controls.
- Prefer explicit baselines over rhetoric.
- Prefer reproducible Markdown/HTML reports generated from code outputs.

## Current Important Files

- `README.md` - project thesis, status, roadmap, and run instructions.
- `src/characteristic_impedance/core.py` - current core bit helpers and Z0 XOR
  loop implementation.
- `docs/codata/README.md` - official CODATA evidence-chain documentation.
- `docs/tokens/legacy-physics-token-catalog.md` - legacy appended-token catalog.
- `docs/experiments/quark-genetic-sequence.md` - next experiment design note for
  quark genetic compression and XOR run comparison.
- `docs/z0-binary-structure.md` - Z0 quark/gluon bit-structure observation.
- `docs/legacy-genetic-sequence-analysis.md` - BigCalc2 gene/run-tape analysis.
- `docs/information-first-position.md` - information-first position statement.
- `tools/codata/build_codata_docs.py` - CODATA artifact builder.
- `tests/` - current regression tests.

## Development Guidance

- Run tests before committing:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m unittest discover -s tests -p "test_*.py"
```

- Keep the Python port clean. Do not mechanically port the WinForms GUI.
- The next major implementation direction is catalog-level experimentation:
  catalog objects, token decomposition, Z0 substrate scans, Z0 run-tape scans,
  randomized controls, and generated reports.
- Use Apache 2.0 headers only if the file style calls for it; do not clutter
  small data artifacts.

## Tone And Scientific Posture

Take the idea seriously without overstating it. The project is allowed to be
weird. The job is to make it precise enough to survive or fail under adversarial
tests.
