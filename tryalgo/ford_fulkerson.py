#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Maximum flow by Ford-Fulkerson

jill-jenn vie et christoph durr - 2014-2018
"""


from tryalgo.graph import add_reverse_arcs


# snip{
# pylint: disable=too-many-arguments
def _augment(graph, capacity, flow, val, u, target, visit, timestamp):
    """Find an augmenting path from u to target with value at most val"""
    visit[u] = timestamp
    if u == target:
        return val
    for v in graph[u]:
        cuv = capacity[u][v]
        if visit[v] < timestamp and cuv > flow[u][v]:  # reachable arc
            res = min(val, cuv - flow[u][v])
            delta = _augment(graph, capacity, flow, res, v, target, visit, timestamp)
            if delta > 0:
                flow[u][v] += delta            # augment flow
                flow[v][u] -= delta
                return delta
    return 0


def ford_fulkerson(graph, capacity, s, t):
    """Maximum flow by Ford-Fulkerson

    :param graph: directed graph in listlist or listdict format
    :param capacity: in matrix format or same listdict graph
    :param int s: source vertex
    :param int t: target vertex

    :returns: flow matrix, flow value
    :complexity: `O(|V|*|E|*max_capacity)`
    """
    add_reverse_arcs(graph, capacity)
    n = len(graph)
    flow = [[0] * n for _ in range(n)]
    INF = float('inf')
    visit = [-1] * n
    timestamp = 0
    while _augment(graph, capacity, flow, INF, s, t, visit, timestamp) > 0:
        timestamp += 1               
    return (flow, sum(flow[s]))      # flow network, amount of flow
# snip}
