# Characteristic Impedance Python

Python-first research instrument for testing whether the characteristic impedance
of vacuum behaves like an unusually generative information substrate inside the
published catalog of fundamental physical constants.

## Status

This is an early research instrument, not a completed proof. The project begins
with one strong legacy observation and turns it into code, tests, baselines, and
failure conditions.

Current project state:

- The pre-2019 `Z0` circular-XOR loop result is reproduced in tested Python code.
- The information-first thesis and legacy BigCalc2 observations are captured in
  GitHub-readable Markdown notes, with companion HTML versions for local/static
  viewing.
- A pre-2019 CODATA 2014 evidence chain exists under `docs/codata/`, including
  source rows, derived binary rows, and a bits-only corpus.
- CODATA documentation generation tools exist under `tools/codata/`.
- Unit tests cover the Z0 anchor, core bit operations, XOR loop behavior, and
  CODATA document generation.
- GitHub Actions runs the Python unit test suite on push and pull request.

The next major implementation step is catalog-level experimentation: scanning
all constants, building randomized controls, and producing reproducible reports
from code outputs rather than hand-written observations.

## Claim Under Test

This project tests the claim that the pre-2019 CODATA significant-digit
representation of the characteristic impedance of vacuum is not merely an
arbitrary decimal artifact. Under a minimal binary encoding and a minimal
circular XOR evolution, it appears to behave as an unusually generative seed
inside the catalog of physical constants.

The claim is not that the ohm is sacred. The claim is that the pre-2019
published `Z0` value may preserve a privileged information object whose
structure became harder to see after the 2019 SI redefinition changed the
exact/measured status of vacuum electromagnetic constants.

## Thesis

Mature physics compresses empirical reality into a finite symbolic catalog of
authoritative constants. Once a constant is published, its significant digits can
be treated as an information object.

The working hypothesis is that the characteristic impedance of vacuum is not
just another constant in that catalog. It may be the impedance boundary between
physical measurement and symbolic compression: a compact seed whose simple
binary evolution reconstructs or intersects an unusually large fraction of the
other published constant bit patterns.

That claim is testable.

## Core Experiment

1. Load pre-2019 CODATA constants as published significant-digit records.
2. Convert each constant's significant digits into a binary information object.
3. Generate four canonical orientations: forward, reverse, inverse, and inverse-reverse.
4. Evolve each seed as a circular XOR ring:

   ```text
   next[i] = current[i] XOR current[(i + 1) mod n]
   ```

5. Detect halt, loop, period, and generated orbit text.
6. Scan each orbit for other constant bit patterns.
7. Compare the characteristic impedance of vacuum (`Z0`) against all other constants and randomized controls.
8. Repeat under precision choices, unit translations, CODATA editions, and alternative encodings.

## Known Verified Result

The legacy observation uses pre-2019 CODATA:

```text
name:   characteristic impedance of vacuum
digits: 376730313461
bits:   101011110110110111000000110001011110101
len:    39
```

The current Python implementation verifies that the forward circular-XOR
evolution of this seed closes a loop at period `4095`:

```text
seed        = 101011110110110111000000110001011110101
period      = 4095
halted      = false
closed_loop = true
```

This is the first anchor result. The project should not make stronger claims
until the catalog-level and randomized-control tests are implemented.

## Evidence Chain

The project now keeps the pre-2019 source and derived binary evidence in-tree:

- [CODATA Evidence Chain](docs/codata/README.md) explains the conversion rule
  and rebuild process.
- [Pre-2019 CODATA 2014 Source](docs/codata/pre-2019-codata-2014-source.md)
  preserves the named/value/unit rows currently used by the project.
- [Pre-2019 CODATA 2014 Binary](docs/codata/pre-2019-codata-2014-binary.md)
  preserves the same rows with significant digits and binary forms.
- [Pre-2019 CODATA 2014 Bits Only](docs/codata/pre-2019-codata-2014-bits-only.txt)
  is the stripped corpus for pure bit experiments.

The conversion rule intentionally uses the published value mantissa only:

```text
376.730 313 461... -> 376730313461 -> binary
6.626 070 040 e-34 -> 6626070040   -> binary
299 792 458        -> 299792458    -> binary
```

That rule ignores sign, decimal point, digit-grouping spaces, ellipsis,
uncertainty, unit, and exponent marker. This is not an accident; it is the
information-object hypothesis made explicit and testable.

## Falsification Criteria

This claim weakens or fails if:

- `Z0` does not outperform other constants under the same encoding and evolution.
- Randomized bitstrings with the same length and density perform comparably.
- Shuffled catalog controls perform comparably.
- The observed structure disappears under reasonable precision and unit transformation tests.
- Post-selection explains the apparent matches.
- The result depends on undocumented choices that cannot be preregistered and repeated.

## Why Pre-2019 Z0 Matters

The 2019 SI revision is not treated here as a mere bookkeeping change. It is
treated as a change in the published information structure of the constants
catalog.

Before the revised SI, the vacuum electromagnetic constants occupied a different
definitional status. After the revision, the SI is defined through exact values
assigned to selected defining constants, including `c`, `h`, and `e`. Under that
regime, the vacuum magnetic permeability and the impedance of free space are no
longer fixed in the same way; they become tied to the measured fine-structure
constant.

This project therefore treats the pre-2019 `Z0` value as a historically specific
information object. The question is not whether a unit convention is sacred. The
question is whether the pre-2019 catalog preserved a compact symbolic seed that
is structurally special under simple computational tests.

## Methodological Context

The computational stance is close to the Wolfram-style lesson that very simple
programs can produce unexpectedly rich behavior. The rule used here is much
smaller than a physics model:

```text
circular binary seed -> XOR with one-bit rotation -> generated orbit
```

If that minimal rule produces non-random reconstruction behavior against a
catalog of physical constants, the next move is not rhetoric. The next move is
controls.

## Install And Run

From the repository root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -e .
python -m unittest
```

Windows cmd:

```bat
.venv\Scripts\activate.bat
pip install -e .
python -m unittest
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -e .
python -m unittest
```

## Initial Notes

- [Information-First Position](docs/information-first-position.md) states the
  central thesis: physical constants are compressed information artifacts before
  they are physics classroom objects, and unit objections must be tested as
  encoding transformations rather than used as a dismissal.
- [Legacy Genetic Sequence Analysis](docs/legacy-genetic-sequence-analysis.md)
  explains what the old BigCalc2 "gene" machinery was doing: circular tape
  decomposition, Z0-facet compression, ablation controls, and Z0-as-running-tape
  scans.
- [Z0 Binary Structure](docs/z0-binary-structure.md) captures the 2019 PDF/RTF
  observation that the characteristic impedance bits already contain whole
  quark mass-signature words, arrange naturally into a gluon-like chart, and
  come from a prime significant-digit integer with a primitive Pythagorean
  triple identity.

Note: the Markdown documents linked above are the GitHub-readable versions.
The companion HTML files in `docs/` are much nicer looking when opened locally
or through a static site, but GitHub's repository file browser shows them as
source code unless GitHub Pages or another static host is used.

## Design Posture

- Treat constants as information artifacts with provenance.
- Treat units as translations to be tested, not as automatic disqualifiers.
- Prefer small, inspectable algorithms over GUI-first exploration.
- Require randomized and cross-constant baselines before making strong claims.
- Keep generated reports separate from core library code.

## Roadmap

### Done

- Reproduce the legacy `Z0` XOR-ring period result.
- Add core bit helpers: significant digits to bits, reverse, invert, canonical
  orientations, XOR ring step, and XOR ring run.
- Add Apache 2.0 licensing, notice, package metadata, and GitHub Actions tests.
- Capture the information-first thesis in project docs.
- Capture the Z0 quark/gluon binary-structure observation in project docs.
- Analyze and document the legacy BigCalc2 genetic-sequence machinery.
- Add a pre-2019 CODATA 2014 evidence chain with generated binary and bits-only
  files.
- Add tests for the CODATA conversion and document rebuild path.

### Next

- Move CODATA records from documentation artifacts into importable Python catalog
  objects.
- Add catalog-wide orientation, period, orbit, and run-tape scans.
- Port the legacy token/gene decomposer as clean Python modules:
  `tokens`, `decompose`, `z0_substrate`, and `run_tape`.
- Add shuffled-bit, random-seed, and alternate-constant baselines.
- Generate reproducible Markdown/HTML reports directly from Python outputs.

### Later

- Add unit-translation and precision-cut experiments.
- Compare pre-2019 CODATA against post-2019 and alternate CODATA editions.
- Add stability-basin scans for uncertain quark mass signatures.
- Publish null results and failed variants alongside positive results.

## References

- BIPM, [The International System of Units (SI)](https://www.bipm.org/en/measurement-units).
- NIST, [SI Redefinition](https://www.nist.gov/si-redefinition).
- Pierre Fayet, [Completing the International System of units with c = hbar = mu0 = epsilon0 = kB = NA = 1](https://arxiv.org/abs/1906.05123), arXiv:1906.05123.
- Wolfram, [Wolfram Science](https://www.wolfram.com/wolfram-science/).
