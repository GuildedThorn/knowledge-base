---
summary: "Memory forensics recovers runtime artifacts such as processes, modules, handles, sockets, credentials, injected code, and malware state."
status: active
tags: [security, dfir, memory-forensics, volatility]
private: false
---

# Memory Forensics with Volatility

## Purpose

Memory forensics recovers runtime artifacts such as processes, modules, handles, sockets, credentials, injected code, and malware state.

## Key Ideas

- Volatility 3 models memory through layers, symbol tables, plugins, contexts, and renderers.
- RAM captures can reveal unpacked malware, live network state, injected memory, terminated artifacts, and decrypted config not present on disk.
- Analysis quality depends on acquisition integrity, OS/kernel symbol support, and preserving the original image.

## Defensive Use

- Acquire memory before powering off when volatile evidence matters, and hash/store images with case metadata.
- Run repeatable plugin sets for triage, then focus on anomalies: hidden processes, suspicious modules, network connections, callbacks, and injected regions.

## Sources

- Volatility 3 documentation - https://volatility3.readthedocs.io/en/latest/index.html
- Volatility 3 Basics - https://volatility3.readthedocs.io/en/latest/basics.html
- The Art of Memory Forensics - https://memoryanalysis.net/amf

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
