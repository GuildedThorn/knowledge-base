---
summary: "Loading a DLL entirely from memory using a self-contained loader that maps and relocates the image without LoadLibrary."
status: active
tags: [security, techniques, injection, in-memory, loader]
private: false
---

# Reflective DLL Injection

## Purpose

Loading a DLL entirely from memory using a self-contained loader that maps and relocates the image without LoadLibrary.

## How It Works

- The DLL exports a `ReflectiveLoader` function that performs the work normally done by the Windows loader on itself.
- The stub locates its own base in memory by walking backward to the PE header, then resolves `kernel32` exports (`LoadLibraryA`, `GetProcAddress`, `VirtualAlloc`) via the PEB.
- It allocates a fresh region, copies headers and each section to their correct relative virtual addresses, and processes the base relocation table.
- The import address table is populated by loading dependencies and resolving each thunk, then `DllMain` is invoked with `DLL_PROCESS_ATTACH`.
- Because the image is delivered as a raw buffer and mapped manually, `LoadLibrary` is never called and no path is registered.

## Engineering Notes

- Leaves no file on disk; the payload can be injected into a remote process via `WriteProcessMemory` + `CreateRemoteThread` pointing at the loader offset.
- The injected module is absent from the PEB `Ldr` module lists, so it evades tools that enumerate loaded modules.
- MITRE tracks the broader pattern as T1620 Reflective Code Loading, spanning native and managed (CLR) loaders.
- Detection focuses on unbacked executable memory, `CreateRemoteThread` into RWX regions, and memory scanning for PE signatures.

## Sources

- Stephen Fewer ReflectiveDLLInjection - https://github.com/stephenfewer/ReflectiveDLLInjection
- MITRE ATT&CK T1620 Reflective Code Loading - https://attack.mitre.org/techniques/T1620/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
