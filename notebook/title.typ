
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
