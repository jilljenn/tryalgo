#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Decompose DAG into a minimum number of chains
# jill-jenn vie et christoph durr - 2015

from tryalgo.bipartite_matching import max_bipartite_matching


# snip{
def dilworth(graph):
    """Decompose a DAG into a minimum number of chains by Dilworth

    :param graph: directed graph in listlist or listdict format
    :assumes: graph is acyclic
    :returns: table giving for each vertex the number of its chains
    :complexity: same as matching
    """
    n = len(graph)
    match = max_bipartite_matching(graph)  # couplage maximum
    part = [None] * n                      # partition en chaînes
    nb_chains = 0
    for v in range(n - 1, -1, -1):         # dans l'ordre topologique inverse
        if part[v] is None:                # début d'une chaîne
            u = v
            while u is not None:           # suivre la chaîne
                part[u] = nb_chains        # marquer
                u = match[u]
            nb_chains += 1
    return part
# snip}

