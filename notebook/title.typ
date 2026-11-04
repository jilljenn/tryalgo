
#grid(
  columns: (1fr, 8fr),
  align: (left, right),
  image("figures/logo_B.png"),
  [= University -- Team

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

```python
import ast, hashlib, sys    # les commentaires sont ignorés pour le code de hashage
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
  // column-gutter: 7pt,
  // row-gutter: 7pt,
  [BFS], $O(V+E)$, [unweighted], [single source],
  [Dijkstra], $O(V+E log(V)$, [non-negative weight], [single source],
  [Bellman-Ford], $O(V E)$, [arbitrary weight], [single source],
  [Floyd-Warshal], $O(V^3)$, [arbitrary weight], [all source target pairs],
  [Gale-Shapley], $O(V^2)$, [stable matching], "",
  [Kuhn], $O(V E)$, [bipartite matching], [max cardinality],
  [Kunh-Munkres], $O(V^3)$, [bipartite matching], [max weight],
  [Ford-Fulkerson], $O(V E C)$, [flow], [constant capacities],
  [Edmonds-Karp], $O(V E^2)$, [max flow], [arbitrary capacities],
  [Dinic], $O(V^2 E)$, [max flow], [arbitrary capacities],
)
