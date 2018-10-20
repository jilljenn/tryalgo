#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Range minimum query
# Minimum d'une plage --- range minimum query
# jill-jenn vie et christoph durr - 2014-2018


from __future__ import print_function


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
        while self.N < len(t):                     # find size N
            self.N *= 2
        self.s = [self.INF] * (2 * self.N)
        for i in range(len(t)):                    # put t at leaves
            self.s[self.N + i] = t[i]
        for p in range(self.N - 1, 0, -1):         # fill nodes
            self.s[p] = min(self.s[2 * p], self.s[2 * p + 1])

    def __getitem__(self, i):
        return self.s[self.N + i]

    def __setitem__(self, i, v):
        """ sets t[i] to v.
            :complexity: O(log len(t))
        """
        p = self.N + i
        self.s[p] = v
        p //= 2                                    # climb up the tree
        while p > 0:                               # update node
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
        if start + span <= i or k <= start:        # disjoint intervals
            return self.INF
        if i <= start and start + span <= k:       # included intervals
            return self.s[p]
        left = self._range_min(2*p,      start,             span // 2, i, k)
        right = self._range_min(2*p + 1, start + span // 2, span // 2, i, k)
        return min(left, right)
# snip}


class LazySegmentTree:
    """maintains a tree to allow quick updates and queries on a table.

    This is more general than a Fenwick tree or a tree for MinRangeQuery. Here
    queries and updates act on index ranges. Updates can be set a range to a
    value or add a value to a range. Queries can be max, min and sum over an
    index range. All operations run in time O(\log n) for a the table size n.
    The given ranges are in the form [i,j] where i is included and j excluded.
    In the recursive calls, node is the index of a node in the tree, and left,
    right its range. Values can be any numerical values allowing max, min, and
    sum, such as integers, floating point numbers or fractions (from the class
    Fraction). Updates over an empty range is valid and does nothing. Queries
    over an empty range is valid and returns the neutral value -inf, +inf or
    0.

    If the node is cleared, then maxval, minval, sumval represent for each
    node the query responses over the corresponding index ranges.  If the node
    is not clean, it means that lazyset and/or lazyadd contain suspendet
    update instructions for that node. Clearing a node means propagating these
    values to the descents in the subtrees, and updating maxval,minval and
    sumval for that node.
    """
    def __init__(self, tab):
        """stores an integer table tab.
        will be padded to get a table with a size of a power of 2.

        :param array tab: of positive length
        """
        self.N = 1
        while self.N < len(tab):
            self.N *= 2
        self.maxval = [float('-inf')] * 2 * self.N  # init with neutral values
        self.minval = [float('+inf')] * 2 * self.N
        self.sumval = [0] * 2 * self.N
        self.lazyset = [None] * 2 * self.N
        self.lazyadd = [0] * 2 * self.N
        for i, tabi in enumerate(tab):             # initialize with given table
            j = self.N + i
            self.maxval[j] = self.minval[j] = self.sumval[j] = tabi
        for node in range(self.N - 1, 0, -1):
            self._maintain(node)                    # maintain invariant

    def _maintain(self, node):
        """maintains the invariant for the given node
        :promize: the lazy values are None/0 for this node
        """
        # requires node and its direct descends to be clean
        l = 2 * node
        r = 2 * node + 1
        assert self.lazyset[node] is None
        assert self.lazyadd[node] == 0
        assert self.lazyset[l] is None
        assert self.lazyadd[l] == 0
        assert self.lazyset[r] is None
        assert self.lazyadd[r] == 0
        self.maxval[node] = max(self.maxval[l], self.maxval[r])
        self.minval[node] = min(self.minval[l], self.minval[r])
        self.sumval[node] = self.sumval[l] + self.sumval[r]

    def _clear(self, node, left, right):
        """propagates the lazy updates for this node to the subtrees.
        as a result the maxval, minval, sumval values for the node
        are up to date.
        """
        if self.lazyset[node] is not None:  # first do the pending set
            val = self.lazyset[node]
            self.minval[node] = val
            self.maxval[node] = val
            self.sumval[node] = val * (right - left)
            self.lazyset[node] = None
            if left < right - 1:            # not a leaf
                self.lazyset[2 * node] = val    # propagate to direct descendents
                self.lazyadd[2 * node] = 0
                self.lazyset[2 * node + 1] = val
                self.lazyadd[2 * node + 1] = 0
        if self.lazyadd[node] != 0:        # then do the pending add
            val = self.lazyadd[node]
            self.minval[node] += val
            self.maxval[node] += val
            self.sumval[node] += val * (right - left)
            self.lazyadd[node] = 0
            if left < right - 1:            # not at a leaf
                self.lazyadd[2 * node] += val     # propagate to direct descendents
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
        self._clear(node, left, right)
        if j <= left or right <= i:
            return   # disjoint intervals, nothing to do
        if i <= left and right <= j:
            self.lazyadd[node] += val
            self._clear(node, left, right)
        else:
            mid = (right + left) // 2
            self._add(i, j, val, 2 * node, left, mid)
            self._add(i, j, val, 2 * node + 1, mid, right)
            self._maintain(node)

    def _set(self, i, j, val, node, left, right):
        self._clear(node, left, right)
        if j <= left or right <= i:
            return   # disjoint intervals, nothing to do
        if i <= left and right <= j:
            self.lazyset[node] = val
            self.lazyadd[node] = 0
            self._clear(node, left, right)
        else:
            mid = (right + left) // 2
            self._set(i, j, val, 2 * node, left, mid)
            self._set(i, j, val, 2 * node + 1, mid, right)
            self._maintain(node)

    def _max(self, i, j, node, left, right):
        if j <= left or right <= i:
            return float('-inf')   # neutral value for max
        self._clear(node, left, right)
        if i <= left and right <= j:
            return self.maxval[node]
        else:
            mid = (right + left) // 2
            a = self._max(i, j, 2 * node, left, mid)
            b = self._max(i, j, 2 * node + 1, mid, right)
            return max(a, b)

    def _min(self, i, j, node, left, right):
        if j <= left or right <= i:
            return float('+inf')   # neutral value for min
        self._clear(node, left, right)
        if i <= left and right <= j:
            return self.minval[node]
        else:
            mid = (right + left) // 2
            a = self._min(i, j, 2 * node, left, mid)
            b = self._min(i, j, 2 * node + 1, mid, right)
            return min(a, b)

    def _sum(self, i, j, node, left, right):
        if j <= left or right <= i:
            return 0               # neutral value for sum
        self._clear(node, left, right)
        if i <= left and right <= j:
            return self.sumval[node]
        else:
            mid = (right + left) // 2
            a = self._sum(i, j, 2 * node, left, mid)
            b = self._sum(i, j, 2 * node + 1, mid, right)
            return a + b

    def _dump(self):
        f = open("tmp.dot", "w")
        print("digraph G{", file=f)
        print('0 [label="lazyset/lazyadd/maxval/minval/sumval"]', file=f)
        for node in range(1, 2 * self.N):
            s = '%i [label="%s/%i/%s/%s/%s"]' % \
                (node, self.lazyset[node], self.lazyadd[node],
                    self.maxval[node], self.minval[node], self.sumval[node])
            print(s.replace('inf', '∞'), file=f)
        for node in range(1, self.N):
            print("%i -> %i" % (node, 2 * node), file=f)
            print("%i -> %i" % (node, 2 * node + 1), file=f)
        print("}", file=f)
        f.close()


if __name__ == '__main__':
    # execute with: rlwrap python3 range_minimum_query.py
    import sys
    tree = LazySegmentTree([0]*8)
    print("open tmp.dot with graphviz")
    print("help: ")
    print("      2 7 ?      queries range[2, 7]")
    print("      2 7 + 4    adds 4 to range[2, 7]")
    print("      2 7 = 1    sets range[2, 7] to 1")
    while True:
        print(">", end='')
        sys.stdout.flush()
        t = sys.stdin.readline().split()
        i = int(t[0])
        j = int(t[1])
        if t[2] == '?':
            print("[%i,%i] max=%s min=%s sum=%s" % (i, j, tree.max(i,j), tree.min(i,j), tree.sum(i,j)))
        elif t[2] == '+':
            tree.add(i, j, int(t[3]))
        elif t[2] == '=':
            tree.set(i, j, int(t[3]))
        tree._dump()
