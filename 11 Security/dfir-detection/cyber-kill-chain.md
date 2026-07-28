---
summary: "The Cyber Kill Chain models intrusions as seven sequential phases from reconnaissance to actions on objectives."
status: active
tags: [security, dfir, kill-chain, intrusion-phases]
private: false
---

# Lockheed Martin Cyber Kill Chain

## Purpose

The Cyber Kill Chain models intrusions as seven sequential phases from reconnaissance to actions on objectives.

## Seven Phases

- Reconnaissance: research and targeting of victims, harvesting emails and infrastructure.
- Weaponization: coupling an exploit with a backdoor into a deliverable payload.
- Delivery: transmitting the weapon (email attachment, web link, USB) to the target.
- Exploitation: triggering the vulnerability to run adversary code.
- Installation: planting a persistent backdoor or implant on the host.
- Command & Control (C2): establishing a channel for remote hands-on-keyboard control.
- Actions on Objectives: exfiltration, destruction, lateral movement, or other goals.

## Intelligence-Driven Defense

- The model is analytic, not just descriptive: earlier detection breaks the chain before objectives are met.
- Defenders map observed indicators to phases, exposing gaps and recurring adversary campaigns.
- Detecting and disrupting any single phase can defeat the whole intrusion, forcing costly adversary retooling.

## Course-of-Action Matrix

- Cross the seven phases against defensive actions: detect, deny, disrupt, degrade, deceive, and destroy.
- The matrix drives phase-based mitigation planning and highlights where controls are thin.

## Sources

- Lockheed Martin Cyber Kill Chain - https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
- Intelligence-Driven Defense Paper - https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
