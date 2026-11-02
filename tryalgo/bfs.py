#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Breadth-first search (bfs)

christoph dürr - jill-jênn vie - 2015-2019, 2023
"""

# snip{
from collections import deque


def bfs(graph, start=0):
    """Shortest path in unweighted graph by BFS

       :param graph: directed graph in listlist or listdict format
       :param int start: source vertex
       :returns: distance table, precedence table
       :complexity: `O(|V|+|E|)`
       """
    to_visit = deque()
    dist = [float('inf')] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_visit.appendleft(start)
    while to_visit:              # an empty queue is considered False
        node = to_visit.pop()
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, prec
# snip}


def bfs_implicit(graph, start, end):
    """Shortest path by BFS in an implicitly directed graph

       :param graph: function mapping a given vertex to 
        an iterator over the neighboring vertices
       :param start: source vertex
       :param end: target vertex
       :returns: list of vertices of a shortest path or None
       :complexity: `O(|V|+|E|)`
       """
    to_visit = deque()
    prec = {start: None}    # predecessor on shortest path
    to_visit.appendleft(start)
    while to_visit:              
        node = to_visit.pop()
        for neighbor in graph(node):
            if neighbor not in prec:    # not yet discovered
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
                if end in prec:
                    # solution found
                    L = [end]       # backtrack the shortest path
                    while prec[L[-1]] is not None:
                        L.append(prec[L[-1]])
                    return L[::-1]  # return in start to end order
    return None
