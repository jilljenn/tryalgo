#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
All pairs shortest paths by Floyd-Warshall

jill-jênn vie, christoph dürr et pascal ortiz - 2014-2019
"""


# snip{
def floyd_warshall(weight):
    """All pairs shortest paths by Floyd-Warshall

    :param weight: edge weight matrix
    :modifies: weight matrix to contain distances in graph
    :returns: True if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    V = range(len(weight))
    for k in V:
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v],
                                   weight[u][k] + weight[k][v])
    for v in V:
        if weight[v][v] < 0:      # negative cycle found
            return True
    return False
# snip}


def floyd_warshall2(weight):
    """All pairs shortest paths by Floyd-Warshall.
    An improved implementation by Pascal-Ortiz

    :param weight: edge weight matrix
    :modifies: weight matrix to contain distances in graph
    :returns: True if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    for k, Wk in enumerate(weight):
        for _, Wu in enumerate(weight):
            for v, Wuv in enumerate(Wu):
                alt = Wu[k] + Wk[v]
                if alt < Wuv:
                    Wu[v] = alt
    for v, Wv in enumerate(weight):
        if Wv[v] < 0:      # negative cycle found
            return True
    return False
