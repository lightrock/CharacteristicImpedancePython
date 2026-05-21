from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "codata"))

from build_codata_docs import build, parse_nist_ascii, read_source_table, value_mantissa_digits  # noqa: E402


class CodataToolTests(unittest.TestCase):
    def test_value_mantissa_digits_ignores_exponent_and_noise(self):
        self.assertEqual(value_mantissa_digits("376.730 313 461..."), "376730313461")
        self.assertEqual(value_mantissa_digits("6.626 070 040 e-34"), "6626070040")
        self.assertEqual(value_mantissa_digits("-2.002 319 304 361 82"), "200231930436182")

    def test_source_table_preserves_z0_anchor(self):
        records = read_source_table(ROOT / "docs" / "codata" / "pre-2019-codata-2014-source.md")
        self.assertEqual(len(records), 336)
        z0 = next(record for record in records if record.quantity == "characteristic impedance of vacuum")
        self.assertEqual(z0.significant_digits, "376730313461")
        self.assertEqual(z0.bits, "101011110110110111000000110001011110101")

    def test_bits_only_file_is_pure_bits_and_matches_row_count(self):
        source = ROOT / "docs" / "codata" / "pre-2019-codata-2014-source.md"
        records = read_source_table(source)
        bits_only = ROOT / "docs" / "codata" / "pre-2019-codata-2014-bits-only.txt"
        lines = bits_only.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), len(records))
        self.assertTrue(lines)
        for line in lines:
            self.assertRegex(line, r"^[01]+$")

    def test_build_recreates_generated_files(self):
        source = ROOT / "docs" / "codata" / "pre-2019-codata-2014-source.md"
        with tempfile.TemporaryDirectory() as temp_dir:
            out_dir = Path(temp_dir)
            build(source, out_dir)
            self.assertTrue((out_dir / "pre-2019-codata-2014-binary.md").exists())
            self.assertTrue((out_dir / "pre-2019-codata-2014-bits-only.txt").exists())
            lines = (out_dir / "pre-2019-codata-2014-bits-only.txt").read_text(encoding="utf-8").splitlines()
            self.assertIn("101011110110110111000000110001011110101", lines)

    def test_parse_nist_ascii_recovers_complete_official_table(self):
        raw_source = ROOT / "docs" / "codata" / "pre-2019-codata-2014-raw.txt"
        records = parse_nist_ascii(raw_source)
        self.assertEqual(len(records), 336)
        self.assertEqual(records[0].quantity, "{220} lattice spacing of silicon")
        self.assertTrue(any(record.quantity == "characteristic impedance of vacuum" for record in records))
        self.assertEqual(records[-1].quantity, "Wien wavelength displacement law constant")


if __name__ == "__main__":
    unittest.main()
