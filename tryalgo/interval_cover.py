#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Minimum interval cover
# jill-jênn vie et christoph dürr - 2014-2015

from sys import stdin
from math import sqrt


def _readarray(f): return map(f, stdin.readline().split())


def _solve(iles, rayon):
    I = []
    for x, y in iles:
        if y > rayon:
            return -1               # île trop loin
        z = sqrt(rayon * rayon - y * y)   # déterminer l'intervalle
        I.append((x + z, x - z))
    I.sort()                        # trier par côté droit
    sol = 0
    last = float('-inf')
    for right, left in I:
        if last < left:             # intervalle pas couvert
            sol += 1
            last = right            # placer une antenne
    return sol


# snip{
def interval_cover(I):
    """Minimum interval cover

    :param I: list of closed intervals
    :returns: minimum list of points covering all intervals
    :complexity: O(n log n)
    """
    S = []
    for start, end in sorted(I, key=lambda v: (v[1], v[0])):
        if not S or S[-1] < start:
            S.append(end)
    return S
# snip}


if __name__ == "__main__":
    # http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1360
    testCase = 1
    while True:
        n, rayon = _readarray(int)   # n=nb îles, d=rayon
        if n == 0:
            break            # fin des instances
        iles = []
        for _ in range(n):
            x, y = _readarray(int)
            iles.append((x, y))
        stdin.readline()          # consommer ligne vide
        print("Case %i: %i" % (testCase, _solve(iles, rayon)))
        testCase += 1
