# Atomic Red Team

Small, portable **detection tests** mapped 1:1 to [MITRE ATT&CK](https://attack.mitre.org/) techniques — Red Canary's [atomic-red-team](https://github.com/redcanaryco/atomic-red-team). Each "atomic" is a single technique executed in isolation so you can answer one question: *when T1059.001 runs on this host, does my pipeline see it?* This is the purple-team bridge between the offensive side ([Tools Index](kb://11-security-tools-tools-index)) and the blue side ([SIEM/SOC Architecture](kb://09-observability-siem-and-soc-architecture)) — it exists to **validate detections**, not to gain access.

> ⚠️ Runs real (benign) attacker behaviour: touches the registry, spawns LOLBins, drops files, opens sockets. **Lab / owned hosts only**, and expect ClamAV/CrowdSec/Suricata to react — that reaction *is* the test. Never run on production or another party's estate. See [SIEM-SOC Rollout → Purple-team loop](kb://08-improvements-siem-soc-rollout).

## Anatomy

- **Atomics** live in `atomics/T####/T####.yaml`, one folder per ATT&CK technique, with a matching markdown doc. Each defines `input_arguments`, `executor` (`command_prompt`, `powershell`, `sh`, `bash`, `manual`), and — critically — a `cleanup_command` to undo the change.
- **Coverage** is broadest on Windows, solid on Linux/macOS. Check the technique's `supported_platforms` before assuming.
- **Invoke-AtomicRedTeam** is the PowerShell runner (cross-platform via `pwsh`) that reads those YAMLs — install/run/cleanup with dependency handling.

## Run it (Invoke-AtomicRedTeam)

```powershell
# install runner + atomics (pwsh works on Linux too)
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1' -UseBasicParsing)
Install-AtomicRedTeam -getAtomics

Invoke-AtomicTest T1059.001 -ShowDetailsBrief   # what would run
Invoke-AtomicTest T1059.001 -GetPrereqs          # fetch deps
Invoke-AtomicTest T1059.001                       # execute
Invoke-AtomicTest T1059.001 -Cleanup              # ALWAYS undo after
```

Scope with `-TestNumbers 1,3` or `-TestGuids <guid>`. `Invoke-AtomicTest All` exists but is a firehose — pick techniques deliberately.

## The loop against *this* SOC

The point isn't the attack, it's confirming the [SIEM/SOC](kb://08-improvements-siem-soc-rollout) chain lights up. Run a technique, then verify each layer:

1. **auditd → Loki** — execve/file-watch record arrives (needs `execScope="all"` on headless hosts; this is the same chain the [detection canary](kb://09-observability-siem-and-soc-architecture) guards).
2. **Suricata** — network techniques (C2, transfer) surface as EVE alerts on `websites`.
3. **CrowdSec** — brute-force / recon atomics trip a scenario (detect-only today).
4. **Grafana `siem` alerts** — did the rule fire and reach Discord? A technique that runs silently is a **detection gap → write the LogQL/rule**.

Map candidate atomics to the rules you already have: T1110 (SSH brute force), T1059 (shell execution → execve audit), T1105 (ingress transfer → Suricata), T1543/T1547 (persistence → identity/unit watches). Track gaps back in [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout).

## Integration notes

- **Blocked on isolation** — a proper end-to-end purple-team run wants the disposable segment that's gated on [VLANs](kb://05-network-vlans). Until then, run single atomics on an owned lab host and watch the pipeline, not `Invoke-AtomicTest All` across the fleet.
- **Not a C2 / not stealthy** — ART makes noise on purpose. For adversary emulation with evasion, that's a different tool class; ART's job is coverage measurement.
- Pairs with [Caldera](https://github.com/mitre/caldera) if you later want automated, chained emulation instead of hand-run atomics.

## Related

- [Offensive Tools — Index](kb://11-security-tools-tools-index)
- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout) · [SIEM/SOC Architecture](kb://09-observability-siem-and-soc-architecture)
- [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow)
- [Security Map](kb://01-maps-security-map)
