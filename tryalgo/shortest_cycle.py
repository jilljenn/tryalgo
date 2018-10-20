#!/usr/bin/env python3

# christoph durr and finn voelkel and louis abraham - 2016-2018

# Find shortest simple cycle
# O(V*E)
# footnote (1) here you can add parity check of cycle_len if only even cycles are requested


from collections import deque
from sys import stdin
from . floyd_warshall import floyd_warshall

def readstr():    return stdin.readline().strip()
def readints():   return map(int, stdin.readline().split())
def readint():    return int(stdin.readline())


__all__ = ["shortest_cycle", "powergraph"]


def bfs(graph, root, prune_level):
    """make a pruned BFS search of the graph starting at root.
    returns the BFS tree, and possibly a traversal edge (u,v) that with the tree
    forms a cycle of some length.

    :param graph: undirected graph in listlist or listdict format
    :param root:  vertex where BFS exploration starts
    :param prune_level: exploration is done only up to the prune_level (included)
    :complexity: O(V + E)
    """
    n = len(graph)
    level = [-1] * n                      # -1 == not seen
    tree = [None] * n                     # pointers to predecessors
    to_visit = deque([root])               # queue for BFS
    level[root] = 0
    tree[root] = root
    best_cycle = float('inf')             # start with infinity
    best_u = None
    best_v = None
    while to_visit:
        u = to_visit.popleft()
        if level[u] > prune_level:
            break
        for v in graph[u]:
            if tree[u] == v:              # ignore the tree edge
                continue
            if level[v] == -1:            # new vertex - tree edge
                level[v] = level[u] + 1
                to_visit.append(v)
                tree[v] = u
            else:                         # vertex already seen - traversal edge
                prune_level = level[v] - 1
                cycle_len = level[u] + 1 + level[v]
                if cycle_len < best_cycle:  # footnote (1)
                    best_cycle = cycle_len
                    best_u = u
                    best_v = v
    return tree, best_cycle, best_u, best_v


def path(tree, v):
    """returns the path in the tree from v to the root
    Complexity: O(V)
    """
    P = []
    while not P or P[-1] != v:
        P.append(v)
        v = tree[v]
    return P


def shortest_cycle(graph):
    """ Finding a shortest cycle in an undirected unweighted graph

    :param graph: undirected graph in listlist or listdict format
    :returns: None or a list C describing a shortest cycle
    :complexity: `O(|V|*|E|)`
    """
    best_cycle = float('inf')
    best_u = None
    best_v = None
    best_tree = None
    V = list(range(len(graph)))
    for root in V:
        tree, cycle_len, u, v = bfs(graph, root, best_cycle // 2)
        if cycle_len < best_cycle:
            best_cycle = cycle_len
            best_u = u
            best_v = v
            best_tree = tree
    if best_cycle == float('inf'):
        return None                   # no cycle found
    Pu = path(best_tree, best_u)      # combine path to make a cycle
    Pv = path(best_tree, best_v)
    cycle = Pu[::-1] + Pv   # last vertex equals first vertex
    return cycle[1:]        # remove duplicate vertex


def powergraph(graph, k):
    """Compute the k-th `powergraph <https://en.wikipedia.org/wiki/Graph_power>`_
       which has an edge u,v for every vertex pair
       of distance at most k in the given graph.

    :param graph: undirected graph in listlist or listdict format
    :param k: non-negative integer.
    :complexity: O(V^3)
    """
    V = range(len(graph))
    # create weight matrix for paths of length 1
    M = [[float('inf') for v in V] for u in V]
    for u in V:
        for v in graph[u]:
            M[u][v] = M[v][u] = 1
        M[u][u] = 0
    floyd_warshall(M)
    return [[v for v in V if M[u][v] <= k] for u in V]
