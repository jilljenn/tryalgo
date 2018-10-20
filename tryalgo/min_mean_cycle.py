#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Minimum mean cycle by Karp
# jill-jenn vie et christoph durr - 2014-2018


# snip{
def min_mean_cycle(graph, weight, start=0):
    """Minimum mean cycle by Karp

    :param graph: directed graph in listlist or listdict format
    :param weight: in matrix format or same listdict graph
    :param int start: vertex that should be contained in cycle
    :returns: cycle as vertex list, average arc weights
              or None if there is no cycle from start
    :complexity:  `O(|V|*|E|)`
    """
    INF = float('inf')
    n = len(graph)                  # compute distances
    dist = [[INF] * n]
    prec = [[None] * n]
    dist[0][start] = 0
    for ell in range(1, n + 1):
        dist.append([INF] * n)
        prec.append([None] * n)
        for node in range(n):
            for neighbor in graph[node]:
                alt = dist[ell - 1][node] + weight[node][neighbor]
                if alt < dist[ell][neighbor]:
                    dist[ell][neighbor] = alt
                    prec[ell][neighbor] = node
    #                               -- find the optimal value
    valmin = INF
    argmin = None
    for node in range(n):
        valmax = -INF
        argmax = None
        for k in range(n):
            alt = (dist[n][node] - dist[k][node]) / float(n - k)
            # do not divide by float(n-k) => cycle of minimal total weight
            if alt >= valmax:     # with >= we get simple cycles
                valmax = alt
                argmax = k
        if argmax is not None and valmax < valmin:
            valmin = valmax
            argmin = (node, argmax)
    #                               -- extract cycle
    if valmin == INF:             # -- there is no cycle
        return None
    C = []
    node, k = argmin
    for l in range(n, k, -1):
        C.append(node)
        node = prec[l][node]
    return C[::-1], valmin
# snip}
