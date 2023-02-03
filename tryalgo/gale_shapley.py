#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Stable matching by Gale-Shapley

jill-jênn vie et christoph durr - 2014-2019
"""

# snip{
from collections import deque


# pylint: disable=no-member
def gale_shapley(men, women):
    """Stable matching by Gale-Shapley

    :param men: table of size n, men[i] is preference list of women for men i
    :param women: similar
    :returns: matching table, from women to men
    :complexity: :math:`O(n^2)`
    """
    n = len(men)
    assert n == len(women)
    current_suitor = [0] * n            # nb of matchings so far
    spouse = [None] * n                 # current matching
    rank = [[0] * n for j in range(n)]  # build rank
    for j in range(n):
        for r in range(n):
            rank[j][women[j][r]] = r
    singles = list(range(n))            # initially all men are single 
    while singles:
        i = singles.pop()
        j = men[i][current_suitor[i]]   # propose matching (i,j)
        current_suitor[i] += 1
        if spouse[j] is None:
            spouse[j] = i
        elif rank[j][spouse[j]] < rank[j][i]:
            singles.append(i)
        else:
            singles.append(spouse[j])  # sorry for spouse[j]
            spouse[j] = i
    return spouse
# snip}
