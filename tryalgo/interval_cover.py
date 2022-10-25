#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Minimum interval cover

jill-jênn vie et christoph dürr - 2014-2020
"""

from sys import stdin
from math import sqrt
from tryalgo.our_std import readarray

# pylint: disable=redefined-outer-name


def _solve(iles, rayon):
    II = []
    for x, y in iles:
        if y > rayon:
            return -1               # island is too far
        z = sqrt(rayon * rayon - y * y)   # find the interval
        II.append((x + z, x - z))
    II.sort()                        # sort by right side
    sol = 0
    last = float('-inf')
    for right, left in II:
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
    # sort by right endpoints
    for start, end in sorted(I, key=lambda v: v[1]):
        if not S or S[-1] < start:
            S.append(end)
    return S
# snip}


if __name__ == "__main__":
    # http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1360
    testCase = 1
    while True:
        n, rayon = readarray(int)   # n=#islands, d=radius
        if n == 0:
            break            # end of instances
        iles = []
        for _ in range(n):
            x, y = readarray(int)
            iles.append((x, y))
        stdin.readline()          # consume empty line
        print("Case %i: %i" % (testCase, _solve(iles, rayon)))
        testCase += 1
