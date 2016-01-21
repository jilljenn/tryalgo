#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# jill-jenn vie et christoph durr - 2014

__all__ = ["kuhn_munkres"]


# snip{
def improve_matching(G, u, mu, mv, au, av, lu, lv):
    assert not au[u]
    au[u] = True
    for v in range(len(G)):
        if not av[v] and G[u][v] == lu[u] + lv[v]:
            av[v] = True
            if mv[v] is None or \
               improve_matching(G, mv[v], mu, mv, au, av, lu, lv):
                mv[v] = u
                mu[u] = v
                return True
    return False


def improve_labels(G, au, av, lu, lv):
    U = V = range(len(G))
    delta = min(min(lu[u] + lv[v] - G[u][v]
                for v in V if not av[v]) for u in U if au[u])
    for u in U:
        if (au[u]):
            lu[u] -= delta
    for v in V:
        if (av[v]):
            lv[v] += delta


def kuhn_munkres(G):      # couplage parfait de profit maximal en O(n^4)
    """Maximal profit perfect matching

    for minimum cost perfect matching just inverse the weights

    :param G: squared weight matrix of a complete bipartite graph
    :complexity: :math:`O(n^4)`
    """
    assert len(G) == len(G[0])
    n = len(G)
    mu = [None] * n                 # couplage vide
    mv = [None] * n
    lu = [max(row) for row in G]    # étiqu. triviaux
    lv = [0] * n
    for u0 in range(n):
        if mu[u0] is None:          # sommet libre
            while True:
                au = [False] * n    # arbre alternant vide
                av = [False] * n
                if improve_matching(G, u0, mu, mv, au, av, lu, lv):
                    break
                improve_labels(G, au, av, lu, lv)
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
                        [960, 376, 682, 962, 300, 780, 486, 502,
                         912, 800, 250, 346, 172, 812, 350],
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
    n = 50    # attention ce code est en O(n^4), alors allez-y mollo avec n
    G = [[(11 * i + 101 * j) % 1001 for j in range(n)] for i in range(n)]
    print(kuhn_munkres(G))
