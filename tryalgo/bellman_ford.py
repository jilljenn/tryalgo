#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Single source shortest paths by Bellman-Ford

jill-jenn vie et christoph durr - 2014-2018
"""

# icpc-ignore
# snip{
# pylint: disable=unused-variable
def bellman_ford(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in listlist or listdict format
    :param weight: can be negative.
                   in matrix format or same listdict graph
    :returns: distance table, precedence table, bool,
                None means no predecessor
    :explanation: bool is True if a negative circuit is
                  reachable from the source, circuits
                  can have length 2.
    :complexity: `O(|V|*|E|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0
    for nb_iterations in range(n):
        changed = False
        for node in range(n):
            for neighbor in graph[node]:
                alt = dist[node] + weight[node][neighbor]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prec[neighbor] = node
                    changed = True
        if not changed:                   # fixed point
            return dist, prec, False
    return dist, prec, True
# snip}


# snip{
def bellman_ford_neg_cycles(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in list[list[int]] format
    :param weight: matrix. can be negative. 
    :returns: distance table, precedence table,
        vertices not reachable have distance inf and predecessor None
        negative cycles reachable from source have have distance -inf
    :complexity: `O(|V|*|E|)`
    """        for node in range(n):

    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0
    for i in range(2 * n):
        for node in range(n):
            for neighbor in graph[node]:
                alt = dist[node] + weight[node][neighbor]
                if alt < dist[neighbor]:
                    if i == n - 1:
                        dist[neighbor] = float('-inf')
                    else:
                        dist[neighbor] = alt
                    prec[neighbor] = node
    return dist, prec
# snip}

#snip{
def bellman_ford_edges(edges, n, s=0):
    """ Single source shortest paths by Bellman-Ford
    does not detect negative cycles

    :param edge: list of arcs (u,v) with their weight
    :param n: vertices are numbered from 0 to n - 1
    :returns: list d where d[u][0] is distance from s 
              and d[u][1] is the predecessor on shortest path, 
              -1 means no predecessor
    :complexity: `O(|V|*|E|)`
    """
    d = [(float('inf'), -1)] * n
    d[s] = (0, -1)
    for _ in range(n):
        for u, v, w in edges:
            d[v] = min(d[v], (d[u][0] + w, u))
    return d
# snip}
