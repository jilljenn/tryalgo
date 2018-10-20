#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Strongly connected components
# composantes fortement connexes
# jill-jênn vie et christoph dürr - 2015-2018

__all__ = ["tarjan_recursif", "tarjan", "kosaraju", "reverse"]


# snip{ sccp-tarjan-recursif
def tarjan_recursif(graph):
    """Strongly connected components by Tarjan, recursive implementation

    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of lists for each component
    :complexity: linear
    """
    global sccp, waiting, dfs_time, dfs_num
    sccp = []
    waiting = []
    waits = [False] * len(graph)
    dfs_time = 0
    dfs_num = [None] * len(graph)

    def dfs(node):
        global sccp, waiting, dfs_time, dfs_num
        waiting.append(node)           # new node is waiting
        waits[node] = True
        dfs_num[node] = dfs_time       # mark visit
        dfs_time += 1
        dfs_min = dfs_num[node]        # compute dfs_min
        for neighbor in graph[node]:
            if dfs_num[neighbor] is None:
                dfs_min = min(dfs_min, dfs(neighbor))
            elif waits[neighbor] and dfs_min > dfs_num[neighbor]:
                dfs_min = dfs_num[neighbor]
        if dfs_min == dfs_num[node]:   # representative of a component
            sccp.append([])            # make a component
            while True:                # add waiting nodes
                u = waiting.pop()
                waits[u] = False
                sccp[-1].append(u)
                if u == node:          # until representative
                    break
        return dfs_min

    for node in range(len(graph)):
        if dfs_num[node] is None:
            dfs(node)
    return sccp
# snip}


# snip{ sccp-tarjan
def tarjan(graph):
    """Strongly connected components by Tarjan, iterative implementation

    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of lists for each component
    :complexity: linear
    """
    n = len(graph)
    dfs_num = [None] * n
    dfs_min = [n] * n
    waiting = []
    waits = [False] * n  # invariant: waits[v] iff v in waiting
    sccp = []          # list of detected components
    dfs_time = 0
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:                    # initiate path
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]                    # top of stack
                if times_seen[node] == 0:              # start process
                    dfs_num[node] = dfs_time
                    dfs_min[node] = dfs_time
                    dfs_time += 1
                    waiting.append(node)
                    waits[node] = True
                children = graph[node]
                if times_seen[node] == len(children):  # end of process
                    to_visit.pop()                     # remove from stack
                    dfs_min[node] = dfs_num[node]      # compute dfs_min
                    for child in children:
                        if waits[child] and dfs_min[child] < dfs_min[node]:
                            dfs_min[node] = dfs_min[child]
                    if dfs_min[node] == dfs_num[node]:  # representative
                        component = []                 # make component
                        while True:                    # add nodes
                            u = waiting.pop()
                            waits[u] = False
                            component.append(u)
                            if u == node:              # until repr.
                                break
                        sccp.append(component)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:        # not visited yet
                        times_seen[child] = 0
                        to_visit.append(child)
    return sccp
# snip}


# snip{ sccp-kosaraju
def kosaraju_dfs(graph, nodes, order, sccp):
    times_seen = [-1] * len(graph)
    for start in nodes:
        if times_seen[start] == -1:                     # initiate DFS
            to_visit = [start]
            times_seen[start] = 0
            sccp.append([start])
            while to_visit:
                node = to_visit[-1]
                children = graph[node]
                if times_seen[node] == len(children):   # end of process
                    to_visit.pop()
                    order.append(node)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:         # new node
                        times_seen[child] = 0
                        to_visit.append(child)
                        sccp[-1].append(child)


def reverse(graph):
    """replace all arcs (u, v) by arcs (v, u) in a graph"""
    rev_graph = [[] for node in graph]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            rev_graph[neighbor].append(node)
    return rev_graph


def kosaraju(graph):
    """Strongly connected components by Kosaraju

    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of lists for each component
    :complexity: linear
    """
    n = len(graph)
    order = []
    sccp = []
    kosaraju_dfs(graph, range(n), order, [])
    kosaraju_dfs(reverse(graph), order[::-1], [], sccp)
    return sccp[::-1]  # follow inverse topological order
# snip}
