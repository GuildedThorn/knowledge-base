---
summary: Ghidra — free SRE suite for disassembly/decompilation; workflow for triaging an unknown binary.
status: active
tags: [security, tools, ghidra, reverse-engineering]
private: false
---

# Ghidra

NSA's open-source software reverse-engineering suite. Free alternative to IDA — strong decompiler, good for static malware analysis and CTF binary/pwn.

## Project workflow

1. **New Project** → **Import File** (the binary) → let the **auto-analysis** run (accept defaults; enable *Decompiler Parameter ID*).
2. **Symbol Tree** → `Functions` → open `main` / `entry`. Dual-pane: disassembly (left) + **Decompiler** (right, C-like).
3. Rename variables/functions as you understand them (`L` on a symbol) — makes the decompiled output readable fast.

## Finding the interesting code

- **Search → For Strings** (or the Defined Strings window) → double-click a string → right-click **References → Show References to** → jumps to the code that uses it. Fastest route to the logic (passwords, URLs, format strings).
- **Symbol Tree → Imports** — flag dangerous APIs: `system`, `exec`, `WinExec`, `CreateRemoteThread`, `VirtualAlloc`, `socket`, `RegSetValue`.
- **Function Call Trees** — see callers/callees of a function.
- **Bookmarks** (`Ctrl-D`) to mark spots as you pivot.

## Decompiler tips

- Right-click a variable → **Retype** to fix wrong types → cleaner output.
- Undefined data → `D` to disassemble, `T` to set data type.
- Watch for XOR/loop deobfuscation routines (common in malware string decryption).

## For CTF / pwn

- Identify the vuln class in the decompiler (`gets`, `strcpy`, format string, integer overflow), read the stack layout, then build the exploit with **pwntools** and debug with **gdb + pwndbg**. Ghidra static-reads what gdb confirms dynamically.

## Related

- [Ghidra tool index](kb://11-security-tools-tools-index)
- [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow)
