# Fundamental Pi: Elastic Hashing, Firebreaks, and Sparse Closure

Status: explicit companion note to `fundamentalPi.md` and `z0-sparse-pi-machine.md`.

This note exists because the hash-table / elastic-hashing issue must be named directly, not left as a vague metaphor.

## 1. The computer-science anchor

The elastic-hashing lesson is:

```text
greedy placement can create global congestion
non-greedy spacing can preserve future reachability
empty slots can be functional firebreaks
```

A hash table that grabs every locally available slot can form clusters and degrade lookup. A sparse/firebreak strategy intentionally avoids some locally available placements so the structure remains searchable near saturation.

The crucial correction is:

```text
local availability != global admissibility
```

## 2. Why this belongs in Fundamental Pi

`fundamentalPi.md` is asking how pi can be produced by closure-return statistics rather than inserted as a primitive geometric constant.

That means the important object is not merely the occupied path, occupied slot, or successful return. The full machine includes:

```text
successful returns
failed returns
skipped windows
unused taps
null receipts
spacing / firebreak structure
```

The elastic-hashing analogy says this explicitly:

```text
The gaps are not automatically waste.
The gaps may preserve reachability.
The non-events may be part of the closure layout.
```

## 3. Z0 sparse-pi reading

For Z0_AsBinary:

```text
Z0 seed
-> circular XOR orbit
-> sparse tap tapes
-> bit-pair relation channels
-> return-window census
-> running pi estimator
```

A greedy reading tries to assign immediate payload meaning to every bit, tap, and local window.

A sparse closure reading asks a better question:

```text
Which selected windows return?
Which windows fail?
How are the failures distributed?
Do the gaps/firebreaks preserve a non-random closure geometry?
Does Z0 separate from shuffled/random/CODATA controls?
```

## 4. Doctrine line

```text
Elastic hashing proves the general process lesson: a locally open slot is not automatically an admissible slot. Z0 should be read the same way. A locally available bit/window/tap is not automatically meaningful payload; gaps, failed returns, and skipped windows may be firebreak-like structure that preserves the closure census.
```

## 5. Brutal version

```text
Do not greedily interpret every bit.
Do not throw away every gap.
The firebreak may be the machine.
```

## 6. Required test addition

Any future Z0/pi return-sampler test should measure not only pi-like convergence, but also the firebreak structure:

```text
successful return density
failed-return distribution
run lengths between returns
gap spacing
orientation dependence
comparison against shuffled Z0
comparison against random same-density seeds
comparison against other CODATA constants
```

The question is not merely:

```text
Can pi-like estimates be produced?
```

Many unbiased samplers can do that.

The sharper question is:

```text
Does Z0 have an unusual sparse/firebreak closure layout?
```
