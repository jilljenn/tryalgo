#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Minimum spanning tree by kruskal
# jill-jenn vie et christoph durr - 2014-2018

from math import sqrt
import random


# snip{ union-find
class UnionFind:
    """Maintains a partition of {0, ..., n-1}
    """
    def __init__(self, n):
        self.up = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """:returns: identifier of part containing x
        :complexity: O(inverse_ackerman(n))
        """
        if self.up[x] == x:
            return x
        else:
            self.up[x] = self.find(self.up[x])
            return self.up[x]

    def union(self, x, y):
        """Merges part that contain x and part containing y

        :returns: False if x, y are already in same part
        :complexity: O(inverse_ackerman(n))
        """
        repr_x = self.find(x)
        repr_y = self.find(y)
        if repr_x == repr_y:       # already in the same component
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up[repr_y] = repr_x
        else:
            self.up[repr_x] = repr_y
        return True
# snip}


# snip{ kruskal
def kruskal(graph, weight):
    """Minimum spanning tree by Kruskal

    :param graph: undirected graph in listlist or listdict format
    :param weight: in matrix format or same listdict graph
    :returns: list of edges of the tree
    :complexity: ``O(|E|log|E|)``
    """
    uf = UnionFind(len(graph))
    edges = []
    for u in range(len(graph)):
        for v in graph[u]:
            edges.append((weight[u][v], u, v))
    edges.sort()
    mst = []
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v))
    return mst
# snip}


if __name__ == "__main__":

    def dist(a, b):
        return sqrt(sum([(a[i] - b[i]) * (a[i] - b[i])
                         for i in range(len(a))]))

    N = 256
    points = [[random.random() * 5, random.random() * 5] for _ in range(N)]
    weight = [[dist(points[i], points[j]) for j in range(N)]
              for i in range(N)]
    graph = [[j for j in range(N) if i != j] for i in range(N)]

    with open('../data/kruskal-points.tex', 'w') as f:
        mst = kruskal(graph, weight)
        val = 0
        for u, v in mst:
            val += weight[u][v]
            f.write('\\draw[blue] (%f, %f) -- (%f, %f);\n'
                    % tuple(points[u] + points[v]))
        for point in points:
            f.write('\\filldraw[black] (%f, %f) circle (1pt);\n'
                    % tuple(point))
        print(val)
