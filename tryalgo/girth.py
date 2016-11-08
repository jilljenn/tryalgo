#!/usr/bin/env python3

# cchristoph durr and finn völkel and louis abraham - 2016

# Find shortest simple cycle
# O(V*E)
# footnote (1) here you can add parity check of cycle_len if only even cycles are requested


from collections import deque
from sys import stdin

def readstr():    return stdin.readline().strip()
def readints():   return map(int, stdin.readline().split())
def readint():    return int(stdin.readline())


__all__ = ["shortest_cycle"]


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
    toVisit = deque([root])               # queue for BFS
    level[root] = 0                       
    tree[root] = root                     
    best_cycle = float('inf')             # start with infinity
    best_u = None
    best_v = None
    while toVisit:
        u = toVisit.popleft()           
        if level[u] > prune_level:
            break
        for v in graph[u]:
            if tree[u] == v:              # ignore the tree edge
                continue
            if level[v] == -1:            # new vertex - tree edge
                level[v] = level[u] + 1
                toVisit.append(v)
                tree[v] = u
            else:                         # vertex already seen - traversal edge
                has_cycle = True
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
    """ Finding a shortest cycle in an undirected graph
    
    :param graph: undirected graph in listlist or listdict format
    :returns: None or a list C describing the a shortest cycle with C[0]==C[-1]
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
    Pu = path(best_tree, best_u)
    Pv = path(best_tree, best_v)
    return Pu[::-1] + Pv              # combine path to make a cycle
    