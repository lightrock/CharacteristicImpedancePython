import unittest
from pathlib import Path

from characteristic_impedance.z0_geometry import (
    KNOWN_FORWARD_LAYOUT,
    TRAVERSAL_PATHS,
    Z0_ORIENTATIONS,
    Z0_SEED_BITS,
    candidate_layout_for_orientation,
    forward_layout_bits,
    render_markdown_report,
    traversal_string,
)


class Z0GeometryTests(unittest.TestCase):
    def test_orientation_bit_strings_match_preserved_documentation(self):
        self.assertEqual(
            Z0_ORIENTATIONS,
            {
                "forward": "101011110110110111000000110001011110101",
                "reverse": "101011110100011000000111011011011110101",
                "inverse": "010100001001001000111111001110100001010",
                "inverse_reverse": "010100001011100111111000100100100001010",
            },
        )

    def test_forward_layout_consumes_original_z0_bits_in_order(self):
        self.assertEqual(forward_layout_bits(), Z0_SEED_BITS)
        self.assertEqual(sum(len(row) for row in KNOWN_FORWARD_LAYOUT), 39)

    def test_candidate_orientation_layouts_use_forward_segment_lengths(self):
        forward_lengths = tuple(len(row) for row in KNOWN_FORWARD_LAYOUT)
        for name, bits in Z0_ORIENTATIONS.items():
            layout = candidate_layout_for_orientation(name)
            self.assertEqual(tuple(len(row) for row in layout), forward_lengths)
            self.assertEqual("".join(layout), bits)

    def test_traversals_do_not_duplicate_or_drop_bits(self):
        expected_indices = set(range(len(Z0_SEED_BITS)))
        for path in TRAVERSAL_PATHS.values():
            with self.subTest(path=path.name):
                self.assertEqual(len(path.bit_indices), len(Z0_SEED_BITS))
                self.assertEqual(set(path.bit_indices), expected_indices)
                self.assertEqual(len(path.bit_indices), len(set(path.bit_indices)))

    def test_outside_clockwise_uses_only_fixed_layout_bits(self):
        outside = traversal_string("outside_clockwise")
        self.assertEqual(len(outside), len(Z0_SEED_BITS))
        self.assertLessEqual(set(outside), set(forward_layout_bits()))

    def test_all_traversal_strings_are_binary(self):
        for name in TRAVERSAL_PATHS:
            with self.subTest(path=name):
                self.assertRegex(traversal_string(name), r"^[01]+$")

    def test_markdown_report_is_generated_from_module_output(self):
        report_path = Path(__file__).resolve().parents[1] / "docs" / "reports" / "z0-orientation-geometry.md"
        self.assertEqual(report_path.read_text(encoding="utf-8"), render_markdown_report())


if __name__ == "__main__":
    unittest.main()
