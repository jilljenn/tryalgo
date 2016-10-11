#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum flow by Edmonds-Karp
# jill-jenn vie et christoph durr - 2015

from collections import deque
from tryalgo.graph import add_reverse_arcs


# snip{
def _augment(graph, capacity, flow, source, target):
    """find a shortest augmenting path
    """
    n = len(graph)
    A = [0] * n               # A[v]=cap.res.min sur chemin source-v
    augm_path = [None] * n    # None = sommet pas encore visité
    Q = deque()               # parcours BFS
    Q.append(source)
    augm_path[source] = source
    A[source] = float('inf')
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            cuv = capacity[u][v]
            residual = cuv - flow[u][v]
            if residual > 0 and augm_path[v] is None:
                augm_path[v] = u    # stocker prédécesseur
                A[v] = min(A[u], residual)
                if v == target:
                    break
                else:
                    Q.append(v)
    return (augm_path, A[target])   # chemin augmentant, cap. res. min


def edmonds_karp(graph, capacity, source, target):
    """Maxmum flow by Edmonds-Karp

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
        v = target                    # remonter vers la source
        while v != source:
            u = augm_path[v]          # et augmenter le flot
            flow[u][v] += delta
            flow[v][u] -= delta
            v = u
    return (flow, sum(flow[source]))  # flot, valeur du flot
# snip}

