#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Minimum interval cover
# jill-jênn vie et christoph dürr - 2014-2018

from sys import stdin
from math import sqrt


def _readarray(f): return map(f, stdin.readline().split())


def _solve(iles, rayon):
    I = []
    for x, y in iles:
        if y > rayon:
            return -1               # island is too far
        z = sqrt(rayon * rayon - y * y)   # find the interval
        I.append((x + z, x - z))
    I.sort()                        # sort by right side
    sol = 0
    last = float('-inf')
    for right, left in I:
        if last < left:             # uncovered interval
            sol += 1
            last = right            # put an antenna
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
        n, rayon = _readarray(int)   # n=#islands, d=radius
        if n == 0:
            break            # end of instances
        iles = []
        for _ in range(n):
            x, y = _readarray(int)
            iles.append((x, y))
        stdin.readline()          # consume empty line
        print("Case %i: %i" % (testCase, _solve(iles, rayon)))
        testCase += 1
