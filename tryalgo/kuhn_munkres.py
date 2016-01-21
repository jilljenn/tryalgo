#!/usr/bin/env python3
# Maximum profit bipartite matching by Kuhn-Munkres
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def kuhn_munkres(G):      # couplage parfait de profit maximal en O(n^3)
    """Maximum profit bipartite matching by Kuhn-Munkres

    :param G: weight matrix G[u][v] is weight of edge (u,v)
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
            if delta > 0:           # arbre est complet
                for u0 in U:        # améliorer les étiquettes
                    if au[u0]:
                        lu[u0] -= delta
                for v0 in V:
                    if Av[v0] is not None:
                        lv[v0] += delta
                    else:
                        (val, arg) = marge[v0]
                        marge[v0] = (val - delta, arg)
            assert lu[u] + lv[v] == G[u][v]
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

if __name__ == "__main__":
    assert kuhn_munkres([[1]])[0] == [0]
    assert kuhn_munkres([[1, 1], [1, 1]])[0] == [1, 0]
    assert kuhn_munkres([[1, 2], [1, 1]])[0] == [1, 0]
    assert kuhn_munkres([[1, 1], [2, 1]])[0] == [1, 0]
    assert kuhn_munkres([[2, 1], [1, 1]])[0] == [0, 1]
    assert kuhn_munkres([[1, 1], [1, 2]])[0] == [0, 1]
    assert kuhn_munkres([[-1, -2, -3], [-6, -5, -4],
                         [-1, -1, -1]])[0] == [0, 2, 1]
    assert kuhn_munkres([[1, 2, 3], [6, 5, 4], [1, 1, 1]])[0] == [2, 0, 1]
    assert kuhn_munkres([[7,   53, 183, 439, 863],
                        [497, 383, 563,  79, 973],
                        [287,  63, 343, 169, 583],
                        [627, 343, 773, 959, 943],
                        [767, 473, 103, 699, 303]])[1] == 3315
    assert kuhn_munkres([[7,  53, 183, 439, 863, 497, 383, 563,
                          79, 973, 287,  63, 343, 169, 583],
                        [627, 343, 773, 959, 943, 767, 473, 103,
                         699, 303, 957, 703, 583, 639, 913],
                        [447, 283, 463,  29,  23, 487, 463, 993,
                         119, 883, 327, 493, 423, 159, 743],
                        [217, 623,   3, 399, 853, 407, 103, 983,
                         89, 463, 290, 516, 212, 462, 350],
                        [960, 376, 682, 962, 300, 780, 486,
                         502, 912, 800, 250, 346, 172, 812, 350],
                        [870, 456, 192, 162, 593, 473, 915,  45,
                         989, 873, 823, 965, 425, 329, 803],
                        [973, 965, 905, 919, 133, 673, 665, 235,
                         509, 613, 673, 815, 165, 992, 326],
                        [322, 148, 972, 962, 286, 255, 941, 541,
                         265, 323, 925, 281, 601,  95, 973],
                        [445, 721,  11, 525, 473,  65, 511, 164,
                         138, 672,  18, 428, 154, 448, 848],
                        [414, 456, 310, 312, 798, 104, 566, 520,
                         302, 248, 694, 976, 430, 392, 198],
                        [184, 829, 373, 181, 631, 101, 969, 613,
                         840, 740, 778, 458, 284, 760, 390],
                        [821, 461, 843, 513,  17, 901, 711, 993,
                         293, 157, 274,  94, 192, 156, 574],
                        [34, 124,   4, 878, 450, 476, 712, 914,
                         838, 669, 875, 299, 823, 329, 699],
                        [815, 559, 813, 459, 522, 788, 168, 586,
                         966, 232, 308, 833, 251, 631, 107],
                        [813, 883, 451, 509, 615,  77, 281, 613,
                         459, 205, 380, 274, 302,  35, 805]])[1] == 13938
    n = 1000  # attention ce code est en O(n^3), alors allez-y mollo avec n
    G = [[(11 * i + 101 * j) % 1001 for j in range(n)] for i in range(n)]
    print(kuhn_munkres(G))
