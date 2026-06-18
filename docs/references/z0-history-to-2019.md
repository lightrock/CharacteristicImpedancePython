# History of Z0 up to the 2019 SI Break

## Status

This is a sober history note for the `Z0_AsBinary` observation.

It does not claim that the pre-2019 characteristic impedance of vacuum proves a
hidden machine. It preserves the historical chain that made `Z0` a special
information artifact before the 2019 SI revision changed its metrological status.

The short version is:

```text
Maxwell found that electric and magnetic field relations propagate as light.
Plane electromagnetic waves expose a vacuum impedance relation: E/H.
Old SI made μ0 exact through the ampere and c exact through the metre.
Therefore Z0 = μ0 c was exact in old SI.
The pre-2019 value gave a stable decimal artifact.
Z0_AsBinary turns the preserved significant digits into a 39-bit object.
That object then shows machine-like structure that must be tested, not worshiped.
2019 breaks the old exact artifact by redefining the ampere through e.
```

---

## 1. Before Z0 had a name: the electromagnetic/light receipt

The deep history begins before `Z0` is a named constant.

In the mid-19th century, electrical experimenters were comparing electrostatic
and electromagnetic unit systems. Weber and Kohlrausch measured a conversion
ratio between those systems that was strikingly close to the speed of light.

Maxwell saw the machine clue.

His field theory made the relationship explicit:

```text
electric field relation
+ magnetic field relation
+ displacement current
-> electromagnetic wave
-> propagation speed 1 / sqrt(μ ε)
```

For vacuum / free space, that becomes:

```text
c = 1 / sqrt(μ0 ε0)
```

The important receipt is not yet `Z0` as a decimal number. It is this:

```text
electric and magnetic constants are not separate catalog facts;
together they set the propagation behavior of light
```

Through the Maxwell-completion lens, this is the first `Z0` ancestor:

```text
E-side accounting and H-side accounting belong to one running wave process
```

---

## 2. Plane waves expose impedance

For a plane electromagnetic wave in free space, the electric and magnetic field
amplitudes are locked by an impedance-like ratio.

The characteristic impedance of vacuum is commonly written:

```text
Z0 = |E| / |H|
```

and equivalently:

```text
Z0 = sqrt(μ0 / ε0)
Z0 = μ0 c
Z0 = 1 / (ε0 c)
```

This makes `Z0` different from a generic constant. It is not just a number in a
table. It is a relation at the electromagnetic interface:

```text
electric field amplitude
<-> magnetic field amplitude
<-> propagation in free space
<-> impedance / boundary behavior
```

In ordinary engineering language, impedance is about how a system accepts,
transmits, reflects, or resists a wave-like exchange. In this repo's language,
that makes `Z0` an interface receipt.

---

## 3. Unit history makes Z0 exact in old SI

The numerical story depends on SI history.

The old ampere definition fixed the vacuum magnetic permeability:

```text
μ0 = 4π × 10^-7 N A^-2
```

exactly.

The 1983 metre definition fixed the speed of light:

```text
c = 299 792 458 m/s
```

exactly.

Since:

```text
Z0 = μ0 c
```

old SI made the characteristic impedance of vacuum exact as well:

```text
Z0 = (4π × 10^-7) × 299 792 458 Ω
Z0 = 376.73031346177066... Ω
```

CODATA 2014 therefore lists the characteristic impedance of vacuum as:

```text
Z0 = 376.730 313 461... Ω    exact
```

This exactness is not mystical. It is metrological. It comes from how the old SI
stitched together the ampere, the metre, `μ0`, and `c`.

But that is exactly why it matters here. Before 2019, `Z0` was a historically
specific receipt of electromagnetic theory plus unit convention:

```text
Maxwell relation
-> free-space wave impedance
-> ampere definition fixes μ0
-> metre definition fixes c
-> Z0 becomes exact in ohms
-> CODATA publishes a stable decimal artifact
```

---

## 4. The pre-2019 binary seed

`Z0_AsBinary` preserves the significant-digit integer:

```text
376730313461
```

That integer is taken from the pre-2019 / old-SI `Z0` artifact:

```text
Z0 = 376.73031346177066... Ω
```

with decimal point and unit removed for the initial information experiment.

The preserved integer is:

```text
376730313461
```

Its binary form is:

```text
101011110110110111000000110001011110101
```

That is a 39-bit object.

The repo's initial surprise was that this compact 39-bit object did not look
like featureless numerical noise. In the preserved forward segmentation, it can
be read as:

```text
10 10111101 101101 1100000011 000 10111101 01
```

or:

```text
edge
DOWN-like word
UP-like word
STRANGE-like word
gluon-like gap
DOWN-like word
edge
```

This is the point where history turns into the `Z0_AsBinary` research question.

The claim is not:

```text
Z0 proves the Standard Model
```

The claim is:

```text
a historically special electromagnetic interface constant produced a compact
binary object whose native-looking segmentation resembles particle-catalog
machinery strongly enough to deserve controls
```

---

## 5. Why it resembles a machine, not just a number

Through the repo's lens, the pre-2019 `Z0` artifact looks machine-like because it
has several properties at once:

```text
historical provenance -> not an invented seed
interface meaning -> E/H vacuum wave impedance
finite seed -> 39-bit object
edge behavior -> visible boundary bits
word behavior -> intact quark-like signatures
repeat behavior -> repeated DOWN-like word
central gap -> 000 gap / possible gluon-index cue
orientation behavior -> forward, reverse, inverse, inverse-reverse views
process behavior -> executable XOR-ring orbit in the repo
closure behavior -> period / return receipts to test
```

None of these individually proves anything. Together, they motivate the central
question:

```text
is this a post-selected coincidence,
or did the pre-2019 Z0 information artifact preserve a real closure receipt?
```

That is why the project must keep two attitudes at once:

```text
take the resemblance seriously enough to reproduce it exactly
stay skeptical enough to demand controls
```

---

## 6. The 2019 SI break

On 20 May 2019, the revised SI took effect.

The ampere stopped being defined by the old force-between-current-carrying-wires
construction. Instead, it is now defined by fixing the elementary charge:

```text
e = 1.602176634 × 10^-19 C    exact
```

The speed of light remains exact:

```text
c = 299 792 458 m/s    exact
```

But `μ0` is no longer exact. It is now determined experimentally through the
fine-structure constant relationship.

That changes `Z0` too:

```text
Z0 = μ0 c
```

If `μ0` is no longer exact, then `Z0` is no longer exact in SI ohms.

CODATA 2018, under the revised-SI framework, gives:

```text
Z0 = 376.730 313 668(57) Ω
```

Later CODATA values can move as measurements of the fine-structure constant move.
For example, the modern NIST table gives a current value near:

```text
Z0 = 376.730 313 412(59) Ω
```

That is not a contradiction. It is the point.

Before 2019:

```text
Z0 in SI ohms was exact because μ0 and c were exact
```

After 2019:

```text
Z0 in SI ohms is measured because μ0 follows α
```

So the `Z0_AsBinary` seed belongs to a specific historical layer:

```text
pre-2019 CODATA / old-SI exact electromagnetic impedance artifact
```

not to the moving post-2019 measured value.

---

## 7. The correct research posture

The pre-2019 `Z0` value should not be treated as sacred.

A better description is:

```text
Z0 before 2019 is a frozen metrological receipt of Maxwellian electromagnetism,
old SI unit definitions, and CODATA presentation practice.
```

That is exactly why it is useful as a first shovel.

It is historically anchored, physically meaningful, compact enough to inspect,
and transformed by a known rule into a 39-bit object with apparent structure.

The controls should ask:

```text
Do other constants produce comparable whole-word particle signatures?
Do random 39-bit strings produce comparable signatures at the same rate?
Do shuffled or rotated Z0 strings preserve the effect?
Does the effect depend on decimal truncation choices?
Does the effect survive alternative CODATA years?
Does the effect survive unit translation?
Does the XOR orbit preserve anything non-random about the seed?
```

Only after those controls should the project ask whether the structure is a
physical receipt rather than a catalog artifact.

---

## One-line version

```text
Z0 reaches 2019 as Maxwell's free-space E/H impedance made exact by old SI
definitions of μ0 and c; Z0_AsBinary preserves that pre-2019 CODATA artifact as
a 39-bit seed whose quark-facing, boundary-like, and runnable structure looks
machine-like enough to test, while the 2019 SI revision marks the break where Z0
stops being exact and becomes a measured α-dependent quantity.
```

---

## References for context

- [Z0 Binary Structure](../z0-binary-structure.md)
- [Maxwell After the BBQ Gold-Star Lineup](maxwell-after-mead-wolfram-thooft.md)
- [Accelerator and Detector EM Receipts](accelerator-detector-em-receipts.md)
- [Gell-Mann Classification Receipts](gell-mann-classification-receipts.md)
- James Clerk Maxwell, "A Dynamical Theory of the Electromagnetic Field," 1865.
- BIPM, SI Brochure, 9th edition, for the revised SI definitions.
- BIPM, SI base unit: metre, fixing `c = 299 792 458 m/s`.
- BIPM, SI base unit: ampere, fixing `e = 1.602176634 × 10^-19 C`.
- CODATA 2014 recommended constants, listing `Z0 = 376.730 313 461... Ω` exact.
- CODATA 2018 recommended constants, listing `Z0 = 376.730 313 668(57) Ω`.
- NIST CODATA current table for characteristic impedance of vacuum.
- Masao Kitano, "The vacuum impedance and unit systems," 2006.
