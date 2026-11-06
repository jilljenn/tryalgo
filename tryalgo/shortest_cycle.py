#!/usr/bin/env python3
"""\
Find shortest simple cycle

christoph durr, finn voelkel and louis abraham - 2016-2019

O(V*E)
footnote (1) here you can add parity check of cycle_len
if only even cycles are requested
"""
# pylint: disable=bad-whitespace, missing-docstring, multiple-statements

from collections import deque
from sys import stdin
from tryalgo.floyd_warshall import floyd_warshall


def readstr(): return stdin.readline().strip()


def readints(): return map(int, stdin.readline().split())


def readint(): return int(stdin.readline())


__all__ = ["shortest_cycle", "powergraph"]


# snip{ shortest_cycle
def shortest_cycle(graph):
    """Find a shortest cycle in an undirected unweighted graph.

    :param graph: undirected graph in listlist or listdict format
    :returns: None or a list of vertices describing a shortest cycle
    :complexity: O(|V| * (|V| + |E|))
    """
    n = len(graph)
    best = n + 1
    answer = None

    for root in range(n):
        dist = [-1] * n
        parent = [-1] * n
        dist[root] = 0
        queue = deque([root])

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and dist[u] + dist[v] + 1 < best:
                    best = dist[u] + dist[v] + 1
                    answer = (parent[:], u, v)

    if answer is None:
        return None

    # Reconstruct the cycle by removing the common tree path.
    parent, u, v = answer
    a, b = [], []
    while u != -1:
        a.append(u)
        u = parent[u]
    while v != -1:
        b.append(v)
        v = parent[v]
    while a and b and a[-1] == b[-1]:
        common = a.pop()
        b.pop()

    return a + [common] + b[::-1]
# snip}

def powergraph(graph, k):
    """Compute the k-th
       `powergraph <https://en.wikipedia.org/wiki/Graph_power>`_
       which has an edge u,v for every vertex pair
       of distance at most k in the given graph.

    :param graph: undirected graph in listlist or listdict format
    :param k: non-negative integer.
    :complexity: O(V^3)
    """
    V = range(len(graph))
    # create weight matrix for paths of length 1
    M = [[float('inf') for v in V] for u in V]
    for u in V:
        for v in graph[u]:
            M[u][v] = M[v][u] = 1
        M[u][u] = 0
    floyd_warshall(M)
    return [[v for v in V if M[u][v] <= k] for u in V]
