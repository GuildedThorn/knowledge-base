---
summary: "The Ising model of interacting spins is the canonical lattice system for studying phase transitions and critical phenomena."
status: active
tags: [reference, science, physics, phase-transition, spin, criticality]
private: false
---

# The Ising Model

## Purpose

The Ising model of interacting spins is the canonical lattice system for studying phase transitions and critical phenomena.

## Core Model

- Spins $s_i = \pm 1$ sit on a lattice with Hamiltonian $H = -J\sum_{\langle ij\rangle} s_i s_j - h\sum_i s_i$, summing over nearest-neighbor pairs.
- $J > 0$ favors ferromagnetic alignment; $J < 0$ is antiferromagnetic. The field $h$ couples to net magnetization.
- The order parameter is the mean magnetization per spin, nonzero in the ordered phase.

## Phase Behavior

- In 1D there is no finite-temperature phase transition; order survives only at $T = 0$ (Ising's original result).
- In 2D on the square lattice, Onsager (1944) solved the zero-field model exactly, giving $T_c$ at $\sinh(2J/k_BT_c)=1$ and a logarithmically divergent specific heat.
- Below $T_c$ the model shows spontaneous magnetization $\propto (1 - \sinh^{-4}(2J/k_BT))^{1/8}$, later confirmed by Yang; the exponent $\beta = 1/8$.
- The 2D Ising universality class fixes critical exponents shared by many real uniaxial magnets and lattice gases.

## Sources

- Onsager (1944), Crystal Statistics I (Phys Rev 65.117) - https://journals.aps.org/pr/abstract/10.1103/PhysRev.65.117
- Scholarpedia: Ising model - http://www.scholarpedia.org/article/Ising_model

## Related

- [Science and Physics - Index](kb://06-reference-science-physics-science-physics-index)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
