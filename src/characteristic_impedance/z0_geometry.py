"""Z0 proto-geometry evidence preservation.

This module preserves the known forward Z0 layout and makes candidate natural
traversals explicit. It does not claim that the candidate traversals prove a
physics model; they are reproducible views of fixed information.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import Z0_PRE_2019_BITS, orientations

Z0_SEED_BITS = Z0_PRE_2019_BITS
Z0_ORIENTATIONS = orientations(Z0_SEED_BITS)

KNOWN_FORWARD_LAYOUT = (
    "10",
    "10111101",
    "101101",
    "1100000011",
    "000",
    "10111101",
    "01",
)

KNOWN_FORWARD_LAYOUT_PROVENANCE = (
    "docs/z0-binary-structure.md manual forward line-break layout"
)

ORIENTATION_LAYOUT_STATUS = {
    "forward": "known manual layout preserved from source notes",
    "reverse": "candidate layout generated from orientation string; legacy visual layout still needs confirmation",
    "inverse": "candidate layout generated from orientation string; legacy visual layout still needs confirmation",
    "inverse_reverse": "candidate layout generated from orientation string; legacy visual layout still needs confirmation",
}


@dataclass(frozen=True)
class TraversalPath:
    """Named traversal over the fixed forward Z0 layout."""

    name: str
    bit_indices: tuple[int, ...]
    description: str
    consumes_all_bits: bool = True

    def bits(self, source_bits: str = Z0_SEED_BITS) -> str:
        """Return the traversal string from source bits."""
        _validate_indices(self.bit_indices, len(source_bits))
        return "".join(source_bits[index] for index in self.bit_indices)


def forward_layout_bits() -> str:
    """Return the confirmed forward layout as one bit string."""
    return "".join(KNOWN_FORWARD_LAYOUT)


def candidate_layout_for_orientation(name: str) -> tuple[str, ...]:
    """Return the known or candidate segmented layout for an orientation."""
    if name not in Z0_ORIENTATIONS:
        raise KeyError(f"unknown orientation: {name}")
    if name == "forward":
        return KNOWN_FORWARD_LAYOUT
    return _apply_segment_lengths(Z0_ORIENTATIONS[name], _segment_lengths(KNOWN_FORWARD_LAYOUT))


def traversal_string(name: str) -> str:
    """Return one named traversal string over the fixed forward layout."""
    try:
        path = TRAVERSAL_PATHS[name]
    except KeyError as exc:
        raise KeyError(f"unknown traversal path: {name}") from exc
    return path.bits()


def render_markdown_report() -> str:
    """Render the Z0 orientation/proto-geometry evidence report."""
    lines = [
        "# Z0 Orientation Geometry",
        "",
        "This generated report preserves the fixed 39-bit Z0 seed, the four",
        "canonical orientation strings, the known forward manual layout, and",
        "candidate natural traversals over that fixed layout.",
        "",
        "It is an evidence-preservation scaffold, not a proof. The other three",
        "proto-geometry structures still need to be restored or confirmed from",
        "legacy source material.",
        "",
        "## Source Seed",
        "",
        "| field | value |",
        "|---|---|",
        "| constant | characteristic impedance of vacuum |",
        "| significant digits | `376730313461` |",
        f"| source bits | `{Z0_SEED_BITS}` |",
        f"| bit length | `{len(Z0_SEED_BITS)}` |",
        "",
        "## Four Canonical Orientations",
        "",
        "| orientation | bits | layout status |",
        "|---|---|---|",
    ]
    for name, bits in Z0_ORIENTATIONS.items():
        lines.append(f"| `{name}` | `{bits}` | {ORIENTATION_LAYOUT_STATUS[name]} |")

    lines.extend(
        [
            "",
            "## Known Forward Layout",
            "",
            f"Source: `{KNOWN_FORWARD_LAYOUT_PROVENANCE}`.",
            "",
            "```text",
            *KNOWN_FORWARD_LAYOUT,
            "```",
            "",
            "The layout consumes the forward Z0 bits in order:",
            "",
            f"```text\n{' '.join(KNOWN_FORWARD_LAYOUT)}\n```",
            "",
            "## Traversals Over The Known Forward Layout",
            "",
            "These traversals read the fixed layout in candidate natural orders. They",
            "do not scramble, mutate, or permute the information to force a result;",
            "they state an order for reading the same indexed bits.",
            "",
            "| traversal | bits | note |",
            "|---|---|---|",
        ]
    )
    for path in TRAVERSAL_PATHS.values():
        lines.append(f"| `{path.name}` | `{path.bits()}` | {path.description} |")

    lines.extend(
        [
            "",
            "## Interpretation Boundaries",
            "",
            "- Fixed bits: the 39-bit pre-2019 Z0 significant-digit binary seed.",
            "- Orientation: forward, reverse, inverse, and inverse-reverse bit views.",
            "- Layout: the confirmed manual forward line-break structure from the",
            "  source notes; other orientation layouts are candidates pending legacy",
            "  confirmation.",
            "- Traversal: row, outside-boundary, and center-out reading orders over",
            "  the known forward layout.",
            "- Interpretation: this prepares later quark genetic sequence work, but",
            "  does not implement decomposition or claim proof.",
            "",
        ]
    )
    return "\n".join(lines)


def _segment_lengths(layout: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(len(row) for row in layout)


def _apply_segment_lengths(bits: str, lengths: tuple[int, ...]) -> tuple[str, ...]:
    rows: list[str] = []
    cursor = 0
    for length in lengths:
        rows.append(bits[cursor : cursor + length])
        cursor += length
    if cursor != len(bits):
        raise ValueError("segment lengths must consume all bits")
    return tuple(rows)


def _layout_index_rows(layout: tuple[str, ...]) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    cursor = 0
    for row in layout:
        indices = tuple(range(cursor, cursor + len(row)))
        rows.append(indices)
        cursor += len(row)
    return tuple(rows)


def _boundary_clockwise_indices(index_rows: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    top = index_rows[0]
    middle = index_rows[1:-1]
    bottom = index_rows[-1]

    right_edges = tuple(row[-1] for row in middle)
    bottom_reversed = tuple(reversed(bottom))
    left_edges = tuple(row[0] for row in reversed(middle))
    boundary = top + right_edges + bottom_reversed + left_edges

    boundary_set = set(boundary)
    centers = tuple(
        index
        for row in index_rows[1:-1]
        for index in row[1:-1]
        if index not in boundary_set
    )
    return boundary + centers


def _boundary_counterclockwise_indices(index_rows: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    top = index_rows[0]
    middle = index_rows[1:-1]
    bottom = index_rows[-1]

    left_edges = tuple(row[0] for row in middle)
    bottom_forward = bottom
    right_edges = tuple(row[-1] for row in reversed(middle))
    boundary = tuple(reversed(top)) + left_edges + bottom_forward + right_edges

    boundary_set = set(boundary)
    centers = tuple(
        index
        for row in index_rows[1:-1]
        for index in row[1:-1]
        if index not in boundary_set
    )
    return boundary + centers


def _center_out_indices(index_rows: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    center_row_number = len(index_rows) // 2
    row_order = sorted(
        range(len(index_rows)),
        key=lambda row_number: (abs(row_number - center_row_number), row_number),
    )
    return tuple(index for row_number in row_order for index in index_rows[row_number])


def _validate_indices(indices: tuple[int, ...], bit_count: int) -> None:
    if any(index < 0 or index >= bit_count for index in indices):
        raise ValueError("traversal index out of range")
    if len(indices) != len(set(indices)):
        raise ValueError("traversal duplicates at least one bit index")


_INDEX_ROWS = _layout_index_rows(KNOWN_FORWARD_LAYOUT)
_ROW_ORDER_INDICES = tuple(index for row in _INDEX_ROWS for index in row)

TRAVERSAL_PATHS = {
    "row_order": TraversalPath(
        "row_order",
        _ROW_ORDER_INDICES,
        "confirmed forward line-break layout read top to bottom, left to right",
    ),
    "outside_clockwise": TraversalPath(
        "outside_clockwise",
        _boundary_clockwise_indices(_INDEX_ROWS),
        "candidate outside boundary clockwise, followed by remaining interior bits in row order",
    ),
    "outside_counterclockwise": TraversalPath(
        "outside_counterclockwise",
        _boundary_counterclockwise_indices(_INDEX_ROWS),
        "candidate outside boundary counterclockwise, followed by remaining interior bits in row order",
    ),
    "center_out": TraversalPath(
        "center_out",
        _center_out_indices(_INDEX_ROWS),
        "candidate center row outward traversal over the same fixed rows",
    ),
}
