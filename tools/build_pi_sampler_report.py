"""Build the generated Z0 pi-return sampler report."""

from __future__ import annotations

from pathlib import Path

from characteristic_impedance import build_pi_sampler_report, render_pi_sampler_markdown


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "reports"


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report = build_pi_sampler_report(ROOT)
    (REPORT_DIR / "z0-pi-return-sampler.md").write_text(
        render_pi_sampler_markdown(report),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
