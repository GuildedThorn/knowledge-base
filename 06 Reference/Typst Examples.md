---
summary: Worked Typst examples and version gotchas — a self-contained showcase plus the built-in features it exercises.
status: active
tags: [reference]
---

## Purpose

Keep reusable Typst examples: a single self-contained document that
exercises most of Typst's built-in typesetting, and the version-specific
gotchas worth remembering. Verified against Typst 0.15.1. The source also
lives at `~/Documents/typst-showcase.typ` and renders in VR Brain's
Documents surface (see [[04 Software/Typst|Typst]]).

## Full showcase

Uses built-in features only — no `@preview` packages — so it compiles in a
sandbox with no network. Renders to three A4 pages themed in Catppuccin
Mocha.

````typst
// ============================================================
//  VR BRAIN — Typst capability showcase
//  Built-in features only; no network packages required.
// ============================================================

#let bg      = rgb("#1e1e2e")
#let surface = rgb("#313244")
#let text-c  = rgb("#cdd6f4")
#let subtle  = rgb("#a6adc8")
#let mauve   = rgb("#cba6f7")
#let blue    = rgb("#89b4fa")
#let green   = rgb("#a6e3a1")
#let peach   = rgb("#fab387")
#let red     = rgb("#f38ba8")

#set document(title: "Typst Capability Showcase", author: "VR Brain")
#set page(
  paper: "a4",
  margin: (x: 2.2cm, top: 2.4cm, bottom: 2.2cm),
  fill: bg,
  header: context {
    set text(size: 8pt, fill: subtle)
    grid(columns: (1fr, 1fr),
      align: (left, right),
      [VR BRAIN · Typst showcase],
      [Capability tour])
    line(length: 100%, stroke: 0.5pt + surface)
  },
  footer: context {
    set text(size: 8pt, fill: subtle)
    line(length: 100%, stroke: 0.5pt + surface)
    grid(columns: (1fr, 1fr), align: (left, right),
      [Rendered in-world],
      [#counter(page).display("1 / 1", both: true)])
  },
)
#set text(size: 10.5pt, fill: text-c, lang: "en")
#set par(justify: true, leading: 0.62em)

// --- heading styles ----------------------------------------
#set heading(numbering: "1.1")
#show heading.where(level: 1): it => block(above: 1.4em, below: 0.8em)[
  #set text(size: 17pt, fill: mauve, weight: "bold")
  #it
]
#show heading.where(level: 2): it => block(above: 1.1em, below: 0.6em)[
  #set text(size: 12.5pt, fill: blue, weight: "bold")
  #it
]
#show link: set text(fill: blue)
#show raw: set text(font: "DejaVu Sans Mono", fill: green, size: 9pt)

// --- a reusable callout function ---------------------------
#let callout(title, body, accent: peach) = block(
  width: 100%, inset: 10pt, radius: 5pt,
  fill: surface, stroke: (left: 3pt + accent),
)[
  #text(fill: accent, weight: "bold")[#title] \
  #body
]

// ============================================================
//  COVER
// ============================================================
#align(center + horizon)[
  #rect(width: 100%, height: 3.4cm, radius: 8pt,
    fill: gradient.linear(rgb("#89b4fa"), rgb("#cba6f7"),
      rgb("#f38ba8"), angle: 35deg))[
    #align(center + horizon)[
      #text(size: 26pt, weight: "bold", fill: rgb("#11111b"))[
        Typst, Fully Loaded
      ]
    ]
  ]
  #v(0.6em)
  #text(size: 12pt, fill: subtle)[
    A one-file tour of typesetting, math, tables, figures, and code
  ]
]

#v(1.2em)
#outline(title: text(fill: mauve)[Contents], indent: 1.2em)
#pagebreak()

// ============================================================
= Typography and structure

Typst sets prose with real microtypography: justified paragraphs,
ligatures, and proper hyphenation across languages. Emphasis comes in
*bold*, _italic_, and `monospace`, with super#super[script] and
sub#sub[script], plus footnotes#footnote[Footnotes collect at the
bottom of the page automatically.] that number themselves.

/ Term list: definitions render with a hanging indent.
/ Grid: the layout primitive behind tables, figures, and columns.
/ Context: lets content read page state — used by the running header.

#callout("Design note")[
  Every colour here is a named Catppuccin Mocha value defined once at the
  top, so the whole document re-themes from six lines.
]

== Multi-column flow

#columns(2, gutter: 1.2em)[
  Body text balances across columns on its own. Typst reflows content to
  fill each column evenly, so notes, references, and dense prose stay
  compact without manual breaks.

  #colbreak()

  Lists survive the split too:
  + first, numbered automatically
  + second, with nesting
    + a nested item
  - and unordered bullets
  - as needed
]

// ============================================================
= Mathematics

Inline math like $e^(i pi) + 1 = 0$ sits naturally in a sentence. Block
equations are numbered and can align on a relation:

#set math.equation(numbering: "(1)")
$ nabla times bold(E) &= - (partial bold(B)) / (partial t) \
  integral_(partial Omega) bold(F) dot dif bold(S)
    &= integral_Omega (nabla dot bold(F)) dif V $

Matrices, cases, and big operators all compose:

$ bold(A) = mat(1, 2, 3; 4, 5, 6; 7, 8, 9), quad
  f(x) = cases(x^2 &"if " x >= 0, -x &"otherwise") $

$ sum_(k=1)^n k = (n(n+1)) / 2, quad
  lim_(x -> 0) sin(x) / x = 1 $

// ============================================================
= Tables and data

#figure(
  caption: [Adaptive quality ladder, by frame-time budget.],
  table(
    columns: (auto, 1fr, auto),
    align: (left, left, right),
    stroke: 0.5pt + surface,
    fill: (x, y) => if y == 0 { surface } else if calc.odd(y) { rgb("#242438") },
    table.header(
      text(fill: mauve, weight: "bold")[Stage],
      text(fill: mauve, weight: "bold")[Action],
      text(fill: mauve, weight: "bold")[Budget],
    ),
    [1], [Thin volumetric fog], [16.6 ms],
    [2], [Cut fill-rate effects], [20.0 ms],
    [3], [Drop shadows and MSAA], [25.0 ms],
    [4], [Survival mode], [33.3 ms],
  ),
) <ladder>

@ladder shows the fallback order. Cross-references, like the link
to #link("https://typst.app")[typst.app], resolve automatically.

// ============================================================
= Figures and vector graphics

Shapes, gradients, and paths are first-class — no external image needed.

#grid(columns: (1fr, 1fr, 1fr), gutter: 1em,
  figure(caption: [Gradient disc],
    circle(radius: 1.4cm,
      fill: gradient.radial(green, blue, rgb("#181825")))),
  figure(caption: [Polygon],
    polygon.regular(vertices: 6, size: 2.6cm,
      fill: peach.transparentize(20%), stroke: 1pt + peach)),
  figure(caption: [Polyline],
    polygon(stroke: 2pt + red,
      (0pt, 0pt), (16pt, 46pt), (32pt, 8pt),
      (48pt, 46pt), (64pt, 0pt))),
)

// ============================================================
= Code

Raw blocks keep syntax highlighting for dozens of languages:

```rust
fn orbit(bodies: &mut [Body], dt: f32) {
    for b in bodies.iter_mut() {
        b.phase += b.speed * dt;      // advance along the orbit
        b.pos = b.parent + offset(b); // children ride their parent
    }
}
```

```python
def markdown_to_typst(md: str) -> str:
    return "\n".join(convert(line) for line in md.splitlines())
```

#callout("That's the tour", accent: green)[
  Headings, math, tables, figures, vector art, multi-column flow, and
  highlighted code — all from a single self-contained source file with no
  external assets or network packages.
]
````

## What it demonstrates

- Themed pages from named colour variables; running header/footer with a
  page counter via `context` + `counter(page)`.
- Custom heading styles with `show heading.where(level: ..)`.
- Auto table of contents (`#outline`), footnotes, term lists.
- A reusable component as a `#let` function (the callout box).
- Two-column balanced flow (`#columns`, `#colbreak`).
- Inline and numbered display math: aligned equations, `mat`, `cases`,
  sums and limits.
- Styled tables with header fill and zebra striping; a labelled `#figure`
  with a `@label` cross-reference.
- Vector graphics with no image files: `circle`, `polygon.regular`,
  `polygon`, and `gradient.linear` / `gradient.radial`.
- Syntax-highlighted raw code blocks.

## Gotchas (Typst 0.15)

- Partial derivative is `partial` (∂); `diff` is **not** a symbol. The
  differential d is `dif`.
- `path` was replaced by `curve`; for straight segments a `polygon` with
  positional points also works.
- `@preview` packages require network access to fetch. In a sandboxed
  compile (VR Brain roots the project and blocks the package server),
  stick to built-ins.
- On a dark `page(fill: ..)` you must set a light `text(fill: ..)` or the
  default black text is invisible.

## Compile

```bash
# One PDF
typst compile showcase.typ showcase.pdf

# One PNG per page (zero-padded), at a chosen resolution
typst compile --format png --ppi 144 showcase.typ "page-{0p}.png"

# Live-reload preview while editing
typst watch showcase.typ
```

## Related

- [[04 Software/Typst|Typst]]
- [[01 Maps/Reference Map|Reference Map]]
- [[06 Reference/Godot UI Architecture and Control Nodes|Godot UI Architecture and Control Nodes]]
