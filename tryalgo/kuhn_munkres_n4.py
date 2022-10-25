#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
kuhn_munkres_n4

jill-jênn vie et christoph dürr - 2014-2019
"""

__all__ = ["kuhn_munkres"]


# snip{
# pylint: disable=too-many-arguments
def improve_matching(G, u, mu, mv, au, av, lu, lv):
    """improve matching"""
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


# pylint: disable=bad-continuation, superfluous-parens
def improve_labels(G, au, av, lu, lv):
    """improve labels"""
    U = V = range(len(G))
    delta = min(min(lu[u] + lv[v] - G[u][v]
                for v in V if not av[v]) for u in U if au[u])
    for u in U:
        if (au[u]):
            lu[u] -= delta
    for v in V:
        if (av[v]):
            lv[v] += delta


def kuhn_munkres(G):      # maximum profit bipartite matching in O(n^4)
    """Maximum profit perfect matching

    for minimum cost perfect matching just inverse the weights

    :param G: squared weight matrix of a complete bipartite graph
    :complexity: :math:`O(n^4)`
    """
    assert len(G) == len(G[0])
    n = len(G)
    mu = [None] * n                 # Empty matching
    mv = [None] * n
    lu = [max(row) for row in G]    # Trivial labels
    lv = [0] * n
    for u0 in range(n):
        if mu[u0] is None:          # Free node
            while True:
                au = [False] * n    # Empty alternating tree
                av = [False] * n
                if improve_matching(G, u0, mu, mv, au, av, lu, lv):
                    break
                improve_labels(G, au, av, lu, lv)
    return (mu, sum(lu) + sum(lv))
# snip}
