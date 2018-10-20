#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Depth first search - DFS
# jill-jenn vie et christoph durr - 2015-2018


# snip{ dfs-recursive
def dfs_recursive(graph, node, seen):
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
def dfs_iterative(graph, start, seen):
    """DFS, detect connected component, iterative implementation

    :param graph: directed graph in listlist or listdict format
    :param int node: to start graph exploration
    :param boolean-table seen: will be set true for the connected component
          containing node.
    :complexity: `O(|V|+|E|)`
    """
    seen[start] = True
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()
        for neighbor in graph[node]:
            if not seen[neighbor]:
                seen[neighbor] = True
                to_visit.append(neighbor)
# snip}


# snip{ dfs-tree
def dfs_tree(graph, start=0):
    """DFS, build DFS tree in unweighted graph

       :param graph: directed graph in listlist or listdict format
       :param int start: source vertex
       :returns: precedence table
       :complexity: `O(|V|+|E|)`
       """
    to_visit = [start]
    prec = [None] * len(graph)
    while to_visit:              # an empty queue equals False
        node = to_visit.pop()
        for neighbor in graph[node]:
            if prec[neighbor] is None:
                prec[neighbor] = node
                to_visit.append(neighbor)
    return prec
# snip}


def dfs_grid_recursive(grid, i, j, mark='X', free='.'):
    """DFS on a grid, mark connected component, iterative version

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
def dfs_grid(grid, i, j, mark='X', free='.'):
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


def find_cycle(graph):
    """find a cycle in an undirected graph

    :param graph: undirected graph in listlist or listdict format
    :returns: list of vertices in a cycle or None
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    prec = [None] * n  # ancestor marks for visited vertices
    for u in range(n):
        if prec[u] is None:  # unvisited vertex
            S = [u]  # start new DFS
            prec[u] = u  # mark root (not necessary for this algorithm)
            while S:
                u = S.pop()
                for v in graph[u]:  # for all neighbors
                    if v != prec[u]:  # except arcs to father in DFS tree
                        if prec[v] is not None:
                            cycle = [v, u]  # cycle found, (u,v) back edge
                            while u != prec[v] and u != prec[u]:  # directed
                                u = prec[u]  # climb up the tree
                                cycle.append(u)
                            return cycle
                        else:
                            prec[v] = u  # v is new vertex in tree
                            S.append(v)
    return None
