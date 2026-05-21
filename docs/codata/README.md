# CODATA Evidence Chain

This folder preserves the pre-2019 CODATA working source and the derived binary
forms used by the project.

The canonical corpus currently contains 336 official CODATA 2014 rows parsed
from the legacy NIST all-values text file. Project-specific BigCalc2 rows that
were appended after the official table, such as `Q_UP` and `Q_DOWN`, are not
part of this CODATA corpus; those belong in a separate physics-token catalog.

## Files

- `pre-2019-codata-2014-raw.txt` - raw NIST-style all-values text used as the import source.
- `pre-2019-codata-2014-source.md` - named/value/unit source table.
- `pre-2019-codata-2014-binary.md` - same row order, with significant digits and binary form.
- `pre-2019-codata-2014-bits-only.txt` - one line of bits per source row, no names, no units, no comments.

## Conversion Rule

The project's binary conversion uses the published value mantissa only.

```text
376.730 313 461... -> 376730313461 -> binary
6.626 070 040 e-34 -> 6626070040   -> binary
299 792 458        -> 299792458    -> binary
```

Ignored during conversion:

- sign
- decimal point
- digit-grouping spaces
- ellipsis
- uncertainty
- unit
- exponent marker such as `e-34`

That is deliberate. The point is to test the significant-digit information
object, not the engineering scale factor.

## Rebuild

From the repo root, rebuild generated files from the Markdown source table:

```bash
python tools/codata/build_codata_docs.py
```

To rebuild the full canonical source table and generated artifacts from the
checked-in raw text:

```bash
python tools/codata/build_codata_docs.py --nist-ascii docs/codata/pre-2019-codata-2014-raw.txt --out-dir docs/codata
```

Optional official-source fetch step:

```bash
python tools/codata/fetch_nist_2014_ascii.py
```

The fetch step downloads the official NIST 2014 all-values ASCII file into
`data/codata/raw/`. Review that file before replacing
`docs/codata/pre-2019-codata-2014-raw.txt` and rebuilding generated binary
files.
