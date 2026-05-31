import unittest

from characteristic_impedance import (
    QlfCandidate,
    bits_to_balanced_twists,
    evaluate_candidate,
    render_qlf_admissibility_html,
    render_qlf_admissibility_markdown,
    run_z0_qlf_admissibility_probe,
    spectral_gap,
    twist_polarity,
)


class QlfAdmissibilityTests(unittest.TestCase):
    def test_twist_polarity(self):
        self.assertEqual(twist_polarity("^"), 1)
        self.assertEqual(twist_polarity("v"), -1)

    def test_spectral_gap(self):
        self.assertEqual(spectral_gap("^v+-"), 0)

    def test_evaluate_candidate_marks_balanced_admissible(self):
        candidate = QlfCandidate(name="balanced", bits="01", twists="^v+-", source="test")
        result = evaluate_candidate(candidate)
        self.assertTrue(result.admissible)
        self.assertEqual(result.spectral_gap, 0)

    def test_evaluate_candidate_marks_unbalanced_non_admissible(self):
        candidate = QlfCandidate(name="unbalanced", bits="11", twists="^>+", source="test")
        result = evaluate_candidate(candidate)
        self.assertFalse(result.admissible)
        self.assertEqual(result.spectral_gap, 3)

    def test_bits_to_balanced_twists_produces_balanced_sequence(self):
        twists = bits_to_balanced_twists("01")
        self.assertEqual(spectral_gap(twists), 0)

    def test_z0_qlf_admissibility_probe_returns_limited_candidates(self):
        report = run_z0_qlf_admissibility_probe(limit=8)
        self.assertEqual(len(report.candidates), 8)
        self.assertEqual(report.period_steps, 4095)

    def test_markdown_report_declares_scope(self):
        report = run_z0_qlf_admissibility_probe(limit=8)
        markdown = render_qlf_admissibility_markdown(report)
        self.assertIn("not a proof", markdown)
        self.assertIn("spectral gap", markdown)
        self.assertIn("admissible", markdown)

    def test_html_report_links_back_to_docs_index(self):
        report = run_z0_qlf_admissibility_probe(limit=8)
        html = render_qlf_admissibility_html(report)
        self.assertIn("../index.html", html)
        self.assertIn("Z0 QLF / ZFA Admissibility Probe", html)


if __name__ == "__main__":
    unittest.main()
