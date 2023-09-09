#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Eulerian cycle

jill-jênn vie et christoph dürr - 2015-2023
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
        if len(graphe[v]) % 2 == 1:
            nb_min_neighbors = 1
        elif n - v == 2:
            nb_min_neighbors = 0
        else:
            nb_min_neighbors = 2
        noeuds = random.sample(range(v + 1, n), random.choice(
            range(nb_min_neighbors, (n - v), 2)))
        graphe[v].extend(noeuds)
        for w in graphe[v]:
            if w > v:
                graphe[w].append(v)
    return graphe


def is_eulerian_tour_directed(graph, tour):
    """Test if a given tour is Eulerian for a directed graph

    :param graph: directed graph in listlist format, cannot be listdict
    :param tour: vertex list 
    :returns: True if tour is eulerian
    :complexity: `O(|V|*|E|)` under the assumption that set membership is in constant time
    """
    m = len(tour) - 1                                   # nb of arcs in the tour
    arcs = set((tour[i], tour[i+1]) for i in range(m))  # all arcs in the tour
    required = sum(len(Gu) for Gu in graph)             # nb of arcs in graph
    if (m != len(arcs) or           # no arc is visited twice
        m != required):             # there are not more arcs in tour than in graph
        return False
    # implicitly check that every arc in tour exists in the graph
    for u, Gu in enumerate(graph):  # loop over all arcs in the graph
         for v in Gu:
            if (u, v) not in arcs:  # check tour visits every arc
                return False
    return True

def is_eulerian_tour_undirected(graph, tour):
    """Test if a given tour is Eulerian for an undirected graph

    :param graph: undirected graph in listlist format, cannot be listdict
    :param tour: vertex list 
    :returns: True if tour is eulerian
    :complexity: `O(|V|*|E|)` under the assumption that set membership is in constant time
    """
    def normalize(u, v):            # normalize so (3,13) or (13,3) are the same edge
        return (min(u, v), max(u, v))

    m = len(tour) - 1                                     # nb of edges in the tour
    arcs = set(normalize(tour[i], tour[i+1]) for i in range(m))  # all edges in tour
    if len(arcs) != m:          
        return False
    # check that tour contains only existing arcs (by counting)
    required = sum(len(Gu) for Gu in graph) // 2          # nb of edges in graph
    if (m != len(arcs) or               # no edge is visited twice
        m != required):                 # there are not more edges in tour than in graph
        return False
    # implicitly check that every arc in tour exists in the graph
    for u, Gu in enumerate(graph):      # loop over all edges in the graph
         for v in Gu:
            if normalize(u, v) not in arcs:    # check tour visits every edges
                return False
    return True
