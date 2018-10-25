#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum flow by Dinic
# jill-jênn vie et christoph dürr - 2015-2018


from collections import deque
from sys import setrecursionlimit
from tryalgo.graph import add_reverse_arcs


setrecursionlimit(5010)  # necessary for big graphs


# snip{
def dinic(graph, capacity, source, target):
    """Maximum flow by Dinic

    :param graph: directed graph in listlist or listdict format
    :param capacity: in matrix format or same listdict graph
    :param int source: vertex
    :param int target: vertex
    :returns: skew symmetric flow matrix, flow value
    :complexity: :math:`O(|V|^2 |E|)`
    """
    assert source != target
    add_reverse_arcs(graph, capacity)
    Q = deque()
    total = 0
    n = len(graph)
    flow = [[0] * n for u in range(n)]   # flow initially empty
    while True:                   # repeat while we can increase
        Q.appendleft(source)
        lev = [None] * n          # build levels, None = inaccessible
        lev[source] = 0           # by BFS
        while Q:
            u = Q.pop()
            for v in graph[u]:
                if lev[v] is None and capacity[u][v] > flow[u][v]:
                    lev[v] = lev[u] + 1
                    Q.appendleft(v)

        if lev[target] is None:   # stop if sink is not reachable
            return flow, total
        up_bound = sum(capacity[source][v] for v in graph[source]) - total
        total += _dinic_step(graph, capacity, lev, flow, source, target,
                             up_bound)


def _dinic_step(graph, capacity, lev, flow, u, target, limit):
    """ tenter de pousser le plus de flot de u à target, sans dépasser limit
    """
    if limit <= 0:
        return 0
    if u == target:
        return limit
    val = 0
    for v in graph[u]:
        residual = capacity[u][v] - flow[u][v]
        if lev[v] == lev[u] + 1 and residual > 0:
            z = min(limit, residual)
            aug = _dinic_step(graph, capacity, lev, flow, v, target, z)
            flow[u][v] += aug
            flow[v][u] -= aug
            val += aug
            limit -= aug
    if val == 0:
        lev[u] = None         # remove unreachable node
    return val
# snip}
