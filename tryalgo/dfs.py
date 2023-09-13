#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Depth-first search - DFS

jill-jênn vie et christoph durr - 2015-2019
"""

from typing import List, Optional
from . graph import Graph

# snip{ dfs-recursive
def dfs_recursive(graph: Graph, node: int, seen: List[bool]) -> None:
    """DFS, detect connected component, recursive implementation

    :param graph: directed graph in listlist or listdict format
    :param int node: to start graph exploration
    :param boolean-table seen: will be set true for the connected component
          containing node.
    :complexity: `O(|V|+|E|)`
    """
    seen[node] = True
    for neighbor in graph[node]:
        if not seen[neighbor]:
            dfs_recursive(graph, neighbor, seen)
# snip}


# snip{ dfs-iterative
def dfs_iterative(graph: Graph, start: int, seen: List[bool]) -> None:
    """DFS, detect connected component, iterative implementation

    :param graph: directed graph in listlist or listdict format
    :param int node: to start graph exploration
    :param boolean-table seen: will be set true for the connected component
          containing node.
    :complexity: `O(|V|+|E|)`
    """
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()   # exploring in top-down order of stack
        if not seen[node]:      # hence the use of reversed
            to_visit.extend(reversed(graph[node]))
            seen[node] = True   # vertex can be multiple times on stack
# snip}


# snip{ dfs-tree
def dfs_tree(graph: Graph, start: int=0) -> List[Optional[int]]:
    """DFS, build DFS tree in unweighted graph

       :param graph: directed graph in listlist or listdict format
       :param int start: source vertex
       :returns: precedence table
       :complexity: `O(|V|+|E|)`
       """
    to_visit = [start]
    prec: List[Optional[int]] = [None] * len(graph)
    while to_visit:              # an empty queue equals False
        node = to_visit.pop()
        for neighbor in graph[node]:
            if prec[neighbor] is None:
                prec[neighbor] = node
                to_visit.append(neighbor)
    return prec
# snip}


def dfs_grid_recursive(grid: List[List[str]], i: int, j: int, mark: str='X', free: str='.') -> None:
    """DFS on a grid, mark connected component, recursive version

    :param grid: matrix, 4-neighborhood
    :param i,j: cell in this matrix, start of DFS exploration
    :param free: symbol for walkable cells
    :param mark: symbol to overwrite visited vertices
    :complexity: linear
    """
    height = len(grid)
    width = len(grid[0])
    grid[i][j] = mark              # mark path
    for ni, nj in [(i + 1, j), (i, j + 1),
                   (i - 1, j), (i, j - 1)]:
        if 0 <= ni < height and 0 <= nj < width:
            if grid[ni][nj] == free:
                dfs_grid(grid, ni, nj)


# snip{ dfs-grid
def dfs_grid(grid, i, j, mark='X', free: str='.') -> None:
    """DFS on a grid, mark connected component, iterative version

    :param grid: matrix, 4-neighborhood
    :param i,j: cell in this matrix, start of DFS exploration
    :param free: symbol for walkable cells
    :param mark: symbol to overwrite visited vertices
    :complexity: linear
    """
    height = len(grid)
    width = len(grid[0])
    to_visit = [(i, j)]
    grid[i][j] = mark
    while to_visit:
        i1, j1 = to_visit.pop()
        for i2, j2 in [(i1 + 1, j1), (i1, j1 + 1),
                       (i1 - 1, j1), (i1, j1 - 1)]:
            if (0 <= i2 < height and 0 <= j2 < width and
                    grid[i2][j2] == free):
                grid[i2][j2] = mark  # mark path
                to_visit.append((i2, j2))
# snip}


# pylint: disable=too-many-nested-blocks, no-else-return
def find_cycle(graph: Graph) -> Optional[List[int]]:
    """find a cycle in an undirected graph

    :param graph: undirected graph in listlist or listdict format
    :returns: list of vertices in a cycle or None
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    prec: List[Optional[int]] = [None] * n  # ancestor marks for visited vertices
    for start in range(n):         # for each connected component
        if prec[start] is None:    # unvisited vertex
            S: List[int] = [start]            # start new DFS
            prec[start] = start       # mark root (not necessary for this algorithm)
            while S:
                u = S.pop()
                for v in graph[u]:  # for all neighbors
                    if v != prec[u]:  # except arcs to father in DFS tree
                        if prec[v] is not None: # v was already visited
                            cycle = [v, u]  # cycle found, (u,v) back edge
                            while u not in (prec[v], prec[u]):  # directed
                                assert u is not None
                                u = prec[u]  # climb up the tree
                                cycle.append(u)
                            return cycle
                        else:
                            prec[v] = u  # v is new vertex in tree
                            S.append(v)
    return None


def is_bipartite(G: Graph) -> bool:
    """ Checks whether a given graph is bipartite.
    
    This is done by a graph traversal, assigning alternating colors.
    Once an edge with identicial endpoint colors is detected
    we know graph is not bipartite.

    :param G: graph
    :returns: True if G is bipartite
    :complexity: linear
    """
    n = len(G)
    color = [0] * n     # 0=not visited, +1,-1=colors
    for u in range(n):  # for each connected component
        if color[u] == 0:
            Q = [u]     # initiate a graph traversal
            color[u] = 1
            while Q:    
                v = Q.pop()
                for w in G[v]:
                    if color[w] == color[v]:
                        return False    # odd cycle detected
                    if color[w] == 0:
                        color[w] = -color[v]    # opposite color
                        Q.append(w)
    return True
