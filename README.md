# Characteristic Impedance Python

Python-first research instrument for testing whether the characteristic impedance
of vacuum behaves like an unusually generative information substrate inside the
published catalog of fundamental physical constants.

## Thesis

The claim is not that the unit "ohm" is physically privileged, or that the
decimal value `376.730313461` is magic.

The claim is that mature physics compresses empirical reality into a finite
symbolic catalog of authoritative constants. Once a constant is published, its
significant digits can be treated as an information object. Under a minimal
binary encoding and a minimal XOR-only ring evolution, the characteristic
impedance of vacuum appears to behave like a privileged seed whose orbit
contains or reconstructs a surprisingly large fraction of the other CODATA
constant bit patterns.

That claim is testable. This repository is the sober instrument for testing it.

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

## Starting Point

The legacy observation uses pre-2019 CODATA:

```text
name:   characteristic impedance of vacuum
digits: 376730313461
bits:   101011110110110111000000110001011110101
len:    39
```

The legacy C# project recorded a forward exact loop for this seed with period
`4095`. The Python implementation should reproduce, isolate, and harden that
result before expanding the test space.

## Initial Notes

- [Z0 Binary Structure](docs/z0-binary-structure.html) captures the 2019 PDF/RTF
  observation that the characteristic impedance bits already contain whole
  quark mass-signature words, arrange naturally into a gluon-like chart, and
  come from a prime significant-digit integer with a primitive Pythagorean
  triple identity.

## Design Posture

- Treat constants as information artifacts with provenance.
- Treat units as translations to be tested, not as automatic disqualifiers.
- Prefer small, inspectable algorithms over GUI-first exploration.
- Require randomized and cross-constant baselines before making strong claims.
- Keep generated reports separate from core library code.

## Legacy Reference

The original exploratory C# / WinForms lab bench is preserved separately:

```text
E:\physics\CharacteristicImpedanceLegacy
```

Do not mechanically port the GUI. Extract the experiment and rebuild it as a
testable Python research tool.
