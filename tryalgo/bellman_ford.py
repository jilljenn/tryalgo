#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Single source shortest paths by Bellman-Ford

jill-jenn vie et christoph durr - 2014-2018
"""


# snip{
# pylint: disable=unused-variable
def bellman_ford(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in listlist or listdict format
    :param weight: can be negative.
                   in matrix format or same listdict graph
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


def bellman_ford2(graph, weight, source):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in listlist or listdict format
    :param weight: can be negative.
                   in matrix format or same listdict graph
    :returns: distance table, precedence table, bool
    :explanation: bool is true if there is a negative cycle 
                  reachable from the source.
                  distance[v] is +inf if vertex v is not reachable 
                  from source and -inf if there are paths from the 
                  source to v of arbitrary small weight.
    :complexity: `O(|V|*|E|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0

    def relax():
        for nb_iterations in  range(n-1):
            for node in range(n):
                for neighbor in graph[node]:
                    alt = dist[node] + weight[node][neighbor]
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prec[neighbor] = node

    relax()
    intermediate = dist[:]  # is fixpoint in absence of neg cycles
    relax()
    for node in range(n):
        if dist[node] < intermediate[node]:
            dist[node] = float('-inf')
    return dist, prec, min(dist) == float('-inf')
