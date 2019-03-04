#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test matrix product AB=C by Freivalds
# jill-jênn vie et christoph dürr - 2015-2018

# snip{
from random import randint
from sys import stdin

#snip}
__all__ = ["freivalds"]
#snip{


def readint():
    return int(stdin.readline())


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M


def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    """Tests matrix product AB=C by Freivalds

    :param A: n by n numerical matrix
    :param B: same
    :param C: same
    :returns: False with high probability if AB != C

    :complexity:
        :math:`O(n^2)`
    """
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(A, B, C))
# snip}
