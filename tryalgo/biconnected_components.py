#!/usr/bin/env python3
# bi-connected components, cut vertices and cut cut-nodes
# jill-jenn vie et christoph durr - 2015


# snip{
# pour faciliter la lecture les variables sont sans préfixe dfs_
def cut_nodes_edges(graph):
    """Bi-connected components

    :param graph: adjacency list of an undirected graph. Cannot be adjacency dictionnary.
    :returns: a tuple with the list of cut-nodes and the list of cut-edges
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    time = 0
    num = [None] * n
    low = [n] * n
    father = [None] * n        # father[v] = père de v, None si racine
    critical_childs = [0] * n  # c_childs[u] = nb fils v tq low[v] >= num[u]
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:               # initier parcours DFS
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]
                if times_seen[node] == 0:         # début traitement
                    num[node] = time
                    time += 1
                    low[node] = float('inf')
                children = graph[node]
                if times_seen[node] == len(children):  # fin traitement
                    to_visit.pop()
                    up = father[node]             # propager low au père
                    if up is not None:
                        low[up] = min(low[up], low[node])
                        if low[node] >= num[up]:
                            critical_childs[up] += 1
                else:
                    child = children[times_seen[node]]   # prochain arc
                    times_seen[node] += 1
                    if times_seen[child] == -1:   # pas encore visité
                        father[child] = node      # arc de liaison
                        times_seen[child] = 0
                        to_visit.append(child)    # (dessous) arc retour
                    elif num[child] < num[node] and father[node] != child:
                        low[node] = min(low[node], num[child])
    cut_edges = []
    cut_nodes = []                                # extraire solution
    for node in range(n):
        if father[node] == None:                  # caractérisations
            if critical_childs[node] >= 2:
                cut_nodes.append(node)
        else:                                     # nœuds internes
            if critical_childs[node] >= 1:
                cut_nodes.append(node)
            if low[node] >= num[node]:
                cut_edges.append((father[node], node))
    return cut_nodes, cut_edges
# snip}

