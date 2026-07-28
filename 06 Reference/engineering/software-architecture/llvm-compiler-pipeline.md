---
summary: "LLVM-based compilers typically lex, parse, build an AST, emit LLVM IR, optimize, JIT or lower to object code, and attach debug information."
status: active
tags: [reference, engineering, compilers, llvm, programming-languages]
private: false
---

# LLVM Compiler Pipeline

## Purpose

LLVM provides reusable compiler infrastructure for frontends, optimizers, code generators, and JIT runtimes. The Kaleidoscope tutorial is the canonical compact path through a toy LLVM language implementation.

## Core Pipeline

- Lex source text into tokens.
- Parse tokens into an AST.
- Perform semantic checks and symbol resolution.
- Generate LLVM IR.
- Run optimization passes.
- JIT execute through ORC or emit object code.
- Add debug information for source-level tooling.

## Engineering Notes

- Frontends own language syntax and semantics; LLVM IR is not a substitute for a real type checker.
- IR generation is easier when AST nodes have clear ownership and scoped symbol tables.
- Optimizations are safest when expressed as IR passes over well-defined invariants.
- JITs need explicit decisions around symbol lookup, lazy compilation, object lifetime, and target machine configuration.

## Sources

- LLVM Kaleidoscope tutorial index - https://llvm.org/docs/tutorial/index.html
- LLVM Kaleidoscope frontend introduction - https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html
- LLVM code generation to IR - https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl03.html
- LLVM ORC JIT tutorial - https://llvm.org/docs/tutorial/BuildingAJIT1.html

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
