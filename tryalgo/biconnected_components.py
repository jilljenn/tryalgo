#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bi-connected components, cut vertices and cut cut-nodes
# jill-jenn vie et christoph durr et louis abraham - 2015-2018
from sys import getrecursionlimit, setrecursionlimit


# snip{
# to ease readiness, variables do not have dfs_ prefix
def cut_nodes_edges(graph):
    """Bi-connected components

    :param graph: undirected graph. in listlist format. Cannot be in listdict format.
    :returns: a tuple with the list of cut-nodes and the list of cut-edges
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    time = 0
    num = [None] * n
    low = [n] * n
    father = [None] * n        # father[v] = None if root else father of v
    critical_childs = [0] * n  # c_c[u] = #childs v s.t. low[v] >= num[u]
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:               # init DFS path
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                if times_seen[node] == 0:         # start processing
                    num[node] = time
                    time += 1
                    low[node] = float('inf')
                children = graph[node]
                if times_seen[node] == len(children):  # end processing
                    to_visit.pop()
                    up = father[node]            # propagate low to father
                    if up is not None:
                        low[up] = min(low[up], low[node])
                        if low[node] >= num[up]:
                            critical_childs[up] += 1
                else:
                    child = children[times_seen[node]]   # next arrow
                    times_seen[node] += 1
                    if times_seen[child] == -1:   # not visited yet
                        father[child] = node      # link arrow
                        times_seen[child] = 0
                        to_visit.append(child)    # (below) back arrow
                    elif num[child] < num[node] and father[node] != child:
                        low[node] = min(low[node], num[child])
    cut_edges = []
    cut_nodes = []                                # extract solution
    for node in range(n):
        if father[node] == None:                  # characteristics
            if critical_childs[node] >= 2:
                cut_nodes.append(node)
        else:                                     # internal nodes
            if critical_childs[node] >= 1:
                cut_nodes.append(node)
            if low[node] >= num[node]:
                cut_edges.append((father[node], node))
    return cut_nodes, cut_edges
# snip}


def cut_nodes_edges2(graph):
    """Bi-connected components, alternative recursive implementation

    :param graph: undirected graph. in listlist format. Cannot be in listdict format.
    :assumes: graph has about 5000 vertices at most, otherwise memory limit is reached
    :returns: a tuple with the list of cut-nodes and the list of cut-edges
    :complexity: `O(|V|+|E|)` in average, `O(|V|+|E|^2)` in worst case due to use of dictionary
    """
    N = len(graph)
    assert N <= 5000
    recursionlimit = getrecursionlimit()
    setrecursionlimit(max(recursionlimit, N + 42))
    edges = set((i, j) for i in range(N) for j in graph[i] if i <= j)
    nodes = set()
    NOT = -2  # not visited yet; -1 would be buggy `marked[v] != prof - 1`
    FIN = -3  # already visited
    marked = [NOT] * N  # if >= 0, it means depth within the DFS

    def DFS(n, prof=0):
        """
        Recursively search graph, update edge list and returns the first
        node the first edge within search to which we can come back.
        """
        if marked[n] == FIN:
            return  # only when there are several connected components
        if marked[n] != NOT:
            return marked[n]
        marked[n] = prof
        m = float('inf')
        count = 0  # useful only for prof == 0
        for v in graph[n]:
            if marked[v] != FIN and marked[v] != prof - 1:
                count += 1
                r = DFS(v, prof+1)
                if r <= prof:
                    edges.discard(tuple(sorted((n, v))))
                if prof and r >= prof:  # only if we are not at root
                    nodes.add(n)
                m = min(m, r)
        # root is an articulation point iff it has more than 2 childs
        if prof == 0 and count >= 2:
            nodes.add(n)
        marked[n] = FIN
        return m
    for r in range(N):
        DFS(r)  # we can count connected components by nb += DFS(r)
    setrecursionlimit(recursionlimit)
    return nodes, edges
