#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Eulerian cycle

jill-jênn vie et christoph dürr - 2015-2020
"""

import random
from tryalgo.graph import write_graph


# snip{ eulerian_tour_undirected
def eulerian_tour_undirected(graph):
    """Eulerian tour on an undirected graph

       :param graph: directed graph in listlist format, cannot be listdict
       :assumes: graph is eulerian
       :returns: eulerian cycle as a vertex list
       :complexity: `O(|V|+|E|)`
    """
    P = []                            # resulting tour
    Q = [0]                           # vertices to be explored, start at 0
    R = []                            # path from start node
    next_ = [0] * len(graph)          # initialize next_ to 0 for each node
    seen = [set() for _ in graph]     # mark backward arcs
    while Q:
        start = Q.pop()               # explore a cycle from start node
        node = start                            # current node on cycle
        while next_[node] < len(graph[node]):   # visit all allowable arcs
            neighbor = graph[node][next_[node]]  # traverse an arc
            next_[node] += 1                     # mark arc traversed
            if neighbor not in seen[node]:      # not yet traversed
                seen[neighbor].add(node)        # mark backward arc
                R.append(neighbor)              # append to path from start
                node = neighbor                 # move on
        while R:
            Q.append(R.pop())         # add to Q the discovered cycle R
        P.append(start)               # resulting path P is extended
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
    P = []                            # resulting tour
    Q = [0]                           # vertices to be explored, start at 0
    R = []                            # path from start node
    next_ = [0] * len(graph)          # initialize next_ to 0 for each node
    while Q:
        start = Q.pop()               # explore a cycle from start node
        node = start                            # current node on cycle
        while next_[node] < len(graph[node]):   # visit all allowable arcs
            neighbor = graph[node][next_[node]]  # traverse an arc
            next_[node] += 1                     # mark arc traversed
            R.append(neighbor)                  # append to path from start
            node = neighbor                     # move on
        while R:
            Q.append(R.pop())         # add to Q the discovered cycle R
        P.append(start)               # resulting path P is extended
    return P
# snip}


def write_cycle(filename, graph, cycle, directed):
    """Write an eulerian tour in DOT format

       :param filename: the file to be written in DOT format
       :param graph: graph in listlist format, cannot be listdict
       :param bool directed: describes the graph
       :param cycle: tour as a vertex list
       :returns: nothing
       :complexity: `O(|V|^2 + |E|)`
    """
    n = len(graph)
    weight = [[float('inf')] * n for _ in range(n)]
    for r in range(1, len(cycle)):
        weight[cycle[r-1]][cycle[r]] = r
        if not directed:
            weight[cycle[r]][cycle[r-1]] = r
    write_graph(filename, graph, arc_label=weight, directed=directed)


def random_eulerien_graph(n):
    """Generates some random eulerian graph

       :param int n: number of vertices
       :returns: undirected graph in listlist representation
       :complexity: linear
    """
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
    """Eulerian tour on an undirected graph

       :param graph: directed graph in listlist format, cannot be listdict
       :param tour: vertex list
       :returns: test if tour is eulerian
       :complexity: `O(|V|*|E|)` under the assumption that
       set membership is in constant time
    """
    m = len(tour)-1
    arcs = set((tour[i], tour[i+1]) for i in range(m))
    if len(arcs) != m:
        return False
    for (u, v) in arcs:
        if v not in graph[u]:
            return False
    return True
