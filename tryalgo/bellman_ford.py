#!/usr/bin/env python3
# Single source shortest paths by Bellman-Ford
# jill-jenn vie et christoph durr - 2014-2015



# snip{
def bellman_ford(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: adjacency list or adjacency dictionnary of a directed graph
    :param weight: matrix, might be negative
    :returns: distance table, precedence table, bool
    :explanation: bool is True if a negative circuit is
                  reachable from the source, circuits
                  can have length 2.
    :complexity: `O(|V|*|E|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0
    for nb_iterations in range(n+2):
        changed = False
        for node in range(n):
            for neighbor in graph[node]:
                alt = dist[node] + weight[node][neighbor]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prec[neighbor] = node
                    changed = True
        if not changed:                   # point fixe
            return dist, prec, False
    return dist, prec, True
# snip}

