---
summary: "Shor's quantum algorithm factors integers in polynomial time by reducing factoring to quantum period-finding."
status: active
tags: [reference, science, physics, factoring, period-finding, qft]
private: false
---

# Shor's Algorithm

## Purpose

Shor's quantum algorithm factors integers in polynomial time by reducing factoring to quantum period-finding.

## How It Works

- Factoring `N` reduces to finding the period `r` of the function `f(x) = a^x mod N` for a random base `a` coprime to `N`.
- Given an even period `r` with `a^(r/2) ≠ -1 mod N`, computing `gcd(a^(r/2) ± 1, N)` yields a nontrivial factor via classical number theory.
- The quantum core prepares a superposition, applies modular exponentiation as a reversible circuit, then uses the quantum Fourier transform (QFT) to concentrate amplitude at multiples of `1/r`.
- Measuring the QFT output gives a fraction that continued-fraction expansion converts into the period `r`; the whole routine repeats a few times to handle bad outcomes.

## Key Ideas

- Runtime is polynomial (roughly `O((log N)^3)`), an exponential speedup over the best known classical factoring algorithms like the general number field sieve.
- Period-finding is an instance of the hidden subgroup problem over abelian groups, which the QFT solves efficiently.
- The same machinery breaks discrete-logarithm systems, so a large fault-tolerant quantum computer threatens RSA, Diffie-Hellman, and elliptic-curve cryptography — the motivation for post-quantum cryptography.

## Sources

- Shor, Polynomial-Time Algorithms for Factoring (arXiv:quant-ph/9508027) - https://arxiv.org/abs/quant-ph/9508027
- Nielsen & Chuang, Quantum Computation and Quantum Information - http://www.michaelnielsen.org/qcqi/

## Related

- [Science and Physics - Index](kb://06-reference-science-physics-science-physics-index)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
