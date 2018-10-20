#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Topological order
# jill-jenn vie et christoph durr - 2014-2018


# snip{ topological_order_dfs
def topological_order_dfs(graph):
    """Topological sorting by depth first search

    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of vertices in order
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    order = []
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                children = graph[node]
                if times_seen[node] == len(children):
                    to_visit.pop()
                    order.append(node)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:
                        times_seen[child] = 0
                        to_visit.append(child)
    return order[::-1]
# snip}


# snip{
def topological_order(graph):
    """Topological sorting by maintaining indegree

    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of vertices in order
    :complexity: `O(|V|+|E|)`
    """
    V = range(len(graph))
    indeg = [0 for _ in V]
    for node in V:            # compute indegree
        for neighbor in graph[node]:
            indeg[neighbor] += 1
    Q = [node for node in V if indeg[node] == 0]
    order = []
    while Q:
        node = Q.pop()        # node without incoming arrows
        order.append(node)
        for neighbor in graph[node]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                Q.append(neighbor)
    return order
# snip}
