#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Minimum spanning tree by kruskal
jill-jenn vie et christoph durr - 2014-2018
-------------------------------------------
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
def kruskal(kk_graph, kk_weight):
    """
    Minimum spanning tree by Kruskal
    :param kk_graph: undirected kk_graph in listlist or listdict format
    :param kk_weight: in matrix format or same listdict kk_graph
    :returns: list of edges of the tree
    :complexity: ``O(|E|log|E|)``
    """
    u_f = UnionFind(len(kk_graph))
    edges = []
    for u_idx, _ in enumerate(kk_graph):
        for v_idx in kk_graph[u_idx]:
            edges.append((kk_weight[u_idx][v_idx], u_idx, v_idx))
    edges.sort()
    min_span_tree = []
    for w_idx, u_idx, v_idx in edges:
        if u_f.union(u_idx, v_idx):
            min_span_tree.append((u_idx, v_idx))
    return min_span_tree
# snip}

def dist(a_point, b_point):
    """
    distance between point a and point b
    """
    return sqrt(sum([(a_point[i] - b_point[i]) * (a_point[i] - b_point[i])
                     for i in range(len(a_point))]))

def main():
    """
    main function
    """
    size = 256
    points = [[random.random() * 5, random.random() * 5] for _ in range(size)]
    weight = [[dist(points[i], points[j]) for j in range(size)]
              for i in range(size)]
    graph = [[j for j in range(size) if i != j] for i in range(size)]

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

if __name__ == "__main__":
    main()
