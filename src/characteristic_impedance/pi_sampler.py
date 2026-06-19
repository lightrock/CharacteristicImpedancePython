"""Pi-return samplers for Z0 circular-XOR closure experiments."""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
import re
import statistics
from pathlib import Path

from .core import Z0_PRE_2019_BITS, invert_bits, reverse_bits, xor_ring_step


PAIR_STEPS: dict[str, tuple[int, int]] = {
    "00": (1, 0),
    "01": (-1, 0),
    "10": (0, 1),
    "11": (0, -1),
}

DEFAULT_PI_SCALES: tuple[int, ...] = (1, 2, 4, 5, 8, 16, 32, 64, 80, 128)
DEFAULT_CONTROL_SCALES: tuple[int, ...] = (8, 16, 32, 64, 80, 128)
Z0_PERIOD_STEPS = 4095


@dataclass(frozen=True)
class PiReturnEstimate:
    """One finite-depth return-statistics estimate of pi."""

    n: int
    walk_steps: int
    return_count: int
    total_windows: int
    probability: float
    pi_hat: float

    @property
    def absolute_error(self) -> float:
        return abs(self.pi_hat - math.pi)


@dataclass(frozen=True)
class SeedPiProfile:
    """Pi-return profile for one seed under circular-XOR evolution."""

    name: str
    seed_bits: str
    steps: int
    estimates: tuple[PiReturnEstimate, ...]
    note: str = ""

    @property
    def bit_length(self) -> int:
        return len(self.seed_bits)

    @property
    def hamming_weight(self) -> int:
        return self.seed_bits.count("1")

    @property
    def mean_control_error(self) -> float:
        return statistics.mean(estimate.absolute_error for estimate in self.estimates)


@dataclass(frozen=True)
class ScaleControlSummary:
    """Control distribution summary for one estimator scale."""

    n: int
    observed: float
    mean: float
    stdev: float
    minimum: float
    maximum: float
    controls_as_close_or_closer: int
    trials: int

    @property
    def empirical_p_close_or_closer(self) -> float:
        return (self.controls_as_close_or_closer + 1) / (self.trials + 1)


@dataclass(frozen=True)
class SeedControlSummary:
    """Control profile summary across selected pi-return scales."""

    label: str
    summaries: tuple[ScaleControlSummary, ...]


@dataclass(frozen=True)
class PiSamplerReport:
    """Generated report object for the Z0 pi-return sampler."""

    z0_profile: SeedPiProfile
    orientation_profiles: tuple[SeedPiProfile, ...]
    shuffled_controls: SeedControlSummary
    same_density_controls: SeedControlSummary
    codata_profiles: tuple[SeedPiProfile, ...]
    codata_top_by_error: tuple[SeedPiProfile, ...]
    codata_z0_rank: int | None


def xor_tap_tapes(seed_bits: str, steps: int = Z0_PERIOD_STEPS) -> tuple[str, ...]:
    """Return one tap tape per bit position after repeated circular-XOR updates."""
    _validate_bits(seed_bits)
    if steps <= 0:
        raise ValueError("steps must be positive")

    current = seed_bits
    columns = [[] for _ in seed_bits]
    for _ in range(steps):
        current = xor_ring_step(current)
        for index, bit in enumerate(current):
            columns[index].append(bit)
    return tuple("".join(column) for column in columns)


def pair_counts_from_tapes(tapes: tuple[str, ...]) -> dict[str, int]:
    """Count non-overlapping bit pairs across tap tapes."""
    counts = {pair: 0 for pair in PAIR_STEPS}
    for tape in tapes:
        for index in range(0, len(tape) - 1, 2):
            counts[tape[index : index + 2]] += 1
    return counts


def pi_return_profile(
    seed_bits: str,
    *,
    name: str = "seed",
    steps: int = Z0_PERIOD_STEPS,
    scales: tuple[int, ...] = DEFAULT_PI_SCALES,
    note: str = "",
) -> SeedPiProfile:
    """Run the circular-XOR tap sampler and estimate pi from return statistics."""
    tapes = xor_tap_tapes(seed_bits, steps=steps)
    estimates = pi_return_estimates_from_tapes(tapes, scales=scales)
    return SeedPiProfile(name=name, seed_bits=seed_bits, steps=steps, estimates=estimates, note=note)


def pi_return_estimates_from_tapes(
    tapes: tuple[str, ...],
    *,
    scales: tuple[int, ...] = DEFAULT_PI_SCALES,
) -> tuple[PiReturnEstimate, ...]:
    """Estimate pi from cyclic return windows over bit-pair relation walks."""
    if not tapes:
        raise ValueError("tapes must not be empty")

    prefixes: list[tuple[list[int], list[int], int]] = []
    for tape in tapes:
        pairs = [tape[index : index + 2] for index in range(0, len(tape) - 1, 2)]
        if not pairs:
            continue
        steps = [PAIR_STEPS[pair] for pair in pairs]
        extended_steps = steps + steps
        prefix_x = [0]
        prefix_y = [0]
        for dx, dy in extended_steps:
            prefix_x.append(prefix_x[-1] + dx)
            prefix_y.append(prefix_y[-1] + dy)
        prefixes.append((prefix_x, prefix_y, len(steps)))

    estimates: list[PiReturnEstimate] = []
    for n in scales:
        walk_steps = 2 * n
        return_count = 0
        total_windows = 0
        for prefix_x, prefix_y, pair_count in prefixes:
            if walk_steps > pair_count:
                continue
            for start in range(pair_count):
                returned = (
                    prefix_x[start + walk_steps] - prefix_x[start] == 0
                    and prefix_y[start + walk_steps] - prefix_y[start] == 0
                )
                if returned:
                    return_count += 1
            total_windows += pair_count
        probability = return_count / total_windows if total_windows else 0.0
        pi_hat = 1.0 / (n * probability) if probability else math.inf
        estimates.append(
            PiReturnEstimate(
                n=n,
                walk_steps=walk_steps,
                return_count=return_count,
                total_windows=total_windows,
                probability=probability,
                pi_hat=pi_hat,
            )
        )
    return tuple(estimates)


def z0_orientation_profiles(
    *,
    steps: int = Z0_PERIOD_STEPS,
    scales: tuple[int, ...] = DEFAULT_CONTROL_SCALES,
) -> tuple[SeedPiProfile, ...]:
    """Return pi profiles for the four canonical Z0 orientations."""
    forward = Z0_PRE_2019_BITS
    reverse = reverse_bits(forward)
    inverse = invert_bits(forward)
    inverse_reverse = reverse_bits(inverse)
    return (
        pi_return_profile(forward, name="Z0 forward", steps=steps, scales=scales),
        pi_return_profile(reverse, name="Z0 reverse", steps=steps, scales=scales),
        pi_return_profile(inverse, name="Z0 inverse", steps=steps, scales=scales),
        pi_return_profile(inverse_reverse, name="Z0 inverse-reverse", steps=steps, scales=scales),
    )


def shuffled_z0_controls(
    *,
    trials: int = 128,
    rng_seed: int = 376730313461,
    steps: int = Z0_PERIOD_STEPS,
    scales: tuple[int, ...] = DEFAULT_CONTROL_SCALES,
) -> SeedControlSummary:
    """Compare Z0 against shuffles of its exact 39-bit population."""
    rng = random.Random(rng_seed)
    observed = pi_return_profile(Z0_PRE_2019_BITS, name="Z0 forward", steps=steps, scales=scales)
    profiles = []
    population = list(Z0_PRE_2019_BITS)
    for index in range(trials):
        shuffled = population[:]
        rng.shuffle(shuffled)
        profiles.append(
            pi_return_profile(
                "".join(shuffled),
                name=f"shuffle_{index:03d}",
                steps=steps,
                scales=scales,
            )
        )
    return summarize_profile_controls("same-bit-population shuffled Z0", observed, tuple(profiles))


def same_density_random_controls(
    *,
    trials: int = 128,
    rng_seed: int = 230519,
    steps: int = Z0_PERIOD_STEPS,
    scales: tuple[int, ...] = DEFAULT_CONTROL_SCALES,
) -> SeedControlSummary:
    """Compare Z0 against random 39-bit seeds with the same Hamming weight."""
    rng = random.Random(rng_seed)
    observed = pi_return_profile(Z0_PRE_2019_BITS, name="Z0 forward", steps=steps, scales=scales)
    ones = Z0_PRE_2019_BITS.count("1")
    zeros = len(Z0_PRE_2019_BITS) - ones
    profiles = []
    for index in range(trials):
        bits = ["1"] * ones + ["0"] * zeros
        rng.shuffle(bits)
        profiles.append(
            pi_return_profile(
                "".join(bits),
                name=f"same_density_{index:03d}",
                steps=steps,
                scales=scales,
            )
        )
    return summarize_profile_controls("same-density random 39-bit seeds", observed, tuple(profiles))


def summarize_profile_controls(
    label: str,
    observed: SeedPiProfile,
    controls: tuple[SeedPiProfile, ...],
) -> SeedControlSummary:
    """Summarize how often controls are as close to pi as the observed profile."""
    if not controls:
        raise ValueError("controls must not be empty")
    summaries: list[ScaleControlSummary] = []
    for index, observed_estimate in enumerate(observed.estimates):
        control_values = [profile.estimates[index].pi_hat for profile in controls]
        finite_values = [value for value in control_values if math.isfinite(value)]
        observed_error = observed_estimate.absolute_error
        summaries.append(
            ScaleControlSummary(
                n=observed_estimate.n,
                observed=observed_estimate.pi_hat,
                mean=statistics.mean(finite_values),
                stdev=statistics.pstdev(finite_values),
                minimum=min(finite_values),
                maximum=max(finite_values),
                controls_as_close_or_closer=sum(
                    1 for value in finite_values if abs(value - math.pi) <= observed_error
                ),
                trials=len(finite_values),
            )
        )
    return SeedControlSummary(label=label, summaries=tuple(summaries))


def load_codata_binary_records(path: Path) -> tuple[tuple[str, str], ...]:
    """Load `(quantity, bits)` records from the generated CODATA binary Markdown."""
    records: list[tuple[str, str]] = []
    row_pattern = re.compile(r"^\|\s*\d+\s*\|\s*(?P<name>.*?)\s*\|.*?\|\s*`(?P<bits>[01]+)`\s*\|")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = row_pattern.match(line)
        if match:
            records.append((match.group("name"), match.group("bits")))
    return tuple(records)


def codata_pi_profiles(
    binary_markdown_path: Path,
    *,
    steps: int = Z0_PERIOD_STEPS,
    scales: tuple[int, ...] = DEFAULT_CONTROL_SCALES,
    max_records: int | None = None,
) -> tuple[SeedPiProfile, ...]:
    """Run pi-return profiles over the generated CODATA binary catalog."""
    records = load_codata_binary_records(binary_markdown_path)
    if max_records is not None:
        records = records[:max_records]
    profiles: list[SeedPiProfile] = []
    for name, bits in records:
        profiles.append(
            pi_return_profile(
                bits,
                name=name,
                steps=steps,
                scales=scales,
                note="pre-2019 CODATA 2014 generated binary row",
            )
        )
    return tuple(profiles)


def build_pi_sampler_report(
    repo_root: Path,
    *,
    control_trials: int = 128,
    steps: int = Z0_PERIOD_STEPS,
    scales: tuple[int, ...] = DEFAULT_CONTROL_SCALES,
) -> PiSamplerReport:
    """Build the generated Z0 pi-return sampler report object."""
    z0_profile = pi_return_profile(
        Z0_PRE_2019_BITS,
        name="Z0 forward",
        steps=steps,
        scales=DEFAULT_PI_SCALES,
        note="pre-2019 characteristic impedance of vacuum",
    )
    orientation_profiles = z0_orientation_profiles(steps=steps, scales=scales)
    shuffled = shuffled_z0_controls(trials=control_trials, steps=steps, scales=scales)
    same_density = same_density_random_controls(trials=control_trials, steps=steps, scales=scales)
    codata = codata_pi_profiles(
        repo_root / "docs" / "codata" / "pre-2019-codata-2014-binary.md",
        steps=steps,
        scales=scales,
    )
    ranked = sorted(codata, key=lambda profile: profile.mean_control_error)
    z0_rank = next(
        (
            index + 1
            for index, profile in enumerate(ranked)
            if profile.name.lower() == "characteristic impedance of vacuum"
        ),
        None,
    )
    return PiSamplerReport(
        z0_profile=z0_profile,
        orientation_profiles=orientation_profiles,
        shuffled_controls=shuffled,
        same_density_controls=same_density,
        codata_profiles=codata,
        codata_top_by_error=tuple(ranked[:12]),
        codata_z0_rank=z0_rank,
    )


def render_pi_sampler_markdown(report: PiSamplerReport) -> str:
    """Render the Z0 pi-return sampler report as Markdown."""
    lines = [
        "# Z0 Pi-Return Sampler",
        "",
        "This generated report tests a bounded version of the `fundamentalPi.md`",
        "claim: a finite running process can produce pi operationally through",
        "closure-return statistics, without storing decimal digits of pi or",
        "assuming circles, radians, or primitive geometry.",
        "",
        "It is not a proof that Z0 uniquely encodes pi. The report exists to",
        "separate the runnable construction from the control ensembles.",
        "",
        "## Method",
        "",
        "```text",
        "Z0 seed",
        "-> circular XOR orbit, S_next = S XOR RotL1(S)",
        "-> one tap tape per bit position",
        "-> non-overlapping bit pairs mapped to four relation-walk channels",
        "-> cyclic return windows of length 2n",
        "-> pi_n = 1 / (n * P_return(2n))",
        "```",
        "",
        "The four bit-pair channels are a diagnostic harness for return statistics,",
        "not a claim that the substrate is a square lattice.",
        "",
        "## Z0 Forward Progression",
        "",
        f"- Seed bits: `{report.z0_profile.seed_bits}`",
        f"- Seed length: `{report.z0_profile.bit_length}`",
        f"- Hamming weight: `{report.z0_profile.hamming_weight}`",
        f"- XOR steps sampled: `{report.z0_profile.steps}`",
        "",
        "| n | walk steps | returns | windows | P_return | pi_hat | error |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for estimate in report.z0_profile.estimates:
        lines.append(
            f"| {estimate.n} | {estimate.walk_steps} | {estimate.return_count} | "
            f"{estimate.total_windows} | {estimate.probability:.6f} | "
            f"{estimate.pi_hat:.6f} | {estimate.pi_hat - math.pi:+.6f} |"
        )

    lines.extend(
        [
            "",
            "## Weyl Orientation Audit",
            "",
            "The four canonical Z0 descriptions are tested as descriptions, not",
            "silently promoted to ontology. The table reports selected estimator",
            "values from the same circular-XOR pi-return sampler.",
            "",
            "| Orientation | bits | weight | n=8 | n=32 | n=80 | n=128 | mean abs error |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for profile in report.orientation_profiles:
        values = {estimate.n: estimate.pi_hat for estimate in profile.estimates}
        lines.append(
            f"| {profile.name} | {profile.bit_length} | {profile.hamming_weight} | "
            f"{values[8]:.6f} | {values[32]:.6f} | {values[80]:.6f} | "
            f"{values[128]:.6f} | {profile.mean_control_error:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Shuffled And Same-Density Controls",
            "",
            "The empirical p column is the fraction of controls whose pi estimate is",
            "as close or closer to mathematical pi than the Z0 forward estimate at",
            "the same scale, with one-count smoothing.",
            "",
        ]
    )
    lines.extend(_render_control_summary(report.shuffled_controls))
    lines.extend([""])
    lines.extend(_render_control_summary(report.same_density_controls))

    lines.extend(
        [
            "",
            "## CODATA Catalog Scan",
            "",
            f"Profiles scanned: `{len(report.codata_profiles)}` official pre-2019 CODATA rows.",
            "",
            "The ranking below uses mean absolute error across the control scales.",
            "This is a diagnostic ranking only. It does not prove physical meaning.",
            "",
            f"Z0 rank by this crude score: `{report.codata_z0_rank}`.",
            "",
            "| rank | CODATA quantity | bits | weight | mean abs error | n=8 | n=32 | n=80 | n=128 |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for rank, profile in enumerate(report.codata_top_by_error, start=1):
        values = {estimate.n: estimate.pi_hat for estimate in profile.estimates}
        lines.append(
            f"| {rank} | {profile.name} | {profile.bit_length} | {profile.hamming_weight} | "
            f"{profile.mean_control_error:.6f} | {values[8]:.6f} | {values[32]:.6f} | "
            f"{values[80]:.6f} | {values[128]:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Result",
            "",
            "The Z0 circular-XOR orbit does produce a sane finite pi-return sampler:",
            "it creates a running closure process whose return statistics enter the",
            "`pi_n = 1 / (n * P_return(2n))` estimator without storing pi.",
            "",
            "The control tables are the brake pedal. Any sufficiently unbiased",
            "four-channel walk can produce a pi-return estimator, so the important",
            "question is not whether pi appears at all. The important question is",
            "whether Z0 separates from shuffled seeds, same-density seeds, and other",
            "CODATA constants by drift, variance, anisotropy, finite-period behavior,",
            "or some stronger invariant.",
            "",
            "## Declared Limits",
            "",
            "- Bit-pair to walk-channel mapping is a diagnostic harness, not substrate.",
            "- Controls use deterministic RNG seeds for reproducibility.",
            "- Same-density controls preserve length and Hamming weight, but not every",
            "  linear cellular-automaton invariant.",
            "- CODATA rows have different bit lengths, so catalog ranking is a lead",
            "  generator, not a normalized final verdict.",
            "- A stronger report should add channel-map permutations, drift/aniso audits,",
            "  exact period handling, and unit/precision transforms.",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_control_summary(summary: SeedControlSummary) -> list[str]:
    lines = [
        f"### {summary.label}",
        "",
        "| n | Z0 pi_hat | control mean | stdev | min | max | controls as close | empirical p |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary.summaries:
        lines.append(
            f"| {row.n} | {row.observed:.6f} | {row.mean:.6f} | {row.stdev:.6f} | "
            f"{row.minimum:.6f} | {row.maximum:.6f} | "
            f"{row.controls_as_close_or_closer}/{row.trials} | "
            f"{row.empirical_p_close_or_closer:.3f} |"
        )
    return lines


def _validate_bits(bits: str) -> None:
    if not bits:
        raise ValueError("bits must not be empty")
    invalid = set(bits) - {"0", "1"}
    if invalid:
        raise ValueError("bits must contain only 0 and 1")
