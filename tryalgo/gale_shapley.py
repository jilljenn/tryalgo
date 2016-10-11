#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Stable matching by Gale-Shapley
# jill-jenn vie et christoph durr - 2014-2015

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
    suiv = [0] * n
    mari = [None] * n
    rang = [[0] * n for j in range(n)]                # construire rang
    for j in range(n):
        for r in range(n):
            rang[j][women[j][r]] = r
    celib = deque(range(n))              # tous les hommes sont célibataires
    while celib:              # tant qu'il y a des hommes à mettre en couple
        i = celib.popleft()
        j = men[i][suiv[i]]
        suiv[i] += 1
        if mari[j] is None:
            mari[j] = i
        elif rang[j][mari[j]] < rang[j][i]:
            celib.append(i)
        else:
            celib.put(mari[j])                       # désolé pour mari[j]
            mari[j] = i
    return mari
# snip}

