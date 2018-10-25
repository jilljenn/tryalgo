#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Union of rectangles
# jill-jenn vie et christoph durr - 2014-2018


# snip{ cover-query
class Cover_query:
    """Segment tree to maintain a set of integer intervals
    and permitting to query the size of their union.
    """
    def __init__(self, L):
        """creates a structure, where all possible intervals
        will be included in [0, L - 1].
        """
        assert L != []              # L is assumed sorted
        self.N = 1
        while self.N < len(L):
            self.N *= 2
        self.c = [0] * (2 * self.N)         # --- covered
        self.s = [0] * (2 * self.N)         # --- score
        self.w = [0] * (2 * self.N)         # --- length
        for i in range(len(L)):
            self.w[self.N + i] = L[i]
        for p in range(self.N - 1, 0, -1):
            self.w[p] = self.w[2 * p] + self.w[2 * p + 1]

    def cover(self):
        """:returns: the size of the union of the stored intervals
        """
        return self.s[1]

    def change(self, i, k, delta):
        """when delta = +1, adds an interval [i, k], when delta = -1, removes it
        :complexity: O(log L)
        """
        self._change(1, 0, self.N, i, k, delta)

    def _change(self, p, start, span, i, k, delta):
        if start + span <= i or k <= start:   # --- disjoint
            return
        if i <= start and start + span <= k:  # --- included
            self.c[p] += delta
        else:
            self._change(2 * p, start, span // 2, i, k, delta)
            self._change(2 * p + 1, start + span // 2, span // 2,
                         i, k, delta)
        if self.c[p] == 0:
            if p >= self.N:                   # --- leaf
                self.s[p] = 0
            else:
                self.s[p] = self.s[2 * p] + self.s[2 * p + 1]
        else:
            self.s[p] = self.w[p]
# snip}


# snip{ union_rectangles
def union_rectangles(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^2)`
    """
    if R == []:
        return 0
    X = []
    Y = []
    for j in range(len(R)):
        (x1, y1, x2, y2) = R[j]
        assert x1 <= x2 and y1 <= y2
        X.append(x1)
        X.append(x2)
        Y.append((y1, +1, j))    # generate events
        Y.append((y2, -1, j))
    X.sort()
    Y.sort()
    X2i = {X[i]: i for i in range(len(X))}
    L = [X[i + 1] - X[i] for i in range(len(X) - 1)]
    C = Cover_query(L)
    area = 0
    last = 0
    for (y, delta, j) in Y:
        area += (y - last) * C.cover()
        last = y
        (x1, y1, x2, y2) = R[j]
        i = X2i[x1]
        k = X2i[x2]
        C.change(i, k, delta)
    return area
# snip}
