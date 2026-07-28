---
summary: "Linux transparent block-device encryption via dm-crypt with the LUKS on-disk key-management format."
status: active
tags: [reference, engineering, linux, luks, dm-crypt, encryption]
private: false
---

# LUKS and dm-crypt

## Purpose

Linux transparent block-device encryption via dm-crypt with the LUKS on-disk key-management format.

## Core Model

- dm-crypt is a device-mapper target that encrypts and decrypts a block device transparently to layers above it.
- It typically uses AES in XTS mode, deriving a per-sector tweak so identical plaintext yields different ciphertext.
- LUKS is a standardized on-disk format layered on dm-crypt that manages keys and metadata in a header.
- The volume is encrypted with a master key; that key is never stored in plaintext on disk.
- cryptsetup is the userspace tool that formats, opens, and manages LUKS devices.

## How It Works

- The LUKS header holds up to several key slots, each storing the master key encrypted under a passphrase or keyfile.
- Unlocking runs the supplied secret through a memory-hard PBKDF (argon2id in LUKS2, PBKDF2 in LUKS1) to derive a slot key.
- The slot key decrypts the master key, which dm-crypt then uses for all sector operations.
- Multiple slots allow independent passphrases/keyfiles; revoking one does not affect the others.

## Security Notes

- The header (and its backups) is critical; losing all key slots or the header makes data unrecoverable.
- Argon2 PBKDF parameters trade unlock latency against brute-force resistance.
- dm-crypt provides confidentiality, not authentication; pair with integrity layers (dm-integrity/LUKS2) where tamper detection matters.

## Sources

- cryptsetup and LUKS - https://gitlab.com/cryptsetup/cryptsetup
- man8 - cryptsetup(8) - https://man7.org/linux/man-pages/man8/cryptsetup.8.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
