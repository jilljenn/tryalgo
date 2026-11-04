#let title-page(team) = [

  #grid(
    columns: (1fr, 8fr),
    align: (left, right),
    image("figures/logo_B.png"),
    [#heading(level: 1, team)

      #datetime.today().display()],
  )

  ```python
  import sys
  from fractions import Fraction
  from itertools import permutations, product
  from collections import Counter, defaultdict
  from cmath import *     # x + y * 1j

  def readint(): return int(sys.stdin.readline())
  def readstr(): return sys.stdin.readline().strip()
  def readints(): return list(map(int, readstr().split()))

  print(f"{answer=}", file=sys.stderr)  # debug
  ```

  == check_hash.py


  #text(size: 8pt)[
    Use this script to check that you have copied the code snippets correctly. It ignores comments and differences in indentation width, and treats statements separated by semicolons the same as statements on separate lines. Docstrings were removed before calculating the hash codes shown in the upper-right corners, hence don't copy them.
  ]

  ```python
  import ast, hashlib, sys    
  with open(sys.argv[1], encoding="utf-8") as f:
      code = f.read()
  normalized = ast.unparse(ast.parse(code))  + "\n"
  hashcode = hashlib.md5(normalized.encode("utf-8")).hexdigest()
  print(hashcode[:6])
  ```

  === Some graph algorithms

  vertices $V$, edges/arcs $E$, maximal capacity $C$

  #table(
    columns: (auto, auto, auto, auto),
    [BFS], $O(V+E)$, [unweighted], [single source],
    [Dijkstra], $O(V+E log(V)$, [non-negative weight], [single source],
    [Bellman-Ford], $O(V E)$, [arbitrary weight], [single source],
    [Floyd-Warshal], $O(V^3)$, [arbitrary weight], [all source target pairs],
    [Gale-Shapley], $O(V^2)$, [stable matching], "",
    [Kuhn], $O(V E)$, [bipartite matching], [max cardinality],
    [Kunh-Munkres], $O(V^3)$, [bipartite matching], [max weight],
    [Ford-Fulkerson], $O(V E C )$, [flow], [constant capacities],
    [Edmonds-Karp], $O(V E^2)$, [max flow], [arbitrary capacities],
    [Dinic], $O(V^2 E)$, [max flow], [arbitrary capacities],
  )
]
