
Directed Acyclic Graph $G=(V,E)$. Single token on some vertex. Move the token along a single out coming arc. Outdegree zero? You lost. Two players in alternation. Token on vertex $v in V$. Can the first player win? Grundy number of $v$ =0 means loosing, and >0 means winning. Definition: minimum excluded number $"mex"(S) = min NN minus S$.

#import "@preview/cetz:0.4.2": canvas, draw

#canvas({
  import draw: *

  set-style(
    stroke: 0.8pt,
    mark: (end: ">", scale: 0.7),
  )

  // Exists: at least one winning move
  content((2, 0), [$d="mex"({a,b,c})$])
  content((3.5, 0), [d])
  content((5, 0.5), [a])
  content((5, 0), [b])
  content((5, -0.5), [c])

  line((3.7, 0), (4.9, 0.5))
  line((3.7, 0), (4.9, 0))
  line((3.7, 0), (4.9, -0.5))
})

Variant play with $k$ tokens. Each turn choose a token and move it.

*Sprague-Grundy Theorem:* Grundy number of configuration $v_1,...,v_k$ := bitwise xor of the Grundy numbers from $v_1$ up to $v_k$.
