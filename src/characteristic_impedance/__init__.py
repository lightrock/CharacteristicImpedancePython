"""Python-first characteristic impedance helpers."""

from .core import (
    ConstantRecord,
    XorRunResult,
    Z0_PRE_2019,
    Z0_PRE_2019_BITS,
    Z0_PRE_2019_DIGITS,
    characteristic_impedance_vacuum,
    digits_to_bits,
    invert_bits,
    orientations,
    reverse_bits,
    xor_ring_run,
    xor_ring_step,
)
from .z0_geometry import (
    KNOWN_FORWARD_LAYOUT,
    TRAVERSAL_PATHS,
    Z0_ORIENTATIONS,
    Z0_SEED_BITS,
    candidate_layout_for_orientation,
    forward_layout_bits,
    render_markdown_report,
    traversal_string,
)

__all__ = [
    "ConstantRecord",
    "XorRunResult",
    "Z0_PRE_2019",
    "Z0_PRE_2019_BITS",
    "Z0_PRE_2019_DIGITS",
    "characteristic_impedance_vacuum",
    "digits_to_bits",
    "invert_bits",
    "orientations",
    "reverse_bits",
    "xor_ring_run",
    "xor_ring_step",
    "KNOWN_FORWARD_LAYOUT",
    "TRAVERSAL_PATHS",
    "Z0_ORIENTATIONS",
    "Z0_SEED_BITS",
    "candidate_layout_for_orientation",
    "forward_layout_bits",
    "render_markdown_report",
    "traversal_string",
]
