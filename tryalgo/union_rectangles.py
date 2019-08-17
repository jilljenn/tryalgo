#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Union of rectangles
jill-jenn vie et christoph durr - 2014-2018
"""
# pylint: disable=too-many-arguments, too-many-locals


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
        for i, _ in enumerate(L):
            self.w[self.N + i] = L[i]
        for p in range(self.N - 1, 0, -1):
            self.w[p] = self.w[2 * p] + self.w[2 * p + 1]

    def cover(self):
        """:returns: the size of the union of the stored intervals
        """
        return self.s[1]

    def change(self, i, k, delta):
        """when delta = +1, adds an interval [i, k],
        when delta = -1, removes it
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


def union_intervals(intervals):
    intervals.sort()
    furthest_x2 = float('-inf')
    length = 0
    for x1, x2 in intervals:
        if x2 <= furthest_x2:
            continue  # Ignore the interval
        elif x1 > furthest_x2:
            length += x2 - x1
        else:
            length += x2 - furthest_x2
        furthest_x2 = x2
    return length


# snip{ union_rectangles
def union_rectangles(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^2 \\log n)`
    """
    events = []
    for x1, y1, x2, y2 in R:
        events.append((y1, 1, x1, x2))  # 1 means opening
        events.append((y2, 0, x1, x2))  # 0 means closing, higher priority
    events.sort()
    previous_y = None
    current_intervals = {}
    area = 0
    for y, op, x1, x2 in events:
        if previous_y is not None and y > previous_y:
            area += (y - previous_y) * union_intervals(list(current_intervals))
        if op == 1:
            current_intervals[x1, x2] = 1
        else:
            del current_intervals[x1, x2]
        previous_y = y
    return area
# snip}


# snip{ union_rectangles_fast
def union_rectangles_fast(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^2)`
    """
    X = set()
    events = []
    for x1, y1, x2, y2 in R:
        assert x1 <= x2 and y1 <= y2
        X.add(x1)
        X.add(x2)
        events.append((y1, 1, x1, x2))  # 1 means opening
        events.append((y2, 0, x1, x2))  # 0 means closing, higher priority
    X = list(X)
    X.sort()
    X2i = {X[i]: i for i in range(len(X))}
    nb_current_rectangles = [0] * (len(X) - 1)
    events.sort()
    previous_y = None
    area = 0
    for y, op, x1, x2 in events:
        length = 0
        for i, nb in enumerate(nb_current_rectangles):
            if nb > 0:
                length += X[i + 1] - X[i]
        if previous_y is not None and y > previous_y:
            area += (y - previous_y) * length
        i = X2i[x1]
        k = X2i[x2]
        if op == 1:
            for j in range(i, k):
                nb_current_rectangles[j] += 1
        else:
            for j in range(i, k):
                nb_current_rectangles[j] -= 1
        previous_y = y
    return area
# snip}


# snip{ union_rectangles_fastest
def union_rectangles_fastest(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n \\log n)`
    """
    if R == []:
        return 0
    X = []
    Y = []
    for j, _ in enumerate(R):
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


def intersect(r1, r2):
    x1a, y1a, x2a, y2a = r1
    x1b, y1b, x2b, y2b = r2
    return not (x2a <= x1b or x2b <= x1a or y2a <= y1b or y2b <= y1a)


# snip{ union_rectangles_naive
def union_rectangles_naive(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^3)`
    """
    X = set()
    Y = set()
    for x1, y1, x2, y2 in R:
        assert x1 <= x2 and y1 <= y2
        X.add(x1)
        X.add(x2)
        Y.add(y1)
        Y.add(y2)
    X = list(X)
    Y = list(Y)
    X.sort()
    Y.sort()
    area = 0
    for i in range(len(Y) - 1):
        for j in range(len(X) - 1):
            if any(intersect(r, (X[j], Y[i], X[j + 1], Y[i + 1])) for r in R):
                area += (Y[i + 1] - Y[i]) * (X[j + 1] - X[j])
    return area
# snip}
