---
summary: "DFT recasts the many-electron problem in terms of electron density via the Hohenberg-Kohn theorems and Kohn-Sham equations."
status: active
tags: [reference, science, physics, dft, electronic-structure, exchange-correlation]
private: false
---

# Density Functional Theory

## Purpose

DFT recasts the many-electron problem in terms of electron density via the Hohenberg-Kohn theorems and Kohn-Sham equations.

## Foundational Theorems

- The first Hohenberg-Kohn theorem (1964) proves the ground-state electron density $n(\mathbf{r})$ uniquely determines the external potential, and hence all ground-state properties.
- The second theorem establishes a variational principle: the true density minimizes the total-energy functional $E[n]$.
- This replaces the $3N$-coordinate many-body wavefunction with a single 3D density field as the basic variable.

## Kohn-Sham Scheme

- Kohn and Sham (1965) map the interacting system onto a fictitious system of non-interacting electrons that reproduces the same density.
- Solving the single-particle Kohn-Sham equations self-consistently yields orbitals whose squared magnitudes sum to the density.
- All many-body complexity is folded into the exchange-correlation functional $E_{xc}[n]$, whose exact form is unknown.

## Exchange-Correlation Functionals

- The local density approximation (LDA) uses the uniform electron gas; generalized gradient approximations (GGA, e.g. PBE) add density gradients.
- Hybrid functionals (e.g. B3LYP) mix in a fraction of exact Hartree-Fock exchange, improving many molecular energetics.
- Functional accuracy governs DFT's reliability; it underpins most modern electronic-structure and materials calculations.

## Sources

- Hohenberg & Kohn (1964) (Phys Rev 136.B864) - https://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B864
- Kohn & Sham (1965) (Phys Rev 140.A1133) - https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
- Nobel Prize in Chemistry 1998 (Kohn) - https://www.nobelprize.org/prizes/chemistry/1998/summary/

## Related

- [Science and Physics - Index](kb://06-reference-science-physics-science-physics-index)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
