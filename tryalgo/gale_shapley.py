#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Stable matching by Gale-Shapley
# jill-jenn vie et christoph durr - 2014-2018

from collections import deque


# snip{
def gale_shapley(men, women):
    """Stable matching by Gale-Shapley

    :param men: table of size n, men[i] is preference list of women for men i
    :param women: similar
    :returns: matching table, from women to men
    :complexity: :math:`O(n^2)`
    """
    n = len(men)
    assert n == len(women)
    current_suitor = [0] * n
    spouse = [None] * n
    rang = [[0] * n for j in range(n)]  # build rank
    for j in range(n):
        for r in range(n):
            rang[j][women[j][r]] = r
    singles = deque(range(n))  # all men are single and get in the queue
    while singles:
        i = singles.popleft()
        j = men[i][current_suitor[i]]
        current_suitor[i] += 1
        if spouse[j] is None:
            spouse[j] = i
        elif rang[j][spouse[j]] < rang[j][i]:
            singles.append(i)
        else:
            singles.put(spouse[j])  # sorry for spouse[j]
            spouse[j] = i
    return spouse
# snip}
