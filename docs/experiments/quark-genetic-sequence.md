# Quark Genetic Sequence Experiment

This note defines the next experiment direction before implementation.

The project should not reduce quark work to ordinary substring counting. The
legacy BigCalc2 idea was closer to genetic compression: ask whether a target
constant can be expressed as a short recipe made from quark tokens, constant
tokens, Z0 facets, and later the output of a simple XOR run.

## Core Question

For a target constant, what is its shortest or strongest genetic recipe?

```text
target constant bits
-> decomposed into named bit tokens
-> scored by coverage, literal leftovers, token count, and token meaning
```

Examples of the intended question shape:

```text
Can UP + UP + DOWN seed or explain part of this target?
Can a small quark sequence grow into the rest of this target under XOR evolution?
What other constants appear inside this constant while it is being decomposed genetically?
What is the quark genetic sequence that compresses this constant?
```

These are compression/generation questions, not just hit-count questions.

## Recursive GeneZip Model

The first useful decomposer should support multiple passes, not only a flat
single-pass recipe. A target may contain a named token, and the leftover material
may itself contain another named token after the first token is removed or
marked.

Example shape:

```text
level 0 target:    111011010110111
level 1 recipe:    11(Q_UP)010110111
level 1 remainder: 11010110111
level 2 recipe:    1101(Q_DOWN)11
level 2 remainder: 110111
```

This is GeneZip by copy-paste semantics:

1. Find named token spans inside the current string.
2. Record those spans as genetic material.
3. Remove or mark the matched spans.
4. Concatenate the remaining unmatched material in natural order.
5. Run the next pass on that remainder.
6. Stop at a configured maximum depth, usually 3 or 4 levels, or when no useful
   token is found.

The output is a tree or stack of decompositions, not merely a list of hits. Each
level must preserve:

- input bits for that level
- token spans found
- literal spans remaining
- remainder bits passed to the next level
- token catalog used
- token lengths and high-noise flags
- score for that level
- cumulative score across levels

The method does not have to be exact. Remainders are expected and should be
reported, not hidden. The point is to ask how much named genetic material can be
peeled out of a target over a few disciplined passes.

## Catalog Boundaries

Every run must state which token catalogs were allowed:

- official CODATA constants only
- legacy quark/hadron tokens only
- Z0 closure words only
- combined official CODATA + legacy tokens
- generated XOR-run fragments

Do not silently mix official CODATA rows with legacy exploratory tokens.

## Token Sources

Initial token classes:

1. Raw quark mass-signature tokens from `docs/tokens/legacy-physics-token-catalog.md`.
2. Longer Z0 closure-style quark words from `docs/z0-binary-structure.md`.
3. Official CODATA constant bit strings from `docs/codata/pre-2019-codata-2014-binary.md`.
4. Z0 facets: contiguous substrings of the Z0 ring, when explicitly enabled.
5. XOR-run tokens: fragments emitted by a seed's circular XOR run, when explicitly enabled.

## Decomposition Score

A genetic decomposition should report at least:

- target constant name
- target bits and bit length
- allowed token catalogs
- token sequence
- token names
- token bit strings
- target spans covered
- orientation/transform used, if any
- literal leftover bits
- coverage percentage
- token count
- total token bit length
- whether overlaps were allowed
- whether circular wrap was allowed
- whether the recipe is exact or approximate
- recursion depth and per-level remainders when recursive GeneZip is enabled

A first implementation should prefer exact, non-overlapping decompositions with
explicit literal leftovers. Recursive GeneZip may then peel named material out of
successive remainders for three or four levels. More permissive modes may come
later, but must be reported as such.

## Quark Priority Rule

Short quark tokens are noisy. A decomposition that relies mostly on `Q_UP`
length-5 matches is weak unless controls say otherwise.

First-pass meaningful quark compression should prioritize longer tokens and
closure words:

```text
Q_CHARM             10011111011   length 11
Q_BOTTOM            110100010     length 9
Q_TOP               11011000011   length 11
DOWN closure word   10111101      length 8
STRANGE closure     1100000011    length 10
```

Raw `Q_UP` and raw `Q_DOWN` may be included, but reports must mark them as
high-noise short tokens.

## XOR Run Relationship

There are two distinct but related views:

1. Genetic material view: decompose a target directly using token strings.
2. Run-tape view: evolve a seed by circular XOR and scan the emitted tape for
   target pieces or token pieces.

The experiment should compare them instead of merging them prematurely.

Questions to preserve:

```text
Does a short quark recipe decompose the target directly?
Does the same recipe or seed generate target fragments under XOR evolution?
Do constants found in the decomposition also appear in the XOR run output?
Are decomposed token neighborhoods similar to run-tape token neighborhoods?
```

## Controls

Every positive-looking result needs controls:

- shuffled target bits
- same-length random targets
- same-density random targets
- fake quark tokens with the same lengths
- alternate constants used as seeds
- official-CODATA-only vs legacy-token-enabled runs

A good report must preserve null results and weak decompositions, not only the
pretty recipes.

## Suggested Python Modules

- `src/characteristic_impedance/catalog.py` - load CODATA and legacy token records.
- `src/characteristic_impedance/tokens.py` - token definitions, labels, lengths, and catalogs.
- `src/characteristic_impedance/decompose.py` - exact/approximate token decomposition.
- `src/characteristic_impedance/run_tape.py` - XOR run emission and token scanning.
- `src/characteristic_impedance/reports.py` - Markdown/HTML report generation.

## First Useful Report

```text
docs/reports/quark-genetic-sequence-codata-2014.md
```

Minimum content:

- catalog used
- token catalogs allowed
- decomposition settings
- recursion depth, usually 3 or 4 levels for recursive GeneZip
- top exact decompositions
- top near decompositions
- per-level remainders for recursive decompositions
- constants grouped by quark-heavy recipes
- comparison to shuffled controls
- notes about whether groupings make human physics sense
