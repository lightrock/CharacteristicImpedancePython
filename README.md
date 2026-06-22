# Z0_AsBinary

> The so called "Characteristic Impedance of Vacuum"... however that's not what it appears to say about itself in its own words.
> Meanwhile, physics often treats a successful predictive formalism as though it were the machine itself. Shouldn't we know better than to allow that?

A fundamental observation of the pre-2019 CODATA value for the Characteristic Impedance of Vacuum is very intereseting and has opened up can of worms.

One portion of the can of worms can ask such qeustions as "As a running process, wouldn't the "chromodynamics machine" be considered "an observer"? How is everybody seeming to still miss that obvious and immediate thought while considering the universe as a process or processing?

## What This Repo Is

This repository is a research instrument, not a completed proof.

It currently provides:

- A tested Python reproduction of the pre-2019 `Z0` circular-XOR loop result.
- A complete pre-2019 CODATA 2014 evidence chain with raw source text, parsed
  official rows, derived binary rows, and a bits-only corpus.
- Legacy BigCalc2 observations translated into GitHub-readable Markdown notes.
- A process-first / closure-machine doctrine map for interpreting what the code
  is testing and what it is not allowed to assume.
- A falsification-first roadmap: randomized controls, catalog-wide scans,
  precision tests, unit-translation tests, and null-result reporting.

## Start Here

- Initial Observation: Z0 Binary Structure:
  [Z0 Binary Structure](https://lightrock.github.io/Z0_AsBinary/z0-binary-structure.html).

- Interesting so far, "quark data compression" of fundamental constants:
  [Z0 Quark GeneZip Compression](https://lightrock.github.io/Z0_AsBinary/z0-genezip-compression.html).

- For the evidence files, read [Evidence Chain](#evidence-chain).
- For the process-first doctrine, read [Process-First Physics](docs/references/process-first-physics.md).
- For the speculative observer/open-closed question, read [Speculative Observer Question: Built-In Open/Closed Horizons](docs/references/observer-built-in-open-closed.md).
- For the theory critique map, read [Theory BBQ Lineup](docs/references/theory-bbq-lineup.md).
- For the new chromodyne/electron gold-star addendum, read [Chromodyne / Electron Lineage Gold Stars](docs/references/chromodyne-electron-lineage-gold-stars.md).
- For the closure question behind `π`, read [Fundamental Pi](docs/references/fundamentalPi.md).
- For the Z0 sparse `π` machine and the explicit elastic-hashing / hash-table firebreak analogy, read [Z0 Machine as a Sparse Pi Machine](docs/references/z0-sparse-pi-machine.md).
- For Jim/QLF's Apéry-period carryback into Fundamental Pi, read [Fundamental Pi: QLF Apéry Carryback](docs/references/fundamental-pi-qlf-apery-carryback.md).
- We are asking this question next in the quark GeneZip compression work:
  [Fine-Structure Constant Alpha and GeneZip](docs/references/fine-structure-alpha-genezip-question.md).
- Next closure target after alpha:
  [Electron as Minimal Stable Charged Spinor Closure](https://lightrock.github.io/Z0_AsBinary/references/electron-minimal-stable-charged-spinor-closure.html).
- For the runnable `Z0`/`π` return-sampler report, read [Z0/Pi Return Sampler](https://lightrock.github.io/Z0_AsBinary/reports/z0-pi-return-sampler.html).
- For the Maxwell/Mead/Wolfram/'t Hooft synthesis, read [Maxwell After Mead, Wolfram, and 't Hooft](docs/references/maxwell-after-mead-wolfram-thooft.md).


## Thesis

Mature physics compresses empirical reality into a finite symbolic catalog of
authoritative constants. Once a constant is published, its significant digits can
be treated as an information object.

The working hypothesis is that the characteristic impedance of vacuum is not
just another constant in that catalog. It may be the impedance boundary between
physical measurement and symbolic compression: a compact seed whose simple
binary evolution reconstructs or intersects an unusually large fraction of the
other published constant bit patterns.

### Sparse/firebreak warning

The Z0 sparse-pi work now explicitly borrows the lesson from elastic hashing and
hash-table firebreaks: a greedy process that fills every locally available slot
can destroy future reachability, while a sparse/firebreak rule preserves useful
access near saturation. In Z0_AsBinary language, gaps, failed returns, skipped
windows, and unclaimed taps are not automatically garbage. They may be part of
the closure layout that makes the return census meaningful.

```text
Greedy occupancy is not the machine.
Firebreaks can be functional structure.
A sparse closure layout can preserve reachability.
```

### Speculative observer/open-closed question

```text
Speculative? Observer is built-in and is naturally open/closed. Question mark.
```

This is not a claim that a human mind creates physics. The question is whether
the massively parallel process-first chromodyne / closure universe is already
observer-like because it generates, bounds, stabilizes, limits, compares, and
preserves information receipts.

In that framing, local minds are finite-capacity information horizons inside a
larger process. Open/closed may be an asymptotic limit state under rate,
coupling, locality, and information-capacity limits, not a primitive binary
metaphysical switch.

```text
Observation is bounded closure, not eyeballs.
Small brain cannot model large brain all at once.
```

Longer note: [Speculative Observer Question: Built-In Open/Closed Horizons](docs/references/observer-built-in-open-closed.md).

## Evidence Chain

The project keeps the full pre-2019 source and derived binary evidence in-tree:

- [CODATA Evidence Chain](docs/codata/README.md) explains the conversion rule
  and rebuild process.
- [Pre-2019 CODATA 2014 Raw Text](docs/codata/pre-2019-codata-2014-raw.txt)
  preserves the raw NIST-style all-values text used as the import source.
- [Pre-2019 CODATA 2014 Source](docs/codata/pre-2019-codata-2014-source.md)
  preserves 336 official named/value/unit rows currently used by the project.
- [Pre-2019 CODATA 2014 Binary](docs/codata/pre-2019-codata-2014-binary.md)
  preserves the same rows with significant digits and binary forms.
- [Pre-2019 CODATA 2014 Bits Only](docs/codata/pre-2019-codata-2014-bits-only.txt)
  is the stripped corpus for pure bit experiments.
- [Legacy Physics Token Catalog](docs/tokens/legacy-physics-token-catalog.md)
  preserves the non-CODATA quark/hadron/convenience rows that BigCalc2 appended
  to its local NIST file so they could be treated like named bit tokens.
- [Z0 Orientation Geometry Report](docs/reports/z0-orientation-geometry.md)
  preserves the four canonical Z0 orientations, the known forward manual layout,
  and candidate natural traversals without treating them as proof.

## Why Pre-2019 Z0 Matters

The 2019 SI revision is not treated here as a mere bookkeeping change. It is
treated as a change in the published information structure of the constants
catalog.

Before the revised SI, the vacuum electromagnetic constants occupied a different
definitional status. After the revision, the SI is defined through exact values
assigned to selected defining constants, including `c`, `h`, and `e`. Under that
regime, the vacuum magnetic permeability and the impedance of free space are no
longer fixed in the same way; they become tied to the measured fine-structure
constant.

This project therefore treats the pre-2019 `Z0` value as a historically specific
information object. The question is not whether a unit convention is sacred. The
question is whether the pre-2019 catalog preserved a compact symbolic seed that
is structurally special under simple computational tests.


### Core Project Notes

- [Information-First Position](docs/information-first-position.md) states the
  central thesis: physical constants are compressed information artifacts before
  they are physics classroom objects, and unit objections must be tested as
  encoding transformations rather than used as a dismissal.
- [Fundamental Pi](docs/references/fundamentalPi.md) asks what physical machine
  produces the closure represented by `π`, `2π`, phase, rotation, and emergent
  geometry, without treating the symbol as the substrate.
- [Z0 Machine as a Sparse Pi Machine](docs/references/z0-sparse-pi-machine.md)
  makes the elastic-hashing / hash-table firebreak issue explicit: sparse gaps,
  failed returns, and skipped windows can preserve reachability and may be part
  of the closure layout rather than waste.
- [Speculative Observer Question: Built-In Open/Closed Horizons](docs/references/observer-built-in-open-closed.md)
  asks whether observerhood is built into the massively parallel chromodyne /
  closure process, with local observers acting as finite information horizons
  and open/closed treated as rate/capacity-relative limit behavior.
- [Fundamental Pi: QLF Apéry Carryback](docs/references/fundamental-pi-qlf-apery-carryback.md)
  records Jim Whitescarver's QLF-side update: `Z0_AsBinary` has been carried into
  `Physical_Pi.md` as another closure-process machine, while QLF's
  `QLF_AperyPeriod.lean` now uses the same central-binomial closure census to
  render `ζ(3)` as a second period receipt.
- [Maxwell Machine Completion Note](docs/references/maxwell-machine-completion-note.md)
  preserves the project posture that Heaviside gives the public interface of
  electromagnetism, while Maxwell preserves the unfinished machine question that
  `Z0` may help turn into testable information-substrate experiments.
- [Pre-Maxwell Electromagnetic Receipt Ledger](docs/references/pre-maxwell-electromagnetic-receipt-ledger.md)
  itemizes the receipt pile Maxwell inherited, now including Boscovich as the
  pre-field point-force / anti-hard-marble ancestor.
- [Boscovich Point-Force Receipts](docs/references/boscovich-point-force-receipts.md)
  records why Boscovich matters here: matter as non-extended centers plus lawful
  attraction/repulsion relations, not primitive hard substance.
- [Maxwell After Mead, Wolfram, and 't Hooft](docs/references/maxwell-after-mead-wolfram-thooft.md)
  states the direct completion frame: Maxwell asks for the engine, Mead points
  to phase handshake, Wolfram and 't Hooft make executable substructure
  respectable, and `Z0_AsBinary` tests whether `Z0` left a binary closure receipt.
- [Carver Mead, Pointer-Swap Closure, and Z0](docs/references/mead-pointer-swap-z0.md)
  connects Mead's phase-handshake electrodynamics to the pointer-swap closure
  model and reframes `Z0` as a possible catalog-visible impedance receipt of EM
  phase-matching, not as a sacred ohm value.
- [Chromodyne / Electron Lineage Gold Stars](docs/references/chromodyne-electron-lineage-gold-stars.md)
  keeps Pati-Salam, Harari-Shupe, Bilson-Thompson, Furey, Wheeler, 't Hooft,
  and Susskind attached to the electron/chromodyne question without collapsing
  the claim into the false statement that electrons carry QCD color.

### Process / Closure Doctrine

- [Process-First Physics](docs/references/process-first-physics.md) captures the
  doctrine that process is already running, while space and coordinate time are
  rendered accounting layers of relation, delay, closure, persistence, and
  observer-facing records.
- [QGP, Boundary Receipts, and the Pancake Inversion](docs/references/qgp-boundary-receipts.md)
  records the high-energy version of the same audit: if the available receipt is
  sheet-like or boundary-like, reconstructed 3D geometry should not be silently
  promoted above the receipt as substrate.
- [Computational Process Lineage](docs/references/computational-process-lineage.md)
  compares Wolfram and 't Hooft as near process-first ancestors: one finds the
  universal walk / everything-generator, the other the machine-instinct, while
  both still need closure depth, pruning, persistence, and rendered observer
  geometry/time.
- [Friston, Free Energy, and the Closure Machine](docs/references/friston-free-energy-closure-machine.md)
  treats Markov blankets, active inference, and free-energy minimization as
  serious persistence machinery that still begins after an admissible system has
  already formed.
- [Quantum Structures of the Hydrogen Atom](docs/references/quantum-structures-hydrogen-atom.md)
  records the Dugić/Francom/Arsenijević structure-selection point: hydrogen is
  not merely electron plus proton in space, but a case where environment,
  operation, and access select the physically usable quantum structure.

### Theory BBQ / Critique Notes

- [Theory BBQ Lineup](docs/references/theory-bbq-lineup.md) is the concise index
  of process-first critiques and repairs across string theory, LQG, Wolfram,
  't Hooft, Wheeler, Tegmark, Everett, Einstein/GR, causal sets, thermodynamic
  gravity, Kitada/Dugić, Friston, Feynman, and related approaches.
- [Chromodyne / Electron Lineage Gold Stars](docs/references/chromodyne-electron-lineage-gold-stars.md)
  is the BBQ addendum for the electron/chromodyne lineage: Pati-Salam,
  Harari-Shupe, Bilson-Thompson, Furey, Wheeler, 't Hooft, and Susskind.
- [String Theory, Holography, and the Closure Machine](docs/references/string-theory-closure-machine.md)
  argues that string/M-theory is best repaired as a holographic/geometric
  rendering language for finite closure, not as the substrate itself.
- [Loop Quantum Gravity and the Closure Machine](docs/references/lqg-closure-machine.md)
  treats LQG as a serious discrete receipt layer that still needs the deeper
  event machine: closure, admissibility, persistence, and process ordering.

### Legacy Reports

- [Legacy Genetic Sequence Analysis](docs/legacy-genetic-sequence-analysis.md)
  explains what the old BigCalc2 "gene" machinery was doing: circular tape
  decomposition, Z0-facet compression, ablation controls, and Z0-as-running-tape
  scans.
- [Legacy Physics Token Catalog](docs/tokens/legacy-physics-token-catalog.md)
  calls out the appended quark and hadron rows from BigCalc2, including their
  values, significant digits, and binary strings.
- [Z0 Orientation Geometry Report](docs/reports/z0-orientation-geometry.md)
  makes fixed bits, orientation, layout, traversal, and interpretation explicit
  before later quark genetic sequence decomposition work.
- [Z0 Binary Structure](docs/z0-binary-structure.md) captures the 2019 PDF/RTF
  observation that the characteristic impedance bits already contain whole
  quark mass-signature words, arrange naturally into a gluon-like chart, and
  come from a prime significant-digit integer with a primitive Pythagorean
  triple identity.

Note: the Markdown documents linked above are the GitHub-readable versions.
The companion HTML files in `docs/` are much nicer looking when opened locally
or through a static site, but GitHub's repository file browser shows them as
source code unless GitHub Pages or another static host is used.

### Done

- Reproduce the legacy `Z0` XOR-ring period result.
- Add core bit helpers: significant digits to bits, reverse, invert, canonical
  orientations, XOR ring step, and XOR ring run.
- Add Apache 2.0 licensing, notice, package metadata, and GitHub Actions tests.
- Capture the information-first thesis in project docs.
- Capture the Z0 quark/gluon binary-structure observation in project docs.
- Analyze and document the legacy BigCalc2 genetic-sequence machinery.
- Add a complete pre-2019 CODATA 2014 evidence chain with raw source, 336 parsed
  official rows, generated binary rows, and bits-only files.
- Add tests for the CODATA conversion and document rebuild path.

## References

- BIPM, [The International System of Units (SI)](https://www.bipm.org/en/measurement-units).
- NIST, [SI Redefinition](https://www.nist.gov/si-redefinition).
- Pierre Fayet, SI units completion paper, arXiv:1906.05123.
