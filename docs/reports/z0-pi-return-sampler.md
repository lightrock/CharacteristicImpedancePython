# Z0 Pi-Return Sampler

This generated report tests a bounded version of the `fundamentalPi.md`
claim: a finite running process can produce pi operationally through
closure-return statistics, without storing decimal digits of pi or
assuming circles, radians, or primitive geometry.

It is not a proof that Z0 uniquely encodes pi. The report exists to
separate the runnable construction from the control ensembles.

## Method

```text
Z0 seed
-> circular XOR orbit, S_next = S XOR RotL1(S)
-> one tap tape per bit position
-> non-overlapping bit pairs mapped to four relation-walk channels
-> cyclic return windows of length 2n
-> pi_n = 1 / (n * P_return(2n))
```

The four bit-pair channels are a diagnostic harness for return statistics,
not a claim that the substrate is a square lattice.

## Z0 Forward Progression

- Seed bits: `101011110110110111000000110001011110101`
- Seed length: `39`
- Hamming weight: `22`
- XOR steps sampled: `4095`

| n | walk steps | returns | windows | P_return | pi_hat | error |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 19759 | 79833 | 0.247504 | 4.040336 | +0.898743 |
| 2 | 4 | 11068 | 79833 | 0.138639 | 3.606478 | +0.464885 |
| 4 | 8 | 5953 | 79833 | 0.074568 | 3.352637 | +0.211045 |
| 5 | 10 | 4895 | 79833 | 0.061315 | 3.261818 | +0.120226 |
| 8 | 16 | 3152 | 79833 | 0.039482 | 3.165966 | +0.024373 |
| 16 | 32 | 1520 | 79833 | 0.019040 | 3.282607 | +0.141014 |
| 32 | 64 | 804 | 79833 | 0.010071 | 3.102962 | -0.038631 |
| 64 | 128 | 409 | 79833 | 0.005123 | 3.049855 | -0.091738 |
| 80 | 160 | 319 | 79833 | 0.003996 | 3.128252 | -0.013340 |
| 128 | 256 | 203 | 79833 | 0.002543 | 3.072391 | -0.069202 |

## Weyl Orientation Audit

The four canonical Z0 descriptions are tested as descriptions, not
silently promoted to ontology. The table reports selected estimator
values from the same circular-XOR pi-return sampler.

| Orientation | bits | weight | n=8 | n=32 | n=80 | n=128 | mean abs error |
|---|---:|---:|---:|---:|---:|---:|---:|
| Z0 forward | 39 | 22 | 3.165966 | 3.102962 | 3.128252 | 3.072391 | 0.063050 |
| Z0 reverse | 39 | 22 | 3.185166 | 3.489205 | 3.108762 | 3.231582 | 0.156190 |
| Z0 inverse | 39 | 17 | 3.165966 | 3.102962 | 3.128252 | 3.072391 | 0.063050 |
| Z0 inverse-reverse | 39 | 17 | 3.185166 | 3.489205 | 3.108762 | 3.231582 | 0.156190 |

## Shuffled And Same-Density Controls

The empirical p column is the fraction of controls whose pi estimate is
as close or closer to mathematical pi than the Z0 forward estimate at
the same scale, with one-count smoothing.

### same-bit-population shuffled Z0

| n | Z0 pi_hat | control mean | stdev | min | max | controls as close | empirical p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 3.165966 | 3.243308 | 0.069684 | 3.058267 | 3.428075 | 9/128 | 0.078 |
| 16 | 3.282607 | 3.175878 | 0.118586 | 2.892500 | 3.536189 | 100/128 | 0.783 |
| 32 | 3.102962 | 3.091205 | 0.188627 | 2.543100 | 3.674199 | 17/128 | 0.140 |
| 64 | 3.049855 | 3.030478 | 0.275910 | 2.489802 | 3.947439 | 33/128 | 0.264 |
| 80 | 3.128252 | 3.030499 | 0.309448 | 2.370338 | 4.023841 | 3/128 | 0.031 |
| 128 | 3.072391 | 3.083982 | 0.440633 | 2.219556 | 4.130433 | 15/128 | 0.124 |

### same-density random 39-bit seeds

| n | Z0 pi_hat | control mean | stdev | min | max | controls as close | empirical p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 3.165966 | 3.244940 | 0.074346 | 3.064842 | 3.441078 | 18/128 | 0.147 |
| 16 | 3.282607 | 3.186944 | 0.132388 | 2.799979 | 3.636707 | 91/128 | 0.713 |
| 32 | 3.102962 | 3.100118 | 0.165564 | 2.668215 | 3.563973 | 17/128 | 0.140 |
| 64 | 3.049855 | 3.035704 | 0.308095 | 2.422118 | 3.998047 | 24/128 | 0.194 |
| 80 | 3.128252 | 3.000295 | 0.293314 | 2.422118 | 3.838125 | 8/128 | 0.070 |
| 128 | 3.072391 | 3.061416 | 0.442868 | 2.058400 | 4.910987 | 12/128 | 0.101 |

## CODATA Catalog Scan

Profiles scanned: `336` official pre-2019 CODATA rows.

The ranking below uses mean absolute error across the control scales.
This is a diagnostic ranking only. It does not prove physical meaning.

Z0 rank by this crude score: `2`.

| rank | CODATA quantity | bits | weight | mean abs error | n=8 | n=32 | n=80 | n=128 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | neutron Compton wavelength | 37 | 24 | 0.046644 | 3.145307 | 3.139050 | 3.187668 | 3.233393 |
| 2 | characteristic impedance of vacuum | 39 | 22 | 0.063050 | 3.165966 | 3.102962 | 3.128252 | 3.072391 |
| 3 | helion-proton mass ratio | 39 | 17 | 0.064953 | 3.227401 | 3.106826 | 3.147989 | 3.282607 |
| 4 | alpha particle-proton mass ratio | 39 | 19 | 0.072742 | 3.051720 | 3.182119 | 3.005761 | 3.149976 |
| 5 | Compton wavelength | 35 | 20 | 0.095767 | 3.164532 | 2.907670 | 3.035805 | 3.009283 |
| 6 | triton-proton mass ratio | 39 | 20 | 0.105359 | 3.185166 | 3.282607 | 3.293441 | 3.214924 |
| 7 | atomic mass unit-hartree relationship | 35 | 22 | 0.119048 | 3.199580 | 3.100978 | 2.755577 | 3.198438 |
| 8 | electron mass in u | 39 | 26 | 0.135342 | 3.396571 | 3.122380 | 3.138090 | 3.214924 |
| 9 | electron molar mass | 39 | 26 | 0.135342 | 3.396571 | 3.122380 | 3.138090 | 3.214924 |
| 10 | neutron-proton mass ratio | 37 | 19 | 0.140949 | 3.288425 | 3.211457 | 3.242252 | 3.003609 |
| 11 | electron mag. mom. to Bohr magneton ratio | 47 | 20 | 0.146033 | 3.247671 | 3.043048 | 3.099517 | 2.713476 |
| 12 | deuteron-electron mass ratio | 39 | 18 | 0.147156 | 3.292354 | 3.102962 | 2.978843 | 2.676804 |

## Result

The Z0 circular-XOR orbit does produce a sane finite pi-return sampler:
it creates a running closure process whose return statistics enter the
`pi_n = 1 / (n * P_return(2n))` estimator without storing pi.

The control tables are the brake pedal. Any sufficiently unbiased
four-channel walk can produce a pi-return estimator, so the important
question is not whether pi appears at all. The important question is
whether Z0 separates from shuffled seeds, same-density seeds, and other
CODATA constants by drift, variance, anisotropy, finite-period behavior,
or some stronger invariant.

## Declared Limits

- Bit-pair to walk-channel mapping is a diagnostic harness, not substrate.
- Controls use deterministic RNG seeds for reproducibility.
- Same-density controls preserve length and Hamming weight, but not every
  linear cellular-automaton invariant.
- CODATA rows have different bit lengths, so catalog ranking is a lead
  generator, not a normalized final verdict.
- A stronger report should add channel-map permutations, drift/aniso audits,
  exact period handling, and unit/precision transforms.
