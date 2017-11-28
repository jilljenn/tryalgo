#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum profit bipartite matching by Kuhn-Munkres
# jill-jenn vie, christoph durr and samuel tardieu - 2014-2017

"""
primal LP

    max sum_{u,v} w[u,v] * x[u,v]

    such that
    for all u in U: sum_v x[u,v] == 1   (l[u])

    for all v in V: sum_u x[u,v] <= 1   (l[v])

    for all u,v: x[u,v] >= 0


dual LP

    min sum_u l[u] + sum_v l[v]

    such that
    for all u,v:  l[u] + l[v] >= w[u,v]   (*)

    for all u in U: l[u] is arbitrary (free variable)
    for all v in V: l[v] >= 0


primal-dual algorithm:

    Start with trivial solution l for dual and with trivial
    non-solution x for primal.

    Iteratively improve primal or dual solution, maintaining complementary
    slackness conditions.

"""


# snip{
def kuhn_munkres(G, TOLERANCE=1e-6):
    """Maximum profit bipartite matching by Kuhn-Munkres

    :param G: weight matrix where G[u][v] is the weight of edge (u,v),
    :param TOLERANCE: a value with absolute value below tolerance
                      is considered as being zero.
                      If G consists of integer or fractional values
                      then TOLERANCE can be chosen 0.
    :requires: graph (U,V,E) is complete bi-partite graph with |U| <= |V|.
               float('-inf') or float('inf') entries in G
               are allowed but not None.
    :returns: matching table from U to V, value of matching
    :complexity: :math:`O(|U|^2 |V|)`
    """
    nU = len(G)
    U = range(nU)
    nV = len(G[0])
    V = range(nV)
    assert nU <= nV
    mu = [None] * nU                # couplage vide
    mv = [None] * nV
    lu = [max(row) for row in G]    # étiqu. triviaux
    lv = [0] * nV
    for root in U:                  # constr. un arbre alterné
        au = [False] * nU           # au, av marquent les sommets ...
        au[root] = True             # ... couverts par l'arbre
        Av = [None] * nV            # Av[v] descendant du sommet v dans l'arbre
        # pour chaque sommet u, marge[u] := (val, v) tel que
        # val est la plus petite marge sur les contraintes (*)
        # avec u fixé et v le sommet correspondant
        marge = [(lu[root] + lv[v] - G[root][v], root) for v in V]
        while True:
            ((delta, u), v) = min((marge[v], v) for v in V if Av[v] is None)
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
