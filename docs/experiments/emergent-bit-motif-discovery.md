# Emergent Bit Motif Discovery

This is a later experiment direction, separate from named-quark GeneZip.

GeneZip starts with known named tokens such as quarks, closure words, CODATA
constants, and legacy physics tokens. Emergent motif discovery starts with no
name at all. It asks which long bit strings recur across multiple constants
strongly enough that they deserve to become candidate proto-tokens.

## Core Question

What are the largest or strongest recurring bit patterns that appear across the
CODATA corpus, regardless of whether they are already known constants, quarks,
or named legacy tokens?

```text
official CODATA bits
-> find recurring substrings
-> rank by length, frequency, coverage, and family concentration
-> inspect the constants occupied by each motif
-> propose cautious names only after the occupation pattern is visible
```

Example interpretation shape:

```text
motif: 101101110001...
occupation: appears across constants related to optical frequency/wavelength
candidate name: optical-transfer motif
status: hypothesis, not proof
```

The naming step comes last. Do not name motifs first and then search for them.

## Difference From Quark GeneZip

Quark GeneZip uses named material:

- raw quark tokens
- Z0 closure quark words
- official CODATA constant tokens
- legacy BigCalc2 tokens

Emergent motif discovery uses unnamed material:

- maximal common substrings
- repeated substrings above a minimum length
- motifs enriched in physical families
- motifs that survive shuffled/random controls

These motifs may later become named tokens, but only after the evidence says
where they live.

## Candidate Terms

Use neutral language until the evidence is strong:

- motif
- proto-token
- recurrent bit motif
- common substrate fragment
- unnamed genetic material

Avoid strong physical names such as "quark-like substance" in generated reports
unless the report also explains the evidence, the occupied constants, and the
controls. A better early phrase is:

```text
candidate quark-like motif occupying constants involving optical physics
```

## Search Rules

A first implementation should prefer:

- official CODATA-only input first
- minimum motif length high enough to avoid noise, probably 8 or more bits
- exact substring matching before fuzzy matching
- row/order provenance for every occurrence
- no hand-picked target families during initial discovery

Report every motif with:

- motif bits
- bit length
- occurrence count
- list of constants containing it
- positions in each constant
- orientations allowed
- source catalog used
- physical-family tags assigned after discovery
- shuffled/random baseline comparison

## Family Interpretation

After motifs are found, inspect what kinds of constants they occupy:

- electromagnetic
- optical / wavelength / frequency
- mass / energy equivalent
- atomic unit
- magnetic moment
- thermodynamic
- Planck-scale
- conversion relationship
- quantum electrical / Josephson / von Klitzing / conductance

The family labels are interpretive metadata, not part of the motif search
itself. Keep discovery and interpretation separate.

## Controls

A motif is not interesting merely because it appears more than once. It becomes
interesting only if it survives controls such as:

- shuffled bits within each constant
- same-length random bitstrings
- same-density random bitstrings
- random substrings of the same length distribution
- comparison to motifs found in alternate constants used as seeds

Short motifs will be common by chance. Long motifs with coherent physical-family
occupation are more interesting.

## Suggested Future Modules

- `src/characteristic_impedance/motifs.py` - substring discovery and motif records.
- `src/characteristic_impedance/families.py` - post-discovery physical-family tags.
- `tools/reports/build_motif_report.py` - generated motif discovery report.

## First Useful Report

```text
docs/reports/emergent-bit-motifs-codata-2014.md
```

Minimum content:

- catalog used
- minimum motif length
- orientation modes enabled
- top motifs by length and occurrence count
- top motifs by family concentration
- motif occurrence tables
- null/shuffled controls
- cautious candidate names, only after occupation evidence is shown
