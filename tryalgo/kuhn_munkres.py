#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum profit bipartite matching by Kuhn-Munkres
# jill-jenn vie et christoph durr - 2014-2015


# snip{
TOLERANCE = 1e-6          # everything smaller is considered zero


def kuhn_munkres(G):      # couplage parfait de profit maximal en O(n^3)
    """Maximum profit bipartite matching by Kuhn-Munkres

    :param G: weight matrix G[u][v] is weight of edge (u,v),
    :requires: graph is complete bi-partite graph and both sides U, V have same size.
               Hence G is a squared matrix where  float('-inf') or float('inf')
               are allowed entries but not None.
    :returns: matching table from U to V, value of matching
    :complexity: :math:`O(|V|^3)`
    """
    assert len(G) == len(G[0])      # matrice carrée
    n = len(G)
    U = V = range(n)
    mu = [None] * n                 # couplage vide
    mv = [None] * n
    lu = [max(row) for row in G]    # étiqu. triviaux
    lv = [0] * n
    for root in U:                  # constr. un arbre alterné
        n = len(G)
        au = [False] * n
        au[root] = True
        Av = [None] * n
        marge = [(lu[root] + lv[v] - G[root][v], root) for v in V]
        while True:
            ((delta, u), v) = min((marge[v], v) for v in V if Av[v] == None)
            assert au[u]
            if delta > TOLERANCE:   # arbre est complet
                for u0 in U:        # améliorer les étiquettes
                    if au[u0]:
                        lu[u0] -= delta
                for v0 in V:
                    if Av[v0] is not None:
                        lv[v0] += delta
                    else:
                        (val, arg) = marge[v0]
                        marge[v0] = (val - delta, arg)
            assert abs(lu[u] + lv[v] - G[u][v]) <= TOLERANCE  # equality test
            Av[v] = u                # ajout (u, v) dans A
            if mv[v] is None:
                break                # chemin alt. trouvé...
            u1 = mv[v]
            assert not au[u1]
            au[u1] = True            # ajout (u1, v) dans A
            for v1 in V:
                if Av[v1] is None:   # mettre à jour les marges
                    alt = (lu[u1] + lv[v1] - G[u1][v1], u1)
                    if marge[v1] > alt:
                        marge[v1] = alt
        while v is not None:         # ...chemin alt. trouvé
            u = Av[v]                # le long du chemin vers la racine
            prec = mu[u]
            mv[v] = u                # augmenter le couplage
            mu[u] = v
            v = prec
    return (mu,  sum(lu) + sum(lv))
# snip}
