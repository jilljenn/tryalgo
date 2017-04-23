#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Range minimum query
# Minimum d'une plage --- range minimum query
# jill-jenn vie et christoph durr - 2014-2015


# snip{
class RangeMinQuery:
    """Range minimum query

    maintains a table t, can read/write items t[i],
    and query range_min(i,k) = min{ t[i], t[i + 1], ..., t[k - 1]}
    :complexity: all operations in O(log n), for n = len(t)
    """
    def __init__(self, t, INF=float('inf')):
        self.INF = INF
        self.N = 1
        while self.N < len(t):                     # trouver la taille N
            self.N *= 2
        self.s = [self.INF] * (2 * self.N)
        for i in range(len(t)):                    # poser t aux feuilles
            self.s[self.N + i] = t[i]
        for p in range(self.N - 1, 0, -1):         # remplir les noeuds
            self.s[p] = min(self.s[2 * p], self.s[2 * p + 1])

    def __getitem__(self, i):
        return self.s[self.N + i]

    def __setitem__(self, i, v):
        """ sets t[i] to v.
            :complexity: O(log len(t))
        """
        p = self.N + i
        self.s[p] = v
        p //= 2                                    # remonter dans l'arbre
        while p > 0:                               # mettre à jour le noeud
            self.s[p] = min(self.s[2 * p], self.s[2 * p + 1])
            p //= 2

    def range_min(self, i, k):
        """:returns:  min{ t[i], t[i + 1], ..., t[k - 1]}
        :complexity: O(log len(t))
        """
        return self._range_min(1, 0, self.N, i, k)

    def _range_min(self, p, start, span, i, k):
        """returns the minimum in t in the indexes [i, k) intersected
           with [start, start + span).
           p is the node associated to the later interval.
        """
        if start + span <= i or k <= start:        # intervalles disjoints
            return self.INF
        if i <= start and start + span <= k:       # intervalles inclus
            return self.s[p]
        left = self._range_min(2*p,      start,             span // 2, i, k)
        right = self._range_min(2*p + 1, start + span // 2, span // 2, i, k)
        return min(left, right)
# snip}


class LazySegmentTree:
    """maintains a tree to allow quick updates and queries on a table.
    This is more general than a Fenwick tree or a tree for MinRangeQuery.
    Here queries and updates act on ranges.
    Updates can be set and add.
    Queries can be max, min and sum.
    All operations run in time O(\log n) for a the table size n.
    The given ranges are in the form [i,j] where i is included and j excluded.
    In the recursive calls, node is the index of a node in the tree,
    and left, right its range.
    Values can be any numerical values allowing max, min, and sum,
    such as integers, floating point numbers or fractions (from the class Fraction).
    Updates over an empty range is valid and does nothing.
    Queryes over an empty range is valide and returns the neutral value -inf, +inf or 0.
    """
    def __init__(self, tab):
        """stores an integer table tab.
        will be padded to get a table with a size of a power of 2.

        :param array tab: of positive length
        """
        self.N = 1
        while self.N < len(tab):
            self.N *= 2
        self.maxval = [float('-inf')] * 2* self.N  # init with neutral values
        self.minval = [float('+inf')] * 2* self.N
        self.sumval = [0] * 2 * self.N
        self.lazyset = [None] * 2 * self.N
        self.lazyadd = [0] * 2 * self.N
        for i, tabi in enumerate(tab):             # initialize with given table
            j = self.N + i
            self.maxval[j] = self.minval[j] = self.sumval[j] = tabi
        for node in range(self.N - 1, 0, -1):
            self.maintain(node)                    # maintain invariant

    def maintain(self, node):
        """maintains the invariant for the given node
        :promize: the lazy values are None/0 for this node
        """
        assert self.lazyset[node] is None
        assert self.lazyadd[node] == 0
        l = 2 * node
        r = 2 * node + 1
        self.maxval[node] = max(self.maxval[l], self.maxval[r])
        self.minval[node] = min(self.minval[l], self.minval[r])
        self.sumval[node] = self.sumval[l] + self.sumval[r]

    def propagate(self, node, left, right):
        """propagates the lazy updates for this node to the subtrees.
        as a result the maxval, minval, sumval values for the node
        are up to date.
        """
        if self.lazyset[node] is None and self.lazyadd[node] == 0:
            return                   # nothing to do
        if self.lazyset[node] is not None:
            val = self.lazyset[node] + self.lazyadd[node]
            self.minval[node] = val
            self.maxval[node] = val
            self.sumval[node] = val * (right - left)
            self.lazyset[node] = None
            self.lazyadd[node] = 0
            if left < right - 1:            # not a leaf
                self.lazyset[2 * node] = val
                self.lazyadd[2 * node] = 0
                self.lazyset[2 * node + 1] = val
                self.lazyadd[2 * node + 1] = 0
        else:
            val = self.lazyadd[node]
            self.minval[node] += val
            self.maxval[node] += val
            self.sumval[node] += val * (right - left)
            self.lazyadd[node] = 0
            if left < right - 1:            # not at a leaf
                self.lazyadd[2 * node] += val
                self.lazyadd[2 * node + 1] += val

    def add(self, i, j, val):
        self._add(i, j, val, 1, 0, self.N)

    def set(self, i, j, val):
        self._set(i, j, val, 1, 0, self.N)

    def max(self, i, j):
        return self._max(i, j, 1, 0, self.N)

    def min(self, i, j):
        return self._min(i, j, 1, 0, self.N)

    def sum(self, i, j):
        return self._sum(i, j, 1, 0, self.N)


    def _add(self, i, j, val, node, left, right):
        if j <= left or right <= i:
            return   # intervals disjoint, nothing to do
        if i <= left and right <= j:
            self.lazyadd[node] += val
            self.propagate(node, left, right)
        else:
            self.propagate(node, left, right)
            mid = (right + left) // 2
            self._add(i, j, val, 2 * node, left, mid)
            self._add(i, j, val, 2 * node + 1, mid, right)
            self.maintain(node)

    def _set(self, i, j, val, node, left, right):
        if j <= left or right <= i:
            return   # intervals disjoint, nothing to do
        if i <= left and right <= j:
            self.lazyset[node] = val
            self.lazyadd[node] = 0
            self.propagate(node, left, right)
        else:
            mid = (right + left) // 2
            self._set(i, j, val, 2 * node, left, mid)
            self._set(i, j, val, 2 * node + 1, mid, right)
            self.maintain(node)

    def _max(self, i, j, node, left, right):
        self.propagate(node, left, right)
        if j <= left or right <= i:
            return float('-inf')   # neutral value for max
        if i <= left and right <= j:
            return self.maxval[node]
        else:
            mid = (right + left) // 2
            a = self._max(i, j, 2 * node, left, mid)
            b = self._max(i, j, 2 * node + 1, mid, right)
            return max(a, b)

    def _min(self, i, j, node, left, right):
        self.propagate(node, left, right)
        if j <= left or right <= i:
            return float('+inf')   # neutral value for min
        if i <= left and right <= j:
            return self.minval[node]
        else:
            mid = (right + left) // 2
            a = self._min(i, j, 2 * node, left, mid)
            b = self._min(i, j, 2 * node + 1, mid, right)
            return min(a, b)

    def _sum(self, i, j, node, left, right):
        self.propagate(node, left, right)
        if j <= left or right <= i:
            return 0               # neutral value for sum
        if i <= left and right <= j:
            return self.sumval[node]
        else:
            mid = (right + left) // 2
            a = self._sum(i, j, 2 * node, left, mid)
            b = self._sum(i, j, 2 * node + 1, mid, right)
            return a + b

    def dump(self):
        f = open("tmp.dot", "w")
        print("digraph G{", file=f)
        print('0 [label="lazyset/lazyadd/maxval/minval/sumval"]', file=f)
        for node in range(1, 2 * self.N):
            print('%i [label="%s/%i/%i/%i/%i"]' %
                (node, self.lazyset[node], self.lazyadd[node],
                    self.maxval[node], self.minval[node], self.sumval[node]), file=f)
        for node in range(1, self.N):
            print("%i -> %i" % (node, 2 * node), file=f)
            print("%i -> %i" % (node, 2 * node + 1), file=f)
        print("}", file=f)
        f.close()