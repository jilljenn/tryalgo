#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum flow by Edmonds-Karp
# jill-jenn vie et christoph durr - 2015-2018

from collections import deque
from tryalgo.graph import add_reverse_arcs


# snip{
def _augment(graph, capacity, flow, source, target):
    """find a shortest augmenting path
    """
    n = len(graph)
    A = [0] * n               # A[v] = min residual cap. on path source->v
    augm_path = [None] * n    # None = node was not visited yet
    Q = deque()               # BFS
    Q.append(source)
    augm_path[source] = source
    A[source] = float('inf')
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            cuv = capacity[u][v]
            residual = cuv - flow[u][v]
            if residual > 0 and augm_path[v] is None:
                augm_path[v] = u    # store predecessor
                A[v] = min(A[u], residual)
                if v == target:
                    break
                else:
                    Q.append(v)
    return (augm_path, A[target])   # augmenting path, min residual cap.


def edmonds_karp(graph, capacity, source, target):
    """Maximum flow by Edmonds-Karp

    :param graph: directed graph in listlist or listdict format
    :param capacity: in matrix format or same listdict graph
    :param int source: vertex
    :param int target: vertex
    :returns: flow matrix, flow value
    :complexity: :math:`O(|V|*|E|^2)`
    """
    add_reverse_arcs(graph, capacity)
    V = range(len(graph))
    flow = [[0 for v in V] for u in V]
    while True:
        augm_path, delta = _augment(graph, capacity, flow, source, target)
        if delta == 0:
            break
        v = target                    # go back to source
        while v != source:
            u = augm_path[v]          # augment flow
            flow[u][v] += delta
            flow[v][u] -= delta
            v = u
    return (flow, sum(flow[source]))  # flow network, amount of flow
# snip}
