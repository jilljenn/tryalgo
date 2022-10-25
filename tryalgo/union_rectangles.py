#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Union of rectangles

jill-jênn vie et christoph dürr - 2014-2019
"""
# pylint: disable=too-many-arguments, too-many-locals


# snip{ union_intervals
from collections import Counter
# snip}


# weighted variant of tryalgo.range_minimum_query.LazySegmentTree
# snip{ cover-query
class CoverQuery:
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

    def change(self, i, k, offset):
        """when offset = +1, adds an interval [i, k],
        when offset = -1, removes it
        :complexity: O(log L)
        """
        self._change(1, 0, self.N, i, k, offset)

    def _change(self, p, start, span, i, k, offset):
        if start + span <= i or k <= start:   # --- disjoint
            return
        if i <= start and start + span <= k:  # --- included
            self.c[p] += offset
        else:
            self._change(2 * p, start, span // 2, i, k, offset)
            self._change(2 * p + 1, start + span // 2, span // 2,
                         i, k, offset)
        if self.c[p] == 0:
            if p >= self.N:                   # --- leaf
                self.s[p] = 0
            else:
                self.s[p] = self.s[2 * p] + self.s[2 * p + 1]
        else:
            self.s[p] = self.w[p]
# snip}


# snip{ union_intervals
OPENING = +1  # constants for events
CLOSING = -1  # -1 has higher priority


def union_intervals(intervals):
    """Size of the union of a set of intervals

    Sweep from left to right.
    Maintain in a counter number of opened intervals
    minus number of closed intervals.

    :param intervals: Counter, which describes a multiset of intervals.
        an interval is a pair of values.
    :returns: size of the union of those intervals
    :complexity: :math:`O(n \\log n)`
    """
    union_size = 0
    events = []
    for x1, x2 in intervals:
        for _ in range(intervals[x1, x2]):
            assert x1 <= x2
            events.append((x1, OPENING))
            events.append((x2, CLOSING))
    previous_x = 0    # arbitrary initial value
    #                   ok, because opened == 0 at first event
    opened = 0
    for x, offset in sorted(events):
        if opened > 0:
            union_size += x - previous_x
        previous_x = x
        opened += offset
    return union_size
# snip}


# snip{ union_rectangles
def union_rectangles(R):
    """Area of union of rectangles.

    Sweep from top to bottom.
    Maintain in a set the horizontal projection of rectangles,
    for which the top border has been processed but not yet the bottom.

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^2 \\log n)`
    """
    events = []
    for x1, y1, x2, y2 in R:                     # initialize events
        assert x1 <= x2 and y1 <= y2
        events.append((y1, OPENING, x1, x2))
        events.append((y2, CLOSING, x1, x2))
    current_intervals = Counter()
    area = 0
    previous_y = 0  # arbitrary initial value,
    #                 ok, because union_intervals is 0 at first event
    for y, offset, x1, x2 in sorted(events):         # sweep top down
        area += (y - previous_y) * union_intervals(current_intervals)
        previous_y = y
        current_intervals[x1, x2] += offset
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
    X = set()                 # set of all x coordinates in the input
    events = []               # events for the sweep line
    for x1, y1, x2, y2 in R:
        assert x1 <= x2 and y1 <= y2
        X.add(x1)
        X.add(x2)
        events.append((y1, OPENING, x1, x2))
        events.append((y2, CLOSING, x1, x2))
    # array of x coordinates in left to right order
    i_to_x = list(sorted(X))
    # inverse dictionary maps x coordinate to its rank
    x_to_i = {xi: i for i, xi in enumerate(i_to_x)}
    # nb_current_rectangles[i] = number of rectangles intersected
    # by the sweepline in interval [i_to_x[i], i_to_x[i + 1]]
    nb_current_rectangles = [0] * (len(i_to_x) - 1)
    area = 0
    length_union_intervals = 0
    previous_y = 0  # arbitrary initial value,
    #                 because length is 0 at first iteration
    for y, offset, x1, x2 in sorted(events):
        area += (y - previous_y) * length_union_intervals
        i1 = x_to_i[x1]
        i2 = x_to_i[x2]         # update nb_current_rectangles
        for j in range(i1, i2):
            length_interval = i_to_x[j + 1] - i_to_x[j]
            if nb_current_rectangles[j] == 0:
                length_union_intervals += length_interval
            nb_current_rectangles[j] += offset
            if nb_current_rectangles[j] == 0:
                length_union_intervals -= length_interval
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
    if R == []:               # segment tree would fail on an empty list
        return 0
    X = set()                 # set of all x coordinates in the input
    events = []               # events for the sweep line
    for Rj in R:
        (x1, y1, x2, y2) = Rj
        assert x1 <= x2 and y1 <= y2
        X.add(x1)
        X.add(x2)
        events.append((y1, OPENING, x1, x2))
        events.append((y2, CLOSING, x1, x2))
    i_to_x = list(sorted(X))
    # inverse dictionary
    x_to_i = {i_to_x[i]: i for i in range(len(i_to_x))}
    L = [i_to_x[i + 1] - i_to_x[i] for i in range(len(i_to_x) - 1)]
    C = CoverQuery(L)
    area = 0
    previous_y = 0  # arbitrary initial value,
    #                 because C.cover() is 0 at first iteration
    for y, offset, x1, x2 in sorted(events):
        area += (y - previous_y) * C.cover()
        i1 = x_to_i[x1]
        i2 = x_to_i[x2]
        C.change(i1, i2, offset)
        previous_y = y
    return area
# snip}


# snip{ union_rectangles_naive
def rectangles_contains_point(R, x, y):
    """Decides if at least one of the given rectangles contains a given point
    either strictly or on its left or top border
    """
    for x1, y1, x2, y2 in R:
        if x1 <= x < x2 and y1 <= y < y2:
            return True
    return False


def union_rectangles_naive(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^3)`
    """
    X = set()        # set of all x coordinates in the input
    Y = set()        # same for y
    for x1, y1, x2, y2 in R:
        assert x1 <= x2 and y1 <= y2
        X.add(x1)
        X.add(x2)
        Y.add(y1)
        Y.add(y2)
    j_to_x = list(sorted(X))
    i_to_y = list(sorted(Y))
    # X and Y partition space into a grid
    area = 0
    for j in range(len(j_to_x) - 1):      # loop over columns in grid
        x1 = j_to_x[j]
        x2 = j_to_x[j + 1]
        for i in range(len(i_to_y) - 1):  # loop over rows
            y1 = i_to_y[i]                # (x1,...,y2) is the grid cell
            y2 = i_to_y[i + 1]
            if rectangles_contains_point(R, x1, y1):
                area += (y2 - y1) * (x2 - x1)  # cell is covered
    return area
# snip}
