# Z0 QLF / ZFA Admissibility Probe

This is not a proof. It does not validate a physics claim or establish
Jim Scarver's framework experimentally.

This layer separates generated bits from candidate QLF/ZFA admissibility:
the XOR orbit is the generated substrate, tap-tape windows are generated
observation streams, named bit tokens are observed words, and QLF/ZFA
candidate objects are interpreted process/capability/proof-like
structures.

A candidate is admissible only when positive/action and negative/lift
twists balance to spectral gap zero. Unbalanced candidates are not bad
strings; they are non-admissible under this interpretation.

## Probe Settings

- Seed bits: `101011110110110111000000110001011110101`
- Period: `4095`
- Tap index: `0`
- Candidate windows: `32`
- Admissible windows: `9`

## Candidate Windows

| Candidate | Bits | Twists | Positive | Negative | Spectral gap | Admissible |
|---|---|---|---:|---:|---:|---|
| z0_tap0_window_0000 | `100010010101` | `^<\-^<\+v>\+` | 5 | 7 | -2 | no |
| z0_tap0_window_0001 | `001011011101` | `v</-^>\+^>\+` | 7 | 5 | 2 | no |
| z0_tap0_window_0002 | `010110101010` | `v>\+^</-^</-` | 6 | 6 | 0 | yes |
| z0_tap0_window_0003 | `000011100000` | `v<\-^>/-v<\-` | 3 | 9 | -6 | no |
| z0_tap0_window_0004 | `100110000111` | `^<\+^<\-v>/+` | 6 | 6 | 0 | yes |
| z0_tap0_window_0005 | `100001101101` | `^<\-v>/-^>\+` | 6 | 6 | 0 | yes |
| z0_tap0_window_0006 | `110011001001` | `^>\-^>\-^<\+` | 6 | 6 | 0 | yes |
| z0_tap0_window_0007 | `010111011101` | `v>\+^>\+^>\+` | 8 | 4 | 4 | no |
| z0_tap0_window_0008 | `010000000101` | `v>\-v<\-v>\+` | 3 | 9 | -6 | no |
| z0_tap0_window_0009 | `011101011011` | `v>/+v>\+^</+` | 8 | 4 | 4 | no |
| z0_tap0_window_0010 | `101011010101` | `^</-^>\+v>\+` | 7 | 5 | 2 | no |
| z0_tap0_window_0011 | `011110000000` | `v>/+^<\-v<\-` | 4 | 8 | -4 | no |
| z0_tap0_window_0012 | `011101010110` | `v>/+v>\+v>/-` | 7 | 5 | 2 | no |
| z0_tap0_window_0013 | `111101100010` | `^>/+v>/-v</-` | 7 | 5 | 2 | no |
| z0_tap0_window_0014 | `010011010011` | `v>\-^>\+v</+` | 6 | 6 | 0 | yes |
| z0_tap0_window_0015 | `100010111101` | `^<\-^</+^>\+` | 7 | 5 | 2 | no |
| z0_tap0_window_0016 | `000000011000` | `v<\-v<\+^<\-` | 2 | 10 | -8 | no |
| z0_tap0_window_0017 | `100000101010` | `^<\-v</-^</-` | 4 | 8 | -4 | no |
| z0_tap0_window_0018 | `111001101001` | `^>/-v>/-^<\+` | 7 | 5 | 2 | no |
| z0_tap0_window_0019 | `110100010110` | `^>\+v<\+v>/-` | 6 | 6 | 0 | yes |
| z0_tap0_window_0020 | `001011001001` | `v</-^>\-^<\+` | 5 | 7 | -2 | no |
| z0_tap0_window_0021 | `111111001111` | `^>/+^>\-^>/+` | 10 | 2 | 8 | no |
| z0_tap0_window_0022 | `111000111110` | `^>/-v</+^>/-` | 8 | 4 | 4 | no |
| z0_tap0_window_0023 | `001100100101` | `v</+v</-v>\+` | 5 | 7 | -2 | no |
| z0_tap0_window_0024 | `110101011010` | `^>\+v>\+^</-` | 7 | 5 | 2 | no |
| z0_tap0_window_0025 | `100110001101` | `^<\+^<\-^>\+` | 6 | 6 | 0 | yes |
| z0_tap0_window_0026 | `011011101111` | `v>/-^>/-^>/+` | 9 | 3 | 6 | no |
| z0_tap0_window_0027 | `000011110010` | `v<\-^>/+v</-` | 5 | 7 | -2 | no |
| z0_tap0_window_0028 | `001011000101` | `v</-^>\-v>\+` | 5 | 7 | -2 | no |
| z0_tap0_window_0029 | `100001110101` | `^<\-v>/+v>\+` | 6 | 6 | 0 | yes |
| z0_tap0_window_0030 | `011001101010` | `v>/-v>/-^</-` | 6 | 6 | 0 | yes |
| z0_tap0_window_0031 | `111010101110` | `^>/-^</-^>/-` | 8 | 4 | 4 | no |

## Next Scientific Step

The serious next step is comparing admissible candidate rates and
compression/reconstruction performance against alternate constants,
same-density randomized controls, shuffled seeds, and fake token
catalogs. This report only adds the admissibility scaffold.
