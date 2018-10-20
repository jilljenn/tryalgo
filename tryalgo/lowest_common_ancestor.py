#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lowest common ancestor
# jill-jenn vie et christoph durr - 2014-2018
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html

from tryalgo.range_minimum_query import RangeMinQuery


def log2floor(n):
    """ log of n in base 2 rounded down """
    k = -1
    assert n >= 0
    while n:
        k += 1
        n >>= 1
    return k


def log2ceil(n):
    """ log of n in base 2 rounded up """
    return log2floor(n - 1) + 1


# snip{ lowest_common_ancestor_by_shortcuts
class LowestCommonAncestorShortcuts:
    """Lowest common ancestor data structure using shortcuts to ancestors
    """
    def __init__(self, prec):
        """builds the structure from a given tree

        :param prec: father for every node, with prec[0] = 0
        :assumes: prec[node] < node
        :complexity: O(n log n), with n = len(nodes)
        """
        n = len(prec)
        self.level = [None] * n        # build levels
        self.level[0] = 0
        for u in range(1, n):
            self.level[u] = 1 + self.level[prec[u]]
        depth = log2ceil(max(self.level[u] for u in range(n))) + 1
        self.anc = [[0] * n for _ in range(depth)]
        for u in range(n):
            self.anc[0][u] = prec[u]
        for k in range(1, depth):
            for u in range(n):
                self.anc[k][u] = self.anc[k - 1][self.anc[k - 1][u]]

    def query(self, u, v):
        """:returns: the lowest common ancestor of u and v
        :complexity: O(log n)
        """
        # -- assume w.l.o.g. that v is not higher than u in the tree
        if self.level[u] > self.level[v]:
            u, v = v, u
        # -- put v at the same level as u
        depth = len(self.anc)
        for k in range(depth-1, -1, -1):
            if self.level[u] <= self.level[v] - (1 << k):
                v = self.anc[k][v]
        assert self.level[u] == self.level[v]
        if u == v:
            return u
        # -- climb until the lowest common ancestor
        for k in range(depth-1, -1, -1):
            if self.anc[k][u] != self.anc[k][v]:
                u = self.anc[k][u]
                v = self.anc[k][v]
        assert self.anc[0][u] == self.anc[0][v]
        return self.anc[0][u]
# snip}


# snip{ lowest_common_ancestor_by_rmq
class LowestCommonAncestorRMQ:
    """Lowest common ancestor data structure using a reduction to
       range minimum query
    """
    def __init__(self, graph):
        """builds the structure from a given tree

        :param graph: adjacency matrix of a tree
        :complexity: O(n log n), with n = len(graph)
        """
        n = len(graph)
        dfs_trace = []
        self.last = [None] * n
        to_visit = [(0, 0, None)]            # node 0 is root
        succ = [0] * n
        while to_visit:
            level, node, father = to_visit[-1]
            self.last[node] = len(dfs_trace)
            dfs_trace.append((level, node))
            if succ[node] < len(graph[node]) and \
               graph[node][succ[node]] == father:
                succ[node] += 1
            if succ[node] == len(graph[node]):
                to_visit.pop()
            else:
                neighbor = graph[node][succ[node]]
                succ[node] += 1
                to_visit.append((level + 1, neighbor, node))
        self.rmq = RangeMinQuery(dfs_trace, (float('inf'), None))

    def query(self, u, v):
        """:returns: the lowest common ancestor of u and v
        :complexity: O(log n)
        """
        lu = self.last[u]
        lv = self.last[v]
        if lu > lv:
            lu, lv = lv, lu
        return self.rmq.range_min(lu, lv + 1)[1]
# snip}
