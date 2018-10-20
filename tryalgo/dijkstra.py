#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Shortest paths by Dijkstra
# jill-jênn vie et christoph dürr - 2015-2018


# snip{
from heapq import heappop, heappush


def dijkstra(graph, weight, source=0, target=None):
    """single source shortest paths by Dijkstra

       :param graph: directed graph in listlist or listdict format
       :param weight: in matrix format or same listdict graph
       :assumes: weights are non-negative
       :param source: source vertex
       :type source: int
       :param target: if given, stops once distance to target found
       :type target: int

       :returns: distance table, precedence table
       :complexity: `O(|V| + |E|log|V|)`
    """
    n = len(graph)
    assert all(weight[u][v] >= 0 for u in range(n) for v in graph[u])
    prec = [None] * n
    black = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)       # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for neighbor in graph[node]:
                dist_neighbor = dist_node + weight[node][neighbor]
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec
# snip}


# snip{ dijkstra_update_heap
from tryalgo.our_heap import OurHeap

# snip}


# snip{ dijkstra_update_heap
def dijkstra_update_heap(graph, weight, source=0, target=None):
    """single source shortest paths by Dijkstra
       with a heap implementing item updates

       :param graph: adjacency list or adjacency dictionary of a directed graph
       :param weight: matrix or adjacency dictionary
       :assumes: weights are non-negatif and weights are infinite for non edges
       :param source: source vertex
       :type source: int
       :param target: if given, stops once distance to target found
       :type target: int
       :returns: distance table, precedence table
       :complexity: `O(|V| + |E|log|V|)`
    """
    n = len(graph)
    assert all(weight[u][v] >= 0 for u in range(n) for v in graph[u])
    prec = [None] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = OurHeap([(dist[node], node) for node in range(n)])
    while heap:
        dist_node, node = heap.pop()       # Closest node from source
        if node == target:
            break
        for neighbor in graph[node]:
            old = dist[neighbor]
            new = dist_node + weight[node][neighbor]
            if new < old:
                dist[neighbor] = new
                prec[neighbor] = node
                heap.update((old, neighbor), (new, neighbor))
    return dist, prec
# snip}
