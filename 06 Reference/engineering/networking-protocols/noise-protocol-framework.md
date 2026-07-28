---
summary: "Framework for building Diffie-Hellman-based secure channel protocols from composable handshake patterns and a small token language."
status: active
tags: [reference, engineering, networking, noise, handshake, crypto]
private: false
---

# Noise Protocol Framework

## Purpose

A framework for building Diffie-Hellman-based secure channel protocols from composable handshake patterns and a small token language.

## Handshake Patterns and Tokens

- A handshake pattern is a sequence of message patterns built from tokens: `e` and `s` transmit ephemeral/static public keys, and `ee`, `es`, `se`, `ss` perform Diffie-Hellman operations.
- Pattern names encode the initiator/responder static-key situation, e.g. `NN`, `XX`, `IK`, where letters denote whether a static key is absent, transmitted, or known in advance.
- Pre-messages declare keys shared out of band before the handshake begins, which changes the security properties a pattern can offer.

## Symmetric and Cipher State

- A CipherState holds an AEAD key and nonce; a SymmetricState wraps it with a running hash `h` and chaining key `ck` that absorb every token.
- Each DH result is mixed into `ck` via HKDF, deriving fresh keys so later messages depend on all prior key material (the handshake transcript is authenticated).
- After the handshake, split produces two CipherStates for bidirectional transport encryption.

## Security Properties per Pattern

- Payloads gain incrementally stronger guarantees as tokens execute; the spec grades each with confidentiality and authentication levels per message.
- Forward secrecy and identity-hiding depend on the chosen pattern; for example `IK` reveals the initiator static key encrypted, while `XX` defers static transmission for stronger identity protection.
- Noise underpins real protocols including WireGuard, the Signal-adjacent ecosystem, and Lightning Network transport.

## Sources

- The Noise Protocol Framework - https://noiseprotocol.org/noise.html

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
