
• The short version: you already have the SIEM core. What’s missing is independent resilience, broader visibility, behavioral detection, and automatic response—not Elastic
  or Wazuh.

  ### Highest-priority gaps

  1. Nothing watches the SOC from outside the SOC (DONE)

     Loki, Prometheus, Grafana, and alerting all live on the same soc VM. Prometheus can notice Loki failing, but a dead VM, Proxmox host, LAN, or Discord path leaves
     nothing able to notify you. Add an off-box dead-man heartbeat and a second notification path.

  2. The controls have not been fully proven

     The canary produces events, but its silence alert has never deliberately been exercised end-to-end. The rollout explicitly calls for stopping the canary and node
     exporter and confirming Discord delivery. Every rule should have an intentional test and recorded result. /home/thorn/Documents/knowledge-base/08 Improvements/SIEM-SOC
     Rollout.md:58

  3. The analyst-review layer is currently broken

     The three-times-daily automated review stopped performing analysis on August 1 because its Claude subscription access was disabled. Grafana’s real-time alerts still
     work, but the second-line review is presently just logging authentication errors. /home/thorn/Documents/knowledge-base/09 Observability/SIEM Review Log.md:375

  4. Evidence is neither offsite nor immutable

     Loki evidence and Prometheus backups depend on TrueNAS. There are no NAS snapshots, replication, offsite observability backup, documented Proxmox vzdump, or tested
     restore. A NAS loss or compromise takes the historical evidence with it. /home/thorn/Documents/knowledge-base/08 Improvements/Backup and DR Strategy.md:30

  ### Visibility gaps

  - Proxmox and TrueNAS are blind spots. These are precisely the systems hosting the SOC and its evidence, yet neither ships logs or metrics.
  - DNS telemetry is missing. pfSense Unbound queries are not in Loki, removing one of the best signals for C2, DGA, and unexpected outbound behavior.
  - pfSense filter logs are not confirmed. Perimeter Suricata arrives, but firewall allow/block decisions still need verification and proper dashboards.
  - The websites Suricata sensor is thin. It exports alert, anomaly, and ssh, but not dns, tls, or flow, so it acts mainly as a signature alarm rather than a network-
    security-monitoring sensor. /home/thorn/Documents/ThornixOS/modules/services/suricata.nix:66

  - There is no east-west sensor. websites sees itself and pfSense sees the perimeter, but lateral LAN traffic is largely invisible. A SPAN-port sensor and VLANs/isolated
    segments are the structural fix. /home/thorn/Documents/knowledge-base/09 Observability/SIEM and SOC - Architecture.md:31

  ### Detection and response gaps

  - CrowdSec is detect-only. Each host has a local LAPI, but there is no central decision point or pfSense bouncer. Nothing currently blocks automatically.
  - Audit data is collected but underused. Identity changes, privilege execution, SSH configuration changes, module loading, and similar events reach Loki, but most are
    dashboard/review material rather than tuned alerts.

  - Correlation and baselining are limited. Most alerts are direct threshold checks. There are no strong rules for new internal service access, unusual lateral flows, log-
    volume deviation, or multi-stage activity. The July 29 review found a suspicious websites → MongoDB internal flow that the paging policy at that time would not have
    escalated. /home/thorn/Documents/knowledge-base/09 Observability/SIEM Review Log.md:287

  - No vulnerability-management loop. The Nix closures provide an unusually precise software inventory, but nothing currently scans them for advisories and exports critical
    findings into Prometheus.

  - No purple-team regression suite or deception beyond pipeline health. There is no disposable attack segment, honeypot, audited fake credential, or canary DNS name.

  ### Hardening gap

  Loki has authentication disabled and uses plain HTTP; Loki 3100 and Prometheus 9090 are open across the LAN. That means the design trusts every LAN participant not to
  read or inject telemetry. On a flat network, a compromised host could poison the record you rely on. /home/thorn/Documents/ThornixOS/modules/computers/soc.nix:94 and /
  home/thorn/Documents/ThornixOS/hosts/soc/networking.nix:23

  My implementation order would be:

  1. External dead-man monitoring plus a second notification channel. (DONE)
  2. Fix the scheduled review and fire-drill every alert.
  3. Add Proxmox, TrueNAS, DNS, and pfSense filter telemetry.
  4. Create an offsite/immutable evidence copy and perform a restore drill.
  5. Add Suricata flow/TLS/DNS telemetry and lateral-movement rules.
  6. Centralize CrowdSec and deploy the pfSense bouncer.
  7. Introduce VLANs, a SPAN sensor, vulnerability scanning, and purple-team tests.

  I would not add Elastic, Wazuh, TheHive, distributed Loki, or another large appliance yet. For a one-person SOC, those add operational weight without fixing the actual
  blind spots above.