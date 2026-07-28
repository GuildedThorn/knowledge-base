---
summary: "BB84 distributes a secret key using conjugate-basis single-photon encoding whose security rests on the no-cloning theorem."
status: active
tags: [reference, science, physics, qkd, cryptography, no-cloning]
private: false
---

# BB84 Quantum Key Distribution

## Purpose

BB84 distributes a secret key using conjugate-basis single-photon encoding whose security rests on the no-cloning theorem.

## How It Works

- Alice encodes each random bit on a single photon in one of two conjugate bases chosen at random: rectilinear (0°/90°) or diagonal (45°/135°).
- Bob measures each photon in a randomly chosen basis; when his basis differs from Alice's the outcome is random and carries no reliable information.
- Over a public authenticated channel they compare only which bases were used (never the bit values) and discard mismatched positions — the "sifting" step.
- Because non-orthogonal states cannot be perfectly copied (no-cloning theorem), an eavesdropper cannot intercept-and-resend without disturbing the states.

## Security Notes

- Eavesdropping is detected as an elevated quantum bit error rate on a sacrificed sample of the sifted key; above a threshold the key is aborted.
- Surviving key bits are processed with classical error correction (reconciliation) and privacy amplification to shrink any partial information Eve holds to negligible.
- Practical systems face side channels — multi-photon pulses (photon-number-splitting) and detector attacks — mitigated by decoy states and measurement-device-independent QKD.
- Security is information-theoretic given the protocol assumptions, unlike computational public-key schemes.

## Sources

- Bennett & Brassard (1984), reprinted Theoretical Computer Science 2014 - https://doi.org/10.1016/j.tcs.2014.05.025
- Scarani et al., The security of practical QKD (arXiv:0802.4155) - https://arxiv.org/abs/0802.4155

## Related

- [Science and Physics - Index](kb://06-reference-science-physics-science-physics-index)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
