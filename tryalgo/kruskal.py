#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Minimum spanning tree by kruskal

jill-jenn vie et christoph durr - 2014-2018
"""

from math import sqrt
import random


# snip{ union-find
class UnionFind:
    """Maintains a partition of {0, ..., n-1}
    """
    def __init__(self, n):
        self.up_bound = list(range(n))
        self.rank = [0] * n

    def find(self, x_index):
        """
        :returns: identifier of part containing x_index
        :complex_indexity: O(inverse_ackerman(n))
        """
        if self.up_bound[x_index] == x_index:
            return x_index
        self.up_bound[x_index] = self.find(self.up_bound[x_index])
        return self.up_bound[x_index]

    def union(self, x_index, y_index):
        """
        Merges part that contain x and part containing y
        :returns: False if x_index, y_index are already in same part
        :complexity: O(inverse_ackerman(n))
        """
        repr_x = self.find(x_index)
        repr_y = self.find(y_index)
        if repr_x == repr_y:       # already in the same component
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up_bound[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up_bound[repr_y] = repr_x
        else:
            self.up_bound[repr_x] = repr_y
        return True
# snip}


# snip{ kruskal
# pylint: disable=redefined-outer-name, unused-variable
def kruskal(graph, weight):
    """Minimum spanning tree by Kruskal

    :param graph: undirected graph in listlist or listdict format
    :param weight: in matrix format or same listdict graph
    :returns: list of edges of the tree
    :complexity: ``O(|E|log|E|)``
    """
    u_f = UnionFind(len(graph))
    edges = []
    for u, _ in enumerate(graph):
        for v in graph[u]:
            edges.append((weight[u][v], u, v))
    edges.sort()
    min_span_tree = []
    for w_idx, u_idx, v_idx in edges:
        if u_f.union(u_idx, v_idx):
            min_span_tree.append((u_idx, v_idx))
    return min_span_tree
# snip}


def dist(a, b):
    """
    distance between point a and point b
    """
    return sqrt(sum([(a[i] - b[i]) * (a[i] - b[i])
                     for i in range(len(a))]))


# pylint: disable=pointless-string-statement
if __name__ == "__main__":
    """
    main function
    """
    N = 256
    points = [[random.random() * 5, random.random() * 5] for _ in range(N)]
    weight = [[dist(points[i], points[j]) for j in range(N)]
              for i in range(N)]
    graph = [[j for j in range(N) if i != j] for i in range(N)]

    with open('../data/kruskal-points.tex', 'w') as infile:
        min_span_tree = kruskal(graph, weight)
        val = 0
        for u_idx, v_idx in min_span_tree:
            val += weight[u_idx][v_idx]
            infile.write('\\draw[blue] (%f, %f) -- (%f, %f);\n'
                         % tuple(points[u_idx] + points[v_idx]))
        for point in points:
            infile.write('\\filldraw[black] (%f, %f) circle (1pt);\n'
                         % tuple(point))
        print(val)
