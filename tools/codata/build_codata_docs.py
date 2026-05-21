"""Build CODATA evidence-chain Markdown and bits-only files.

The source of truth is a Markdown table with these columns:
index, quantity, value, uncertainty, unit.

Conversion rule used by this project:
- Use the published value mantissa only.
- Ignore sign, spaces, decimal point, grouping, ellipsis, uncertainty, unit,
  and exponent marker such as e-34.
- Convert the remaining significant digits to an integer and then to base 2.

Example: "376.730 313 461..." -> "376730313461" -> binary.
Example: "6.626 070 040 e-34" -> "6626070040" -> binary.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class CodataRecord:
    index: int
    quantity: str
    value: str
    uncertainty: str
    unit: str

    @property
    def significant_digits(self) -> str:
        return value_mantissa_digits(self.value)

    @property
    def bits(self) -> str:
        return digits_to_bits(self.significant_digits)


def split_markdown_row(line: str) -> list[str] | None:
    if not line.lstrip().startswith("|"):
        return None
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def read_source_table(path: Path) -> list[CodataRecord]:
    header: list[str] | None = None
    records: list[CodataRecord] = []

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        cells = split_markdown_row(line)
        if not cells or is_separator_row(cells):
            continue

        lowered = [cell.lower() for cell in cells]
        if lowered[:5] == ["index", "quantity", "value", "uncertainty", "unit"]:
            header = lowered
            continue

        if header is None:
            continue

        if len(cells) < 5:
            raise ValueError(f"Malformed source row at {path}:{line_number}: {line}")

        row = dict(zip(header, cells))
        records.append(
            CodataRecord(
                index=int(row["index"]),
                quantity=row["quantity"],
                value=row["value"],
                uncertainty=row["uncertainty"],
                unit=row["unit"],
            )
        )

    if not records:
        raise ValueError(f"No CODATA records found in {path}")

    expected = list(range(1, len(records) + 1))
    actual = [record.index for record in records]
    if actual != expected:
        raise ValueError(f"Source indexes must be contiguous and ordered: expected {expected}, got {actual}")

    return records


def parse_nist_ascii(path: Path) -> list[CodataRecord]:
    """Parse a NIST all-values ASCII listing into canonical CODATA records.

    The legacy BigCalc2 source file includes a few project-specific rows after
    the official CODATA table. This parser stops before those local additions.
    """
    records: list[CodataRecord] = []
    stop_names = {"FIXED_PlanckTime", "Q_CesiumSecond"}

    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        raw = line.strip()
        if not raw:
            continue
        if raw.startswith(("Fundamental", "From:", "Quantity", "---")):
            continue

        parts = re.split(r"\s{2,}", raw)
        if len(parts) < 3:
            continue

        quantity = parts[0].replace("_", "-")
        if quantity in stop_names or quantity.startswith("Q_"):
            break

        value = parts[1]
        uncertainty = parts[2]
        unit = parts[3] if len(parts) > 3 else ""

        # Guard against non-data prose accidentally parsed as rows.
        value_mantissa_digits(value)

        records.append(
            CodataRecord(
                index=len(records) + 1,
                quantity=quantity,
                value=value,
                uncertainty=uncertainty,
                unit=unit,
            )
        )

    if not records:
        raise ValueError(f"No CODATA rows parsed from {path}")

    return records


def value_mantissa_digits(value: str) -> str:
    normalized = value.replace("−", "-").replace("×", "x")
    normalized = re.sub(r"\([^)]*\)", "", normalized).strip()

    mantissa_tokens: list[str] = []
    for token in normalized.split():
        if re.fullmatch(r"[eE][+-]?\d+", token):
            break
        mantissa_tokens.append(token)

    mantissa = "".join(mantissa_tokens)
    digits = re.sub(r"\D", "", mantissa)
    if not digits:
        raise ValueError(f"value contains no significant digits: {value!r}")
    return digits


def digits_to_bits(digits: str) -> str:
    if not digits or not digits.isdigit():
        raise ValueError(f"digits must be decimal digits only: {digits!r}")
    return bin(int(digits))[2:]


def write_binary_markdown(records: list[CodataRecord], path: Path, source_name: str, bits_only_name: str) -> None:
    lines = [
        "# Pre-2019 CODATA 2014 Binary Form",
        "",
        f"Generated from `{source_name}` by `tools/codata/build_codata_docs.py`.",
        "",
        f"Evidence-chain rule: row order must match the source table and `{bits_only_name}` exactly.",
        "",
        "| index | quantity | value | significant digits | bits | unit |",
        "|---:|---|---:|---:|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record.index} | {record.quantity} | {record.value} | "
            f"{record.significant_digits} | `{record.bits}` | {record.unit} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_bits_only(records: list[CodataRecord], path: Path) -> None:
    path.write_text("\n".join(record.bits for record in records) + "\n", encoding="utf-8")


def write_source_markdown(records: list[CodataRecord], path: Path, raw_source_name: str | None = None) -> None:
    source_line = (
        f"Generated from `{raw_source_name}` by `tools/codata/build_codata_docs.py --nist-ascii`."
        if raw_source_name
        else "Versioned local source table used by the repository pipeline."
    )
    lines = [
        "# Pre-2019 CODATA 2014 Source Copy",
        "",
        source_line,
        "",
        "Source: NIST CODATA 2014 Fundamental Physical Constants, Complete Listing.",
        "Canonical URL: https://physics.nist.gov/cuu/Constants/ArchiveASCII/allascii_2014.txt",
        "",
        "Evidence-chain rule: this file is the named/value/unit source. The generated binary files must be rebuilt from this table by `tools/codata/build_codata_docs.py`, not hand-edited.",
        "",
        "| index | quantity | value | uncertainty | unit |",
        "|---:|---|---:|---:|---|",
    ]
    for record in records:
        lines.append(
            f"| {record.index} | {record.quantity} | {record.value} | "
            f"{record.uncertainty} | {record.unit} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build(source: Path, out_dir: Path) -> None:
    records = read_source_table(source)
    out_dir.mkdir(parents=True, exist_ok=True)
    binary_name = "pre-2019-codata-2014-binary.md"
    bits_name = "pre-2019-codata-2014-bits-only.txt"
    write_binary_markdown(records, out_dir / binary_name, source.name, bits_name)
    write_bits_only(records, out_dir / bits_name)


def build_from_nist_ascii(nist_ascii: Path, out_dir: Path) -> None:
    records = parse_nist_ascii(nist_ascii)
    out_dir.mkdir(parents=True, exist_ok=True)
    source_name = "pre-2019-codata-2014-source.md"
    binary_name = "pre-2019-codata-2014-binary.md"
    bits_name = "pre-2019-codata-2014-bits-only.txt"
    write_source_markdown(records, out_dir / source_name, nist_ascii.name)
    write_binary_markdown(records, out_dir / binary_name, source_name, bits_name)
    write_bits_only(records, out_dir / bits_name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/codata/pre-2019-codata-2014-source.md"),
        help="Markdown source table to convert.",
    )
    parser.add_argument(
        "--nist-ascii",
        type=Path,
        help="Optional NIST all-values ASCII file. When provided, rebuilds the source table and generated artifacts from this raw file.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("docs/codata"),
        help="Directory for generated binary files.",
    )
    args = parser.parse_args()
    if args.nist_ascii:
        build_from_nist_ascii(args.nist_ascii, args.out_dir)
    else:
        build(args.source, args.out_dir)


if __name__ == "__main__":
    main()
