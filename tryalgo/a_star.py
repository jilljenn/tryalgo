#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Shortest Path algorithm A*.

jill-jênn vie et christoph dürr - 2023
"""

from heapq import heappop, heappush


def a_star(graph, start, lower_bound):
    """single source shortest path by A* on an unweighted graph

       :param graph: iterator on adjacent vertices
       :param source: source vertex
       :param lower_bound: lb function on distance to target,
                must return 0 on target and only there.

       :returns: distance or -1 (target unreachable)
       :complexity: `O(|V| + |E|log|V|)`
    """
    closedset = set()
    openset   = set([start])
    g         = {start: 0 }
    Q         = [(lower_bound(start), start)]
    while Q:
        (val, x) = heappop(Q)
        if lower_bound(x) == 0:
            return g[x]
        closedset.add(x)
        for y in graph(x):
            if not y in closedset and not y in openset:
                g[y] = g[x] + 1
                val = g[y] + lower_bound(y)
                heappush(Q, (val, y))
                openset.add(y)
    return -1
