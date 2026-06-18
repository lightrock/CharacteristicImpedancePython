# Boltzmann / Gibbs / Wheeler / Landauer / Bennett Receipts

## Status

This is a sober entropy-information-computation note for the Maxwell-completion /
closure-machine program.

It groups the missing information-physicality figures:

```text
Boltzmann -> microstate counting / entropy as multiplicity
Gibbs     -> ensemble entropy / probability distribution over states
Wheeler   -> yes/no question receipts / it-from-bit pressure
Landauer  -> information erasure has physical cost
Bennett   -> reversible computation and logical/thermodynamic distinction
```

Boltzmann and Gibbs are especially important here because they do not merely
"prefigure" information theory. Up to the choice of logarithm base and the
physical unit factor `k_B`, this is the same state-counting math that later
becomes bits.

---

## Boltzmann: physical entropy as microstate multiplicity

Boltzmann's core receipt is:

```text
S = k_B ln W
```

where:

```text
W   -> number of compatible microstates
ln  -> natural logarithm
k_B -> Boltzmann constant, converting state-counting into thermodynamic units
```

The same count in bits is:

```text
bits = log2 W
```

So the conversion is direct:

```text
S = k_B ln 2 * bits
bits = S / (k_B ln 2)
```

That is the missing punchline.
Boltzmann entropy is already a bit count of compatible physical alternatives,
except measured in thermodynamic units rather than base-2 information units.

Through this lens:

```text
macrostate -> many compatible microstates
entropy -> log measure of compatible hidden arrangements
bit count -> number of yes/no distinctions needed to identify the microstate
arrow of time -> typical motion from special states to more numerous states
```

This translates directly toward information entropy because the structure is
already about counting possibilities compatible with a description.

In repo language:

```text
visible receipt -> many possible hidden states
entropy -> how much state multiplicity is hidden behind the same visible surface
bits -> how many binary distinctions are needed to specify the hidden choice
```

That is exactly the bridge to Shannon, Wheeler, Landauer, Bennett, and Lloyd.

---

## Gibbs: ensemble / distribution receipt

Gibbs generalizes the statistical frame:

```text
state of knowledge / ensemble distribution -> entropy over possible states
```

For probabilities over states, Gibbs entropy is:

```text
S_G = -k_B sum_i p_i ln p_i
```

Shannon entropy in bits is:

```text
H = -sum_i p_i log2 p_i
```

Same exact functional form. The conversion is only units:

```text
S_G = k_B ln 2 * H
H   = S_G / (k_B ln 2)
```

This is why Gibbs matters so much for `Z0_AsBinary`.
He is not just "thermodynamics before Shannon."
He supplies the ensemble/probability version of the same entropy math.

Through this lens:

```text
not only one gas box
but probability distributions over possible states
not only one bitstring
but an ensemble of possible bitstrings
```

This matters for controls:

```text
randomized bitstrings
shuffled catalogs
precision cuts
unit changes
null distributions
likelihood comparisons
```

Gibbs is the ancestor of treating a pattern as meaningful only against an
explicit ensemble.

---

## Boltzmann / Gibbs -> bits, exactly

The strong version is:

```text
Boltzmann: S = k_B ln W
bits:      B = log2 W
therefore: S = k_B ln 2 * B
```

and:

```text
Gibbs:   S = -k_B sum p ln p
Shannon: H = -sum p log2 p
therefore: S = k_B ln 2 * H
```

So the conceptual bridge is not a metaphor.
It is the same logarithmic counting law written with different units.
Thermodynamics writes the count in joules per kelvin.
Information theory writes the count in binary alternatives.

This is the `Programming the Universe` receipt:
physical systems register information by occupying one state rather than
another, and physical evolution transforms that registered information.
A molecule, field mode, detector, or bit register is not an abstract symbol
floating above physics; it is a physical state selected from alternatives.

Repo translation:

```text
entropy in thermodynamics -> how many physical alternatives fit the macrostate
entropy in information    -> how many binary alternatives fit the message/state
Z0_AsBinary controls      -> what ensemble of alternatives makes the hit surprising
```

This is why Boltzmann/Gibbs deserve two gold stars.
They are the clean bridge from heat/statistical mechanics into bits without
collapsing into bit mysticism.

---

## Boltzmann -> Shannon bridge

Shannon entropy is not thermodynamic entropy by default, but the mathematical
kinship is not accidental:

```text
Boltzmann/Gibbs -> count compatible physical state possibilities
Shannon         -> count uncertainty / information possibilities in messages
```

The careful statement is:

```text
same logarithmic probability/state-counting form
same conversion through k_B ln 2
not automatically the same physical system
not automatically the same semantics
```

For `Z0_AsBinary`, this is crucial:

```text
a bit hit is not enough;
we need to know the ensemble of possible hits
```

Boltzmann/Gibbs provide the physical-statistical discipline behind Shannon-style
information hygiene.

---

## Wheeler: yes/no question receipt

Wheeler's useful pressure is:

```text
physical meaning may arise from yes/no acts of distinction
```

or in his compressed phrase:

```text
it from bit
```

For this repo, Wheeler is useful but dangerous.

Useful:

```text
binary distinctions may be physically serious
measurement/questions matter
observer-participancy and records cannot be ignored
```

Danger:

```text
information worship
mistaking yes/no payload for substrate
```

So Wheeler should always be paired with Shannon, Landauer, Zurek, and controls.

---

## Landauer: erasure has physical cost

Landauer makes information physical:

```text
erasing information has thermodynamic cost
```

This is a hard guardrail against treating bits as ghostly abstractions.

Machine receipt:

```text
logical operation -> physical process -> thermodynamic consequence
```

For this repo:

```text
if bits are doing work as selectors, triggers, or admissibility marks,
there must be a physical accounting layer
```

---

## Bennett: reversible computation receipt

Bennett clarifies that computation and dissipation are not the same thing.

```text
logical irreversibility -> thermodynamic cost
reversible computation -> computation can in principle avoid erasure cost until reset
```

That matters for closure-machine thinking:

```text
update can be reversible or irreversible
recording and erasure are distinct operations
return/period behavior may matter physically
```

---

## Lloyd / Programming the Universe receipt

Seth Lloyd's useful pressure is the modern computation-language version of the
same bridge:

```text
physical systems register information by being in distinguishable states
physical dynamics transforms those states
collisions and interactions are information-processing events
```

The sober version for this repo is:

```text
not "the universe is literally a laptop"
not "bits are magic substrate"
not "a pretty binary pattern proves ontology"
```

The useful version is:

```text
a physical state selected from W alternatives carries log2 W bits
entropy measures the hidden alternatives behind the visible macrostate
computation is physical state-transition, not abstract symbol shuffling alone
```

This is exactly why Boltzmann/Gibbs must sit next to Wheeler, Landauer, and
Bennett. They give the state-counting math. Lloyd gives the modern machine
language. Landauer/Bennett keep the machine honest about physical cost and
reversibility.

---

## Combined receipt

Together:

```text
Boltzmann -> entropy as hidden physical multiplicity, S = k_B ln W
Gibbs     -> ensemble/probability entropy, S = -k_B sum p ln p
Shannon   -> same entropy form in bits, H = -sum p log2 p
Lloyd     -> physical systems register and process information
Wheeler   -> yes/no question pressure
Landauer  -> information operation has physical cost
Bennett   -> reversibility/erasure distinction
Zurek     -> stable records become objective through copying/witnessing
```

For Maxwell completion:

```text
records are physical,
information is disciplined,
entropy is state multiplicity,
bits are logarithmic state-counts,
erasure costs,
and bits cannot be worshiped as substrate without a running accounting machine
```

---

## Relation to Z0_AsBinary

The `Z0` bit pattern must be treated with this whole stack:

```text
Boltzmann/Gibbs -> compare against ensembles and multiplicities
Shannon         -> count information carefully
Lloyd           -> treat bits as physical state/register/process candidates
Wheeler         -> yes/no distinctions may matter
Landauer        -> bits as operations must have physical accounting
Bennett         -> update/reversal/erasure are different receipts
Zurek           -> hits and records require custody
```

The most important control question is:

```text
what is W?
```

Meaning:

```text
what is the actual ensemble of alternatives?
how many possible encodings, precisions, units, constants, and slices were available?
how many binary distinctions does the observed receipt really select?
```

This is why controls are not optional. A striking pattern is only a receipt after
its ensemble, cost, reversibility, record, and selection context are audited.

---

## One-line version

```text
Boltzmann and Gibbs are already doing bit math: S = k_B ln W is bits = log2 W
with thermodynamic units attached, and Gibbs entropy is Shannon entropy times
k_B ln 2; Wheeler, Lloyd, Landauer, and Bennett then force those bits to become
physical yes/no, registered, cost-bearing, reversible-or-irreversible processes
rather than free-floating bit mysticism.
```

---

## References for context

- [Theory BBQ Lineup](theory-bbq-lineup.md)
- [Leibniz, Binary, Yin/Yang, and Process Receipts](leibniz-binary-yinyang-process-receipt.md)
- [Kitada / Dugić Local-Time Receipts](kitada-dugic-local-time-receipts.md)
- [Smolin Real-Time Receipts](smolin-real-time-receipts.md)
- Ludwig Boltzmann, statistical mechanics and entropy formula `S = k_B ln W`.
- J. Willard Gibbs, ensemble methods and statistical mechanics.
- Claude Shannon, information entropy.
- Seth Lloyd, `Programming the Universe` and physical limits / computational capacity of the universe.
- John Archibald Wheeler, "It from bit" / yes-no question framing.
- Rolf Landauer, information erasure and physical cost.
- Charles Bennett, reversible computation.
