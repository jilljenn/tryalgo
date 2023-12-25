#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Bipartie maximum matching

jill-jenn vie et christoph durr - 2014-2018
"""

__all__ = ["max_bipartite_matching", "max_bipartite_matching2"]


# snip{
def augment(u, bigraph, visit, match):
    """augment """
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph,
                                           visit, match):
                match[v] = u       # found an augmenting path
                return True
    return False


def max_bipartite_matching(bigraph):
    """Bipartie maximum matching

    :param bigraph: adjacency list, index = vertex in U,
                                    value = neighbor list in V
    :assumption: U = V = {0, 1, 2, ..., n - 1} for n = len(bigraph)
    :returns: matching list, match[v] == u iff (u, v) in matching
    :complexity: `O(|V|*|E|)`
    """
    n = len(bigraph)                # same domain for U and V
    match = [None] * n
    for u in range(n):
        if bigraph[u]:              # if u is not an isolated vertex
            augment(u, bigraph, [False] * n, match)
    return match
# snip}

def augment2(u, bigraph, visit, timestamp, match):
    """augment """
    for v in bigraph[u]:
        if visit[v] < timestamp:
            visit[v] = timestamp
            if match[v] is None or augment2(match[v], bigraph,
                                            visit, timestamp, match):
                match[v] = u       # found an augmenting path
                return True
    return False


def max_bipartite_matching2(bigraph):
    """Bipartie maximum matching

    :param bigraph: adjacency list, index = vertex in U,
                                    value = neighbor list in V
    :comment: U and V can have different cardinalities
    :returns: matching list, match[v] == u iff (u, v) in matching
    :complexity: `O(|V|*|E|)`
    """
    nU = len(bigraph)
    nV = max(max(adjlist, default=-1) for adjlist in bigraph) + 1
    match = [None] * nV
    visit = [-1] * nV
    for u in range(nU):
        augment2(u, bigraph, visit, u, match)
    return match
# snip}
