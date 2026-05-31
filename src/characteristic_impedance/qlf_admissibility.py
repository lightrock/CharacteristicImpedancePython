"""First-pass QLF/ZFA admissibility layer.

This module deliberately separates generated bit observations from interpreted
candidate objects. A tap tape window can be turned into a QLF/ZFA candidate, but
it is admissible only when positive/action and negative/lift twists balance.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

from .core import Z0_PRE_2019_BITS, xor_ring_run
from .zfa import z0_tap_tape


POSITIVE_TWISTS = ("^", ">", "/", "+")
NEGATIVE_TWISTS = ("v", "<", "\\", "-")
BALANCED_BIT_TWIST_PAIRS = {
    "0": "^v",
    "1": "+-",
}


@dataclass(frozen=True)
class QlfCandidate:
    """Candidate interpreted process/capability/proof-like twist object."""

    name: str
    bits: str
    twists: str
    source: str


@dataclass(frozen=True)
class QlfAdmissibility:
    """Admissibility decision for one candidate under twist balance."""

    candidate: QlfCandidate
    positive_count: int
    negative_count: int
    spectral_gap: int
    admissible: bool


@dataclass(frozen=True)
class QlfAdmissibilityReport:
    """First-pass admissibility report over deterministic Z0 tap-tape windows."""

    seed_bits: str
    period_steps: int
    tap_index: int
    candidates: tuple[QlfAdmissibility, ...]


def twist_polarity(twist: str) -> int:
    """Return +1 for action/positive twists, -1 for lift/negative twists."""
    if twist in POSITIVE_TWISTS:
        return 1
    if twist in NEGATIVE_TWISTS:
        return -1
    raise ValueError(f"unknown twist symbol: {twist!r}")


def spectral_gap(twists: str) -> int:
    """Return positive_count - negative_count."""
    return sum(twist_polarity(twist) for twist in twists)


def evaluate_candidate(candidate: QlfCandidate) -> QlfAdmissibility:
    """Evaluate whether a candidate is ZFA-admissible under twist balance."""
    gap = spectral_gap(candidate.twists)
    positive_count = sum(1 for twist in candidate.twists if twist_polarity(twist) == 1)
    negative_count = len(candidate.twists) - positive_count
    return QlfAdmissibility(
        candidate=candidate,
        positive_count=positive_count,
        negative_count=negative_count,
        spectral_gap=gap,
        admissible=gap == 0,
    )


def bits_to_balanced_twists(bits: str) -> str:
    """Map each bit to a balanced twist pair. This is a safe embedding, not a discovery claim."""
    _validate_bits(bits)
    return "".join(BALANCED_BIT_TWIST_PAIRS[bit] for bit in bits)


def bits_to_window_candidate(name: str, bits: str, source: str = "") -> QlfCandidate:
    """Map a bit word into a candidate twist sequence that may be balanced or unbalanced.

    This windowed mapping is intentionally lossy: each bit becomes one twist,
    with `1` selecting from action/positive symbols and `0` selecting from
    lift/negative symbols by position. It creates an inspectable balance test
    without making every candidate automatically admissible.
    """
    _validate_bits(bits)
    twists = "".join(
        POSITIVE_TWISTS[index % len(POSITIVE_TWISTS)]
        if bit == "1"
        else NEGATIVE_TWISTS[index % len(NEGATIVE_TWISTS)]
        for index, bit in enumerate(bits)
    )
    return QlfCandidate(name=name, bits=bits, twists=twists, source=source)


def run_z0_qlf_admissibility_probe(
    tap_index: int = 0,
    window_size: int = 12,
    limit: int = 32,
) -> QlfAdmissibilityReport:
    """Evaluate deterministic Z0 tap-tape windows as QLF/ZFA candidates."""
    if window_size <= 0:
        raise ValueError("window_size must be positive")
    if limit <= 0:
        raise ValueError("limit must be positive")

    run = xor_ring_run(Z0_PRE_2019_BITS)
    tape = z0_tap_tape(Z0_PRE_2019_BITS, tap_index=tap_index, steps=run.period_steps)
    candidates: list[QlfAdmissibility] = []

    for candidate_index in range(limit):
        start = candidate_index * window_size
        end = start + window_size
        if end > len(tape):
            break
        bits = tape[start:end]
        candidate = bits_to_window_candidate(
            name=f"z0_tap{tap_index}_window_{candidate_index:04d}",
            bits=bits,
            source=f"Z0 tap tape bits {start}:{end}",
        )
        candidates.append(evaluate_candidate(candidate))

    return QlfAdmissibilityReport(
        seed_bits=Z0_PRE_2019_BITS,
        period_steps=run.period_steps,
        tap_index=tap_index,
        candidates=tuple(candidates),
    )


def render_qlf_admissibility_markdown(report: QlfAdmissibilityReport) -> str:
    """Render a Markdown report for the QLF/ZFA admissibility layer."""
    admissible_count = sum(1 for result in report.candidates if result.admissible)
    lines = [
        "# Z0 QLF / ZFA Admissibility Probe",
        "",
        "This is not a proof. It does not validate a physics claim or establish",
        "Jim Scarver's framework experimentally.",
        "",
        "This layer separates generated bits from candidate QLF/ZFA admissibility:",
        "the XOR orbit is the generated substrate, tap-tape windows are generated",
        "observation streams, named bit tokens are observed words, and QLF/ZFA",
        "candidate objects are interpreted process/capability/proof-like",
        "structures.",
        "",
        "A candidate is admissible only when positive/action and negative/lift",
        "twists balance to spectral gap zero. Unbalanced candidates are not bad",
        "strings; they are non-admissible under this interpretation.",
        "",
        "## Probe Settings",
        "",
        f"- Seed bits: `{report.seed_bits}`",
        f"- Period: `{report.period_steps}`",
        f"- Tap index: `{report.tap_index}`",
        f"- Candidate windows: `{len(report.candidates)}`",
        f"- Admissible windows: `{admissible_count}`",
        "",
        "## Candidate Windows",
        "",
        "| Candidate | Bits | Twists | Positive | Negative | Spectral gap | Admissible |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for result in report.candidates:
        lines.append(
            f"| {result.candidate.name} | `{result.candidate.bits}` | `{result.candidate.twists}` | "
            f"{result.positive_count} | {result.negative_count} | {result.spectral_gap} | "
            f"{'yes' if result.admissible else 'no'} |"
        )

    lines.extend(
        [
            "",
            "## Next Scientific Step",
            "",
            "The serious next step is comparing admissible candidate rates and",
            "compression/reconstruction performance against alternate constants,",
            "same-density randomized controls, shuffled seeds, and fake token",
            "catalogs. This report only adds the admissibility scaffold.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_qlf_admissibility_html(report: QlfAdmissibilityReport) -> str:
    """Render a standalone HTML report for the QLF/ZFA admissibility layer."""
    admissible_count = sum(1 for result in report.candidates if result.admissible)
    rows = "\n".join(
        "<tr>"
        f"<td>{escape(result.candidate.name)}</td>"
        f"<td><code>{result.candidate.bits}</code></td>"
        f"<td><code>{escape(result.candidate.twists)}</code></td>"
        f"<td>{result.positive_count}</td>"
        f"<td>{result.negative_count}</td>"
        f"<td>{result.spectral_gap}</td>"
        f"<td>{'yes' if result.admissible else 'no'}</td>"
        "</tr>"
        for result in report.candidates
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Z0 QLF / ZFA Admissibility Probe</title>
  <style>
    :root {{
      --ink: #14201b;
      --muted: #58655f;
      --line: #ccd8d2;
      --paper: #fbfcfa;
      --panel: #ffffff;
      --soft: #eef6f1;
      --blue: #245c88;
    }}
    body {{
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: "Segoe UI", Arial, sans-serif;
      line-height: 1.55;
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 36px 20px 64px;
    }}
    h1 {{
      margin: 0;
      font-size: 38px;
      line-height: 1.1;
    }}
    h2 {{
      margin-top: 36px;
      border-bottom: 1px solid var(--line);
      padding-bottom: 8px;
      font-size: 24px;
    }}
    p {{
      max-width: 860px;
    }}
    a {{
      color: var(--blue);
      font-weight: 700;
      text-decoration-thickness: 1px;
      text-underline-offset: 3px;
    }}
    .back-link {{
      display: inline-block;
      margin-bottom: 18px;
    }}
    .lede {{
      color: var(--muted);
      font-size: 18px;
    }}
    .note {{
      padding: 14px 16px;
      border-left: 4px solid var(--blue);
      background: var(--soft);
    }}
    .facts {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-top: 18px;
    }}
    .fact {{
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
    }}
    .fact strong {{
      display: block;
      font-size: 22px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
      background: var(--panel);
      font-size: 14px;
    }}
    th,
    td {{
      border: 1px solid var(--line);
      padding: 8px 10px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: #edf3ef;
    }}
    code {{
      font-family: Consolas, "Courier New", monospace;
    }}
    @media (max-width: 800px) {{
      .facts {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <a class="back-link" href="../index.html">Back to docs index</a>
    <h1>Z0 QLF / ZFA Admissibility Probe</h1>
    <p class="lede">
      A generated first-pass report that separates Z0 tap-tape observations
      from interpreted QLF/ZFA candidate objects. Admissible means positive and
      negative twist counts balance to spectral gap zero.
    </p>

    <div class="note">
      This is not a proof. It does not validate a physics claim or establish
      Jim Scarver's framework experimentally. It only adds an inspectable
      admissibility scaffold.
    </div>

    <h2>Probe Settings</h2>
    <div class="facts">
      <div class="fact"><span>Period</span><strong>{report.period_steps}</strong></div>
      <div class="fact"><span>Tap index</span><strong>{report.tap_index}</strong></div>
      <div class="fact"><span>Windows</span><strong>{len(report.candidates)}</strong></div>
      <div class="fact"><span>Admissible</span><strong>{admissible_count}</strong></div>
    </div>

    <h2>Interpretation Boundary</h2>
    <p>
      The XOR orbit is the generated substrate. Tap-tape windows are generated
      observation streams. Named bit tokens are observed words. QLF/ZFA
      candidates are interpreted process/capability/proof-like structures, and
      unbalanced candidates are non-admissible under this interpretation rather
      than bad strings.
    </p>

    <h2>Candidate Windows</h2>
    <table>
      <thead>
        <tr>
          <th>Candidate</th>
          <th>Bits</th>
          <th>Twists</th>
          <th>Positive</th>
          <th>Negative</th>
          <th>Spectral gap</th>
          <th>Admissible</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>

    <h2>Next Scientific Step</h2>
    <p>
      The serious next step is comparing admissible candidate rates and
      compression/reconstruction performance against alternate constants,
      same-density randomized controls, shuffled seeds, and fake token catalogs.
    </p>
  </main>
</body>
</html>
"""


def _validate_bits(bits: str) -> None:
    if not bits:
        raise ValueError("bits must not be empty")
    invalid = set(bits) - {"0", "1"}
    if invalid:
        raise ValueError("bits must contain only 0 and 1")
