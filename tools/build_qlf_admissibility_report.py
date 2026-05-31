"""Build the generated Z0 QLF/ZFA admissibility report."""

from __future__ import annotations

from pathlib import Path

from characteristic_impedance import (
    render_qlf_admissibility_html,
    render_qlf_admissibility_markdown,
    run_z0_qlf_admissibility_probe,
)


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "reports"


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report = run_z0_qlf_admissibility_probe()
    (REPORT_DIR / "z0-qlf-admissibility-probe.md").write_text(
        render_qlf_admissibility_markdown(report),
        encoding="utf-8",
    )
    (REPORT_DIR / "z0-qlf-admissibility-probe.html").write_text(
        render_qlf_admissibility_html(report),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
