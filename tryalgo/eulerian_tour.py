#!/usr/bin/env python3
# Eulierian cycle
# jill-jenn vie et christoph durr - 2015

import random
from collections import deque
from tryalgo.graph import write_graph


# snip{ eulerian_tour_undirected
def eulerian_tour_undirected(graph):
    """Eulerian tour on an undirected graph

       :param graph: directed graph in listlist format, cannot be listdict
       :assumes: graph is eulerian
       :returns: eulerian cycle as a vertex list
       :complexity: `O(|V|+|E|)`
    """
    P = []
    Q = [0]
    R = []
    next = [0] * len(graph)
    seen = [set() for _ in graph]
    while Q:
        node = Q.pop()
        P.append(node)
        while next[node] < len(graph[node]):
            neighbor = graph[node][next[node]]
            next[node] += 1
            if neighbor not in seen[node]:
                seen[neighbor].add(node)
                R.append(neighbor)
                node = neighbor
        while R:
            Q.append(R.pop())
    return P
# snip}


# snip{ eulerian_tour_directed
def eulerian_tour_directed(graph):
    """Eulerian tour on a directed graph

       :param graph: directed graph in listlist format, cannot be listdict
       :assumes: graph is eulerian
       :returns: eulerian cycle as a vertex list
       :complexity: `O(|V|+|E|)`
    """
    P = []
    Q = [0]
    R = []
    next = [0] * len(graph)
    while Q:
        node = Q.pop()
        P.append(node)
        while next[node] < len(graph[node]):
            neighbor = graph[node][next[node]]
            next[node] += 1
            R.append(neighbor)
            node = neighbor
        while R:
            Q.append(R.pop())
    return P
# snip}


def write_cycle(filename, graph, cycle, directed):
    n = len(graph)
    weight = [[float('inf')] * n for _ in range(n)]
    for r in range(1, len(c)):
        weight[c[r-1]][c[r]] = r
        if not directed:
            weight[c[r]][c[r-1]] = r
    write_graph(filename, graph, arc_label=weight, directed=directed)


def random_eulerien_graph(n):
    graphe = [[] for _ in range(n)]
    for v in range(n - 1):
        noeuds = random.sample(range(v + 1, n), random.choice(
          range(0 if len(graphe[v]) % 2 == 0 else 1, (n - v), 2)))
        graphe[v].extend(noeuds)
        for w in graphe[v]:
            if w > v:
                graphe[w].append(v)
    return graphe


def is_eulerian_tour(graph, tour):
    m = len(tour)-1
    arcs = set((tour[i], tour[i+1]) for i in range(m))
    if len(arcs) != m:
        return False
    for (u,v) in arcs:
        if v not in graph[u]:
            return False
    return True

