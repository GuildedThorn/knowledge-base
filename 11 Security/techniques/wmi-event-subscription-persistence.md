---
summary: "Registering permanent WMI event filters and consumers to trigger payloads on system events without files on autoruns."
status: active
tags: [security, techniques, wmi, persistence, fileless]
private: false
---

# WMI Event Subscription Persistence

## Purpose

Registering permanent WMI event filters and consumers to trigger payloads on system events without files on autoruns.

## How It Works

- A permanent subscription pairs an `__EventFilter` (a WQL query defining the trigger) with an `__EventConsumer` (the action), joined by a `__FilterToConsumerBinding`.
- All three objects live in the WMI repository (`%SystemRoot%\System32\wbem\Repository`), not in Run keys or the file system, so common autorun tools miss them.
- Filters typically query intrinsic events such as `__InstanceModificationEvent` against `Win32_LocalTime` or `Win32_PerfFormattedData` to fire on a schedule or at boot.
- `CommandLineEventConsumer` runs an arbitrary process; `ActiveScriptEventConsumer` runs inline VBScript or JScript. Both execute as SYSTEM under the WMI provider host.

## Detection

- Objects registered in `root\subscription` (or legacy `root\default`) persist across reboots and survive most cleanup; enumerate them with `Get-WmiObject -Namespace root\subscription`.
- Enable and monitor WMI-Activity operational logging and Sysmon events 19/20/21, which record filter, consumer, and binding creation.
- Treat `scrcons.exe` spawning shells or LOLBins, and `wmiprvse.exe` writing to disk, as high-signal indicators.

## Sources

- MITRE ATT&CK T1546.003 - https://attack.mitre.org/techniques/T1546/003/
- Microsoft Receiving a WMI Event - https://learn.microsoft.com/en-us/windows/win32/wmisdk/receiving-a-wmi-event

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
