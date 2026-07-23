---
summary: "Capture the FORScan-on-NixOS setup notes from `~/Downloads/forscan-linux-nixos.md`, which had real, detailed setup work but no vault note."
status: active
tags: [hobbies]
---

## Purpose

Capture the FORScan-on-NixOS setup notes from `~/Downloads/forscan-linux-nixos.md`, which had real, detailed setup work but no vault note.

## Why Not a Rewrite

FORScan (Ford/Mazda/Lincoln OBD diagnostics and As-Built configuration) is closed-source and depends on ~15 years of reverse-engineered proprietary UDS/KWP2000 protocol work, per-ECU module definition databases, and adapter/timing-sensitive CAN handling that the FORScan authors themselves built up over time. The notes conclude a faithful rewrite is realistically a 5–15+ person-year undertaking and the wrong tool for the job — since **FORScan already runs on Linux today via Wine/Proton** with the main work being USB/serial passthrough, not a rewrite.

## NixOS + Wine Setup (as documented)

1. **32-bit graphics support** (`hardware.graphics.enable32Bit` on NixOS ≥24.11, or `hardware.opengl.driSupport32Bit` on older releases) — FORScan is a 32-bit-ish Windows app.
2. **System packages**: `wineWowPackages.stable` (combined 32/64-bit Wine), `winetricks`, `socat` (bridges a WiFi/BT ELM327 into a Wine-visible COM port), `usbutils`, `picocom` (sanity-checks the serial link outside Wine first).
3. **udev rules** giving a stable `/dev/ttyOBD` symlink for the common ELM327 USB chip vendor:product IDs (CH340, FTDI, CP210x, PL2303) — ch341/ftdi_sio/cp210x/pl2303 kernel modules autoload on plug, no `boot.kernelModules` needed.
4. **Dedicated Wine prefix** (`WINEARCH=win32`), install via `wine FORScanSetup2.3.71.release.exe`.
5. **Adapter → COM port mapping**: symlink `/dev/ttyOBD` into `dosdevices/comN` for a USB adapter; for a WiFi ELM327, bridge the TCP socket to a pseudo-terminal with `socat pty,link=$WINEPREFIX/dosdevices/comN,raw,echo=0 tcp:<adapter-ip>:<port>` (a `systemd.user.services.obd-bridge` unit can automate this); Bluetooth SPP adapters work the same way via `rfcomm bind`.
6. **Launch wrapper**: a `writeShellScriptBin "forscan"` that re-asserts the symlink on each launch (in case of a re-plug) and execs Wine directly at the installed `.exe`.

## Gotchas (as documented)

- Verify the serial link outside Wine first with `picocom -b 38400 /dev/ttyOBD` and an `ATI` command — if that fails, it's a permissions/driver issue, not a Wine issue.
- Cheap CH340 clones sometimes need `usb_modeswitch` or a specific baud rate; FTDI/CP210x adapters are the most trouble-free.
- Timing-sensitive operations (module programming, As-Built writes) are riskiest over Wine, especially over WiFi where latency is higher — do config *writes* over wired USB, reserve WiFi for reads/PID logging.
- If FORScan's COM dropdown is empty, check `HKLM\Software\Wine\Ports` in `wine regedit`, or re-verify the `dosdevices` symlink.

## Open Questions

- Has this actually been turned into real `configuration.nix`/`ThornixOS` module code yet, or does it still live only as freeform notes in `~/Downloads`? If the latter, this is a good candidate to fold into a `modules/apps/forscan.nix` (or similar) the same way `mcpelauncher.nix` already exists.
- Which vehicle(s) is this for, and which adapter (USB/WiFi/Bluetooth) is actually on hand?

## Related

- [[01 Maps/Hobbies Map|Hobbies Map]]
- [[02 Systems/NixOS - Repository Layout|NixOS - Repository Layout]]
