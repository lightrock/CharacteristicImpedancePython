import math
import unittest

from characteristic_impedance import (
    Z0_PRE_2019_BITS,
    pair_counts_from_tapes,
    pi_return_profile,
    xor_tap_tapes,
)


class PiSamplerTests(unittest.TestCase):
    def test_xor_tap_tapes_preserve_z0_period_shape(self):
        tapes = xor_tap_tapes(Z0_PRE_2019_BITS)

        self.assertEqual(len(tapes), 39)
        self.assertTrue(all(len(tape) == 4095 for tape in tapes))

    def test_z0_pair_counts_match_documented_sampler(self):
        counts = pair_counts_from_tapes(xor_tap_tapes(Z0_PRE_2019_BITS))

        self.assertEqual(
            counts,
            {
                "00": 20092,
                "01": 19757,
                "10": 20227,
                "11": 19757,
            },
        )

    def test_z0_pi_return_profile_matches_recorded_values(self):
        profile = pi_return_profile(
            Z0_PRE_2019_BITS,
            scales=(1, 2, 4, 5, 8, 16, 32, 64, 80, 128),
        )
        by_scale = {estimate.n: estimate for estimate in profile.estimates}

        self.assertEqual(by_scale[1].return_count, 19759)
        self.assertEqual(by_scale[1].total_windows, 79833)
        self.assertAlmostEqual(by_scale[1].pi_hat, 4.040336, places=6)
        self.assertAlmostEqual(by_scale[8].pi_hat, 3.165966, places=6)
        self.assertAlmostEqual(by_scale[32].pi_hat, 3.102962, places=6)
        self.assertAlmostEqual(by_scale[80].pi_hat, 3.128252, places=6)
        self.assertAlmostEqual(by_scale[128].pi_hat, 3.072391, places=6)
        self.assertLess(abs(by_scale[80].pi_hat - math.pi), 0.02)


if __name__ == "__main__":
    unittest.main()
