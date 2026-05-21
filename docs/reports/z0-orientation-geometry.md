# Z0 Orientation Geometry

This generated report preserves the fixed 39-bit Z0 seed, the four
canonical orientation strings, the known forward manual layout, and
candidate natural traversals over that fixed layout.

It is an evidence-preservation scaffold, not a proof. The other three
proto-geometry structures still need to be restored or confirmed from
legacy source material.

## Source Seed

| field | value |
|---|---|
| constant | characteristic impedance of vacuum |
| significant digits | `376730313461` |
| source bits | `101011110110110111000000110001011110101` |
| bit length | `39` |

## Four Canonical Orientations

| orientation | bits | layout status |
|---|---|---|
| `forward` | `101011110110110111000000110001011110101` | known manual layout preserved from source notes |
| `reverse` | `101011110100011000000111011011011110101` | candidate layout generated from orientation string; legacy visual layout still needs confirmation |
| `inverse` | `010100001001001000111111001110100001010` | candidate layout generated from orientation string; legacy visual layout still needs confirmation |
| `inverse_reverse` | `010100001011100111111000100100100001010` | candidate layout generated from orientation string; legacy visual layout still needs confirmation |

## Known Forward Layout

Source: `docs/z0-binary-structure.md manual forward line-break layout`.

```text
10
10111101
101101
1100000011
000
10111101
01
```

The layout consumes the forward Z0 bits in order:

```text
10 10111101 101101 1100000011 000 10111101 01
```

## Traversals Over The Known Forward Layout

These traversals read the fixed layout in candidate natural orders. They
do not scramble, mutate, or permute the information to force a result;
they state an order for reading the same indexed bits.

| traversal | bits | note |
|---|---|---|
| `row_order` | `101011110110110111000000110001011110101` | confirmed forward line-break layout read top to bottom, left to right |
| `outside_clockwise` | `101110110101110111100110100000010011110` | candidate outside boundary clockwise, followed by remaining interior bits in row order |
| `outside_counterclockwise` | `011110101101110111100110100000010011110` | candidate outside boundary counterclockwise, followed by remaining interior bits in row order |
| `center_out` | `110000001110110100010111101101111011001` | candidate center row outward traversal over the same fixed rows |

## Interpretation Boundaries

- Fixed bits: the 39-bit pre-2019 Z0 significant-digit binary seed.
- Orientation: forward, reverse, inverse, and inverse-reverse bit views.
- Layout: the confirmed manual forward line-break structure from the
  source notes; other orientation layouts are candidates pending legacy
  confirmation.
- Traversal: row, outside-boundary, and center-out reading orders over
  the known forward layout.
- Interpretation: this prepares later quark genetic sequence work, but
  does not implement decomposition or claim proof.
